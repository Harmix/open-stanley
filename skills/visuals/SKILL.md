---
name: visuals
description: Make the images that go with content — a feed-accurate preview card of a draft (LinkedIn or X, fold marked) so the user reviews the real thing, a simple chart from the user's own numbers, a PDF carousel for LinkedIn documents, a screenshot of a source, or an image via any image-generation MCP the user has. Use when the user asks "show me how it will look", "make a visual for this", "turn these numbers into a chart", "make a carousel", or when write hands over a draft (a preview is always attached).
---

# Visuals

What the paid product actually does for visuals, from a month of its messages: it renders every draft as a feed mockup card (that is the "Edit this draft" image), it sends a daily stat card ("Today, 131 saw my content and 2 reacted"), an orbit graph of engagers, and static mascot illustrations for rituals. It does not generate post imagery. Everything it does here is reproducible; a few things can be done better.

## 1. Preview cards (always)

`skills/stanley/scripts/stanley-preview <draft> --platform linkedin|x --out drafts/<slug>.png --name "…" --headline "…" --handle … [--avatar path]`

Renders the post as it will appear, with the LinkedIn "…more" fold marked at ~210 characters and per-tweet counts for X threads (over-limit tweets in red). Attach the PNG whenever you hand over a draft; the fold line is what makes people fix the hook. If Playwright isn't available, the script writes the HTML next to the PNG path; open it with a browser tool and screenshot it.

## 2. Charts from the user's numbers

Only from receipts in `stories/` or `ledger/`. For a chart the reader will see on a phone: one series, a title that states the claim ("Overlap in our top-5 picks: 2.0/5 in the status sync, 3.0/5 in the R&D review"), no legend if one series, axis labels with units, 1200×675 or 1080×1080. Use matplotlib via a `scripts/` call (the `dataviz` skill in Claude sets palette and marks; follow it when present). Never chart a number the post doesn't state.

## 3. Documents (LinkedIn carousels)

When a story is a how-to or a list of steps with a result, a native document (PDF, 5–10 pages, one idea per page, 1080×1350) outperforms text on engagement rate. Build with the `pdf` skill or a headless-browser render of simple HTML pages; the first page is the hook, the last page is the claim, no CTA page. Keep the post text short and let the document carry the steps.

## 4. Screenshots as evidence

A screenshot of the source (the dashboard number, the email, the paper's abstract with date visible) is the strongest specificity move in the creators studied (Zaremba posts his own inbox). Take it with the browser tool, crop to the fact, redact anything under the user's private line (`my-human.md`), save to `drafts/<slug>.assets/`.

## 5. Generated imagery

Only if the user has an image-generation MCP connected (probe: tool names with `image`, `generate`, `imagen`, `dall`). Use it for the rare illustrative post the user asks for, never as a default; the 2026 feeds treat generic AI imagery like generic AI text. Prefer a real photo the user has (`inbox/`) over a generated one.

## 6. Recap and orbit cards (optional)

For users who like the daily card: `stanley-preview` HTML templates can be extended (`scripts/` accepts a `--template` in a future version). The plugin's default recap is text; a card is decoration.

## Rules

- No stock imagery, no text-heavy quote cards, no "AI-generated" look.
- Every visual maps to a receipt or to the draft itself.
- Save assets next to the draft so `publish` attaches the right file.
