# How Open Stanley works

*Review copy, updated 12 Sep 2026, v0.3.0. Written for Nazar to read once, end to end, before installing it next to Stanley. Every claim about what "works" is marked as tested, prose-only, or not built.*

## 1. What it is, in one paragraph

A Claude plugin that does the job of an "AI head of content" the way Stanley does it, minus the parts that failed for a month: it reads your own material through whatever MCPs you have connected (Pam, Slack, Gmail, Notion, Drive, your browser), turns it into stories with receipts, edits those stories into posts in your voice instead of generating from a topic, lints every draft against the 2026 AI-slop rules before you see it, publishes and comments through your own logged-in browser, runs the daily rituals as scheduled tasks that log what they promised and delivered, and learns from every edit you make by changing a file. State lives in a folder of markdown you can read; nothing is a black box.

## 2. The loop, end to end

```mermaid
flowchart LR
  A[Your sources<br/>Pam · Slack · Gmail · Notion · Drive · inbox/ · voice notes] -->|mine| B[stories/*.md<br/>each with a receipt]
  B -->|write: edit, don't generate<br/>voice.md exemplars + shapes| C[draft]
  C -->|stanley-audit| D{clean?}
  D -- no --> C
  D -- yes --> E[critic agent + preview card]
  E -->|you edit or approve| F[final]
  F -->|diff-add| L[learn/diffs.jsonl → voice.md rules]
  F -->|publish via your browser| G[LinkedIn + X]
  G -->|recap: metrics-add| H[ledger/posts.jsonl]
  H -->|stanley-stats| I[lifts by lane / shape / hook;<br/>experiments in strategy.md]
  I --> J[strategy.md resolved bets]
  K[scout: your feeds via browser] -->|filters: not yours, not shown, not stale| M[2–3 comments/day]
  M --> G
```

The step that matters most is the first arrow. Stanley generated a claim from a topic and then tried to make it sound like you. Here nothing is drafted until there is a story file with a `source:` line pointing at a real record (a Pam meeting id, a Slack permalink, an upload, a dated chat message), and a claim in your words. That is what fixes "fake stories that fit the viral pattern," and it is also what the detector research and Anthropic's watermark note both say survives: text that starts as your words and is edited by the model.

## 3. The pieces

### 3.1 The vault (your state)

A folder of markdown and jsonl, created by `skills/stanley/scripts/stanley-vault init <path>`, kept in a desktop-synced Drive folder that the scheduled tasks open directly (laptop mode). Cloud mode mirrors it through the Drive or Notion MCP instead, one call per file.

- `my-human.md`: who you are, handles (so the scout never suggests your own posts), the public/private line, which MCPs map to which capability.
- `strategy.md`: goal, three lanes, cadence, what good looks like with numbers, and an **Experiments** block (`experiment: number-in-hook | variants: with, without | metric: engagement | min_n: 4`).
- `voice.md`: 15–40 of your real posts and comments verbatim as the few-shot set, observations of how you write with evidence, and a yaml block the linter reads (`em_dash: ban`, `closing_question: allow`, `banned_extra`, `allowed`, `freshness_days`).
- `instructions.md`: standing rules you gave, dated ("only today's news counts").
- `stories/`: one file per story with frontmatter `topic / lesson / status / source / date / sensitivity`; `index.md` is generated.
- `ledger/`: `posts.jsonl` (every post with lane, shape tags, experiment variant, metrics by 1h/24h/7d), `comments.jsonl` (posted and skipped, with your reason), `surfaced.jsonl` (every URL ever shown to you), `runs.jsonl` (every scheduled run: promised vs delivered).
- `learn/`: `diffs.jsonl` (every draft→final pair), `rules.md` (what you confirmed).
- `drafts/`, `inbox/` (drop transcripts, voice notes, screenshots).

This is the same shape as Stanley's dashboard (My Human, Instructions, Strategy, Stories, Uploads), with three things added: receipts on stories, a ledger of everything shown and run, and the diffs.

### 3.2 The skills (what Claude reads)

Thirteen `SKILL.md` files. Each is instructions plus references; Claude loads the one that matches what you said.

| Skill | What it does | Status |
|---|---|---|
| `stanley` | Front door. Six rules, the capability probe (which MCPs you have → meetings/messages/mail/docs/memory/browser/post/notify), routing, how to talk, run records | Prose, exercised in this session's tests of the scripts |
| `onboard` | Reads the LinkedIn creator analytics (top posts by impressions, then engagements) before the feed; asks which post you think did best and treats a mismatch as a missed read; reports top-by-reach and top-by-pull separately; three lanes; builds `voice.md` from your real posts; asks the private line; first stories; one MCP per gap | Run on you 2026-09-12; first pass named the wrong best post (read the feed, not the analytics), fixed the same day; the miss is recorded in `skills/onboard/references/onboarding-misses.md` |
| `mine` | Pulls stories from every source with receipts; Pam `retrieve_memory` is a lead, `get_meeting_summary` is the receipt | Pam path tested live (returned three numbered stories from your last two weeks; note its `sources: []`, hence the receipt rule) |
| `write` | Edit story + claim into a post using your exemplars and, if asked, a creator's shapes; tags lane/shape/experiment; audit; critic; preview card; one question back to you | Prose; scripts it calls are tested |
| `audit` | Runs the linter; adds the editor checks the linter can't do (is the claim yours, is it fresh, is it new, watermark share) | Linter tested on your export |
| `scout` | Reads LinkedIn and X feeds via your browser, hard filters (yours / already shown / stale / announcements), scores lane fit and "adjacent viral", drafts 1–3 sentence comments, posts approved ones via the browser (X reply box works where the API refused) | Prose; browser mechanics are the same ones used to read Dharmesh/Yamini/Zaremba/Dodonov feeds in this session |
| `publish` | LinkedIn and X via browser (threads, first-comment links, LinkedIn's scheduler), or any posting MCP; records URL, lane, shape, experiment | Prose |
| `recap` | Pulls analytics via browser, `metrics-add`, runs `stanley-stats`, three lines of deltas, who showed up, one recommendation with evidence | Prose + tested script |
| `rituals` | Soapbox (08:00 question grounded in a fresh story), Sunday drafts, repackage, orbit, strategy check-in, trend alert | Prose; scheduled-task templates ready |
| `learn` | Diff → category → rule after three recurrences (with your yes); skip reasons → scout weights; stats → resolved bets; opt-in text-free community contribution | Prose; ledger plumbing tested |
| `study` | Reads a creator's feed via browser, extracts shapes (opener/body/ending/specificity/form/never), never sentences; ships a catalog for PG, Dharmesh, Yamini, Zaremba, Dodonov from today's live reads | Catalog written; extraction procedure prose |
| `visuals` | Preview cards (tested), charts from your numbers, PDF carousels, source screenshots, image MCPs if present | Preview tested; rest prose |
| `humanpass` | Brief → human writes → verify. Tiers: you (voice note), retained editor, Prolific (~$1.50–2.20), Microworkers (cents), Textbroker ($6–9), human-mcp.io / Upwork MCP (experimental) | Brief/verify script tested; platform API calls prose |

### 3.3 The scripts (what is actually code, all tested)

- `skills/stanley/scripts/stanley-audit`: 30+ rules. Lexicon (measured LLM-excess words and LinkedIn-guru phrases), structure ("not X but Y", tricolons, choppy runs, uniform sentence length, bold-colon lists, setup sentences, wrap-ups, bait closers), platform (hashtags, links, length, hook length, X thread limits), receipts (numbers with no story file), self-plagiarism (3-gram overlap with your ledger), your voice overrides. On your export: blocks Stanley's Cloudflare comment (four phrases), blocks the "containers" comment (agreement opener, 83 words), passes your final note-taker post and your real comments, and flags the "2.08 mathematical floor" you rejected as a number with no receipt.
- `skills/stanley/scripts/stanley-vault`: init/sync (git), run-start/run-end, surfaced-check/add (URL-normalized dedupe), is-self, post-add with lane/shape/experiment, metrics-add, comment-add, diff-add, stories-index.
- `skills/stanley/scripts/stanley-stats`: median and lift by lane, shape, and hook feature; experiment arms with `min_n`; refuses to call a result under 8 posts per arm.
- `skills/stanley/scripts/stanley-preview`: LinkedIn card with the "…more" fold marked at ~210 chars; X thread with per-tweet counts, over-limit in red. Playwright renders PNG; falls back to HTML.
- `skills/stanley/scripts/stanley-brief`: `make` (claim, facts to keep, forbidden terms, length band, ending, one-screen negative style guide from `voice.md`) and `verify` (facts, terms, length, ending, hashtags, and 3-gram overlap with any model draft < 25%).

25 unit tests plus 7 audit fixtures, all passing on your Mac. `claude plugin validate .` passes.

### 3.4 Agents

`critic` (reads as your audience: did the first line stop you, what could only you know, what to cut), `fact-checker` (every claim → receipt or cut, never "studies suggest"), `scout` (feed reader that returns scored candidates, posts nothing).

### 3.5 Scheduled tasks (cloud + laptop)

In laptop mode (default) every task runs on your Mac with the vault folder and Claude in Chrome, so each ritual is one run with nothing queued. Cloud mode is for runs with the laptop closed: tasks run remotely with connectors, skills and plugins but no local files or browser, so each ritual has a cloud part and a laptop part. Cloud: mine via MCPs, drafts, audit, Soapbox, X via the official X MCP, analytics via a posting MCP, notify. Laptop: LinkedIn feed scans, LinkedIn comments and posts, LinkedIn analytics, X replies to accounts that haven't mentioned you. The cloud parks the laptop part in `ledger/local-queue.jsonl` with an expiry; `drain` runs it when a session starts (SessionStart hook) or when the launchd job fires inside your window (every 30 minutes, 08:00–23:00, re-fired on wake). In cloud mode the vault is therefore mirrored from Drive, and your own overrides live in the vault's `skills/` folder so both cloud and laptop runs see them.



Prompts in `templates/scheduled-tasks/` for Cowork Scheduled tasks or Claude Code `/schedule`: scout 10:00 and 22:00, recap 22:00, soapbox 08:00, weekly drafts Sunday 10:00, mine weekly, orbit + strategy monthly. Each starts by cloning the vault, probing MCPs, `run-start`; ends with `run-end`, `sync`, and a message that says what was checked even when the answer is nothing. That is the fix for the scans that silently didn't fire.

## 4. Why it should beat Stanley on the things that hurt

| Stanley failure (from the export) | What replaces it |
|---|---|
| Draft copies your own post; duplicates resurfaced | `surfaced.jsonl` + `is-self` + self-plagiarism rule |
| Stale papers as news; "recent literature shows" | receipts on stories, freshness window, `uncited-study` block, fact-checker agent |
| "Sounds like AI", seven times | linter blocks the measured tells before you see the draft; your edits become rules |
| Feedback acknowledged, never persisted | `diff-add` → recurring category → one-line rule you confirm → file changes |
| 10am/10pm scans didn't fire; LinkedIn skipped | `runs.jsonl` promised vs delivered; every run reports |
| Suggested commenting on your own posts (4×) | `is-self` hard filter |
| X API can't reply to non-mentioning accounts; LinkedIn search quota | your browser: no quota, real feed, reply box works |
| No custom MCPs (Pam refused) | capability probe uses whatever is connected; Pam tested live |
| Recap: "131 saw, 2 reacted" | deltas + who showed up + one recommendation from `stanley-stats` |
| Off-topic comment picks | "adjacent viral" scoring weighted equal to lane fit; skip reasons retune weights |

## 5. Detection and the watermark, plainly

Since 2 Aug 2026 every word Claude generates carries Anthropic's SynthID-Text watermark; light edits keep it, a full rewrite removes it, and proofreading your text adds almost none. LinkedIn demotes "generic AI" posts silently (May 2026) and a million people have clicked "seems like AI slop." The plugin's answer is not a humanizer (they are themselves detectable and make text worse). It is: your claim, your material, the model as editor, the linter for the measured tells, and, when you want none of the words to be model-written, `humanpass`: the model writes a brief, a human writes the post, `stanley-brief verify` proves it is a real rewrite. Detector scores, if you add keys, are shown as information and never used to reject a human.

## 6. What is not built yet (so you don't expect it)

- The browser flows in `scout`, `publish`, `recap` are instructions; they have not been run end to end as the plugin (the same browser mechanics worked in this session by hand).
- `learn`'s clustering of diffs into rule candidates is judgment in prose, not code.
- The Prolific/Microworkers/Textbroker API calls in `humanpass` are described, not scripted.
- Behavioral evals (`evals/evals.json`) exist but have not been run through skill-creator; the deterministic tests have.
- Preview PNGs need Playwright on your Mac (`pip install playwright && playwright install chromium`); otherwise you get HTML.

## 7. Running it beside Stanley: a fair test

Two weeks, same lanes, both tools fed the same inputs.

1. Install locally first: `claude --plugin-dir ~/Downloads/temp/open-stanley` (or push to GitHub and `/plugin marketplace add`). Say "set up Stanley" and let onboarding build `voice.md` from your real posts; check the yaml block matches how you write.
2. Create the vault as a private repo; add the scheduled tasks (scout 10/22, recap 22, soapbox 08) in Cowork.
3. Each morning, give both tools the same material (the same voice note or the same Pam meeting). Keep both drafts.
4. Score, per draft, in `ledger/` and a note for Stanley: minutes you spent editing, words changed (diff), whether it shipped, and 7-day engagement. Comments: relevance (posted / skipped and why), and whether the target was fresh.
5. Two things to watch that the export says Stanley loses on: repeats/own-post suggestions (should be zero here), and whether feedback sticks after three days.
6. At the end, `stanley-stats` gives the medians for the plugin's posts; compare against Stanley's on the same platform and window.

## 8. Before pushing to GitHub

- Confirm `.gitignore` covers the export, `transcript.txt`, `stanley-vault/`, `evals/private/` (it does).
- Decide the repo name and whether "Stanley" in the name is a trademark problem you're comfortable with.
- Fill `author.url` / `repository` in `.claude-plugin/plugin.json` with the real GitHub path.
- Run `make test` once more on the Mac; `claude plugin validate .`.
- Then the go-to-market plan in `DESIGN.md` §8: build-in-public series drafted by the plugin from its own `runs.jsonl`, marketplace and ClawHub/skills.sh submissions, the 20 DMs, Product Hunt.
