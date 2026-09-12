# Open Stanley

An open head of content for the agent you already pay for.

It mines your own meetings, Slack, email, docs, and notes through whatever MCPs you have connected, drafts LinkedIn and X posts by editing your material into your voice (never by generating a claim from a topic), audits every draft against the 2026 AI-slop and platform rules, publishes and comments through your own browser, runs the daily rituals as scheduled tasks with a run log, and learns from every edit you make.

It is the loop that "AI head of content" products sell for $47–149 a month, rebuilt as a plugin, with the three things they can't do: read your custom sources, remember your corrections, and prove where every claim came from.

## Install

```
# Claude Code / Cowork
/plugin marketplace add Harmix/open-stanley
/plugin install open-stanley@open-stanley

# Codex, or any agent that reads SKILL.md (Agent Skills standard)
npx skills add Harmix/open-stanley
```

Then say: **"set up Stanley"**. Onboarding reads your last 40–60 posts through your browser, tells you your median engagement and why your top three posts worked, proposes three lanes, builds a voice profile from your own words, and asks where the vault should live (a plain folder in your synced Google Drive, so scheduled runs on your laptop can read it).

## Repo layout

```
.claude-plugin/   manifest + marketplace entry
skills/           14 skills; stanley/scripts/ holds the 5 CLI scripts, stanley/references/ the shared rules
agents/           critic, fact-checker, scout subagents
templates/        scheduled-task prompts (laptop and cloud preambles) and the launchd drain job
vault-template/   the empty vault a new user starts from
hooks/            one SessionStart hook: reports queued items (cloud mode)
tests/            unit tests + tests/evals (audit fixtures, behavioral evals)
docs/             HOW-IT-WORKS, DESIGN, RESEARCH, CONTRIBUTING, research notes
dist/             open-stanley.plugin for installing into Cowork by file
```

## What it does

| You say | It does |
|---|---|
| "anything worth posting from this week's meetings?" | `mine`: pulls your meetings, Slack, sent mail, docs via your MCPs → story files with receipts |
| "write it" | `write`: edits the story into a post in your voice, audits it, hands it over with one question |
| "does this sound like AI?" | `audit`: the linter (`skills/stanley/scripts/stanley-audit`) plus an editor's read: claims, freshness, novelty |
| "find posts to comment on" | `scout`: your feeds through your browser, hard filters (not yours, not shown before, not stale), 1–3 sentence comments |
| "post it to both" | `publish`: LinkedIn + X through your browser (threads, first-comment links, scheduling), ledger updated |
| "how did it do?" | `recap`: deltas, who showed up, one recommendation |
| morning question, Sunday drafts, repackage, orbit, strategy check-in | `rituals`, as scheduled tasks from `templates/scheduled-tasks/` |
| "learn from what I actually posted" | `learn`: diff → rule after three recurrences; opt-in, text-free community contribution |

## The rules it runs on

1. Human-origin material first; no post from a topic.
2. Edit, don't generate; your own posts are the few-shot set.
3. No receipt, no claim.
4. Never re-say (your posts, your comment targets, your own posts as targets).
5. Audit before you see it.
6. Your edit is the training signal, and a file changes.

`skills/stanley/references/why-these-rules.md` has the failure log they come from.

## What about a "humanizer"?

There isn't one, on purpose. And there is a watermark to think about: since 2 August 2026 every word Claude generates carries Anthropic's SynthID-Text watermark, in the API, Claude Code and Cowork, no opt-out. Anthropic's own wording: light edits probably won't remove it, a complete rewrite will, and when Claude only proofreads a person's text there's very little for the watermark to attach to. That is the same conclusion the detector research reaches from the other side, so the plugin's answer is the same: keep as many words as possible yours. Commercial humanizers are themselves models with a detectable style (Pangram ships a classifier for them), and they make text worse for readers. The protection here is structural: the claim comes from you, the draft is an edit of your material with your own posts as the few-shot set, `stanley-audit` blocks the measured tells (vocabulary, "not X but Y", staccato lines, em-dash density, bold lists, bait closers, hashtags), a critic agent reads as your audience, and you make the last pass, which is recorded as training data. If you have detector API keys, `audit` reports their scores as information; it never rewrites to game them. When you want none of the text to be model-written, `humanpass` inverts the pipeline: Claude writes a structured brief (claim, facts with sources, forbidden terms, length, ending, a one-screen style guide), a human writes the post (you, a retained editor, or a writer hired by API at ~$1.50–2 on Prolific, cents on Microworkers, $6–9 on Textbroker), and `stanley-brief verify` checks facts, terms, length, and that the result is a real rewrite (3-gram overlap with any model draft under 25%).

## Recommended MCPs

The plugin works with whatever you have connected and suggests, once, one server per gap from `skills/stanley/references/recommended-mcps.md`: Buffer or Typefully for posting, the official X MCP for X search and analytics, Pam Memory & Notetaker for meetings and memory in one server (built by the author's company, so read that as a maintainer's pick; Fathom/Granola/Fireflies work the same for transcripts), Exa for fact-checking (no key needed), Replicate or Recraft for images, Canva for carousels, Deepgram for voice notes, Slack for approvals, GPTZero or Pangram for detection scores, Prolific for the paid human lane. Ready-to-copy entries are in `skills/stanley/references/recommended.mcp.json` (not auto-loaded). No LinkedIn scrapers, ever.

## How it learns, and how it experiments

- **Your voice**: `voice.md` holds 15–40 of your real posts and comments verbatim, plus a yaml block the linter reads. Every draft→final diff is stored; a pattern that recurs three times is proposed as one rule, and on your yes it becomes a file change.
- **Creators you admire**: `study` reads a creator's feed through your browser and extracts *shapes* (openers, bodies, endings, specificity moves), never sentences, into `shapes/`. A catalog for Paul Graham, Dharmesh Shah, Yamini Rangan, Yuriy Zaremba, and Vitalii Dodonov (Sept 2026) ships in `skills/study/references/`.
- **Your audience**: `stanley-stats` computes medians and lifts by lane, shape and hook feature from the ledger, and runs the experiments you declare in `strategy.md` (`experiment: number-in-hook | variants: with, without | metric: engagement | min_n: 4`). Posts alternate variants; the weekly recap reports arms and refuses to call a result under the minimum sample. Resolved bets are written into `strategy.md` with numbers and dates.

## Visuals

`stanley-preview` renders any draft as a LinkedIn or X card with the "…more" fold marked and per-tweet counts (this is the "Edit this draft" image the paid product sends, with the fold added). `visuals` also covers charts from your own numbers, PDF carousels for LinkedIn documents, source screenshots, and image-generation MCPs if you have one connected. No stock imagery, no generated illustrations by default.

## Why it works in 2026

LinkedIn silently demotes "generic AI" posts (May 2026) and a million people have clicked "seems like AI slop" (Aug 2026). Detectors measure post-training style, not authorship: text that starts as your words and is edited by a model reads human to both readers and classifiers; text generated from a prompt and then "humanized" does not. The biggest AI builders on LinkedIn now write "no AI was used" on their posts. Open Stanley is built for that environment: it only ever edits what you gave it, and it shows you the receipt. The research behind this is in `docs/research/` and `docs/RESEARCH.md`.

## Vault

Your state is a folder of markdown and jsonl (`vault-template/`): who you are, your strategy, your voice with verbatim exemplars, standing instructions, stories with sources, a ledger of every post/comment/run/surfaced link, and your draft→final diffs. Keep it in a plain folder inside your synced Google Drive (laptop mode) or mirror it through the Drive/Notion MCP (cloud mode); git is an option for Claude Code and CI.

## Scheduled tasks: laptop or cloud

The rituals (`templates/scheduled-tasks/`) run as Cowork scheduled tasks or Claude Code routines. Every run records what it promised and what it delivered; a run that finds nothing still reports.

Two modes. **Laptop mode (default):** the vault is a plain folder inside your desktop-synced Google Drive (or iCloud/Dropbox), every scheduled task runs on your computer with that folder and your browser, so each job reads LinkedIn and X itself; runs happen only while the computer is awake, and a run the computer missed is caught up by the next run or on "catch up" (`stanley-vault missed`). **Cloud mode:** tasks run in the cloud with your connectors and no browser; the vault is mirrored through the Google Drive (or Notion) MCP and browser-only work waits in a queue for the `drain` task on your laptop. Git is for Claude Code users running jobs from their own machine; Cowork scheduled tasks can't clone a private repo. Details and costs: `skills/stanley/references/vault-backends.md` and `scheduling.md`. Your own rule overrides live in the vault's `skills/` folder and load in every run, local or cloud. The plugin is the same on Cowork and Claude Code; Claude Code inherits your claude.ai connectors when you're logged in with the subscription.

## Tests, versioning, CI

`make test` runs the deterministic audit fixtures and 23 unit tests (`tests/`: audit rules, vault ledger, stats and experiments, preview rendering, plugin structure and version consistency). `.github/workflows/ci.yml` runs them on every push. Versions are semver in `.claude-plugin/plugin.json`, mirrored in `marketplace.json` and `CHANGELOG.md`; a test fails if they disagree. Behavioral evals for the skills live in `tests/evals/evals.json` and run through Anthropic's skill-creator (blind A/B against the previous version).

## Contributing

Rules are measurable. `tests/evals/run_audit_tests.py` runs the deterministic tests; `tests/evals/evals.json` holds the behavioral evals for skill-creator. A rule PR needs a fixture that proves it. See `docs/CONTRIBUTING.md`. If you opt in inside the plugin, it will prepare a monthly, text-free contribution of which rules fired and which edits you made (schema in `skills/learn/references/contribution-schema.md`).

## Status

0.1.0, MVP. Built by a founder who paid for the closed version for a month and kept the chat log. MIT.
