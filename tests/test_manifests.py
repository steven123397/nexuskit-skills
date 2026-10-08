"""Manifest drift regression tests; no installs or skill execution."""
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from check_manifests import validate

ROOT = Path(__file__).resolve().parents[1]


class ManifestChecks(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory(prefix="nk-manifest-")
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        for source in (ROOT / "skills").rglob("SKILL.md"):
            target = self.root / source.relative_to(ROOT)
            target.parent.mkdir(parents=True)
            shutil.copy2(source, target)
        for rel in [".codex-plugin/plugin.json", ".kimi-plugin/plugin.json",
                    ".agents/plugins/marketplace.json", "README.md"]:
            target = self.root / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / rel, target)

    def mutate(self, rel, edit):
        path = self.root / rel
        data = json.loads(path.read_text(encoding="utf-8"))
        edit(data)
        path.write_text(json.dumps(data), encoding="utf-8")

    def test_current_inventory(self):
        self.assertEqual([], validate(self.root))

    def test_semver_and_matching_plugin_versions(self):
        for invalid in [None, 2, "0.2.0beta", "01.2.0", "0.2.0-01"]:
            with self.subTest(version=invalid):
                self.mutate(".codex-plugin/plugin.json", lambda d: d.update(version=invalid))
                self.assertTrue(any("SemVer" in p for p in validate(self.root)))
        self.mutate(".codex-plugin/plugin.json", lambda d: d.update(version="99.0.0-beta.1"))
        self.assertTrue(any("versions must match" in p for p in validate(self.root)))

    def test_release_tag_and_notes(self):
        for rel in [".codex-plugin/plugin.json", ".kimi-plugin/plugin.json"]:
            self.mutate(rel, lambda d: d.update(version="0.2.0-beta.1"))
        self.assertEqual([], validate(self.root))
        self.assertTrue(any("release tag" in p for p in validate(self.root, "v0.1.1")))
        self.assertTrue(any("release notes missing" in p for p in validate(self.root, "v0.2.0-beta.1")))
        notes = self.root / "docs/releases/v0.2.0-beta.1.md"
        notes.parent.mkdir(parents=True)
        notes.write_text("# Beta release\n", encoding="utf-8")
        self.assertEqual([], validate(self.root, "v0.2.0-beta.1"))

    def test_invalid_json_and_root_types(self):
        for rel in [".codex-plugin/plugin.json", ".kimi-plugin/plugin.json", ".agents/plugins/marketplace.json"]:
            path = self.root / rel
            original = path.read_text(encoding="utf-8")
            for text in ["{", "[]", "null"]:
                with self.subTest(path=rel, text=text):
                    path.write_text(text, encoding="utf-8")
                    self.assertTrue(any("invalid manifest" in p for p in validate(self.root)))
            path.write_text(original, encoding="utf-8")

    def test_new_disk_skill_requires_inventory_update(self):
        path = self.root / "skills/engineering/nk-new/SKILL.md"
        path.parent.mkdir()
        path.write_text("", encoding="utf-8")
        problems = validate(self.root)
        self.assertTrue(any("skill count" in p for p in problems))
        self.assertTrue(any("skill inventory differs" in p for p in problems))

    def test_correct_count_but_incomplete_list(self):
        self.mutate(".codex-plugin/plugin.json", lambda d: d["interface"].update(
            longDescription=d["interface"]["longDescription"].replace("nk-grill, ", "")))
        self.assertTrue(any("skill inventory differs" in p for p in validate(self.root)))

    def test_wrong_count_in_each_manifest(self):
        for rel in [".codex-plugin/plugin.json", ".kimi-plugin/plugin.json"]:
            with self.subTest(path=rel):
                self.mutate(rel, lambda d: d.update(description="999 个 nk-* 技能"))
                self.assertTrue(any(rel in p and "skill count" in p for p in validate(self.root)))

    def test_distribution_path(self):
        self.mutate(".codex-plugin/plugin.json", lambda d: d.update(skills="../skills"))
        self.assertTrue(any("skills path" in p for p in validate(self.root)))

    def test_marketplace_identity_and_source(self):
        rel = ".agents/plugins/marketplace.json"
        self.mutate(rel, lambda d: d.update(name="wrong", plugins=[{"name": "wrong"}]))
        problems = validate(self.root)
        self.assertTrue(any("marketplace name" in p for p in problems))
        self.assertTrue(any("identity/source" in p for p in problems))

    def test_unknown_or_missing_router_entry(self):
        for rel in ["README.md"]:
            path = self.root / rel
            path.write_text(path.read_text(encoding="utf-8").replace("nk-grill", "nk-missing"), encoding="utf-8")
            self.assertTrue(any(rel in p and "skill inventory" in p for p in validate(self.root)))

    def test_legacy_and_empty_slots_are_not_installable(self):
        path = self.root / "skills/productivity/nk-draft"
        path.mkdir(parents=True)
        (path / "SKILL.legacy.md").write_text("Old workflow", encoding="utf-8")
        (path / ".gitkeep").touch()
        self.assertEqual([], validate(self.root))

    def test_duplicate_name_in_another_group_is_rejected(self):
        path = self.root / "skills/productivity/nk-grill/SKILL.md"
        path.parent.mkdir(parents=True)
        path.write_text("", encoding="utf-8")
        self.assertTrue(any("duplicate skill names" in p for p in validate(self.root)))


if __name__ == "__main__":
    unittest.main()
