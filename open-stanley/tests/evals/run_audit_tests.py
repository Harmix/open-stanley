#!/usr/bin/env python3
"""Run the deterministic audit tests in tests/evals/evals.json. Exit 1 on any failure."""
import json, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
tests = json.loads((ROOT / "tests/evals/evals.json").read_text())["audit_tests"]
fails = 0
for t in tests:
    f = ROOT / "tests/evals" / t["file"]
    if not f.exists():
        if t.get("optional"): print(f"skip  {t['file']} (missing)"); continue
        print(f"FAIL  {t['file']} missing"); fails += 1; continue
    r = subprocess.run([sys.executable, str(ROOT / "skills/stanley/scripts/stanley-audit"), str(f), "--platform", t["platform"], "--json"], capture_output=True, text=True)
    j = json.loads(r.stdout)
    fired = {x["rule"] for x in j["findings"]}
    ok = (j["pass"] == (t["expect"] == "PASS"))
    missing = [r_ for r_ in t.get("must_fire", []) if r_ not in fired]
    wrong = [r_ for r_ in t.get("must_not_fire", []) if r_ in fired]
    ok = ok and not missing and not wrong
    print(("ok    " if ok else "FAIL  ") + t["file"] + (f"  missing={missing}" if missing else "") + (f"  wrong={wrong}" if wrong else "") + f"  result={'PASS' if j['pass'] else 'BLOCK'}")
    fails += 0 if ok else 1
print(f"{len(tests)-fails}/{len(tests)} passed"); sys.exit(1 if fails else 0)
