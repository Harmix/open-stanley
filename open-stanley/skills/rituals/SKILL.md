---
name: rituals
description: The proactive habits of a head of content — the morning Soapbox question that pulls a voice note out of the user, Sunday weekly drafts, bi-weekly repackaging of the user's best old post shapes, the monthly Orbit (who kept showing up) and strategy check-in, and trend alerts. Use when the user asks for a morning prompt, "plan my week", "what old posts could I redo", "who's in my orbit", "review my strategy", or when a scheduled task names one of these rituals.
---

# Rituals

These are the parts of the paid product the user opted into and kept. Each is a small, predictable message with one ask. The difference here: every ritual is grounded in a receipt and records what it delivered.

## Soapbox (daily, ~08:00)

Purpose: extract two minutes of the person's own words before anything is drafted. Pick one fresh story from `stories/index.md` (or a "needs material" angle, or yesterday's calendar event from `calendar`) and ask one question that only this person can answer and that a post could be built on. Format, exactly three parts:

1. one line of context that proves you read something real ("been thinking about the note-taker overlap experiment from Sunday");
2. the question, one sentence, specific ("what would you have wanted the note-taker to do differently for the R&D meeting?");
3. "voice-note it for two minutes or type three lines, here."

The answer comes back in this conversation (in a scheduled run, as a reply in the run's session). Filing it is your job, never theirs: write the reply verbatim to `inbox/soapbox-<date>.md` with the question above it, update or create the story it belongs to (the human's account overrides whatever the summary said; see `mine`, "a summary is a lead"), and push. Never ask the user to put anything in the vault themselves.

Never ask a question the user already answered in a post or in `stories/`. If they reply "I cannot answer", drop the angle and don't re-ask for two weeks. If the user's reply corrects your reading of the source ("it was triggered by design, not spontaneous"), the correction is the story; record it and add the misreading to `learn/rules.md` as a candidate.

Do not skip a meeting because most of it is inside the private line (investor call, runway, deprioritised products). Those meetings hold the sharpest lessons; find the one that can be told without the private facts, mark the story `sensitivity: anonymize`, and let the human decide. Only the private facts stay out, not the meeting.

## Weekly drafts (Sunday, ~10:00)

Three drafts, each from a different fresh story and a different lane, each run through `write` (so audited, with receipts and the one question attached). Deliver as three hooks with one line each and the drafts below; ask which to schedule and when. Nothing is scheduled without a yes. Record the three as `drafts/` files; anything not chosen in 14 days is archived, and the user is told once ("archived two stale drafts; reversible in drafts/archive/").

## Tune (inside the Sunday run, before drafting)

Corrections already land the moment they happen: when the user rewrites a draft, a comment or a reply, the running skill files the diff to `learn/diffs.jsonl` and any standing instruction to `instructions.md`, and the next draft reads both. That loop works and does not need a scheduled meeting.

What nothing does is the step the vault's own design calls for: `learn/rules.md` says "candidates live in diffs.jsonl until confirmed", and nothing ever promotes them. So once a week, at the top of the weekly-drafts run and before writing anything:

- **Promote** any correction that has now appeared twice from a candidate diff to a confirmed line in `learn/rules.md`. Twice is the bar; once is a one-off and stays a diff.
- **Retire** a confirmed rule the user has overridden twice since it was written. A rule that keeps getting overridden is wrong, and leaving it in makes every future draft worse.
- **Check the arms** of the experiments in `strategy.md` with `stanley-stats --experiments`. Report counts, call no winner before both arms hold `min_n`, and if one arm is starving say so with a number ("open-question endings: 1 of 4; three of this week's drafts should end on a question"). Then write those drafts so the thin arm fills — that is the one place the plugin should let the experiment steer what it writes.

Two changes at most, and none applied without a yes.

## Repackage (every two weeks)

From `ledger/posts.jsonl`, find the top 3 posts by engagement relative to the median. For each, name the *shape* that worked (a hand-over-the-system how-to; a claim about the future; a story with a number) and find a fresh story that fits the same shape. Draft one, labelled as a repackage so the audit's self-overlap check is expected. Don't re-post the same lesson; re-use the shape.

## Orbit (monthly)

From `ledger/posts.jsonl`, `ledger/comments.jsonl`, and the recap pulls: the 5–8 people who engaged most often, with role, what they engaged with, and any open thread with them. Suggest at most two actions (reply to an open thread; comment on something they posted this week that fits a lane). This is relationship data; never DM on the user's behalf.

## Strategy check-in (monthly)

Show `strategy.md` goal and lanes against the month's numbers: posts per lane, median per lane, best and worst with the one reason. Propose at most one change (a lane to drop, a cadence to shift, a bet resolved). Ask the user to confirm or edit; then rewrite `strategy.md` with the date. A lift computed on fewer than 3 posts is not evidence; `stanley-stats` marks those rows.

Three things the monthly owns that the weekly Tune deliberately does not:

- **Close or rotate the experiment.** If both arms have 4+ posts, declare the verdict, write it into `## Resolved bets` with the numbers and the date, and propose the next experiment. If an experiment has been open for two months without filling its arms, it is the wrong experiment — kill it and pick one that every post can be tagged with.
- **Bring in something from outside.** Self-observation recombines what the user already does; it cannot add a move they have never made. Once a month run `/open-stanley:study` on one person who is winning in one of their lanes (not the same person twice running) and add the shapes to the catalog. Propose one to try next month.
- **Find a format gap.** From the creators studied this month, name a format or shape that works in the user's lane and that the user has never tried — a carousel, a short video, a teardown, a build-in-public series, whatever the evidence actually shows. Propose exactly one, as the next experiment with its arms and `min_n`, not as a thing to go do. The plugin should arrive at new formats by watching what works and testing it, never by adopting whatever someone mentioned in passing.

## Trend alert (on event)

Only when a `research` or `browser` source shows something under N hours old (from `voice.md` `freshness_days`) in a lane, with a primary source you opened. Deliver: the source link with its date, one line on why it's a fit, a drafted angle (not a post) that ends with "want the draft?". Never post. The user's rule: if he already saw it a week ago, it's not news.

## Delivery in remote runs

Each ritual is a scheduled-task template in `templates/scheduled-tasks/`. In a remote run, deliver through the `notify` capability the user chose at onboarding (Slack DM, Telegram bot, email draft to self) and end the message with what was checked, so a "nothing today" is visibly a result and not a missed run.
