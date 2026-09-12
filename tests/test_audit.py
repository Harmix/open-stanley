import json, subprocess, sys, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
AUDIT = ROOT / "skills/stanley/scripts/stanley-audit"

def run(text, platform="linkedin", vault=None):
    args = [sys.executable, str(AUDIT), "-", "--platform", platform, "--json"] + (["--vault", str(vault)] if vault else [])
    r = subprocess.run(args, input=text, capture_output=True, text=True)
    return json.loads(r.stdout)

def rules(j): return {f["rule"] for f in j["findings"]}

class AuditRules(unittest.TestCase):
    def test_lexicon_blocks(self):
        j = run("We leverage a robust, cutting-edge approach to delve into memory.")
        self.assertIn("lexicon", rules(j)); self.assertFalse(j["pass"])
    def test_not_x_but_y(self):
        self.assertIn("not-x-but-y", rules(run("It's not about the model. It's about the memory.")))
    def test_choppy(self):
        self.assertIn("choppy", rules(run("Short one. Another one. And one more. Then a much longer sentence that keeps going for a while to balance it.")))
    def test_setup_and_wrapup(self):
        r = rules(run("In today's fast-paced world, agents matter. We tried some things and learned a few. Ultimately, the future belongs to the focused."))
        self.assertIn("setup-sentence", r); self.assertIn("wrap-up", r)
    def test_hashtags_and_link(self):
        r = rules(run("A real post with a link https://example.com and tags.\n#ai #agents"))
        self.assertIn("hashtags", r); self.assertIn("link-in-body", r)
    def test_human_post_passes(self):
        t = (ROOT / "evals/fixtures/human-post-notetaker.txt").read_text()
        self.assertTrue(run(t)["pass"])
    def test_comment_mode(self):
        r = rules(run("This is such a great point and it really resonates with me because context matters.", "comment"))
        self.assertIn("agreement-opener", r)
        self.assertTrue(run("How do you know which project context is still relevant? Most projects are dynamic, and decisions change between meetings.", "comment")["pass"])
    def test_x_thread_limits(self):
        long = "x" * 300
        j = run(f"first\n\n---\n\n{long}", "x")
        self.assertIn("tweet-length", rules(j))
    def test_allowed_override_and_receipts(self):
        import tempfile, os
        with tempfile.TemporaryDirectory() as d:
            v = Path(d); (v / "stories").mkdir()
            (v / "voice.md").write_text("```yaml\nallowed: [robust]\nem_dash: allow\n```\n")
            (v / "stories/s.md").write_text("---\ntopic: t\nlesson: l\nsource: chat:2026-09-01\n---\nOverlap was 2.0 out of 5.\n")
            j = run("Our system is robust. Overlap was 2.0 out of 5 in one meeting and 3.7 in another, a longer sentence to be safe here.", vault=v)
            self.assertNotIn("lexicon", rules(j))
            recs = [f for f in j["findings"] if f["rule"] == "receipt-number"]
            self.assertTrue(any("3.7" in f["msg"] for f in recs)); self.assertFalse(any("2.0" in f["msg"] for f in recs))

if __name__ == "__main__":
    unittest.main()

class SelfTest(unittest.TestCase):
    def test_selftest_passes(self):
        import subprocess, sys
        r = subprocess.run([sys.executable, str(AUDIT), "selftest"], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr); self.assertIn("selftest: ok", r.stdout)
