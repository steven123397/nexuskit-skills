"""Malformed metadata must fail; supported optional fields must remain usable."""
import unittest

from check_frontmatter import validate_frontmatter


class FrontmatterChecks(unittest.TestCase):
    def check(self, metadata):
        return validate_frontmatter(f"---\n{metadata}\n---\n# Body\n", "nk-demo")

    def test_supported_metadata_and_multiline_description(self):
        self.assertEqual([], self.check(
            "name: nk-demo\ndescription: >\n  A multiline description\n  with English text.\n"
            "argument-hint: '[scope]'\ndisable-model-invocation: true\n"
            "metadata:\n  tags: [review, plans]\n  custom-field: enabled"
        ))

    def test_legal_comments_and_quoted_hash(self):
        self.assertEqual([], self.check(
            'name: nk-demo # legal YAML comment\ndescription: "Explain # issues: clearly"'
        ))

    def test_malformed_yaml(self):
        for value in ('[unclosed', 'bad: nested', '"unclosed', '\tbad'):
            with self.subTest(value=value):
                self.assertTrue(self.check(f"name: nk-demo\ndescription: {value}"))

    def test_duplicate_keys(self):
        for extra in ('name: nk-demo', 'description: second', 'metadata:\n  x: 1\n  x: 2'):
            with self.subTest(extra=extra):
                self.assertTrue(any("duplicate key" in p for p in self.check(
                    f"name: nk-demo\ndescription: first\n{extra}"
                )))

    def test_non_mapping_frontmatter(self):
        for body in ('', '[]', 'scalar', '- name: nk-demo'):
            with self.subTest(body=body):
                self.assertTrue(self.check(body))

    def test_required_fields_are_strings(self):
        for value in ('null', 'true', '42', '[]', '{}', '" "'):
            with self.subTest(value=value):
                self.assertTrue(self.check(f"name: nk-demo\ndescription: {value}"))
        self.assertTrue(self.check("description: example"))
        self.assertTrue(self.check("name: nk-demo"))

    def test_directory_mismatch(self):
        self.assertTrue(self.check("name: nk-other\ndescription: example"))

    def test_description_policy_does_not_restrict_body_language(self):
        self.assertTrue(any("English-only" in p for p in self.check(
            "name: nk-demo\ndescription: English with 中文 keywords")))
        self.assertEqual([], validate_frontmatter(
            "---\nname: nk-demo\ndescription: Explain clearly.\n---\n中文正文\n", "nk-demo"))

    def test_invocation_flag_is_boolean(self):
        for value in ('"true"', '1', 'null'):
            with self.subTest(value=value):
                self.assertTrue(any("YAML boolean" in p for p in self.check(
                    f"name: nk-demo\ndescription: Example\ndisable-model-invocation: {value}")))

    def test_delimiters_are_whole_lines(self):
        self.assertTrue(validate_frontmatter("---\nname: nk-demo\n---extra", "nk-demo"))
        self.assertTrue(validate_frontmatter("# Body", "nk-demo"))
        self.assertEqual([], validate_frontmatter(
            "---\r\nname: nk-demo\r\ndescription: example\r\n---\r\n", "nk-demo"
        ))

    def test_unsafe_tags_and_multiple_documents(self):
        self.assertTrue(self.check("name: nk-demo\ndescription: !!python/object:os.system {}"))
        self.assertTrue(self.check("name: nk-demo\ndescription: example\n...\nname: another"))


if __name__ == "__main__":
    unittest.main()
