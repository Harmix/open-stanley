# Platform access: official API/MCP before the browser

The browser is the fallback, not the default. Before automating anything on a platform, ask which of two things you are doing, because the answer is different for each:

- **Write** — post, comment, like, reply *as the user, on the user's own behalf*.
- **Read** — the feed, search, other people's posts, analytics.

Then check, in this order: (1) an MCP the user already has connected that covers it (`post` capability in `capabilities.md`); (2) an official first-party API or hosted MCP the user could connect in ten minutes; (3) the browser. Record the answer per platform in `my-human.md` as `post_path: <platform>=<mcp|api|browser>` so later runs do not re-derive it.

## Why writing through the browser is the risky half

Reading through a logged-in browser looks like a person scrolling. Posting through one is the part that looks like automation to a platform's own detectors: the typing is machine-fast, the timing is exact, and it arrives from a session that never idles. Both platforms below publish rules against third-party automation of the account, and both offer an official write path to your *own* profile that is free or nearly free. So when a write has an official path, use it.

Data point, not a proven cause: this plugin posted a four-tweet X thread through the browser on 12 September 2026; the account was suspended the following day. It may have been unrelated. It is still the reason the order above is what it is.

## LinkedIn (September 2026)

| | Path | Notes |
|---|---|---|
| Write | **Official, self-serve.** A LinkedIn developer app with the `w_member_social` scope posts, comments and likes on the authenticated member's own behalf. No partner approval, no fee. | The only open scopes are OpenID Connect sign-in and `w_member_social`. Setting it up is a one-time thing the user does; offer it once at onboarding and record the answer. |
| Read | **Browser.** | Feed reading, member/content search, and analytics on anyone (including the user's own creator analytics) all sit behind the Marketing/partner products, which need an application and approval. There is no self-serve read surface, so scout, recap and onboarding read through Claude in Chrome. This has worked without friction. |

## X (September 2026)

| | Path | Notes |
|---|---|---|
| Write | **Official hosted MCP**, `https://api.x.com/mcp` (first-party, shipped 30 June 2026). Posts, replies, bookmarks, and draft+publish Articles. Writes need OAuth 2.0. | The MCP layer is free; calls bill against the user's X API plan. The free tier covers roughly 500 posts/month of writes, which is far more than this plugin will ever use. Prefer it over the browser for every X write. |
| Read | **Browser**, unless the user pays. | The free X API tier includes no reads, so full-archive search, timelines and analytics through the MCP require Basic (~$200/mo) or pay-per-use credits. Not worth it for one person's content loop: read X in the browser, write through the MCP. |

X's MCP also exposes trends and news, which the scout can use for "what is happening today" *if* the user is on a paid tier. Check the tier before promising it.

## Any other platform

Same procedure, no guessing: search the user's connected MCPs for the platform by name, then look for a first-party API or hosted MCP, then fall back to the browser. Say in one line which path you used and why. Never scrape a platform that offers a self-serve write API for the thing you are about to do.

## When the browser is the only path

- Human pacing: one action at a time, a real pause between them, never a burst of posts or comments.
- Never post the same text to two accounts, and never run the same action on a loop.
- Keep to the `scout` skill's cap (25 posts opened per run) and the strategy's comment budget.
- One session, the user's own logged-in profile. No second account, no credential sharing.
- If a platform shows a captcha, a rate-limit notice, or a "confirm you are human" interstitial, stop, report it, and do not retry. That is the platform saying no.
