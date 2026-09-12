# Open Stanley — Research Report

*Compiled 8 Sep 2026 from (a) Nazar's full Stanley Telegram export (4 Aug – 7 Sep 2026, 370 messages, 103 screenshots), (b) public sources on Stanley / Stan, (c) live reads of Dharmesh Shah, Yamini Rangan, Yuriy Zaremba and Vitalii Dodonov's current LinkedIn and X feeds, (d) the 2026 literature on AI-text detection and platform ranking. Raw sub-reports are in `research/`.*

---

## 1. How Stanley actually works (reverse-engineered from the chat)

### 1.1 The product surface

Stanley is a chat-first agent (Telegram, iMessage, SMS, web) with a web dashboard at `x.getstanley.ai`. Every action Stanley takes ends in a short link into that dashboard (`/go/...`), and the dashboard is where the real state lives. The screenshots show that the dashboard is essentially **a markdown wiki about the user**, with a sidebar of:

- **My Human** — profile/identity
- **Instructions** — standing rules the user gave (voice, cadence, filters)
- **Strategy** — the strategy doc ("target: 1,000 followers, pillars: contrarian lessons / product decisions / behind-the-scenes engineering reality")
- **Stories** — an index plus one file per story, each tagged by topic, with a one-line "lesson" and a "Needs material" list of story ideas Stanley wants raw material for. It is refreshed weekly by re-reading the user's posts.
- **Uploads / Photos** — raw material the user dropped in
- A **drafts pile** (the `/write?post=...` pages), a calendar, analytics, a "rituals" section, and an "earn" page

This is important: the whole "AI head of content" is a chat loop over a small set of markdown files plus a job scheduler. There is nothing here that a Claude plugin with a folder of `.md` files cannot reproduce.

### 1.2 The loop Stanley runs

1. **Onboarding**: scrape the LinkedIn profile URL, compute median engagement per post, name the 2–3 top posts and why they worked, propose 3 content lanes, offer a first draft. (Nazar's onboarding read was genuinely good: "median ~36 engagements, fundraise post hit 72 because it told a story, Google Cloud post hit 123 because it made a claim about the future".)
2. **Draft → edit link → approve → post** on LinkedIn and X (X as a thread when >280 chars and no Premium).
3. **Scheduled jobs** the user opted into during the month:
   - 10:00 and 22:00 daily "scan X + LinkedIn feed, pick 2–3 posts worth commenting on, draft comments"
   - 22:00 daily "wrap" (an image card: "Today, 131 saw my content and 2 reacted") and later a text recap
   - 08:00 "rituals": *Soapbox* (a morning question in the user's lane, "voice-note 2 min and I'll turn it into a post"), *Autonomous* (offer to draft a week of posts every Sunday), *Repackage Old Posts*, *Orbit Celebration* (who engaged most this month, with a graph image), *Ways to Earn* (referral 20%, gift codes, up to $500/post for mentioning Stanley), a monthly "strategy check-in"
   - ~08:55 "drafts tidy" (archive stale drafts, resurface one strong forgotten draft)
   - Sunday 10:00 weekly drafts
   - A "trend alert" job, a "who's engaging back" tracker
4. **Memory**: stories index, a dedupe blacklist of surfaced URLs (added only after Nazar complained), the instructions file.

### 1.3 Integrations and limits observed

- LinkedIn: scraped, not API. Posting works. Feed search hits a **monthly quota** (twice in one month: 25 Aug, 27 Aug) after which Stanley stops scanning LinkedIn entirely.
- X: official API. Can post and thread. **Cannot reply or quote-tweet accounts that have not mentioned you** (API limitation, not Premium) — so the entire "comment on X" job degrades to "paste this yourself".
- Meeting transcripts: only Fathom, Granola, Wispr Flow, plus Notion/Drive/Slack. **No custom MCP servers** ("logged the request with the team").
- Payments: Stripe links; price negotiated in chat ($59 → $29 → $19 → $10 in four messages, in exchange for a testimonial, a post, and 3 intros).

### 1.4 Where it broke (the failure log)

Counting from the export, over 35 days Stanley shipped 5 original posts (Cloudflare wallets, the Google A2A attack, "the person whose job you're automating", the note-taker overlap experiment, and prompt-hacks nostalgia; two of them substantially rewritten by Nazar), plus one standalone tweet, and Nazar posted roughly 20 comments manually from Stanley's drafts, editing most of them down. Against that:

| Failure | Evidence | Root cause |
|---|---|---|
| Drafts that copy the user's own past posts | Draft 1 on day 1 was "almost a copycat" of an existing LinkedIn post | Generation conditioned on the user's corpus without a "don't re-say what you already said" check |
| Stale "news" presented as fresh | 2024–25 papers cited in 2026; news "I saw two weeks ago" | No recency gate; no source date check |
| Wrong lesson from a story | GPT-5.6 math-conjecture draft "got the wrong lesson" | Drafting before the user has confirmed the *claim* |
| Sounds like AI | Said explicitly 7 times ("sounds like AI as hell", "learn true PG style, use simple words") | Model generates the central claim and the phrasing; short choppy lines, tricolons, "not X, it's Y", tidy conclusions |
| Fabricated authority | "recent literature shows" with no citation; later admitted "the subagent turned your observation into a vague line" | No citation requirement on factual claims |
| Scheduled jobs not firing / half-firing | 10pm on 13 Aug, 10am on 15 Aug missing; LinkedIn skipped in 4 of the first 6 scans; "coming in a separate message" that never came | No run log, no self-check that the job produced what was promised |
| Duplicates | Same three LinkedIn posts surfaced on 15 Aug and again 19 Aug; an "older version" draft resurfaced after the post shipped | Dedupe list added reactively, per-URL only |
| Suggested commenting on the user's own posts | 28 Aug, 30 Aug (twice), 4 Sep — four times | Scanner never checked author == user |
| Comment drafts off-topic | "bad selection of posts", "not relevant" — most scans; the one Nazar loved (Matt Rothenberg, 4.9k likes) was one he found himself | Relevance filter too narrow (keyword: "agent memory") and no "adjacent viral topic where your angle is a natural reply" heuristic until the user spelled it out |
| Editor UX bugs | Hook silently deleted on rewrite; broken `/write` link | — |
| Bold recap numbers, no insight | Daily recap: "X: 5 followers, no posts" for weeks | Reporting, not coaching |

And the strongest independent confirmation: **Yuriy Zaremba (AiSDR CEO) posted on 4 Sep 2026** that he is testing "an AI agent for posting on X" that he fed his LinkedIn posts, Fathom calls and Slack (Stanley's exact integration list) and got "same stories repeated several times; fake stories that fit the viral pattern but have nothing to do with my life; it keeps happening despite recurring feedback." That is the same three failures Nazar hit — repetition, fabrication, and feedback that doesn't stick.

### 1.5 What Stanley does well (keep these)

- The **proactive cadence**. Morning Soapbox question + "voice-note 2 min and I'll turn it into a post" is the best mechanism in the product, because it extracts human-origin material before drafting.
- The onboarding diagnosis and the three-lane strategy.
- The stories index with a "needs material" backlog.
- Meeting-transcript mining: from the Nick/Shonn Li onboarding transcript it found the "person whose job you're automating won't help you" angle in seconds, and that became the best post of the month.
- The 10pm scan format when it works: post link + why + paste-ready comment.
- Instant learning-from-edits acknowledgements ("these edits make the pattern very clear: zero setup sentences, grounded questions, natural vocabulary"). It just failed to persist them.

---

## 2. Stanley the business (what to copy about distribution)

Corrections to what the chat implied: Stanley is not a standalone startup. It is a product of **Stan** (Find Community, Inc., ~$40M ARR link-in-bio platform), co-founded by John Hu (CEO) and **Vitalii Dodonov (CTO, Toronto)**. Public pricing is $47/mo (Instagram app) and $149/mo (LinkedIn); the negotiate-in-chat pricing is a Stanley-for-X mechanic. From Vitalii's own posts this week:

- "**I made $3.42M in August 2026. Stanley $243K, Stan Store $2.99M, Stanley Studio $2.1K**" (X, 2 Sep 2026, 35.8k views).
- "**20,000 sign-ups a month, 11.4% free-to-paid, ~24% churn**, stabilizing around 9,000 paying customers"; a power user "replaced $3–5k/mo ghostwriting teams" but would not pay $1,000/mo "in its current state"; they introduced a $1,000 plan anyway (LinkedIn, 5 Sep 2026).
- "I'd rather have 500 founders who know what Stan is than 500K impressions from strangers. That's the whole marketing strategy."

How they distributed (all sourced in `research/stanley-distribution.md`):

1. **Built it in public in 14 days** in a London "hacker house": 17 LinkedIn posts during the sprint, 500+ beta applications, 200+ paying by day 14. The launch-day LinkedIn post alone: 2,000+ comments, ~$200K ARR.
2. **Hyper-personalized cold email to marquee creators** (Justin Welsh, Lara Acosta, Steven Bartlett) with "I spent 3 days analyzing your competitors" as the hook; Welsh's quote "this knows me better than Claude or ChatGPT" became the marketing.
3. **Cross-sell into 80,000 existing Stan creators**; 20% lifetime referral; PR Newswire releases each built around one dramatic number (20M views from one video, +80K followers).
4. Product Hunt #2 of the day (Stanley for X, 22 Apr 2026, 406 upvotes), a Business Insider as-told-to essay, podcasts, and now an in-person "Launchpad" accelerator with a $500 referral bounty.
5. Inside the product: the "Ways to Earn" ritual (20% rev share, gift codes, up to $500/post for mentioning Stanley) turns every user into distribution.

The honest read: **the moat is distribution and cadence, not technology**. The backend was "vibe coded" on Claude in two weeks. Every competitor review says the same thing ("coaches more than it writes", "generic templates", "no memory"), and the App Store 1–2★ reviews say "can't remember things from a few lines prior".

---

## 3. What the best creators actually do (live feeds, Sep 2026)

### Dharmesh Shah (HubSpot CTO; 1.19M LinkedIn, ~500K X)

- ~2 LinkedIn posts/week, 70% plain text. Formats: `BREAKING NEWS:` + a joke, `Woo hoo!` + milestone, `How I Grow Better With YouSpot: Episode N`, one-line aphorisms ("Fortune favors the focused.").
- His best recent LinkedIn post (626 reactions, 121 comments) is 90 words: "product manager → product builder → product entrepreneur". His 145-comment post is a 300-word story about losing a 15-year argument on signup friction. Neither has a hook formula; both open with "One of..." or "10+ years ago...".
- He now writes **"p.s. It's sad that I have to say this, but AI was not at all used to write this or edit it. p.p.s. I actually like AI and use it a lot."** and "Wrote it myself. No AI." on the pricing page tweet. The most-followed AI-builder on LinkedIn is signalling *human authorship* as a feature. That is the environment Open Stanley must write into.
- On X his 1.35M-view post was a plain product announcement starting "Woo hoo!"; everything else is 15–50k views. He answers replies and uses `#recommend` as a personal tag. Uses X for raw, late-night, more technical posts; LinkedIn gets framing.
- Advice he encodes in his own product: "The first line determines if anyone reads the rest"; each platform gets native content; voice must be pre-selected so output sounds "like you, not generic AI garbage".

### Yamini Rangan (HubSpot CEO; LinkedIn-only in practice)

- Weekly-ish, text-only, 150–300 words, always **situation → what I saw → what it means → what we're doing at HubSpot**. Opens with a personal past ("Early on in my career I had 10 direct reports"; "I started my career in sales"). Ends with a values line, no question, no hashtags now.
- Her historically best posts are admissions of being wrong (498 comments) — an order of magnitude above product posts. Encodable rule: for a CEO voice, admitted fallibility beats achievement.

### Yuriy Zaremba (AiSDR CEO, YC S23, Ukraine)

- Near-daily, every post with an image/screenshot, short lines, exact un-rounded numbers ("1,239,964 emails sent"), named failures ("3 biggest screw-ups in AiSDR history"), his own inbox as content, and a running "09.09" teaser across posts. Engagement per post is modest (25–60 reactions) but the cadence and specificity build the brand; comments run high relative to reactions (30 comments on 28 reactions).
- His stated stance: AI content is fine when expectations are calibrated; he uses AI for research and iteration, not for the claim. And, as above, he publicly documented the AI-poster failure modes.

### Vitalii Dodonov (Stan CTO)

- Build-in-public with real numbers (revenue by product, churn, conversion), one contrarian operating lesson per post ("Indecision is the real enemy"), and every post carries a CTA to a concrete thing (Launchpad, Stanley). 48–182 comments per LinkedIn post; on X 1–5k views per post, with the revenue post at 36k.

### The pattern across all four

The claim is always something only that person could know: a number from their dashboard, a mistake they made, a debate they lost, an email they got. Structure is loose. Hooks are plain ("One of my favorite books...", "Someone tried to hack my GSuite today."). The most-engaged posts are the least formatted. None of them use the LinkedIn-guru scaffolding (one-line paragraphs, "Here's the thing", "Agree?").

---

## 4. Platform reality in 2026 (what the "black box" actually is)

Details and sources are in `research/detection-and-platforms.md`; the load-bearing facts:

1. **LinkedIn now demotes AI-generic posts silently.** From 20 May 2026 an ML classifier (claimed 94% accuracy, no published false-positive rate) suppresses flagged posts from the recommendation feed while leaving them visible to 1st-degree connections. 31 Jul 2026: a "Seems like AI slop" report button, clicked by ~1M users in the first month; LinkedIn removed its own "Enhance your post" writer. Named tells include "it's not X, it's Y" and comment bots that restate the post. LinkedIn also rebuilt its feed (Mar 2026) as an LLM retrieval + generative-recommender ranker trained on 1,000+ interactions per member, with **dwell** as a first-class signal and *shown-and-skipped* posts as hard negatives.
2. **X does not penalize AI-assisted writing; it hunts bot accounts** and rate-limits automation. Premium is effectively required (Buffer, 18.8M posts: ~10x reach per post). Replies the author answers carry the single largest ranking weight. The first 30 minutes decide ~70% of reach.
3. **Anthropic watermarks Claude text since 2 Aug 2026** (SynthID-Text; Claude, Claude Code, Cowork and the API; no opt-out; detector available to regulators, media, fact-checkers, researchers, educational institutions and compliance-obligated enterprises). Anthropic's own wording: "Light editing probably won't remove the watermark completely; a complete rewrite where every word is replaced will," and when Claude proofreads a person's text "there's very little (if anything) for the watermark to attach to." Short posts carry weak signal. Consequence for this plugin: the fewer model-generated words in the final post, the better; a paid human "polish" of a model draft removes nothing, a human writing from a brief removes everything. (Verified on anthropic.com/news/claude-text-watermark, 8 Sep 2026.)
4. **Detectors measure RLHF style, not machine authorship.** Base-model text scores ~97% "human" on GPTZero; instruct-model text from the same weights scores ~30%. Detectors collapse (TPR 0.94 → 0.15) on *human-origin text rewritten by an LLM* but hold (0.83) on *LLM-origin text rewritten by an LLM*. Commercial "humanizers" are themselves detectable (Pangram ships a humanizer classifier). Practical consequence: **start from human material and let the model edit; never generate the claim and then humanize.**
5. **Stylometric tells are measurable**: excess vocabulary (delve, intricate, pivotal, underscore, showcase, realm, testament, landscape, leverage, seamless), em-dash density ~3–6x human, tricolons, negative parallelism, uniform sentence length, editorializing tails ("...highlighting the need for"), weasel attribution ("experts say"), closing audience question, zero proper nouns/numbers/dates.
6. **Prevalence**: Pangram measured 41% of LinkedIn long-form posts as fully AI-generated (Apr–Jun 2026); LinkedIn produced 62% of all AI content in the sample. Being the human-sounding post in that feed is now the whole game.
7. Encodable numbers (with the caveat that sources conflict, see the sub-report): LinkedIn 1,300–1,900 chars sweet spot, hook self-contained in ~140 chars, zero hashtags, no links in body (and link-in-first-comment is now penalized too), 3–4 posts/week not daily, Tue–Thu 8–10am local, native documents > multi-image > video > text by engagement rate but plain text still wins at authority scale. X: single long post over threads unless the story is sequential (5–7 tweets max), link in first reply, reply to every reply, 15–20 substantive replies/day to accounts 5–20x your size within 5 minutes of their posting.

---

## 5. Human-in-the-loop options for "rewrite so it doesn't read as AI"

- The cheap, correct version is **the user's own edit pass with diff capture**: every `(draft, final)` pair is the highest-information voice signal there is. Nazar's edits in the export (e.g. removing "innate", cutting setup sentences, adding "how do you know which project context is still relevant?") are exactly this signal, and Stanley discarded them.
- **Upwork shipped an official MCP server (10 Aug 2026)**: agents can search, shortlist, post jobs, manage milestones; a human must confirm writes and finalize payment on upwork.com. That is the only marketplace with a real, OAuth'd agent interface. `human-mcp.io` (15% fee, escrow, explicitly lists proofreading) and Toloka's Tendem MCP are the agent-native options with unverified liquidity / unpublished pricing. Amazon MTurk shuts down 30 Sep 2026. Fiverr has no official MCP. RentAHuman is physical-world tasks; don't build on it.
- Editing services for LinkedIn ghostwriting run $50–500/post or $500–10k/mo, human-brokered, no API.
- Recommendation: tier 1 = own approval via MCP elicitation / Slack; tier 2 = a retained editor in the same Slack channel; tier 3 = Upwork MCP for on-demand sourcing; Prolific for periodic "do 100 readers think this is AI" measurement rather than for editing.

---

## 6. Ecosystem: what already exists (don't rebuild, integrate or outdo)

- **`sergebulaev/linkedin-skills`** (MIT, 582★): 11 Claude/Codex skills including a Post Audit against algorithm + AI-detection rules and a Humanizer with a multi-detector spread test (no Pangram). Installable via `/plugin install linkedin-skills@linkedin-skills`, `codex plugin marketplace add`, `npx skills add`. Strong on writing rules, has no scheduling, no memory, no scouting, no learning loop.
- **SocialClaw** (MCP + skill, 12 networks, free tier), **Postiz** (28+ platforms, OpenClaw skill), **post-bridge**, `bird` (X CLI on ClawHub), `linkedin-post-writer` on ClawHub. These solve *publishing*, not the head-of-content loop.
- Claude Code **Routines** (14 Apr 2026: scheduled/API/webhook triggers on Anthropic's infra, Pro 5/day, Max 15/day) and **Cowork scheduled tasks** (hourly/daily/weekly/weekdays; each run is its own session with connected tools; cannot touch local folders). Both exist today and are what Stanley's cron jobs map onto.
- **Agent Skills open standard** (Dec 2025; adopted by OpenAI Codex, VS Code/Copilot, Gemini CLI, Kiro, Goose, etc.; ClawHub's SKILL.md format is convergent). One SKILL.md folder can ship to Claude, Codex, and OpenClaw. `claude-community` marketplace has open submission with automated safety screening; ClawHub is MIT-0 only, no paywalls.
- **skill-creator** (3 Mar 2026) ships evals, benchmarking, blind A/B comparator agents, and description optimization — the acceptance gate for community contributions is already built.
- Cautionary tale: the Vercel plugin (Apr 2026) shipped always-on telemetry of full bash commands and consent solicited by injecting an `AskUserQuestion` into Claude's context; it was ripped out under public pressure. Any community-learning loop has to be opt-in, content-free, and native.

---

## 7. The one-paragraph conclusion

Stanley is a 14-day Claude wrapper with a markdown wiki, a cron scheduler, and a great proactive cadence, sold at $47–149/mo into an existing audience, doing ~$243K/month with 24% churn. Its failures (repetition, fabrication, AI voice, feedback that doesn't persist, jobs that don't fire, no custom integrations) are all failures of *state and verification*, which is precisely what an agent running on the user's own machine with the user's own MCPs, a git-backed vault, and a diff-learning loop can do better. The 2026 platform environment (LinkedIn's silent AI-slop demotion, "no AI was used" as a status signal from the biggest creators) makes "human-origin material, model as editor, human as final pass" not just the safer design but the only design that will keep reach. The distribution playbook to copy is Stan's: build it in public, launch with a number, DM the 20 people whose endorsement matters, and make every user's success post the marketing.
