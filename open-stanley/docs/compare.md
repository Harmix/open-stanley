# Open Stanley compared with the paid "AI head of content" tools

Written from the tools' own pages, their public MCP docs and third-party reviews, read on 7 November 2026; prices change, check theirs. This page is also honest about what they do better. If something here is out of date, open an issue; the comparison is a claim this repo makes in public.

## The thing that changed in autumn 2026

Every paid tool in this category now ships an MCP server: Stanley (`xapi.getstanley.ai/mcp`, one `message_stanley` tool), Taplio (MCP V2, comment drafting), Supergrow (drafting, analytics, team management). So "it works from Claude" is no longer a difference. The differences left are what the loop reads, where your material lives, whether edits become rules, whether claims carry a receipt, and the price.

## Stanley (getstanley.ai, by Stan)

Launched March 2026, iMessage/Telegram/WhatsApp-first, an iOS app, and since autumn an MCP that Claude can drive (a community cookbook, `JayantChopra/stanley-mcp-playground`, documents it). Posts natively to X, LinkedIn, Threads, Instagram and Substack Notes. $44.99/month in the App Store after a 3-day trial; earlier LinkedIn plans were reported around $149/month.

What Stanley does that Open Stanley does not: native publishing on Threads, Instagram and Substack Notes; media staging from any URL, generated explainer diagrams and code-rendered carousels; SQL over your post metrics; trend clustering on X and video teardowns from a YouTube or Reels link; overnight comment replies; a mobile app; zero setup. Through its MCP it also reads GitHub commits and PRs, Granola meeting notes, Notion, Google Calendar, Slack and YouTube. If you will not install anything, or you need Instagram, use Stanley.

What Open Stanley does that Stanley does not: everything stays in a folder you own (Stanley's loop runs on Stan's servers, through one 8,000-character message channel); every draft→final edit is stored as a diff and a repeated edit becomes a rule you can read in a file; every number and name in a draft maps to a story file with its source, and a fact-checker agent recomputes experiments; an audit script scores each draft against the measured 2026 demotion signals and prints a `landing:` line; posts carry an experiment arm and the ledger reports lifts by lane, shape and hook feature; the research it runs on is in the repo with sources; it reads any MCP you have (Pam, Fathom, Granola, Gmail, Drive, memory servers), not a fixed list; it works in Cowork, Claude Code and any agent that reads SKILL.md; and it costs nothing beyond the Claude plan you have.

Open Stanley was built in a four-hour hackathon as a reply to Stanley, and credits it: the growth strategy inside Stanley is real work by its founders, and this plugin copies the loop and changes the parts that did not work for a founder with his material spread across tools.

## Taplio ($39–149/month)

The biggest LinkedIn tool: idea and hook generators from a daily feed of viral posts in your niche, "My tone" rewrites, live reach prediction before publishing, a scheduling queue with best-time slots, carousel drip, an engage feed with AI comment starters, lead lists with automatic connection requests and DMs, a Chrome extension, an academy, and MCP V2 for comments. 12K+ creators by its own count.

What Taplio does better: the scheduling calendar, reach prediction, the viral-post feed, carousels, team seats, support, and a free LinkedIn post generator and carousel maker on its site.

What Open Stanley does differently: it refuses to generate a post from a topic or a trending post. Every draft starts from a thing that happened to you with a source. The audit script flags the patterns the 2026 feeds demote. Nothing sends connection requests or DMs on your behalf, ever.

## Supergrow ($29–99/month)

AI interviews (PostCast asks you questions and drafts from the answers; Open Stanley's morning Soapbox question is the same idea with a voice note), Content DNA, repurposing, a Kanban content board, queue and first-comment scheduling, Focus Mode for engagement, team features with approval and leaderboards, an MCP, free hook/headline/carousel/post-preview tools, templates and "skills" as downloads. 4.8 on G2.

What Supergrow does better: teams, approval workflows, the Kanban board, the free tools, and support.

What Open Stanley does differently: the interview is grounded in your week (a story from a meeting, a calendar event, a Slack thread), not a generic question bank, and the answer is filed as a story with its receipt before anything is drafted.

## AuthoredUp, Kleo, PostAgent, 2PR and the rest

AuthoredUp ($20–40/month): the best LinkedIn editor and preview, formatting, snippets, analytics; no drafting from your sources. Kleo: a Chrome extension that shows a creator's best posts. PostAgent and 2PR: newer agents that, like Open Stanley, learn from your material and check claims; both are hosted and paid. STANCE and FenPost: voice-preserving drafting from your ideas, hosted.

## Roadmap items that come from this comparison

In order of how often users asked. None is promised with a date; the changelog says what shipped.

1. `code` as a mine source: commits and merged PRs become build-in-public stories (Stanley's cookbook does this; the `mine` skill now lists it, through the GitHub MCP or `git log` in a connected repo).
2. Reach-before-publish: the audit's `landing:` line plus `stanley-stats` lifts already say which shape has done well for you; a single predicted band is the missing piece.
3. Threads and Substack Notes through the browser, the way LinkedIn and X work today. Instagram needs media and a business account; not planned.
4. A free, client-side version of the audit on the website, so anyone can paste a post and see the flags without installing anything: `harmix.github.io/open-stanley/audit`.

## When not to use Open Stanley

- You post for a brand page with a team and approval workflow: Supergrow, or Oktopost's open-source Claude plugin, fits better.
- You want nothing installed and no folder on your machine, or you need Instagram or Threads today: Stanley.
- You want a scheduling calendar with reach prediction and a viral-post feed: Taplio.
