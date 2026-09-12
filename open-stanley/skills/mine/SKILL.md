---
name: mine
description: Find post material in the user's own life through every connected source — meeting transcripts and summaries (Pam, Fathom, Granola, any MCP with meeting tools), Slack/Discord messages they wrote, sent email, calendar events, docs, memory MCPs, uploads and voice notes in the vault inbox — and turn it into story files with receipts. Use when the user asks "what should I post", "anything interesting from my meetings this week", "turn this transcript/voice note/thread into a post", drops a file, or when any other open-stanley skill needs fresh material. Also runs weekly as a scheduled task.
---

# Mine: stories with receipts

The best post of the month, in the export this plugin was built from, came from a meeting transcript the user pasted into chat: a line about the person whose job was being automated refusing to help. The paid tool could only read transcripts from three vendors. You can read from anything the user has connected. Use that.

## 1. Sources, in priority order

Probe capabilities (see `skills/stanley/references/capabilities.md`). Then pull, for the window asked (default: last 7 days; onboarding: 30 days):

1. `inbox/` — anything the user dropped: voice-note transcripts, pasted transcripts, PDFs, screenshots. This is the human explicitly handing you material; read it first and fully.
2. `meetings` — list meetings in the window; read summaries first, transcripts only for meetings whose summary has a candidate. Prefer the user's own lines in the transcript. With a memory MCP like Pam, `retrieve_memory("what surprised us / went wrong / changed a decision in the last two weeks?")` is a fast first pass, but its answer is a synthesis and may come back with no source references; treat it as a lead, then open the specific meeting summary or transcript (`list_meetings` → `get_meeting_summary`) so the story file's `source:` points at a real record. A number that only exists in a memory answer is not yet a receipt.
3. `messages` — the user's own messages over ~60 words in channels they post in (search by their handle). Founders write their sharpest takes in Slack at 11pm.
4. `mail` — sent mail only, unless told otherwise. Replies over ~80 words to customers, investors, candidates.
5. `memory` — ask it the questions a good editor would ask: "what did I decide this week", "what surprised me", "what went wrong", "what number changed".
6. `calendar` — what happened (talks, conferences, customer calls) as prompts for the Soapbox question, not as posts ("heading to X" is the pattern the diagnosis flagged as the bottom performer).
7. `docs` — memos, specs, decks the user authored in the window.
8. The user's own recent posts and comments (from the ledger and `browser`) — to see which stories are already spent.

Read-only, always. If a source errors, say which one and continue.

## 2. What counts as a story

A story is a specific thing that happened, with at least one of: a number, a named decision, a mistake, a surprise, a disagreement, a quote. It is not a topic and not an opinion without an event under it. Test: could a stranger have written this without being in the room? If yes, it's not a story yet.

Sensitivity: default `anonymize` for anything involving customers, employees, money, or a third party's words; `private` for health, legal, HR, unreleased numbers the user hasn't said are public; `ok` only for the user's own actions and things already public. When unsure, mark `anonymize` and ask in one line. A meeting that is mostly private (investor call, runway, deprioritised products) is not skipped; it usually holds the sharpest lesson. Take the lesson that survives without the private facts, mark it `anonymize`, and say in the run message which meeting it came from so the human can veto.

A summary is a lead, not a receipt. Meeting summaries flatten "by design" into "spontaneous", "the customer asked" into "the customer complained", and "we discussed" into "we decided". Before a story's lesson rests on a surprising claim from a summary (an agent acted unprompted, a customer reacted badly, a rule was broken), open the transcript, or mark the story `status: needs-confirmation` and ask the human in one line. The Soapbox ritual is the cheapest way to ask.

Provenance. When the idea in a story came from an AI assistant's recommendation that the human then followed (it happens often now), record `origin: ai-suggested` in the frontmatter and say so in the body. A post built on it must either credit that or angle on what the human did with the advice; presenting it as the human's own discovery is the kind of thing readers catch. `origin` is `own` (the human's action or observation), `team` (someone on the team), `third-party` (something they read or saw), or `ai-suggested`.

## 3. Write the story files

One file per story in `stories/<slug>.md` using `stories/_TEMPLATE.md`. Frontmatter: `topic` (a lane), `lesson` (one sentence a reader would remember), `status: fresh`, `source` (the receipt: `pam:meeting/<id>`, `slack:<channel>/<ts>`, `gmail:<thread id>`, `upload:<file>`, `chat:<date>`), `date`, `sensitivity`. Body: what happened, a direct quote, the numbers with their origin, two or three angles with the lane and audience each serves. Then `skills/stanley/scripts/stanley-vault stories-index`.

Also maintain "needs material": angles the user has hinted at but that have no receipt yet, listed at the bottom of `stories/index.md` so the Soapbox ritual can ask for them.

## 4. Report

For a weekly run: the three freshest stories in one line each (lesson + source + suggested lane), what you skipped as sensitive, and which sources you couldn't reach. For an on-demand request ("turn this into a post"): write the story file, then hand off to `/open-stanley:write` with the angle the user chose or the strongest one if they didn't.

Never invent a story to fill a gap. An empty week is a real finding; say so and ask one question instead.
