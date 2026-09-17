# Changelog

All notable changes to this plugin. Versions follow semver: MAJOR for a change that breaks the vault format or a skill's contract, MINOR for a new skill/script/rule set, PATCH for rule tweaks and fixes. Users only receive updates when `version` in `.claude-plugin/plugin.json` is bumped; the marketplace entry and this file must carry the same number (enforced by `tests/test_plugin_structure.py`).

## 0.9.2 — 2026-09-17

The right scheduler for laptop mode was in the docs all along: Claude Desktop's **local routines** (Code tab → Routines → New routine → Local) run on the machine, skip cleanly when it sleeps, and "start exactly one catch-up run for the most recently missed time" when it wakes; skipped runs are listed with their reason, and Settings has "Keep computer awake". The cloud routines with "Require this computer" that 0.6–0.9.1 ran on are a different thing: they get switched off when the computer is absent, need the watchdog, and cannot see the plugin. Laptop mode now documents both (A local, recommended; B cloud-bound, with watchdog), `templates/scheduled-tasks/_preamble-local.md` is the preamble for A (vault = working folder, scripts from `${CLAUDE_PLUGIN_ROOT}`, no `.stanley-scripts/`), and `stanley-vault` resolves the vault to the current folder when `my-human.md` is there.

## 0.9.1 — 2026-09-17

Second time a day offline took tasks out: the morning Soapbox and Scout came due with the laptop closed, Cowork switched both off (`device_absent`), and they stayed off until the user found them. The 0.7.0 catch-up only helps when some run fires, and a switched-off task never fires. Three layers now (`scheduling.md`, Missed runs): a **cloud watchdog** task with "Require this computer" off — the only one — that runs twice a day, re-enables any suspended Open Stanley task (`templates/scheduled-tasks/watchdog-daily.md`; it never fires them, because a fire from the cloud runs a device-bound task without the computer); **self-repair** in every laptop run, which re-enables suspended siblings right after `run-start`; and per-job catch-up windows in `my-human.md` (`soapbox<6h, scout<6h`: a morning question at noon still works, at 23:00 it is noise). `stanley-vault missed` reads the windows.

## 0.9.0 — 2026-09-14

**Platform access.** New `skills/stanley/references/platform-access.md`. The order is: an MCP the user already has connected, else the browser. The browser is not a compromise at this volume — a post a day and a few comments is a person using their own account — and the plugin never sends someone to register a developer app before it will work. What carries risk is volume, velocity and repetition, so the pacing discipline attaches to the scout's scanning (the highest-volume thing here) rather than to posting, and bulk messaging is ruled out entirely. The official surfaces are documented for the one-line answer when someone hits a limit: LinkedIn's self-serve `w_member_social`, X's hosted MCP at `api.x.com/mcp`. `publish` no longer claims "LinkedIn has no public posting API for individuals", which was false. The 13 Sep X suspension, a day after a four-tweet thread went out in about two minutes, is recorded as a data point with an unknown cause; the lesson taken is to space a thread, not to distrust the browser.

**Experiments read themselves.** `strategy.md` had two experiments declared with `min_n: 4` and 2 of 28 posts carried an arm tag, because anything published outside the write→publish path never got tagged. Where an experiment's variants are an observable property of the text — the experiment name is a hook feature, or `classify:` names one — `stanley-stats` now classifies every untagged post from its text (manual tags still win). On the first vault this filled both arms from history immediately and retired a hypothesis: number-in-hook posts run a median 28 against 30 without, i.e. no effect. The other experiment turned out to be 26 posts against 1, which is not a close race but an unbalanced arm, and is now reported as such.

**Tune, inside the Sunday run.** Corrections already apply the moment they are made — the diff and any standing instruction are filed in-session and the next draft reads them — so this is not a new scheduled job. What was missing is the step the vault's own design names: `learn/rules.md` says candidates live in `diffs.jsonl` until confirmed, and nothing promoted them. The weekly-drafts run now opens by promoting anything that recurred twice, retiring any rule overridden twice, and reporting the experiment's arms — including writing into a starving arm so it fills. The monthly gains a **format gap** step: from the creators studied that month, propose one format the user has never tried as the next experiment. The plugin is supposed to find new formats by watching what works and testing it, not by adopting whatever was mentioned in passing.

**Longform.** New `longform` skill — a teardown, field report or build log built from an evidence ledger where every line carries a receipt, then cut into 4–6 posts, comment angles and a soapbox question. Each shape has an entry condition checked against `stories/` first, so a thin piece is refused rather than padded. It is a format the plugin can execute when the user asks or the strategy loop picks it, not a scheduled ritual. `stanley-audit --platform longform` adds word-band, receipt-density, listicle and summary-box checks. Prior art: the teardown skill at `github.com/MisreadableMind/human-writing-skill`.

**Also:** `stanley-vault missed` treats a miss older than one period of the job (daily 24h, weekly 7d, monthly 30d) as superseded rather than a catch-up.

## 0.8.0 — 2026-09-14

From the first real recap. (1) Recap now checks both sides of every conversation: comments on the user's posts *and* replies under comments the user left on other people's posts (ledger plus the profile's comments page), and drafts a paste-ready response for anything substantive, never posting without a yes. The first recap only looked at the user's own posts and a founder's reply sat unanswered for a day. (2) A reply is a conversation, not a post: the first draft opened with a benchmark number and a question; the user rewrote it as "yeah, fascinating area, we're trying X, want to hop on a call?". That register is now the rule (recap skill, `voice.md` template gets a *Reply voice* block, scout notes the difference from a first comment). (3) `stanley-stats` marks lifts with fewer than 3 posts as `n<3: not a signal` and recap must not call a shape the user's worst on one post; the first recap did exactly that ("lift 0.23, one prior post").

## 0.7.2 — 2026-09-13

A weekly-drafts run (Opus, marketplace install) produced three good drafts with the plugin's own fact-checker agent and then told the user the plugin was not installed, because `ListPlugins` does not list marketplace plugins and a skill search returned nothing. The `stanley` skill now says so (step 1c): if this file loaded, the plugin is installed; load the other skills by exact `open-stanley:<name>` id, fall back to reading `${CLAUDE_PLUGIN_ROOT}/skills/<name>/SKILL.md`, and never report the plugin missing from inside it. Both preambles name the skill ids.

## 0.7.1 — 2026-09-12

The repo is now a marketplace with the plugin in `open-stanley/` (Cowork's Add marketplace refused a plugin at the marketplace root; `source: "./open-stanley"` is the layout Anthropic's own marketplaces use). `dist/open-stanley.plugin` is gone: install from the marketplace in Cowork or Claude Code.

## 0.7.0 — 2026-09-12

Missed runs. The Saturday 18:00 mine job came due while the laptop was closed; Cowork switched the task off (`device_absent`) rather than running it later, which would also have silenced every following Saturday. New `stanley-vault missed` reads a `- schedule:` and `- catch_up:` line from `my-human.md`, compares with `ledger/runs.jsonl`, and lists what did not run. Every laptop-mode run does one overdue catch-up job after its own; the `SessionStart` hook prints "missed: mine" at the top of the next session; "catch up" in a chat re-enables the suspended task and fires it through the Claude Code Remote MCP when it is connected. `scheduling.md` has the procedure; the vault template carries the default schedule.

## 0.6.2 — 2026-09-12

Housekeeping after the hackathon push. README and manifest point at `Harmix/open-stanley`; the last "private repo" wording is gone (laptop mode is the story everywhere). The root is now ten entries: `RESEARCH.md`, `DESIGN.md`, `CONTRIBUTING.md` and `research/` moved under `docs/`, `evals/` under `tests/`, and `mcp/recommended.mcp.json` next to the reference that describes it. No behaviour change.

## 0.6.1 — 2026-09-12

From the first laptop-mode Scout run: the device shell cannot see the plugin, so the run spent three minutes searching for the scripts and then improvised a copy. Now the convention: scripts are installed into `<vault>/.stanley-scripts/` with a `VERSION` stamp, re-installed only when the plugin version changes, via one staged-file commit (never by reading the scripts into the conversation). `stanley` skill step 1a, the laptop preamble and `scheduling.md` say so; the vault template gains a `.gitignore` for it. Laptop runs also clear leftover cloud-mode queue items.



- **Two modes, laptop mode is the default.** The vault is a plain folder inside a desktop-synced Drive; scheduled tasks run on the user's computer with that folder and their browser, so every job does its own LinkedIn/X work and nothing is queued. Cloud mode (Drive/Notion mirror, queue, drain) stays for runs with the laptop closed.
- Git is no longer the default and is not offered to Cowork users: scheduled tasks have no repository field and the cloud git proxy refuses to inject a credential for a repo that is not a session source (tested; `403 not in this session's authorized repository set`). The git backend and `sync` remain for Claude Code / CI users.
- `sync` commit identity is `open-stanley@noreply.invalid`; the previous `stanley@users.noreply.github.com` was attributed by GitHub to a real user of that name.
- Templates: `_preamble-laptop.md` (default) and `_preamble-cloud.md`; job templates describe the laptop behaviour first. `my-human.md` gains `mode:` and `vault_path:`.



- **Default vault backend is now git** (a private GitHub repo). The Drive mirror cost one MCP call and one permission prompt per file, and three parallel runs on the first day left three copies of `runs.jsonl`. With git a run is one clone in and one `stanley-vault sync` out.
- `stanley-vault sync` handles concurrent runs: on a rebase conflict it unions `*.jsonl` lines (append-only ledgers lose nothing), lets the syncing run win for markdown, retries the push three times, and never force-pushes. It sets a commit identity if the session has none. Test added.
- Onboard asks for an empty private repo URL; `vault-backends.md`, the preamble, README and HOW-IT-WORKS describe git first and Drive/Notion as fallbacks.
- Setting up requires the Claude GitHub App (Settings → Claude Code → Connect GitHub) with access to the repo, and the repo added as a source on every scheduled task that touches the vault; the cloud git proxy only injects the credential for a session's listed repos. The docs say so, and say never to put a token in a prompt.



From the first scheduled Scout run:

- Docs referred to `ledger/queue.jsonl`; the file is `ledger/local-queue.jsonl`. Aligned.
- `stanley-vault run-end` takes `--shown N --queued N --browser yes|no` so `runs.jsonl` can tell a quiet run from a broken one without reading prose.
- `stanley-audit selftest` lints three bundled texts (a human comment, a slop comment, a slop post) so a fresh session can prove the linter works before drafting; runs are told to call it once.
- Speed: the preamble and `vault-backends.md` now say to issue all Drive downloads (and pushes) in one turn as parallel tool calls, and to pull only the job's files. Most of a run's wall time was sequential single-file MCP calls, not Drive itself.


From the first scheduled Soapbox run and the user's corrections to it:

- Soapbox never asks the human to put anything in the vault. They answer in the conversation; the ritual files the reply to `inbox/soapbox-<date>.md`, corrects the story when their account differs from the summary, and pushes.
- `mine`: a summary is a lead, not a receipt. Surprising claims from a summary ("the agent acted unprompted") get the transcript or `status: needs-confirmation` and a one-line question before they become a lesson. Mostly-private meetings are not skipped; the tellable lesson is taken and marked `anonymize`.
- Provenance: stories carry `origin: own | team | third-party | ai-suggested`; `write` credits AI-suggested ideas or angles on what the human did with them.
- `stanley-vault changed` now always exits 0 (it used to exit 1 when there were changes, which wrappers read as failure).
- Drive mirror: pull only the files the job needs; the full 18-file pull is for `mine` and weekly drafts.

 — 2026-09-12

- Moved `bin/` to `skills/stanley/scripts/`: claude.ai-hosted (Cowork) plugins may not ship a top-level `bin/` directory, so the package was refused at install. Every SKILL.md, the SessionStart hook, the launchd drain script, Makefile, CI and tests now point at the new path. `stanley-vault` honours `CLAUDE_PLUGIN_ROOT` when locating `vault-template/`.
- Onboard: read the LinkedIn creator analytics top-posts page (by impressions, then engagements) before the recent-activity feed; ask "which of your posts do you think did best?" and treat a mismatch as a missed read; report top-by-reach and top-by-pull separately; never quote a number not read from a page this session. Added `skills/onboard/references/onboarding-misses.md` with the first recorded miss.
- `stanley-stats`: prints "top by reach" alongside the engagement ranking and warns when they differ; shape lifts now use only the categorical axes (opener/body/ending, receipt yes/no, hashtags 0/1+) so free-text fields stop creating n=1 buckets.
- Test: fail if a top-level `bin/` reappears.

## 0.4.0 — 2026-09-12

- Vault backends made explicit (`skills/stanley/references/vault-backends.md`): `drive` (default for Cowork: the Drive the MCP sees, mirrored each run because the Drive MCP cannot edit in place), `git`, `notion`, `local`. `stanley-vault snapshot` / `changed` tell the skill which files to upload back.
- Documented that Claude Code inherits claude.ai connectors under subscription login, so the same plugin and the launchd drain see Pam/Drive/Slack; Cowork local scheduled task offered as the no-CLI alternative.
- Tests: +1.

## 0.3.0 — 2026-09-12

- Cloud/local split. Cloud scheduled runs (no browser) do MCP work and park browser-only work in `ledger/local-queue.jsonl` with expiries; `drain` skill + `SessionStart` hook + `templates/launchd/` (30-minute interval inside an 08:00–23:00 window; launchd re-fires missed jobs on wake) run it whenever the laptop is online.
- `stanley-vault queue-add / queue-check / queue-done`.
- Vault `skills/` folder for the user's own overrides, loaded by the router in every run (local or cloud), so nothing inside the installed plugin is edited.
- Vault backends documented: Google Drive folder (local folder + Drive MCP from the cloud) or git.
- Scheduled-task templates rewritten for the split; Pam Memory & Notetaker as the recommended meetings + memory server.
- Tests: +2 (queue, overrides).

## 0.2.0 — 2026-09-08

- `humanpass` skill: brief → human writes → verify. Tiers: the user (default), retained editor, Prolific, Microworkers, Textbroker, human-mcp.io / Upwork MCP. Grounded in Anthropic's 2 Aug 2026 SynthID-Text watermark (light edits keep it, full rewrites remove it, proofreading a person's text adds almost none).
- `stanley-brief` script: `make` (structured brief from a story + claim + voice) and `verify` (facts, forbidden terms, length, ending, 3-gram overlap with any model draft).
- Recommended MCPs by capability (`skills/stanley/references/recommended-mcps.md`) and ready-to-copy `mcp/recommended.mcp.json` (not auto-loaded); onboarding suggests one server per gap, once.
- Watermark notes in the router rule 2, `audit`, and README.
- Makefile/CI unchanged; tests: +2 for the brief script.

## 0.1.0 — 2026-09-08

First scaffold.

- Skills: stanley (router, six rules, capability probe), onboard, mine, write, audit, scout, publish, recap, rituals, learn, study, visuals
- Agents: critic, fact-checker, scout
- Scripts: `stanley-audit` (lint: lexicon, structure, platform, receipts, self-plagiarism, voice overrides), `stanley-vault` (state: init/sync, runs, surfaced dedupe, own-post check, posts/comments/diffs ledger, metrics, stories index), `stanley-stats` (medians and lifts by lane/shape/hook feature; experiments from strategy.md), `stanley-preview` (LinkedIn/X preview cards with fold and per-tweet counts)
- Vault template with receipts-first stories and an experiments block in strategy.md
- Scheduled-task templates for scout, recap, soapbox, weekly drafts, mine, monthly orbit/strategy
- Creator shapes catalog (Paul Graham, Dharmesh Shah, Yamini Rangan, Yuriy Zaremba, Vitalii Dodonov; Sept 2026)
- Tests (`tests/`, `evals/run_audit_tests.py`), CI, CONTRIBUTING with the text-free contribution schema
