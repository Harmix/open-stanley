# Onboarding misses (so they don't repeat)

Each entry: what went wrong, how the human caught it, the rule that came out of it. Add to this file whenever an onboarding diagnosis is corrected by the person. Contributions to the community stats use the rule line only, never the person's data.

## 2026-09-12 — named the wrong best post

**What happened.** The first onboarding read the LinkedIn recent-activity feed (27 items), seeded the ledger from it, and reported a 2025 program-acceptance post (107 reactions) as the person's best. The person's best post by a factor of ten was a June 2026 observation post about a Google Scholar alert hack: 31,324 impressions, half of the whole year's reach, with only 24 reactions. It was not in the feed pull, and the strategy file even carried a note saying "get its numbers from the analytics page" that nobody acted on.

**Three separate mistakes.**
1. Read the feed, not the analytics. The feed is ordered by recency, so anything older than a few weeks needs scrolling that the browser tools cut short. The creator analytics `top-posts` page lists a full year sorted by impressions in one page load.
2. Ranked by reactions only. Reactions come from the network (friends congratulating a milestone). Impressions come from the algorithm sending a post outside the network. The two rankings disagree, and the one the person cares about is usually reach.
3. Quoted a number that was never on a page. The 4,290 impressions attributed to the program post came from a misread; the analytics page shows 100 in-window. Numbers come from a page read this session or they do not appear.

**How it was caught.** The person said "nope, my best post is the Google Scholar distribution hack".

**Rules now in the skill.**
- Analytics first (`/analytics/creator/top-posts/?metricType=IMPRESSIONS&timeRange=past_365_days`, then `ENGAGEMENTS`), feed second.
- Ask "which of your posts do you think did best?" before diagnosing, and treat a mismatch as a missed read, not a difference of opinion.
- Report top-by-reach and top-by-pull separately (`stanley-stats` now prints both and warns when they differ).
- Seed the ledger with impressions, and with dates decoded from share ids where available.
- No number without a page read this session.

**What the post itself teaches (goes in the lane notes, not here).** Third-party observation, named famous people, one absurd concrete example, a screenshot as the receipt, a punchline last line, no product, no hashtags, 90 words. It is the shape of a post that leaves the network.
