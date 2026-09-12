---
name: learn
description: Turn the user's edits, skips, and results into durable rules — update voice.md and learn/rules.md from draft→final diffs, retune scout scoring from skip reasons, and (only if the user opts in) prepare an anonymized, text-free contribution of rule statistics for the shared Open Stanley skill. Use when the user says "learn from my edits", "here's what I actually posted", "stop doing X", "remember that I never say Y", "why do you keep doing this", or "contribute my improvements".
---

# Learn

The paid product said "calibrating to this exact standard" and then did the same thing the next day. Learning here means a file changed.

## 1. From a diff

When the user pastes what they actually posted, or edits a draft, store the pair: `skills/stanley/scripts/stanley-vault diff-add --draft-file <d> --final-file <f> --platform <p> --kind post|comment`. Then read the diff and name the edit in one of these categories (or a new one if none fits):

- cut setup sentence / cut wrap-up / cut restated claim
- shortened (by what fraction) / lengthened
- replaced a word (draft word → final word)
- changed opener to start on the event / on the claim
- removed a number or name (sensitivity) / added a number or name (specificity)
- changed the ending to an open question / to a flat last line
- de-jargoned a term (record the pair)
- softened a claim about someone else / hardened a claim about themselves

Write the category and evidence into the diff record. When a category has recurred three times, propose exactly one line for `voice.md` ("Never opens with a setup sentence" / add `innate` to `banned_extra`) or `learn/rules.md`, quote the three examples, and ask for a yes. On yes, write it. On no, record the no so you don't propose it again.

## 2. From skips

Every scout skip reason (`ledger/comments.jsonl` with `skipped: true`) is a filter adjustment. Cluster the reasons monthly ("too abstract" ×6, "not my lane" ×4, "hallucination is common knowledge" ×1) and add the top cluster as a line to `instructions.md` with the date. Tell the user in one line what changed in the scoring.

## 3. From results

When `recap` writes metrics, run `skills/stanley/scripts/stanley-stats`. A lift that holds across an experiment's `min_n` (and preferably 8+ posts per arm) becomes a "Resolved bets" line in `strategy.md` with the numbers and the date, and a default in `voice.md` or `strategy.md` (e.g. "end on an open question: +40% comments over 9 posts, Sep–Oct 2026"). One line, not a report. Anything below that sample size stays a hint.

## 4. Community contribution (opt-in, text-free)

Off by default. Ask once, at onboarding or when the user mentions it, in plain words: "Open Stanley can send anonymized counts of which audit rules fire and which edits you make (never any text) to help improve the shared rules. Turn on?" Store the answer in `my-human.md` as `contribute: yes|no`. Never ask again unless they bring it up.

When `contribute: yes`, once a month prepare `learn/contribution-<yyyy-mm>.json` following `references/contribution-schema.md`: rule ids with fire counts and revert counts, edit categories with counts, skip-reason clusters with counts, platform and post counts as ranges, no handles, no text, no server names, no dates finer than the month. Show the file to the user, then submit as a GitHub issue on the plugin repo labelled `contribution` via `gh issue create` (or tell them where to paste it if `gh` isn't available). Maintainers aggregate with a k-anonymity floor, turn recurring signals into rule PRs, and gate merges on the eval suite in `tests/evals/`.

What never leaves the machine: drafts, finals, comments, story files, meeting content, names, handles, URLs, the vault. If in doubt, leave it out; the schema has no field for it anyway.
