"""stanley-stats --predict: a reach band from the ledger for a draft."""
import json, os, subprocess, sys, tempfile, unittest
from pathlib import Path
SS = Path(__file__).resolve().parent.parent / "skills/stanley/scripts/stanley-stats"

class PredictTests(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp()); (self.d / "ledger").mkdir(); (self.d / "drafts").mkdir()
        (self.d / "my-human.md").write_text("- name: t\n")
        rows = []
        for i in range(6):
            txt = ("I asked a YC partner about this. " if i < 3 else "Here is a tip. ") + "x" * 1000 + ("?" if i < 3 else ".")
            rows.append({"platform": "linkedin", "url": f"u{i}", "date": "2026-10-0%d" % (i + 1), "lane": "founder" if i < 3 else "tips", "text": txt, "hook": txt[:40],
                         "metrics": {"7d": {"impressions": 5000 + i * 1000 if i < 3 else 500 + i, "reactions": 20, "comments": 2, "reposts": 0, "saves": 0}}})
        (self.d / "ledger/posts.jsonl").write_text("\n".join(json.dumps(r) for r in rows) + "\n")
        (self.d / "drafts/a.md").write_text("I asked a YC partner where the moat is. " + "y" * 1000 + "?")
        (self.d / "drafts/a.meta.json").write_text(json.dumps({"lane": "founder", "image": "image"}))

    def run_predict(self, *args):
        return subprocess.run([sys.executable, str(SS), "--vault", str(self.d), "--days", "3650", "--predict", str(self.d / "drafts/a.md"), *args], capture_output=True, text=True)

    def test_band_from_similar_posts(self):
        r = self.run_predict("--json"); self.assertEqual(r.returncode, 0, r.stderr)
        out = json.loads(r.stdout)
        self.assertEqual(out["similar_posts"], 3)
        self.assertEqual(out["impressions"]["median"], 6000)
        self.assertIn("lane:founder", out["features"])

    def test_too_few_posts(self):
        (self.d / "ledger/posts.jsonl").write_text("")
        r = self.run_predict(); self.assertIn("fewer than 3", r.stdout)

if __name__ == "__main__":
    unittest.main()
