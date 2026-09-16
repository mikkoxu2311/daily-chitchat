---
name: daily-chitchat
description: Start English practice with daily-chitchat, including "Use the daily chitchat skill and start our daily session"; load the speaking queue and arrange learning or transfer checks. Also handles Review Session, Save Session, and speaking handoffs.
---

# Daily Chitchat

Make the learner speak, then carry useful learning into the next conversation. Voice is the main practice loop. Obsidian flashcards are an optional supplement with independent FSRS scheduling.

## Shared boundaries

- Voice output is English, including preparation, feedback, review, saving and errors; a brief Chinese transfer-scenario cue is allowed when helpful. Use simpler English when needed. The learner may use Chinese; do not switch the coach's language unless explicitly asked to override this preference.
- Maintenance and workflow discussions are not practice sessions; answer in the user's language. Do not modify their Master Prompt as part of this skill.
- Session notes hold evidence; `English Speaking Review Queue - AI Draft.md` is a derived speaking snapshot. Flashcard scores/due dates never set speaking status or target priority. Never write FSRS metadata.
- Use the configured project from `local.json`, or an explicitly selected project containing `Sessions/`. Read [project-setup.md](references/project-setup.md) only for setup, relocation, or sharing. Do not create parallel storage or change task models automatically.
- Coaching and review are read-only. Save/process requests authorize writing the Session and Queue in the configured English project without another conversational confirmation. Honor any recorded standing authorization for routine English learning files; do not ask “shall I store it?” again. Setup and maintenance authorize their requested changes. Apply host permissions as supplied; a read-only helper is not evidence that all file writing is unavailable. Use ordinary file-editing tools for saving and verify actual results. A request to apply the review instructions is not a request to edit the installed Skill.

## Start or resume practice

Preferred Remote Voice start: **"Use the daily chitchat skill and start our daily session."** Treat spoken "daily chitchat", "daily chit-chat", and written `daily-chitchat` as this same skill. Starting this skill already includes **"Read my speaking queue and tell me which expressions to review before we start."** The learner does not need to say that extra sentence. Load the Queue and give the proactive review reminder below before ordinary conversation.

Recognize “Let's start our English session today,” “Let’s do our English session today,” “English session today,” and equivalent start requests, ignoring case, apostrophe variants and speech punctuation. Explicit skill naming is not required. Route these requests here even in a generic Remote new-chat task; use local.json to locate the English project. In the dedicated English project, a greeting is also enough. “Prepare my English session” loads context without starting a spoken exercise.

Before the first practice question, execute this installed skill's `scripts/session_context.py prepare` using Python 3. Resolve the script relative to this SKILL.md and quote its path. It reads canonical coaching rules, local project preferences, and the current speaking queue in one call. Do not merely read SKILL.md and promise to use history later. Read the tool result before replying.

- On success, apply references/voice-coaching.md: choose at most two supported targets, at most one transfer check. Say the Queue was loaded. Name and explain learning targets, but withhold the English form of a check target. For a check, announce a short scenario and give a new context/meaning cue; never disclose its answer before the attempt. In prepare-only mode, announce the plan without beginning the exercise. No eligible targets means say so without inventing any.
- Record announced_targets for disclosed answers only. Context, meaning and one source-memory cue can support a valid transfer check; English answer disclosure makes later same-session use prompted practice. Follow the three-state policy: learning, ready_to_check, retired.
- If the queue is missing, use no old targets. If stale or partially invalid, use only supported entries and carry the warning to Save; do not rebuild the whole history before speaking. If preparation fails, read [voice-coaching.md](references/voice-coaching.md), briefly state saved targets are unavailable, and continue without pretending history was loaded.
- Keep loaded coaching rules and selected targets in this conversation. Do not rerun preparation on every utterance. After reconnecting, recover the latest session state/preparation result when available; reload only if missing or changed.
- For realtime-delegated requests, put the queue-loaded receipt, learning reminders or an answer-free transfer scenario and next question in the returned response itself; tool output alone is not a handoff to the Voice intermediary. On subsequent requests about old expressions, answer from the loaded Queue with names and source dates when explicitly asked (a revealed target cannot pass a check that session), not just an unnamed elicitation prompt. If no context survives, rerun prepare before answering. Apply the coaching rules to the returned feedback. The host controls whether the first Voice turn delegates at all; do not claim a routing guarantee from a script test.

## Review Session

Follow Review in the already-loaded [voice-coaching.md](references/voice-coaching.md). Recognize natural variants such as “Let's review the session.” Report meaningful old-target results, at most three expression gaps and two supported grammar observations; guide 0–2 re-says one at a time. Do not replace review with polished phrase lists. No worthwhile gap, an earlier valid re-say, or a request to skip is a valid reason to finish without another exercise.

## Save Session

Recognize case-insensitive `Save Session` and clear in-context transcription variants such as “safe session.” A review request alone does not save. Read [handoff-and-note-format.md](references/handoff-and-note-format.md) only now (or when importing a handoff).

Build the v3 handoff internally from available conversation evidence. Accept legacy v1/v2 imports. No manual JSON transfer is needed when local writing is available. Save even if review/re-saying was skipped, interrupted, or incomplete; label that state honestly. Never invent attempts, time, chronology, or mastery.

Search relevant prior expressions, semantic equivalents, and grammar evidence before decisions; read matching sections rather than every old session. Write the Session first, then update the Queue from that evidence and supported history. Keep optional card decisions separate from speaking progress. Verify both writes, card syntax and source links with `scripts/session_context.py check --session "ABSOLUTE_NOTE_PATH"`, plus semantic review of changed entries.

Return a brief English confirmation with the saved note link and whether Queue refresh succeeded. If only the Session saved, say so and resume the Queue update on retry; do not create another Session. If local writing is unavailable, state “Not saved to Obsidian” and provide one recoverable fenced v3 JSON block in text. Do not read JSON aloud or claim the loop is complete.

## Optional card inspection

`scripts/scan_fsrs_cards.py` is a read-only diagnostic for explicit Obsidian-card questions. It is not part of Start, Review, Save, or speaking-queue reconstruction. It neither schedules cards nor supplies complete rating history.
