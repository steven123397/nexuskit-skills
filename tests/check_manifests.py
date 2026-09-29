"""Check published inventory against disk and user-facing entry maps."""
import json
from pathlib import Path
import re


def validate(root):
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

    for rel in [".codex-plugin/plugin.json", ".kimi-plugin/plugin.json"]:
        data = load(rel)
        if data is None:
            continue
        if data.get("name") != "nexuskit":
            problems.append(f"{rel}: plugin name must be nexuskit")
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
