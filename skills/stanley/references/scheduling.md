# Scheduling the rituals

Two modes. Pick one at onboarding and write it into `my-human.md` as `mode: laptop|cloud`.

## Laptop mode (default)

Every scheduled task runs **on the user's own computer** (Cowork: Scheduled → task → "Require this computer" on, and "Work in a folder" = the vault folder). The vault is a plain folder, ideally inside a desktop-synced Google Drive / iCloud / Dropbox folder so it is backed up and readable elsewhere. Each run has the user's MCPs, the vault as files, **and their browser** (Claude in Chrome), so every job does its own LinkedIn/X reading and analytics; there is no queue and no drain.

Cost: runs fire only while the computer is awake. Cowork shows "Only runs while your computer is awake"; a task that fires with the lid closed is missed, not caught up. Fine for people whose laptop is open during the day (set the daily jobs inside that window); wrong for people who need runs with the laptop closed for days. Keep the Mac from sleeping on power if 08:00 matters.

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

Times are the user's local time; Cowork takes local times, `create_trigger` takes UTC cron. Defaults (from `strategy.md`): soapbox 08:00, scout 10:00 and 22:00, recap 22:00, weekly drafts Sunday 10:00, mine Saturday 18:00, orbit + strategy check-in on the 1st.

## Which model runs each job

The skills carry the judgment; the runs mostly execute them.

| Job | Model | Why |
|---|---|---|
| soapbox, scout (both), recap, mine, monthly, drain | Sonnet | reading, linting, one short message; no writing in the user's voice |
| weekly drafts | Opus | writes three posts in the user's voice and runs the critic and fact-checker on them |

Change it per task in Scheduled → task → model. Model ids accepted in September 2026: `claude-sonnet-5`, `claude-opus-5`.
