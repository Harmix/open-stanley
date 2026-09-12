import json, re, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent

class StructureTests(unittest.TestCase):
    def test_manifest_and_marketplace_versions_match(self):
        pj = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
        mk = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        self.assertEqual(pj["version"], mk["plugins"][0]["version"])
        self.assertIn(pj["version"], (ROOT / "CHANGELOG.md").read_text())
    def test_every_skill_has_valid_frontmatter(self):
        for skill in (ROOT / "skills").glob("*/SKILL.md"):
            t = skill.read_text()
            m = re.match(r"^---\nname: ([a-z0-9-]+)\ndescription: (.+?)\n---\n", t, re.S)
            self.assertIsNotNone(m, skill); self.assertEqual(m.group(1), skill.parent.name, skill)
            self.assertLess(len(m.group(2)), 1024, skill); self.assertLess(t.count("\n"), 500, skill)
    def test_agents_have_frontmatter(self):
        for a in (ROOT / "agents").glob("*.md"):
            self.assertTrue(a.read_text().startswith("---\nname: "), a)
    def test_scripts_referenced_exist(self):
        text = "".join(p.read_text() for p in ROOT.rglob("*.md") if "stanley-vault/" not in str(p))
        for s in re.findall(r"scripts/(stanley-[a-z]+)", text):
            self.assertTrue((ROOT / "skills" / "stanley" / "scripts" / s).exists(), s)
    def test_no_top_level_bin(self):
        # claude.ai-hosted plugins may not ship a top-level bin/ (it would be added to PATH); scripts live under a skill.
        self.assertFalse((ROOT / "bin").exists())
        for s in ("stanley-audit", "stanley-vault", "stanley-stats", "stanley-preview", "stanley-brief"):
            self.assertTrue((ROOT / "skills" / "stanley" / "scripts" / s).exists(), s)
    def test_gitignore_in_template(self):
        self.assertIn(".stanley-scripts/", (ROOT / "vault-template/.gitignore").read_text())
    def test_no_private_fixtures_tracked(self):
        self.assertIn("tests/evals/private/", (ROOT / ".gitignore").read_text())

if __name__ == "__main__":
    unittest.main()
