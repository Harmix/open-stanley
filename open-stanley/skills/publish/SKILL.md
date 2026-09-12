---
name: publish
description: Post or schedule an approved draft to LinkedIn and/or X through the user's own logged-in browser (or a posting MCP such as SocialClaw/Postiz/X API if they have one), including X threads, first-comment links, and LinkedIn's native scheduler, then record the live URL in the vault ledger. Use when the user says "post it", "publish", "schedule for Thursday 10am", "put this on both", or "post the X version too".
---

# Publish

Only ever with text the user approved verbatim (or a lane marked `autonomous: true` in `strategy.md`). Publishing is the one irreversible step; do it carefully and record it.

## 1. Choose the adapter

1. **Browser** (default; the user's own session). Safest for both platforms: LinkedIn has no public posting API for individuals, and X's API blocks replies/quotes to non-mentioning accounts and draws automation scrutiny.
2. **Posting MCP** if present (`post` capability): use it when the user asked for it or the browser is unavailable (remote scheduled runs usually have no browser). Confirm the MCP returns a URL.
3. Otherwise: hand the final text back formatted for copy-paste and say why you couldn't post.

## 2. LinkedIn via browser

Open linkedin.com/feed → Start a post. Paste the text exactly (preserve blank lines; LinkedIn collapses double spaces). Attach an image/document if the draft names one in `drafts/<file>.assets`. For scheduling, use LinkedIn's clock icon and set the time from the user's request in their time zone. Post. Read back the post URL from the "View post" toast or the profile activity page. If a link belongs in the first comment, add it now.

## 3. X via browser

Compose. Without Premium, post the thread: tweet 1, then reply with tweet 2… (the `---` blocks from the draft), each ≤280 chars; verify the count before each. With Premium, a single long post. Links in the first reply. Read back the status URL.

## 4. Record and follow up

- `skills/stanley/scripts/stanley-vault post-add --platform <p> --url <url> --text-file <final> --story <slug>… --lane <lane> --shape opener:<x> --shape ending:<y> [--experiment <name>=<variant>]` for each platform. The tags are what make `recap` and `stanley-stats` able to say which shapes and lanes work for this audience.
- If a draft→final diff exists, make sure it was stored (`diff-add`).
- Tell the user both URLs in two lines and one thing to do in the next hour: reply to the first comments (largest ranking weight on both platforms). If `recap` is scheduled, note the post for the 1h/24h/7d metric pulls.
- Mark the story `status: used` and rebuild the index.

## 5. Failure modes to handle explicitly

- Character limit exceeded on X: ask trim vs thread; don't decide silently.
- LinkedIn "posted" but no URL: open the profile's recent-activity page and take the top post's URL; verify the first line matches.
- Duplicate: if the ledger already has a post with the same hook in the last 30 days, stop and ask.
- Remote run with no browser and no posting MCP: deliver the text to the user's `notify` channel with "ready to paste", and log the run as partial.
