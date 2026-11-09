---
name: onboard
description: Set up Open Stanley for a person — ask which platforms, formats and languages they post in, check which sources are connected and say what is missing, diagnose their posts so far (median engagement, what worked and why), offer strategies from creators who do it well, propose three content lanes, build a voice profile from their own posts, and schedule the runs for their machine. Use when the user says "set up Stanley", "onboard me", shares their LinkedIn or X profile for the first time, asks "what should my content strategy be", or whenever the vault has no strategy.md or voice.md yet.
---

# Onboard

Goal: in one sitting, produce four short files the rest of the plugin runs on: `my-human.md`, `strategy.md`, `voice.md`, `instructions.md`, plus the first `stories/` and the scheduled tasks. The paid product did the diagnosis well; it then forgot the voice part. Do both.

Setup has to work without anyone explaining it. An early user installed the plugin, followed the written steps, got drafts that made no sense to him and stopped. Every reason was something setup should have asked or checked: which platforms and formats he posts in (short video and Threads, not LinkedIn text), which languages, where his context lives (chat apps and messengers the plugin was not reading), and how much his laptop can run (a daily run froze it). Ask, check, and say what is missing before the first draft.

## 0. Six questions first (one message, multiple choice where the tool allows)

Ask these together, before reading anything, with an "other" option each. Record the answers in `my-human.md` and `strategy.md`; every later step reads them.

1. **Platforms**, as many as apply: LinkedIn, X, Threads, Instagram, TikTok, YouTube Shorts, Substack (Notes or newsletter), Bluesky, Reddit, a blog. → `platforms:` in `strategy.md`. The plugin posts through the user's logged-in browser on any of them (`publish` §3b), so do not steer them to LinkedIn.
2. **Formats** they will actually make: text posts, posts with images or charts, carousels, short video, long articles, memes. → `formats:`. Short video turns on the `video` skill.
3. **Languages**, and whether each language is the same account or a separate one. → `languages:`. Drafts come in the first language; a second language is a rewrite in that language's voice, not a translation, and needs its own exemplars in `voice.md`.
4. **Who should care and what for**: the audience in one line (industry, role, city) and the goal (followers, inbound leads, credibility for direct sales, hiring, a personal brand). → `audience:` and `goal:`.
5. **How much help with the writing**: full drafts they edit, or questions and angles only and they write ("I write well myself, I just run out of things to say"). → `drafting: drafts | questions`.
6. **The machine**: laptop RAM (8 GB is tight), whether it stays on and open during the day, and when they would rather the runs happen. → `machine:` in `my-human.md`; decides the schedule in step 8.

If they named creators they like ("I want to post like X"), write them down; step 3 studies them.

## 1. Vault and mode

Default is **laptop mode**: the vault is a plain folder inside a desktop-synced Google Drive (or iCloud/Dropbox) folder, and every scheduled task runs on the user's computer with that folder connected and their browser available (`skills/stanley/references/scheduling.md`). Ask where their synced Drive lives (macOS: `~/Library/CloudStorage/GoogleDrive-<account>/My Drive/...`), create `stanley-vault` there with `skills/stanley/scripts/stanley-vault init <path>`, and have them connect the folder to the chat. Record `mode: laptop`, `vault: local`, `vault_path: <path>` in `my-human.md`.

Offer **cloud mode** only if they say runs must happen with the laptop closed, and say what it costs (Drive-mirror runs are slower and browser work waits for the drain). Then `vault: drive` with the folder id, or `notion`. Do not offer git to Cowork users; scheduled tasks cannot clone a private repo (`vault-backends.md`).

Explain in one line where the vault lives and that it is plain markdown they can edit.

## 1b. Sources, and say plainly when there are too few

Probe the capabilities (`skills/stanley/references/capabilities.md`) and count the sources that hold the user's own week: `meetings`, `messages`, `mail`, `docs`, `memory`, `calendar`, `code`, plus chats reachable in the logged-in browser (Telegram Web, WhatsApp Web, LinkedIn messages) if they agree to them being read. Mining finds stories only where it can read, and the morning question has nothing to ask about without them.

- **Two or fewer**: say it in one plain line ("I can only read your calendar, so the weekly drafts will be thin and generic"), then name the two connectors that would help most for this person, in this order: their meeting notetaker (Pam Memory & Notetaker, Fathom, Granola, Fireflies), their team chat (Slack, Teams, Discord), sent mail, their docs. Offer to wait while they connect them. Do not start drafting from nothing; that is how drafts turn into nonsense.
- **Chats in messengers**: if they say their work talk happens in Telegram or WhatsApp, offer to read them through the logged-in web app in the browser, only the chats they name, and record the list in `my-human.md` as `browser_sources:`.
- **Their main assistant is ChatGPT**: suggest exporting their ChatGPT history (ChatGPT → Settings → Data controls → Export) and asking Claude to fill its memory from it, so the plugin knows their company, people and projects from the first run. Check what Claude's memory already says before suggesting it.
- **Coding agents**: if they build in public, their Claude Code and Codex session transcripts on this machine are a source too (`mine`, source `code`).

Record the count and the gaps in `my-human.md` (`sources: meetings=pam, messages=slack, ...`).

## 2. Read what they've posted (no questionnaire)

Read the analytics pages first, the feed second. The feed shows what is recent; the analytics show what worked. Confusing the two is how the first onboarding named the wrong best post (see `references/onboarding-misses.md`).

With the `browser` capability (logged in as the user), in this order:

1. **LinkedIn creator analytics, top posts by impressions**: `https://www.linkedin.com/analytics/creator/top-posts/?metricType=IMPRESSIONS&timeRange=past_365_days`. It lists every post of the last year with full text, reactions, comments, reposts and impressions, sorted by reach. Read it with `get_page_text` (the "Top performing posts" widget on the overview page often never loads; the `top-posts` URL does). Then the same URL with `metricType=ENGAGEMENTS`.
2. **The overview** `https://www.linkedin.com/analytics/creator/content/?timeRange=past_365_days` for the totals (impressions, reactions, comments, saves, sends) so you can say what share of the year's reach one post carried.
3. **Recent activity** (`/in/<handle>/recent-activity/all/`) only for the last 30 comments and for posts older than the analytics window.
4. **X**: the profile page and `x.com/<handle>/with_replies`, plus `analytics.x.com` if Premium.
5. **Every other platform from step 0**: the profile grid or feed in the browser (Instagram, TikTok, YouTube Shorts, Threads, Substack). Read views, likes, comments and saves where the page shows them, and for video, the opening seconds and the format of the three most watched. A person new to a platform has no history there; say so and lean on step 3.

If no browser is available, ask them to paste 10–20 posts and, separately, "which post do you think did best, and why?"

Before you diagnose, ask that same question anyway, in one line: **"Which of your posts do you think did best?"** Their answer is a check on your read: if the post they name is not in your top three, you missed something. Go back to the analytics, search their posts for it (`/search/results/content/?keywords=<phrase>` with their name), and only then write the diagnosis.

Save the raw pull to `inbox/own-posts-<date>.md` so you never scrape twice, and seed `ledger/posts.jsonl` from it (one line per post, impressions included, dates exact where the share id gives them: `date = epoch_ms(id >> 22)`).

Compute and tell them, in five lines:
- median engagement and median impressions per post on each platform;
- the top post **by reach** and the top post **by pull** (reactions+comments), named separately if they differ, each with the one reason it worked (a story, a claim about the future, a hand-over-the-system how-to). A post that carried half the year's impressions with 24 reactions is a different lesson from a post with 107 reactions and 100 impressions: the first left the network, the second was the network congratulating them;
- the bottom pattern (event announcements, paper shares with academic framing, "excited to attend");
- what the audience that should care is not seeing.

This diagnosis is the most-liked thing the paid product did; keep the numbers exact and the reasons blunt. Never quote a number you did not read on a page this session. If a metric is missing, say "no number" rather than estimating.

## 3. Strategy, then three lanes

Offer two or three strategies from `references/strategies.md` that fit the step 0 answers and the diagnosis (story first, data maps, habit then the tool, short essays, founder life on video, questions not drafts, industry field notes, memes), each in one line with its evidence and whether the plugin has tested it. If they named creators, run `/open-stanley:study` on one of them now and offer what it finds. They pick one main and at most one second; write `strategy:` and `strategy_second:` into `strategy.md`. The pick decides what the weekly run produces: text drafts, data graphics, video ideas, or questions.

Then propose three lanes, each with: the thesis this person can own, who it's for, the existing post that proves it, and the first three angles. One of the three, or a fourth, is the **atlas** lane (`/open-stanley:atlas`): posts from public data in their vertical that need no meetings or voice notes, so the account can post from day one while mining builds up stories; name the first three questions it would answer, with the famous name each ranking would carry. A lane is not a topic ("AI agents"); it is a position ("memory systems ask the wrong first question"). Write them into `strategy.md` with a follower/inbound goal the user states, cadence (default 2–3 LinkedIn posts/week, X mirrored, 2–4 comments/day), and the "what good looks like" numbers from step 2.

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

Step 1b already said what is missing for mining. Here, for the rest: For each gap, suggest one server from `skills/stanley/references/recommended-mcps.md` with its one-line install (e.g. Exa for fact-checking works with no key). Ask once; record `recommended_mcps: asked` in `my-human.md`. Also ask whether they want a human pass lane (`/open-stanley:humanpass`) and at which tier; record `humanpass:`.

## 8. Schedule the runs for their machine

Create the scheduled tasks from `templates/scheduled-tasks/` (see `skills/stanley/references/scheduling.md`), matched to the answers:

- **Standard** (16 GB or more, laptop open in the day): soapbox 08:00, scout 10:00 and 22:00, recap 22:00, mine Saturday, weekly drafts Sunday, monthly check-in.
- **Light** (8 GB, or "it froze"): one scout a day at a time they are away from the computer (lunch or evening), recap folded into that run, mine and weekly drafts on the weekend, and no browser runs during their working hours. Say why: a run drives the same Chrome they work in.
- **Questions only** (`drafting: questions`): weekly drafts become weekly prompts; keep scout and recap.
- **Video** (`formats` has short video): add the weekly `video` ideas run after mine.

Every task runs only while the computer is on and the desktop app is open; say that once, and how to keep it awake (lid open, a keep-awake app).

## 9. Team mode (when co-founders or a team use it together)

If they say others in the company will use the plugin too, ask for their names and public profiles and write `team:` into `my-human.md`. Then: `scout` puts teammates' new posts first (the cheapest reach is commenting on each other early), `mine` marks company stories `scope: company` so two people do not post the same story the same week (check the teammates' recent posts before drafting one), and each person keeps their own vault and voice. One shared voice for several people is how a team's posts start to sound alike.

## 10. Check the setup before saying it is done

Run through this and show the list with a yes or a fix for each: the vault folder is connected; `.stanley-scripts/VERSION` matches the plugin; `stanley-audit selftest` passes; the browser is reachable and logged in on each platform from step 0; the scheduled tasks exist with this vault folder attached (`list_triggers` where available); `my-human.md` has handles for every platform (the scout uses them to skip the user's own posts); sources counted in step 1b. Anything that says no is the first thing to fix, not a footnote.

## Output of onboarding (say this back)

Six lines: where the vault is; median + top post reason; the strategy they picked and the three lanes in one line each; what sources you can mine and what is missing; which runs are scheduled and when; the one draft (or, for `drafting: questions`, the one question) you're offering. Then stop and wait.
