# Design notes for the website

Reference: midjourney.com/home, measured on 6 Nov 2026. Copy the structure, not the pixels.

What was measured there: background rgb(13,14,18); the hero is a canvas 77% of the viewport high; one 768px column; JetBrains Mono for headings (30px, regular weight) and body (16px/26px, grey-blue); DM Sans only on buttons; buttons are 9999px pills with a 20% tinted background, a coloured line icon and bold 14px text; each section heading has a 32px icon of its own colour sitting left of the column; a wordmark drawn as an outline, not a fill; almost no glow anywhere.

Ban list (from the AI-design tells collected in Nov 2026: the ux-skill wiki, the Fountain Institute's seven tells, the Show HN scoring post, 925 Studios):
- three equal cards in a row; identical rounded panels; stat tiles with round numbers
- glow on cards, buttons or body text; gradient heroes; purple-to-blue gradients; glassmorphism everywhere
- a centred hero with everything stacked and two CTAs of equal weight; a full-viewport hero on mobile
- decorative floating shapes; grid backgrounds as decoration
- filler verbs (empower, unlock, leverage, transform), slogans without a sentence after them, "Why choose us"
- em dashes, rule-of-three lists, Title Case, emoji in headings
- stock photos, AI-generated images, placeholder testimonials

What the site uses instead: a canvas that shows the material the plugin reads; the founder's real analytics screenshot; first-person copy in short sentences; lists with a border line between rows; one table. Every claim on the page is listed in `open-stanley/docs/claims.yml` and tested.

## Subpages follow the landing page, nothing else

Teardowns (`docs/creators/`), the comparison pages (`docs/compare/`) and the browser audit (`docs/audit.html`) use only the landing page's elements: the Jekyll `default` layout, a `##` heading with a coloured line icon in front of it, `img class="shot"` for real screenshots, `ul class="rows"` for small comparisons, plain tables, `pre` for command output, pill links. First person, short sentences, no em dashes, no middle dots joining facts anywhere (not under a title, not in a count line, not in a label), no legends with coloured bullets, no stat tiles, no cards, no coloured badges of their own. A test (`tests/test_claims.py`) checks that every `##` heading on a subpage carries an icon and that no page in `docs/` contains an em dash. Render a new page at desktop and phone width and look at it before committing.

## Learned from aisdr.com (8 Nov 2026)

What they do that we copied: a footer with link columns (Product, Why us, Helpful info, Legal) so every page is one click from every other and search engines see the whole site from any page; a "Still deciding? Let AI make the case" block with Ask ChatGPT, Ask Claude, Ask Grok buttons that open the model with a prompt about the product (we send the model to the README and the compare pages, and the prompt asks for the trade-offs); brand icons on those buttons (we load Anthropic, Cursor and Perplexity marks from Simple Icons; OpenAI's mark is not available there, so ChatGPT gets a line icon). What they do that we did not: a demo form in the footer, award badges, a "What is X?" page separate from the home page, an "Is X a fit for me?" page, case studies. The last two are worth a page each once there are users to write about.
