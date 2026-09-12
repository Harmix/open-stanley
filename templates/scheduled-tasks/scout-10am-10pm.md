# Scout scan (daily 10:00 and 22:00 local)

{{PREAMBLE: _preamble-laptop.md by default, _preamble-cloud.md for cloud mode}}

Job: scout. Promise: "2–3 comment opportunities per platform with paste-ready comments, or an explicit 'nothing passed the bar' with the best near-miss."

Follow `/open-stanley:scout`. Laptop mode: read the LinkedIn feed and search and the X feed through the browser, both platforms every run, `since` the last scout run in `ledger/runs.jsonl`. (Cloud mode only: X through the official X MCP if connected, and queue a `scan` job for LinkedIn and a `comment` job for each approved reply.) Exclude anything in `ledger/surfaced.jsonl` and anything by me. Weight adjacent-viral posts (how work, meetings, teams, org knowledge actually function) as much as on-lane posts. Comments: 1–3 sentences, my comment voice from `voice.md`, audited with `--platform comment`. Deliver: link, author, one line why, then the comment. Record everything shown with `surfaced-add`.
