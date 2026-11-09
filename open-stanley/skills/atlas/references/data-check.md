# The atlas check: rules first, two sweeps, a blind rebuild, a script

Why. The first real "Top N" atlas post (Toronto AI startups by money raised, Nov 2026) went through four rounds of checking because each round re-read the numbers by eye and each checker invented its own scope. Companies went in and out, amounts changed, a round was counted and then dropped, coverage leaned on one tracker, and the obvious #1 (Cohere) was missing from the first version. The fourth round, run this way, found that 6 of 19 rows broke the rules: three companies were headquartered elsewhere, one round closed outside the year, one product was not AI, one round went to a parent company, and one qualifying company was missing. Do it this way the first time.

No check can promise the sources are right. What it can promise is that any error left comes from a source, not from us.

## 1. Rulebook before any checking: `rules.md`

Write it, freeze it, and cite it on every include and exclude. A later checker cannot change the scope. The template:

- R1 Place. What counts as "in" the place (city limits or metro; the company's own materials win over aggregators; dual headquarters footnoted).
- R2 Kind. What counts as the category ("AI startup": private, venture-backed, AI is the core product, not a feature).
- R3 Money type (or metric type). What counts (priced rounds, SAFEs, notes) and what does not (debt, grants, secondaries, acquisitions, milestone money, lifetime totals).
- R4 Date. Which date decides the period: announced, first reported, or closed. This is a judgment call: ask the user once, with your recommendation, before checking, and write their answer into the rule with the date.
- R5 Amount. Source figure, currency conversion with the rate stated, "over X" = X, "up to"/targets shown separately (dashed outline on the graphic, `status=target` in data.csv), currency not stated = excluded.
- R6 Ranking. How rows combine, ties, the cut.
- R7 Claims. Every number, date, name and description in the post, the graphic, the footnote and the first comment has a row in `claims.csv` with a URL and an exact quote opened in this session.

## 2. Two coverage sweeps by different methods

One sweep goes through the news month by month for the period (the sector's trade press and the national business press). The other goes through dedicated trackers and lists (a national AI index, Crunchbase news, VC portfolio pages, sector searches). Before either, search the biggest names the audience knows in the space by name: a "Top N" that misses the obvious #1 is a failed post. Every candidate goes into `candidates.csv` with `decision` and `rule`. Compare the two sweeps. Anything only one of them found gets opened and settled.

## 3. A ledger of every claim: `claims.csv`

`claim,value,url,quote`. The quote is the exact sentence from the source, and the value must appear in it. A number you computed (a total, a ratio, a share) gets `url` = `computed` and a Python expression over `d` (name -> value) as the quote: `5000 / (sum(d.values()) - d["Cohere"])`.

## 4. A blind rebuild

Give a second agent only the company names and `rules.md`, never your numbers, and have it rebuild every figure from sources it opens itself. Compare its table with `data.csv` row by row; open every disagreement and settle it with a source.

## 5. The script

`skills/stanley/scripts/stanley-trace --data data.csv --claims claims.csv drafts/<post>.md graphic-labels.txt first-comment.txt` must print PASS. It refuses any number in the text that is not in `data.csv` (or a total of it, or the same value in the next unit up) and not in a sourced or computed claim. Other currencies, percentages and ratios always need a claim. Write the graphic's text to `graphic-labels.txt` (title, note, tile labels, footer) so the graphic is checked too, and render the graphic from the same `data.csv` with `stanley-chart`, never by hand-copying numbers.

## 6. One adversarial pass on the final version

A fresh agent reads the final post, graphic and first comment and tries to break one claim. Fix what it finds and run step 5 again.

Keep everything in `stories/assets/atlas-<slug>/`: `rules.md`, `candidates.csv`, `data.csv`, `claims.csv`, `sources.md`, `graphic-labels.txt`, and a `reconciliation.md` listing every exclusion with its rule and source. Then the post can be defended line by line when someone asks.
