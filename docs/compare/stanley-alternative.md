---
layout: default
title: "Open Stanley vs Stanley AI: a free, open-source alternative"
description: "Stanley (getstanley.ai) costs $44.99 to $149 a month and runs on Stan's servers. Open Stanley is the same loop as a free Claude plugin, with your material in a folder you own. When to pick each, with the November 2026 facts."
---

# Open Stanley vs Stanley AI

I paid for Stanley. I built Open Stanley because of what it could not do for me. This page says what each one does, from Stanley's own pages, its MCP docs and third-party reviews read on 7 November 2026, so you can pick the right one. Prices change; check theirs.

## The short version

| | Stanley (getstanley.ai) | Open Stanley |
|---|---|---|
| Price | $44.99/month (iOS, 3-day trial); LinkedIn plans reported at $149/month | $0 on top of the Claude plan you have |
| Where it runs | Stan's servers; iMessage, Telegram, WhatsApp, iOS app, MCP | Your computer, as a Claude plugin (Cowork, Claude Code, any SKILL.md agent) |
| Where your material lives | Their servers | A folder you own, plain markdown and jsonl |
| Platforms | X, LinkedIn, Threads, Instagram, Substack Notes, native publishing | LinkedIn and X, through your own logged-in browser |
| What it reads | Your posts, voice notes; through its MCP: GitHub, Granola, Notion, Calendar, Slack, YouTube | Any MCP you have connected: meetings (Pam, Fathom, Granola), Slack, Gmail, Calendar, Drive, Notion, memory, code, plus voice notes |
| Receipts | No | Every number and name maps to a story file with its source; a fact-checker agent recomputes |
| Learns from edits | "Learns your voice" | Stores every draft→final diff; the same edit twice becomes a rule you can read |
| Audit for AI tells | Per-platform quality checks | A linter for the measured 2026 demotion signals, plus a landing scorecard; [try it in the browser](../audit.html) |
| Experiments | No | Each post carries an arm; the ledger reports lifts by lane, shape and hook |
| Analytics | SQL over your metrics, follower counts, streaks | Nightly recap through your browser, medians and lifts from your own ledger |
| Media | URL staging, generated diagrams, code-rendered carousels | Preview cards, charts from your numbers, PDF carousels, real screenshots; no image model by default |
| Setup | Text a number | Install the plugin, say "set up Stanley", pick a folder |

## Choose Stanley if

- You want nothing installed and no folder on your machine.
- You need Instagram, Threads or Substack Notes today.
- You want a mobile app and overnight comment replies.
- You want media generated for you (diagrams, carousels from code).

## Choose Open Stanley if

- Your stories live in meetings, Slack, email and docs, and you want every post to start from one of them, with the source attached.
- You want your corrections to become rules you can read, not a model's memory you cannot inspect.
- You want to know which lane, shape and hook actually moved your numbers, from your own ledger.
- You do not want your material on anyone's server, and you do not want another subscription.

## What the two have in common

Both copy the job of a head of content: ideas before you ask, drafts in your voice, scheduling, numbers back. Stanley's founders did the strategy work first; Open Stanley says so in its README and changed the parts that did not work for a founder whose material is spread across tools.

## The numbers behind this page

The first account on Open Stanley, under 5K followers, went from a median of about 1,150 impressions a post to 108,048 impressions in 90 days on 7 November 2026, with one post at 85,934. The screenshot and what the plugin learned from it are on the [home page](../#results).

## Install

Cowork: Plugins → Add marketplace → `Harmix/open-stanley`. Claude Code: `/plugin marketplace add Harmix/open-stanley` then `/plugin install open-stanley@open-stanley`. Other agents: `npx skills add Harmix/open-stanley`. Source and docs: [github.com/Harmix/open-stanley](https://github.com/Harmix/open-stanley).
