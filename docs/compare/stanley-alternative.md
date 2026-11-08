---
layout: default
title: "Open Stanley vs Stanley AI: a free, open-source alternative"
description: "Stanley (getstanley.ai) costs $44.99 to $149 a month and runs on Stan's servers. Open Stanley is the same loop as a free Claude plugin, with your material in a folder you own. When to pick each, with the November 2026 facts."
---

# Open Stanley vs Stanley AI

I paid for Stanley. I built Open Stanley because of what it could not do for me. Below is what each one does. I took Stanley's side from its own pages, its MCP docs and reviews by other people, read on 7 November 2026. Prices change, so check theirs.

## <svg class="orange" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 6h16M4 12h16M4 18h16"/></svg>The short version

| | Stanley (getstanley.ai) | Open Stanley |
|---|---|---|
| Price | $44.99/month (iOS, 3-day trial); LinkedIn plans reported at $149/month | $0 on top of the Claude plan you have |
| Where it runs | Stan's servers; iMessage, Telegram, WhatsApp, iOS app, MCP | Your computer, as a Claude plugin (Cowork, Claude Code, any SKILL.md agent) |
| Where your material lives | Their servers | A folder you own, plain markdown and jsonl |
| Platforms | X, LinkedIn, Threads, Instagram, Substack Notes, native publishing | LinkedIn and X first; Threads, Substack Notes, Bluesky, Mastodon and Instagram captions through your own logged-in browser |
| What it reads | Your posts, voice notes; through its MCP: GitHub, Granola, Notion, Calendar, Slack, YouTube | Anything the agent can reach: every MCP you have (meetings, Slack, Gmail, Calendar, Drive, Notion, memory, code), your logged-in browser (LinkedIn analytics, pages that block bots), local files and apps, voice notes |
| Receipts | No | Every number and name maps to a story file with its source; a fact-checker agent recomputes |
| Learns from edits | "Learns your voice" | Stores every draft→final diff; the same edit twice becomes a rule you can read |
| Audit for AI tells | Per-platform quality checks | A linter for the measured 2026 demotion signals, plus a landing scorecard; [try it in the browser](../audit.html) |
| Experiments | No | Each post carries an arm; the ledger reports lifts by lane, shape and hook |
| Analytics | SQL over your metrics, follower counts, streaks | Nightly recap through your browser, medians and lifts from your own ledger |
| Media | URL staging, generated diagrams, code-rendered carousels | Preview cards, charts from your numbers, PDF carousels, real screenshots; no image model by default |
| Setup | Text a number | Install the plugin, say "set up Stanley", pick a folder |

## <svg class="rose" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l2.7 5.5 6 .9-4.4 4.2 1 6-5.3-2.8-5.3 2.8 1-6L3.3 9.4l6-.9z"/></svg>Choose Stanley if

- You want nothing installed and no folder on your machine.
- You want Instagram, Threads or Notes posted by an API while your laptop is closed.
- You want a mobile app and overnight comment replies.
- You want media generated for you (diagrams, carousels from code).

## <svg class="green" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>Choose Open Stanley if

- Your stories live in meetings, Slack, email and docs, and you want every post to start from one of them, with the source attached.
- You want your corrections saved as rules in a file you can open and edit.
- You want to know which lane, shape and hook actually moved your numbers, from your own ledger.
- You do not want your material on anyone's server, and you do not want another subscription.

## <svg class="violet" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zM2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/></svg>What the two have in common

Both do the job of a head of content. They bring you ideas before you ask, draft in your voice, schedule the post and report the numbers. Stanley's founders did the strategy work first; Open Stanley says so in its README and changed the parts that did not work for a founder whose material is spread across tools.

## <svg class="yellow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 20h18M5 16l4-5 4 3 6-8"/></svg>The numbers behind this page

The first account on Open Stanley, under 5K followers, went from a median of about 1,150 impressions a post to 108,048 impressions in 90 days on 7 November 2026, with one post at 85,934. The screenshot and what the plugin learned from it are on the [home page](../#results).

## <svg class="sky" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12m-5-5 5 5 5-5M4 21h16"/></svg>Install

Cowork: Plugins → Add marketplace → `Harmix/open-stanley`. Claude Code: `/plugin marketplace add Harmix/open-stanley` then `/plugin install open-stanley@open-stanley`. Other agents: `npx skills add Harmix/open-stanley`. Source and docs: [github.com/Harmix/open-stanley](https://github.com/Harmix/open-stanley).
