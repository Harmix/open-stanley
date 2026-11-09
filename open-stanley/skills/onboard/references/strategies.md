# Strategies to offer at setup

Onboarding offers two or three of these, picked by the person's audience, platforms, formats and how much time they have. The choice decides what the scheduled runs produce: text drafts, data graphics, video ideas or questions. Each one says where its evidence comes from. "Tested here" means the plugin's own users have numbers for it; "from a teardown" means a creator page in this plugin; "untested here" means general knowledge only, so say that when you offer it.

When the user adds creator teardowns (`docs/creators/`, `skills/study/references/creators-latest.md`, or `shapes/` in their vault), read them first: a strategy backed by a creator the user admires beats one from this list. When someone names a creator ("I like how X posts"), run `/open-stanley:study` on them during setup and offer the strategy it finds.

## 1. Story first (tested here)

For: anyone with a real working week (founders, operators, researchers, salespeople) on LinkedIn or X.
What it is: every post starts from something that happened, found in their meetings, chats and mail, with a name people know in the first line when there is one. The first user's two biggest posts were "I asked / I saw" stories with an institution's name in the first line and a real screenshot (87,288 and 31,324 impressions on an account under 5K followers); his announcements stayed in his network.
Set up: lanes from their own work, `mine` weekly, the morning Soapbox question, weekly drafts as text, 2 posts a week.
Needs: at least two connected sources (meetings and messages are the best pair). Without them this strategy runs dry; say so.

## 2. Data maps for a vertical (from a teardown, tested here)

For: anyone selling into an industry who needs credibility there (real estate, mining, manufacturing, healthcare, a city's startup scene). Works with no personal stories at all.
What it is: "Top N <things the audience knows> by <one money or size number>" as a treemap with real logos, three details behind the names, and "what should I map next". A mining data designer's best post was "Top 30 copper miners by market cap" (1,342 reactions, 70 reposts on under 5K followers); the first user's "Top 17 Toronto AI startups by money raised in 2026" was built the same way.
Set up: the `atlas` lane weekly, the data check in `skills/atlas/references/data-check.md`, local or industry data first.

## 3. Habit, then the tool (from a teardown: Dharmesh Shah)

For: founders whose product is something they use themselves.
What it is: a habit they have kept for years, the annoying part, the exact request they gave their own product pasted in, the obvious objection answered, the price last. His best post in 45 was this shape, about twice the next one; his reshares of other people's praise were all in his bottom quarter.
Set up: one post every two weeks in this shape inside the story-first lane; never reshare praise.

## 4. Short essays and observations (from a teardown: Paul Graham)

For: people with opinions and a following on X, or people who write well and want to.
What it is: one observation, said plainly, often from a conversation, no hook formula. Works on X and Threads.
Set up: X and Threads as the main platforms, short posts, the comment lane weighted up.

## 5. Founder life on video (untested here)

For: people on Instagram, TikTok, YouTube Shorts or Threads who want followers to know them as a person first, with the product in the background.
What it is: short vertical videos from their real days (a trip, a meal, a move, a hard week at work), each one copying a format that already works on the platform, with the business story mixed in sometimes. The bottleneck is usually the idea and the reference, not the filming.
Set up: the `video` skill: weekly video ideas from mined stories, each with a reference reel found on the platform, a shot list, the spoken lines in their voice, on-screen text and a caption; editing with HyperFrames when installed. Text posts for Threads from the same stories.
Ask: which accounts they like on that platform, so the references come from formats they would actually shoot.

## 6. Questions, not drafts (untested here)

For: people who write well themselves and do not want a model's draft, but run out of things to say.
What it is: the plugin finds the story and asks the one question that gets the post out of them, and gives two or three angles; it never writes the prose unless asked.
Set up: `drafting: questions` in `strategy.md`; weekly drafts become weekly prompts; the audit still runs on what they write.

## 7. Industry field notes for direct sales (untested here)

For: people whose sales happen in person (office visits, events, calls) and who post so that a prospect who looks them up sees someone who knows the industry.
What it is: short notes from the field (what a broker said about this month's market, what an office visit showed), plus data maps of the local market, plus comments on the industry's local voices.
Set up: lanes around the industry, `scout` pointed at the industry's people, atlas monthly with local data, fewer posts and more comments.

## 8. Memes and jokes for a technical audience (untested here)

For: people whose audience shares an inside world (developers, security, AI engineers). Some co-founders of developer tools post mostly memes.
What it is: a joke about a situation every reader has lived, as text or a simple image the user makes or screenshots. Never a copyrighted character or a stock meme with a brand on it.
Set up: an occasional format inside another strategy, not a whole strategy, until the ledger shows it works for this person.

## How to offer them

Say which two or three fit and why, in one line each, with the evidence and its label. Ask them to pick one main strategy and at most one second. Write the pick into `strategy.md` as `strategy: <name>` and `strategy_second: <name>`, then set the lanes, formats, platforms, cadence and the scheduled tasks to match. Revisit at the monthly check-in with the ledger's numbers.
