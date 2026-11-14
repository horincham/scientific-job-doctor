from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "scientific-job-doctor"


class DistributionTest(unittest.TestCase):
    def test_entry_point_and_reference_routes(self):
        content = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        frontmatter = re.match(r"\A---\n(.*?)\n---\n", content, re.S)
        self.assertIsNotNone(frontmatter)
        self.assertIn(f"name: {SKILL.name}", frontmatter[1].splitlines())
        description = re.search(r'^description: "(.+)"$', frontmatter[1], re.M)
        self.assertIsNotNone(description)
        self.assertLessEqual(len(description[1]), 1024)
        for reference in (SKILL / "references").glob("*.md"):
            self.assertIn(f"(references/{reference.name})", content)

    def test_relative_markdown_links_resolve(self):
        for document in ROOT.rglob("*.md"):
            if ".git" in document.parts:
                continue
            for target in re.findall(r"\]\(([^)]+)\)", document.read_text(encoding="utf-8")):
                if "://" in target or target.startswith("#"):
                    continue
                with self.subTest(document=document.relative_to(ROOT), target=target):
                    self.assertTrue((document.parent / target.split("#", 1)[0]).exists())

    def test_manual_topics_have_official_sources(self):
        text = (SKILL / "references" / "gaussian-manual.md").read_text(encoding="utf-8")
        cards = re.split(r"(?m)^### ", text)[1:]
        self.assertGreaterEqual(len(cards), 12)
        for card in cards:
            with self.subTest(topic=card.splitlines()[0]):
                self.assertRegex(card, r"\]\(https://gaussian\.com/[^)]+\)")


if __name__ == "__main__":
    unittest.main()
