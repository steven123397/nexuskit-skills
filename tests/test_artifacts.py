"""Artifact-path drift regression tests for the spec -> plan -> build pipeline."""
from pathlib import Path
import tempfile
import unittest

from check_artifacts import GUARDED_FILES, REQUIRED_ARTIFACTS, validate

ROOT = Path(__file__).resolve().parents[1]


class ArtifactChecks(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory(prefix="nk-artifacts-")
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        for rel in GUARDED_FILES:
            path = self.root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(" ".join(label for label, _ in REQUIRED_ARTIFACTS[rel]), encoding="utf-8")

    def test_current_pipeline(self):
        self.assertEqual([], validate(ROOT))

    def test_unapproved_artifact_path(self):
        path = self.root / ".claude/commands/nk-spec.md"
        path.write_text(path.read_text(encoding="utf-8") + " docs/features/foo/spec.md", encoding="utf-8")
        self.assertTrue(any("unapproved artifact path" in p for p in validate(self.root)))

    def test_case_drift_is_rejected(self):
        path = self.root / ".claude/commands/nk-plan.md"
        path.write_text(path.read_text(encoding="utf-8") + " Spec.md", encoding="utf-8")
        self.assertTrue(any("unapproved artifact path Spec.md" in p for p in validate(self.root)))

    def test_required_artifact_must_stay_named(self):
        path = self.root / ".claude/commands/nk-build.md"
        path.write_text(path.read_text(encoding="utf-8").replace("tasks/todo.md", ""), encoding="utf-8")
        self.assertTrue(any("missing required artifact path tasks/todo.md" in p for p in validate(self.root)))

    def test_missing_pipeline_file(self):
        (self.root / ".claude/commands/nk-build.md").unlink()
        self.assertTrue(any("pipeline file missing" in p for p in validate(self.root)))


if __name__ == "__main__":
    unittest.main()