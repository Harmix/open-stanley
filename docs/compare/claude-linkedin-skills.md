---
layout: default
title: "Claude skills for LinkedIn posts: the open-source options compared"
description: "Open-source Claude skills and plugins for writing LinkedIn and X posts: sergebulaev/linkedin-skills, liftli-ai/linkedin-agent-skills, the Stanley MCP cookbook, Social Daily Poster, Oktopost's plugin and Open Stanley. What each one does and when to use it."
---

# Claude skills for LinkedIn posts

If you search for a Claude skill that writes LinkedIn posts, you find hundreds of single SKILL.md files with a prompt inside. A few projects go further. These are the open-source ones I would look at, read in November 2026. I built the last one.

## <svg class="orange" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 6h16M4 12h16M4 18h16"/></svg>The list

| Project | What it is | Use it when |
|---|---|---|
| [sergebulaev/linkedin-skills](https://github.com/sergebulaev/linkedin-skills) | Claude Code and Codex skills for LinkedIn posts, comments and replies, with a post audit | You want good writing rules and call each skill by hand |
| [liftli-ai/linkedin-agent-skills](https://github.com/liftli-ai/linkedin-agent-skills) | Skills for Claude Code, Codex, Cursor and Gemini CLI: hooks, comments, a profile audit and a pre-post check | You switch between agents and want the same skills in each |
| [JayantChopra/stanley-mcp-playground](https://github.com/JayantChopra/stanley-mcp-playground) | Recipes for driving the paid Stanley from Claude over its MCP | You already pay for Stanley and want Claude to run it |
| [dimamak/sdp](https://github.com/dimamak/sdp) | Social Daily Poster: a Python app that drafts one post a night from your Claude Code or Codex sessions, screenshots and messages, asks for approval in Telegram and posts through the official LinkedIn and X APIs | You want one post a day from your coding work, with a tap to approve |
| Oktopost's Claude plugin | Open source, built for brand pages and employee advocacy | You post for a company with a team and approvals |
| [Open Stanley](https://github.com/Harmix/open-stanley) | A full plugin: 18 skills and 3 agents that find stories in your meetings, chats and mail, draft for LinkedIn, X, Threads and other platforms, plan short videos, audit, schedule, measure, fix your profile and learn from your edits | You want the whole loop running on a schedule, not single skills |

## <svg class="rose" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l2.7 5.5 6 .9-4.4 4.2 1 6-5.3-2.8-5.3 2.8 1-6L3.3 9.4l6-.9z"/></svg>Skills or a loop

A skill writes a post when you ask. That is enough if you already know what to post about. Most people do not, and that is where a writing skill alone starts to make the generic posts the feed now hides. A loop does the part before the writing: it reads what happened in your week, saves each story with its source, asks you one question in the morning, and after the post goes out it records what the post did. Open Stanley is a loop. The skill repos above are good at the writing part, and you can use them together.

## <svg class="green" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>Check a post without installing anything

The audit Open Stanley runs on every draft is also a [web page](../audit.html). Paste a post and it shows the AI vocabulary, the "not X but Y" lines, bait closers, hashtags and the other patterns LinkedIn demotes. It runs in your browser and sends nothing anywhere.

## <svg class="sky" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12m-5-5 5 5 5-5M4 21h16"/></svg>Install Open Stanley

Cowork: Plugins → Add marketplace → `Harmix/open-stanley`. Claude Code: `/plugin marketplace add Harmix/open-stanley` then `/plugin install open-stanley@open-stanley`. Other agents: `npx skills add Harmix/open-stanley`. More comparisons: [Stanley alternatives](stanley-alternatives.html).
