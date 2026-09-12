# Human rewrite lanes and complementary MCPs — 8 Sep 2026

Two sub-reports. Prices are as published on the date; verify before budgeting.

---

## Part A — Can an agent hire a human to write a 150–300 word post for cents?

### Corrections to the premise

- **"Hire Human" (hirehuman.ai)** is a free AI-skills training and job-placement program founded by Jim McKelvey, not a marketplace; no API. The ~8 similarly named 2026 startups (Human API, human-mcp.io, HumanMCP.ai, HumanOps, HumanPing, Human Pages, RentAHuman, RentHuman) are what people usually mean.
- **Anthropic watermarks Claude text since 2 Aug 2026** (SynthID-Text; Claude, Claude Code, Cowork, API; no opt-out). "Light editing probably won't remove the watermark completely; a complete rewrite where every word is replaced will." Proofreading a person's text leaves "very little (if anything) for the watermark to attach to." Short passages carry weak signal. Detector access: regulators, law enforcement, media, fact-checkers, researchers, educational institutions, compliance-obligated enterprises; a free checker exists at claude.com/check-content. Verified on anthropic.com/news/claude-text-watermark.
- **Amazon MTurk closes 30 Sep 2026** (new customers stopped ~5 Jul); SageMaker Ground Truth goes with it. No named successor.

### Ranked options (price per ~250-word rewrite, all-in)

| # | Service | Price | Turnaround | API / MCP | Min spend | Quality / native English | Link |
|---|---|---|---|---|---|---|---|
| 1 | **Prolific, AI Task Builder** | ~$1.50–2.20 ($8/hr floor for ~8 min + ~40% fee) | minutes–hours | Full REST API + CLI (`prolific collection create/publish`, `submission list`, export) | none stated | Vetted pool; "AI Taskers" tier; filter by country + first language; `rich_text` blocks carry the style guide and exemplars | docs.prolific.com/api-reference |
| 2 | **Microworkers API 2.0** | $0.30–1.00 (you set it; 7.5–10% fee; $0.75 campaign fee on Basic) | minutes–hours | Documented REST: campaign create, submissions, rate, bonus | $10 deposit | Weakest tier; country/city targeting; pay only if satisfied; revisions | api2docs.microworkers.com |
| 3 | **CloudResearch Connect** | ~$1.75–2.20 ($7.50/hr floor; +40% commercial fee) | 500 participants in 1–2 h | AI-training project type; API not public | none | US-only pool; Sentry fraud detection | connect-researcher-help.cloudresearch.com |
| 4 | **human-mcp.io** | $1.15+ ($1 min + 15%) | unproven liquidity | 19 MCP tools + REST (`post_task`, `invite_to_task`, `approve_and_pay`, `request_revision`, attachments) | $1, prepaid wallet | Escrow, ratings, disputes; lists proofreading/copywriting; **no published pool size** | human-mcp.io/docs |
| 5 | **Toloka Tendem** | not published | "hours" | MCP integration | "no minimums" | 20+ domains, verified experts; positioned for judgment tasks | nebius.com/solutions/tendem |
| 6 | **Textbroker (SOAP API)** | $6.25 (3★, 2.3¢/w) · $8.50 (4★) · $23 (5★) + $0.50/order | hours–days | Yes: place/accept orders, sub-accounts, budgets; **TeamOrder** = standing writer group | $0.50/order; managed service $2,500 | 100k+ star-rated authors; briefing field native | textbroker.com/automate-content-publishing |
| 7 | **Upwork MCP** (10 Aug 2026) | freelancer rate (~$10–30) | hours–days | Official MCP, OAuth 2.1; **human confirms writes; payment on upwork.com** | standard fees | Excellent quality, full profiles | upwork.com/ai/mcp |
| 8 | **Scribendi API** | on request | to deadline | Editing API, gated access | unknown | ISO 9001; **supports custom house style guides** | scribendi.com/editing_services_api.en.html |
| 9 | **Freelancer.com API** | bid | hours–days | Public API ("Task humans from software") | varies | variable | developers.freelancer.com |
| — | RentAHuman.ai | $10–300+ | days | REST + MCP; 793k humans | — | **physical-world tasks only** | rentahuman.ai |
| — | HumanMCP.ai / HumanOps / HumanPing / Human Pages | undisclosed | undisclosed | MCP | — | calls/research/verification; no text editing; no traction data | — |
| — | Human API (thehumanapi.com) | n/a | n/a | "agent-native" | — | currently voice-data collection | — |

Ruled out: MTurk (closing), Rev (transcription only), Appen/CrowdGen, Scale Rapid, Surge, Mercor (enterprise), Fiverr (developers.fiverr.com is marketing; Fiverr Go is an AI product), Contra, PeoplePerHour, Scribbr, Wordvice, ProofreadingPal, Grammarly (no API), Verblio, WriterAccess, Crowd Content, Contentfly, iWriter (no public ordering API), Gengo (translation), Payman (payment rails only).

### Does a human pass defeat detection?

- Watermark robustness (arXiv 2508.20228, SynthID-Text at 200 tokens): synonym substitution at 70% still F1 0.884; heavy paraphrase 0.842; back-translation 0.711; copy-paste dilution is the strongest attack.
- Classifiers vs. light human editing (arXiv 2608.11256): Pangram flagged **64–80%** of lightly edited AI rewrites, GPTZero 38–49%; automated humanizers left <4% flagged. Same study: false positives on genuine 2023–25 human abstracts, Pangram 14.9%, GPTZero 8.9%.
- Synthesis: a light human pass over model prose is the worst of both worlds. Only a substantive rewrite where the human writes every word clears both watermark and classifiers, and only that is honestly human-authored.

### Recommended architecture (adopted in the plugin as `humanpass`)

1. Claude emits a **brief**, never prose: claim, facts with sources, required/forbidden terms, length, ending, one-screen negative style guide, 3–5 exemplars.
2. Human writes: tier 0 the user (voice note), tier 1 retained editor via Slack/Telegram, tier 2 Prolific (~$1.50–2), tier 3 Microworkers (cents, variance), tier 4 Textbroker TeamOrder (quality), tier 5 human-mcp.io / Upwork MCP (experimental).
3. Verify: facts retained, forbidden terms absent, length/ending/format, **3-gram overlap with any model draft < 25%** (else it was an edit, request revision), optional detector score as information only.
4. Pay per task on the platform's own rails; rate honestly.

---

## Part B — MCP servers by capability (Sept 2026)

Headline facts: **X has an official hosted MCP** (`https://api.x.com/mcp`, OAuth via `xurl`, pay-per-use: post $0.015, post with URL $0.20, owned reads $0.001). **LinkedIn has no official MCP**; `r_member_social` access requests are closed; session-cookie scrapers warn of bans in their own READMEs. **Claude Code supports MCP elicitation** (form and URL modes). Plugins can bundle MCP servers (`mcpServers` in plugin.json or `.mcp.json`, stdio/sse/http/ws, `userConfig` with `sensitive: true`, `channels` for notifications) but **cannot declare recommended connectors**; Anthropic's directory auto-enrolls entries in Suggested Connectors.

| Capability | Default | Alternatives | Avoid |
|---|---|---|---|
| Posting LinkedIn + X | **Buffer MCP** (official, OAuth, free on all plans, both networks, analytics) | **Typefully MCP** (`https://mcp.typefully.com/mcp`, OAuth; X, LinkedIn, Threads, Bluesky, Mastodon); Ayrshare (27 tools, multi-user pricing); SocialClaw (19 tools, `preview_campaign`/`apply_schedule`, free tier); Postiz (30+ platforms; API key in URL); post-bridge (14 tools) | Upload-Post (3 stars); Late/Zernio (community only); Hootsuite (no MCP) |
| X read/search/analytics | **X MCP official** | — | third-party X scrapers |
| LinkedIn analytics | Publishing vendor's analytics tools | Taplio / ContentIn (approved API, paid) | Apify LinkedIn actors; Shield (reported shutdown) |
| Feeds/browsing | Claude in Chrome / built-in browser; **Playwright MCP** (Microsoft, official) | ScreenshotOne MCP, Browserbase MCP | `stickerdaniel/linkedin-mcp-server` (3.3k★; README warns of bans) |
| Meetings | **Fathom** (`https://api.fathom.ai/mcp`), **Granola** (`https://mcp.granola.ai/mcp`), **Fireflies** — all official OAuth | **Pam Memory & Notetaker** (transcripts + memory in one), Zoom MCP, tl;dv | Otter (Enterprise-gated) |
| Memory | Claude built-in | **Supermemory** (`https://mcp.supermemory.ai/mcp`, OAuth), Mem0 MCP | Letta as a plugin dependency |
| Research | **Exa MCP** (`https://mcp.exa.ai/mcp`, no key on free tier; `web_search_exa`, `web_fetch_exa`) | **Tavily** (OAuth; search/extract/map/crawl), **Firecrawl**, Perplexity | anything claiming a Google Scholar API |
| Images | **Replicate MCP** (official, `https://mcp.replicate.com` or `npx replicate-mcp`) | **Recraft MCP** (OAuth; vector + brand styles), fal (community action servers) | community gpt-image / Nano Banana wrappers by default |
| Design / carousels | **Canva MCP** (`https://mcp.canva.com/mcp`, OAuth; export PDF/PNG/PPTX) | **PostNitro MCP** ($10/mo, 35 tools, carousels), Figma MCP (official), Bannerbear via Zapier/Composio | Placid, Adobe Express (no MCP) |
| Diagrams | Native mermaid in Artifacts | Mermaid Chart MCP, Excalidraw MCP (community) | QuickChart (low confidence) |
| Voice notes | **Deepgram MCP** (`dg mcp`; local file path; summary/topics) | **ElevenLabs MCP** (Scribe; free tier; 1.5k★) | Whisper community servers unless audio must stay local |
| Detection APIs | **GPTZero** (sentence-level highlights; no retention) | **Pangram** (three base URLs; Developers plan), Originality, Copyleaks, Sapling | any score used as a verdict (FPR 9–15% on real human text) |
| Notifications / approvals | **MCP elicitation** + **Slack MCP official** (`https://mcp.slack.com/mcp`, GA Feb 2026; request/response only) | Telegram notify-only servers via plugin `channels`; Gmail connector | full-account Telegram MCPs |

Packaging recipe: bundle nothing that needs a secret by default; ship `mcp/recommended.mcp.json` as copy-ready entries; suggest one server per gap in conversation at onboarding; write detection calls as HTTPS from a script (no MCP wrappers exist); use elicitation for approvals; never bundle a LinkedIn scraper.

### Sources (selected)

anthropic.com/news/claude-text-watermark · support.claude.com/en/articles/16266773 · arxiv.org/abs/2508.20228 · arxiv.org/abs/2608.11256 · techrepublic.com (MTurk shutdown) · docs.prolific.com/api-reference · api2docs.microworkers.com · human-mcp.io/docs · nebius.com/solutions/tendem · textbroker.com/automate-content-publishing · upwork.com/ai/mcp · scribendi.com/editing_services_api.en.html · hirehuman.ai · docs.x.com/tools/mcp · docs.x.com/x-api/getting-started/pricing · buffer.com/mcp · support.typefully.com (MCP server) · ayrshare.com/docs/additional/mcp-server · postiz.com/mcp · post-bridge.com/mcp · getsocialclaw.com/mcp · github.com/stickerdaniel/linkedin-mcp-server · learn.microsoft.com/linkedin/marketing/community-management · docs.apify.com/integrations/mcp · replicate.com/docs/reference/mcp · recraft.ai/docs/mcp-reference · canva.dev/docs/mcp · help.figma.com (Figma MCP) · postnitro.ai/mcp · mcpservers.org (Playwright, Fathom, Granola, Browserbase) · fireflies.ai/blog/fireflies-mcp-server · supermemory.ai/docs/supermemory-mcp/setup · docs.mem0.ai/platform/mem0-mcp · exa.ai/docs/reference/exa-mcp · docs.tavily.com/documentation/mcp · github.com/firecrawl/firecrawl-mcp-server · docs.pangram.com · gptzero.me/developers · code.claude.com/docs/en/mcp · code.claude.com/docs/en/plugins-reference · claude.com/docs/connectors/directory · claude.com/docs/cowork/3p/extensions · developers.deepgram.com/developer-tools/cli/mcp-server · github.com/elevenlabs/elevenlabs-mcp
