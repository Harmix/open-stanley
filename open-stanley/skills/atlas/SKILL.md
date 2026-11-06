---
name: atlas
description: Map the user's vertical with public data — rank, compare or chart companies, tools, papers, funding, prices or usage from sources anyone could check, render the graphic with the bundled stanley-chart (no image model), and write the post around the one comparison nobody had seen laid out. Needs no meetings, no voice notes and no inside knowledge, so it is the lane a new account can post in from day one while mining warms up. Use when the user says "map the market", "rank the top N", "what does the data say about X", "make a data post", "do a Scholar-style post", or when the weekly drafts need one post that does not depend on the user's own stories.
---

# Atlas: a post from public data in your vertical

Why this exists. The two best posts of the plugin's first real account needed nothing from the user's own week: one was an observation about Google Scholar's recommendation feed with a screenshot, the other a comparison with a famous institution's name in the first line. A creator in mining with under 5K followers gets 1,300 reactions and 69 reposts on "Top 30 copper miners by market cap": a treemap of public market values, four specific details from filings, one methodology line, and an invitation to request the next map. The pattern is general. People in a vertical share a graphic that puts numbers they half-know next to each other, because sharing it makes them look informed. This skill makes that post on demand and on schedule; it is one lane among the user's lanes, never the whole account.

## 1. Pick the question (10 minutes, not an afternoon)

A good atlas post answers a question the audience in `strategy.md` argues about with a number they could check: who is biggest, who grew, how concentrated, what share, how much does it cost, what changed since last year. Pick by three tests: the top entity in the ranking is a name the audience knows (famous name in the first line is the single strongest signal in the ledger); the comparison has at least one surprise (a leader twice the runner-up, a well-known name far down, a share under 10% where people assume a majority); the data is public and dated within the user's freshness window. Keep a running list of candidate questions in `stories/atlas-questions.md`; the monthly check-in adds the ones comments asked for.

Rotate the shape across weeks: a ranking (treemap or bars), a share ("less than 9% of X is Y"), a concentration ("three companies are 72% of…"), a change over time, a price or cost comparison, a map. The same shape twice in a row is a series; three times is a habit the feed learns to skip.

## 2. Gather the numbers with receipts

Sources, in order of trust: primary filings and reports (annual reports, 10-K/40-F, regulator databases, company investor pages), official statistics, papers with the number in the abstract or a table, then well-known aggregators named as such. Each number gets a row in `stories/assets/atlas-<slug>/data.csv` (`name,value,group`) and a line in `stories/assets/atlas-<slug>/sources.md` (entity, value, unit, as-of date, URL). The story file `stories/atlas-<slug>.md` (`kind: atlas`, `origin: third-party`, `source:` the sources file) carries the question, the as-of date, what is included and excluded, and the three or four details worth a bullet.

Rules: one unit and one as-of date per graphic (say which: "market value at close, 4 Nov 2026"); mixed currencies converted and the rate stated; if two sources disagree by more than a few percent, use the primary one and footnote the other; no number from memory, ever. The fact-checker agent recomputes the ranking from `data.csv` before publish.

## 3. Render it

`skills/stanley/scripts/stanley-chart stories/assets/atlas-<slug>/data.csv --kind treemap|bars --title "<claim as the title>" --subtitle "<what is measured, as-of date>" --unit "<unit>" --source "<sources, short>" --top N --out drafts/<date>-atlas-<slug>.image.png`. The title states the finding, not the topic ("Four copper miners are worth more than US$100 bn", not "Copper miners"). Add a `domain` column (e.g. `bhp.com`) and each tile gets the company's favicon when the machine can fetch it (a `logo` column takes a local file); a ranking with logos reads as a map of the industry rather than a chart, which is what gets shared. Treemap for a ranking of 10–40 entities with one or two groups; bars for under 12 or when exact values matter. The script writes HTML always and a PNG where Chromium exists, metadata stripped; on a machine without Chromium, render in the cloud container or screenshot the HTML with the browser tool, then `stanley-vault image-clean`. Never an image model. A screenshot of the source itself (the filing table, the feed) is also a valid graphic when the point is "look, this is what it says".

## 4. Write the post (through `write`, in the user's voice)

The shape that works, four parts and nothing else:
1. The finding in the first line, with the famous name: "Top 30 copper miners by market cap." / "Four companies in this selection are valued above US$100 billion: BHP at…"
2. One line of method in plain words: "I have mapped 30 listed companies…", "Each tile is the whole company's equity value, including its other businesses."
3. Three or four details behind the names, one per bullet, each with its own number and a reason it is interesting (a second year at the same level, a target for 2027, a by-product nobody counts). This is where the post earns reposts: the reader learns something about a name they knew.
4. The next-map invitation: "Let me know what data you would like displayed next." It is a specific ask, not "thoughts?"; comments that name a dataset are the next post's queue, and the monthly check-in reads them.

No opinion paragraph, no lesson, no "this shows that the industry…". The user's own view goes in the first comment if they have one. Hashtags: this is the one post type where 3–4 topical hashtags are tolerable in the ledger of creators doing it well; follow `strategy.md`, default none. Audit as usual (`--has-image`); the `landing:` line should read named-entity-early=yes, number-or-receipt=yes, has-image=yes.

## 5. Cadence and what to log

One atlas post a week at most, in the slot the research marks for insight posts, never two data posts in a row. Tag the ledger row `--lane atlas --shape opener:finding ending:invitation --image image` so `stanley-stats` can compare the lane against the user's own-story lanes after eight posts; if it wins, the monthly check-in says so and the mix shifts, if it loses, the lane drops to monthly. Every comment that asks for a dataset goes to `stories/atlas-questions.md` with the commenter's name (that is a people story too).

## What it is not

Not a replacement for the user's own stories: an account that is only maps becomes a feed, not a person, and the research shows first-person posts travel further per follower. Not an excuse for a number without a receipt. Not a place for AI-generated imagery.
