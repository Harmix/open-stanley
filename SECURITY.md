# Security

Report a vulnerability to nazar@harmix.ai with "open-stanley security" in the subject. You will get a reply within 72 hours. Do not open a public issue for anything that could expose a user's vault or account.

What the plugin touches, so you know where to look: it reads the user's connected sources (meetings, Slack, mail, calendar, docs) through the MCPs the user has already authorized; it writes only to the vault folder on the user's machine and, after the user approves exact text, posts through the user's own logged-in browser. It stores no credentials, calls no server of ours, and sends nothing off the machine unless the user opts into the text-free community contribution. The threat model and the last audit are in `open-stanley/docs/SECURITY-AUDIT.md`.
