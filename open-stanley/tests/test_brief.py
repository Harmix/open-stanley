import json, subprocess, sys, tempfile, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
B = ROOT / "skills/stanley/scripts/stanley-brief"
STORY = "---\ntopic: t\nlesson: l\nsource: chat:2026-09-01\nsensitivity: ok\n---\nThree of us picked top 5 facts; overlap was 2.0 out of 5 in the sync and 3.0 out of 5 in R&D. \"the person holding the knowledge had no reason to help\"\n"

def run(*a, inp=None):
    return subprocess.run([sys.executable, str(B), *a], capture_output=True, text=True)

class BriefTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); d = Path(self.tmp.name)
        self.story = d / "s.md"; self.story.write_text(STORY)
        (d / "voice.md").write_text("```yaml\nem_dash: ban\nclosing_question: allow\nbanned_extra: [innate]\n```\n## How this person writes\n- Opens on the event.\n## Post exemplars\n")
        self.d = d
    def tearDown(self): self.tmp.cleanup()
    def test_make_has_facts_terms_and_no_prose(self):
        r = run("make", str(self.story), "--claim", "C", "--vault", str(self.d))
        j = json.loads(r.stdout)
        self.assertIn("2.0 out of 5", j["facts_to_keep_exactly"]); self.assertIn("innate", j["forbidden_terms"])
        self.assertIn("No em dashes.", j["style_rules"]); self.assertEqual(j["claim"], "C")
        self.assertNotIn("draft", j)
    def test_verify_flags_copy_and_forbidden(self):
        r = run("make", str(self.story), "--claim", "C", "--vault", str(self.d)); brief = self.d / "b.json"; brief.write_text(r.stdout)
        draft = self.d / "draft.txt"; draft.write_text("We picked top 5 facts and the overlap was 2.0 out of 5 in the sync, then 3.0 out of 5 in R&D, which is a robust result. " * 3)
        copy = self.d / "copy.txt"; copy.write_text(draft.read_text())
        r = run("verify", str(brief), str(copy), "--draft", str(draft))
        self.assertEqual(r.returncode, 1); self.assertIn("overlap", r.stdout); self.assertIn("robust", r.stdout)
        human = self.d / "h.txt"; human.write_text(("After our sync I asked two co-founders to rank what mattered. " * 3) + "Overlap was 2.0 out of 5. The R&D session came in at 3.0 out of 5. " + ("Each of us reads the same meeting through a different job, and that changes what we keep. " * 6))
        r = run("verify", str(brief), str(human), "--draft", str(draft))
        self.assertEqual(r.returncode, 0, r.stdout)

if __name__ == "__main__":
    unittest.main()
