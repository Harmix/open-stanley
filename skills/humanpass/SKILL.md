---
name: humanpass
description: Get a post written or fully rewritten by a human — the user themselves (default), a retained editor, or a paid writer hired through an API (Prolific, Microworkers, Textbroker, human-mcp.io, Upwork MCP) — from a structured brief rather than from model prose, so the final text is human-authored and carries no model watermark. Use when the user asks for a human rewrite, "hire someone to rewrite this", a second pair of eyes, "make sure this passes AI detection", or when strategy.md marks a lane as human-written.
---

# Human pass

Since 2 August 2026 every word Claude generates carries a SynthID-Text watermark, in Claude, Claude Code, Cowork, and the API, with no opt-out. Anthropic's own wording: "light editing probably won't remove the watermark completely; a complete rewrite where every word is replaced will," and when Claude proofreads a person's text "there's very little for the watermark to attach to." Independent work says the same about classifiers: lightly edited model prose still gets flagged 40–80% of the time by GPTZero/Pangram, while the other direction (a person writes, a model tidies) is close to undetectable and, more importantly, is honestly human.

So the human pass is not "a human polishes Claude's draft." That costs money and defeats nothing. It is: **Claude produces a brief, a human writes, Claude verifies.** The writer never sees model prose.

## 1. Who writes

| Tier | Who | Cost | Latency | When |
|---|---|---|---|---|
| 0 (default) | **The user**, from a voice note or three typed lines, with Claude only structuring | free | minutes | Every post, if they'll do it. Their words, their watermark-free text, their best voice |
| 1 | **A retained editor** reached through the user's `notify` channel (Slack/Telegram/email), briefed once with the style guide | $50–500/post, or a monthly retainer | hours | Users who already have one |
| 2 | **Prolific (AI Task Builder)** via REST/CLI: native-English filter, style guide as `rich_text` blocks, ~8-minute task | ~$1.50–2.20 per 250 words all-in ($8/hr floor + ~40% fee) | minutes–hours | The default paid lane: scriptable end to end, vetted pool |
| 3 | **Microworkers API 2.0**: set your own price, country-filter to US/UK/CA, pay only on "satisfied" | $0.30–1.00 per task (+7.5–10% fee, $10 deposit) | minutes–hours | The cents lane; expect variance, use for volume or A/B against tier 2 |
| 4 | **Textbroker TeamOrder** (SOAP API): a standing hand-picked writer group that learns the voice | ~$6–9 per 250 words at 3–4★ | hours–days | Posts that matter, once you've found writers who nail it |
| 5 | **human-mcp.io** (19 MCP tools, escrow, `post_task`/`request_revision`/`approve_and_pay`, $1 min) or **Upwork MCP** (official, OAuth; a human must confirm hires and pay on upwork.com) | $1.15+ / freelancer rate | unverified / hours–days | Agent-native experiments; liquidity unproven, say so to the user |

Not usable: Amazon MTurk (closes 30 Sep 2026), Fiverr (no ordering API), RentAHuman (physical tasks only), Rev (transcription only), "Hire Human" (hirehuman.ai is a job-training program, not a marketplace). Full research with prices and links: the parent repo's `research/human-rewrite-and-mcps.md`.

## 2. The brief, never the draft

`skills/stanley/scripts/stanley-brief make stories/<slug>.md --claim "<the user's one sentence>" --vault <vault> --platform linkedin --length 180 > drafts/<slug>.brief.json`

The brief carries: the claim, the material (quoted story text with its source), the facts to keep exactly, required and forbidden terms, length band, ending style, and a short negative style guide from `voice.md` (what this person never does), plus 3–5 of the user's own posts as exemplars when the writer is human (add them by hand from `voice.md`; keep the guide under one screen, long guides get skimmed at these prices). Sensitivity: if the story is `anonymize`, strip names and exact figures before the brief leaves the machine; if `private`, no external writer at all.

If a Claude draft already exists, do not send it. Keep it only to run the overlap check in verification.

## 3. Placing the task

- Tier 0: the Soapbox question, or "give me three lines on this and I'll shape them"; then Claude edits *their* text lightly (proofread mode), which is the watermark-free regime.
- Tier 1: send the brief through `notify`; wait for the reply in the same channel; no chasing more than once a day.
- Tier 2/3: create the task from the brief through the platform API (the platform is configured by the user in `my-human.md` under `humanpass:` with tier, API key location, budget per post, and country filter). Poll for completion; never auto-approve on receipt.
- Never use tier 2–5 for a `private` story, and never include the user's handles or company name unless `sensitivity: ok`.

## 4. Verify before it goes anywhere

`skills/stanley/scripts/stanley-brief verify drafts/<slug>.brief.json <returned.txt> --draft drafts/<slug>.md`

- FAIL on: forbidden terms, hashtags, length outside band, wrong ending style, or **3-gram overlap above 25% with a model draft** (that means the writer edited instead of writing; request a revision, don't pay for it).
- CHECK on: a fact not found verbatim (ask the writer or the user; a dropped number may be deliberate).
- Then the normal path: `stanley-audit`, preview, the user's own final read. If the user edits the human text, store the diff; it's still voice data.
- Optional detector scores (`audit`), reported as information. Never reject a human writer on a detector score alone; false positives on genuine human writing run 9–15% in 2026 studies.

## 5. Pay and record

Approve on the platform only after verification passes; rate honestly (ratings are the platform's quality control). Record the cost and tier in the ledger entry (`post-add --lane … --shape …` plus `humanpass: {tier, cost}` if the user wants spend tracked) so `stanley-stats` can compare human-written vs. self-written posts on the same metric. That comparison is the only way to know whether the paid lane is worth it for this audience.
