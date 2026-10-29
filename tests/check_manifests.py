"""Check published inventory against disk and user-facing entry maps."""
import json
from pathlib import Path
import re


# SemVer, including prereleases such as 0.2.0-beta.1.
NUMBER = r"(?:0|[1-9][0-9]*)"
IDENTIFIER = rf"(?:{NUMBER}|[0-9]*[A-Za-z-][0-9A-Za-z-]*)"
VERSION = re.compile(rf"{NUMBER}\.{NUMBER}\.{NUMBER}(?:-{IDENTIFIER}(?:\.{IDENTIFIER})*)?(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?")


def validate(root, release_tag=None):
    root = Path(root).resolve()
    problems = []
    entries = list((root / "skills").rglob("SKILL.md"))
    names = {p.parent.name for p in entries}
    if len(names) != len(entries):
        problems.append("inventory: duplicate skill names across groups")
    for entry in entries:
        parts = entry.relative_to(root).parts
        if len(parts) != 3 or not re.fullmatch(r"[a-z][a-z0-9-]*", parts[1]):
            problems.append(f"inventory: unexpected skill location {entry.relative_to(root)}")
        if (entry.parent / "SKILL.legacy.md").exists():
            problems.append(f"inventory: remove legacy draft before enabling {entry.parent.name}")
    if not names:
        return ["inventory: no nk-* skills found"]

    def load(rel):
        try:
            value = json.loads((root / rel).read_text(encoding="utf-8"))
            if not isinstance(value, dict):
                raise ValueError("expected JSON object")
            return value
        except (OSError, ValueError) as exc:
            problems.append(f"{rel}: invalid manifest: {exc}")
            return None

    def inventory(label, text, expected):
        found = {n for n in expected
                 if re.search(rf"(?<![A-Za-z0-9-]){re.escape(n)}(?![A-Za-z0-9-])", text)}
        if found != expected:
            problems.append(f"{label}: skill inventory differs; missing={sorted(expected - found)}, extra={sorted(found - expected)}")

    def count(label, text):
        counts = re.findall(r"(\d+)\s*(?:个\s*(?:nk-\*\s*)?技能|skills)", text)
        if not counts or any(int(n) != len(names) for n in counts):
            problems.append(f"{label}: skill count must match disk ({len(names)})")

    # v0.4.0 起主体客户端为 Claude Code；Codex 安装方式废止（SKILL.md 体积超其读取上限），
    # Kimi 适配挂起至收尾阶段（.kimi-plugin/ 保留在仓但暂不参与校验）。
    versions = []
    for rel in [".claude-plugin/plugin.json"]:
        data = load(rel)
        if data is None:
            continue
        if data.get("name") != "nexuskit":
            problems.append(f"{rel}: plugin name must be nexuskit")
        version = data.get("version")
        if not isinstance(version, str) or not VERSION.fullmatch(version):
            problems.append(f"{rel}: version must be valid SemVer")
        else:
            versions.append(version)
        path = data.get("skills")
        if not isinstance(path, str) or (root / path).resolve() != root / "skills":
            problems.append(f"{rel}: skills path must distribute ./skills/")
        count(rel, str(data.get("description", "")))

    if release_tag is not None:
        if len(versions) != 1 or release_tag != f"v{versions[0]}":
            problems.append("release tag must match plugin version")
        elif not (root / "docs/releases" / f"{release_tag}.md").is_file():
            problems.append(f"release notes missing for {release_tag}")

    markets = {
        ".agents/plugins/marketplace.json": {"source": "local", "path": "./"},
        ".claude-plugin/marketplace.json": "./",
    }
    for market_rel, expected_source in markets.items():
        market = load(market_rel)
        if market is None:
            continue
        if market.get("name") != "nexuskit-skills":
            problems.append(f"{market_rel}: marketplace name must be nexuskit-skills")
        plugins = market.get("plugins")
        if not isinstance(plugins, list) or len(plugins) != 1 or not isinstance(plugins[0], dict):
            problems.append(f"{market_rel}: expected one plugin entry")
        else:
            entry = plugins[0]
            if entry.get("name") != "nexuskit" or entry.get("source") != expected_source:
                problems.append(f"{market_rel}: plugin identity/source differs from local manifest")

    for rel in ["README.md"]:
        try:
            text = (root / rel).read_text(encoding="utf-8")
            start, end = "<!-- installable-skills -->", "<!-- /installable-skills -->"
            if start not in text or end not in text:
                problems.append(f"{rel}: missing installable skill section")
            else:
                inventory(rel, text.split(start, 1)[1].split(end, 1)[0], names)
        except OSError as exc:
            problems.append(f"{rel}: cannot read routing map: {exc}")
    return problems
