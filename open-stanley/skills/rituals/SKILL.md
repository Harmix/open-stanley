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

## Tune (weekly, ~Friday 17:00)

The improvement loop. Everything else in this plugin produces content; this is the only ritual whose output is a change to how the plugin works, and it runs weekly because the signals it reads accumulate weekly — where the monthly numbers do not.

Load `/open-stanley:learn` and work only from what happened this week:

- **Draft→final diffs** (`learn/diffs/`): what the user cut, added, or reworded in the 2–3 drafts they actually posted, plus any comment or reply they rewrote before sending. This is the densest signal the plugin gets, it arrives every week, and one clear pattern beats a month of engagement noise.
- **Skips**: scout picks shown and not used, drafts left unposted. Ask why in one line if the reason is not obvious from the ledger; a skip with a reason retunes scoring, a skip without one is noise.
- **Rules that fired**: which `stanley-audit` rules tripped repeatedly, and whether the user overrode any of them. A rule the user overrides twice is a rule that is wrong for them.

Then the **active experiment**, which lives under `## Experiments` in `strategy.md`. At most one runs at a time; `write` assigns the arm for each new post and tags it (`--experiment name=variant`). Report `stanley-stats --experiments` arm counts plainly and *do not* call a winner until both arms have at least four posts, however tempting the gap looks. Observation alone cannot separate a shape from its topic, its timing, and its luck — the experiment is the only thing here that produces a real answer, so protect it from being read early.

Update `voice.md` and `learn/rules.md` with anything that recurred at least twice. Propose at most two changes and apply none without a yes. A week with nothing to learn from gets one honest line, not an invented rule.

## Repackage (every two weeks)

From `ledger/posts.jsonl`, find the top 3 posts by engagement relative to the median. For each, name the *shape* that worked (a hand-over-the-system how-to; a claim about the future; a story with a number) and find a fresh story that fits the same shape. Draft one, labelled as a repackage so the audit's self-overlap check is expected. Don't re-post the same lesson; re-use the shape.

## Orbit (monthly)

From `ledger/posts.jsonl`, `ledger/comments.jsonl`, and the recap pulls: the 5–8 people who engaged most often, with role, what they engaged with, and any open thread with them. Suggest at most two actions (reply to an open thread; comment on something they posted this week that fits a lane). This is relationship data; never DM on the user's behalf.

## Strategy check-in (monthly)

Show `strategy.md` goal and lanes against the month's numbers: posts per lane, median per lane, best and worst with the one reason. Propose at most one change (a lane to drop, a cadence to shift, a bet resolved). Ask the user to confirm or edit; then rewrite `strategy.md` with the date. A lift computed on fewer than 3 posts is not evidence; `stanley-stats` marks those rows.

Three things the monthly owns that the weekly Tune deliberately does not:

- **Close or rotate the experiment.** If both arms have 4+ posts, declare the verdict, write it into `## Resolved bets` with the numbers and the date, and propose the next experiment. If an experiment has been open for two months without filling its arms, it is the wrong experiment — kill it and pick one that every post can be tagged with.
- **Bring in something from outside.** Self-observation recombines what the user already does; it cannot add a move they have never made. Once a month run `/open-stanley:study` on one person who is winning in one of their lanes (not the same person twice running) and add the shapes to the catalog. Propose one to try next month.
- **Flagship check.** Has a `longform` piece run in the last quarter? If not, say which story cluster is closest to meeting one of the three entry conditions in the `longform` skill.

## Trend alert (on event)

Only when a `research` or `browser` source shows something under N hours old (from `voice.md` `freshness_days`) in a lane, with a primary source you opened. Deliver: the source link with its date, one line on why it's a fit, a drafted angle (not a post) that ends with "want the draft?". Never post. The user's rule: if he already saw it a week ago, it's not news.

## Delivery in remote runs

Each ritual is a scheduled-task template in `templates/scheduled-tasks/`. In a remote run, deliver through the `notify` capability the user chose at onboarding (Slack DM, Telegram bot, email draft to self) and end the message with what was checked, so a "nothing today" is visibly a result and not a missed run.
