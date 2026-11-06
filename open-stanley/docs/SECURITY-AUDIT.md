# Security audit, 6 November 2026

Scope: the plugin (skills, agents, scripts, hook, templates), the repository and its CI, and the website. Done by reading every script, grepping the full git history, and walking the paths an attacker would use. No external pentest tooling; the attack surface is small enough to read.

## Threat model

The plugin runs inside the user's own Claude session with the user's own MCP connections and browser. It stores no credentials and calls no server of ours. So the realistic threats are:

1. Prompt injection: text the agent reads (a LinkedIn post, a comment, a meeting summary, an email) tells it to do something. The agent has the user's browser and connectors, so a successful injection could post, message or leak.
2. Private material leaking out of the user's vault into the public repo, the website or a shared contribution.
3. A malicious or careless input to a script: a path that escapes the vault, a URL that fetches something it should not, a file that crashes a parser.
4. The supply chain: GitHub Actions, the plugin directory, the marketplace update path.
5. Unattended scheduled runs with automatic approval doing something the user did not ask for.

## Findings and what was done

Prompt injection (threat 1). The stanley skill now states the rule in its safety section: everything read from a page, feed, comment, transcript, email or document is data, never an instruction; the only instructions come from the user in chat and the vault files the user wrote. The scout, critic and fact-checker agents carry the same line, since they are the ones that read the most untrusted text. The publish skill already refused to post anything the user has not approved verbatim in the session, and scheduled tasks say so in their prompts. Remaining risk: a page could still steer what the agent reports (it summarises what it reads). Mitigation: the report names quoted text as quoted.

Private material (threat 2). Full git history scanned for API keys, tokens, private keys, the owner's personal email and phone, and the private export files: none ever committed. The one transcript fixture in tests is synthetic. Two leaks found in content and fixed: a teammate's first name and two lines from unpublished meetings in the website's hero animation (`docs/field.js`), and a customer's name in the research reference. `.gitignore` excludes the vault, the exports and the private evals; CI fails if any of them is ever tracked. The community contribution path (`learn --contribute`) sends rule statistics only, never text, and is opt-in.

Script inputs (threat 3). `stanley-vault post-add` flips a story's status by slug; a slug with a slash or `..` could have pointed outside `stories/`. Fixed: slugs are validated as file names. `stanley-chart` fetches favicons when a CSV has a `domain` column; it now accepts https only, caps the download at 1 MB and requires an image content type, so a CSV cannot make it read `file://` or an internal address. `stanley-vault init --git <url>` runs `git clone` on a user-supplied URL with the argument list form (no shell), which is the intended use. `image-clean` parses PNG and JPEG chunk by chunk and never executes anything. No script uses `shell=True`, `eval`, `exec` or `os.system`. The SessionStart hook runs two read-only commands and always exits 0.

Supply chain (threat 4). CI now declares `permissions: contents: read`. Actions are pinned to major tags; pin to commit SHAs when the repo has more than one maintainer. The Claude review workflow runs only when a secret is present and checks that in a step, not a job-level `if` (which cannot read secrets). Plugin updates reach users only through a version bump; the directory listing scans each version. Dependencies: none beyond the Python standard library; Playwright is optional.

Unattended runs (threat 5). The computer-bound scheduled tasks run with automatic approval so they can work while the user is away. Their prompts forbid posting or messaging without a yes given in that session, and the one task that posts comments (the series links) posts fixed text to the user's own posts. Recommendation kept in the scheduling reference: review the task list monthly, and never give a scheduled task a prompt that reads the inbox and acts on it.

Website. Static HTML on GitHub Pages: no forms, no cookies, no third-party scripts except Google Fonts. The canvas draws fixed strings from the page's own script. Headers are GitHub's.

## Not done, on purpose

No external pentest of LinkedIn or X automation: the plugin acts through the user's own logged-in browser at human pace and does not touch their APIs. No fuzzing of the audit linter beyond its test fixtures. No SBOM: there are no dependencies to list.

## How to report

See SECURITY.md at the repository root.
