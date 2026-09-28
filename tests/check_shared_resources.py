"""Validate single-source role assets, callers and relocatable install layouts."""
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import re


def referenced_paths(path):
    """Actual Markdown links and inline relative file paths (including code spans)."""
    text = path.read_text(encoding="utf-8")
    links = re.findall(r"\]\(([^)\s]+)\)", text)
    inline = re.findall(r"`([^`\n]+\.md)`", text)
    for raw in links + inline:
        raw = raw.split("#", 1)[0]
        if not raw or raw.startswith(("http:", "https:", "mailto:", "file:")):
            continue
        if any(c in raw for c in "<>*{}") or " " in raw:
            continue
        if raw.startswith(("./", "../", "agents/", "personas/", "references/")):
            yield (path.parent / raw).resolve()


def validate(root):
    root = Path(root).resolve()
    problems = []
    try:
        registry = json.loads((root / "tests/shared-resources.json").read_text(encoding="utf-8"))
        shared = registry["shared"]
        local = registry["local_groups"]
    except (OSError, ValueError, KeyError) as exc:
        return [f"shared resource registry: {exc}"]
    sources = set()
    for name, entry in shared.items():
        source = root / entry["source"]
        sources.add(source.resolve())
        if source.name != name or not source.is_relative_to(root / "skills/conventions"):
            problems.append(f"{name}: source must be its named file under conventions")
        if not source.is_file():
            problems.append(f"missing shared source: {entry['source']}")
            continue
        if not entry["callers"]:
            problems.append(f"{name}: no registered caller")
        for rel in entry["callers"]:
            caller = root / rel
            if not caller.is_file():
                problems.append(f"missing caller: {rel}")
            elif source.resolve() not in set(referenced_paths(caller)):
                problems.append(f"{rel}: does not reference {entry['source']}")
    # Canonical role files cannot silently escape ownership registration.
    for path in (root / "skills/conventions/agents").glob("*.md"):
        if path.resolve() not in sources:
            problems.append(f"unregistered shared role: {path.relative_to(root)}")
    groups = defaultdict(list)
    hashes = defaultdict(list)
    for path in sorted((root / "skills").glob("nk-*/references/**/*.md")):
        rel = path.relative_to(root).as_posix()
        groups[path.name].append(rel)
        if path.name in shared:
            problems.append(f"local copy of shared source: {rel}")
        text = re.sub(r"<!--.*?-->", "", path.read_text(encoding="utf-8"), flags=re.S).strip()
        if len(text) > 200:
            hashes[hashlib.sha256(text.encode()).hexdigest()].append(rel)
    for path in sources:
        if path.is_file():
            text = re.sub(r"<!--.*?-->", "", path.read_text(encoding="utf-8"), flags=re.S).strip()
            if len(text) > 200:
                hashes[hashlib.sha256(text.encode()).hexdigest()].append(path.relative_to(root).as_posix())
    for paths in hashes.values():
        if len(paths) > 1:
            problems.append("identical reference bodies: " + ", ".join(paths))
    for name, paths in groups.items():
        if len(paths) > 1 and name not in local:
            problems.append(f"unclassified same-name references: {name}: {paths}")
    for name, entry in local.items():
        if not entry.get("reason", "").strip() or sorted(groups.get(name, [])) != sorted(entry["paths"]):
            problems.append(f"{name}: local workflow ownership or membership differs")
    for path in (root / "skills").rglob("*.md"):
        for target in referenced_paths(path):
            if not target.exists():
                problems.append(f"unresolved reference: {path.relative_to(root)} -> {target}")
    # These manifests distribute the whole skill tree; conventions must be discoverable too.
    for rel in [".codex-plugin/plugin.json", ".kimi-plugin/plugin.json"]:
        try:
            manifest = json.loads((root / rel).read_text(encoding="utf-8"))
            tree = (root / manifest["skills"]).resolve()
            if tree != root / "skills" or not (tree / "conventions/SKILL.md").is_file():
                problems.append(f"{rel}: distribution omits the shared conventions library")
        except (OSError, ValueError, KeyError, TypeError) as exc:
            problems.append(f"{rel}: invalid skills distribution path: {exc}")
    return problems
