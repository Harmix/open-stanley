# Strategies

The same list as the landing page (`docs/index.html`, #strategies). Your own stories come first; the rest are for thin weeks and new accounts, and the ledger's numbers decide which ones stay for each person. This list grows: new creator teardowns (`docs/creators/`, `skills/study/references/creators-latest.md`, the vault's `shapes/`) and tactics users send with their numbers (the `strategy-tip` issue form) are added under "From teardowns" and "From users" with the source and the numbers. Read those two sections first every time; they are newer than the rest.

Each entry says what it is, where it runs in the plugin, and the evidence: "tested here" (users of this plugin have numbers), "from a teardown" (a creator page in this plugin), or "untested here". Say the label when you offer it.

## The list

- **Your stories.** What happened to you this week, with the source. Runs in `mine` → `write`, weekly drafts, the morning question. Tested here: the first user's two furthest posts were "I asked / I saw" stories with an institution's name in the first line and a real screenshot (87,288 and 31,324 impressions on an account under 5K followers). Needs connected sources; with two or fewer it runs dry.
- **Atlas.** Your industry mapped from public data; works from day one, no stories needed. Runs in `atlas`. Tested here and from a teardown: "Top 30 copper miners by market cap" (1,342 reactions on under 5K followers), "Top 17 Toronto AI startups by money raised in 2026". Strongest for people who sell into one industry or city and need credibility there.
- **Observation.** A screenshot of something odd and one plain line about it. Runs in `write` from a story of `kind: observation`; `scout` and the morning question find candidates. Tested here: the Google Scholar alert post.
- **Experiment.** A small test you ran, raw outputs saved, result first. Runs in `mine` (`kind: experiment`, assets saved) → `write`. Tested here, with one lesson: the first one flipped when rerun under a cleaner setup, so the numbers must be recomputable from the saved files.
- **Series.** A build log, each post linked to the one before. Runs in `write` + `publish` (the "How this started" first comment). Tested here (the hackathon hour-by-hour posts and the YC series).
- **Repackage.** The shape of your best post with a new story in it. Runs in `rituals` every two weeks from the ledger's top posts.
- **Study.** What works for creators in your field, and in one field outside it. Runs in `study`; weekly teardowns on the site. From teardowns, e.g. Dharmesh Shah: a habit, then the exact request to his own product pasted in, the price last; his reshares of others' praise were all in his bottom quarter.
- **Longform.** One long piece a month, cut into posts. Runs in `longform`.
- **Yours.** A tactic a user sent with their numbers; if it holds up, it goes in below with their name.

## From teardowns

(Add one line per creator page as teardowns are published: the creator, the field, the one move that beat their median, the numbers, the page.)

- Dharmesh Shah (SaaS founder, LinkedIn): habit then the tool; price in his own words beats borrowed praise. `docs/creators/dharmesh-shah.md`.
- James Hawkins (PostHog co-founder, LinkedIn, 65K followers): jokes about startups and AI, never naming his own product. A screenshot or meme with a caption of 0 to 17 words had a median of 493 against his 259 and all three of his biggest posts; a parody list ranking something every founder knows had a median of 901; reshares of his company sat at the bottom. Pictures brought reach, text jokes brought replies, and his first post of the day beat the second. For an audience with a shared inside world, this is the evidence for Observation as a joke. `docs/creators/james-hawkins.md`.
- A mining data designer (LinkedIn, under 5K followers): "Top N <names the audience knows> by <one number>" treemaps; the most universal unit and the biggest names won. See `skills/atlas/SKILL.md`.

## From users

(Tactics accepted from the `strategy-tip` form, with the sender's name, their numbers and the date checked.)

## Formats and modes are not strategies

Any strategy can come out as text, an image, a carousel, a data graphic or a short video (`video` skill), in any language, on any platform the person uses. How much the plugin writes is a mode (`drafting: drafts | questions`), and how often it runs is a schedule (`schedule: standard | light`). All of these live in `strategy.md` and change with one sentence ("switch me to questions only", "I'm on Threads now"); they never need a different skill or a different scheduled task.
