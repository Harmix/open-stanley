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
