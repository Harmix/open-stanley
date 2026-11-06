import json, subprocess, sys, tempfile, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent

class StatsTests(unittest.TestCase):
    def test_lifts_and_experiments(self):
        with tempfile.TemporaryDirectory() as d:
            v = Path(d); (v / "ledger").mkdir()
            rows = [
                {"platform": "linkedin", "url": "u1", "date": "2099-01-01", "hook": "A 12% number hook", "lane": "a", "shape": {"opener": "number"}, "text": "A 12% number hook\nbody", "metrics": {"7d": {"reactions": 40, "comments": 5, "reposts": 0}}, "experiment": {"e": "with"}},
                {"platform": "linkedin", "url": "u2", "date": "2099-01-02", "hook": "No number hook", "lane": "b", "shape": {"opener": "claim"}, "text": "No number hook\nbody", "metrics": {"7d": {"reactions": 10, "comments": 0, "reposts": 0}}, "experiment": {"e": "without"}},
            ]
            (v / "ledger/posts.jsonl").write_text("\n".join(json.dumps(r) for r in rows) + "\n")
            (v / "strategy.md").write_text("- experiment: e | variants: with, without | metric: engagement | min_n: 1\n")
            r = subprocess.run([sys.executable, str(ROOT / "skills/stanley/scripts/stanley-stats"), "--vault", str(v), "--days", "100000", "--json"], capture_output=True, text=True)
            j = json.loads(r.stdout)
            self.assertEqual(j["posts_with_metrics"], 2)
            lanes = {x["key"]: x for x in j["by_lane"]}; self.assertGreater(lanes["a"]["lift"], lanes["b"]["lift"])
            e = j["experiments"][0]; self.assertEqual(e["arms"]["with"]["median"], 50); self.assertIn("directional", e["status"])
            r = subprocess.run([sys.executable, str(ROOT / "skills/stanley/scripts/stanley-stats"), "--vault", str(v), "--days", "100000", "--experiments"], capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr); self.assertIn("experiment e", r.stdout); self.assertNotIn("by lane", r.stdout)
            rows.append({"platform": "linkedin", "url": "u3", "date": "2099-01-03", "hook": "x", "text": "x", "kind": "repost"})
            (v / "ledger/posts.jsonl").write_text("\n".join(json.dumps(r) for r in rows) + "\n")
            r = subprocess.run([sys.executable, str(ROOT / "skills/stanley/scripts/stanley-stats"), "--vault", str(v), "--days", "100000", "--json"], capture_output=True, text=True)
            self.assertEqual(json.loads(r.stdout)["posts"], 2, "reposts must not count as posts")

class PreviewTests(unittest.TestCase):
    def test_html_is_written_and_fold_marked(self):
        with tempfile.TemporaryDirectory() as d:
            draft = Path(d) / "d.txt"; draft.write_text("x" * 300)
            out = Path(d) / "p.png"
            subprocess.run([sys.executable, str(ROOT / "skills/stanley/scripts/stanley-preview"), str(draft), "--platform", "linkedin", "--out", str(out)], capture_output=True, text=True)
            html = out.with_suffix(".html").read_text()
            self.assertIn("fold", html); self.assertIn("300 characters", html)
    def test_x_thread_overflow_flagged(self):
        with tempfile.TemporaryDirectory() as d:
            draft = Path(d) / "d.txt"; draft.write_text("short\n\n---\n\n" + "y" * 300)
            out = Path(d) / "p.png"
            subprocess.run([sys.executable, str(ROOT / "skills/stanley/scripts/stanley-preview"), str(draft), "--platform", "x", "--out", str(out)], capture_output=True, text=True)
            self.assertIn("— over", out.with_suffix(".html").read_text())

if __name__ == "__main__":
    unittest.main()


class ChartTests(unittest.TestCase):
    def test_chart_writes_html_with_tiles_and_bars(self):
        with tempfile.TemporaryDirectory() as d:
            csv = Path(d) / "d.csv"; csv.write_text("name,value,group\nA,100,x\nB,50,y\nC,25,x\nD,10,y\n")
            for kind, n in (("treemap", 4), ("bars", 4)):
                out = Path(d) / f"{kind}.png"
                r = subprocess.run([sys.executable, str(ROOT / "skills/stanley/scripts/stanley-chart"), str(csv), "--kind", kind, "--title", "T", "--unit", "u", "--out", str(out)], capture_output=True, text=True)
                self.assertEqual(r.returncode, 0, r.stderr)
                html = out.with_suffix(".html").read_text()
                self.assertGreaterEqual(html.count("<rect"), n); self.assertIn(">T<", html); self.assertNotIn("http", html.split("<svg")[1][:50])
            r = subprocess.run([sys.executable, str(ROOT / "skills/stanley/scripts/stanley-chart"), str(csv), "--title", "T", "--top", "2", "--out", str(Path(d) / "t.png")], capture_output=True, text=True)
            self.assertEqual(r.returncode, 0); self.assertEqual((Path(d) / "t.html").read_text().count("font-weight=\"600\""), 2)
