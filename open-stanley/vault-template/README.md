# stanley-vault

This folder is the memory of your Open Stanley. It is plain markdown and jsonl so you can read and edit everything.

- `my-human.md`, `strategy.md`, `voice.md`, `instructions.md` — who you are, what you're doing, how you sound, what you told it
- `stories/` — one file per story with a **receipt** (where it came from); `index.md` is generated
- `ledger/` — `posts.jsonl`, `comments.jsonl`, `surfaced.jsonl` (everything ever shown to you), `runs.jsonl` (every scheduled run)
- `drafts/` — drafts in progress; git keeps versions
- `inbox/` — drop voice notes, transcripts, screenshots, PDFs here
- `learn/` — `diffs.jsonl` (every draft→final pair), `rules.md` (what you confirmed)

Keep it somewhere cloud scheduled runs can reach: a folder inside Google Drive (a normal folder on your laptop; the Drive MCP reads and writes the same files from the cloud) or a private git repo. `skills/` holds your own overrides, loaded in every run. `ledger/local-queue.jsonl` is where cloud runs park browser-only work for your laptop to drain.
