# Platform rules, September 2026

Numbers are the current best evidence from the sources in `docs/research/` of the parent repo; they drift, so treat bands as bands. The audit script enforces the hard ones.

## LinkedIn

- **Ranking**: unified LLM retrieval + generative recommender (Mar 2026). Signals: dwell time, saves, comments with substance (≥ ~12 words from accounts that don't comment on everything), reshares with text, and *shown-and-skipped* as a hard negative. The first 60–90 minutes decide whether a post leaves the 1st-degree network.
- **Generic-AI demotion** (May 2026, classifier; "Seems like AI slop" button Jul 2026): flagged posts stay visible to connections but are not recommended. No public false-positive rate. Assume anything that reads like a template is throttled.
- **Length**: 1,300–1,900 characters for stories; the first ~140 characters (about two short lines) show before "…more". The hook must be a complete thought at the cut.
- **Format**: plain text wins at authority scale; native document (PDF carousel) and multi-image posts get higher engagement rate for how-tos; video is fine but not required. No hashtags. No links in the body; links in the first comment are also throttled now, so link only when it's the point.
- **Cadence**: 2–4 posts/week beats daily; one post per ~18 hours minimum so posts don't cannibalize. Tue–Thu 8–10am local is still the best window, but consistency beats timing.
- **Comments**: replying to every comment in the first hour matters; comments on others' posts should be 1–3 sentences with a specific observation, no agreement opener, and ideally on posts under 2 hours old from accounts larger than yours.
- **Profile**: the headline shows under the name on every post; keep it a claim, not a title list.

## X

- **Ranking**: replies the author answers carry the largest weight; then reposts with quotes, bookmarks, profile clicks. First ~30 minutes decide ~70% of reach. Links in the post body cut reach; put them in the first reply.
- **Premium** is effectively required for reach (~10x per post in Buffer's 18.8M-post dataset) and for long single posts. Without it: 280 chars, threads.
- **Threads**: 3–7 tweets, only when the story is sequential. Tweet 1 stands alone. No "🧵" or "a thread:" unless the exemplars do it. The last tweet carries the claim.
- **Replies**: 15–20 substantive replies/day to accounts 5–20x your size, within minutes of their posting, is the growth engine for small accounts. Replies to accounts that haven't mentioned you must go through the browser; the X API refuses them.
- **Bots**: X hunts automation at the account level; posting via the user's own browser session is safest. Don't post identical text to LinkedIn and X within seconds from an API; mirror through the browser or space it.

## Cross-posting

Same story, different packaging: LinkedIn gets the story with paragraphs; X gets the sharpest claim first and the story as the thread. Never post the LinkedIn text unchanged to X unless the user has Premium and the exemplars show they do that.
