#!/usr/bin/env python3
"""Check maintained docs and installable skills; legacy drafts are not runtime inputs."""
from pathlib import Path
import os
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
NK_BYTE_LIMIT = 8000  # nk-* 自写技能：Codex 客户端的 SKILL.md 读取上限（Codex 暂停期间保留约束）
VENDOR_BYTE_LIMIT = 25000  # vendored 上游技能：同步保真优先于体积（v0.4.0 政策，见 docs/plans/2026-10-29-v0.4.0-osmani-vendor-plan.md）


def skill_entries(root):
    return sorted((root / 'skills').rglob('SKILL.md'))


def maintained_docs(root):
    docs = list(root.glob('*.md'))
    docs += list((root / 'docs').glob('*.md'))
    docs += list((root / 'docs/adr').rglob('*.md'))
    for entry in skill_entries(root):
        docs += list(entry.parent.rglob('*.md'))
    return sorted(set(docs))


def strip_fences(text):
    text = re.sub(r'```.*?```', '', text, flags=re.S)
    text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
    return re.sub(r'`[^`\n]*`', '', text)


def link_problems(root):
    problems = []
    entries = skill_entries(root)
    for path in maintained_docs(root):
        owner = next((e.parent for e in entries if path.is_relative_to(e.parent)), None)
        text = strip_fences(path.read_text(encoding='utf-8'))
        for match in re.finditer(r'\]\(([^)\s#]+)(#[^)]*)?\)', text):
            link = match.group(1)
            if link.startswith(('http:', 'https:', 'file:', 'mailto:', '#')):
                continue
            if '<' in link or '*' in link:
                continue
            if owner and link.startswith(('docs/', 'CONCEPTS', 'AGENTS')):
                continue  # Paths in the user's project.
            target = (path.parent / link).resolve()
            if not target.exists():
                problems.append(f'{path.relative_to(root)} -> {link}')
            elif owner and not target.is_relative_to(owner):
                if target.is_relative_to((root / 'references').resolve()):
                    continue  # 仓库级共享 references/：整包分发，无单技能安装断链问题
                problems.append(f'{path.relative_to(root)}: use a public skill name instead of a cross-skill file: {link}')
    return problems


def reference_problems(root):
    problems = []
    # Planned slots are public names; only SKILL.md entries are installable.
    names = {p.parent.name for p in skill_entries(root)}
    names |= {p.parent.name for p in (root / 'skills').rglob('.gitkeep')}
    # Slash commands share the nk- prefix but are not skills.
    names |= {p.stem for p in (root / '.claude/commands').glob('*.md')}
    for entry in skill_entries(root):
        for path in entry.parent.rglob('*.md'):
            text = path.read_text(encoding='utf-8')
            for name in set(re.findall(r'\bnk-[a-z][a-z0-9-]*\b', text)) - names - {'nk-section'}:
                problems.append(f'{path.relative_to(root)}: unknown skill {name}')
            if 'conventions/' in text or 'SKILL.legacy.md' in text:
                problems.append(f'{path.relative_to(root)}: runtime dependency on retired conventions or legacy drafts')
    return problems


def byte_problems(root):
    problems = []
    for p in skill_entries(root):
        limit = NK_BYTE_LIMIT if p.parent.name.startswith('nk-') else VENDOR_BYTE_LIMIT
        if p.stat().st_size > limit:
            problems.append(f'{p.relative_to(root)} exceeds {limit} bytes')
    return problems


def main():
    from check_manifests import validate
    from check_frontmatter import validate_frontmatter
    from check_artifacts import validate as validate_artifacts
    entries = skill_entries(ROOT)
    ref = os.environ.get('GITHUB_REF', '')
    tag = ref.removeprefix('refs/tags/') if ref.startswith('refs/tags/') else None
    checks = {
        'link-integrity': link_problems(ROOT),
        'references': reference_problems(ROOT),
        'byte-budget': byte_problems(ROOT),
        'distribution': validate(ROOT, tag),
        'artifact-paths': validate_artifacts(ROOT),
        'frontmatter': [f'{p.relative_to(ROOT)}: {error}' for p in entries
                        for error in validate_frontmatter(p.read_text(encoding='utf-8'), p.parent.name)],
    }
    for name, problems in checks.items():
        print(f"{'FAIL' if problems else 'OK  '} {name}")
        for problem in problems:
            print(f'  - {problem}')
    if any(checks.values()):
        return 1
    print('\nall checks passed')
    return 0


if __name__ == '__main__':
    sys.exit(main())
