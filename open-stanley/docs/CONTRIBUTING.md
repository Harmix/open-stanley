# Contributing

Two kinds of contribution, one gate.

## 1. Rules and skills (pull requests)

- A new audit rule goes in `skills/stanley/scripts/stanley-audit` with a row in `skills/audit/references/rules.md` (what, why, evidence) and at least one fixture in `tests/evals/fixtures/` that fires it, plus one human-written fixture that must not. `python3 tests/evals/run_audit_tests.py` must pass.
- A skill change ships with an eval in `tests/evals/evals.json` describing the prompt and the expected output. Maintainers run the skill-creator blind comparison (old vs new) on the eval set; the change merges when the comparator prefers it and a maintainer agrees.
- Voice rules that are personal (this person never says X) do not belong here; they belong in that person's `voice.md`. Only rules that generalize across authors are accepted.
- No humanizer/paraphraser integrations. No telemetry hooks. No prompts that impersonate native UI.

## 2. Usage signals (opt-in, text-free)

Users who set `contribute: yes` get a monthly `learn/contribution-<month>.json` (schema: `skills/learn/references/contribution-schema.md`) that they review and post as a GitHub issue labelled `contribution`. It contains counts only: which rules fired, which fixes were reverted, which edit categories recurred, which skip reasons clustered, and coarse volume buckets. Maintainers aggregate with a minimum of five contributors per bucket before anything is published, then turn recurring signals into rule PRs that go through the gate above.

Never include in an issue: draft or post text, comments, story files, meeting content, names, handles, URLs, or MCP server names. If you see one in someone else's issue, flag it and we'll delete it.

## Style pack proposals

A style pack is a sub-skill with its own exemplars and yaml overrides (e.g. "founder build-in-public numbers post", "PG-style X replies"). Propose one as a directory under `skills/packs/<name>/` with a `SKILL.md`, 10+ exemplars that are either your own or explicitly licensed, and an eval. Packs never ship someone else's private posts.

## Running the evals

```
python3 tests/evals/run_audit_tests.py            # deterministic
# behavioral, with the skill-creator plugin:
/skill-creator  →  point it at this repo, tests/evals/evals.json
```
