# Getting the real link of a LinkedIn post

Since autumn 2026 the LinkedIn feed, search results and activity pages carry no post URNs and no post links in the page: `urn:li:activity` appears only inside comment ids, and the first URN after a post's text can belong to the next post. Guessing from those gave wrong links twice. Never build or guess a post URL. Read it from LinkedIn's own "Copy link to post" action.

What works (tested 8 Nov 2026 on the home feed and on an activity page): replace the clipboard write with a recorder, then press "Copy link to post" in each post's menu. Run this with the javascript tool on the page you are reading, after it has loaded (scroll first if you want more posts):

```js
window.__copied = [];
navigator.clipboard.writeText = (t) => { window.__copied.push(String(t)); return Promise.resolve(); };
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
const out = [];
for (const b of document.querySelectorAll('button[aria-label^="Open control menu for post by"]')) {
  const before = window.__copied.length;
  b.click(); await sleep(900);
  const item = [...document.querySelectorAll('[role=menuitem],[role=button],button,div,span')]
    .filter(e => /^Copy link to post$/i.test((e.innerText || '').trim())).pop();
  if (item) { item.click(); await sleep(700); }
  document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', bubbles: true }));
  await sleep(300);
  out.push({ author: b.getAttribute('aria-label').replace('Open control menu for post by ', ''),
             url: window.__copied.length > before ? window.__copied.at(-1).split('?')[0] : null });
}
JSON.stringify(out);
```

- Strip the query string before returning it (`split('?')[0]`); the tool refuses output with tracking parameters.
- The list is in page order, so match each row to the post text you read with `get_page_text` by author and order.
- `url: null` means the menu had no copy item (some ads and suggested posts). Skip that candidate or open it and repeat.
- Do not read the system clipboard (`navigator.clipboard.readText`); it waits for a permission prompt and hangs the run.
- A target without a link from this method is not delivered as a profile link with a guess. Say "no permalink" and give the author and the first line, or drop it.
