---
name: video
description: Short vertical video for Instagram Reels, TikTok, YouTube Shorts, LinkedIn or X — turn the user's mined stories into video ideas, each paired with a reference video that already works on the platform, a shot list they can film on a phone, the spoken lines in their voice, on-screen text and a caption; then cut and caption their footage with HyperFrames when it is installed. Use when the user says "give me reel ideas", "what should I film", "make a video from this story", "turn this into a reel", "edit my clips", or when strategy.md lists short video in formats.
---

# Video: what to film this week, and how

Why this exists. People who post short video about their life as founders say the filming is the easy part (a phone propped in front of them, or on the counter while they cook). The hard part is the idea and the reference: seeing someone film a format and thinking "I can do that". What they ask for is a plugin that takes what is happening in their business and their life, finds a reference video that fits, and says how to film it, with the words if they talk. That is this skill. It never generates a video of the person or a synthetic voice; the person films themselves.

## 1. Ideas from real stories

Read `stories/` (fresh first) and the week's calendar. A video idea is a story with something to see: a place, a thing being made, a before and after, a reaction, a number on a screen, a day in a sequence. A story that is only an opinion becomes a talking-head video only if the person likes talking to the camera (check `voice.md` and their past videos). Mix in the person's life when the strategy is founder life (`strategy.md`): a move, a trip, a meal, the gym, a hard day, told plainly. Respect `sensitivity` and `status: hold` exactly as `write` does; a customer's office or screen never appears without a yes.

## 2. A reference for each idea

With the browser, logged in as the user, search the platform for the format: the accounts the user said they like (`strategy.md` `reference_accounts:`), the platform's search for the topic, and the user's own best video. For each idea pick one reference video that is recent, did well for its account, and is filmable by one person with a phone. Record its link, the account, its view count as shown, and in one line what makes the format work (a fixed camera and a time-lapse, a fast cut every second, text on screen answering a question, a "day in" sequence, a reaction to a screenshot). Copy the format, never the content, music or footage. Save the references to `stories/assets/video-<slug>/references.md`.

## 3. The plan they can film in ten minutes

For each idea, in `drafts/<date>-video-<slug>.md`:
- **Hook**: what is on screen and said in the first two seconds. The same two-sentence test as `write`: something surprising, funny or personal, shown, not announced.
- **Shot list**: 3 to 8 shots, each with where the phone goes, what is in frame, and how long; vertical 9:16.
- **Spoken lines** (only if they talk): in their voice from `voice.md`, short, in the language of the account; under 40 seconds unless their past videos say longer works.
- **On-screen text**: the few words that carry it with the sound off.
- **Caption**: platform-native (Instagram: the first line carries it, 3 hashtags at most if their past posts use them; TikTok: short; LinkedIn: the story as a short text post).
- **The reference** from step 2, and the one move it copies.
Tag the draft `--lane`, `format: video`, platform, and the reference account in its `.meta.json`, so `recap` and `stanley-stats` can compare formats later.

## 4. Edit with HyperFrames (when installed)

HyperFrames (HeyGen, Apache 2.0) renders video from HTML: clips on tracks, kinetic captions, overlays, transitions. It needs Node 22+ and FFmpeg. If it is not installed, offer it once: in Claude Code `claude plugin marketplace add heygen-com/hyperframes` then `claude plugin install hyperframes@hyperframes`; in other agents `npx skills add heygen-com/hyperframes`. Then, with the user's footage in `inbox/` (they drop the clips there):
1. Transcribe the speech if there is any (whisper where installed; otherwise ask for the text) so captions match the words.
2. Build a composition from the shot list: the clips in order, cut to the lengths in the plan, the on-screen text, burned-in captions, 9:16.
3. Preview, then render to MP4 in `drafts/`. Show it; never post it without a yes.
Without HyperFrames, give the cut list (clip, in and out time, text on screen) so they can edit in CapCut, Instagram's editor or any app.

## 5. Publish and measure

Posting goes through `publish` (§3b covers any web composer; Instagram and TikTok uploads are done in the user's browser, or by the user from the phone when the web upload is not available, then `post-add --via manual`). `recap` reads views, likes, comments, saves and shares from the platform's insights page in the browser. After eight videos, `stanley-stats` can say which format and which kind of hook travels for this person; until then, call no winner.

## What it is not

No generated faces, avatars, voices or stock footage presented as the user's life. No reposting someone else's video. No trending audio that the account has no right to use. A reference is studied for its format, then left alone.
