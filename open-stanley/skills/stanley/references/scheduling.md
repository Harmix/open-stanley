# Scheduling the rituals

Two modes. Pick one at onboarding and write it into `my-human.md` as `mode: laptop|cloud`.

## Laptop mode (default)

Every scheduled task runs **on the user's own computer** (Cowork: Scheduled → task → "Require this computer" on, and "Work in a folder" = the vault folder). The vault is a plain folder, ideally inside a desktop-synced Google Drive / iCloud / Dropbox folder so it is backed up and readable elsewhere. Each run has the user's MCPs, the vault as files, **and their browser** (Claude in Chrome), so every job does its own LinkedIn/X reading and analytics; there is no queue and no drain.

Cost: runs fire only while the computer is awake. Cowork shows "Only runs while your computer is awake"; a task that fires with the lid closed is missed, not caught up. Fine for people whose laptop is open during the day (set the daily jobs inside that window); wrong for people who need runs with the laptop closed for days. Keep the Mac from sleeping on power if 08:00 matters.

Missed runs. A device-bound task that comes due while the computer is asleep or offline is not skipped: Cowork switches it **off** (`suspension_reason: device_absent`) and moves its next run to the following occurrence, and nothing switches it back on. Seen twice in September 2026: once a Saturday job, once the morning Soapbox and Scout together, which then also missed the next day until the user noticed. Three layers, all needed:

1. **A cloud watchdog** (`templates/scheduled-tasks/watchdog-daily.md`): the one Open Stanley task with "Require this computer" *off*, so it always fires. Twice a day it lists the tasks and re-enables any suspended ones. It must not fire them: a `fire_trigger` from the cloud runs a device-bound task without the computer (`no_signed_approval`, observed 17 Sep 2026), which cannot reach the vault or the browser. The re-enabled task fires at its next scheduled time on the computer, and that run's `missed` step does the catch-up. Without it, a day offline can leave every task switched off with no run left to notice. Suggested times: 07:30 (repairs anything suspended overnight before the morning jobs) and 12:00 (repairs the morning jobs before the evening ones). Sonnet; it finishes in under a minute.
2. **Self-repair in every laptop run**: the laptop preamble lists the tasks after `run-start` and re-enables any suspended sibling, so the first run that does fire fixes the rest.
3. **Catch-up inside a run**: `my-human.md` carries the schedule (`- schedule: mine=weekly sat 18:00; ...`, local time) and `- catch_up:` — which jobs are worth running late. A bare name means always (recap, weekly drafts, mine, monthly); `name<6h` means only if fewer than 6 hours late, which is right for soapbox and scout: a morning question at noon still works, at 23:00 it is noise. `stanley-vault missed` compares the schedule with `ledger/runs.jsonl`; every laptop run does one overdue catch-up job after its own. A miss older than one period of that job (daily 24h, weekly 7d, monthly 30d) is superseded, not caught up; the first time a job is added to `schedule:` its last occurrence looks missed once, harmlessly.

On "catch up" in a chat: run `missed`; with the Claude Code Remote MCP connected, re-enable any suspended task as the watchdog does, then do the overdue jobs in the current session from their templates (a fire from a chat may run cloud-only, like the watchdog's). Without the MCP, do the jobs here and tell the user to re-enable the tasks in Scheduled.

Keep the computer awake when it matters (System Settings → Battery → prevent sleeping on power, or `caffeinate`), and put weekly jobs at hours the laptop is normally open.

Concurrency: tasks that overlap append to the same jsonl files; appends are line-atomic, nothing to merge.

Scripts: the device shell cannot see the plugin, so the bundled scripts are installed once into `<vault>/.stanley-scripts/` (with a `VERSION` file) and re-installed only when the plugin version changes; the `stanley` skill, step 1a, has the exact commands. The first run of a new version costs one extra minute; every later run costs nothing. `.stanley-scripts/` is in the vault's `.gitignore` and is safe to delete.

Queue: `ledger/local-queue.jsonl` is unused in laptop mode. If a vault carries pending items from an earlier cloud-mode run, the next laptop run does them as part of its own work when they fit the job, otherwise `queue-done <id> --result "laptop mode: superseded"`.

## Cloud mode

Tasks run in Anthropic's cloud without "Require this computer". They have the user's MCPs but no browser and no local folders, so:

- the vault must be reachable through an MCP: a folder in the Google Drive the Drive MCP sees (`drive` backend, mirror procedure in `vault-backends.md`; one MCP call per file, so pull only the job's files and issue the calls in one turn), or Notion;
- browser-only work (LinkedIn reads, comments, analytics, X replies) is parked in `ledger/local-queue.jsonl` with an expiry and worked by the `drain` task, which does require the computer.

Git is not a cloud-mode option in Cowork today: scheduled tasks have no repository field, and the cloud git proxy only injects a credential for repos listed as a session's source, so a private repo cannot be cloned from a scheduled run. Git remains fine for Claude Code users who run the jobs from their own machine or CI (`vault-backends.md`).

## Setting up in Cowork

Sidebar → Scheduled → New: name, prompt (from `templates/scheduled-tasks/<job>.md` with the mode's preamble), model, frequency, **Permissions: Automatically approve** (otherwise each file write asks), and for laptop mode the computer toggle plus the vault folder. A task created from a chat session inherits that session's model; set it explicitly (see below). Each run is its own session with the user's connectors and installed plugins.

**Claude Code → Routines** (`/schedule`): same prompts; laptop mode is the natural fit there too.

Every template starts with the mode's preamble: find the vault, probe capabilities, `run-start`, `stanley-audit selftest`, do the job, `run-end` with `--shown/--queued/--browser`, deliver the result in the session output (or via the user's `notify` capability). The delivered message says what it looked at and what it found even when the answer is "nothing".

Times are the user's local time; Cowork takes local times, `create_trigger` takes UTC cron. Defaults (from `strategy.md`): soapbox 08:00, scout 10:00 and 22:00, recap 22:00, mine Saturday 18:00, weekly drafts Sunday 10:00, orbit + strategy check-in on the 1st, and the cloud watchdog at 07:30 and 12:00 (the only task without "Require this computer").

## The cadence ladder

Each rung reads a signal that actually accumulates at that frequency. Putting a question on the wrong rung is how a content loop stops improving: ask "is this shape working" weekly and you are reading noise, ask "what did the user cut from my draft" monthly and you have thrown away three weeks of the clearest feedback there is.

| Rung | Job | Reads | Produces |
|---|---|---|---|
| Continuously | every run | the user's corrections, in the moment they are made | a diff and a standing instruction the next draft reads |
| Daily | soapbox, scout, recap | today's feed, today's numbers, open threads on both sides | material, comments, a reaction |
| Weekly | mine (Sat) → tune + drafts (Sun) | the week's meetings; then repeated corrections and the experiment's arms | stories, then promoted rules, then three posts |
| Monthly | orbit + strategy check-in | 30 days of metrics, who kept showing up, one creator studied from outside | one strategy change, a verdict, one new format to test |

The learning is not concentrated in one job: corrections apply immediately, the weekly run promotes what recurred, and the monthly is where a change to the strategy itself gets proposed. Nothing waits a month to be noticed.

## Which model runs each job

The skills carry the judgment; the runs mostly execute them.

| Job | Model | Why |
|---|---|---|
| soapbox, scout (both), recap, mine, monthly, drain, watchdog | Sonnet | reading, linting, one short message; no writing in the user's voice |
| weekly drafts, longform | Opus | writes in the user's voice and runs the critic and fact-checker |

Change it per task in Scheduled → task → model. Model ids accepted in September 2026: `claude-sonnet-5`, `claude-opus-5`.
