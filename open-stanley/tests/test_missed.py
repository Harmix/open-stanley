import json, os, subprocess, sys, tempfile, datetime as dt, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
SV = ROOT / "skills/stanley/scripts/stanley-vault"

class MissedTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(); self.v = Path(self.tmp)
        (self.v / "ledger").mkdir()
        (self.v / "my-human.md").write_text(
            "- Time zone and posting window: UTC\n"
            "- schedule: soapbox=daily 00:00; mine=weekly sat 00:00; monthly=monthly 1 00:00\n"
            "- catch_up: mine, monthly\n", encoding="utf-8")
        self.env = dict(os.environ, STANLEY_VAULT=str(self.v))

    def run_missed(self, *args):
        return subprocess.run([sys.executable, str(SV), "missed", *args], env=self.env, capture_output=True, text=True)

    def test_reports_missed_and_catch_up_flag(self):
        r = self.run_missed("--json")
        rows = {x["job"]: x for x in json.loads(r.stdout)}
        self.assertIn("soapbox", rows); self.assertFalse(rows["soapbox"]["catch_up"])
        self.assertIn("mine", rows); self.assertTrue(rows["mine"]["catch_up"])
        self.assertEqual(r.returncode, 1)

    def test_run_clears_it(self):
        today = dt.datetime.now(dt.timezone.utc).replace(hour=0, minute=1).isoformat(timespec="seconds")
        with (self.v / "ledger/runs.jsonl").open("a") as f:
            f.write(json.dumps({"id": "a", "job": "soapbox", "started": today}) + "\n")
        rows = {x["job"] for x in json.loads(self.run_missed("--json").stdout)}
        self.assertNotIn("soapbox", rows)

    def test_superseded_miss_is_not_reported(self):
        # a daily job whose miss is older than one period is dropped, not caught up
        (self.v / "my-human.md").write_text(
            "- Time zone and posting window: UTC\n"
            "- schedule: soapbox=daily 23:59\n"
            "- catch_up: soapbox\n", encoding="utf-8")
        rows = json.loads(self.run_missed("--json").stdout)
        self.assertTrue(all(r["hours_ago"] <= 24 for r in rows), rows)

    def test_brief_names_only_catch_up_jobs(self):
        r = self.run_missed("--brief")
        self.assertIn("mine", r.stdout); self.assertNotIn("soapbox", r.stdout)

if __name__ == "__main__":
    unittest.main()
