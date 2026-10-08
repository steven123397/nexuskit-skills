"""Nested skill discovery and isolation from legacy drafts."""
from pathlib import Path
import tempfile
import unittest

from run_checks import link_problems, reference_problems, skill_entries


class LayoutChecks(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name).resolve()
        self.entry = self.root / 'skills/engineering/nk-demo/SKILL.md'
        self.entry.parent.mkdir(parents=True)
        self.entry.write_text('Demo', encoding='utf-8')

    def test_nested_entries_ignore_legacy(self):
        legacy = self.root / 'skills/productivity/nk-old/SKILL.legacy.md'
        legacy.parent.mkdir(parents=True)
        legacy.write_text('[old](missing.md)', encoding='utf-8')
        self.assertEqual([self.entry], skill_entries(self.root))
        self.assertEqual([], link_problems(self.root))

    def test_broken_private_link_and_cross_skill_dependency(self):
        self.entry.write_text('[local](template.md)', encoding='utf-8')
        self.assertTrue(link_problems(self.root))
        (self.entry.parent / 'template.md').write_text('Template', encoding='utf-8')
        self.assertEqual([], link_problems(self.root))
        other = self.entry.parent.parent / 'nk-other'
        other.mkdir()
        (other / 'prompt.md').touch()
        self.entry.write_text('[other](../nk-other/prompt.md)', encoding='utf-8')
        self.assertTrue(any('cross-skill' in p for p in link_problems(self.root)))

    def test_unknown_name_and_retired_runtime_dependency(self):
        self.entry.write_text('Call `nk-missing`.', encoding='utf-8')
        self.assertTrue(reference_problems(self.root))
        (self.entry.parent.parent / 'nk-missing').mkdir()
        self.assertEqual([], reference_problems(self.root))
        self.entry.write_text('Read `../../conventions/rules.md`.', encoding='utf-8')
        self.assertTrue(reference_problems(self.root))
