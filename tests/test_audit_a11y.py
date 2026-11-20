"""Regression tests for the accessibility audit report merger."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


def _find_bash():
    if os.name != "nt":
        return shutil.which("bash")
    git = shutil.which("git")
    if not git:
        return None
    for parent in Path(git).resolve().parents:
        for candidate in (parent / "bin/bash.exe", parent / "usr/bin/bash.exe"):
            if candidate.is_file():
                return str(candidate)
    return None


BASH = _find_bash()
NODE = shutil.which("node")
SCRIPT = ROOT / "skills/accessibility-engineering/scripts/audit-a11y.sh"


@unittest.skipUnless(BASH and NODE, "requires bash and node")
class AuditA11yTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory(prefix="nk-a11y-")
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.bin = self.root / "bin"
        self.bin.mkdir()
        self._write_npx_stub()

    def _write_npx_stub(self):
        stub = self.bin / "npx"
        stub.write_text(
            """#!/bin/bash
set -u
if [[ "${1:-}" == "--yes" ]]; then shift; fi
tool=${1:-}
if (($#)); then shift; fi
if [[ "$tool" == @axe-core/cli@* ]]; then
  dir=
  save=
  while (($#)); do
    case "$1" in
      --dir) dir=$2; shift 2 ;;
      --save) save=$2; shift 2 ;;
      *) shift ;;
    esac
  done
  printf '%s' '[{"violations":[{"id":"image-alt","impact":"serious","nodes":[]}]}]' > "$dir/$save"
  exit 0
elif [[ "$tool" == pa11y@* ]]; then
  printf '%s' '[{"code":"WCAG2AA.H37","typeCode":1,"message":"Img missing alt"}]'
  exit 2
fi
exit 99
""",
            encoding="utf-8",
            newline="\n",
        )
        stub.chmod(0o755)

    def _posix_path(self, path):
        if os.name != "nt":
            return str(path)
        return subprocess.check_output(
            [BASH, "-c", 'cygpath -u "$1"', "audit-test", str(path)],
            text=True,
        ).strip()

    def _run_audit(self, *args):
        command = [
            BASH,
            "-c",
            'export PATH="$1:$PATH"; export TMPDIR=/tmp; shift; exec bash "$@"',
            "audit-test",
            self._posix_path(self.bin),
            self._posix_path(SCRIPT),
            *args,
        ]
        return subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )

    def test_url_mode_merges_valid_reports_with_posix_tmpdir(self):
        completed = self._run_audit("url", "https://example.invalid", "--json")

        self.assertEqual(0, completed.returncode, completed.stderr)
        report = json.loads(completed.stdout)
        self.assertEqual(2, report["summary"]["violations"])
        self.assertEqual(2, report["summary"]["serious"])
        self.assertEqual(
            {"axe-core", "pa11y"},
            {violation["source"] for violation in report["violations"]},
        )

    def test_text_mode_reads_merged_report_with_posix_tmpdir(self):
        completed = self._run_audit("url", "https://example.invalid")

        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertIn("Total violations: 2", completed.stdout)
        self.assertIn("Serious:  2", completed.stdout)


if __name__ == "__main__":
    unittest.main()
