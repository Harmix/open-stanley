# Audit rules and the evidence behind them

Rule ids match the linter output. "Evidence" cites the research bundle in the parent repo (`research/detection-and-platforms.md`) unless noted.

| id | level | what | why |
|---|---|---|---|
| `lexicon` | BLOCK | Words and phrases with measured LLM over-representation (delve r≈28, intricate, pivotal, meticulous, underscore, showcase, realm, testament, landscape, navigate, unlock, elevate, robust, seamless…) and the LinkedIn-guru set ("here's the thing", "let that sink in", "game-changer", "makes you wonder", "the implications are", "foundational shift", "this resonates") | Kobak et al. 2024 excess-vocabulary study over 15M abstracts; Juzek & Ward, COLING 2025 (RLHF origin of the tells); LinkedIn's own May 2026 examples; Wikipedia's Signs of AI writing |
| `lexicon-user` | BLOCK | `banned_extra` from `voice.md` | Personal idiolect: the person never says it |
| `weasel` | BLOCK | "experts say", "studies show", "recent literature", "industry reports" without a name | Wikipedia taxonomy item 4; the export's "recent literature shows" fabrication |
| `not-x-but-y` | BLOCK | "It's not X, it's Y" / "isn't just X, it's Y" | LinkedIn named it explicitly (May 2026); Wikipedia item 3 |
| `editorial-tail` | WARN | fact + ", highlighting/underscoring the need for…" | Wikipedia item 2 |
| `em-dash` / `em-dash-density` | BLOCK/WARN | any em dash when `voice.md` bans them; density > ~0.15/100 words otherwise | AI business writing ≈0.71/100 words vs human ≈0.06–0.11 (aislopscanner, 700k words) |
| `tricolon` | INFO | three-item lists | Wikipedia item 7; one is fine, a pattern isn't |
| `choppy` | BLOCK | ≥3 consecutive sentences under 8 words | The user's own feedback ("I don't like such short sentences, it reads like AI"); burstiness is a detector feature |
| `uniform-length` | WARN | sentence-length stdev below the voice floor | Burstiness; Wikipedia item 8 |
| `one-line-paragraphs` | WARN | >50% of paragraphs are ≤6 words | LinkedIn-guru scaffolding; reads templated in 2026 |
| `bold-colon-list` | BLOCK | `**Term**: restatement` items | Wikipedia item 6 |
| `closing-question` | BLOCK/WARN | generic audience question at the end ("what do you think?") | Engagement bait is demoted; a specific open question is allowed when `voice.md` says so |
| `setup-sentence` | BLOCK | "In today's…", "Have you ever…", "Let's talk about…" openers | The user cut every setup sentence in his edits; hook is the only thing shown before "…more" |
| `empty-opener` / `agreement-opener` | WARN/BLOCK | comments that start "This is so real / such a crucial point / great post" | The comments the user actually posted never did this; LinkedIn treats restating comments as bot-like |
| `wrap-up` | BLOCK | "In short / Ultimately / The takeaway is" closers | The user: "reads like a conclusion, I want to open a discussion" |
| `no-specifics` | WARN | no numbers, names, dates, places in >60 words | Detectors and readers converge on specificity; generic-true = generated |
| `no-first-person` | WARN | no I/we/my | Stories need the author in them |
| `emoji` | WARN | >2 emoji | Template signal |
| `hashtags` | BLOCK | any, unless `max_hashtags` raised | 2026 reach data: zero |
| `link-in-body` | BLOCK (LinkedIn) | URL in the post | Reach penalty; first comment or nothing |
| `length` / `hook-length` | WARN/INFO | outside 1,300–1,900 chars; first line > ~210 chars | Dwell band; ~140 chars shown before the fold |
| `engagement-bait` | BLOCK | "like/share/comment if" | Demoted |
| `x-length` / `tweet-length` / `thread-length` / `link-in-first` | INFO–BLOCK | 280-char rule without Premium; 5–7 tweets max; links in first reply | X ranking notes in `skills/write/references/platforms.md` |
| `receipt-number` | WARN | a number in the draft that appears in no story file | Rule 3: no receipt, no claim |
| `dated-claim` / `freshness` | INFO | years mentioned; "just/yesterday/today/breaking" | The user's freshness rule; the 2024–25-papers-as-news failure |
| `uncited-study` | BLOCK | "a study found" with no name | Same |
| `self-plagiarism` / `self-overlap` | BLOCK/WARN | 3-gram Jaccard > 0.35 / > 0.15 with any ledger post | "Almost a copycat of my post" (day-1 failure) |
| `comment-length` | WARN | > 70 words in a comment | The user's posted comments were 1–3 sentences |
