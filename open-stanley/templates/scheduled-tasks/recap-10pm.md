# Recap (daily 22:00 local)

{{PREAMBLE: _preamble-laptop.md by default, _preamble-cloud.md for cloud mode}}

Job: recap. Promise: "what changed today, who showed up, one recommendation, under 12 lines."

Follow `/open-stanley:recap`. Laptop mode: read LinkedIn analytics (`/analytics/creator/top-posts/?metricType=IMPRESSIONS&timeRange=past_365_days` plus each recent post's page) and X analytics through the browser and `metrics-add` every post younger than 7 days. Also read the 90-day total at `/analytics/creator/content/?metricType=IMPRESSIONS&timeRange=past_90_days` and run `stanley-vault milestone-check --impressions-90d <number>`; on `CROSSED`, draft the milestone post in this run (recap 4c). (Cloud mode only: X via the X MCP, and queue an `analytics` job for LinkedIn; include what is still in the queue and since when.) Attach metrics to the ledger. If nothing was posted and nothing moved, say so in one line and still give the one recommendation with evidence from the ledger.
