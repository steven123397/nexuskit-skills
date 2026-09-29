#!/usr/bin/env python3
"""NexusKit mechanical checks. Run from repo root: python tests/run_checks.py

Five checks, each maps to a class of failure that actually happened:
1. link-integrity   - relative markdown links must resolve
2. references       - nk-* mentions resolve to real skills; no dangling K/R code refs
3. byte-budget      - SKILL.md <= 8000 bytes (Codex injection limit), ratchet list
4. shared-resources - canonical methods, caller references, local workflow ownership
                      controlled planning guardrail copies, distribution and manifest inventories
5. frontmatter      - safe YAML parsing with duplicate-key rejection, English description,
                      boolean invocation policy, name and
                      description, and name matches its directory (installers such
                      as the skills CLI derive the install dir from frontmatter name)
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SKILL_REF_DENYLIST = {"nk-section"}  # semantic marker, not a skill
BYTE_LIMIT = 8000
OVER_BUDGET: set = set()  # ratchet: may only shrink; a listed file under budget fails the check

failures = []


def check(name, problems):
    if problems:
        failures.append((name, problems))
        print(f"FAIL {name}: {len(problems)} problem(s)")
        for p in problems[:20]:
            print(f"  - {p}")
    else:
        print(f"OK   {name}")


def md_files():
    return [
        f.replace(os.sep, "/")
        for f in glob.glob("**/*.md", recursive=True)
        if not f.startswith(".git")
    ]


def strip_fences(text):
    # fenced blocks, then HTML comments (meta), then inline code (examples/templates)
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)


# --- 1. link integrity ---
def check_links():
    problems = []
    for f in md_files():
        base = os.path.dirname(f)
        in_skill = f.startswith("skills/nk-")
        text = strip_fences(open(f, encoding="utf-8").read())
        for m in re.finditer(r"\]\(([^)\s#]+)(#[^)]*)?\)", text):
            link = m.group(1)
            if link.startswith(("http", "file:", "mailto:", "#")):
                continue
            if "<" in link or "*" in link:  # template placeholder or glob
                continue
            if in_skill and link.startswith(("docs/", "CONCEPTS", "AGENTS")):
                continue  # target-repo paths, not repo-internal
            if not os.path.exists(os.path.normpath(os.path.join(base, link))):
                problems.append(f"{f} -> {link}")
    check("link-integrity", problems)


# --- 2. reference resolution ---
def check_references():
    problems = []
    skill_dirs = {os.path.basename(d) for d in glob.glob("skills/nk-*") if os.path.isdir(d)}
    for f in md_files():
        if not (f.startswith("skills/nk-") or f.startswith("skills/conventions")):
            continue
        text = strip_fences(open(f, encoding="utf-8").read())
        for m in re.finditer(r"[（(]K[0-9]+[）)]", text):
            problems.append(f"{f}: dangling K-code label {m.group(0)} (contracts live in conventions/)")
        for m in re.finditer(r"\bR[0-9]+\.[0-9]+\b", text):
            problems.append(f"{f}: decimal cadence ref {m.group(0)} does not exist (use e.g. 'R4 第 4 条')")
        if f.startswith("skills/nk-"):
            for m in re.finditer(r"\b(nk-[a-z][a-z0-9-]*)\b", text):
                name = m.group(1)
                if name in SKILL_REF_DENYLIST:
                    continue
                if name not in skill_dirs:
                    problems.append(f"{f}: references skill `{name}` but no {name}/ directory exists")
    check("references", problems)


# --- 3. byte budget ---
def check_byte_budget():
    problems = []
    over_now = set()
    for f in glob.glob("skills/nk-*/SKILL.md"):
        size = os.path.getsize(f)
        if size > BYTE_LIMIT:
            over_now.add(f)
            if f not in OVER_BUDGET:
                problems.append(f"{f}: {size} bytes exceeds {BYTE_LIMIT} (Codex injection limit)")
    for f in OVER_BUDGET - over_now:
        problems.append(f"{f}: now under budget - remove it from OVER_BUDGET (ratchet only shrinks)")
    check("byte-budget", problems)


# --- 4. shared method ownership ---
def work_fragment_problems():
    source = os.path.join(ROOT, "skills", "conventions", "work-guardrails.md")
    target = os.path.join(ROOT, "skills", "nk-work", "SKILL.md")
    problems = []
    source_text = open(source, encoding="utf-8").read()
    target_text = open(target, encoding="utf-8").read()
    names = re.findall(r"<!-- fragment: ([^ ]+) -->\n(.*?)\n<!-- /fragment -->", source_text, flags=re.S)
    for name, body in names:
        marker = f"<!-- fragment: {name} -->\n{body}\n<!-- /fragment -->"
        if marker not in target_text:
            problems.append(f"nk-work: fragment {name} is missing or differs from conventions/work-guardrails.md")
    return problems


def check_shared_resources():
    from check_shared_resources import validate
    from check_manifests import validate as validate_manifests
    ref = os.environ.get("GITHUB_REF", "")
    release_tag = ref.removeprefix("refs/tags/") if ref.startswith("refs/tags/") else None
    check("shared-resources", validate(ROOT) + work_fragment_problems() + validate_manifests(ROOT, release_tag))


# --- 5. frontmatter ---
def check_frontmatter():
    problems = []
    try:
        from check_frontmatter import validate_frontmatter
    except ModuleNotFoundError as exc:
        if exc.name != "yaml":
            raise
        check("frontmatter", ["PyYAML is required; run python -m pip install -r tests/requirements.txt"])
        return
    for f in sorted(glob.glob("skills/*/SKILL.md")):
        f = f.replace(os.sep, "/")
        with open(f, encoding="utf-8") as stream:
            text = stream.read()
        problems.extend(f"{f}: {problem}" for problem in validate_frontmatter(text, f.split("/")[1]))
    check("frontmatter", problems)


if __name__ == "__main__":
    check_links()
    check_references()
    check_byte_budget()
    check_shared_resources()
    check_frontmatter()
    if failures:
        print(f"\n{sum(len(p) for _, p in failures)} problem(s) in {len(failures)} check(s)")
        sys.exit(1)
    print("\nall checks passed")
