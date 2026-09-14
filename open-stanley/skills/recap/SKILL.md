---
name: recap
description: Report what the user's posts and comments did (impressions, reactions, comments, followers, who engaged), attach the numbers to the stories and lanes that produced them, and give one concrete recommendation. Use for "how did my post do", "daily recap", "weekly numbers", "who's engaging with me", and as the nightly scheduled task. Reads LinkedIn analytics and X analytics through the user's browser.
---

# Recap

The paid product's recap was "Today, 131 saw my content and 2 reacted." Numbers without a decision are noise. A recap here has three parts: what changed, who showed up, one thing to do.

## 1. Pull

Through the browser: LinkedIn post analytics for every post in `ledger/posts.jsonl` younger than 7 days (impressions, unique members, reactions, comments, reposts, saves if shown), profile follower count, and the notifications page for new comments/replies. X: post analytics (views, likes, replies, bookmarks, profile visits) and follower count. If analytics are unavailable in a remote run, report what the ledger has and say so.

Write the pulled metrics into the ledger: `skills/stanley/scripts/stanley-vault metrics-add --url <post url> --bucket 1h|24h|7d --impressions N --reactions N --comments N --reposts N [--saves N]`. Then run `skills/stanley/scripts/stanley-stats --vault <vault>` (add `--platform`): it prints the median, lifts by lane / shape / hook feature, the top and bottom posts, and the status of every experiment declared in `strategy.md`. Read its warnings literally: under 8 posts per arm it says "directional only", and so should you.

## 2. What changed (three lines max)

Only deltas: which post moved, versus the median in `strategy.md`; new comments that need a reply (with the commenter's name and the comment's first line); follower delta over 24h and 7d.

## 2b. Conversations you are in

Two places, both every run. (a) Comments on the user's own posts: the notifications page plus each post younger than 7 days. (b) Replies to comments the user left on other people's posts: `ledger/comments.jsonl` for the last 7 days, and LinkedIn `/in/<handle>/recent-activity/comments/` (X: `x.com/<handle>/with_replies`) for anything the ledger missed; open each thread and look for replies under the user's comment. The first recap only checked (a) and left a reply from a founder unanswered for a day; the user had to ask.

For every substantive reply or comment (a question, a disagreement, someone describing what they built, anything longer than a thank-you), draft the response and hand it over paste-ready; skip reactions and one-word replies. The register is a conversation, not a post: it is fine to open with "Yeah" or "Thanks"; no benchmark numbers, receipts or story lessons unless the person asked for them; no closing question by default. When the person is building something adjacent to the user's work, offer the next step (a call or DM) in plain words. Audit with `stanley-audit --platform comment`, then wait for a yes; post through the browser and `comment-add` with `--reply-to <url>`. Record the draft→final diff when the user rewrites it; the first such diff taught the plugin the paragraph above.

## 3. Who showed up

People who engaged twice or more in the window, with what they do (from their headline) and which post they reacted to. This feeds the monthly Orbit ritual. Never suggest engaging with them unless there's an actual thread to reply to.

## 4. The one recommendation

Pick one, with evidence from `stanley-stats`, never from memory. A lift on fewer than 3 posts (the table marks them `n<3: not a signal`) is not evidence for or against a shape; say "one post, no read" rather than calling a shape the user's worst. Examples: reply to X's comment now; the number-in-hook posts are running 3x, do another; you haven't posted in 9 days and the streak matters less than the compounding; the X account has 5 followers, so comments on larger accounts matter more than original posts there this month. When two posts in the same lane are underperforming, say the lane may be wrong, not the timing.

## 5. Weekly and monthly

Weekly (Sunday): same shape over 7 days, plus the `stanley-stats` experiment table. When an experiment reaches `min_n` per arm, state the result in one line and move it to "Resolved bets" in `strategy.md` with the numbers and date; propose the next experiment (one at a time, alternating variants post by post). This is the whole experimentation method: declare, alternate, wait for n, resolve, write it down. Monthly: rewrite the "what good looks like" section of `strategy.md` with the new median and top three, and hand the orbit list to `rituals`.

Keep the whole message under 12 lines. If nothing was posted and nothing moved, say that in one line and give the one recommendation anyway.
