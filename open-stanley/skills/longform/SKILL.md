---
name: longform
description: Write one long piece — a teardown, a field report, or a build log — from the vault's own receipts, then cut it into the posts and comments that point back at it. Use when the user says "write an article", "a blog post", "a teardown of X", "we should write something like that piece", "turn this into an essay", or when the monthly strategy check-in says the lane needs a flagship. Also handles LinkedIn Articles and X Articles.
---

# Longform

A post is worth a day. A good long piece is worth a quarter: it is the thing people link to, quote back at you, and remember you for, and it feeds four to six posts that each point at it.

This is a format the plugin knows how to execute, not a ritual with a slot in the calendar. Use it when the user asks for it, or when the monthly strategy check-in proposes it as an experiment because the evidence says long pieces work in their lane. Do not schedule it on a hunch, and never pad one out: a thin long piece is worse than no long piece.

## 1. Does the material carry a long piece?

Only three shapes earn the length, and each has an entry condition you can check in `stories/` before writing a word:

- **Teardown** — the field is using a word wrong, and you can prove it mechanically. Needs: the artifact you are arguing with (a post, a doc, a product page, quoted exactly), *and* your own measured numbers. Without numbers of your own it is a complaint.
- **Field report** — you ran something real for weeks and can say what happened. Needs: a start state, a change, an end state, and at least one thing that went wrong.
- **Build log** — you built the thing and can hand over the system. Needs: the decisions, including the two you reversed.

If no story file or cluster of story files meets the condition, say so and stop. Offer the strongest near-miss and what evidence would make it viable ("the DIY-memory conversations are a teardown as soon as we have our own contradiction numbers").

Prior art worth reading before a teardown: the "human-writing-skill" teardown skill (`github.com/MisreadableMind/human-writing-skill`), shared by Vitalii Ratushnyi in September 2026 after the team read a memory teardown they all wished they had written. The beats below are this plugin's own, but the discipline is the same: fairness before criticism, and nothing from memory.

## 2. Evidence ledger first, prose second

Before drafting, build `drafts/<slug>.evidence.md`:

- every claim you intend to make, one per line, each with its receipt: a story file, a ledger row, a primary source URL, or a number you measured this session;
- every artifact you quote, with the exact quote and its link;
- the alternatives and the people who hold the opposing view, in their words.

No slot gets filled from memory or inference. A line with no receipt is cut, not softened. Run the fact-checker agent against this file, not just against the finished draft.

## 3. The beats

Six, in this order on the page. Write them in whatever order the evidence supports; the mechanism section is usually easiest first.

1. **Cold open on the artifact or the event.** The thing that happened, or the sentence you are arguing with, quoted. No throat-clearing, no "in today's fast-moving landscape".
2. **Stakes.** Who is about to build on this, and what it costs them. Two or three sentences.
3. **Steelman.** The strongest version of the position you are about to take apart, in its advocates' own terms, long enough that one of them would recognise it. If you cannot write this, you do not understand the thing well enough to publish on it. This beat is what separates a teardown from a rant.
4. **The hinge.** One paragraph: the specific move that is wrong, named plainly.
5. **Mechanism and ceilings.** How it actually works, then where each advantage stops working. Concrete units throughout — "832KB", "six of fifty conversations", "50.4% against 82.8%" — never adjectives where a number exists.
6. **Receipts, failure modes, and the honest concession.** What you measured, where your own approach breaks, and the legitimate use you are handing back. Close on the open question, not a summary.

Length: 1,500–2,500 words. One analogy, in one section. No listicle, no bolded takeaway boxes, no "Key insights".

## 4. Voice and audit

Same rules as `write`: it is an edit of the user's own material, not generation from a topic. Pull their phrasings from `voice.md`, `inbox/` and their Slack and meeting language in the story files; keep their sentence rhythm. Then `stanley-audit --platform longform` (falls back to `--platform linkedin` rules minus the length cap) plus the critic agent reading as the target audience from `strategy.md`.

The watermark point from the README applies double at this length: the more of the sentences that started as the user's own words, the better the piece reads and the less there is for a detector to find. For a flagship piece, offer `humanpass` explicitly.

## 5. Where it goes, and the cut-down

Ask before publishing; this is the highest-stakes thing the plugin writes.

Destination, in order of preference: the user's own blog or newsletter (they keep the URL and the SEO), then LinkedIn Articles, then X Articles (the official X MCP can draft and publish Articles — see `references/platform-access.md`). A cross-post of the first paragraphs with a link beats a full duplicate.

Then the part that makes the month's arithmetic work — cut it down, and log it:

- 4–6 **posts**, one per beat that stands alone (the steelman is usually the best post, the receipts second), each written properly through `write`, each with its own hook, spread over the following three weeks. Mark them in `posts.jsonl` with `--story <slug>` so the ledger knows they share a parent.
- 2–3 **comment angles** for `scout`: when someone posts about this topic, the user now has a linkable answer.
- one **soapbox question** for the part the piece could not resolve.

Record the article itself with `stanley-vault post-add --platform article --url <url>` so the recap tracks it and the monthly can see whether the flagship moved anything.
