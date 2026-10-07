# External evidence on what works on LinkedIn (2026)

Priors for the experiment loop, not rules. The monthly strategy check-in reads this when it proposes the next experiment; `write` and `stanley-audit` carry the few findings that are large, consistent, and cheap to check. Everything here is correlational and from other people's accounts; the user's own ledger decides.

## Virio, "What 226,000 LinkedIn Posts Revealed" (March 2026)

25 research agents over 226K B2B posts, validated on 236 held-out posts, then compared with 20 ghostwriting clients (1,138 posts before, 527 after). Public engagement only; no pipeline metrics. Shared by Krishan Karia, October 2026.

Higher engagement, by effect size:
- **Career milestone posts: +56–108%**, the strongest type in every industry. Milestone + gratitude ("Grateful to [Name] for…") adds ~30% on top.
- **Opening with "I…": +8–25%** over "You should…" framing. Across their 20 clients fewer than 10% of posts started with "I", so it is under-used even by paid writers.
- **Ending with a question: +4.4% comments**, 2.2x stronger for B2B executive accounts; asking for comments outright: +6.2% comments. These drive comments, not reactions.
- Specific numbers ("$2M ARR" over "strong revenue growth"): +5%. Naming real people and companies: +5%.

Lower engagement:
- **Opening with a question: −5%**, worse at 3+ posts/week.
- **Two text-only posts in a row: −8 to −11%**, the biggest avoidable penalty at 3+/week.
- **URLs in the body: −4 to −8%**; put the link in the first comment.
- "You should" advice framing: −2%. "Unpopular opinion"/hot takes: the worst risk-reward of any pattern (0.5% viral, 1.3% flop). Tension→resolution arcs underperform a steady positive tone.

Images depend on account size: **under 5K followers +12%**, 5–50K −1 to −2%, 50–100K neutral, over 100K slightly positive. (Their own clients, mostly 5–50K, saw images win anyway; they say so and call it unresolved.)

Reactions are not interchangeable. **Insight (💡) is the single best predictor of reposts** (top-10% insight-share posts get 8x more reposts); Celebrate drives volume but not resharing; Love builds depth, not reach; a high **Like share means people scrolled past** and correlates with lower performance. Insight and Celebrate suppress each other, so a post optimises for one. Insight/Celebrate peak Tuesday–Wednesday, Love on Sunday, humour on Friday.

Cadence and cycles: each extra weekly post costs ~2% per-post engagement but total weekly reach still grows; each additional *format* in a week (text, image, carousel) adds ~3.6%. Creators cycle through slumps (~13 posts), cold plateaus (~19 posts, the hardest to leave), warm growth (~16) and hot streaks (~8, short). This is normal cycling, not a content problem. Posts off a creator's usual topics get ~22% less engagement, while creators who widen topics slowly over months improve: consistency week to week, evolution quarter to quarter.

Their clients after ghostwriting: median post length 522 → 1,670 chars; comments 2 → 4; insight share 2.2% → 4.4%; 14 of 20 improved on engagement, 6 got worse (strong organic baselines or tiny samples).

## Philip Sørensen (Brew), "I finally cracked the LinkedIn algo" (September 2026; 208 reactions, 53 comments)

Founder's own account, not a study. Five claims: (1) write for the followers you already have — LinkedIn's first test batch is largely them, so check Settings → Audience for the top country and write for it; (2) use less AI, a few minutes of your own thinking per post is now the bar; (3) be positive and shout people out after events and meetings, "everything you do is content"; (4) be yourself, the only advantage left; (5) posting time does not matter. The comments push back on (5) and note the trade-off between impressions and reaching the actual ICP. Shared by the user, October 2026.

## What this plugin does with it

| Finding | Where it lives |
|---|---|
| First-person opener; no "you should"; no question opener; no hot takes | `write` §2 and `stanley-audit --platform linkedin` (`question-opener` WARN, `advice-framing` INFO, `hot-take` INFO) |
| Two text-only posts in a row | `stanley-audit` reads the previous post's `image` flag from the ledger; `post-add --image` records it |
| Images for accounts under 5K followers | `my-human.md` `followers:` line; audit says which side of 5K the account is on |
| Ending with a question | the `ending` experiment, classified from the text; an arm with no posts is reported as starving |
| Milestones, gratitude, shout-outs after events | `mine` §2 story kinds `milestone` and `people` |
| Insight share, like share | `metrics-add --insight --celebrate --love --like`; `stanley-stats` reports insight and like share; recap reads the reaction breakdown |
| Performance cycles; on-brand drift | monthly check-in: no lane change on fewer than ~20 posts; slumps are cycles |
| Format mix per week | monthly format-gap step; the weekly drafts vary format when the ledger shows a text-only run |
| Posting time | not a rule; a candidate experiment at most |
