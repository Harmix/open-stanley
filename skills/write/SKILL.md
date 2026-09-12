---
name: write
description: Draft or rewrite a LinkedIn post, X post, or X thread in the user's own voice from a story with a receipt, then audit it and hand it over with the one question that makes it theirs. Use whenever the user asks to write, draft, rewrite, shorten, "make this a post", "turn this into a thread", "post this to LinkedIn and X", or reacts to a draft ("too long", "sounds like AI", "change the hook"). Also used by rituals for weekly drafts and repackages.
---

# Write: edit the person's material into a post

You are not generating a post about a topic. You are editing something the person already knows into the shape a feed rewards, in their voice. That distinction is what keeps the post out of LinkedIn's generic-AI demotion and what makes a reader stop.

## 1. Inputs, and what to do if one is missing

- **A story with a receipt** (`stories/<slug>.md`). Missing → run `/open-stanley:mine` or ask for the material ("tell me what happened, two minutes, voice note is fine"). Don't draft from a topic. `status: needs-confirmation` means the lesson rests on an unverified summary line: ask the human first, don't draft. `origin: ai-suggested` means the idea came from an AI's advice the human followed: the draft credits that or is about what they did with it, never "here's what I figured out".
- **The claim, from the human.** One sentence of what they believe about the story. Missing → ask exactly one question, or, if the user said "just go", use the story's own quoted line as the claim and mark the draft `unclaimed` so the audit and the handover say it needs their sentence.
- **Voice** (`voice.md` exemplars + yaml). Missing → onboarding.
- **Platform** and whether it also goes to X (default: both, same time, X as thread if no Premium; from `strategy.md`).

## 2. Drafting

Read 10–15 exemplars from `voice.md` right before writing; match their sentence rhythm, vocabulary level, punctuation, and how they open and close. If the user asked for a shape ("PG-style", "like Dharmesh's episode posts") or the lane names a reference creator, read that creator's entry in `shapes/` (vault) or `skills/study/references/creators-2026-09.md` and borrow the *moves* only; every word still comes from the story and the voice. Then:

1. **Open on the event or the claim.** "Ran a quick experiment with my team this weekend." "Someone tried to hack my GSuite today." "One of the debates I've had for 15 years and mostly lost is…" No framing sentence, no rhetorical question, no "In today's…". The first ~140 characters are all LinkedIn shows; make them a complete thought that a founder scrolling at speed would stop on.
2. **Say what happened with the specifics only this person has.** The number, the name (if `sensitivity: ok`), the date, the thing that went wrong. Quote the source where its words are better than yours.
3. **The claim, once, plainly.** Not restated three ways. If the story has two lessons, that's two posts.
4. **End on the last real sentence,** or, if this person does it (check `voice.md`), one specific open question that a peer could actually answer. Never a summary, never "Agree?", never "What do you think?".
5. **Length**: LinkedIn 1,300–1,900 characters for a story; 400–900 for a single claim; aphorisms are fine when the exemplars show them. Paragraphs of 1–3 sentences, not one line each. Zero hashtags, no links in the body (first comment if needed).
6. **X**: the same post as a single long post if the user has Premium; otherwise a thread of 3–7 tweets separated by `---`, where tweet 1 stands alone as a post and the last tweet carries the claim, not "that's a wrap". Links go in the first reply. `references/platforms.md` has the rest.

Things that mark a draft as generated and therefore get demoted and skipped: three short sentences in a row; "not X, it's Y"; a rule-of-three list; em dashes (unless the exemplars use them); bolded-term-colon lists; "delve/leverage/robust/pivotal/…"; an editorializing tail ("…, highlighting the need for…"); "experts say"; a closing question addressed to everyone. The audit catches most of these; write so it has nothing to catch.

## 3. Audit, critic, handover

0. Tag the draft with its lane and shape (`opener:`, `body:`, `ending:` from `skills/study/references/shape-vocabulary.md`) and, if `strategy.md` has an open experiment, the variant this post takes (alternate variants post by post). `publish` records these so `stanley-stats` can tell you later what worked.
1. Save the draft to `drafts/<date>-<slug>.md` (git keeps versions; the paid product lost a hook in a rewrite once, don't).
2. `skills/stanley/scripts/stanley-audit drafts/<file> --platform linkedin --vault <vault>` (and `--platform x` for the thread). Fix every BLOCK yourself. Re-run until clean.
3. If the draft is a full post (not a comment), ask the `critic` agent (`agents/critic.md`) for its three answers and include them in the handover only if they change something.
4. Render the preview: `skills/stanley/scripts/stanley-preview drafts/<file> --platform linkedin --out drafts/<slug>.png --name … --headline …` (and `--platform x` for the thread). The fold line is what gets hooks fixed.
5. Hand over: the draft and the preview image, then at most three lines: any WARN the human should decide on, the receipts used (story slug + source), and the one question ("this says 2.0 out of 5 — that's from your Sunday message, right?"). Then stop.

## 4. Revisions

When the user edits or reacts:
- "too long" → cut the setup and the restated claim first, never the specifics.
- "sounds like AI" → find the pattern (usually staccato lines, a tricolon, a wrap-up, or a generic adjective), fix that, and add the pattern to `learn/diffs.jsonl` via `skills/stanley/scripts/stanley-vault diff-add` so `learn` can propose a rule.
- "change the hook to start with X" → keep everything else byte-identical; diff before you send.
- When they paste their own final version, that's the ground truth: store the diff, and use *their* version for publishing, formatted for X only if they asked.

Every accepted change is logged. Every third recurrence of the same change becomes a proposed rule (see `/open-stanley:learn`).
