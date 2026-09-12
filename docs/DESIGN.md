# Open Stanley — Design

*An open "head of content" for Claude (and any agent that reads SKILL.md). Companion to RESEARCH.md.*

---

## 0. What we are building, in one sentence

A plugin that turns the agent the user already pays for (Claude Cowork / Claude Code, or Codex / OpenClaw via the skills standard) into a proactive head of content that (1) mines the user's own material through whatever MCPs they have connected, (2) drafts in the user's voice by editing that material rather than generating from a topic, (3) audits every draft against the 2026 AI-slop and platform rules, (4) publishes and comments through the user's own browser and accounts, (5) runs the daily/weekly rituals as scheduled tasks with a run log, and (6) learns from every edit the user makes, locally first, and optionally contributes anonymized rule improvements back to a reviewed shared skill.

Stanley's job description, minus the black box, minus the $149.

---

## 1. Form factor: plugin with portable skills

**Decision: ship as a Claude plugin (`open-stanley`) whose `skills/` folder is also a standalone, standard-conformant skills pack.**

Why not "just a skill": a skill is instructions. Stanley is instructions *plus* state (the vault), *plus* scheduled jobs, *plus* publishing tools, *plus* a learning loop. Only a plugin can bundle skills, subagents, hooks, an MCP config, a `bin/` with helper scripts, and install with one command. Why not "a separate app": the whole point is that the user's existing agent, credentials, and MCPs are the runtime, and that Anthropic gets paid instead of Stanley.

Portability: every skill is a plain `SKILL.md` folder with `references/` and `scripts/`, so `npx skills add open-stanley/open-stanley`, `codex plugin marketplace add`, and ClawHub publishing all work with no changes. Cowork-only or Claude-Code-only features (scheduled task templates, hooks, monitors) degrade to documentation on other runtimes.

```
open-stanley/
├── .claude-plugin/plugin.json
├── README.md                      # 1-command install, 3-minute onboarding
├── skills/
│   ├── stanley/                   # the front door: routes to the others, holds the operating rules
│   ├── onboard/                   # profile diagnosis, lanes, strategy.md, voice.md from the user's own posts
│   ├── mine/                      # find post material in every connected MCP + uploads (the "stories" engine)
│   ├── write/                     # source-first drafting, platform formatting, X threading
│   ├── audit/                     # AI-slop + platform-rule linter, voice diff, claim/receipt check
│   ├── scout/                     # feed scan → comment opportunities → paste-ready comments
│   ├── publish/                   # adapters: browser (LinkedIn), X API/CLI, or any posting MCP the user has
│   ├── recap/                     # nightly/weekly numbers with an actual recommendation
│   ├── rituals/                   # soapbox, weekly drafts, repackage, orbit, strategy check-in
│   └── learn/                     # diff capture → voice.md / rules; optional anonymized contribution
├── agents/
│   ├── critic.md                  # adversarial reader: "would a founder in this niche scroll past this?"
│   ├── fact-checker.md            # every claim gets a receipt or gets cut
│   └── scout.md                   # read feeds via browser, score candidates
├── hooks/hooks.json               # PostToolUse on publish → append to ledger; SessionStart → load vault index
├── monitors/monitors.json         # optional: watch the vault inbox folder for new voice notes / transcripts
├── .mcp.json                      # optional bundled servers (e.g. an X posting MCP); everything else is discovered
├── bin/                           # stanley-vault, stanley-audit (python), stanley-ledger
├── templates/scheduled-tasks/     # copy-paste prompts for Cowork Scheduled / Claude Code Routines
└── evals/                         # skill-creator eval suite; the acceptance gate for contributions
```

---

## 2. The vault (state)

Stanley's dashboard is a wiki; ours is a folder of markdown under git. Same shape, but with provenance and a ledger, because every Stanley failure in the research was a missing piece of state.

```
stanley-vault/
├── my-human.md          # who they are, audience, what they will and won't say publicly
├── strategy.md          # goal, 3 lanes, cadence, platforms, what "good" looks like (with examples)
├── voice.md             # learned voice profile: banned words, sentence-length band, hook patterns they
│                        #   actually use, punctuation habits, sign-offs, 15–40 exemplar posts (verbatim)
├── instructions.md      # standing rules the user gave in chat ("only today's news", "no hallucination tropes")
├── stories/
│   ├── index.md         # topic → story → one-line lesson → status (fresh / used-on / needs material)
│   └── <slug>.md        # the story, the claim, and the RECEIPT: source (MCP + id / URL / upload), date, quote
├── ledger/
│   ├── posts.jsonl      # every published post: platform, url, hook, story ids used, metrics over time
│   ├── comments.jsonl   # every comment posted (or drafted-and-skipped, with the user's reason)
│   ├── surfaced.jsonl   # every URL ever shown to the user (the dedupe set), with author handle
│   └── runs.jsonl       # every scheduled run: started, what it promised, what it delivered, errors
├── drafts/              # one file per draft, with version history via git
├── inbox/               # raw material the user drops: voice notes, transcripts, screenshots, PDFs
└── learn/
    ├── diffs.jsonl      # (draft, final) pairs + derived rule candidates
    └── rules.md         # rules learned from diffs that the user has confirmed
```

**Where it lives.** Three backends, chosen at onboarding:

- Local folder (Claude Code / Cowork with a connected folder). Best for privacy; scheduled tasks in Cowork cannot reach it.
- Private GitHub repo (recommended default). Claude Code Routines and Cowork scheduled sessions can both clone it with a token; history is free; the user can read and edit it anywhere.
- Notion / Google Drive via the user's MCP, for people who never want a repo. The vault skill writes the same files as pages.

The `stanley-vault` helper script abstracts read/write over all three so skills never care.

---

## 3. The writing pipeline (opening the black box)

The research says one thing loudly: detectors and readers both key on *whether the claim could only have come from this person*, and LinkedIn now demotes the generic. So the pipeline is ordered to make generation impossible without human-origin material.

**Step 1 — Material, not topics.** `mine` asks the runtime which MCPs exist (see §5) and pulls candidate material: last week's meetings (Pam, Fathom, Granola…), Slack threads the user wrote, sent emails, calendar events, docs edited, the inbox folder, and the user's own recent posts and comments. It writes *story* files with receipts. Nothing without a receipt enters the stories index. (This kills Zaremba's "fake stories that fit the viral pattern".)

**Step 2 — Claim from the human.** For a new post the skill proposes 3 angles from fresh stories and asks one question: "which one, and what's the thing you actually believe about it?" or "voice-note it". The user's answer (typed or transcribed) becomes `claim.md`. If the user just says "go", the skill picks the angle but uses the story's own quoted material as the claim, and marks the draft `unclaimed` so the audit demands an edit pass.

**Step 3 — Draft by editing.** The writer is instructed to *rewrite the human material into a post*, in the voice profile, with the exemplar posts in context (few-shot with the user's own words, never a style adjective list). Platform packaging: LinkedIn body 1,300–1,900 chars with the first 140 chars self-contained; X either a single long post (Premium) or a 5–7 tweet thread with the hook standing alone; links only in the first X reply, never in the LinkedIn body.

**Step 4 — Audit (deterministic, in `bin/stanley-audit`).** Scores and blocks:
- Banned lexicon (delve, leverage, harness, pivotal, intricate, meticulous, underscore, showcase, realm, testament, landscape, navigate, unlock, elevate, robust, seamless, tapestry, ever-evolving, game-changer, "here's the thing", "let that sink in", "in today's fast-paced")
- Structural tells: "not X, it's/but Y"; tricolon lists; bolded-term-colon lists; more than one em dash per ~1,000 words; three or more consecutive sentences under 8 words; sentence-length variance below a floor; closing audience question when `strategy.md` says the user doesn't do that (Nazar does, as a discussion opener — the rule is per user)
- Platform rules: hashtags (0), links in body (0), length band, hook length, engagement-bait phrases, polls
- Receipt check: every number, name, date, paper, or "study" in the draft must map to a story file with a source; every "news" item must be dated within the user's freshness window (Nazar: today)
- Self-plagiarism: cosine similarity against `ledger/posts.jsonl` hooks and bodies; block above a threshold ("almost a copycat of my post")
- Optional detector spread: GPTZero / Originality / Pangram APIs if the user adds keys; reported, not treated as truth

**Step 5 — Critic.** A subagent reads the draft as the target reader ("AI-native founder, sees 200 posts a day") and answers three questions: would I stop scrolling, is there anything here only this author could know, what would I cut. Its notes go to the user with the draft, not into another rewrite loop.

**Step 6 — Human pass with diff capture.** The user edits (in chat, in the file, or in a Slack/MCP-elicitation approval). The `(draft, final)` pair is written to `learn/diffs.jsonl`. No publish without this step unless the user has explicitly set `autonomous: true` for a lane.

**Step 7 — Publish and track.** Through the adapter (§4). The ledger records the post; `recap` polls metrics at 1h, 24h, 7d and attaches them to the story ids used, so `strategy.md` can be updated with evidence ("stories with a number in the hook: 3.1x median").

**Optional Step 6b — a second human.** If the user configures it: post the draft to a retained editor via the same Slack/approval channel, or open an Upwork MCP job with a fixed brief and budget (human confirms the hire). The skill never uses "humanizer" tools; the research shows they are themselves detectable and they make text worse for readers.

---

## 4. Scouting, commenting, publishing (the parts Stanley couldn't do)

**Feeds via the user's own browser.** Stanley scrapes LinkedIn with a quota and hits an X API wall on replies. Open Stanley reads the feeds with Claude in Chrome / the built-in browser while logged in as the user: LinkedIn home feed, search, hashtag pages, X home/For You and lists. No quota, and it sees exactly what the user sees. Fallbacks: any social MCP the user has (SocialClaw, Postiz, `bird`), or the official X API for posting.

**Scout scoring** (learned from the export): candidates are scored on (a) topical fit to the lanes, (b) *adjacent-viral*: high engagement on an org/workplace/AI-tools topic where the user's angle is a natural reply (the Matt Rothenberg pattern), (c) freshness (X: under 30 min old is gold), (d) author size relative to the user (5–20x on X), (e) not already in `surfaced.jsonl`, (f) **author ≠ user**, (g) not the user's own reposts. Each pick ships as: link, one line on why, paste-ready comment in the user's comment voice (which is shorter and plainer than their post voice; from the diffs, Nazar's real comments were 1–2 sentences), and a "skip" button that records the reason.

**Comment posting.** LinkedIn comments and X replies are typed by the browser tool after approval (this bypasses the X API restriction entirely). Reply-to-replies on the user's own posts are surfaced in the recap because they are the highest-weight ranking action on X.

**Publishing adapters** (`publish` skill): LinkedIn via browser (compose, attach image/document, schedule via LinkedIn's own scheduler when the user wants a time), X via browser or API, plus passthrough to any posting MCP found at runtime. Every adapter returns the canonical URL for the ledger.

---

## 5. Generic MCP discovery (Nazar's key requirement)

The `stanley` skill starts every run with a capability probe rather than a fixed integration list:

1. In Claude Code: `claude mcp list` (status + tool counts). In Cowork / this harness: the tool namespace (`mcp__<server>__*`) and tool search by keyword. In other runtimes: whatever list the host exposes.
2. Map servers to *capabilities*, not names: `meetings` (anything with transcript/meeting/summary tools: Pam, Fathom, Granola, Zoom, Notion meeting notes), `messages` (Slack, Discord, Teams, Gmail sent), `docs` (Drive, Notion, Confluence), `calendar`, `crm`, `memory` (Pam Memory, mem0-style retrieve), `post` (SocialClaw, Postiz, X), `notify/approve` (Slack, Telegram, email).
3. Tell the user what it found and what it will use each for, once, and store the mapping in `my-human.md`. Re-probe when the tool list changes.
4. Read-only by default for material; write only through `post` and `notify` capabilities and only after approval.

This is the single biggest structural advantage over Stanley: Pam's meeting summaries, the user's Gmail, Slack, Notion and Calendar are already connected in this very session, and none of them are reachable by Stanley.

---

## 6. Scheduled tasks (the cron layer, done so it can't silently fail)

Templates in `templates/scheduled-tasks/`, one prompt each, for Cowork Scheduled tasks and Claude Code Routines (the user picks; both run remotely, so the vault must be the git or Notion/Drive backend for these). Each run must (a) append a `runs.jsonl` entry with what it promised and delivered, (b) post a message even when it found nothing ("scanned 62 posts, 0 passed the bar, here is the best near-miss"), and (c) never resend anything in `surfaced.jsonl`.

| When | Job | Output |
|---|---|---|
| Daily 08:00 | Soapbox | One question in the user's lane grounded in a fresh story with a receipt; "voice-note 2 min" |
| Daily 10:00 & 22:00 | Scout | 2–3 comment opportunities per platform with paste-ready comments; posts the ones marked auto-approve |
| Daily 22:00 | Recap | Metrics that changed, who replied (reply-to-them prompts), one concrete recommendation |
| Sunday 10:00 | Weekly drafts | 3 drafts from the freshest stories, each with the claim question attached |
| Weekly | Mine | Re-index meetings/Slack/email/docs from the last 7 days → stories + "needs material" |
| Bi-weekly | Repackage | Best-performing old post shapes → fresh spins, marked as repackages |
| Monthly | Orbit + strategy check-in | Top engagers and what to do about them; diff of strategy vs. evidence |
| On event | Trend alert | Only with a dated source under N hours old; drafts an angle, never posts |

Local-only extras (Claude Code): a monitor on `inbox/` so dropping a transcript or voice note triggers `mine` immediately.

---

## 7. Self-improvement, three layers

**Layer 1 — personal, automatic.** Every diff becomes a rule candidate ("removed setup sentence", "replaced 'innate' with plain word", "cut conclusion, ended with a question"). Candidates that recur 3 times are proposed to the user as one line for `voice.md`/`rules.md`; confirmed ones become hard audit rules for that user. Every skip reason on scout picks tunes the scout scoring weights. Every metric that comes back tunes lane weights in `strategy.md`. This is what Stanley promised ("logged, calibrating") and never actually persisted.

**Layer 2 — run-level.** `runs.jsonl` plus a weekly "what I got wrong" line in the recap (missed posts the user found themselves, duplicates, off-topic picks), so regressions are visible in-product rather than discovered by the user shouting.

**Layer 3 — community, opt-in, content-free.** The Vercel telemetry incident sets the bar. So:
- Default off; a native, plainly labelled question at onboarding; the decision stored in a file the user can read and flip.
- What leaves the machine: *derived rule statistics only*. E.g. `{rule: "ban:not-x-but-y", fired: 14, user_reverted_fix: 1}`, `{candidate_rule: "cut-setup-sentence", recurrences: 9, accepted: true}`, `{scout_skip_reason: "too-abstract", count: 6}`. Never draft text, never post text, never handles, never MCP names. Rotating per-submission salt, no device id, k-anonymity floor before anything is aggregated.
- Transport: a GitHub issue opened by `gh` under a bot label (the user sees the exact JSON before it goes), or a form endpoint. No hooks on SessionStart, nothing fires outside the skill.
- Review: maintainers turn recurring candidates into proposed rule changes as PRs against `skills/audit/references/rules.md` and `skills/write/references/*.md`. Acceptance gate = the skill-creator eval suite in `evals/` (blind A/B comparator on a held-out prompt set) plus a maintainer read. Merged rules ship in the next version; `plugin.json` version bump propagates to everyone.
- Contributors can also just open PRs. The eval suite makes "does this make writing sound more like a person" a measurement instead of an argument.

A later, optional "personal skill exchange": users who want to can publish their own `voice.md`-derived *style packs* (e.g. "PG-style X comments", "CEO admitted-mistake post") as sub-skills in the community marketplace, reviewed the same way.

---

## 8. Distribution plan (copying Stan, minus the $149)

1. **Build it in public, on the accounts the skill itself runs.** Nazar's LinkedIn/X become the case study: the first post is the Stanley experience (the $59→$10 negotiation, the 8-drafts-1-usable day, the "suggested I comment on my own post" moment) with the receipts from the export. Then a 14-day build series with numbers, exactly the Stan playbook. The skill drafts these posts from its own `runs.jsonl` — the product marketing itself.
2. **Launch surfaces in order:** GitHub (1-command install, 90-second demo GIF, the RESEARCH.md as the README's "why"), `claude-community` marketplace submission, ClawHub and skills.sh listings, `npx skills add`, a PR to `VoltAgent/awesome-openclaw-skills` and to the awesome-claude lists, Show HN, r/ClaudeAI + r/ClaudeCode + r/LinkedInLunatics-adjacent founder subs, Product Hunt (target #1 of the day; Stanley for X got #2 with 406 votes).
3. **The 20 DMs.** Personalized notes to the people whose complaint or endorsement moves the category: Yuriy Zaremba (he posted the exact failure list four days ago), Serge Bulaev (linkedin-skills — propose integration rather than competition), Justin Welsh / Lara Acosta / Jasmin Alić (offer the diff-learning angle), Dharmesh (the "no AI was used" p.s. is the hook: "here's the tool for people who want to keep writing their own claims"), Buffer/Typefully/Postiz teams (adapter partnerships).
4. **Positioning line:** "Stanley charges $47–149/mo to run a chat loop over your posts. Open Stanley runs the same loop inside the Claude you already pay for, with your meetings, Slack and email plugged in, and it learns from your edits instead of forgetting them."
5. **Growth loop inside the product, without paying for mentions:** the monthly strategy check-in offers (once) to draft the user's own "how I run my content" post from their real numbers. Opt-in, honest, and it is the same mechanism Stan uses, minus the $500.
6. **Anthropic angle:** submit to the official directory once evals are green; write the plugin to be the showcase for scheduled tasks + MCP discovery + skill-creator evals, which is what Anthropic wants to feature.

---

## 9. Roadmap

**Week 1 — MVP (usable by Nazar alone).** Vault (local + git), `onboard`, `mine` (Pam + Gmail + Slack + Notion + uploads), `write`, `audit` v1 (lexicon, structure, receipts, self-plagiarism), `publish` via browser for LinkedIn + X, `scout` via browser, ledger. Two scheduled-task templates (scout 10/22, recap 22). Diff capture on.

**Week 2 — Rituals + learning.** Soapbox, weekly drafts, repackage, orbit; Layer-1 learning proposing rules; critic and fact-checker agents; detector spread optional; evals seeded from the export (Nazar's real drafts and finals are a ready-made test set).

**Week 3 — Ship.** README, demo, marketplace submissions, ClawHub/skills.sh, launch posts drafted by the skill from its own logs, the 20 DMs.

**Week 4+ — Community.** Contribution loop (Layer 3), style packs, adapter MCPs, Codex/OpenClaw verification, human-editor tier via Upwork MCP.

---

## 10. Decisions needed from Nazar

1. Vault backend default for scheduled runs: private GitHub repo (my recommendation) vs Notion vs Drive.
2. Should LinkedIn publishing be browser-only (safe, no ToS question for the plugin itself) or also support third-party posting MCPs?
3. Autonomy default: approve-everything (recommended for launch) vs auto-post comments that pass audit.
4. Name and license: "open-stanley" is descriptive but leans on their trademark; alternatives: "headofcontent", "ghost", "stanly-oss". MIT or Apache-2.0 (ClawHub requires MIT-0 for its listing).
5. Whether the first public post is the Stanley story (it is the strongest hook, but it burns the relationship with a team you negotiated a deal with and promised a testimonial to).
