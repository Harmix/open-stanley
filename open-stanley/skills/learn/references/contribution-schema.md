# Contribution schema (v1)

Everything is a count or a range. There is deliberately no field that can hold free text longer than a rule id.

```json
{
  "schema": 1,
  "plugin_version": "0.1.0",
  "month": "2026-09",
  "salt_rotated": true,
  "platforms": {"linkedin": true, "x": true},
  "volume": {"posts": "1-5", "comments": "10-30", "scans": "20-60"},
  "audit": {
    "fired": {"lexicon": 14, "not-x-but-y": 3, "choppy": 6, "closing-question": 2},
    "user_reverted_fix": {"closing-question": 2}
  },
  "edits": {
    "cut-setup-sentence": 9, "shortened-25-50pct": 5, "replaced-word": 7,
    "changed-ending-to-question": 4, "removed-number": 2
  },
  "word_swaps": [["innate", "*"], ["leverage", "*"]],
  "skip_reasons": {"too-abstract": 6, "off-lane": 4, "already-commented": 2},
  "new_rule_candidates": ["ban:agreement-opener-comments"],
  "runtime": {"host": "claude-code|cowork|codex|openclaw|other", "browser": true, "capabilities": ["meetings", "messages", "browser"]}
}
```

Rules for `word_swaps`: only the *draft* word is kept (it is by definition a generated word); the replacement is always `*`. Rule ids come from the linter's fixed set or from `new_rule_candidates` as `ban:<slug>` / `allow:<slug>`. Ranges for volume are fixed buckets. Capabilities are category names, never server names. Maintainers drop any bucket with fewer than 5 contributors before publishing aggregates.
