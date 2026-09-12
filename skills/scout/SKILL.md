---
name: scout
description: Scan the user's LinkedIn and X feeds (through their own logged-in browser, or any social MCP they have) for posts worth commenting on, and draft paste-ready comments in their comment voice. Use when the user asks "anything worth commenting on", "find posts to engage with", "who should I reply to", "what's trending in my niche today", or as the scheduled 10am/10pm scan. Also handles "draft a comment for this link".
---

# Scout

The paid product's scan job was the feature the user kept and the one that failed most: wrong posts, no LinkedIn, duplicates, his own posts, comments that read like essays. Each step below removes one of those.

## 1. Read the feeds as the user

Use the `browser` capability, logged in as the user. Sources, in order:
- LinkedIn home feed (scroll ~3 screens), then LinkedIn search for each lane's 2–3 key phrases sorted by recent, then the "Posts" tab of 5–10 accounts listed in `strategy.md` as people to be near.
- X: home/For You (~3 screens), a list if the user has one, and search for lane phrases with `min_faves:50` where the UI allows it.
- If a `post`/social MCP with feed-reading tools exists, use it as a supplement, not a replacement (API feeds lack the ranking the user actually sees).

Capture for each candidate: URL, author handle and display name, follower count if shown, age of the post, reactions/comments, the text. Save the raw pull to `inbox/scan-<date>-<am|pm>.md` so a re-run never re-scrapes.

If no browser is available, say so and ask the user to paste links; do not fabricate candidates from memory.

## 2. Filter (hard)

Drop anything that is:
- by the user (`skills/stanley/scripts/stanley-vault is-self <url or handle>`), or a repost/reshare of the user's post;
- already in `ledger/surfaced.jsonl` (`skills/stanley/scripts/stanley-vault surfaced-check <urls...>`);
- older than 24h on LinkedIn or 6h on X (comments on stale posts don't get seen);
- a product announcement, a news roundup, a job post, or generic AI hype with no argument in it.

## 3. Score (soft) and pick 2–3 per platform

Score 0–5 on each, keep the top:
- **Lane fit**: the post is about one of the lanes, or directly invites the user's thesis.
- **Adjacent-viral**: high engagement on how work, teams, meetings, hiring, or org knowledge actually function, where the user's angle is a natural reply even though the post never mentions their field. This is the pattern the user pointed to as the one that was missed ("I need more posts like Matt's"). Weight it as much as lane fit.
- **Reach**: author bigger than the user (5–20x on X) and the post is still rising.
- **Openness**: the post asks something, admits something, or takes a position someone could add to. Skip announcements.
- **Freshness**: under 2h is best on both platforms.

Explain the pick in one line each ("4.9k likes, meetings-are-broken take, your 80%-of-questions-were-answerable data is the reply").

## 4. Draft the comment

Read the comment exemplars in `voice.md` first. A good comment here is 1–3 sentences: one observation from the user's own experience or data (with a receipt in `stories/` if it's a number), no agreement opener, no restating the post, no wrap-up. It should read like the person typed it in 30 seconds because they had one specific thought. Two shapes that worked for this user:
- an observation plus a pointed question back to the author ("how do you know which project context is still relevant? most projects are dynamic, and decisions change or conflict between meetings and emails");
- a plain first-person data point ("we tested this: the agent answered 80% of the recurring questions; the other 20% were decisions that only existed in the meeting").

Audit each with `skills/stanley/scripts/stanley-audit - --platform comment --vault <vault>`.

## 5. Deliver and record

For each pick: the link, the author, one line of why, then the comment on its own lines so it can be copied. Then ask: post which? The user may answer with numbers.

- Approved → post through the browser (LinkedIn comment box; X reply box, which works for any account, unlike the API) or through a `post` MCP; then `skills/stanley/scripts/stanley-vault comment-add`.
- Skipped → `comment-add --skipped --reason "<their words>"`; the reason tunes the next scan.
- Everything shown → `skills/stanley/scripts/stanley-vault surfaced-add <urls> --author <handle> --platform <p>`.

Also record what the user posted if they changed the text; the diff is voice data (`diff-add --kind comment`).

## 6. Widening when told

When the user says "you missed this one" and gives a link, read it, say in one line what feature made it a good target that your filter missed, add that feature to `instructions.md` with the date, and re-weight. Don't just apologize.
