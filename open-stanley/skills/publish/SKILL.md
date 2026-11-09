---
name: publish
description: Post or schedule an approved draft to LinkedIn and/or X through the user's own logged-in browser (or a posting MCP such as SocialClaw/Postiz/X API if they have one), including X threads, first-comment links, and LinkedIn's native scheduler, then record the live URL in the vault ledger. Use when the user says "post it", "publish", "schedule for Thursday 10am", "put this on both", or "post the X version too".
---

# Publish

Only ever with text the user approved verbatim (or a lane marked `autonomous: true` in `strategy.md`). Publishing is the one irreversible step; do it carefully and record it.

## 1. Choose the adapter

1. **An MCP the user already has connected** for this platform (`post` capability, or an official one they set up such as X's hosted MCP at `api.x.com/mcp`). Confirm it returns a URL.
2. **Browser** (the user's own logged-in session). Correct for everything at this volume — a post or two a day is a person using their account, not automation worth routing around. Post at human pace and space the parts of a thread: an X thread on 12 Sep 2026 went out as four writes in about two minutes and the account was suspended the next day. Cause unknown, but velocity is the part worth not repeating.
3. Otherwise: hand the final text back formatted for copy-paste and say why you couldn't post.

`my-human.md` records `post_path:` per platform; check it rather than re-deriving. Official APIs exist for writing on both platforms and are in `../stanley/references/platform-access.md` — mention one once if the user hits a limit or asks, never as a prerequisite. Record which path you used in the ledger row (`--via mcp|browser`).

## 2. LinkedIn via browser

Open linkedin.com/feed → Start a post. The composer is a ProseMirror/tiptap editor (since autumn 2026): a plain-text paste drops the blank lines between paragraphs, so insert the text as HTML, one `<p>` per line and `<p><br></p>` for each blank line (`clipboardData` with `text/html`, or set the editor's content through the javascript tool), then read the composer back and compare paragraph by paragraph with the draft before anything else. LinkedIn collapses double spaces.

Image first, text second. Before any upload, `stanley-vault image-clean <file>`: a PNG rendered in a cloud sandbox carries a C2PA manifest ("made by Claude"), and LinkedIn turns that into a "Content credentials" label on the post; the command strips it (and EXIF/XMP) in place and says whether it found one. Then click "Photo", `file_upload` on `input[type=file]`, Next, then insert the text; the draft names its asset in `drafts/<file>.assets`. A scheduled post can be edited later to add a photo and tag people in it.

Picking the slot when the user says "schedule it" without a time: the cadence in `strategy.md` sets how many this week; `../stanley/references/research-linkedin-2026.md` sets the day (insight-type posts peak Tue–Wed, the morning window in `my-human.md`'s platform notes sets the hour); keep posts at least 18 hours apart and never two on one day. Say which rule put a post where. For scheduling, use LinkedIn's clock icon and set the time from the user's request in their time zone. After "Post schedule updated", open the scheduled post once and confirm text, image and tags are all there. Do not save a scheduled post from an "Edit post" view that shows the text without its image: that view sometimes loads without the media and saving it drops the photo; close it and reopen.

Post. Read back the post URL from the "View post" toast or the profile activity page. If a link belongs in the first comment, add it now.

## 3. X via browser

Compose. Without Premium, post the thread: tweet 1, then reply with tweet 2… (the `---` blocks from the draft), each ≤280 chars; verify the count before each. With Premium, a single long post. Links in the first reply. Read back the status URL.

## 3b. Any other platform with a web composer (Threads, Substack Notes, Bluesky, Mastodon, Instagram captions)

The browser adapter is not LinkedIn-specific. For a platform the user asks for and is logged into: open its composer (threads.com → new thread; substack.com/notes → "Write a note"; bsky.app → new post; Mastodon instance → compose), insert the text the way section 2 does for a rich-text editor and section 3 for a plain one, respect the platform's limit (Threads 500 characters per post and chains; Notes no hard cap but short wins; Bluesky 300 graphemes), attach the image first if there is one, post, and read back the URL from the post's own page or the profile feed. Record it with `post-add --platform <name>` (any lowercase name works; `recap` reads metrics only where it knows the analytics page, so for a new platform record impressions by hand from the post page or leave them empty). Instagram's composer needs an image or video and a business account for scheduling; post the caption with the media the user gives you, never a generated image. First time on a new platform: write the composer steps and the limit into `my-human.md` under `post_path:` so the next run does not rediscover them.

## 4. Record and follow up

- Before anything else here: reload the live post and check it per `../stanley/references/verify-live.md`. Say "posted" only after that, and pass what you saw as `--verified` (with `--via publish` the script refuses without it).
- `skills/stanley/scripts/stanley-vault post-add --platform <p> --url <url> --text-file <final> --story <slug>… --lane <lane> --shape opener:<x> --shape ending:<y> [--experiment <name>=<variant>]` for each platform. The tags are what make `recap` and `stanley-stats` able to say which shapes and lanes work for this audience.
- A scheduled post has no URL yet: set `status: scheduled` and `scheduled_for: <ISO local time>` in the draft's `.meta.json` and stop there; `recap` picks it up with `stanley-vault drafts-due` once the time has passed and adds the ledger row with `post-add --from-meta … --via reconciled` when it finds the live post.
- If a draft→final diff exists, make sure it was stored (`diff-add`).
- Tell the user both URLs in two lines and one thing to do in the next hour: reply to the first comments (largest ranking weight on both platforms). If `recap` is scheduled, note the post for the 1h/24h/7d metric pulls.
- Mark the story `status: used` and rebuild the index (`post-add` flips it when it knows the slug).
- Series: a post that continues an earlier one gets a first comment "How this started: <first post>" when it goes live, and the previous post gets a comment "Next update: <new post>" (LinkedIn refuses an edit that adds a URL to a published post, and a URL in the body kills reach). A scheduled post has no URL until it is live, so when the user cannot be there at posting time, create a one-time scheduled task for ~20 minutes after the slot that finds the live URL, checks the comment is not already there, posts both comments, records the post (`post-add --from-meta`), and reports in one line; the user's browser must be open and logged in for it.
- Images: a real photo from the user or a screenshot of the real thing (the confirmation email, the dashboard, the message), private names blacked out, beats a rendered card; the first real user called the cards "AI slop" after three weeks. Render a card only when nothing real exists, and say so. Never name or tag the other party of a private conversation.

## 5. Failure modes to handle explicitly

- Character limit exceeded on X: ask trim vs thread; don't decide silently.
- LinkedIn "posted" but no URL: open the profile's recent-activity page and take the top post's URL; verify the first line matches.
- Duplicate: if the ledger already has a post with the same hook in the last 30 days, stop and ask.
- Remote run with no browser and no posting MCP: deliver the text to the user's `notify` channel with "ready to paste", and log the run as partial.
