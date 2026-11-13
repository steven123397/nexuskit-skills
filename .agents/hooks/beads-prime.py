#!/usr/bin/env python3
"""Antigravity SessionStart hook to inject Beads workflow context via bd prime."""
import json
from pathlib import Path
import subprocess
import sys


def main() -> int:
    # Drain stdin to satisfy the hook stdin/stdout contract cleanly.
    try:
        sys.stdin.read()
    except OSError:
        pass

    repo_root = Path(__file__).resolve().parents[2]
    if not (repo_root / ".beads").is_dir():
        sys.stdout.write("{}\n")
        return 0

    try:
        result = subprocess.run(
            ["bd", "prime"],
            cwd=repo_root,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=8,
            check=False,
        )
    except (OSError, subprocess.SubprocessError):
        sys.stdout.write("{}\n")
        return 0

    context = result.stdout.strip()
    if result.returncode != 0 or not context:
        sys.stdout.write("{}\n")
        return 0

    payload = {
        "injectSteps": [
            {
                "systemMessage": {
                    "systemMessage": context,
                }
            }
        ]
    }
    sys.stdout.write(json.dumps(payload, ensure_ascii=True) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
