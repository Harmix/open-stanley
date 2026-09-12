#!/bin/bash
# Drains the Open Stanley local queue inside a daily window, using Claude Code headless with the plugin.
# Install: cp this file to ~/.claude/plugins/open-stanley-drain.sh && chmod +x it; edit the four variables;
#          cp com.open-stanley.drain.plist ~/Library/LaunchAgents/ && launchctl load ~/Library/LaunchAgents/com.open-stanley.drain.plist
WINDOW_START=8      # local hour, inclusive
WINDOW_END=23       # local hour, exclusive
PLUGIN_DIR="$HOME/Downloads/temp/open-stanley"        # or the marketplace-installed path
export STANLEY_VAULT="$HOME/stanley-vault"   # git clone or synced Drive folder; for a Drive-MCP vault leave unset and the drain skill mirrors it
# Claude Code inherits your claude.ai connectors (Pam, Drive, Slack…) when logged in with the subscription (`claude /login`), not with an API key.
# Alternative to launchd for Cowork-only users: create the drain as a Cowork scheduled task; tasks that need local apps run locally when the app is open.

H=$(date +%H)
if [ "$H" -lt "$WINDOW_START" ] || [ "$H" -ge "$WINDOW_END" ]; then exit 0; fi
if "$PLUGIN_DIR/skills/stanley/scripts/stanley-vault" queue-check --brief >/dev/null 2>&1; then exit 0; fi   # exit 0 = nothing pending
command -v claude >/dev/null || { echo "claude CLI not found"; exit 0; }
# --chrome uses the Claude in Chrome extension if Chrome is running; without it the drain falls back to reporting.
# Headless runs can't answer permission prompts: grant the extension "allow all actions" for linkedin.com and x.com once
# (extension settings), sign in with `claude /login` (API-key auth disables --chrome), and allow the browser tools below.
claude -p "/open-stanley:drain" --plugin-dir "$PLUGIN_DIR" --chrome --max-turns 60 \
  --allowedTools "mcp__claude-in-chrome__*,Bash(\"$PLUGIN_DIR\"/skills/stanley/scripts/*),Read,Write" 2>&1 | tail -20
