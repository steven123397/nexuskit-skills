"""Check spec/plan/todo artifact paths stay consistent across the pipeline."""
from pathlib import Path
import re

# Canonical artifact paths shared by /nk-spec, /nk-plan, /nk-build and the
# skills they invoke. Module specs are named by id, so they are matched as a
# pattern rather than a fixed filename. To change the convention, update this
# list and every guarded file in the same change.
ARTIFACT_ALLOWLIST = (
    r'SPEC\.md',
    r'docs/SPEC\.md',
    r'spec/SPEC-(?:<id>|[A-Za-z0-9_-]+)\.md',
    r'spec/capability-map\.md',
    r'tasks/plan\.md',
    r'tasks/todo\.md',
)

# Only the files that define the spec -> plan -> build pipeline.
GUARDED_FILES = [
    '.claude/commands/nk-spec.md',
    '.claude/commands/nk-plan.md',
    '.claude/commands/nk-build.md',
    'skills/spec-driven-development/SKILL.md',
    'skills/planning-and-task-breakdown/SKILL.md',
]

# Producers and consumers must keep naming the artifacts they write or read.
# Each entry is (label, regex); labels are used in failure messages.
REQUIRED_ARTIFACTS = {
    '.claude/commands/nk-spec.md': (
        ('SPEC.md', r'(?<![\w/])SPEC\.md\b'),
        ('spec/capability-map.md', r'spec/capability-map\.md'),
        ('spec/SPEC-<id>.md', r'spec/SPEC-(?:<id>|[A-Za-z0-9_-]+)\.md'),
    ),
    '.claude/commands/nk-plan.md': (
        ('SPEC.md', r'(?<![\w/])SPEC\.md\b'),
        ('spec/SPEC-<id>.md', r'spec/SPEC-(?:<id>|[A-Za-z0-9_-]+)\.md'),
        ('tasks/plan.md', r'tasks/plan\.md'),
        ('tasks/todo.md', r'tasks/todo\.md'),
    ),
    '.claude/commands/nk-build.md': (
        ('SPEC.md', r'(?<![\w/])SPEC\.md\b'),
        ('docs/SPEC.md', r'docs/SPEC\.md'),
        ('tasks/plan.md', r'tasks/plan\.md'),
        ('tasks/todo.md', r'tasks/todo\.md'),
    ),
    'skills/spec-driven-development/SKILL.md': (
        ('SPEC.md', r'(?<![\w/])SPEC\.md\b'),
        ('spec/capability-map.md', r'spec/capability-map\.md'),
        ('spec/SPEC-<id>.md', r'spec/SPEC-(?:<id>|[A-Za-z0-9_-]+)\.md'),
        ('tasks/plan.md', r'tasks/plan\.md'),
        ('tasks/todo.md', r'tasks/todo\.md'),
    ),
    'skills/planning-and-task-breakdown/SKILL.md': (
        ('tasks/plan.md', r'tasks/plan\.md'),
        ('tasks/todo.md', r'tasks/todo\.md'),
    ),
}

# A path-like token ending in a spec/plan/todo artifact filename. Case
# insensitive so a drifted spec.md is caught and compared against the
# case-sensitive allowlist.
ARTIFACT_RE = re.compile(
    r'(?<![\w/])(?:[A-Za-z0-9._\[\]<>-]+/)*'
    r'(?:SPEC(?:-[A-Za-z0-9_<>\[\]-]+)?|capability-map|plan|todo)\.md\b',
    re.IGNORECASE,
)


def _approved(token):
    return any(re.fullmatch(pattern, token) for pattern in ARTIFACT_ALLOWLIST)


def validate(root):
    root = Path(root).resolve()
    problems = []
    for rel in GUARDED_FILES:
        path = root / rel
        if not path.is_file():
            problems.append(f'{rel}: pipeline file missing')
            continue
        text = path.read_text(encoding='utf-8')
        for match in ARTIFACT_RE.finditer(text):
            token = match.group(0)
            if not _approved(token):
                line = text.count('\n', 0, match.start()) + 1
                problems.append(f'{rel}:{line}: unapproved artifact path {token}')
        for label, pattern in REQUIRED_ARTIFACTS.get(rel, ()):
            if not re.search(pattern, text):
                problems.append(f'{rel}: missing required artifact path {label}')
    return problems