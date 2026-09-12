# Vault backends

The scripts in `skills/stanley/scripts/` always work on a local folder. What differs is how that folder reaches a scheduled run. Pick one at onboarding and write it into `my-human.md` as `vault: local|drive|notion|git` plus `vault_path:` (local) or the folder/page id.

**Default: `local`, a plain folder inside a desktop-synced Google Drive (or iCloud/Dropbox) folder, with scheduled tasks set to run on the user's computer (laptop mode, see `scheduling.md`).** No mirror, no per-file MCP calls, no permission prompts, no tokens; the sync client handles backup and other devices; runs have the browser. Concurrent runs append to jsonl files line-atomically.

| Backend | Where runs get it | Use when |
|---|---|---|
| `local` **default** | the folder itself (tasks require the computer, "Work in a folder" = the vault) | laptop mode; the user's computer is awake during the job window |
| `drive` (folder in the Google Drive the Drive MCP is connected to) | mirror via the Drive MCP (below): one call per file, one permission prompt per write unless the task auto-approves; concurrent runs can leave duplicate files | cloud mode: runs must happen with the laptop closed |
| `notion` (a page tree) | via the Notion MCP | cloud mode for people who live in Notion |
| `git` (private repo) | `git clone` / `stanley-vault sync` | Claude Code users running jobs from their own machine or CI. **Not usable from Cowork scheduled tasks**: they have no repository field and the cloud git proxy refuses to inject a credential for a repo that is not a session source. |

If the same person uses both modes (laptop by day, a cloud job at night), point the cloud job's Drive mirror at the same synced folder: the desktop client syncs what the cloud run replaces. Keep the folder name `stanley-vault` so `search_files` finds it.

## The git flow (Claude Code / CI only)

```
git clone <vault_git> ./stanley-vault        # start of every run (or `git -C ./stanley-vault pull --rebase` if it exists)
export STANLEY_VAULT=./stanley-vault
skills/stanley/scripts/stanley-vault run-start <job> --promised "..."
# ... work ...
skills/stanley/scripts/stanley-vault run-end <id> --delivered "..." --shown N --queued N --browser yes|no
skills/stanley/scripts/stanley-vault sync    # git add -A, commit "stanley sync <time>", pull --rebase, push
```

`sync` never force-pushes. If the rebase hits a conflict (two runs appended to the same jsonl at once), it keeps both sides' lines for `*.jsonl` (append-only ledgers lose nothing) and lets the syncing run's own version win for markdown, then pushes; `sync` prints which files were merged and the run message repeats it. If `push` is rejected twice, the run reports it and leaves the commit local for the next run to carry.

Setting it up: the user creates an empty private repo, `stanley-vault init ./stanley-vault --git <url>`, write the onboarding files, `stanley-vault sync`. Credentials come from the machine's own git setup (Claude Code on the laptop, or a CI runner's deploy key). Never put a personal access token in a prompt. The commit identity `sync` sets is `Open Stanley <open-stanley@noreply.invalid>`; never use a `@users.noreply.github.com` address you do not own, GitHub attributes it to that username's real owner.

## The Drive mirror (cloud mode)

The Drive MCP can `download_file_content` (base64), `create_file` (text, keep it a plain file with `disableConversionToGoogleType: true`), and `trash_file`; it cannot update a file's content in place. So every run is: pull, work, replace.

1. **Find the vault folder**: `search_files` with `title = 'stanley-vault' and mimeType = 'application/vnd.google-apps.folder'` (store the folder id in `my-human.md` after the first time). List its files with `parentId = '<id>'` (and the subfolders `stories`, `ledger`, `drafts`, `learn`, `skills`, `inbox`; keep the tree flat-ish, one level of subfolders).
2. **Pull**: for each file, `download_file_content`, base64-decode, write to a temp mirror dir (`${CLAUDE_PLUGIN_DATA}/vault-mirror` locally, a temp dir in the cloud). Then `skills/stanley/scripts/stanley-vault --vault <mirror> snapshot`.
3. **Work** with `STANLEY_VAULT=<mirror>` as usual. Scripts append to jsonl, write drafts, etc.
4. **Push**: `skills/stanley/scripts/stanley-vault --vault <mirror> changed` lists added/changed/deleted paths. For each: `create_file` with the new text in the right subfolder (`contentMimeType: text/markdown` or `application/json`, `disableConversionToGoogleType: true`), then `trash_file` on the old file id. Deleted → `trash_file`. Nothing else is touched.
5. Say in the run message how many files were replaced.

**Issue the downloads in one turn.** Each `download_file_content` is a separate MCP call; sending them all in a single turn (parallel tool calls) is the difference between a 30-second pull and a five-minute one. Same for the `create_file` + `trash_file` pairs at the end.

**Pull only what the job needs.** Every file is one MCP call, so an 18-file pull is 18 calls before any work starts; the first smoke-test Soapbox run spent most of its time there. The core set every job needs: `my-human.md`, `strategy.md`, `voice.md`, `instructions.md`, `learn/rules.md`, `stories/index.md`, `ledger/runs.jsonl`, `ledger/local-queue.jsonl`. Then per job: soapbox adds `stories/needs-material.md` and the one story it asks about; scout adds `ledger/surfaced.jsonl` and `ledger/comments.jsonl`; recap adds `ledger/posts.jsonl`; mine and weekly drafts pull everything. Snapshot what you pulled; `changed` only compares what is in the mirror, so a partial mirror is safe as long as you never write a file you did not pull. If a push fails halfway, the next run's pull sees the newer file (Drive keeps both until trashed); prefer the newest `modifiedTime` when two files share a name.

Uploads, images and PDFs in `inbox/` and `drafts/*.assets/` go up with `base64Content`. Keep jsonl files under a few MB; when `ledger/surfaced.jsonl` grows past that, archive by month (`surfaced-2026-09.jsonl`).

If the user *also* has that Drive synced to the laptop, local sessions can skip the mirror and use the synced folder directly; the cloud still mirrors. Both write the same files, and Drive's own sync handles the rest.

## Notion

Same idea without the replace step: one page per vault file under a `stanley-vault` page; `notion-fetch` to read, `notion-update-page` to write, `notion-create-pages` for new stories/drafts. jsonl ledgers become Notion databases if the user prefers, but a code block on a page is fine and keeps the scripts unchanged (pull the block text into the mirror, push it back).

## Which one to suggest

`local` in a synced folder, laptop mode. Offer cloud mode (`drive`, or `notion`) only when the user says runs must happen with the laptop closed, and say plainly what it costs: slower runs, a queue and a drain task for anything that needs the browser.
