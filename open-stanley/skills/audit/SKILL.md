---
name: audit
description: Check a LinkedIn/X post or comment for the things that get it demoted, flagged as AI, or skipped by readers — AI-flagged vocabulary and structures, platform rules (hashtags, links, length, hook), unsupported claims without receipts, and overlap with the user's past posts — using the bundled stanley-audit linter. Use whenever the user asks "does this sound like AI", "check this post", "review before I publish", "why isn't this getting reach", or pastes a draft they wrote elsewhere; the write and scout skills run it automatically.
---

# Audit

Run the linter, then read the result like an editor, not a checklist.

```
skills/stanley/scripts/stanley-audit <file-or-`-` for stdin> --platform linkedin|x|comment --vault <vault> [--json]
```

Exit 0 = clean. BLOCK findings are things a 2026 feed or a founder reader would punish; fix them before the human sees the draft. WARN needs a judgment call; INFO is for the human pass. `references/rules.md` explains every rule and the evidence behind it, so you can tell the user *why* rather than "the linter said".

## What the linter cannot catch (do these yourself)

1. **Is the claim actually the person's?** A draft can pass every rule and still assert something they never said ("As CEO, I was tracking commercial commitments" was written by a tool, not the founder, and he cut it). Check the draft's claims against the story file and the user's own words. If a sentence has no source in either, mark it `[unclaimed]` in the handover.
2. **Is it fresh?** For anything presented as news, open the source and check the date against `freshness_days` in `voice.md`. Papers from 2024–25 are not news in 2026.
3. **Is it new for this author?** The linter checks 3-gram overlap with the ledger; you check ideas. If the lesson is one the ledger already carries, either make it a deliberate repackage (say so) or drop it.
4. **Would the target reader stop?** Ask the `critic` agent for posts; for comments, ask yourself whether the comment adds an observation or just agrees.
5. **Watermark reality.** Model-generated words carry Anthropic's SynthID-Text watermark (since 2 Aug 2026); the detector is available to regulators, media, fact-checkers, researchers and compliance-obligated enterprises, and LinkedIn-scale platforms may follow. Short posts carry weak signal, light edits don't remove it, a full human rewrite does. Report how much of the draft is model-written vs. the user's own words (compare with the story quotes and the claim) so the user can decide whether to route through `/open-stanley:humanpass`.
6. **Detector spread (optional).** If the user has API keys for GPTZero / Originality / Pangram in their environment, run them and report the scores as information. Do not "humanize" to game them; rewrite from the material instead.

## Reporting to the user

Lead with the verdict in one line ("clean", or "two blocks fixed: a tricolon and a 'not X but Y'; one warning for you: the 2.08 number has no receipt"). Show the fixed draft. Do not list every rule that passed.

## Extending the rules

Global rules live in `skills/stanley/scripts/stanley-audit` and are the community's; personal rules live in `voice.md` (yaml: `banned_extra`, `allowed`, `em_dash`, `closing_question`) and `learn/rules.md`. When the user says "I actually use that word", add it to `allowed` rather than arguing.
