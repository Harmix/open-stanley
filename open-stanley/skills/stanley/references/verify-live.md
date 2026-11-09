# Verify a post or comment is live before saying so

On 2026-11-08 a run told the user "your comment is posted" when it was not. The check searched the page text for the comment, and the page text included the comment box, where the unsent text was still sitting. The user looked and saw nothing.

The rule: nothing is reported as posted, and nothing goes into the ledger as posted, until the page has been reloaded and the text is found outside every editor, under the user's name.

1. Before you press Comment or Post, read the count ("8 comments") if the page shows one.
2. Press the button, wait 3 seconds, then reload the post's own URL (not the feed) and wait for it to load. On LinkedIn, if the comment is not in "Most relevant", switch the comments to "Most recent".
3. Run this with the javascript tool. Set `TEXT` to the first ~60 characters you posted and `NAME` to the user's display name from `my-human.md`:

```js
const TEXT = "<first ~60 characters>"; const NAME = "<display name>";
const norm = s => (s || '').replace(/\s+/g, ' ').toLowerCase();
const t = norm(TEXT).slice(0, 60);
const inEditor = [...document.querySelectorAll('[contenteditable=true],textarea')].some(e => norm(e.innerText || e.value).includes(t));
const hits = [...document.querySelectorAll('article,li,section,div')].filter(e =>
  !e.closest('[contenteditable=true]') && !e.querySelector('[contenteditable=true],textarea') &&
  norm(e.innerText).includes(t) && e.innerText.includes(NAME));
JSON.stringify({ saved: hits.length > 0, stillInEditor: inEditor });
```

4. Live only when `saved` is true and `stillInEditor` is false. A plain search of `document.body.innerText` is not a check: in the 2026-11-08 test it found unsent text in the box and said yes.
5. If it is not live: say so, try once more, verify again. Never write "posted" on a guess.
6. Record what you saw in the ledger: `comment-add ... --verified "reloaded, found under <name>, comments 8 -> 9"`, or `post-add ... --via publish --verified "reloaded <url>, first line found under <name>"`. The script refuses a posted comment or a `--via publish` post without `--verified`.

Tested 2026-11-08 on a LinkedIn post: a saved comment gave `saved: true`, and text typed in the box but not sent gave `saved: false, stillInEditor: true`.
