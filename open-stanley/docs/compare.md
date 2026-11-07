# Open Stanley compared with the paid "AI head of content" tools

Written from the tools' own pages, their public MCP docs and third-party reviews, read on 7 November 2026; prices change, check theirs. This page is also honest about what they do better. If something here is out of date, open an issue; the comparison is a claim this repo makes in public.

## The thing that changed in autumn 2026

Every paid tool in this category now ships an MCP server: Stanley (`xapi.getstanley.ai/mcp`, one `message_stanley` tool), Taplio (MCP V2, comment drafting), Supergrow (drafting, analytics, team management). So "it works from Claude" is no longer a difference. The differences left are what the loop reads, where your material lives, whether edits become rules, whether claims carry a receipt, and the price.

## Stanley (getstanley.ai, by Stan)

Launched March 2026, iMessage/Telegram/WhatsApp-first, an iOS app, and since autumn an MCP that Claude can drive (a community cookbook, `JayantChopra/stanley-mcp-playground`, documents it). Posts natively to X, LinkedIn, Threads, Instagram and Substack Notes. $44.99/month in the App Store after a 3-day trial; earlier LinkedIn plans were reported around $149/month.

What Stanley does that Open Stanley does not: native API publishing (Open Stanley posts through your logged-in browser, which covers the same platforms but needs the browser open); media staging from any URL, generated explainer diagrams and code-rendered carousels; SQL over your post metrics (Open Stanley has medians, lifts and a reach band from its ledger, not a query language); trend clustering on X and video teardowns from a YouTube or Reels link; overnight comment replies; a mobile app; zero setup. Through its MCP it also reads GitHub commits and PRs, Granola meeting notes, Notion, Google Calendar, Slack and YouTube. If you will not install anything, or you need Instagram, use Stanley.

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

All four shipped in 0.17.0, the same day the comparison was written, because a plugin that has the browser and the ledger needed instructions, not infrastructure:

1. `code` as a mine source: commits and merged PRs become build-in-public stories, through a GitHub MCP, `gh`, or `git log` in a connected repo.
2. Reach band before publishing: `stanley-stats --predict drafts/<file>` reports the p25/median/p75 impressions and engagement of the user's own past posts that share the draft's features; `write` quotes it in every handover. It is a band from the ledger, not Taplio's single number, on purpose.
3. Any platform with a web composer through the browser: Threads, Substack Notes, Bluesky, Mastodon, Instagram captions with the user's media (`publish` §3b); the ledger takes any platform name.
4. The audit's vault-free rules on the website, with an "Open in Claude" button: `harmix.github.io/open-stanley/audit.html`.

What stays different by design: Open Stanley reads whatever the agent can reach (MCPs, the logged-in browser, local files and apps), so a source without an MCP, or one that blocks bots like LinkedIn's analytics pages, is still readable; the paid tools read a fixed list through their own servers.

## When not to use Open Stanley

- You post for a brand page with a team and approval workflow: Supergrow, or Oktopost's open-source Claude plugin, fits better.
- You want nothing installed and no folder on your machine, or you want Instagram and Threads posted by an API while your laptop is closed: Stanley.
- You want a scheduling calendar, a single predicted reach number and a viral-post feed: Taplio.
