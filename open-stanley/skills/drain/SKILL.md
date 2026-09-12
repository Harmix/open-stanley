---
name: drain
description: Work through the local queue that cloud scheduled runs left for this machine — LinkedIn comments to post, LinkedIn feed scans, analytics pulls, posts approved for publishing — using this computer's logged-in browser, then mark each item done or expired and report. Use when a session starts with queued items, when the user says "catch up", "run the queue", "post what's pending", or when the launchd/cron drain job fires. Runs only on a machine with a browser.
---

# Drain the local queue

**Cloud mode only.** In laptop mode (the default) every job runs with the browser and nothing is queued, so this skill has nothing to do; `queue-check` prints nothing and that is the normal outcome. In cloud mode, scheduled runs can reach your MCPs but not your browser, so anything that needs LinkedIn's UI or an X reply box is parked in `ledger/local-queue.jsonl` with an expiry. This skill is the worker. It runs whenever the laptop is online: from the `SessionStart` hook (it tells you at the top of any session that items are waiting), from the launchd job in `templates/launchd/` inside your window, or when you ask.

## 1. Read the queue

`skills/stanley/scripts/stanley-vault queue-check` prints pending, unexpired items as JSON lines and marks expired ones. If the vault is on Google Drive, `sync` first so you see what the cloud wrote. Group by job type and do the oldest first.

## 2. Job types and what to do

| `job` | payload | action |
|---|---|---|
| `comment` | platform, url, text, author | Open the post, confirm it still exists and the author is not the user, post `text` exactly, `comment-add`, `surfaced-add` |
| `publish` | platform, draft path or text, assets, schedule time | Follow `/open-stanley:publish`; if the scheduled time has passed by more than 2h, ask before posting |
| `scan` | platform, lanes, since | Follow `/open-stanley:scout` steps 1–5 for that platform only; results go to the user through `notify` and to `surfaced.jsonl` |
| `analytics` | post urls | Pull metrics via the browser, `metrics-add` for each |
| `study` | creator handle | Follow `/open-stanley:study` |

Items whose payload references a URL that no longer exists, or whose target is older than the expiry, are marked `--failed` with the reason. Never post a comment on a stale thread just because it was queued.

## 3. Close each item

`skills/stanley/scripts/stanley-vault queue-done <id> --result "<one line>"` or `--failed`. Then `sync`.

## 4. Report

One message: what was done (with URLs), what failed and why, what's still pending and when it expires. Keep it under eight lines. This message is what the next cloud recap reads, so it must be in the vault (`runs.jsonl` via `run-start`/`run-end`) as well as in chat.
