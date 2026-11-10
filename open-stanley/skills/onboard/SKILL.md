---
name: onboard
description: Set up Open Stanley for a person — work out from memory, connected sources, profiles and the machine which platforms, formats, languages and audience they have and confirm it in one message, say plainly which sources are missing, diagnose what they have tried (median engagement, what worked and why), offer strategies with evidence, propose three lanes, build a voice from their own posts plus the changes the evidence supports as experiments, check the profile strangers land on, and schedule the runs. Use when the user says "set up Stanley", "onboard me", shares their LinkedIn or X profile for the first time, asks "what should my content strategy be", or whenever the vault has no strategy.md or voice.md yet.
---

# Onboard

Goal: in one sitting, produce four short files the rest of the plugin runs on: `my-human.md`, `strategy.md`, `voice.md`, `instructions.md`, plus the first `stories/` and the scheduled tasks. The paid product did the diagnosis well; it then forgot the voice part. Do both.

Setup has to work without anyone explaining it. An early user installed the plugin, followed the written steps, got drafts that made no sense to him and stopped. Every reason was something setup should have asked or checked: which platforms and formats he posts in (short video and Threads, not LinkedIn text), which languages, where his context lives (chat apps and messengers the plugin was not reading), and how much his laptop can run (a daily run froze it). Ask, check, and say what is missing before the first draft.

## 0. Work it out first, then confirm once

Do not open with a questionnaire. Most of what setup needs is already readable: Claude's memory of the user, their connected sources (calendar, mail signature, Slack profile, docs), their public profiles and posts in the browser, and the machine itself. Read those first, then show one short proposal with your best guess for each item and why, and ask them to correct anything that is wrong. "I think this works for you: ... Tell me what to change" is one message; six questions are six chances to stop.

What to fill in, and where to find it:

- **Platforms** they post on or should: the profiles they are logged into in the browser, links in their bios and mail signature, where their past posts are. The plugin posts through the logged-in browser on any platform (`publish` §3b); do not steer them to LinkedIn. → `platforms:` in `strategy.md`.
- **Formats** they make: what their own best posts are (text, images, carousels, short video, articles). Short video turns the `video` mode on for weekly drafts. → `formats:`.
- **Languages**: the languages of their posts and of their messages. A second language is written in that language from the story, never translated line by line, and needs its own exemplars in `voice.md`. → `languages:`.
- **Audience and goal**: their role, company and customers from memory and sources; the goal from what the company sells (followers, inbound leads, credibility for direct sales, hiring, a personal brand). → `audience:`, `goal:`.
- **Drafts or questions**: default full drafts they edit; offer `drafting: questions` (the story, one question, two or three angles, no prose) if their own posts are already well written and frequent, or if they say they write themselves.
- **Likes**: `likes: ask` by default (the recap lists the comments that only need a like and likes them after a yes); offer `likes: auto` so it likes them itself. Never more than likes without a yes.
- **The machine**: read the RAM on the device (`sysctl -n hw.memsize` on a Mac, `free -g` on Linux) rather than asking. 8 GB or less gets the light schedule in step 8. → `machine:` in `my-human.md`.

Ask a question only for what nothing above can answer, and then one at a time. Creators they admire, if they mention any, go to step 3.

Setup has to work without anyone explaining it. An early user installed the plugin, followed the written steps, got drafts that made no sense to him and stopped. Every reason was something setup should have found out: the platforms and formats he posts in (short video and Threads, not LinkedIn text), his languages, where his context lives (chat apps and messengers the plugin was not reading), and his laptop (a daily run froze it).

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

Read `references/strategies.md` (its "From teardowns" and "From users" sections first; they grow) and offer the two or three that fit the step 0 picture and the diagnosis, each in one line with its evidence and its label (tested here, from a teardown, untested). If they named creators, run `/open-stanley:study` on one of them now and offer what it finds. They pick one main and at most one second; write `strategy:` and `strategy_second:` into `strategy.md`. The pick decides what the weekly run produces: text drafts, data graphics, video ideas, or questions.

Then propose three lanes, each with: the thesis this person can own, who it's for, the existing post that proves it, and the first three angles. One of the three, or a fourth, is the **atlas** lane (`/open-stanley:atlas`): posts from public data in their vertical that need no meetings or voice notes, so the account can post from day one while mining builds up stories; name the first three questions it would answer, with the famous name each ranking would carry. A lane is not a topic ("AI agents"); it is a position ("memory systems ask the wrong first question"). Write them into `strategy.md` with a follower/inbound goal the user states, cadence (default 2–3 LinkedIn posts/week, X mirrored, 2–4 comments/day), and the "what good looks like" numbers from step 2.

## 4. Voice: where they are, and where to take it

People come to this plugin because their posts are not getting read. Their current voice is the starting point, not the target. Build `voice.md` in two parts.

**Keep** (from their own words): paste 15–40 of their real posts verbatim (best by reach first, then newest) under "Post exemplars", and 10–20 real comments under "Comment exemplars". Derive the yaml block from them (em dashes, hashtags, closing questions, emoji, sentence length spread, `banned_extra`, `allowed`), and write "How this person writes" as observations with evidence. This is what makes a draft sound like them: their words, their rhythm, the things they know.

**Change** (from the evidence, not taste): a short list of what to do differently, each line with where it came from:
- from their own ledger: what their weaker posts share that their better ones do not (announcements, academic framing, a hook that hides the point, no name or number early);
- from their audience: what the people they want to reach respond to (read the comments and the posts those people share and engage with);
- from creators in their field, and in one field outside it: run `/open-stanley:study` on one or two (the ones they named, or ones who reach their audience), and take the moves that beat those creators' own medians;
- from `skills/stanley/references/research-linkedin-2026.md` where the platform data is clear.

Each change goes into `strategy.md` as an open experiment (variant vs their current habit, the metric, `min_n`), so the plugin tests it on their own posts instead of imposing it. The weekly tune promotes what wins and drops what does not. The goal is their own voice, getting better on numbers, not a borrowed one.

## 5. My human and instructions

`my-human.md`: name, role, handles (the scout uses these to avoid suggesting their own posts), audience in one line, the public/private line (ask this explicitly: customer names? revenue? hiring? health?), time zone, and the capability mapping from the probe.

`instructions.md`: anything they said in this conversation that is a standing rule, dated.

## 6. First stories

Run `/open-stanley:mine` for the last 30 days immediately so the first draft can be source-first. Then offer one draft, from a fresh story, in a lane, and ask the one question that makes it theirs ("what do you actually believe about this?").

## 7. The profile people land on, and the other gaps

A post that reaches strangers sends them to the profile. From the profiles read in step 2, check as a stranger would: does the first line of the headline or bio say who they are and for whom, is a lane from step 3 visible, is there one checkable proof, does the featured or pinned item show their best post or the next step. If not, offer a rewrite that a stranger understands at a glance; clarity first, their voice second. Change a profile only with a yes to the exact text, then reload and check it (`skills/stanley/references/verify-live.md`). The monthly check-in looks at it again.

Step 1b covered the sources for mining. For the rest, suggest one server per gap from `skills/stanley/references/recommended-mcps.md` with its one-line install (e.g. Exa for fact-checking works with no key). Ask once; record `recommended_mcps: asked` in `my-human.md`. Also ask whether they want a human pass lane (`/open-stanley:humanpass`) and at which tier; record `humanpass:`.

## 8. Schedule the runs (the same tasks for everyone; modes change what they do)

Create the standard scheduled tasks from `templates/scheduled-tasks/` (see `skills/stanley/references/scheduling.md`): soapbox 08:00, scout 10:00 and 22:00, recap 22:00, mine Saturday, weekly drafts Sunday, monthly check-in. What each task produces follows `strategy.md`, so the person switches with one sentence and the tasks stay the same:

- `drafting: questions` makes weekly drafts deliver prompts instead of prose.
- `formats` with short video makes weekly drafts include video ideas (`/open-stanley:video`).
- `schedule: light` (set automatically at 8 GB or less, or when they say a run made the computer slow): keep one scout at a time they are away, fold the recap into it, and move every browser run out of their working hours; say why (a run drives the same Chrome they work in).

Every task runs only while the computer is on and the desktop app is open; say that once, and how to keep it awake (lid open, a keep-awake app).

## 9. Team mode (when co-founders or a team use it together)

If they say others in the company will use the plugin too, ask for their names and public profiles and write `team:` into `my-human.md`. Then: `scout` puts teammates' new posts first (the cheapest reach is commenting on each other early), `mine` marks company stories `scope: company` so two people do not post the same story the same week (check the teammates' recent posts before drafting one), and each person keeps their own vault and voice. One shared voice for several people is how a team's posts start to sound alike.

## 10. Check the setup before saying it is done

Run through this and show the list with a yes or a fix for each: the vault folder is connected; `.stanley-scripts/VERSION` matches the plugin; `stanley-audit selftest` passes; the browser is reachable and logged in on each platform from step 0; the scheduled tasks exist with this vault folder attached (`list_triggers` where available); `my-human.md` has handles for every platform (the scout uses them to skip the user's own posts); sources counted in step 1b. Anything that says no is the first thing to fix, not a footnote.

## Output of onboarding (say this back)

Six lines: where the vault is; median + top post reason; the strategy they picked, the three lanes in one line each, and the first experiment from the voice's change list; what sources you can mine and what is missing; which runs are scheduled and when; the one draft (or, for `drafting: questions`, the one question) you're offering. Then stop and wait.
