---
layout: default
title: "How to turn meeting notes into a LinkedIn post with Claude"
description: "A free way to turn your meeting transcripts, Slack threads and voice notes into LinkedIn and X posts with Claude, keeping the source of every number and quote. Works with Granola, Fathom, Fireflies, Pam or a pasted transcript."
---

# Meeting notes to a LinkedIn post, with Claude

One of my best posts came from one line in a meeting transcript. The drafts I threw away started from a topic. That is the whole idea of this page: start from a thing that happened, keep where it was said, then write.

## <svg class="orange" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 6h16M4 12h16M4 18h16"/></svg>What you need

- Claude (Cowork or Claude Code) with your meeting tool connected: Granola, Fathom, Fireflies, Pam or any MCP that lists meetings. No connector? Paste the transcript or drop the file in a folder.
- Slack, Gmail and Calendar if you want them. They often hold the sharpest line of the week.
- The free [Open Stanley](https://github.com/Harmix/open-stanley) plugin, or the steps below by hand.

## <svg class="rose" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l2.7 5.5 6 .9-4.4 4.2 1 6-5.3-2.8-5.3 2.8 1-6L3.3 9.4l6-.9z"/></svg>The steps

1. **Read summaries first, transcripts second.** List the week's meetings, read the summaries, and open the transcript only where a summary has something: a number, a decision, a mistake, a surprise, a quote.
2. **Check the summary against the transcript.** Summaries turn "we discussed" into "we decided" and "the customer asked" into "the customer complained". Before a post rests on it, open the original line.
3. **Write a story file, not a post.** One sentence a reader would remember, what happened, the quote, the numbers and where they came from. A stranger could not have written it without being in the room.
4. **Mark what is private.** Customers, money and other people's words stay anonymous by default. A private meeting usually still has a lesson you can share without the private facts.
5. **Draft from the story, in your voice, and check it.** Run the draft through a check for AI patterns. You can paste it into [this free one](../audit.html).
6. **Answer one question before you post.** The draft gets better when you add the detail only you know.

## <svg class="green" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>With Open Stanley it is one sentence

Install the plugin and say "anything interesting from my meetings this week". The `mine` skill reads every source you have connected, writes each story to a file with its source (`pam:meeting/<id>`, `slack:<channel>/<ts>`, `gmail:<thread>`), ranks them and hands the best one to `write`. It runs every week on its own if you want. Your files stay in a folder you own.

## <svg class="sky" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12m-5-5 5 5 5-5M4 21h16"/></svg>Install

Cowork: Plugins → Add marketplace → `Harmix/open-stanley`. Claude Code: `/plugin marketplace add Harmix/open-stanley` then `/plugin install open-stanley@open-stanley`. Other agents: `npx skills add Harmix/open-stanley`. Comparing tools? See [Stanley alternatives](../compare/stanley-alternatives.html).
