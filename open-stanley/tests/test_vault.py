import json, subprocess, sys, tempfile, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
V = ROOT / "skills/stanley/scripts/stanley-vault"

def vault(*args, cwd=None, inp=None):
    return subprocess.run([sys.executable, str(V), *args], capture_output=True, text=True, cwd=cwd, input=inp)

class VaultTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.d = Path(self.tmp.name) / "v"
        r = vault("init", str(self.d), "--no-git"); self.assertEqual(r.returncode, 0, r.stderr)
        (self.d / "my-human.md").write_text("- Handles: linkedin.com/in/someone · x.com/some_one\n")
    def tearDown(self): self.tmp.cleanup()
    def v(self, *a): return vault("--vault", str(self.d), *a)
    def test_init_creates_template(self):
        for f in ["strategy.md", "voice.md", "stories/_TEMPLATE.md", "ledger", "learn/rules.md"]:
            self.assertTrue((self.d / f).exists(), f)
    def test_surfaced_dedupe_normalizes_urls(self):
        self.assertEqual(self.v("surfaced-add", "https://x.com/a/status/1", "--platform", "x").returncode, 0)
        r = self.v("surfaced-check", "https://www.x.com/a/status/1/?s=20", "https://x.com/b/status/2")
        self.assertEqual(r.returncode, 1); self.assertIn("status/1", r.stdout); self.assertNotIn("status/2", r.stdout)
    def test_is_self(self):
        self.assertEqual(self.v("is-self", "https://www.linkedin.com/in/someone/").returncode, 0)
        self.assertEqual(self.v("is-self", "@some_one").returncode, 0)
        self.assertEqual(self.v("is-self", "@stranger").returncode, 1)
    def test_run_records(self):
        rid = self.v("run-start", "scout", "--promised", "3 picks").stdout.strip()
        self.assertEqual(self.v("run-end", rid, "--delivered", "2").returncode, 0)
        lines = (self.d / "ledger/runs.jsonl").read_text().splitlines()
        self.assertEqual(len(lines), 2); self.assertEqual(json.loads(lines[1])["id"], rid)
    def test_post_add_and_metrics(self):
        f = self.d / "final.txt"; f.write_text("Hook line here.\nBody.")
        r = self.v("post-add", "--platform", "linkedin", "--url", "https://l/1", "--text-file", str(f), "--lane", "founder", "--shape", "opener:event", "--experiment", "number-in-hook=without")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(self.v("metrics-add", "--url", "https://l/1", "--bucket", "24h", "--reactions", "5", "--comments", "2").returncode, 0)
        row = json.loads((self.d / "ledger/posts.jsonl").read_text().splitlines()[0])
        self.assertEqual(row["lane"], "founder"); self.assertEqual(row["shape"]["opener"], "event")
        self.assertEqual(row["metrics"]["24h"]["reactions"], 5); self.assertEqual(row["experiment"]["number-in-hook"], "without")
    def test_stories_index_skips_template(self):
        (self.d / "stories/one.md").write_text("---\ntopic: memory\nlesson: L\nstatus: fresh\nsource: chat:2026-09-01\n---\nbody\n")
        self.assertEqual(self.v("stories-index").returncode, 0)
        idx = (self.d / "stories/index.md").read_text()
        self.assertIn("[one](one.md)", idx); self.assertNotIn("_TEMPLATE", idx)

if __name__ == "__main__":
    unittest.main()

class SyncMergeTests(unittest.TestCase):
    def test_concurrent_runs_merge_jsonl(self):
        import tempfile
        with tempfile.TemporaryDirectory() as t:
            t = Path(t); run = lambda *a, **k: subprocess.run(a, cwd=k.get("cwd", t), check=True, capture_output=True, text=True)
            run("git", "init", "-q", "--bare", "-b", "main", "origin.git")
            run("git", "init", "-q", "-b", "main", "seed"); (t / "seed/ledger").mkdir(); (t / "seed/ledger/runs.jsonl").write_text('{"id":"base"}\n')
            run("git", "-c", "user.name=t", "-c", "user.email=t@t", "-C", "seed", "add", "-A"); run("git", "-c", "user.name=t", "-c", "user.email=t@t", "-C", "seed", "commit", "-qm", "base")
            run("git", "-C", "seed", "remote", "add", "origin", str(t / "origin.git")); run("git", "-C", "seed", "push", "-q", "-u", "origin", "main")
            run("git", "clone", "-q", str(t / "origin.git"), "a"); run("git", "clone", "-q", str(t / "origin.git"), "b")
            with open(t / "a/ledger/runs.jsonl", "a") as f: f.write('{"id":"a1"}\n')
            with open(t / "b/ledger/runs.jsonl", "a") as f: f.write('{"id":"b1"}\n')
            for d in ("a", "b"):
                r = subprocess.run([sys.executable, str(V), "--vault", str(t / d), "sync"], capture_output=True, text=True)
                self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            self.assertIn("merged ledger/runs.jsonl", r.stdout)
            lines = (t / "b/ledger/runs.jsonl").read_text().splitlines()
            self.assertEqual(sorted(lines), sorted(['{"id":"base"}', '{"id":"a1"}', '{"id":"b1"}']))
