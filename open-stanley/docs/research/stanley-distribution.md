# Stanley (getstanley.ai / x.getstanley.ai) — Deep Research Report
*Research date: 2026-09-08. Every claim carries a source URL. Where the brief's premises diverged from what's publicly verifiable, I flag it explicitly.*

---

## 0. Headline correction to the brief

The brief describes Stanley as an independent product by "Vitalii Dodonov and team." That's partly right but misses the key structural fact:

**Stanley is a product of Stan** (legal name *Find Community, Inc.*), the creator link-in-bio/storefront company doing ~$40M ARR, co-founded by **John Hu (CEO)** and **Vitalii Dodonov (CTO)**. Stanley is Stan's first upsell/expansion product into its existing ~80,000-creator base. ([Sacra](https://sacra.com/c/stan/), [Crunchbase](https://www.crunchbase.com/organization/stan-9644), [PRNewswire](https://www.prnewswire.com/news-releases/stan-the-creator-platform-powering-80-000-active-users-launches-stanley-an-ai-head-of-content-for-linkedin-302716013.html))

Second correction: **public pricing is $47/mo (Instagram) and $149/mo (LinkedIn)**, sold as separate subscriptions — not $10–100/mo. The "negotiate with Stanley in chat" mechanic is real and documented, but it appears to be specific to the **Stanley for 𝕏** product and to early cohorts, not the mainline LinkedIn/IG SKUs. Details in §2.4.

Third: there are now **at least four distinct "Stanley" surfaces**, which is why sources conflict:

| Surface | URL | Notes |
|---|---|---|
| Stanley for LinkedIn | stanley.stan.store | $149/mo, launched Mar 17 2026 |
| Stanley for Instagram | iOS app "Stanley: AI Head of Content" | $44.99–47/mo, App Store |
| Stanley for 𝕏 | x.getstanley.ai / twt.getstanley.ai | Product Hunt Apr 22 2026, #2 of day |
| Stanley (unified, multi-platform) | getstanley.ai | iMessage/Telegram/web, current positioning |
| Stanley Studio | separate | AI video editor, $49/mo, Aug 2026 |

---

## 1. Team, company, funding, geography

### 1.1 People

**Vitalii Dodonov — Co-founder & CTO, Stan; the driving force behind Stanley**
- Ukrainian-born, immigrated to Canada without English proficiency; the only school that would accept his IELTS score was a community college in **Grande Prairie, Alberta**. ([StartWell](https://startwell.co/blogs/insights/stans-co-founder-killed-his-own-revenue-line-on-purpose-vitalii-dodonov))
- Studied **chemical engineering at the University of Alberta**, self-taught coding. ([Benzatine summary of his Business Insider essay](https://benzatine.com/news-room/from-zero-to-50000-in-six-weeks-the-journey-of-a-toronto-creator-with-ai))
- **Data scientist at Deloitte** → **senior engineer at eBay** (got the eBay job by demoing a self-built product instead of doing a conventional interview). ([StartWell](https://startwell.co/blogs/insights/stans-co-founder-killed-his-own-revenue-line-on-purpose-vitalii-dodonov), [Indie Hackers](https://www.indiehackers.com/post/tech/going-all-in-and-hitting-30m-arr-in-three-years-IBwjFYRHPn5joh0Qm17J))
- **Prior company: Vhinny**, a financial information platform. ([Benzatine](https://benzatine.com/news-room/from-zero-to-50000-in-six-weeks-the-journey-of-a-toronto-creator-with-ai))
- Age ~29, **based in Toronto**. ([Let's Data Science](https://letsdatascience.com/news/founder-builds-stanley-and-hits-50000-in-revenue-566e8b41), [Benzatine](https://benzatine.com/news-room/from-zero-to-50000-in-six-weeks-the-journey-of-a-toronto-creator-with-ai))
- Met John Hu **through a mutual customer during the pandemic**. ([StartWell](https://startwell.co/blogs/insights/stans-co-founder-killed-his-own-revenue-line-on-purpose-vitalii-dodonov))
- Member, **Forbes Technology Council**. ([Forbes Councils](https://councils.forbes.com/profile/Vitalii-Dodonov-Co-Founder-Stan/0a3f33b3-a74a-44ac-a00c-4aba2ab2004c))
- LinkedIn audience grew **~6,500 → 22,600 followers**; Favikon scores him 96.5/100 authenticity, 92 "Authentic" on AI signals. Content style: "part hiring board, part founder diary, part playbook" — metrics, roadmaps, screenshots, feedback requests. ([Favikon](https://www.favikon.com/blog/who-is-vitalii-dodonov))
- X: [@vitaliidodonov](https://x.com/vitaliidodonov); Medium: [@vitddnv](https://medium.com/@vitddnv)

**John Hu — Co-founder & CEO, Stan**
- Left **private equity** to become a content creator; identified the monetization problem that became Stan. ([Indie Hackers](https://www.indiehackers.com/post/tech/going-all-in-and-hitting-30m-arr-in-three-years-IBwjFYRHPn5joh0Qm17J))
- X: [@JayHoovy](https://x.com/JayHoovy) — the primary X launch account for Stanley.

**Other named people**
- **"Pascio"** — credited maker on the Stanley for 𝕏 Product Hunt launch; a real X ghostwriter who "grew accounts from zero to 10K followers"; the X product is explicitly "trained on data from a real $5k/m Twitter ghostwriter." ([Product Hunt](https://www.producthunt.com/products/stanley-for-x), [twt.getstanley.ai](https://www.twt.getstanley.ai/))
- **Jordyn Kerr** — Stan's content/blog author, writes the Stanley case studies. ([stan.store/blog](https://stan.store/blog/how-we-built-stanley-linkedin/))
- **Ricky P.** — Stan team member surfaced in search. ([LinkedIn](https://www.linkedin.com/in/rpatel8457/))

### 1.2 Company & funding

- **Legal entity:** Find Community, Inc.; App Store developer name is **"FindCommunity, Inc."** ([Crunchbase](https://www.crunchbase.com/organization/stan-9644), [App Store](https://apps.apple.com/us/app/stanley-ai-head-of-content/id6754887783))
- **Founded:** 2020–2021 (sources differ; Sacra says 2020, Indie Hackers says launched 2021). ([Sacra](https://sacra.com/c/stan/), [Indie Hackers](https://www.indiehackers.com/post/tech/going-all-in-and-hitting-30m-arr-in-three-years-IBwjFYRHPn5joh0Qm17J))
- **HQ:** Sacra says **Los Angeles**; Crunchbase says **New York**; Dodonov personally operates from **Toronto**. Treat it as distributed/remote. ([Sacra](https://sacra.com/c/stan/), [Crunchbase](https://www.crunchbase.com/organization/stan-9644))
- **Funding:** $5M seed (2022) from **Forerunner Ventures** per Sacra; Crunchbase lists 3 rounds (pre-seed, seed, venture) with **Norwest Venture Partners** (Jeff Crowe) and **Gary Vaynerchuk** as lead investor. Amounts obfuscated on Crunchbase. ([Sacra](https://sacra.com/c/stan/), [Crunchbase](https://www.crunchbase.com/organization/stan-9644))
- **Revenue trajectory:** $3M ARR (18mo) → $10M (yr 2) → $30M (yr 3) → **$40M ARR (Apr 2026)**, ~$3.3M/month. ([Sacra](https://sacra.com/c/stan/), [Indie Hackers](https://www.indiehackers.com/post/tech/going-all-in-and-hitting-30m-arr-in-three-years-IBwjFYRHPn5joh0Qm17J))
- **Creator earnings facilitated:** $500M+ (Mar 2026 PR) → $600M+ (StartWell, later). Stan takes **zero transaction commission** — a deliberate kill of its own revenue line, made because creators kept asking "how much are they taking?" ([PRNewswire](https://www.prnewswire.com/news-releases/stan-the-creator-platform-powering-80-000-active-users-launches-stanley-an-ai-head-of-content-for-linkedin-302716013.html), [StartWell](https://startwell.co/blogs/insights/stans-co-founder-killed-his-own-revenue-line-on-purpose-vitalii-dodonov))
- **Team:** fewer than 50 people, ~$800K+ revenue/employee. (Crunchbase's "1–10" is stale.) ([Indie Hackers](https://www.indiehackers.com/post/tech/going-all-in-and-hitting-30m-arr-in-three-years-IBwjFYRHPn5joh0Qm17J))
- **Stan Store pricing:** Creator $29/mo, Creator Pro $99/mo, no free tier, ~13% monthly churn as of Q1 2024. ([Sacra](https://sacra.com/c/stan/), [Sacra interview](https://sacra.com/research/vitalii-dodonov-stan-creator-aligned-store-in-bio/))

---

## 2. Launch & distribution

### 2.1 The origin sprint

Stanley was built in a **14-day "Hacker House" sprint in London** — a trip Dodonov originally booked as honeymoon prep. Numbers from the sprint: **200+ hours of coding, 10+ customer interviews, 500+ beta applications, 200+ paying customers by day 14.** ([StartWell](https://startwell.co/blogs/insights/stans-co-founder-killed-his-own-revenue-line-on-purpose-vitalii-dodonov), [stan.store/blog](https://stan.store/blog/how-we-built-stanley-linkedin/))

### 2.2 Timeline

| Date | Event | Source |
|---|---|---|
| Feb 18, 2026 | "How We Built a $1M+ AI Agent in 14 Days" blog published | [stan.store](https://stan.store/blog/how-we-built-stanley-linkedin/) |
| **Mar 17, 2026** | **Stanley for LinkedIn** official launch (PRNewswire) | [PRNewswire](https://www.prnewswire.com/news-releases/stan-the-creator-platform-powering-80-000-active-users-launches-stanley-an-ai-head-of-content-for-linkedin-302716013.html) |
| Mar 12–25, 2026 | First iOS App Store reviews (incl. critical ones) | [App Store](https://apps.apple.com/us/app/stanley-ai-head-of-content/id6754887783) |
| **Apr 2, 2026** | **Stanley for Instagram** PR: 20M views from one video, creator +80K followers | [PRNewswire](https://www.prnewswire.com/news-releases/stanley-for-instagram-drives-20m-views-from-one-video-helps-creator-gain-80k-followers-302732526.html) |
| **Apr 22, 2026** | **Stanley for 𝕏 on Product Hunt — #2 Product of the Day, 406 upvotes** | [Product Hunt awards](https://www.producthunt.com/products/stanley-for-x/awards) |
| May 12, 2026 | App v1.37: "Set up iMessage with Stanley" | [App Store](https://apps.apple.com/us/app/stanley-ai-head-of-content/id6754887783) |
| May 29, 2026 | Business Insider as-told-to essay by Dodonov ($50K in 6 weeks) | [Let's Data Science](https://letsdatascience.com/news/founder-builds-stanley-and-hits-50000-in-revenue-566e8b41), [MSN copy](https://www.msn.com/en-us/money/other/i-built-an-ai-content-tool-for-creators-that-hit-50-000-in-revenue-in-6-weeks-here-s-what-it-takes-to-vibe-code-successfully/ar-AA24luOZ) |
| Jul 9 / Jul 21 / Jul 31 | Content Calendar improvements; blog updates | [App Store](https://apps.apple.com/us/app/stanley-ai-head-of-content/id6754887783), [stan.store](https://stan.store/blog/stanley/) |
| **Aug 7, 2026** | **Stanley Studio** (AI video editor) launched | [stan.store](https://stan.store/blog/stanley-studio/) |
| Aug 25, 2026 | App v1.56 | [App Store](https://apps.apple.com/us/app/stanley-ai-head-of-content/id6754887783) |

### 2.3 Product Hunt (Stanley for 𝕏)

- **Date:** April 22, 2026. **Rank: #2 Product of the Day. 406 upvotes. 723 followers. 5.0 rating from 3 reviews.** ([PH awards page](https://www.producthunt.com/products/stanley-for-x/awards), [PH product page](https://www.producthunt.com/products/stanley-for-x))
- **Tagline:** *"The world's first AI Head of Content."*
- **Makers:** Vitalii Dodonov + Pascio.
- Maker comments on the launch:
  - Vitalii: *"It syncs your social content in real-time — so it writes in whatever voice you write!"*
  - Pascio: the tool handles *"niche research and what's working at this very moment"* even for accounts with almost no posting history.
  - A commenter on the packaging: *"attention is attention - someone will get it - better be you!"*
- **Pricing framing on PH: free tier available, paid "negotiable" — explicitly, "you can negotiate with Stanley."** ([Product Hunt](https://www.producthunt.com/products/stanley-for-x))
- Interfaces named on PH: **iMessage, SMS, Telegram, desktop.**
- I could **not** retrieve the launch video itself — Product Hunt's media isn't text-extractable and X/Nitter mirrors are robots-blocked. The narrative framing across every surface, though, is consistent: *a real ghostwriter's system, encoded, that texts you like an employee.*

### 2.4 The growth loop — what's verified vs. not

**Verified: build-in-public as the primary channel.**
> *"Stanley didn't scale to $1M+ ARR because we ran ads. It scaled because we built it in public."* — [stan.store/blog](https://stan.store/blog/how-we-built-stanley-linkedin/)

Mechanics:
- **17 LinkedIn posts during the 14-day sprint**, documenting failures and wins in real time. ([StartWell](https://startwell.co/blogs/insights/stans-co-founder-killed-his-own-revenue-line-on-purpose-vitalii-dodonov))
- **The launch-day LinkedIn post alone generated 2,000+ comments and $200K ARR** with 200–250 paying customers on day one. ([stan.store/blog](https://stan.store/blog/how-we-built-stanley-linkedin/), [Indie Hackers](https://www.indiehackers.com/post/tech/going-all-in-and-hitting-30m-arr-in-three-years-IBwjFYRHPn5joh0Qm17J))
- **Hyper-personalized cold email to marquee LinkedIn creators** — Justin Welsh, Lara Acosta, Steven Bartlett — using an analysis-as-hook: *"I spent the last 3 days analyzing your competitors."* Founder framing: *"A great cold email will get you into rooms you have absolutely no business being in."* Justin Welsh's quoted reaction: ***"This knows me a lot better than Claude or ChatGPT does."*** ([stan.store/blog](https://stan.store/blog/how-we-built-stanley-linkedin/))
- **Founder-DM'd creators directly** for feedback and adoption; shipped fixes within hours. ([Indie Hackers](https://www.indiehackers.com/post/tech/going-all-in-and-hitting-30m-arr-in-three-years-IBwjFYRHPn5joh0Qm17J))
- **Customer-as-salesperson loop:** *"Your customers are your best salespeople. That's how you grow."* Early customers publicly attributed results (e.g. *"$200K in contract lead value"*) which then became the marketing. ([stan.store/blog](https://stan.store/blog/how-we-built-stanley-linkedin/))
- **Cross-sell into the installed base:** Sacra explicitly calls Stanley *"Stan's first meaningful attempt at upsell within its creator base"* and a new expansion-revenue lever across 80,000 creators. ([Sacra](https://sacra.com/c/stan/))
- **PR flywheel:** three PRNewswire releases in ~6 weeks, syndicated to Yahoo Finance, TMCnet, Dealroom, techintelpro, BriefGlance. Each is built around a single dramatic creator number (20M views, +80K followers). ([Yahoo](https://finance.yahoo.com/sectors/technology/articles/stanley-instagram-drives-20m-views-130000821.html), [Dealroom](https://app.dealroom.co/news/feed/stan-launches-stanley-an-ai-head-of-content-for-linkedin-to-help-80-000-creators-build-personal-brands), [TMCnet](https://www.tmcnet.com/usubmit/2026/03/17/10349343.htm))
- **Podcasts:** StartWell Podcast, Mike Wystrach's podcast, Canadian Business, BrainStation "Creators of Toronto" (Mar 3, 2026). ([StartWell](https://startwell.co/blogs/insights/stans-co-founder-killed-his-own-revenue-line-on-purpose-vitalii-dodonov), [mikewystrach.com](https://mikewystrach.com/podcast/vitalii-dodonov), [Canadian Business](https://canadianbusiness.com/people/vitalii-dodonov-stan/), [BrainStation](https://brainstation.io/events/leadership/creators-of-toronto-20260303))
- **Owned-media essay placement:** Business Insider as-told-to, which then got re-aggregated across MSN, Let's Data Science, Benzatine, Machinebrief.

**Verified: 20% recurring referral.** Stan's referral program pays **20% recurring commission for as long as the referred creator stays subscribed, "for life,"** paid monthly via Stripe or PayPal. Important caveat: the help doc lists **only Stan Store Creator/Creator Pro subscriptions as qualifying** — it does *not* name Stanley. There's also an **invite-only Ambassador Program** for creators already promoting Stan, gated on active subscription + active referral earnings. ([Stan help center — referral](https://help.stan.store/article/89-what-is-stans-referral-or-affiliate-program), [Ambassador](https://help.stan.store/article/225-stan-ambassador-program))

**Verified: price negotiation with the agent.** Two independent confirmations:
> *"Its pricing model is unconventional: users negotiate directly with the AI based on perceived value rather than fixed rates."* — [StartWell](https://startwell.co/blogs/insights/stans-co-founder-killed-his-own-revenue-line-on-purpose-vitalii-dodonov)

and the Product Hunt listing's "you can negotiate with Stanley." However, **no public source anywhere states a $10–100/mo band.** Every published price is $44.99/$47 (IG), $149 (LinkedIn), $49 (Studio). AuthoredUp notes free trials exist only via *"affiliate/member referral links only"*, and Carly warns *"trial terms depend on which checkout surface you use."* That variable-checkout-surface behavior is consistent with negotiated pricing but doesn't confirm the range. ([AuthoredUp](https://authoredup.com/blog/stanley-review), [Carly](https://www.usecarly.com/blog/stanley-pricing/))

**NOT verified — treat as unconfirmed:**
- **"Pay-per-view for mentions up to $500/post."** Nothing in Stan's help center, PR, blog, or any third-party review mentions paid creator posts, per-view rates, or a $500 cap. The Ambassador Program page explicitly declines to state compensation. If this exists it's an in-DM/in-Telegram offer with no public paper trail.
- **"Gift codes."** No public documentation found.
- **"Rituals"** as a named product feature. The closest public analogue is documented as **"daily nudges, checklists, streaks, weekly feedback"** and *"Proactive from day one… Stanley reaches out with ideas and draft concepts before you ask."* If "rituals" is the internal/in-product name, it isn't in any indexed page. ([Carly](https://www.usecarly.com/blog/stanley-ai-review/), [getstanley.ai](https://getstanley.ai/))
- **Hacker News.** I found no HN submission or discussion of Stanley/getstanley. This is a LinkedIn/IG/X-creator-native launch; HN was not a channel.
- **Reddit.** No indexed Reddit threads about Stanley surfaced across multiple query formulations. Notably absent given the price point.

### 2.5 Public numbers

| Metric | Value | Source |
|---|---|---|
| Day-1 paying customers | 200–250 | [stan.store](https://stan.store/blog/how-we-built-stanley-linkedin/), [Benzatine](https://benzatine.com/news-room/from-zero-to-50000-in-six-weeks-the-journey-of-a-toronto-creator-with-ai) |
| Launch-day ARR from one post | $200K | [stan.store](https://stan.store/blog/how-we-built-stanley-linkedin/) |
| MRR at 6 weeks | $50,000 | [Let's Data Science](https://letsdatascience.com/news/founder-builds-stanley-and-hits-50000-in-revenue-566e8b41) |
| ARR at 7 months | $1M+ | [stan.store](https://stan.store/blog/how-we-built-stanley-linkedin/) |
| Beta applications | 500+ | [stan.store](https://stan.store/blog/how-we-built-stanley-linkedin/) |
| iOS ratings | 4.6–4.7 / 5 from ~451–455 ratings | [App Store](https://apps.apple.com/us/app/stanley-ai-head-of-content/id6754887783) |
| Claimed user outcomes | +50% engagement, +70% comments | [Net Influencer](https://www.netinfluencer.com/stan-helped-creators-make-500m-selling-digital-products-its-biggest-lesson-was-that-products-arent-the-problem/) |
| Landing page social proof | "Trusted by 1,500 founders" / "3,000 founders" (both strings present) | [twt.getstanley.ai](https://www.twt.getstanley.ai/) |

**Named case studies:** Elly Walton, 43, +60K followers from one video (40K → 100K); Charlie Dadia, 160 product sales + 48% IG view jump in two months; Khadaura, 16K → 100K+ followers in 3 months. ([PRNewswire](https://www.prnewswire.com/news-releases/stanley-for-instagram-drives-20m-views-from-one-video-helps-creator-gain-80k-followers-302732526.html), [Net Influencer](https://www.netinfluencer.com/stan-helped-creators-make-500m-selling-digital-products-its-biggest-lesson-was-that-products-arent-the-problem/), [App Store](https://apps.apple.com/us/app/stanley-ai-head-of-content/id6754887783))

⚠️ Sourcing caveat, from the one outlet that applied any: the $50K figure comes from *"an as-told-to first-person essay by Dodonov in Business Insider without independent auditor verification… early revenue alone doesn't reveal unit economics, retention rates, or scaling sustainability."* ([Let's Data Science](https://letsdatascience.com/news/founder-builds-stanley-and-hits-50000-in-revenue-566e8b41))

### 2.6 Landing page copy (verbatim)

**getstanley.ai** — [source](https://getstanley.ai/)
> "Build your audience with Stanley."
> "Your AI Head of Content across social media."
> "One thread, across platforms, always on."
> "Stanley drafts, schedules, and checks back when posts land, all through iMessage, Telegram, or on the web."
> "Proactive from day one." / "Drafts in your voice." / "Knows what performs." / "He handles the whole loop." / "You create. He keeps you posting."
> "He learns how you talk from your posts and voice notes. Every draft reads like you wrote it."
> "Voice note in. Draft, schedule, post, and the numbers back. All in one thread."
> "Stanley starts learning your voice on day one. Your first text arrives within the week."
> Without Stanley: *"Blank pages and a calendar you dread."*
> Onboarding sample text: *"saw your last reel. the hook was great. want me to draft two more like it?"*
> Contact: iMessage / Telegram / SMS **+1 (646) 382-4202** (a second number, +1 (646) 382-4226, appears on /welcome; the X-product page lists +1 (205) 354-4431 — they appear to A/B or rotate numbers)
> Footer: "© 2026 · Part of Stan Store"

Testimonials on the unified page — **Elly Walton (Creator)**, **Daniel Park (Creator)**, **Nadia O'Connor (Realtor)**. The realtor one is the sharpest positioning tell:
> *"I sell houses. I do not have time to 'build a content strategy.' Stanley does it from my voice notes."*

**twt.getstanley.ai / x.getstanley.ai (Stanley for 𝕏)** — [source](https://www.twt.getstanley.ai/)
> "Make 𝕏 your unfair advantage"
> "Your AI Head of Content For Growing On 𝕏"
> "Meet Your AI Twitter Ghostwriter — Stanley"
> "An AI employee to run your entire Twitter strategy"
> "Trained On Data From A Real $5k/m Twitter Ghostwriter"
> "Always Using The Latest AI Model" · "Infinite Memory — Stanley remembers everything you talk about together"
> "While you sleep, he locates the conversations you should be joining and drafts replies for you"
> "Stanley finds interesting people in your niche and even writes the DMs you should be sending"
> "Free to try! (no credit card or sign up required)"

The X page runs an explicit **three-column comparison — GPT/Claude vs. Real Ghostwriter vs. Stanley** — anchoring against a **$5,000/mo human retainer** ("limited by human bandwidth… not available when ideas hit… hard to scale content volume fast") while dismissing general LLMs as "generic and robotic… weak memory of your voice… writes words, no positioning."

X-page testimonials with follower counts: **Tim Denning (134K)**, **Aaron Will (286K)** — *"I sat down with Stanley for 30 minutes and he asked me some questions, studied my best content, and then started producing content that I would actually write myself. This is my new Head of Content now."* — and **Valdo (52K)** — *"Stanley has taste. He didn't just say 'yeah looks great' to everything, but pushed back, had opinions."*

Also on the X page: a **founder-as-case-study growth chart for Vitalii's own X account** — 355 followers (stalled) → 2,000+ by day 14 → ~9,600 by day 90 (97% of a 10K goal). ([twt.getstanley.ai](https://www.twt.getstanley.ai/))

**Positioning quotes from Dodonov:** ([Net Influencer](https://www.netinfluencer.com/stan-helped-creators-make-500m-selling-digital-products-its-biggest-lesson-was-that-products-arent-the-problem/), [PRNewswire](https://www.prnewswire.com/news-releases/stan-the-creator-platform-powering-80-000-active-users-launches-stanley-an-ai-head-of-content-for-linkedin-302716013.html))
> *"a head of content that lives in your pocket"* · *"the world's first prototype of an AI employee accessible to most people"*
> *"The problem we're solving is that people who are exceptional at what they do are often invisible online."*
> *"General-purpose tools average the voice of the internet… the output is going to be representative of the average, not what makes you uniquely you."*
> *"Our intention with Stanley is not to replace you in the content creation, but rather to amplify what makes you, and get you distribution."*

---

## 3. Tech stack & integrations

### 3.1 What's actually documented

- **Model:** started on **ChatGPT, switched to Claude on day 9** of the sprint. ([stan.store](https://stan.store/blog/how-we-built-stanley-linkedin/)) Marketing claims "always using the latest AI model."
- **Build method: "vibe coding"** — Dodonov built the backend in natural language without hand-writing code. This is the *narrative centerpiece* of the Business Insider essay and the blog post. ([stan.store](https://stan.store/blog/how-we-built-stanley-linkedin/), [Benzatine](https://benzatine.com/news-room/from-zero-to-50000-in-six-weeks-the-journey-of-a-toronto-creator-with-ai))
- **LinkedIn: scraping, not API.** The blog says they "built LinkedIn data scraping capabilities." Reviewers confirm the LinkedIn product only needs **a LinkedIn URL — no login, no extension, no OAuth**, which is consistent with scraping a public profile. AuthoredUp counts this as a *pro* ("no Terms of Service risks from automation") precisely because Stanley doesn't publish. ([stan.store](https://stan.store/blog/how-we-built-stanley-linkedin/), [ghostwriting-ai](https://www.ghostwriting-ai.com/comparisons/stanley-review), [AuthoredUp](https://authoredup.com/blog/stanley-review))
- **Delivery surfaces:** iMessage (shipped v1.37, May 12 2026), Telegram (@getstanley_bot), SMS shortcodes, iOS app, web. ([App Store](https://apps.apple.com/us/app/stanley-ai-head-of-content/id6754887783), [getstanley.ai](https://getstanley.ai/))
- **Features built in sprint:** post-history analysis, voice-to-text, image generation (photos, diagrams, comics, icons), analytics, profile analysis, and a deliberately theatrical **dynamic loading state showing the analysis in progress**. ([stan.store](https://stan.store/blog/how-we-built-stanley-linkedin/), [ghostart](https://ghostart.io/blog/is-stanley-ai-worth-149-a-month-honest-review))
- **Platform coverage claimed on the unified page:** YouTube, X, LinkedIn, Threads, Instagram, Substack. Threads repurposing was shipped later per John Hu's "shipped this week" post. ([getstanley.ai](https://getstanley.ai/), [John Hu on X](https://x.com/JayHoovy/status/2085712575023432010))
- **Billing:** Stripe and PayPal (per referral payouts); Apple IAP for the iOS app at $44.99/mo w/ 3-day trial. ([Stan help](https://help.stan.store/article/89-what-is-stans-referral-or-affiliate-program), [App Store](https://apps.apple.com/us/app/stanley-ai-head-of-content/id6754887783))

### 3.2 The integrations claim — important correction

The X landing page shows an integrations strip including **X, Zapier, Notion, Discord, Slack, Make, Telegram**. ([twt.getstanley.ai](https://www.twt.getstanley.ai/)) That's the only public integration list I found, and logo strips on Framer marketing pages are frequently aspirational rather than shipped.

**I found zero evidence of Fathom, Granola, Wispr Flow, or Google Drive integrations.** Every search for those terms alongside Stanley returned only unrelated pages about those products themselves. If the brief's source for that list was an in-chat conversation with the agent or a Telegram announcement, it isn't publicly documented. Carly independently flags this exact problem: *"Feature inconsistency: public descriptions vary across help center and app-store materials."* ([Carly](https://www.usecarly.com/blog/stanley-ai-review/))

### 3.3 Docs / changelog / jobs

- **Blog:** [stan.store/blog](https://stan.store/blog/stanley/) (Jordyn Kerr) — Stanley overview, the 14-day build story, Stanley Studio.
- **Help center:** help.stan.store — thin on Stanley; article 150 ("What Can Stanley Do For You?") describes an in-Stan-Store support assistant, a *different, older* Stanley than the content agent. ([help.stan.store/150](https://help.stan.store/article/150-what-can-stanley-do-for-you))
- **Changelog:** effectively the **iOS version history** (v1.37 iMessage, v1.52 Content Calendar, v1.56 perf) plus John Hu's weekly "everything we shipped this week" X posts. No dedicated changelog page.
- **Pricing page:** none. Pricing is deliberately absent from every getstanley.ai surface — consistent with the negotiate-in-chat model.
- **Job posts:** none found for Stan/Stanley. Dodonov's LinkedIn functions as the de-facto hiring board ("part hiring board" per Favikon).

---

## 4. Competitive landscape, 2026

### 4.1 LinkedIn ghostwriter/agent tools

| Tool | Price | What it does | Distribution tactic |
|---|---|---|---|
| **Stanley (LinkedIn)** | **$149/mo**, no trial, no free tier | Chat-based coach: Write / Analyze / Interview modes + analytics dashboard | Build-in-public, PR, founder cold email, Stan cross-sell |
| **Taplio** | $39 Starter (0 AI credits) / $69 Growth (250 credits) / $199 Pro (unlimited + lead DB) | AI posts, scheduling, 5M+ viral post library, lead gen | Heavy content SEO — runs its own "X alternatives" blog attacking every rival ([taplio.com/blog](https://taplio.com/blog/supergrow-alternatives)) |
| **Supergrow** | $19/mo Starter ($16 annual), $39 Pro ($31 annual), Teams $133/mo | Voice-trained AI, Content DNA, carousels, first-comment scheduler, **official LinkedIn API** | Programmatic SEO alternatives pages; leans hard on "API = safe" vs. extension tools ([supergrow.ai](https://www.supergrow.ai/blog/taplio-alternatives)) |
| **Kleo** | $99/mo flat, no tiers, no credit limits | Voice-trained AI + persistent knowledge base, image creator, scheduling, swipe-file extension; **LinkedIn + X** | Same playbook — published a "Stanley Review" hit piece ([kleo.so](https://www.kleo.so/blog/stanley-review)) |
| **AuthoredUp** | $19.95/mo ($16.63 annual), 14-day trial | Formatting/preview/analytics, 300+ hook templates. **No AI generation, no scheduling** | Also published a "Stanley Review" ([authoredup.com](https://authoredup.com/blog/stanley-review)) |
| **MagicPost** | $21/mo analytics, $39/mo creator | Claims "only official LinkedIn API-verified tool"; hooks generator, scheduling, watchlist | Published a "Stanley Review" ([magicpost.in](https://magicpost.in/blog/stanley-review)) |
| **Draftly** | Free (5 posts) / $19 Starter / $49 Pro; +$19 inbox, +$19 outreach add-ons | Posts, carousels, extension comments, brand voices, scheduling, LinkedIn outreach campaigns (**requires a Claude account** for AI Campaign) | Substack + freemium ([draftly.so/pricing](https://www.draftly.so/pricing)) |
| **EasyGen** | ~$59.99/mo ($49.99 annual) | Trained on "top 1% LinkedIn creator data," trend intel, voice dictation | Founder-brand (built by a 100M-view creator) |
| **Socialsonic** | $20/mo ($13.33 annual) | Trending-topic alerts + AI generation, gamified streaks | Price-leader positioning |
| **Bluecast** | $29/mo ($23 annual) | Repurposes YouTube/blogs/PDFs/audio → LinkedIn | Repurposing niche |
| **Postiv AI, CannerAI, Sona, ConnectSafely, Writio, Ghostart, Carly, Exeedin** | various | Mostly thin wrappers | **All of them exist primarily as SEO surfaces**; nearly every one has published a "Stanley review" |

### 4.2 X/Twitter tools

| Tool | Price | Notes |
|---|---|---|
| **Stanley for 𝕏** | Negotiated; "free to try, no card" | Ghostwriter-system framing, DM writing, reply-finding |
| **Tweet Hunter** | $29–$200/mo | Viral library + AI ghostwriting + lead tracking |
| **Typefully** | $8–$39/mo (Starter $12.50 / Creator $19 / Team $39) | Cross-platform: X, LinkedIn, Threads, Bluesky, Mastodon |
| **Postwise** | $37–$97/mo | "GhostWriter" style-matched tweets/threads/hooks |
| **Hypefury** | $29–$199/mo | ⚠️ **X support discontinued**; now Bluesky/Threads/LinkedIn/IG |
| **Buffer** | Free (3 ch) → $5–12/channel/mo | AI Assistant included on free plan |
| **Black Magic** | $7.99–$59.99/mo | Tweet analytics + private CRM |
| **Circleboom** | $24.99–$74.99/mo | Scheduling + fake-follower detection |
| **Hootsuite / Sprout Social** | $99–$249+ / $199–$499+ | Enterprise |
| **Castmagic** | Free (3 files) / $39 Starter (40h) / $99 Pro (100h) / $295 Business | Audio→content repurposing; Riverside/Zoom/YouTube/Spotify integrations |

Sources: [posteverywhere.ai](https://posteverywhere.ai/blog/25-best-ai-tools-for-x-twitter), [postiv.ai](https://postiv.ai/blog/taplio-alternatives), [supergrow.ai](https://www.supergrow.ai/blog/taplio-alternatives), [aisotools/Castmagic](https://aisotools.com/pricing/castmagic)

⚠️ **Pricing across these comparison blogs is mutually inconsistent** (Kleo is quoted at $49–79, $99, and $83.25/mo across three sources; Taplio at $39, $99+, and $199). Each is written by a competitor to make itself look cheap. Verify at source before citing.

### 4.3 Agent-native / open-source competitors — the real structural threat

This is the category that most directly undercuts Stanley's $149/mo, because it delivers the same "agent that posts for you" loop at near-zero marginal cost:

- **SocialClaw** ([getsocialclaw.com](https://getsocialclaw.com/), [GitHub](https://github.com/ndesv21/socialclaw)) — self-described "official social publishing layer for AI agents." **12+ networks** (IG, TikTok, X, LinkedIn, FB, YouTube, Reddit, Discord, Telegram, WordPress, Pinterest, Snapchat). Four integration paths: **MCP server for Claude Code, agent skill via `npx skills add ndesv21/socialclaw`, REST API, CLI.** Free tier.
- **sergebulaev/linkedin-skills** ([GitHub](https://github.com/sergebulaev/linkedin-skills)) — **MIT, 582 stars.** 11 Claude Code/Codex skills: Post Writer (20 hook formulas), Comment Drafter, Reply Handler, **Post Audit (checks drafts against algorithm rules *and AI-detection patterns*)**, **Humanizer (removes AI vocabulary and fingerprints)**, Hook Extractor, Content Planner, Engagement Monitor, Profile Optimizer, Employee Advocacy, Repurposer. Publishes via optional Publora integration.
- **langchain-ai/social-media-agent** ([GitHub](https://github.com/langchain-ai/social-media-agent)) — sourcing, curating, scheduling with human-in-the-loop.
- **Postiz** ([openclaw/linkedin](https://postiz.com/openclaw/linkedin)), **post-bridge** ([post-bridge.com/agents](https://www.post-bridge.com/agents)), **Posta skill** ([GitHub](https://github.com/STGime/posta-skill)), **LocoreMind/locoagent** (browser-automation posting).
- Skill directories now index this category: [ClaudSkills](https://claudskills.com/use-case/social-media/), [SkillsLLM](https://skillsllm.com/skill/linkedin-skills), [PostFast](https://postfa.st/blog/best-openclaw-skills-for-social-media-marketing).

The "AI chief of staff" adjacent category is also crowding in — Product Hunt now has [a dedicated AI Chief of Staff category](https://www.producthunt.com/categories/ai-chief-of-staff), and roundups from [Vellum](https://www.vellum.ai/blog/best-ai-employees), [Saner](https://blog.saner.ai/best-ai-chief-of-staff/), and [Alfred](https://get-alfred.ai/blog/best-ai-chief-of-staff-tools) treat "AI employee" as a settled product noun. Stanley's "world's first AI employee accessible to most people" claim has a short shelf life.

---

## 5. Criticism

### 5.1 First-party user complaints (App Store, the most credible source)

Rating is strong overall — **4.6–4.7 from ~451–455 ratings** — but the negative reviews cluster on three specific, repeated failures: ([App Store reviews](https://apps.apple.com/us/app/stanley-ai-head-of-content/id6754887783?see-all=reviews&platform=iphone))

**Memory loss — the most damaging, because "infinite memory" is a headline marketing claim:**
> *"When it works it's great but it's incredibly glitchy. Freezes constantly and even in the same thread can't remember things that have been said."* — Hklompmaker, 2★, Mar 12
> *"Complete waste of money. Repetitive suggestions... a complete inability to recall literally anything, even things from just a few lines prior."* — Rhondagreene, 2★, Jun 13

**Broken data sync:**
> *"This app is $47 a month for something that's glitchy and inaccurate. It's supposed to be synced to your IG, but it says things like 'you haven't posted in a week' even if you posted every day."* — mslo781, 1★, Mar 25

**Billing / cancellation — the most serious:**
> *"There is absolutely no way to cancel a subscription... they force you into continuing... no customer service."* — Jalisa review, 1★, Mar 16

**Value vs. free alternatives:** *"ChatGPT is free and does everything this does."* — mslo781

### 5.2 Third-party review criticism

Caveat first: **almost every "Stanley review" on the open web is published by a direct competitor** (Kleo, AuthoredUp, MagicPost, Carly, Ghostart, ghostwriting-ai). Their conclusions are motivated. That said, several independent findings recur across all of them, which raises confidence:

- **It coaches, it doesn't execute.** *"Stanley coaches, Oiti writes"* — *"even inside the paid tool, Stanley coaches more than it writes."* The paid drafting editor reportedly produced **generic templates** and the analysis *"simply reflected users' own posts back to them."* ([ghostwriting-ai](https://www.ghostwriting-ai.com/comparisons/stanley-review))
- **No scheduling or publishing** on the LinkedIn product — confirmed independently by Kleo, AuthoredUp, and MagicPost. Also no Chrome extension, no formatting tools (bold/italic/bullets), no company pages, no drafts panel, no hooks library, no data export. ([Kleo](https://www.kleo.so/blog/stanley-review), [AuthoredUp](https://authoredup.com/blog/stanley-review), [MagicPost](https://magicpost.in/blog/stanley-review))
- **Analytics start at signup** — no historical archive import. ([AuthoredUp](https://authoredup.com/blog/stanley-review))
- **Fully paywalled with no preview.** *"Users cannot run a single prompt without an active subscription"* at $149/mo. ([MagicPost](https://magicpost.in/blog/stanley-review))
- **Onboarding hangs.** *"Can get stuck in a permanent loading state"* on profiles with long post histories, requiring repeated chat restarts. ([MagicPost](https://magicpost.in/blog/stanley-review))
- **Data-access concerns:** requires connecting social accounts *"with sensitive permissions."* ([Carly](https://www.usecarly.com/blog/stanley-ai-review/))
- **Two products, two bills.** IG and LinkedIn are separate subscriptions, not channels in one plan — a common purchase surprise. ([Carly](https://www.usecarly.com/blog/stanley-pricing/))
- **Documentation inconsistency:** *"Public descriptions vary across help center and app-store materials."* ([Carly](https://www.usecarly.com/blog/stanley-ai-review/))
- On Stanley for 𝕏 specifically: risk of generic output if under-tuned, no deep analytics integration, no competitor content analysis. ([FunBlocks](https://www.funblocks.net/aitools/reviews/stanley-for-x))

### 5.3 The category-level risk — the biggest one

**LinkedIn began actively suppressing AI-generated content on May 20, 2026.** The platform uses an ML classifier trained on human-annotated examples to detect "AI slop" — generic posts lacking original perspective, including the "it's not X, it's Y" construction and summarize-only bot comments — claiming **94% accuracy** (false-positive rate undisclosed). Flagged posts stay visible to direct connections but are **suppressed in the broader recommendation feed**. LinkedIn explicitly permits AI-*assisted* content with original insight; what's penalized is AI substituting for human thinking. ([Neil Patel](https://neilpatel.com/blog/linkedin-ai-slop-crackdown-content-strategy/))

This is an existential problem for the whole category and it lands hardest on the highest-volume, most-templated tools. Stanley's coach-rather-than-writer posture is arguably *less* exposed than Taplio's viral-library-remix model — but its entire pitch is that it drafts in your voice at scale.

Related coverage: [Hiration on the 2026 AI-slop backlash](https://www.hiration.com/blog/ai-slop-linkedin/), [Boston Institute of Analytics on "exposing fake experts"](https://bostoninstituteofanalytics.org/blog/linkedin-ai-slop-crackdown-exposing-fake-experts-2026/), and an entire competitor positioning itself as [tools "that aren't AI slop"](https://www.ghostwriting-ai.com/comparisons/best-linkedin-ai-tools-that-arent-ai-slop).

Stanley's own X landing page anticipates this — one of its six FAQs is literally *"What if my audience finds out I use AI?"* — but the answer text is loaded dynamically and I could not extract it. ([twt.getstanley.ai](https://www.twt.getstanley.ai/))

### 5.4 Parent-company reputational spillover

Stan Store itself carries a mixed review profile (["Is Stan Store Legit"](https://crevio.co/blog/is-stan-store-legit), ["when to walk away"](https://www.group.app/blog/stan-store-review/), [Trustpilot](https://ca.trustpilot.com/review/stan.store)), and the 13% monthly churn Dodonov disclosed to Sacra is high. Since Stanley is sold into that same base and bills through the same infrastructure, cancellation friction complaints are likely to compound.

---

## 6. Assessment

**The genuinely replicable thing here is the distribution, not the product.** Stanley's technology is a Claude wrapper over LinkedIn scraping, built in 14 days by a non-specialist using natural language. What produced $200K on day one was: a founder with an existing 22K-follower LinkedIn audience, 17 build-in-public posts creating a launch-day audience, hyper-personalized cold email to a dozen creators with 100K+ audiences each, an installed base of 80,000 creators to cross-sell into, and PR built around single dramatic numbers. Every one of those is a distribution asset, not a technical one.

**The product's public reception is bifurcated.** 4.7 stars with 450+ ratings is real traction. But the negative reviews attack precisely the two things the marketing promises loudest — "infinite memory" and account sync — and the independent-ish reviews converge on the same verdict: it's a $149/mo coach in a market where $19–49/mo tools also schedule and publish.

**Three specific gaps in the public record you may want to chase differently:** the $10–100 negotiated pricing band, the $500/post pay-per-view mention program, and the Fathom/Granola/Wispr Flow integrations are all *absent from every indexed public source*. If those are real, they live in Telegram/iMessage conversations, in-product offers, or gated creator communities. The way to verify is to text the bot (+1 646 382-4202 / @getstanley_bot) and transcribe what it offers — that's a primary source no amount of web search will substitute for. Similarly, the Product Hunt launch video and the X launch threads are behind robots.txt for automated fetching; a browser session would get them.

---

## Sources

**Stanley / Stan primary**
- [getstanley.ai](https://getstanley.ai/) · [getstanley.ai/welcome](https://www.getstanley.ai/welcome) · [x.getstanley.ai](https://x.getstanley.ai/) · [twt.getstanley.ai](https://www.twt.getstanley.ai/)
- [stan.store/blog/how-we-built-stanley-linkedin](https://stan.store/blog/how-we-built-stanley-linkedin/) · [stan.store/blog/stanley](https://stan.store/blog/stanley/) · [stan.store/blog/stanley-studio](https://stan.store/blog/stanley-studio/)
- [help.stan.store — referral program](https://help.stan.store/article/89-what-is-stans-referral-or-affiliate-program) · [Ambassador Program](https://help.stan.store/article/225-stan-ambassador-program) · [referral category](https://help.stan.store/category/321-referral-program) · [What Can Stanley Do For You](https://help.stan.store/article/150-what-can-stanley-do-for-you)
- [App Store — Stanley: AI Head of Content](https://apps.apple.com/us/app/stanley-ai-head-of-content/id6754887783) · [reviews](https://apps.apple.com/us/app/stanley-ai-head-of-content/id6754887783?see-all=reviews&platform=iphone)
- [Product Hunt — Stanley For 𝕏](https://www.producthunt.com/products/stanley-for-x) · [awards](https://www.producthunt.com/products/stanley-for-x/awards)
- [X — @stanleybystan](https://x.com/stanleybystan) · [@JayHoovy launch post](https://x.com/JayHoovy/status/2082872226517307471) · [@JayHoovy shipping post](https://x.com/JayHoovy/status/2085712575023432010) · [@vitaliidodonov](https://x.com/vitaliidodonov)

**Press & company data**
- [PRNewswire — Stanley for LinkedIn (Mar 17 2026)](https://www.prnewswire.com/news-releases/stan-the-creator-platform-powering-80-000-active-users-launches-stanley-an-ai-head-of-content-for-linkedin-302716013.html) · [TMCnet syndication](https://www.tmcnet.com/usubmit/2026/03/17/10349343.htm)
- [PRNewswire — Stanley for Instagram (Apr 2 2026)](https://www.prnewswire.com/news-releases/stanley-for-instagram-drives-20m-views-from-one-video-helps-creator-gain-80k-followers-302732526.html) · [Yahoo Finance](https://finance.yahoo.com/sectors/technology/articles/stanley-instagram-drives-20m-views-130000821.html) · [Dealroom](https://app.dealroom.co/news/feed/stan-launches-stanley-an-ai-head-of-content-for-linkedin-to-help-80-000-creators-build-personal-brands)
- [Sacra — Stan company profile](https://sacra.com/c/stan/) · [Sacra — Dodonov interview](https://sacra.com/research/vitalii-dodonov-stan-creator-aligned-store-in-bio/) · [Crunchbase](https://www.crunchbase.com/organization/stan-9644)
- [Indie Hackers — $30M ARR in three years](https://www.indiehackers.com/post/tech/going-all-in-and-hitting-30m-arr-in-three-years-IBwjFYRHPn5joh0Qm17J)
- [StartWell Podcast — Dodonov](https://startwell.co/blogs/insights/stans-co-founder-killed-his-own-revenue-line-on-purpose-vitalii-dodonov) · [Mike Wystrach podcast](https://mikewystrach.com/podcast/vitalii-dodonov) · [Canadian Business](https://canadianbusiness.com/people/vitalii-dodonov-stan/) · [BrainStation](https://brainstation.io/events/leadership/creators-of-toronto-20260303) · [Forbes Councils](https://councils.forbes.com/profile/Vitalii-Dodonov-Co-Founder-Stan/0a3f33b3-a74a-44ac-a00c-4aba2ab2004c)
- [Net Influencer](https://www.netinfluencer.com/stan-helped-creators-make-500m-selling-digital-products-its-biggest-lesson-was-that-products-arent-the-problem/) · [Let's Data Science](https://letsdatascience.com/news/founder-builds-stanley-and-hits-50000-in-revenue-566e8b41) · [Benzatine](https://benzatine.com/news-room/from-zero-to-50000-in-six-weeks-the-journey-of-a-toronto-creator-with-ai) · [MSN/Business Insider essay](https://www.msn.com/en-us/money/other/i-built-an-ai-content-tool-for-creators-that-hit-50-000-in-revenue-in-6-weeks-here-s-what-it-takes-to-vibe-code-successfully/ar-AA24luOZ) · [Favikon](https://www.favikon.com/blog/who-is-vitalii-dodonov)

**Reviews & criticism (mostly competitor-authored — read accordingly)**
- [Kleo](https://www.kleo.so/blog/stanley-review) · [AuthoredUp](https://authoredup.com/blog/stanley-review) · [MagicPost](https://magicpost.in/blog/stanley-review) · [Carly review](https://www.usecarly.com/blog/stanley-ai-review/) · [Carly pricing](https://www.usecarly.com/blog/stanley-pricing/) · [Ghostart](https://ghostart.io/blog/is-stanley-ai-worth-149-a-month-honest-review) · [ghostwriting-ai](https://www.ghostwriting-ai.com/comparisons/stanley-review) · [FunBlocks (X product)](https://www.funblocks.net/aitools/reviews/stanley-for-x) · [HuntScreens](https://huntscreens.com/products/stanley-for)

**Competitors & category**
- [Postiv — Taplio alternatives](https://postiv.ai/blog/taplio-alternatives) · [Supergrow — Taplio alternatives](https://www.supergrow.ai/blog/taplio-alternatives) · [Taplio — Supergrow alternatives](https://taplio.com/blog/supergrow-alternatives) · [Kleo — Taplio alternatives](https://www.kleo.so/blog/taplio-alternatives)
- [PostEverywhere — 27 best AI tools for X](https://posteverywhere.ai/blog/25-best-ai-tools-for-x-twitter) · [Draftly pricing](https://www.draftly.so/pricing) · [Castmagic pricing](https://aisotools.com/pricing/castmagic)
- [SocialClaw](https://getsocialclaw.com/) · [ndesv21/socialclaw](https://github.com/ndesv21/socialclaw) · [sergebulaev/linkedin-skills](https://github.com/sergebulaev/linkedin-skills) · [langchain-ai/social-media-agent](https://github.com/langchain-ai/social-media-agent) · [STGime/posta-skill](https://github.com/STGime/posta-skill) · [Postiz OpenClaw](https://postiz.com/openclaw/linkedin) · [post-bridge](https://www.post-bridge.com/agents) · [ClaudSkills](https://claudskills.com/use-case/social-media/) · [SkillsLLM](https://skillsllm.com/skill/linkedin-skills) · [PostFast](https://postfa.st/blog/best-openclaw-skills-for-social-media-marketing)
- [Product Hunt — AI Chief of Staff category](https://www.producthunt.com/categories/ai-chief-of-staff) · [Vellum — best AI employees](https://www.vellum.ai/blog/best-ai-employees) · [Saner — AI chief of staff](https://blog.saner.ai/best-ai-chief-of-staff/) · [Alfred](https://get-alfred.ai/blog/best-ai-chief-of-staff-tools)

**AI-slop / platform risk**
- [Neil Patel — LinkedIn AI slop crackdown](https://neilpatel.com/blog/linkedin-ai-slop-crackdown-content-strategy/) · [Hiration](https://www.hiration.com/blog/ai-slop-linkedin/) · [Boston Institute of Analytics](https://bostoninstituteofanalytics.org/blog/linkedin-ai-slop-crackdown-exposing-fake-experts-2026/) · [ghostwriting-ai — tools that aren't AI slop](https://www.ghostwriting-ai.com/comparisons/best-linkedin-ai-tools-that-arent-ai-slop)

**Stan parent-company reviews**
- [Crevio](https://crevio.co/blog/is-stan-store-legit) · [Group.app](https://www.group.app/blog/stan-store-review/) · [LinoDash](https://linodash.com/stan-store-review/) · [Trustpilot](https://ca.trustpilot.com/review/stan.store)
