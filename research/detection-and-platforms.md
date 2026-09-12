# Deep Research Report — 8 September 2026

Three sections. Confidence tags: **[A]** primary/official or peer‑reviewed · **[B]** credible press or independent third party · **[C]** vendor marketing / SEO blog — treat as directional only.

---

## Section 1 — AI‑text detection, stylometry, and platform enforcement in 2026

### 1.1 How the detectors actually work

Three technical families, in rough order of how much they matter commercially in 2026:

| Family | Mechanism | Who uses it |
|---|---|---|
| **Statistical / zero-shot** | Score text by *perplexity* (how surprising each token is to a reference LM) and *burstiness* (variance in sentence-level perplexity/length). Human writing is high-perplexity and high-variance; instruction-tuned LLM output is low-perplexity and metronomic. Modern variants: **Binoculars** (ratio of two LMs' cross-perplexity), **FastDetectGPT** (curvature of the log-likelihood surface). | GPTZero's original 2023 method; still the academic baseline. |
| **Supervised neural classifiers** | Fine-tuned transformers trained on large paired human/AI corpora; learn *post-training artifacts* (RLHF style) rather than "AI-ness" per se. | Pangram, Originality.ai, Copyleaks, Turnitin, GPTZero's current stack (which layers classifiers over the perplexity features). |
| **Watermarking** | Provider-side. **SynthID-Text** biases the sampling distribution via a tournament over a keyed pseudorandom function; detection requires the key. Open-sourced and shipped in Hugging Face Transformers ≥ v4.46.0. | Google/Gemini. Effectively *nobody else* for text. |

Key structural facts:

- **Watermarking is a dead letter for third-party detection of social text.** SynthID-Text is open source and running across Gemini, and the 2026 SynthID coalition announcements (OpenAI, NVIDIA, ElevenLabs, post–Google I/O May 2026) are about **images and audio**, not text. C2PA 2.1 became an ISO standard with 6,000+ member orgs, but C2PA is metadata attached to media files — it does not travel with a pasted paragraph. EU AI Act Art. 50 disclosure duties bit on **2 Aug 2026**, with provider-side watermarking obligations landing **2 Dec 2026** — again, mostly synthetic media. **[B/C]**
- **OpenAI has no detector and no text watermark in the wild.** Its own AI Text Classifier was withdrawn in July 2023 for low accuracy and has never returned; reporting through 2025–26 says OpenAI built a text watermarking scheme internally but declined to ship it, citing evasion-triviality and user-base harm. Its public position remains that reliable post-hoc text detection is not achievable. **[B]**
- Practical consequence: **all detection you will encounter on social platforms is classifier-based stylometry**, with all the failure modes that implies.

### 1.2 Real accuracy and false-positive rates (independent studies)

The honest summary: **Pangram is a genuine step-change on clean, unmodified LLM output, and near-useless guarantees survive contact with rewriting.**

**University of Chicago Booth — Jabarian & Imas, *Artificial Writing and Automated Detection* (Aug 2025), 3,984 texts across genres [A]**

| Detector | False positive rate | False negative rate |
|---|---|---|
| Pangram | 0.001 | 0.01 |
| Originality.ai | 0.002 | 0.035 |
| GPTZero | 0.007 | 0.06 |
| Open-source RoBERTa detector | ~0.30–0.69 | — |

Short passages degrade everything: FPRs rise to ~1% (Pangram) and ~2.4–3% (GPTZero, Originality.ai) on short text.

**Vrije Universiteit Brussel (June 2026), peer-reviewed, 160+ academic papers [A]** — on fully AI-generated text: Pangram 97.5% detection at 0% FPR; **Turnitin, Copyleaks and GPTZero each detected 0%**. That result is startling enough to warrant caution (it is reported via Pangram's own roundup and likely reflects specific settings/thresholds), but it is a peer-reviewed paper, and it is directionally consistent with the ESL and adversarial literature.

**University of Maryland (2025), humanized text [A/C]** — Pangram 99.3% detection at 2.7% FPR against humanizers; GPTZero 85.3% at 0.7% FPR.

**Vendor counter-claim [C]** — GPTZero's own head-to-head (Oct 2025, updated Apr 2026) reports GPTZero 99.6% accuracy / 0.13% FPR vs Pangram 97.5% / 0.20%, and argues Pangram is weaker on o3, Gemini 2.5 Pro and paraphrase. Vendor benchmarks on self-chosen datasets; note the direct contradiction with Booth.

**The non-native-speaker problem [A]** — Liang et al. (*Patterns*, 2023) found 7 detectors misclassified **61.3%** of non-native TOEFL essays as AI. Pangram claims 0.00% on that exact set and ~0.03% across four ESL corpora **[C, vendor]**. This is the single biggest fairness liability in the field and the reason most universities backed out.

**Adversarial robustness — the important 2026 result [A]**

- **ARB benchmark (arXiv 2607.29539, 31 Jul 2026)**: detectors trained on direct LLM generation collapse on **human-origin text rewritten by an LLM**. Binoculars: 0.935 → **0.151** TPR@1%FPR (a 78-point drop). FastDetectGPT: 0.912 → 0.308. But when *LLM* text is rewritten by an LLM, recall holds at ~78–83%. So: "AI drafts, human-ish source" defeats detectors far more than "AI rewrites AI."
- **"Base Models Look Human To AI Detectors" (arXiv 2605.19516, 19 May 2026)**: text from **base** (non-instruction-tuned) models scores ~96.7% human on GPTZero vs ~30.3% for the instruct version of the *same* model. Their HIP method (Humanization by Iterative Paraphrasing — minimally fine-tune a base model into a paraphraser, run ≤10 rounds) reliably flips commercial detectors. **Detectors are measuring RLHF style, not machine authorship.** This is the most load-bearing finding in this whole section.
- **Adversarial Paraphrasing (arXiv 2506.07001)**: universal humanization attack, generalizes across detectors.

**Institutional retreat [B]** — universities that switched Turnitin's AI detector off: UBC (Apr 2023), Pittsburgh (Jun 2023), Boston University (Jul 2023), **Vanderbilt (Aug 2023 — the canonical case; ~750 of 75,000 papers would be wrongly flagged at a "<1%" FPR)**, Georgetown (Oct 2023), Michigan State, Toronto, Manchester. Turnitin's own claim is <1% document-level, ~4% sentence-level.

### 1.3 The stylometric surface — what actually gets flagged

**Measured, not folklore:**

- **Excess vocabulary (arXiv 2406.07016, 15M PubMed abstracts, 2010–2024) [A]** — 2024's excess words are overwhelmingly *stylistic* (66% verbs, 14% adjectives), unlike prior years' content nouns: **delves (frequency ratio r = 28.0), intricate, meticulously, pivotal, compelling, comprehensive, crucial, potential, notably, underscores, showcasing, realm, garnered, boasts**. 454 excess words in 2024 vs 190 at the 2021 COVID peak. Lower-bound estimate: **≥13.5% of 2024 abstracts LLM-processed** (~200k papers/yr), >40% in some countries/open-access venues.
- **"Why Does ChatGPT 'Delve' So Much?" (COLING 2025, arXiv 2412.11385) [A]** — traces the lexical overrepresentation to RLHF preference data, plausibly to annotator populations (notably Nigerian English usage of "delve"). Useful because it explains *why* the tells exist: they are annotator-preference artifacts, and they will drift as annotation pools drift.
- **Em dash density (aislopscanner, 702,939 words, 31 Jul 2026) [C, but the only quantified figure available]** — em dashes per 100 words: human journalism **0.11**, human essays/forums **0.06**, AI business writing **0.71**, AI casual writing **0.34**. So ~3–6× enrichment. Their own caveat is correct: **register matters more than authorship** — a skilled human business writer sits in the AI band.

**Wikipedia's "Signs of AI writing" (WP:AICATCH / WikiProject AI Cleanup)** is the best crowd-maintained taxonomy in existence, and worth reading in full at `en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing` (note: the domain is fetch-blocked from this environment; summarized here from secondary reproductions **[B]**). Its categories:

1. **Promotional / puffery framing** — "rich cultural heritage," "enduring legacy," "stands as a testament to," "plays a significant role in," "a pivotal moment."
2. **Editorializing tails** — appending a vague significance clause to a factual sentence: "…, improving convenience for residents," "…, highlighting the need for innovation."
3. **The negative parallelism / "not X, but Y"** — correcting a misconception nobody held. Also "It's not just X — it's Y."
4. **Weasel attribution** — "some critics argue," "observers have noted," "industry reports suggest," with no referent.
5. **Formulaic connectives** — moreover, furthermore, additionally, in addition, importantly.
6. **Formatting tells** — em dash overuse; **bolded term + colon + restatement** list items; mechanical boldface on product names; title-case headers everywhere; emoji-bulleted sections.
7. **Rule of three / tricolons** — three-item lists where two or four would be natural.
8. **Structural uniformity** — near-constant sentence length, near-constant paragraph length, every paragraph the same shape.
9. **Fabricated or mismatched citations.**

The page's own caveat is the right one and matters legally and socially: **these signs suggest, they do not prove** — humans write this way too, and the ESL evidence shows the penalty falls hardest on people who learned formal English as a second language.

Additional tells widely cited but *not* rigorously measured: absence of typos and self-correction, generic hedging ("it depends," "there are pros and cons"), "here's the thing," "let's dive in," parallel short punchy sentences ("Big claim. Short sentence. Bigger claim."), zero proper nouns / zero numbers / zero dates, no first-person specificity, and a closing question addressed to the audience.

### 1.4 Do social platforms actually detect, label, or suppress AI text?

This is where the picture changed sharply in 2026. **Yes — for the first time, at scale.**

**Baseline prevalence — Pangram, 1,002,627 posts, 24 Apr – Jun 2026, Pangram 3.3 at 0.01% FPR, >50 words, Chrome-extension opt-in panel [B]:**

| Platform | Longform posts fully AI-generated |
|---|---|
| **LinkedIn** | **41%** |
| X/Twitter | 29% (47% fully-or-partially) |
| Medium | 31% |
| Reddit | 13% longform / 4.4% overall |
| Substack | 10% |

LinkedIn was 35% of the scanned corpus but produced **62% of all AI content**. Replies are far more human than top-level posts (Reddit replies 98.1% human; top-level posts 5.25× likelier to be AI). Originality.ai's separate July 2026 study of 5,000 ≥100-word LinkedIn posts put the figure at **81.2%** at a 15% AI-allowance threshold **[C]** — the gap between 41% and 81% is a threshold/methodology artifact, and a good illustration of why single numbers here are soft.

**LinkedIn — the most aggressive [A/B]**

- **20 May 2026**: VP of Product Laura Lorenzetti announced ML-based detection of "generic AI content." Flagged posts are **not removed — their distribution is suppressed**: they stay visible to direct connections and followers, but the recommendation engine will not amplify them. LinkedIn claims **94% accuracy at identifying generic AI content**; **it has not disclosed a false-positive rate.**
- **31 Jul 2026**: shipped the **"Seems like AI slop"** report button in the post three-dot menu. CPO **Hari Srinivasan**: *"Slop is hard to define and the definition changes; this lets us tune our models and make better feeds."* By **25 Aug 2026, ~1 million users had clicked it.** LinkedIn says it blocks hundreds of thousands of automated spam comments daily and "billions of automation attempts in the last couple of months alone." It also **killed the "Enhance your post" AI rewriter**, replacing it with a proofreader that preserves voice, and tightened profile/page verification.
- Nuance worth keeping: LinkedIn's ranking shift (Hristo Danchev's Mar 2026 engineering post on a unified LLM-powered retrieval/ranking system) means generic content is *also* demoted behaviorally — low dwell time, few saves, shallow comments — independent of any authorship classifier. Both mechanisms point the same way.

**Substack — the most transparent [A]**

- **21 Jul 2026**: launched **"Scan for AI text"** powered by **Pangram**. Reader-initiated, on posts/notes/comments above the length threshold (docs say 100 characters; press reporting says 100 words), in the Substack Reader web app and iOS. Returns a **percentage human-written vs AI-assisted**.
- Writer controls: add a **"How I make this"** statement shown alongside any scan; **disable detection per post/note** (readers then see "AI detection unavailable"); dispute inaccurate scans. Neither Substack nor Pangram trains on publisher content. Not available for video/audio posts, standalone sites, or emailed copies.
- CEO **Chris Best**: *"software should do everything else, but I think you do want the person to do the hard part."*
- The design contrast is the key strategic fact: **Substack tells the reader and lets them decide; LinkedIn tells no one and silently throttles.** Opting out of Substack's scan is itself a visible signal.

**X / Twitter — labels for media, bot-hunting for text [B]**

- "Made with AI" self-labeling toggle for synthetic *media*; unlabeled synthetic content on sensitive topics (armed conflicts) draws 90-day revenue-share suspension, permanent on repeat.
- Head of Product **Nikita Bier** (Feb 2026) announced systems to detect and remove bot profiles at scale: *"People come to X to get a pulse on humanity… There is nothing more unsettling than expecting you're reading the words of a human, only to find it was a machine."* This is **account-level bot detection, not text-level AI classification.**
- Community Notes moved to **AI-written notes** (Grok-generated, human-rated) in 2025–26 — i.e. X is deploying AI *as* the labeling layer, not labeling AI text.
- Meanwhile X actively pushes Grok composition from the "G" icon in the composer. No text-level AI label, no documented reach penalty for AI-written posts.

**Reddit — no sitewide ban, community-level enforcement [A/B]**

- Reddit's policy: generative-AI content is **generally allowed**, subject to each community's rules; sitewide enforcement targets *behavior* (spam, deception, coordinated inauthenticity), not authorship.
- **Cornell Tech**, 300,000+ subreddits sampled Jul 2023 and Nov 2024: **subreddits with explicit AI rules more than doubled in 16 months**; concentrated in art and celebrity communities and in larger subs. Researcher Travis Lloyd's caveat: communities lack the tools to enforce these rules equitably.
- Estimates put ~5–8% of subreddits with explicit AI policies **[C]**. Bans/disclosure requirements: r/writing, r/worldbuilding, r/ChangeMyView (AI arguments violate good-faith rules), r/programming (banned generative content in 2026), r/MachineLearning, r/science. Effectively unregulated: r/SaaS, r/startups, r/Entrepreneur, r/marketing.

**Medium** — banned AI-generated content from the **Partner Program** (paywalled/monetized content) in 2024; enforcement is human + heuristic and widely described as porous. **Threads/Meta** — no text-level AI labeling found; Meta's AI labeling program is media-only (C2PA/IPTC metadata). **YouTube** — moved auto-labels from the collapsed description to directly under the player in **May 2026**, non-removable **[B]**.

**Bottom line for a LinkedIn-focused workflow:** the operative risks in 2026 are, in order: (1) LinkedIn's undisclosed-FPR classifier silently capping your reach at your first-degree network; (2) a reader clicking "seems like AI slop," which both hides the post for them and feeds LinkedIn's training data; (3) reputational damage from a third party running Pangram on your text and screenshotting the result. Nothing removes the post. Nothing labels it publicly. The penalty is invisible.

### 1.5 What makes text read as *human* — to people, not machines

**Humans are bad at this, and the better the model, the worse they get [A]:**

| Study | Population | Detection accuracy |
|---|---|---|
| Teachers vs. student essays (ScienceDirect) | Pre-service teachers | 45.1% (below chance) |
| " | Experienced teachers | **37.8%** (well below chance) |
| All That's 'Human' Is Not Gold (Clark et al.) | Crowdworkers, GPT-2 | 57.9% |
| " | Crowdworkers, **GPT-3** | **49.9% (chance)** |
| GPT-4 Turing test (n=500) | General public | GPT-4 judged human 54% of the time; real humans 67% |
| Can you spot the bot? (IJEI) | 140 instructors / 145 students | 70% / 60% |
| Shoulder & elbow surgery abstracts | Journal reviewers | 62% |
| Plastic surgery residency statements | 2 veteran surgeons | 65.9% |

And the **decoder finding**: readers rate AI-generated short stories *higher* than human ones — until they are told a machine wrote them, at which point ratings collapse. **The penalty is disclosure, not quality.** Which means the thing that makes text read as human to readers is not craft in the abstract; it is the presence of things a machine could not have known.

**What consistently reads as human (synthesized across the above plus the Wikipedia taxonomy):**

- **Specificity that could only be first-hand**: a named person, a real number, a date, a place, a price, a thing that went wrong. Detectors and readers converge here — LLM output is generically true; humans are specifically true.
- **Unevenness**: variable sentence length, one paragraph that runs long because the thought did, a fragment, an aside that doesn't advance the argument.
- **A position with a cost** — an opinion that could lose you something. Generic hedging is the single strongest "AI" signal to a human reader.
- **Register mismatches and idiolect**: your own recurring words, your own dumb metaphors, your own punctuation habits.
- **Retained imperfection**: a typo is a costly signal; so is an unhedged overstatement.
- **No closing engagement-bait question.**

**Do "humanizer" tools work?** Split verdict, and the split is the useful part.

- Against **statistical/zero-shot** detectors and older classifiers: **yes, decisively** — ARB and Adversarial Paraphrasing both show 60–78 point drops.
- Against **Pangram specifically**: **no** — Maryland 2025 measured 99.3% detection on humanized text at 2.7% FPR; Pangram markets a dedicated "Humanizers" classifier that detects the *humanizer's own* stylistic fingerprint. Commercial humanizers (Undetectable AI, StealthGPT, WriteHuman, Phrasly) are locked in a version-race they are structurally losing, because each humanizer is itself a model with a detectable style.
- The one approach that *does* work on commercial detectors is the academic one: **HIP / base-model iterative paraphrasing** (arXiv 2605.19516) — because it removes the RLHF artifact rather than layering a second one on top. Not available as a consumer product.
- Practical reading: **buying a humanizer is a bad bet; writing from real material is not.** The thing that beats Pangram is text whose *source* is human, per ARB's H2L finding — human-origin content that an LLM rewrote is near-undetectable (TPR 0.151), while LLM-origin content stays detectable even after rewriting (TPR 0.83).

**Best practices for writing in a real person's voice (agent-facing):**

1. **Few-shot with their own corpus, not a style description.** Feed 15–40 of the person's actual posts verbatim. Descriptions of voice ("punchy, contrarian, warm") produce the generic register; examples produce the idiolect. Bias sampling toward their *highest-engagement* and *most-recent* posts.
2. **Editing diffs as the real training signal.** Every time the human edits a draft, store `(draft, final)` and derive rules from the delta. The diff is a far higher-information signal than any prompt — it captures what they *remove* (which is usually the AI-isms) as much as what they add. Accumulate these into a **voice profile**: banned words, preferred sentence-length distribution, hook patterns they actually use, topics they refuse, punctuation habits, whether they use em dashes at all.
3. **Ban-list + measured targets, not vibes.** Hard-ban the excess-vocabulary list (delve, leverage, harness, pivotal, intricate, meticulous, underscore, showcase, realm, testament, landscape, navigate, unlock, elevate, robust, seamless, tapestry, ever-evolving). Cap em-dash density at the human band (~0.1/100 words). Enforce sentence-length variance. Ban tricolons, "not X but Y," bolded-term lists, and the closing question.
4. **Source-first drafting.** Start from raw human material — a voice memo, a Slack rant, meeting notes, a real anecdote — and have the model *edit* rather than *generate*. This is exactly the ARB H2L regime that detectors fail on, and it is also the regime that produces text readers rate as human, because it contains things only the person knows.
5. **Human final pass.** Which is Section 2.

---

## Section 2 — Human-in-the-loop rewriting marketplaces and MCPs, 2026

### 2.1 The headline structural change: MTurk is dead, Upwork went agent-native

**Amazon Mechanical Turk shuts down permanently 30 September 2026** (stopped accepting new customers ~5 July 2026; SageMaker Ground Truth goes with it), after 21 years. The stated/reported cause is data-quality collapse — 2023 research found **33–46% of crowdworkers were themselves using LLMs** on text tasks, which destroys the value proposition of buying "human judgment" by the unit. **[B — CNBC, TechCrunch, Quartz, TechRepublic]** *(Note: one secondary source gives 30 July 2026 as the shutdown date; the well-sourced date is 30 July for new-customer cutoff and 30 September for closure.)*

**Upwork shipped an official MCP server on 10 August 2026** — the single most important development for this use case. **[A — Upwork investor press release + product page]**

| | Upwork MCP |
|---|---|
| **Endpoint** | `https://mcp.upwork.com/mcp` |
| **Auth** | OAuth 2.1 with dynamic client registration; browser login; no API keys stored; revocable in Account Settings |
| **Client support** | Claude (Web, Desktop, **Code**), Cursor (App, CLI), Codex (App, CLI), ChatGPT "coming soon", any MCP client |
| **Client-side tools** | search/shortlist talent, post & manage jobs, review proposals, extend offers, create/track milestones, timesheets, payment history |
| **Guardrails** | every write action requires user confirmation; **financial transactions must be finalized on upwork.com** |
| **Cost** | free; standard Upwork fees apply |

CBO **Peter Sanborn**: *"The future of work isn't a choice between humans and AI agents, it's both, working together"* — and notably, that they were already observing AI agents attempting autonomous logins.

The critical caveat for autonomous flows: **Upwork's MCP is agent-assisted, not agent-autonomous.** An agent can find and shortlist an editor and draft the offer, but a human confirms writes and completes payment. For a "hire a human to polish this LinkedIn post, unattended, at 6am" workflow, that human confirmation is the blocker.

### 2.2 Landscape: who an agent can actually hire, programmatically

| Platform | Agent interface | Model | Pricing | Turnaround | Verdict for text editing |
|---|---|---|---|---|---|
| **Upwork** | **Official MCP** (Aug 2026) + REST | Full freelance marketplace, escrow, verified identity | Free MCP; standard Upwork fees; editors typically $25–100/hr | Hours–days (human-paced) | **Best real option.** Huge copyeditor pool. Requires human confirm on writes/payment. |
| **human-mcp.io** | MCP + REST, purpose-built | "First marketplace where AI agents programmatically hire humans." Post task + budget → human accepts → agent approves → escrow releases | **15% platform fee on completed tasks**, no subscription, prepaid wallet, Stripe | Async by design, webhooks for status; hours–days | Explicitly lists **writing, copywriting, proofreading, translation**. Sandbox available. Unknown liquidity — treat scale claims as unverified. **[C]** |
| **Tendem by Toloka** | **MCP server**, one config-file entry, no SDK | 10,000+ verified domain experts across 20+ specialties, exposed as callable endpoints; hybrid AI+human execution; multi-layer QA; async non-blocking | Not published — sales contact | "Most tasks complete within hours" | Strongest **quality** story: internal benchmark of 94 real business tasks — **74.5% "Good" vs 53.2% for human-only freelancers**. Vendor-internal benchmark. **[C]** |
| **RentAHuman** | REST + MCP, 60+ tools | Agents post bounties, browse workers by GPS/rate, review photo proof-of-presence, auto-release Stripe/crypto | Free to join; $9.99/mo verified tier; platform cut of bounty | Variable | Launched 1 Feb 2026 (Alex Liteplo, Patricia Tani). ~590k–787k workers, 4M visits, 11,300 bounties, **but only ~5,500 jobs completed** and ~50 workers per task. Journalists report "radio silence from agents" even at $5/hr; critics call it a "circular AI hype machine" with founder-micromanaged bots; reports of payment errors and crypto scams. **Oriented to physical-world tasks, not copyediting. Do not build on this.** **[B — Built In]** |
| **Prolific** | Research REST API | Identity-verified research participants | **42.8% platform fee (corporate), 33.3% academic**; floor £6/$8 per hour, recommended £9/$12; e.g. 200×15min at $12/hr ≈ **$857** | Hours | Excellent for **A/B testing whether readers perceive a post as AI-written**. Wrong shape for "rewrite this." |
| **CloudResearch Connect** | REST | Verified research participants; lowest-effort MTurk migration | Per-response | Hours | Same use case as Prolific. |
| **Clickworker** | REST | High-volume microtasks | Per-task | Hours | Microtask-shaped; poor fit for voice-sensitive rewriting. |
| **Surge AI** | Enterprise API | Vetted expert pool | **$85–$200+/hour** | Days | Expert RLHF/eval labor. Overkill and over-priced for social posts. |
| **Scale AI / Outlier** | Enterprise contracts | Managed workforce (Outlier merged in) | Custom | Weeks | Enterprise labeling. Not for this. |
| **Fiverr** | **No official MCP.** Only community/unofficial servers (KyuRish/fiverr-mcp-server, realitechteam/fiverr-mcp — explicitly "educational/research"), plus viasocket's Fiverr Workspace MCP | — | Gig-priced; LinkedIn post editing gigs commonly $10–50 | 1–3 days | Scraping/unofficial. ToS risk. |
| **Contra** | No MCP found; commission-free freelance marketplace with a public API | — | 0% commission | Days | Worth a manual check; nothing agent-native surfaced. |
| **Rev.com** | **Official REST API** (`rev.com/api`) — but human **transcription and captions only** | — | ~$1.99/min human transcription | Hours | No human *copyediting* API. Not applicable. |

### 2.3 The other pattern: approval/elicitation, not hiring

For most real workflows the requirement is not "hire a stranger" but "get *my* human to approve/edit before publish." That is a solved, cheap problem:

**MCP-native (open source, free):**
- **MCP Elicitation** — since the 2025-06-18 MCP spec revision, servers can request structured input from the user mid-tool-call. This is the standards-track answer, and the right primitive to build on.
- `GongRzhe/Human-In-the-Loop-MCP-Server` — native GUI dialogs (text input, multiple choice, confirmation, feedback) on Windows/macOS/Linux. `pip install human-in-the-loop-mcp`.
- `KOBA789/human-in-the-loop` — asks questions via **Discord**.
- `ifmelate/clarify-mcp`, `LIghtJUNction/human-mcp`, AskMeMCP, feedback-loop-mcp — variations.
- FlowHunt ships a hosted Human-in-the-Loop MCP integration.

**Workflow platforms with a *real* approval step (verified against vendor docs) [B]:**

| Tool | Mechanism | External approvers (no account)? | Cost |
|---|---|---|---|
| **n8n** | "Send and Wait for Response" across 9+ channels (Slack, Gmail, Outlook, Teams, Discord…), plus webhooks/forms | **Yes** | Free self-hosted |
| **Pipedream** | Prebuilt approvals for Slack/Gmail/Outlook, 24h default timeout | **Yes** (resume/cancel URLs) | Free tier |
| **Activepieces** | Legacy approval links | **Yes** | Free, MIT |
| **Zapier** | "Request Approval" + "Collect Data" actions; Slack approval integration | **No** — reviewers need Zapier accounts | **Professional+ plans only** |
| **Power Automate** | Rich multi-approver | Only licensed Entra B2B guests | Included with M365 business |
| **Make** | Approval app in **closed beta**, Enterprise only | — | — |
| **Gumloop** | Agent-level approval only | No | — |

**Payment rails for agent→human:**
- **Payman AI** — purpose-built: per-agent wallets with programmable policy (transaction limits, approval thresholds, recipient whitelists). REST API + Python/TypeScript/JS SDKs, webhooks, sandbox, **MCP server**, and prebuilt LangChain / CrewAI / AutoGen integrations. Free sandbox; production is Stripe-style per-transaction (% + flat); no monthly platform fee. Raised $3M pre-seed. As of Aug 2026 described as actively maintained but **very early-stage in a market that "barely exists yet."** **[C]**
- **Nevermined** — x402-based agentic payments; launched **AI agent card payments via x402** in 2026, plus an x402 facilitator. Oriented to agent→API/agent→merchant billing rather than agent→human labor. **[C]**

### 2.4 "Human editing as a service" specifically for LinkedIn ghostwriting

No agent-callable API exists for this niche. The market is entirely human-brokered:

| Tier | Monthly | Volume | What you get |
|---|---|---|---|
| Budget | **$500–$1,500** | 8–12 posts | Newer freelancers or AI-assisted services; template-driven, thin strategy |
| Mid | **$2,000–$4,000** | 12–16 posts | Experienced writers/small agencies; voice matching, topic strategy, engagement optimization |
| Premium | **$5,000–$10,000+** | 16–20+ posts | Established agencies; full strategy, done-for-you engagement, analytics |
| **Per post** | **$50–$500** | — | Most professionals prefer retainers |

Typical founder spend: $2,000–$5,000/mo. **[C — aggregated from Windmill Growth, Foundera, Mylance; these are SEO-marketing sources and should be read as order-of-magnitude.]**

**The realistic architecture for an agent-driven "human polish" step on LinkedIn posts, in priority order:**

1. **Own-human approval loop** via MCP elicitation or an n8n/Pipedream Slack approval — near-zero cost, sub-minute latency, and it doubles as the **editing-diff capture mechanism** from §1.5. This is where almost all the value is.
2. **A retained human editor** reachable through the same Slack/n8n approval channel — $50–500/post, hours of latency, and they know the voice.
3. **Upwork MCP** for on-demand sourcing when the retained editor is unavailable — agent-assisted sourcing, human-confirmed hire.
4. **Prolific/CloudResearch** for periodic *measurement* — does a panel of 100 readers perceive these posts as AI-written? — rather than for editing.
5. **human-mcp.io / Tendem** as the genuinely agent-native options if you want unattended operation, accepting unverified liquidity (human-mcp) or opaque pricing (Tendem).

---

## Section 3 — Claude Code / Cowork plugin & skill mechanics, 2026

### 3.1 Plugin anatomy

A plugin is a directory. Only `plugin.json` lives inside `.claude-plugin/`; **everything else sits at the plugin root** (this is the single most common authoring mistake, and the docs call it out explicitly).

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json          # manifest — ONLY this goes in here
├── skills/<name>/SKILL.md   # skills (preferred layout)
├── commands/*.md            # legacy flat-file skills; use skills/ for new work
├── agents/                  # subagent definitions
├── hooks/hooks.json         # event handlers
├── .mcp.json                # bundled MCP servers
├── .lsp.json                # LSP servers
├── monitors/monitors.json   # background monitors
├── bin/                     # executables added to Bash PATH while enabled
├── settings.json            # defaults: only `agent` and `subagentStatusLine`
└── README.md
```

`plugin.json`: `name` (required — also the skill namespace), `description`, `version` (optional; users only get updates when you bump it, except for `command` sources), `author`, plus `homepage`, `repository`, `license`.

Key mechanics:

- **Namespacing**: plugin skills invoke as `/plugin-name:skill-name`. A plugin shipping exactly one skill may put `SKILL.md` at the plugin root and use the frontmatter `name`.
- **Bundled MCP servers**: drop `.mcp.json` at plugin root. Their tools are namespaced `mcp__plugin_<plugin_name>_<server_name>__<tool_name>`; the server registers as `plugin:<plugin>:<server>`. Use those full names in permission rules, skill `allowed-tools`, subagent `tools`, and hook matchers.
- **Monitors** (`monitors/monitors.json`): each entry is `{name, command, description}`; every stdout line from `command` is delivered to Claude as a notification. Started automatically when the plugin is active.
- **Dev loop**: `claude --plugin-dir ./my-plugin` (accepts `.zip`, repeatable, local copy shadows an installed same-name plugin); `claude --plugin-url https://…/plugin.zip` for hosted archives; `/reload-plugins` to hot-reload skills/agents/hooks/MCP/LSP; `claude plugin validate ./my-plugin` (`--strict` to fail on warnings).
- **Skills-directory plugins**: `claude plugin init my-tool` scaffolds `~/.claude/skills/my-tool/` with a manifest + starter SKILL.md; it auto-loads next session as `my-tool@skills-dir` — **no marketplace, no install step**. This is the fastest path for a personal skill you may later publish.

### 3.2 Marketplaces

`.claude-plugin/marketplace.json` at repo root:

```json
{
  "name": "my-plugins",
  "owner": { "name": "You", "email": "you@example.com" },
  "plugins": [
    { "name": "linkedin-voice", "source": "./plugins/linkedin-voice",
      "description": "…", "version": "1.0.0", "category": "productivity",
      "tags": ["writing","linkedin"] }
  ]
}
```

Source types: relative path · `github` (`{source:"github", repo:"owner/repo", ref, sha}`) · `url` (any git host) · `git-subdir` (monorepos) · `npm` · `archive` (zip, v2.1.224+) · `command` (local tool output, v2.1.229+). `strict:false` makes the marketplace entry the complete definition. A `renames` map handles renames (`"old":"new"`) and removals (`"old": null`).

Commands:
```
/plugin marketplace add owner/repo         # or a git URL, marketplace.json URL, or local dir
/plugin install my-plugin@marketplace-name
/plugin validate .
```

**Anthropic's two public marketplaces:**
- `claude-plugins-official` — curated by Anthropic, auto-registered on first interactive launch. No application process; Anthropic picks.
- `claude-community` — `/plugin marketplace add anthropics/claude-plugins-community`, install as `@claude-community`. **Open submission** via in-app forms: claude.ai/admin-settings/directory/submissions/plugins/new (needs Team/Enterprise + directory management) or platform.claude.com/plugins/submit (individual authors). Review runs `claude plugin validate` plus automated safety screening; approved plugins are **pinned to a commit SHA** in the catalog with CI bumping the pin as you push; the public catalog **syncs nightly**.

Private/team distribution: host `marketplace.json` in a private repo; `gh auth setup-git` or a git URL rewrite with a token for background auto-updates. Container pre-seeding via `CLAUDE_CODE_PLUGIN_CACHE_DIR` at build and `CLAUDE_CODE_PLUGIN_SEED_DIR` at runtime.

### 3.3 Skills

**Frontmatter** — only two fields required:

```yaml
---
name: linkedin-voice          # ≤64 chars, lowercase/digits/hyphens, no XML tags,
                              # must not contain "anthropic" or "claude"
description: >                # non-empty, ≤1024 chars, no XML tags.
  What it does AND when to use it.
---
```
Claude Code additionally honors `disable-model-invocation: true` (slash-only), `allowed-tools`, and `$ARGUMENTS` in the body.

**Progressive disclosure — three levels:**

| Level | When loaded | Cost | Content |
|---|---|---|---|
| 1 — Metadata | Startup, every skill | ~100 tokens each | `name` + `description` only |
| 2 — Instructions | On trigger | <5k tokens | SKILL.md body |
| 3 — Resources & code | On reference | 0 until read | `references/*.md`, `scripts/*` (run via bash — **only stdout enters context**), `assets/` |

```
skill-name/
├── SKILL.md
├── REFERENCE.md
├── scripts/          # code never enters context, only its output
└── resources/
```

**Where skills live:** `~/.claude/skills/` (personal) · `.claude/skills/` (project) · inside plugins · uploaded as zips on claude.ai (Settings → Features, individual user only, paid plans) · via `/v1/skills` on the API (workspace-wide). **Custom skills do not sync across surfaces** — Claude Code, claude.ai and the API are three separate stores. Network access: full in Claude Code, **none** on the API, variable on claude.ai.

### 3.4 Scheduled execution

Three distinct systems — do not conflate them:

**Claude Code Routines** — research preview, **14 April 2026** **[A]**
- Run on Claude Code's **web infrastructure**; your machine can be off.
- Three triggers: **scheduled** (cron-like cadence, managed via `/schedule` in the CLI), **API** (each routine gets its own endpoint + auth token; HTTP POST returns a session URL), **webhook** (GitHub repo events — one session per PR, with PR updates fed into that session).
- Limits: Pro **5/day**, Max **15/day**, Team/Enterprise **25/day**; overflow bills usage credits.

**Cowork scheduled tasks** **[A]**
- Sidebar → **Scheduled**. Configure name, prompt, approval mode, frequency: **hourly, daily, weekly, weekdays, or manual**.
- Each run is **its own Cowork session**; results appear on the Scheduled tasks page.
- Paid plans (Pro/Max/Team/Enterprise). Runs remotely, works with your connected tools, skills and installed plugins.
- **Hard limit: a scheduled task cannot be tied to a folder on your computer.** If it needs local files or apps, it only runs locally.

**Claude Code Remote triggers** (the environment this report was produced in) — `create_trigger` / `update_trigger` / `delete_trigger` / `fire_trigger` / `list_triggers`, plus `send_later` for a one-shot message back into the same session. 5-field cron, **evaluated in UTC** (convert local times, and shift day fields if the conversion crosses midnight); minimum interval normally hourly; hourly schedules at minute 0 are anchored to the creation minute so tasks spread across the hour. `requires_local_device: true` binds a trigger to the user's machine — **and that binding can never be added after creation**, so declare it up front if runs will ever touch local files. Prompt changes on a device-bound trigger require re-approval **on that device**; schedule/name/enabled changes go through freely, so send them in a separate call without a prompt.

### 3.5 How a skill discovers which MCP servers a user has connected

There is **no first-class "list my connected MCP servers" tool** exposed to skills. Four practical routes, best to worst:

1. **`claude mcp list` via Bash** — the canonical answer in Claude Code. Returns each server with a status glyph: `✔ Connected`, `! Needs authentication`, `✘ Failed to connect`, `⏸ Pending approval`, `⊘ Disabled for this project`. `claude mcp get <name>` gives detail including **tool count**, auth status, and cached-vs-live state (v2.1.221+). This is the right primitive for a skill that must adapt to whatever the user has.
2. **Read the config files** — `.mcp.json` at project root (project scope, version-controlled, supports `${VAR:-default}` expansion), `~/.claude.json` (local scope per-project *and* user scope). Precedence, highest first: **local → project → user → plugin-provided → claude.ai connectors**.
3. **Inspect the tool namespace** — every MCP tool is `mcp__<server>__<tool>`; plugin-bundled ones are `mcp__plugin_<plugin>_<server>__<tool>`. A skill can pattern-match available tool names to infer capability ("is there anything matching `mcp__.*__.*slack.*send`?"). In this session's harness, deferred tools surface by name in system reminders and are loaded with `ToolSearch("select:...")` — a skill can search the registry by keyword rather than by exact server name.
4. **Agent SDK** — `setMcpServers()` / the `mcpServers` client config, for programmatic control.

**Generic-use pattern for a portable skill:** declare the *capability* you need, not the server. Probe with `claude mcp list`, map to whichever server satisfies it (e.g. any of Slack / Discord / Gmail for "notify a human"; any of Notion / Google Drive / filesystem for "store the voice profile"), degrade gracefully with a named fallback, and tell the user exactly which server you chose and why. Also note the runtime affordances: MCP `list_changed` notifications refresh tools mid-session, failed remote servers retry with exponential backoff, calls over 2 minutes auto-background, and tool search is the default scaling mechanism when many tools are present.

### 3.6 How skills persist memory and state

Four mechanisms, with genuinely different semantics **[A]**:

| Mechanism | Written by | Scope | Loaded |
|---|---|---|---|
| **CLAUDE.md** | You | Managed policy → user (`~/.claude/CLAUDE.md`) → project (`./CLAUDE.md` or `./.claude/CLAUDE.md`) → local (`./CLAUDE.local.md`) | Every session, concatenated root-down (nearest file read last) |
| **`.claude/rules/*.md`** | You | Project or `~/.claude/rules/` | Every session, or **on demand** when `paths:` frontmatter globs match a file Claude reads |
| **Auto memory** | **Claude** | Per git repository, shared across worktrees | `MEMORY.md` index only — first **200 lines or 25KB**; topic files read on demand |
| **Skill `scripts/` + data files** | Skill code | Wherever you write them | Never automatically — the skill must read them |

Auto-memory specifics that matter for building a voice-profile skill:

- Storage: `~/.claude/projects/<project>/memory/`, containing `MEMORY.md` (the index) plus one topic file per memory. Relocatable via `autoMemoryDirectory` in `settings.json` (absolute or `~/`-prefixed).
- Claude tags each memory with a `type` in frontmatter: `user` (role, expertise, working preferences), `feedback` (**corrections you gave and approaches you confirmed** — this is exactly the editing-diff signal from §1.5), `project`, `reference`. It deliberately skips anything derivable from the codebase or already stated in CLAUDE.md.
- Files that begin with YAML frontmatter get a `modified` ISO-8601 timestamp written on each save (v2.1.214+).
- Auto memory is **machine-local** — not synced across machines or to cloud environments. It is also **excluded from the `cleanupPeriodDays` retention sweep**, so it survives transcript deletion.
- Toggle: `/memory`, or `autoMemoryEnabled` in settings, or `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`. Subagents can have their own separate memory directory (`memory` field); the main conversation's memory is **not** inherited by subagents except in a fork.
- Size discipline: CLAUDE.md target **<200 lines** (hard skip above 4 MiB); if `MEMORY.md` exceeds its read limit the write succeeds but Claude Code returns an error telling Claude to rewrite the index, because overflow is dropped at next load.

Also: `AGENTS.md` is **not** read by Claude Code — bridge it with `@AGENTS.md` at the top of CLAUDE.md, or symlink. `/import` (v2.1.213+) pulls another agent's config — instruction files, MCP servers, commands, subagents, skills — into Claude Code.

**Design implication for a voice-writing skill:** put the durable, small stuff (banned words, tone rules) in `~/.claude/rules/` or a plugin skill; let **auto memory** accumulate the `feedback`-type learnings from edits; keep the large corpus (the person's 40 past posts, the diff history) in Level-3 skill `references/` or an external store that scripts read on demand — never in CLAUDE.md, which is loaded in full every session.

### 3.7 The official skills repo, skill-creator, and evals

**`anthropics/skills`** — "Public repository for Agent Skills." Layout: `./skills` (examples across Creative & Design, Development & Technical, Enterprise & Communication, Document Skills), **`./spec`** (the Agent Skills specification), `./template`, `.claude-plugin`. Licensing is split: most skills **Apache 2.0**; the production document skills (`docx`, `pdf`, `pptx`, `xlsx`) are **source-available, not open source**. Install:
```
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```
Reported metrics (~169k stars, ~20.1k forks, 771 PRs) are implausibly large for this repo and are likely a scraping artifact of the fetch — **do not cite the star count**; the rest of the structure is verifiable.

**skill-creator** — lives at `anthropics/claude-plugins-official/plugins/skill-creator/`. On **3 March 2026** Anthropic shipped a major upgrade **[A]**:

1. **Evals** — skill-creator helps you write tests asserting Claude does what you expect for given prompts. Catches regressions when models update, and reveals when base-model improvement has made a skill redundant.
2. **Benchmarking** — standardized mode tracking eval pass rate, wall-clock time, and token consumption.
3. **A/B testing with comparator agents** — independent agents compare two skill versions **blind** (they don't know which is which), removing bias about whether a change actually helped.
4. **Description optimization** — analyzes the `description` against sample prompts and proposes refinements to cut both false triggers and missed triggers. Given that Level-1 metadata is the *only* thing loaded at startup, this is the highest-leverage knob in the whole system.

Available on Claude.ai and Cowork, as a Claude Code plugin, and from the official repo.

### 3.8 The Agent Skills open standard — adoption, verified and unverified

Anthropic opened the SKILL.md format as the **Agent Skills standard on 18 December 2025**, spec at **agentskills.io/specification** **[B]**.

**Adoption (as reported, ~32–40 products by mid-2026):** Anthropic (Claude Code, Cowork, claude.ai, API) · **OpenAI** (Codex CLI, ChatGPT — experimental support was merged *before* the public announcement; users found a `/home/oai/skills` folder by 12 Dec 2025) · **Microsoft** (VS Code, GitHub Copilot — shipped within 48 hours) · Google (Gemini CLI) · JetBrains (Junie) · AWS (Kiro IDE, 5 Feb 2026) · Block (Goose) · Sourcegraph (Amp) · Snowflake · Databricks · ByteDance (TRAE) · Mistral AI · Spring AI. Vercel launched the **skills.sh** marketplace on 20 Jan 2026.

**Verification status — be careful here.** OpenAI Codex CLI adoption is well-corroborated (and independently confirmed by the `linkedin-skills` repo shipping a working `codex plugin marketplace add` install path, and by `npx skills add` as a generic installer). **Cursor's adoption is asserted in secondary write-ups without a primary link, and no source I found documents OpenClaw as an adopter of the Anthropic standard** — though ClawHub's skill format is essentially convergent (see below). Treat the "32 tools" number as a marketing tally, not a verified registry.

**Ecosystem scale and quality (June 2026) [C — Agentman, a vendor with an interest in curation]:**

| Registry | Scale | Review |
|---|---|---|
| Anthropic official directory | Small, curated; verified partners (Stripe, Figma, Notion) | Manual |
| `claude-community` | Open submission | Validate + automated safety screening, SHA-pinned |
| **skills.sh** (Vercel) | "Hundreds of thousands," npm-style install | Open |
| **SkillsMP** | ~1.9M scraped from GitHub | **None** |
| SkillHub | 7,000+ | AI scoring |
| Agensi | Small curated | 8-point security scan |

Category distribution: Development & Engineering 288,811 · Product Management 86,948 · Marketing 74,510 · Healthcare 6,354. The two numbers that matter: **curated skills raised task pass rates by an average of 16.2 percentage points**, while **the average public skill scores 6.2/12**, and a security audit found **36% of tested skills vulnerable to prompt injection**.

### 3.9 OpenClaw and ClawHub

**Lineage**: Clawdbot → Moltbot → **OpenClaw**, the open-source agent orchestration layer; ~250k GitHub stars; covered by Forbes on 6 Feb 2026. Positioned for self-hosted operation (Mac Mini clusters, Docker), local data sovereignty, no third-party telemetry. Security is a live issue — the project cites mitigation of **CVE-2026-25253** and blocking of the **"ClawHavoc"** infostealer campaign via hardened Docker sandboxes. **[B/C]**

**ClawHub** (`github.com/openclaw/clawhub`, docs at `docs.openclaw.ai/clawhub`) is the **skill + plugin registry** **[A — official docs]**:

- **Format**: a skill is a folder whose manifest is **`SKILL.md`** (or `skill.md`) with YAML frontmatter — i.e. convergent with the Agent Skills standard. `description` becomes the search/UI summary. `.clawhubignore` / `.gitignore` control what publishes.
- **Runtime declaration** — the OpenClaw-specific extension, under `metadata.openclaw` (alias `metadata.clawdbot`): `requires.env` (required env vars), `requires.bins` (required CLI tools), `requires.anyBins` (at least one of), `primaryEnv` (main credential), and optional `envVars` with `required: false`. **Static analysis verifies the declared metadata matches actual code usage** — undeclared credential access fails review.
- **Constraints**: 50MB bundle cap; lowercase-hyphen names matching the parent directory; **all published skills are MIT-0 by default**; **ClawHub does not support paid skills, per-skill pricing, paywalls, or revenue sharing.**
- **Publishing**: authenticated `clawhub` CLI with a dry-run preview; each release creates an **immutable version record** with changelog tags.
- **Install**: `openclaw skills install @openclaw/demo`; `openclaw plugins install clawhub:<package>`. Install source metadata is recorded so updates come from the same registry package.
- **Moderation**: open to publishing, but subject to upload gates, automated scans, user reports and moderator action. Public pages show scan summaries; content can be held, hidden, or search-suppressed while staying visible to the owner for diagnostics.
- **Signals**: download, install and star counts per listing. **Public read APIs** for discovery, search, package details and downloads — third-party catalogs may mirror if they link back to canonical listings and respect rate limits.

### 3.10 Existing social-media / LinkedIn / X skills

**Claude ecosystem — the standout is `sergebulaev/linkedin-skills` [A — GitHub]**

MIT, **582 stars / 91 forks**, "Content engineering by Creative Content Crafts." **11 skills**, and notably it already implements much of Section 1:

| Skill | Function |
|---|---|
| Post Writer | 20 hook formulas, founder-specific angles |
| **Post Audit** | Checks drafts against **2026 algorithm rules and AI-detection patterns** |
| **Humanizer** | *"Strips em dashes, AI vocabulary ('leverage', 'delve', 'harness'), rule-of-three lists."* Sub-tools: **AI-emoji density scorer** and a **multi-detector spread tester (GPTZero, Originality.ai, ZeroGPT, Sapling, Copyleaks)** |
| Comment Drafter | Comments from a post URL |
| Reply Handler | Handles LinkedIn's thread flattening |
| Hook Extractor | Reverse-engineers hooks from viral posts |
| Content Planner | 7-day plans with topics and timing |
| Engagement Monitor | Tracks replies, scores engagers by ICP fit |
| Profile Optimizer | Headline/section rewrites |
| Employee Advocacy | Team programs, cadence, governance |
| Repurposer | Cross-platform → native LinkedIn |

Cross-runtime install paths, which is itself the best evidence of the open standard working in practice:
```
claude:   /plugin install linkedin-skills@linkedin-skills
codex:    codex plugin marketplace add sergebulaev/linkedin-skills
generic:  npx skills add sergebulaev/linkedin-skills
claude.ai: Skills → Add from GitHub
```
Its voice rules across all 11 skills prohibit em dashes, AI vocabulary, and vague adjectives in favor of specificity — i.e. it encodes the Wikipedia taxonomy. **Notably absent: Pangram** from its detector spread — a real gap given Pangram is what Substack runs and what the independent literature ranks first.

Others in the Claude ecosystem: `linkedin-post-writer` and `social-media-post-writer` on mcpmarket.com; `linkedin-skills` mirrored on mdskills.ai and skillsllm.com. Nothing with comparable depth.

**OpenClaw / ClawHub** — via `VoltAgent/awesome-openclaw-skills` (52.3k stars on the aggregator repo; **no per-skill star counts published**), the marketing-and-sales category lists **108 skills**, of which the relevant ones are:

- **`linkedin-post-writer`** — viral hooks, comment strategies, algorithm optimization (the only LinkedIn-specific skill)
- **`bird`** — X/Twitter CLI: read, search, post
- **`postiz`** — schedule posts/threads across **28+ platforms**
- **`postnitro`** — branded carousels and single posts for LinkedIn, Instagram, TikTok, Threads
- **`simplified-social-media`**, **`posteahora`** — cross-channel posting, scheduling, analytics
- `kit-email-operator`, `brevo`, `cold-email`, `tiktok-viral-marketing`, `tiktok-trend-challenger`

Third-party OpenClaw posting integrations: **Upload-Post**, **AdaptlyPost**. **No OpenClaw skill found that addresses AI-detection avoidance or voice matching** — that is an open niche on ClawHub, and ClawHub's MIT-0 default plus no-paywall policy means anything published there is unmonetizable but maximally distributable.

### 3.11 How a community could accept contributions to a shared skill

**Distribution/review models available today:**

| Model | Mechanism | Review | Trade-off |
|---|---|---|---|
| GitHub PRs to a repo used directly as a marketplace | `/plugin marketplace add owner/repo` | Whatever your CI + maintainers do | Simplest; full control; you own moderation |
| Submit to `claude-community` | In-app form → `claude plugin validate` + automated safety screening → **SHA-pinned** in catalog, CI bumps the pin, catalog **syncs nightly** | Anthropic | Reach + trust; nightly lag between approval and installability |
| ClawHub | `clawhub` CLI publish, immutable versions | Upload gates, automated scans, user reports, moderators; static analysis of declared `requires.env` vs actual usage | MIT-0 only; no monetization |
| Private/team | Marketplace in a private repo (`gh auth setup-git`) | Yours | Internal governance, audit trails |

**Telemetry — read the Vercel case before designing any.** In April 2026 the Vercel Claude Code plugin registered three hooks: `SessionStart` (device ID, OS, detected frameworks, CLI version), `PostToolUse` on Bash (**full bash command strings**, including file paths and infrastructure details, sent to telemetry.vercel.com against a persistent device UUID, **always on regardless of consent**), and `UserPromptSubmit` (**full prompt text**, if consented). Worse, consent was solicited by **injecting instructions into Claude's context telling it to ask the question with `AskUserQuestion`** and then shell out to record the answer — visually indistinguishable from a native Claude prompt, with no plugin attribution. And it fired on **all projects**, not just Vercel ones; framework detection existed but only reported, never gated. Resolution: **PR #47 on 14 April 2026 deleted 24,677 lines** and addressed all four concerns. **[B]**

**Contribution + telemetry pattern that would survive scrutiny, for a voice-writing skill:**

1. **Default off. Explicit, native, per-project opt-in.** Never solicit consent by instructing the model to impersonate a native prompt. Store the decision in a file the user can read and revert.
2. **Never transmit content.** For a voice skill, the tempting payload — draft/final pairs — is the user's private writing plus their client's identity. Ship **derived statistics only**: which rule fired, whether the human accepted or reverted it, sentence-length variance before/after, em-dash delta. Never the text.
3. **Anonymize properly**: no persistent device UUID, rotating salt per submission, k-anonymity floor (drop any rule-firing bucket with fewer than N contributors), and strip anything free-text.
4. **Scope the hook.** Fire only when the skill is actually invoked, never on `SessionStart` or on every Bash call, and never in unrelated projects.
5. **Contribution loop**: the highest-value community artifact here is a **shared, versioned ban-list and rule-set** — `references/ai-isms.md`, `references/hooks.md` — accepting PRs with a required **eval** per rule. skill-creator's blind comparator A/B is the natural acceptance gate: a PR is merged if the comparator prefers the new version on the held-out prompt set. That turns "does this rule make writing sound more human?" from an argument into a measurement.
6. **Publish the eval suite alongside the skill** so contributors can reproduce the benchmark (pass rate, time, tokens) before opening a PR — and so the skill can be re-benchmarked after every model update, which is exactly the regression skill-creator's evals were built to catch.

---

## Cross-cutting synthesis (three things worth acting on)

1. **The detection arms race has an asymmetry you can exploit legitimately.** ARB shows detectors collapse on **human-origin text rewritten by an LLM** (TPR 0.151) but hold on **LLM-origin text rewritten by an LLM** (TPR 0.83). This is not a loophole — it is the same fact as "readers want things only you know." A pipeline that starts from the person's raw material (voice memo, Slack message, meeting note) and uses the model to *edit* is simultaneously the most detector-resistant, the most reader-authentic, and the most defensible. A pipeline that generates from a topic prompt and then runs a humanizer is the opposite on all three.

2. **The binding constraint on LinkedIn in 2026 is an undisclosed-FPR classifier, not a label.** LinkedIn suppresses distribution without telling anyone, claims 94% accuracy, and has published no false-positive rate — while a million users have now hand-labeled "AI slop" for its training set. Substack, by contrast, discloses and lets writers add a "How I make this" statement. The defensive posture differs by platform: on Substack, disclose and own it; on LinkedIn, there is nothing to disclose to and the only lever is not tripping the classifier.

3. **The human-in-the-loop step is cheap and the marketplace step mostly isn't.** MCP elicitation plus an n8n/Pipedream Slack approval costs nothing, adds seconds, and generates the editing-diff corpus that is the single best voice-training signal available. Upwork's MCP (Aug 2026) is the only marketplace with a real, official, OAuth'd agent interface, and it deliberately keeps a human on writes and payments. Everything genuinely autonomous — human-mcp.io, Tendem, RentAHuman — is either unverified in liquidity, opaque in pricing, or pointed at the wrong kind of work.

---

## Sources

**Section 1 — detection, stylometry, platforms**
- [Pangram — Third-Party Evaluations](https://www.pangram.com/blog/third-party-pangram-evals)
- [Pangram — AI Content Is Everywhere on Social Media, Especially LinkedIn](https://www.pangram.com/blog/ai-in-your-feed)
- [Pangram — All About False Positives in AI Detectors](https://www.pangram.com/blog/all-about-false-positives-in-ai-detectors)
- [Pangram technical report (arXiv 2402.14873)](https://arxiv.org/html/2402.14873v3)
- [GradPilot — AI Detector False Positive Rates Compared (2026)](https://gradpilot.com/news/ai-detector-false-positive-rates-compared)
- [GradPilot — Colleges That Disabled AI Detectors tracker](https://gradpilot.com/news/colleges-that-disabled-ai-detectors)
- [GPTZero vs. Pangram benchmark (vendor)](https://gptzero.me/news/gptzero-vs-pangram/)
- [ARB: Matched Authorship-Rewriting Benchmark (arXiv 2607.29539, Jul 2026)](https://arxiv.org/html/2607.29539v1)
- [Base Models Look Human To AI Detectors (arXiv 2605.19516, May 2026)](https://arxiv.org/html/2605.19516v1)
- [Adversarial Paraphrasing (arXiv 2506.07001)](https://arxiv.org/abs/2506.07001)
- [DAMAGE: Detecting Adversarially Modified AI Generated Text (arXiv 2501.03437)](https://ar5iv.labs.arxiv.org/html/2501.03437)
- [Delving into LLM-assisted writing in biomedical publications: excess vocabulary (arXiv 2406.07016)](https://arxiv.org/html/2406.07016v5)
- [Why Does ChatGPT "Delve" So Much? (COLING 2025 / arXiv 2412.11385)](https://aclanthology.org/2025.coling-main.426/)
- [Word Overuse and Alignment in LLMs (arXiv 2508.01930)](https://arxiv.org/pdf/2508.01930)
- [Em dash density measured across human vs AI corpora](https://aislopscanner.com/blog/em-dash-ai-tell-data/)
- [Rolling Stone — 'ChatGPT Hyphen': Are Em Dashes a Giveaway of AI Writing?](https://www.rollingstone.com/culture/culture-features/chatgpt-hypen-em-dash-ai-writing-1235314945/)
- [Wikipedia:WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup) · [Guide and resources](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup/Guide_and_resources) · [Talk:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia_talk:Signs_of_AI_writing) · [secondary summary](https://smartinbound.com/wikipedia-signs-of-ai-writing/) · [MakeUseOf coverage](https://www.makeuseof.com/wikipedia-best-ai-writing-detection-guide/)
- [Originality.ai — Can Humans Detect AI-Generated Text? 6 Studies](https://originality.ai/blog/can-humans-detect-ai-content)
- [Originality.ai — LinkedIn AI Content Study: 81% of long-form posts](https://originality.ai/blog/ai-content-published-linkedin)
- [Do humans identify AI-generated text better than machines? (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S1477388025000131)
- [The Decoder — Readers rate AI short stories higher until told a machine wrote them](https://the-decoder.com/readers-rate-ai-generated-short-stories-higher-than-human-ones-until-they-learn-a-machine-wrote-them/)
- [Fortune — LinkedIn adds 'seems like AI slop' button (31 Jul 2026)](https://fortune.com/2026/07/31/linkedin-seems-like-ai-slop-button-billions-automated-comments-attempts/)
- [Fortune — 1 million LinkedIn users clicked its 'seems like AI' button (25 Aug 2026)](https://fortune.com/2026/08/25/1-million-people-clicked-linkedin-ai-slop/)
- [Neil Patel — LinkedIn Is Suppressing AI Slop (Lorenzetti, 20 May 2026; 94% claim)](https://neilpatel.com/blog/linkedin-ai-slop-crackdown-content-strategy/)
- [Zoomsphere — LinkedIn algorithm 2026: generic AI content and organic reach](https://www.zoomsphere.com/blog/linkedin-algorithm-2026-why-generic-ai-content-kills-your-organic-reach)
- [How LinkedIn and Substack detect AI content in 2026 (Goodman)](https://melaniegoodmanlinkedinconsultant.substack.com/p/linkedin-substack-ai-detection)
- [TechCrunch — Substack's new tool tells you who's writing with AI (22 Jul 2026)](https://techcrunch.com/2026/07/22/substacks-new-tool-tells-you-whos-been-writing-their-newsletters-with-ai/)
- [Substack Help — How can I detect AI on Substack?](https://support.substack.com/hc/en-us/articles/50891130623508-How-can-I-detect-AI-on-Substack)
- [Inc. — YouTube, LinkedIn and Substack are flagging AI content](https://www.inc.com/amy-zwagerman/youtube-linkedin-and-substack-are-flagging-ai-generated-content-brands-need-a-public-policy/91389773)
- [Social Media Today — X moves to stamp out AI bots while promoting Grok (Feb 2026)](https://www.socialmediatoday.com/news/x-formerly-twitter-moves-to-stamp-out-ai-bots-while-promoting-grok/812910/)
- [Gizmodo — X is turning Community Notes over to AI](https://gizmodo.com/elon-musks-x-is-turning-community-notes-over-to-ai-2000623401)
- [Cornell — Dataset reveals how Reddit communities are adapting to AI](https://news.cornell.edu/node/330648)
- [MediaFast — Is AI-generated content allowed on Reddit? (2026 rules)](https://www.mediafa.st/is-ai-generated-content-allowed-on-reddit)
- [Vucense — r/programming bans generative content](https://vucense.com/privacy-sovereignty/digital-independence/reddit-programming-ai-content-ban-2026/)
- [AlternativeTo — Medium bans AI content from Partner Program](https://alternativeto.net/news/2024/4/medium-bans-ai-generated-content-from-its-partner-program-upholding-human-storytelling)
- [SynthID / C2PA watermarking in 2026](https://www.buildmvpfast.com/blog/synthid-content-provenance-c2pa-watermarking-ai-2026) · [SynthID explained](https://www.textsight.ai/blog/google-synthid-watermarking-explained/) · [AI watermarking 2026: Google, OpenAI, Anthropic](https://wp-nitin.com/blog/ai-watermarking-google-openai-anthropic/)
- [OpenAI Text Classifier discontinued](https://gowinston.ai/openai-text-classifier-ai-detector-discontinued/) · [The quiet death of the OpenAI classifier](https://paperbleach.ai/post/openai-shut-down-its-own-detector-what-it-means)
- [CASRAI — AI detector false positives: 2026 update](https://casrai.org/news/ai-detector-false-positive-controversies-2026)
- [Turnitin false positives 2025–2026](https://www.popularai.org/p/these-turnitin-false-positives-in)
- [DataFloq — Pangram is nearly perfect in the lab; publishing treats its score like a verdict](https://datafloq.com/pangrams-ai-detector-is-nearly-perfect-in-the-lab-publishing-is-treating-its-score-like-a-verdict/)
- [StealthGPT review tested against 6 detectors](https://phrasly.ai/blog/stealthgpt-review-does-it-work) · [Best AI humanizers tested](https://theairankings.com/best-ai-humanizer/)

**Section 2 — human-in-the-loop marketplaces**
- [Upwork — MCP: Hire with AI Agents (product page)](https://www.upwork.com/ai/mcp)
- [Upwork Investor Relations — "Upwork Talent Is Now Everywhere AI Works" (10 Aug 2026)](https://investors.upwork.com/news-releases/news-release-details/upwork-talent-now-everywhere-ai-works)
- [TechCrunch — Amazon stops accepting new MTurk customers (5 Jul 2026)](https://techcrunch.com/2026/07/05/amazon-will-stop-accepting-new-customers-for-mechanical-turk/)
- [CNBC — Amazon shutting down the service Bezos called 'artificial artificial intelligence'](https://www.cnbc.com/2026/08/25/amazon-service-that-jeff-bezos-called-artificial-ai-is-shutting-down.html) · [Quartz](https://qz.com/amazon-mechanical-turk-shutting-down-082626) · [TechRepublic](https://www.techrepublic.com/article/news-amazon-mechanical-turk-shutdown/)
- [MTurk closing: 6 alternatives compared (2026)](https://ecorpit.com/mturk-closing-human-data-labeling-alternatives-2026/)
- [human-mcp.io — AI agents hire humans via MCP](https://human-mcp.io/)
- [Toloka — Human-in-the-loop for AI agents: why MCP servers need human expertise (Tendem)](https://toloka.ai/blog/human-in-the-loop-for-ai-agents-why-mcp-servers-need-human-expertise/)
- [Built In — What Is RentAHuman?](https://builtin.com/articles/what-is-rentahuman) · [RentAHuman docs/MCP](https://rentahuman.ai/docs) · [RentAHuman — best platforms for agents to hire humans (vendor)](https://rentahuman.ai/blog/best-platforms-ai-agents-hire-humans-2026)
- [Prolific pricing 2026: platform fees and real costs](https://www.koji.so/blog/prolific-pricing-2026) · [Prolific official pricing](https://www.prolific.com/pricing) · [Prolific vs MTurk](https://www.prolific.com/prolific-vs-mturk)
- [Payman review 2026 — API/SDK/MCP, pricing](https://dupple.com/tools/payman) · [Payman AI on Crunchbase](https://www.crunchbase.com/organization/payman-ai-inc)
- [Nevermined — x402 AI agent billing](https://nevermined.ai/blog/x402-ai-agent-billing) · [Nevermined launches agent card payments with x402 (Morningstar)](https://www.morningstar.com/news/accesswire/1154916msn/nevermined-launches-ai-agent-card-payments-with-x402-opening-a-new-market)
- [Which HITL automation tools have a real approval step in 2026](https://www.usecarly.com/blog/human-in-the-loop-automation-tools/)
- [Zapier — Human in the Loop: pause Zaps for review](https://zapier.com/blog/human-in-the-loop-guide/) · [Zapier — add approval steps to your agent](https://help.zapier.com/hc/en-us/articles/41776074420493-Add-approval-steps-to-your-agent-s-instructions) · [Zapier Slack approvals](https://zapier.com/blog/slack-approval-for-ai-automation/)
- [MCP Elicitation: Human-in-the-Loop for MCP Servers (DEV)](https://dev.to/kachurun/mcp-elicitation-human-in-the-loop-for-mcp-servers-m6a)
- [GongRzhe/Human-In-the-Loop-MCP-Server](https://github.com/GongRzhe/Human-In-the-Loop-MCP-Server) · [KOBA789/human-in-the-loop (Discord)](https://github.com/KOBA789/human-in-the-loop) · [ifmelate/clarify-mcp](https://github.com/ifmelate/clarify-mcp) · [human-in-the-loop-mcp on PyPI](https://pypi.org/project/human-in-the-loop-mcp/) · [FlowHunt HITL MCP](https://www.flowhunt.io/integrations/human-in-the-loop/)
- [OpenAI Agents SDK — human-in-the-loop](https://openai.github.io/openai-agents-python/human_in_the_loop/)
- [Fiverr MCP (unofficial, realitechteam)](https://github.com/realitechteam/fiverr-mcp) · [Fiverr Workspace MCP (viasocket)](https://viasocket.com/mcp/fiverr-workspace)
- [Rev — Human Transcription and Caption API](https://www.rev.com/api)
- [Scale AI status after the Outlier merger](https://hirefeed.co.in/blog/scale-ai-status-after-outlier-merger) · [Remotasks vs Toloka vs Clickworker vs Outlier (2026)](https://remotebridgeai.com/remotasks-vs-toloka-vs-clickworker-vs-outlier/)
- [LinkedIn ghostwriter cost 2026 ($500–$10K/mo)](https://windmillgrowth.com/blogseo/linkedin-ghostwriter-cost) · [LinkedIn ghostwriting pricing $1.5K–$15K/mo](https://www.foundera.co/blog/linkedin-ghostwriting-pricing-guide-2026) · [Mylance — how much does a LinkedIn ghostwriter cost](https://www.mylance.co/blog/how-much-does-a-linkedin-ghostwriter-cost)

**Section 3 — Claude Code / Cowork plugins, skills, scheduling**
- [Claude Code docs — Create plugins](https://code.claude.com/docs/en/plugins)
- [Claude Code docs — Plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces)
- [Claude Code docs — MCP (scopes, `claude mcp list`, tool namespacing)](https://code.claude.com/docs/en/mcp)
- [Claude Code docs — How Claude remembers your project (CLAUDE.md, rules, auto memory)](https://code.claude.com/docs/en/memory)
- [Claude platform docs — Agent Skills overview (frontmatter, progressive disclosure, limits)](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Anthropic — Introducing routines in Claude Code (14 Apr 2026)](https://claude.com/blog/introducing-routines-in-claude-code)
- [Claude Help Center — Schedule recurring tasks in Claude Cowork](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork)
- [Claude docs — Install plugins in Cowork (limits, git marketplaces, org-managed)](https://claude.com/docs/cowork/guide/plugins)
- [Anthropic — Customize Cowork with plugins (30 Jan 2026, 11 official plugins)](https://claude.com/blog/cowork-plugins)
- [Anthropic — Improving skill-creator: test, measure, and refine Agent Skills (3 Mar 2026)](https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills)
- [anthropics/skills — Public repository for Agent Skills](https://github.com/anthropics/skills) · [skill-creator SKILL.md](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) · [skill-creator in claude-plugins-official](https://github.com/anthropics/claude-plugins-official/blob/main/plugins/skill-creator/skills/skill-creator/SKILL.md) · [Skill Creator plugin page](https://claude.com/plugins/skill-creator)
- [anthropics/claude-plugins-community catalog](https://github.com/anthropics/claude-plugins-community/blob/main/.claude-plugin/marketplace.json)
- [Agent Skills open standard: adopted by Claude Code, Codex, Cursor & 32 tools](https://www.paperclipped.de/en/blog/agent-skills-open-standard-interoperability/) · [Portable SKILL.md across Codex CLI, Claude Code and 30+ tools](https://codex.danielvaughan.com/2026/05/05/agent-skills-open-standard-portable-skills-codex-cli-cross-agent/)
- [The Agent Skills Ecosystem in 2026: who's building, what's working](https://agentman.ai/blog/agent-skills-ecosystem-report-2026) · [Agent Skills marketplaces compared](https://www.totalum.app/blog/agent-skills-marketplaces-2026) · [skills.sh guide](https://virtualuncle.com/agent-skills-marketplace-skills-sh-2026/)
- [OpenClaw docs — ClawHub](https://docs.openclaw.ai/clawhub) · [How ClawHub works](https://docs.openclaw.ai/clawhub/how-it-works) · [ClawHub skill format](https://docs.openclaw.ai/clawhub/skill-format) · [Creating skills](https://docs.openclaw.ai/tools/creating-skills) · [openclaw/clawhub repo](https://github.com/openclaw/clawhub)
- [Forbes — What is OpenClaw, formerly Moltbot? (6 Feb 2026)](https://www.forbes.com/sites/kateoflahertyuk/2026/02/06/what-is-openclaw-formerly-moltbot--everything-you-need-to-know/) · [Clawdbot → Moltbot → OpenClaw name history](https://www.openclawexperts.io/clawdbot-moltbot-openclaw-name-history) · [OpenClaw 2026 guide (ClawHub skills, security)](https://github.com/SkillsMP/openclaw-ai)
- [VoltAgent/awesome-openclaw-skills — marketing and sales category](https://github.com/VoltAgent/awesome-openclaw-skills/blob/main/categories/marketing-and-sales.md) · [Best OpenClaw skills for social media marketing](https://postfa.st/blog/best-openclaw-skills-for-social-media-marketing) · [ClawHub guide for marketers](https://contentstudio.io/blog/clawhub-guide)
- [sergebulaev/linkedin-skills — 11 Claude/Codex LinkedIn skills (MIT)](https://github.com/sergebulaev/linkedin-skills) · [LinkedIn Claude Skills guide](https://blog.mystrika.com/linkedin-claude-skills/)
- [TechRadar — Claude Code plugin quietly triggers consent prompts and collects data](https://www.techradar.com/pro/that-felt-wrong-dev-uses-claude-to-expose-why-a-popular-no-code-platform-wants-to-read-all-your-prompts) · [The Vercel plugin on Claude Code wants to read all your prompts](https://akshaychugh.xyz/writings/png/vercel-plugin-telemetry)
- [Claude Code telemetry with OpenTelemetry](https://docs.kuberocketci.io/blog/claude-code-telemetry-opentelemetry-token-cost-tracking) · [Feature request: skill invocation tracking and usage analytics](https://github.com/anthropics/claude-code/issues/35319)agentId: a32f77d79844544e0 (use SendMessage with to: 'a32f77d79844544e0', summary: '<5-10 word recap>' to continue this agent)
<usage>subagent_tokens: 181860
tool_uses: 107
duration_ms: 814063</usage>