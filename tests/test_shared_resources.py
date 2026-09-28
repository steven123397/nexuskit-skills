"""Single-source migration regression tests; no agent execution or live installs."""
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from check_shared_resources import validate

ROOT = Path(__file__).resolve().parents[1]


class SharedResourceChecks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="nk-resource-check-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / "relocated plugin"
        for directory in ["skills", ".codex-plugin", ".kimi-plugin"]:
            shutil.copytree(ROOT / directory, self.root / directory)
        (self.root / "tests").mkdir()
        shutil.copy2(ROOT / "tests/shared-resources.json", self.root / "tests/shared-resources.json")

    def failures(self):
        return validate(self.root)

    def test_complete_relocated_install(self):
        self.assertEqual([], self.failures())

    def test_missing_shared_role(self):
        (self.root / "skills/conventions/agents/learnings-researcher.md").unlink()
        self.assertTrue(any("missing shared source" in x for x in self.failures()))

    def test_missing_conventions_in_flat_install(self):
        shutil.rmtree(self.root / "skills/conventions")
        self.assertTrue(any("distribution omits" in x for x in self.failures()))

    def test_restored_local_copy(self):
        src = self.root / "skills/conventions/agents/web-researcher.md"
        dst = self.root / "skills/nk-ideate/references/web-researcher.md"
        shutil.copy2(src, dst)
        self.assertTrue(any("local copy of shared source" in x for x in self.failures()))

    def test_renamed_identical_copy(self):
        src = self.root / "skills/conventions/agents/web-researcher.md"
        dst = self.root / "skills/nk-ideate/references/renamed-research.md"
        shutil.copy2(src, dst)
        self.assertTrue(any("identical reference bodies" in x for x in self.failures()))

    def test_root_reference_duplicates_are_scanned(self):
        for skill in ["nk-plan", "nk-brainstorm"]:
            (self.root / f"skills/{skill}/references/new-flow.md").write_text(skill, encoding="utf-8")
        self.assertTrue(any("unclassified same-name" in x for x in self.failures()))

    def test_caller_link_removed(self):
        p = self.root / "skills/nk-plan/references/research-roles.md"
        p.write_text(p.read_text(encoding="utf-8").replace("../../conventions/agents/web-researcher.md", "missing.md"), encoding="utf-8")
        self.assertTrue(any("does not reference" in x for x in self.failures()))

    def test_stale_inline_path(self):
        p = self.root / "skills/nk-plan/references/research.md"
        with p.open("a", encoding="utf-8") as f:
            f.write("\nRead `agents/web-researcher.md`.\n")
        self.assertTrue(any("unresolved reference" in x for x in self.failures()))

    def test_missing_local_workflow(self):
        (self.root / "skills/nk-plan/references/handoff.md").unlink()
        self.assertTrue(any("membership differs" in x for x in self.failures()))

    def test_incomplete_plugin_manifest(self):
        p = self.root / ".codex-plugin/plugin.json"
        data = json.loads(p.read_text(encoding="utf-8"))
        data["skills"] = "./skills/nk-plan"
        p.write_text(json.dumps(data), encoding="utf-8")
        self.assertTrue(any("distribution omits" in x for x in self.failures()))

    def test_unregistered_shared_role(self):
        (self.root / "skills/conventions/agents/new-role.md").write_text("new method", encoding="utf-8")
        self.assertTrue(any("unregistered shared role" in x for x in self.failures()))


if __name__ == "__main__":
    unittest.main()
