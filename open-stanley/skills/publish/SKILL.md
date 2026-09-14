---
name: publish
description: Post or schedule an approved draft to LinkedIn and/or X through the user's own logged-in browser (or a posting MCP such as SocialClaw/Postiz/X API if they have one), including X threads, first-comment links, and LinkedIn's native scheduler, then record the live URL in the vault ledger. Use when the user says "post it", "publish", "schedule for Thursday 10am", "put this on both", or "post the X version too".
---

# Publish

Only ever with text the user approved verbatim (or a lane marked `autonomous: true` in `strategy.md`). Publishing is the one irreversible step; do it carefully and record it.

## 1. Choose the adapter

Writing on the user's own behalf has an official path on both platforms, and the browser is the fallback — not the other way round. Full table, with what is and is not self-serve, in `../stanley/references/platform-access.md`; read it before you automate a platform this skill does not already cover. `my-human.md` records the decision per platform as `post_path:`, so check there first and do not re-derive it every run.

1. **A connected MCP that covers this platform** (`post` capability, or the official X MCP at `api.x.com/mcp` — it posts, replies, and publishes Articles; the free X tier covers writes). Confirm it returns a URL.
2. **An official first-party API the user has set up**: on LinkedIn, a developer app with the `w_member_social` scope posts, comments and likes as the authenticated member, self-serve and free. If they have not set one up, offer it once, and keep going with the browser meanwhile.
3. **Browser** (the user's own logged-in session) — the fallback, and the only path for anything the official surfaces do not cover. Post at human pace: one action, a real pause, never a burst. A four-tweet X thread posted through the browser on 12 Sep 2026 was followed by a suspension the next day; unproven as cause, but the reason writes prefer the official path.
4. Otherwise: hand the final text back formatted for copy-paste and say why you couldn't post.

Record which path you used in the ledger row (`--via mcp|api|browser`) so a later suspension or rate-limit has something to correlate against.

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
