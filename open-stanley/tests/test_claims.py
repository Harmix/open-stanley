"""The public claims (README, landing, llms.txt, manifest) must agree with the repo. See docs/claims.yml."""
import json, re, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent   # open-stanley/
REPO = ROOT.parent

def read(rel): return (REPO / rel).read_text(encoding="utf-8")

class ClaimsTests(unittest.TestCase):
    def test_versions_agree(self):
        v = json.loads(read("open-stanley/.claude-plugin/plugin.json"))["version"]
        self.assertEqual(json.loads(read(".claude-plugin/marketplace.json"))["plugins"][0]["version"], v)
        self.assertIn(f"version-{v}-", read("README.md"), "README badge version")
        top = re.search(r"^## (\d+\.\d+\.\d+)", read("open-stanley/CHANGELOG.md"), re.M).group(1)
        self.assertEqual(top, v, "CHANGELOG top entry")

    def test_counts_agree(self):
        skills = len([p for p in (ROOT / "skills").iterdir() if (p / "SKILL.md").exists()])
        scripts = len([p for p in (ROOT / "skills/stanley/scripts").iterdir() if p.name.startswith("stanley-")])
        agents = len(list((ROOT / "agents").glob("*.md")))
        for rel in ("README.md", "docs/index.html", "llms.txt"):
            m = re.findall(r"(\d+) skills", read(rel))
            for n in m: self.assertEqual(int(n), skills, f"{rel} says {n} skills, repo has {skills}")
        for n in re.findall(r"(\d+) CLI scripts", read("README.md")): self.assertEqual(int(n), scripts)
        for n in re.findall(r"(\d+) agents", read("docs/index.html")): self.assertEqual(int(n), agents)
        # test count stated as "N at <version>" in the README Tests section
        loader = unittest.defaultTestLoader
        suite = loader.discover(str(ROOT / "tests"), top_level_dir=str(ROOT / "tests"))
        total = suite.countTestCases()
        m = re.search(r"`tests/`, (\d+) at (\d+\.\d+\.\d+)", read("README.md"))
        self.assertIsNotNone(m, "README should state the test count as '`tests/`, N at <version>'")
        self.assertEqual(int(m.group(1)), total, f"README says {m.group(1)} tests, discover finds {total}")
        self.assertEqual(m.group(2), json.loads(read("open-stanley/.claude-plugin/plugin.json"))["version"])

    def test_install_commands_everywhere(self):
        for rel in ("README.md", "docs/index.html", "llms.txt"):
            s = read(rel)
            for cmd in ("/plugin marketplace add Harmix/open-stanley", "/plugin install open-stanley@open-stanley", "npx skills add Harmix/open-stanley"):
                self.assertIn(cmd, s, f"{cmd} missing from {rel}")

    def test_landing_strategies_exist(self):
        site = read("docs/index.html")
        for name, target in {"Atlas": "skills/atlas", "Study": "skills/study", "Longform": "skills/longform", "Repackage": "skills/rituals"}.items():
            self.assertIn(f"<b>{name}</b>", site)
            self.assertTrue((ROOT / target / "SKILL.md").exists(), target)
        self.assertTrue((REPO / ".github/ISSUE_TEMPLATE/strategy-tip.yml").exists())
        self.assertTrue((ROOT / "templates/scheduled-tasks/creator-teardown-weekly.md").exists())

    def test_landing_links_resolve(self):
        site = read("docs/index.html")
        for rel in re.findall(r'href="(?!https?:|#|mailto:)([^"]+)"', site):
            path = rel.split("#")[0].rstrip("/")
            if not path: continue
            p = REPO / "docs" / path
            md = p.with_suffix(".md") if p.suffix == ".html" else None
            self.assertTrue(p.exists() or (md is not None and md.exists()) or (p / "index.md").exists() or (p / "index.html").exists(), f"landing links to missing {rel}")
        for rel in re.findall(r'https://github.com/Harmix/open-stanley/blob/main/([^"#)]+)', site + read("README.md") + read("llms.txt")):
            self.assertTrue((REPO / rel).exists(), f"link to missing repo file {rel}")

    def test_browser_audit_lexicon_matches_script(self):
        """docs/audit.html claims to mirror stanley-audit's lexicon; every label in the script must appear in the page."""
        script = read("open-stanley/skills/stanley/scripts/stanley-audit")
        page = read("docs/audit.html")
        labels = re.findall(r'^\s*r"[^"]+":\s*"([^"]+)",\s*$', script[script.index("BANNED = {"):script.index("WEASEL = [")], re.M)
        self.assertGreater(len(labels), 40)
        missing = [l for l in labels if l.replace("'", "'") not in page]
        self.assertEqual(missing, [], f"labels in stanley-audit missing from docs/audit.html: {missing}")

    def test_site_llms_txt_is_a_copy(self):
        """docs/llms.txt is what the site serves at /llms.txt; it must equal the repo-root llms.txt."""
        self.assertEqual(read("docs/llms.txt"), read("llms.txt"), "run: cp llms.txt docs/llms.txt")

if __name__ == "__main__":
    unittest.main()
