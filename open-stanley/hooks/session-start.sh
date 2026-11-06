#!/bin/sh
# SessionStart hook: one line about missed scheduled runs and queued items. Always exits 0.
ROOT="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}"
python3 "$ROOT/skills/stanley/scripts/stanley-vault" missed --brief 2>/dev/null
python3 "$ROOT/skills/stanley/scripts/stanley-vault" queue-check --brief 2>/dev/null
exit 0
