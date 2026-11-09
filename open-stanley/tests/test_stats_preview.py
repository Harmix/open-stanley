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
            self.assertEqual(r.returncode, 0); self.assertEqual((Path(d) / "t.html").read_text().count("font-weight=\"700\""), 3)   # title + 2 tiles
    def test_chart_default_style_groups_targets_and_money_pattern(self):
        """The style the first user approved: portrait, paper, one colour per group with a legend, dashed targets, $750M not 750 $M."""
        with tempfile.TemporaryDirectory() as d:
            csv = Path(d) / "d.csv"; csv.write_text("name,value,group,status\nBig,750,Physical,\nMid,425,Enterprise,\nOut,5000,Enterprise,target\nSmall,4.1,Health,\n")
            out = Path(d) / "c.png"
            r = subprocess.run([sys.executable, str(ROOT / "skills/stanley/scripts/stanley-chart"), str(csv), "--title", "Top 4", "--unit", "${}M", "--source", "x", "--asof", "Data as of Nov 8", "--out", str(out)], capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr); html = out.with_suffix(".html").read_text()
            self.assertIn('width="1080" height="1350"', html); self.assertIn("#F3F0E8", html); self.assertIn("$750M", html); self.assertNotIn("750 $M", html)
            self.assertIn("stroke-dasharray", html)                       # the target row
            for g in ("Physical", "Enterprise", "Health"): self.assertIn(f">{g}<", html)   # legend
            self.assertIn("Small boxes: Small $4.1M", html); self.assertIn("Data as of Nov 8", html); self.assertNotIn("monospace", html)

class TraceTests(unittest.TestCase):
    def run_trace(self, d, *files, claims=None):
        args = [sys.executable, str(ROOT / "skills/stanley/scripts/stanley-trace"), "--data", str(d / "data.csv")] + (["--claims", str(claims)] if claims else []) + [str(d / f) for f in files]
        return subprocess.run(args, capture_output=True, text=True)
    def test_every_number_traces_or_fails(self):
        """The Toronto atlas post needed four rounds of checks by eye; the script refuses any number it cannot trace."""
        with tempfile.TemporaryDirectory() as t:
            d = Path(t); (d / "data.csv").write_text("name,value\nCohere,5000\nWaabi,750\nBeacon,425\nBiossil,196\n")
            (d / "post.md").write_text("Top 4 Toronto AI startups in 2026. Waabi leads with $750M, Beacon has $425M, Biossil $196M. Without Cohere the other 3 raised $1.37B. Cohere targets C$7B, about 3.6 times the rest. Biossil is valued at $1B. Data as of Nov 8, 2026.\n")
            r = self.run_trace(d, "post.md"); self.assertEqual(r.returncode, 1)
            for bad in ("C$7B", "3.6 times", "$1B"): self.assertIn(bad, r.stdout)
            for good in ("$750M", "$1.37B", "Nov 8", "2026"): self.assertNotIn("untraced: post.md: " + good, r.stdout)
            (d / "claims.csv").write_text('claim,value,url,quote\ntarget,7,https://e.com/a,"targeting CAD 7 billion"\nratio,3.6,computed,"5000 / (sum(d.values()) - d[\'Cohere\'])"\nvaluation,1,https://e.com/b,"at a $1 billion valuation"\n')
            r = self.run_trace(d, "post.md", claims=d / "claims.csv"); self.assertEqual(r.returncode, 0, r.stdout); self.assertIn("PASS", r.stdout)
            (d / "claims.csv").write_text('claim,value,url,quote\ntarget,7,https://e.com/a,"targeting a big round"\n')
            r = self.run_trace(d, "post.md", claims=d / "claims.csv"); self.assertIn("not in the quoted sentence", r.stdout)
