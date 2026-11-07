---
name: study
description: Learn how a specific writer wins on LinkedIn or X — Paul Graham, Dharmesh Shah, Yamini Rangan, Yuriy Zaremba, or anyone the user names — by reading their recent posts through the user's browser and extracting reusable *shapes* (openers, structures, endings, specificity moves, cadence) into a shapes catalog, never their sentences. Use when the user says "write like Paul Graham", "learn from X's posts", "why do their posts work", "study my competitor", or when write needs a shape for a lane. Ships with a catalog of the creators studied in September 2026.
---

# Study: shapes, not sentences

"Copy Paul Graham's style" was the most repeated instruction in the chat log this plugin came from, and the paid product answered it with adjectives ("plain, one thought, no structure") and then wrote 120-word essays. A style is learned from examples and stored as *shapes*: the moves a writer makes that another writer can make with different material. Sentences stay with their author.

## 1. Read

Through the `browser` capability, logged in as the user: the creator's LinkedIn recent-activity page (posts tab) and X profile. Collect 20–40 posts with dates and engagement. Sort by engagement relative to their own median; the top quartile is what to learn from, the bottom quartile is what to avoid. Save the raw pull to `inbox/study-<handle>-<date>.md` (private; it's for analysis, never for reuse).

If the browser is unavailable, search results expose first lines and comment counts; that is enough for openers and cadence, not for structure. Say which you had.

## 2. Extract shapes

For each top-quartile post, name the moves. Use the vocabulary in `references/shape-vocabulary.md` so shapes are comparable across creators:

- **Opener**: event / claim / number / question-to-self / list-promise / "one of…"
- **Body**: single observation / story → lesson / argument-you-lost / numbered steps / contrast (then vs now) / product episode
- **Specificity**: what only they could know — exact number, named person, dated event, their own mistake
- **Ending**: flat last line / callback to opener / one open question / CTA with price / p.s.
- **Length band, paragraph shape, sentence-length spread**, punctuation habits (em dashes? parentheses? "p.s."?)
- **Cadence and mix**: posts/week, text vs image, how often they sell
- **What they never do** (from the bottom quartile and from absence): hashtags? questions? emoji?

Write `shapes/<handle>.md` in the vault: 5–10 shapes with a one-line description and *paraphrased* evidence ("opens on a lost argument: 'One of the debates I've had for 15+ years (and pretty much always lost)…'"; a quoted fragment under ~15 words is fine as a pointer, a whole post is not). Add the creator to `shapes/index.md`.

## 3. Use

`write` reads `shapes/` when the user asks for a shape ("PG-style comment", "a Dharmesh-style episode post") or when a lane in `strategy.md` names a reference creator. The shape supplies the moves; the user's story supplies every word of content; `voice.md` supplies the sentence-level voice. If a draft could be mistaken for the studied creator's post, it has failed: the reader should recognize the user.

## 3b. Public teardown (the creator-spotlight loop)

A teardown written for the user's own vault is a shapes catalog. A teardown written for the public is also distribution: the creator shares it ("someone studied my posts"), their audience reads it, and the page is a third-party-looking citation for AI search. The paid product's founders did this by hand as cold email with a personalized analysis; the plugin does it weekly as a page (`templates/scheduled-tasks/creator-teardown-weekly.md`).

A public teardown: 500–900 words, Markdown with front matter (`layout: default`, `title`, `description` (one line), `creator`, `platform`, `followers` read this run, `posts_read`, `date`); the site's Jekyll layout styles it, sections: what the numbers say (median and top three, read this run, nothing from memory), the five shapes with one described example each (described, never quoted beyond six words), cadence and images, and "what a founder in <vertical> could borrow this week". Say what did not work for them too; a teardown that is all praise is an ad. Never a sentence of theirs reproduced, never a private detail, never a guess about their business. Saved to `docs/creators/<slug>.md` in the repo named in `my-human.md` (`teardown_repo:`), linked from `docs/creators/index.md`, committed, not pushed. When the teardown repo is the Open Stanley repo itself (it contains `open-stanley/skills/study/references/`), add the same findings as a shapes-only entry at the top of `open-stanley/skills/study/references/creators-latest.md` in the same commit, replacing that creator's older entry there: tags from the shape vocabulary, the numbers read this run, no sentence of theirs. That file ships with the plugin, so every user's `write` and `rituals` get the finding at the next version bump. Any other repo: the vault's `shapes/<handle>.md` is where it stays, and `/open-stanley:learn` can propose it upstream. Run the teardown and the note through a plain-language pass before handing them over (no em dashes, no punchline lines, no bold lead-in lists, no claim the numbers don't show). The two-line note to the creator is drafted and left for the user's yes. Its "one thing surprised me" line must be a pattern across posts that the creator cannot see on any single post's analytics page (a whole class of posts landing above or below their median, a shape that changes comments per reaction), never "post A beat post B" or "your best post was X".

## 4. Ships with

`references/creators-latest.md`: one entry per creator from the weekly public teardowns, newest first; where a creator appears in both files, this one wins. `references/creators-2026-09.md`: shapes for Paul Graham (X), Dharmesh Shah, Yamini Rangan, Yuriy Zaremba, and Vitalii Dodonov, derived from live reads of their feeds on 8 Sep 2026. Re-study every quarter; shapes drift with platforms.
