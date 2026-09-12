---
name: onboard
description: Set up Open Stanley for a person — create the vault, diagnose their LinkedIn/X so far (median engagement, what worked and why), propose three content lanes, and build a voice profile from their own posts and comments. Use when the user says "set up Stanley", "onboard me", shares their LinkedIn or X profile for the first time, asks "what should my content strategy be", or whenever the vault has no strategy.md or voice.md yet.
---

# Onboard

Goal: in one sitting, produce four short files the rest of the plugin runs on: `my-human.md`, `strategy.md`, `voice.md`, `instructions.md`, plus the first `stories/`. The paid product did the diagnosis well; it then forgot the voice part. Do both.

## 1. Vault and mode

Default is **laptop mode**: the vault is a plain folder inside a desktop-synced Google Drive (or iCloud/Dropbox) folder, and every scheduled task runs on the user's computer with that folder connected and their browser available (`skills/stanley/references/scheduling.md`). Ask where their synced Drive lives (macOS: `~/Library/CloudStorage/GoogleDrive-<account>/My Drive/...`), create `stanley-vault` there with `skills/stanley/scripts/stanley-vault init <path>`, and have them connect the folder to the chat. Record `mode: laptop`, `vault: local`, `vault_path: <path>` in `my-human.md`.

Offer **cloud mode** only if they say runs must happen with the laptop closed, and say what it costs (Drive-mirror runs are slower and browser work waits for the drain). Then `vault: drive` with the folder id, or `notion`. Do not offer git to Cowork users; scheduled tasks cannot clone a private repo (`vault-backends.md`).

Explain in one line where the vault lives and that it is plain markdown they can edit.

## 2. Read what they've posted (no questionnaire)

Read the analytics pages first, the feed second. The feed shows what is recent; the analytics show what worked. Confusing the two is how the first onboarding named the wrong best post (see `references/onboarding-misses.md`).

With the `browser` capability (logged in as the user), in this order:

1. **LinkedIn creator analytics, top posts by impressions**: `https://www.linkedin.com/analytics/creator/top-posts/?metricType=IMPRESSIONS&timeRange=past_365_days`. It lists every post of the last year with full text, reactions, comments, reposts and impressions, sorted by reach. Read it with `get_page_text` (the "Top performing posts" widget on the overview page often never loads; the `top-posts` URL does). Then the same URL with `metricType=ENGAGEMENTS`.
2. **The overview** `https://www.linkedin.com/analytics/creator/content/?timeRange=past_365_days` for the totals (impressions, reactions, comments, saves, sends) so you can say what share of the year's reach one post carried.
3. **Recent activity** (`/in/<handle>/recent-activity/all/`) only for the last 30 comments and for posts older than the analytics window.
4. **X**: the profile page and `x.com/<handle>/with_replies`, plus `analytics.x.com` if Premium.

If no browser is available, ask them to paste 10–20 posts and, separately, "which post do you think did best, and why?"

Before you diagnose, ask that same question anyway, in one line: **"Which of your posts do you think did best?"** Their answer is a check on your read: if the post they name is not in your top three, you missed something. Go back to the analytics, search their posts for it (`/search/results/content/?keywords=<phrase>` with their name), and only then write the diagnosis.

Save the raw pull to `inbox/own-posts-<date>.md` so you never scrape twice, and seed `ledger/posts.jsonl` from it (one line per post, impressions included, dates exact where the share id gives them: `date = epoch_ms(id >> 22)`).

Compute and tell them, in five lines:
- median engagement and median impressions per post on each platform;
- the top post **by reach** and the top post **by pull** (reactions+comments), named separately if they differ, each with the one reason it worked (a story, a claim about the future, a hand-over-the-system how-to). A post that carried half the year's impressions with 24 reactions is a different lesson from a post with 107 reactions and 100 impressions: the first left the network, the second was the network congratulating them;
- the bottom pattern (event announcements, paper shares with academic framing, "excited to attend");
- what the audience that should care is not seeing.

This diagnosis is the most-liked thing the paid product did; keep the numbers exact and the reasons blunt. Never quote a number you did not read on a page this session. If a metric is missing, say "no number" rather than estimating.

## 3. Three lanes

Propose three lanes, each with: the thesis this person can own, who it's for, the existing post that proves it, and the first three angles. A lane is not a topic ("AI agents"); it is a position ("memory systems ask the wrong first question"). Write them into `strategy.md` with a follower/inbound goal the user states, cadence (default 2–3 LinkedIn posts/week, X mirrored, 2–4 comments/day), and the "what good looks like" numbers from step 2.

## 4. Voice profile

Fill `voice.md`:
- Paste 15–40 of their real posts verbatim (best and newest first) under "Post exemplars", and 10–20 real comments under "Comment exemplars". These are the few-shot set for `write`; a description of their style is not a substitute.
- Derive the yaml block by looking at the exemplars: do they use em dashes at all, hashtags, closing questions, emoji; typical sentence length spread. Set `banned_extra` from words they never use and `allowed` for global-ban words they genuinely do.
- Write "How this person writes" as observations with evidence ("opens on the event: 'Ran a quick experiment with my team this weekend.'"), not adjectives.

## 5. My human and instructions

`my-human.md`: name, role, handles (the scout uses these to avoid suggesting their own posts), audience in one line, the public/private line (ask this explicitly: customer names? revenue? hiring? health?), time zone, and the capability mapping from the probe.

`instructions.md`: anything they said in this conversation that is a standing rule, dated.

## 6. First stories

Run `/open-stanley:mine` for the last 30 days immediately so the first draft can be source-first. Then offer one draft, from a fresh story, in a lane, and ask the one question that makes it theirs ("what do you actually believe about this?").

## 7. Gaps and recommended MCPs

From the capability probe, list what is connected and the gaps. For each gap, suggest one server from `skills/stanley/references/recommended-mcps.md` with its one-line install (e.g. Exa for fact-checking works with no key). Ask once; record `recommended_mcps: asked` in `my-human.md`. Also ask whether they want a human pass lane (`/open-stanley:humanpass`) and at which tier; record `humanpass:`.

## Output of onboarding (say this back)

Five lines: where the vault is; median + top post reason; the three lanes in one line each; what sources you can mine; the one draft you're offering. Then stop and wait.
