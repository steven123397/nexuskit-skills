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
    names = {p.parent.name for p in (root / "skills").glob("nk-*/SKILL.md")}
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
        found = set(re.findall(r"\bnk-[a-z][a-z0-9-]*\b", text))
        if found != expected:
            problems.append(f"{label}: skill inventory differs; missing={sorted(expected - found)}, extra={sorted(found - expected)}")

    def count(label, text):
        counts = re.findall(r"(\d+)\s*(?:个\s*nk-\*|nk-\*\s+skills)", text)
        if not counts or any(int(n) != len(names) for n in counts):
            problems.append(f"{label}: skill count must match disk ({len(names)})")

    versions = []
    for rel in [".codex-plugin/plugin.json", ".kimi-plugin/plugin.json"]:
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
        if rel.startswith(".codex-plugin"):
            interface = data.get("interface")
            long_text = interface.get("longDescription", "") if isinstance(interface, dict) else ""
            if not isinstance(long_text, str):
                long_text = ""
            count(f"{rel} longDescription", long_text)
            inventory(f"{rel} longDescription", long_text, names)

    if len(versions) == 2 and len(set(versions)) != 1:
        problems.append("plugin versions must match across Codex and Kimi")
    if release_tag is not None:
        if len(versions) != 2 or any(release_tag != f"v{version}" for version in versions):
            problems.append("release tag must match both plugin versions")
        elif not (root / "docs/releases" / f"{release_tag}.md").is_file():
            problems.append(f"release notes missing for {release_tag}")

    market_rel = ".agents/plugins/marketplace.json"
    market = load(market_rel)
    if market is not None:
        if market.get("name") != "nexuskit-skills":
            problems.append(f"{market_rel}: marketplace name must be nexuskit-skills")
        plugins = market.get("plugins")
        if not isinstance(plugins, list) or len(plugins) != 1 or not isinstance(plugins[0], dict):
            problems.append(f"{market_rel}: expected one plugin entry")
        else:
            entry = plugins[0]
            if entry.get("name") != "nexuskit" or entry.get("source") != {"source": "local", "path": "./"}:
                problems.append(f"{market_rel}: plugin identity/source differs from local manifest")

    for rel in ["README.md", "skills/nk-ask-ljq/SKILL.md"]:
        try:
            inventory(rel, (root / rel).read_text(encoding="utf-8"), names)
        except OSError as exc:
            problems.append(f"{rel}: cannot read routing map: {exc}")
    return problems
