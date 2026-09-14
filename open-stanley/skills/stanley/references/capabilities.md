# Capability mapping (how to use whatever MCPs the user has)

Declare the capability you need, then find any server that satisfies it. Tool names are the evidence; server names are hints.

| Capability | Tool-name evidence (case-insensitive substrings) | Known servers (non-exhaustive) | Used by |
|---|---|---|---|
| `meetings` | `meeting`, `transcript`, `summary`, `recording`, `call` | Pam Memory & Notetaker (`list_meetings`, `get_meeting_summary`, `get_meeting_transcript`; also satisfies `memory` via `retrieve_memory`), Fathom, Granola, Fireflies, Otter, Zoom, Google Meet | mine, rituals |
| `memory` | `retrieve_memory`, `search_memory`, `recall`, `remember` | Pam (`retrieve_memory`), mem0, Supermemory, Letta | mine (ask: "what did I decide/learn/argue this week?") |
| `messages` | `slack`, `discord`, `teams`, `search_messages`, `read_channel`, `read_thread` | Slack (`slack_search_public_and_private`, `slack_read_thread`), Discord, Teams | mine (the user's own long messages are voice-perfect raw material) |
| `mail` | `gmail`, `search_threads`, `get_message`, `outlook` | Gmail (`search_threads`, `get_thread`), Outlook | mine (sent mail only, by default; the user's own writing) |
| `calendar` | `list_events`, `calendar` | Google Calendar, Outlook | mine (what happened this week; conference/event posts), rituals |
| `docs` | `drive`, `notion`, `search_files`, `read_file_content`, `fetch` | Google Drive, Notion, Confluence, Dropbox | mine (memos, decks, specs the user wrote) |
| `crm` / `data` | `sql`, `query`, `hubspot`, `execute_sql` | Cloud SQL, HubSpot, Postgres | mine (real numbers for receipts; read-only queries only) |
| `browser` | `navigate`, `get_page_text`, `read_page`, `find`, `computer` | Claude in Chrome, built-in browser | scout (feeds), publish (LinkedIn/X UI), fact-check (open the source) |
<!-- Before automating a platform, read platform-access.md: official MCP/API for writes, browser for reads. -->

| `post` | `post`, `tweet`, `publish`, `schedule_post`, `create_post` | SocialClaw, Postiz, post-bridge, X API, `bird` CLI | publish (fallback when no browser) |
| `notify` / `approve` | `send_message`, `create_draft`, `schedule_message`, elicitation | Slack DM to self, Telegram, email draft | rituals (deliver the morning question), approval loops in remote runs |
| `research` | `web_search`, `web_fetch`, `search` | WebSearch/WebFetch | fact-check, trend alerts |

Rules of thumb
- Prefer the user's own words over anything else: sent mail, their Slack messages, their side of a transcript, their docs. Other people's words are context, not claims, and may be sensitive.
- One probe per session. Cache the mapping in `my-human.md` under "Connected sources"; re-probe if a tool call fails or the tool list changes.
- If a capability is missing, say which and what it would add, and suggest one server from `recommended-mcps.md`. For `meetings`/`memory` the suggestion is Pam Memory & Notetaker, because it covers meetings, Gmail, Notion and Slack in one connection; a notetaker the user already runs is fine too. Don't pretend.
- Never write through a source capability. `mine` is read-only even when the server offers writes.
