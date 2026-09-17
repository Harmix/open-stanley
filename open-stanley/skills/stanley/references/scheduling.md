# Scheduling the rituals

Two modes. Pick one at onboarding and write it into `my-human.md` as `mode: laptop|cloud`.

## Laptop mode (default)

Every job runs **on the user's own computer** with the vault as a plain folder (ideally inside a desktop-synced Drive/iCloud/Dropbox folder), the user's MCPs, and their browser (Claude in Chrome), so each run does its own LinkedIn/X reading; there is no queue and no drain. Which scheduler you get depends on the surface, and the two behave differently when the laptop is closed:

**Cowork → cloud routine bound to the computer** (option B below). Cowork's Scheduled tab has no local scheduler; this is the path for Cowork users and what this plugin was built on.

**Claude Code Desktop → local routine** (option A). **Code** tab → Routines → New routine → **Local**, working folder = the vault, permission mode set to auto-approve after the first "Run now" (click "always allow" on each prompt). Needs Desktop 1.1.5368 or newer. Prompt = `templates/scheduled-tasks/<job>.md` with `_preamble-local.md`. This runs on the machine itself, so the plugin is visible at `${CLAUDE_PLUGIN_ROOT}` and the vault is the working folder: no `.stanley-scripts/` install, no mount paths. Documented behaviour (code.claude.com/docs/en/desktop-scheduled-tasks): a run that comes due while the computer sleeps is *skipped*, not switched off; "when the app starts or your computer wakes, Desktop checks whether each task missed any runs in the last seven days. If it did, Desktop starts exactly one catch-up run for the most recently missed time"; skipped runs show in the task's history with the reason; and Settings → Desktop app → General → **Keep computer awake** prevents idle-sleep (a closed lid still sleeps). The plugin's own `missed` step still runs inside each job for jobs that Desktop's one-catch-up rule leaves behind. No watchdog needed. Not available from Cowork.

**B. Cloud routine bound to the computer** (Cowork → Scheduled → "Require this computer" + "Work in a folder"). The Cowork path. The run reaches the vault only through a mount (`$HOME/mnt/<folder>`), cannot see the plugin (hence `.stanley-scripts/`), and — the important part — a task that comes due while the computer is offline is **switched off** (`suspension_reason: device_absent`) and never switched back on; a fire from the cloud runs it without the computer. Run it with the watchdog and the self-repair step below; together they cover the switch-off, though not a same-morning catch-up. Prompt = `_preamble-laptop.md`.

Cost either way: runs happen only while the computer is awake. Fine for people whose laptop is open during the day; wrong for people who need runs with the laptop closed for days — that is cloud mode.

Concurrency: tasks that overlap append to the same jsonl files; appends are line-atomic, nothing to merge. Desktop local routines are additionally serialised (a run is skipped if another scheduled task is still running), so keep the 22:00 scout and recap a few minutes apart.

## Cloud mode

Tasks run in Anthropic's cloud without "Require this computer". They have the user's MCPs but no browser and no local folders, so:

- the vault must be reachable through an MCP: a folder in the Google Drive the Drive MCP sees (`drive` backend, mirror procedure in `vault-backends.md`; one MCP call per file, so pull only the job's files and issue the calls in one turn), or Notion;
- browser-only work (LinkedIn reads, comments, analytics, X replies) is parked in `ledger/local-queue.jsonl` with an expiry and worked by the `drain` task, which does require the computer.

Git is not a cloud-mode option in Cowork today: scheduled tasks have no repository field, and the cloud git proxy only injects a credential for repos listed as a session's source, so a private repo cannot be cloned from a scheduled run. Git remains fine for Claude Code users who run the jobs from their own machine or CI (`vault-backends.md`).

## Setting up

**Claude Code Desktop, local routine (A):** Code tab → Routines → New routine → Local; name, instructions from the template with `_preamble-local.md`, model, schedule preset (ask Claude in a Desktop session for the 1st-of-month or 22:00 variants), working folder = the vault, permission mode auto-approve, then Run now once and always-allow the prompts.

**Cowork, cloud routine bound to the computer (B):** Sidebar → Scheduled → New: name, prompt (from `templates/scheduled-tasks/<job>.md` with the mode's preamble), model, frequency, **Permissions: Automatically approve** (otherwise each file write asks), and for laptop mode the computer toggle plus the vault folder. A task created from a chat session inherits that session's model; set it explicitly (see below). Each run is its own session with the user's connectors and installed plugins.

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
