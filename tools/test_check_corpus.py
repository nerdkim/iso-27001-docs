"""Regression tests for the corpus boundaries, using real documents in temporary copies."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import check_corpus as checker


class DocumentBoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(checker.ROOT)
        catalog = json.loads(Path(checker.CATALOG).read_text(encoding="utf-8"))
        cls.catalog = {item["no"]: item for item in catalog["controls"]}

    def check(self, lang, transform):
        source = self.root / "docs" / lang / "A.5-organizational" / "A.5.1.md"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / source.name
            path.write_text(transform(source.read_text(encoding="utf-8")), encoding="utf-8")
            checker.problems.clear()
            checker.clause_titles = {"ko": {}, "en": {}}
            checker.check_document(str(path), lang, self.catalog)
            return list(checker.problems)

    def test_real_documents_pass(self):
        for lang in checker.LANGS:
            with self.subTest(lang=lang):
                self.assertEqual(self.check(lang, lambda text: text), [])

    def test_arbitrary_quote_cannot_replace_copyright_notice(self):
        for lang in checker.LANGS:
            with self.subTest(lang=lang):
                issues = self.check(lang, lambda text: text.rsplit("\n---\n", 1)[0]
                                    + "\n---\n> An unrelated quote.\n")
                self.assertTrue(issues, "A footer-shaped quote must not satisfy the copyright rule")

    def test_removing_limitation_fails(self):
        for lang, limitation in (("en", "not the normative text"), ("ko", "규범 텍스트가 아닙니다")):
            with self.subTest(lang=lang):
                self.assertTrue(self.check(lang, lambda text: text.replace(limitation, "")))

    def test_footer_must_remain_last(self):
        self.assertTrue(self.check("en", lambda text: text + "\nUnattributed content.\n"))

    def test_extra_or_duplicate_section_fails(self):
        for title in ("Unexpected section", "Key checkpoints"):
            with self.subTest(title=title):
                self.assertTrue(self.check("en", lambda text: text.replace(
                    "\n---\n", f"\n## {title}\n\nExtra content.\n\n---\n")))


class AgentEntrypointTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        (self.root / "CLAUDE.md").write_text("Project instructions\n")
        (self.root / "AGENTS.md").symlink_to("CLAUDE.md")
        skill = self.root / "skill" / "iso-27001-review"
        skill.mkdir(parents=True)
        (skill / "SKILL.md").write_text("Skill instructions\n")
        (skill / "topic-index.json").write_text("{}\n")
        self.link = self.root / ".agents" / "skills" / "iso-27001-review"
        self.link.parent.mkdir(parents=True)
        self.link.symlink_to("../../skill/iso-27001-review")

    def issues(self):
        checker.problems.clear()
        with patch.object(checker, "ROOT", str(self.root)):
            checker.check_agent_entrypoints()
        return list(checker.problems)

    def test_portable_links_pass(self):
        self.assertEqual(self.issues(), [])

    def test_missing_skill_entrypoint_fails(self):
        self.link.unlink()
        self.assertTrue(self.issues())

    def test_missing_skill_source_fails(self):
        (self.link / "SKILL.md").unlink()
        self.assertTrue(self.issues())

    def test_instruction_copy_fails(self):
        path = self.root / "AGENTS.md"
        path.unlink()
        path.write_text("Instructions that can drift\n")
        self.assertTrue(self.issues())


if __name__ == "__main__":
    unittest.main()
