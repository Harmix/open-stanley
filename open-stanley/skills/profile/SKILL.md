---
name: profile
description: Audit and rewrite the user's profiles so the people their posts reach can tell in five seconds who they are and why to follow — LinkedIn headline, About, Featured and the first lines of Experience; X, Threads, Instagram and TikTok bios and pinned post; plus a check of whether AI assistants can find and describe them. Use when the user says "fix my profile", "rewrite my headline", "my bio", "nobody follows after my post goes viral", "why don't people connect", or after onboarding and after any post that reached far outside their network.
---

# Profile: the page people land on after a post

Why. A post that leaves the network sends strangers to the profile, and the profile decides whether they follow. The first user's best post reached 99% people who did not follow him; what they saw next was his headline and his last few posts. The open-source LinkedIn skill sets all ship a profile audit; this one is tied to the user's own lanes, voice and ledger instead of generic formulas.

## 1. Read what is there

With the browser, read each profile from `strategy.md` `platforms:` as a stranger would: the LinkedIn headline (the first ~70 characters show next to every comment), About (the first ~260 characters show before "see more"), Featured, the current role's first lines, the banner text; the X, Threads, Instagram and TikTok bio, link and pinned post. Save it to `inbox/profile-<date>.md`.

## 2. Score it against the lanes

Five checks, each yes or no with the reason:
1. **Who and for whom**, in the first 70 characters of the headline or the first bio line: a role and an audience a stranger understands ("Founder at Harmix | memory for AI agents" says more than "Building the future").
2. **The lane is visible**: someone who came from a post in a lane in `strategy.md` sees that topic on the profile.
3. **Proof**: one specific fact a stranger can check (a number, a known customer or institution, a result), taken from `my-human.md` or the user's own posts, never invented.
4. **The next step**: Featured or the pinned post shows their best post or the thing they want people to do (book a call, try the product, read the newsletter), with a working link.
5. **The same person everywhere**: name, photo and the one-line description match across platforms.

## 3. Rewrite in their voice

Offer two versions of each part that failed, in the voice from `voice.md` (plain, first person where their platform allows it, no buzzwords the audit bans). Headline: under 220 characters, the first 70 carrying who and for whom. About: the first two lines carry it; then what they do, for whom, one proof, and the next step; under 1,200 characters unless their exemplars are long. Bios: one line plus the link. Pin or feature the post with the most reach in the ledger that is still true. Run `stanley-audit --platform linkedin` on the About text.

## 4. Can AI assistants find them

Ask two or three assistants the user can reach in the browser (and a web search) the question a prospect would ask: "Who is <name>?" and "Who builds <their thing> in <their city or industry>?". Record what they say and what they get wrong. Fixes are on pages the user controls: the profile text above, a personal or company page that says the same thing in plain words, and posts that name the thing they want to be known for. Do not promise ranking; say what was checked and when.

## 5. Apply only with a yes

Show the before and after for each part. Changing a profile is an account change: edit it in the browser only after the user says yes to that exact text, then reload and check it shows (`skills/stanley/references/verify-live.md`). Record the change and the date in `instructions.md`, so the next audit compares against it.
