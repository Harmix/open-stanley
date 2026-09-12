import json, subprocess, sys, tempfile, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
V = ROOT / "skills/stanley/scripts/stanley-vault"
def v(d, *a): return subprocess.run([sys.executable, str(V), "--vault", str(d), *a], capture_output=True, text=True)
class QueueTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.d = Path(self.tmp.name) / "v"
        subprocess.run([sys.executable, str(V), "init", str(self.d), "--no-git"], capture_output=True)
    def tearDown(self): self.tmp.cleanup()
    def test_add_check_done_expire(self):
        self.assertEqual(v(self.d, "queue-check").returncode, 0)
        qid = v(self.d, "queue-add", "--job", "comment", "--payload", json.dumps({"url": "u", "text": "t"})).stdout.strip()
        v(self.d, "queue-add", "--job", "scan", "--payload", "{}", "--expires-hours", "0")
        r = v(self.d, "queue-check"); self.assertEqual(r.returncode, 1)
        pend = [json.loads(l) for l in r.stdout.splitlines()]
        self.assertEqual([p["id"] for p in pend], [qid])
        r = v(self.d, "queue-check", "--brief"); self.assertIn("1 queued", r.stdout)
        self.assertEqual(v(self.d, "queue-done", qid, "--result", "posted").returncode, 0)
        self.assertEqual(v(self.d, "queue-check").returncode, 0)
        rows = [json.loads(l) for l in (self.d / "ledger/local-queue.jsonl").read_text().splitlines()]
        self.assertTrue(any(r.get("status") == "expired" for r in rows)); self.assertTrue(any(r.get("status") == "done" for r in rows))
    def test_vault_template_has_overrides_dir(self):
        self.assertTrue((self.d / "skills/README.md").exists())
if __name__ == "__main__": unittest.main()

class SnapshotTests(unittest.TestCase):
    def test_snapshot_and_changed(self):
        with tempfile.TemporaryDirectory() as t:
            d = Path(t) / "v"; subprocess.run([sys.executable, str(V), "init", str(d), "--no-git"], capture_output=True)
            self.assertEqual(v(d, "snapshot").returncode, 0)
            self.assertEqual(v(d, "changed").returncode, 0)
            (d / "voice.md").write_text("changed"); (d / "stories/new.md").write_text("x"); (d / "instructions.md").unlink()
            r = v(d, "changed"); self.assertEqual(r.returncode, 0)
            self.assertIn("changed  voice.md", r.stdout); self.assertIn("added    stories/new.md", r.stdout); self.assertIn("deleted  instructions.md", r.stdout)
