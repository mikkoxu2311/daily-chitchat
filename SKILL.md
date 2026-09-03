---
name: daily-chitchat
description: Run English speaking practice and turn a Voice handoff into source-traceable Obsidian session notes, production flashcards, and a bounded review queue. Use when the user starts an English speaking session, provides an english-speaking-session-handoff/v1 or v2 object, or asks to save or review a speaking session.
---

# Daily Chitchat

Run a short English conversation, review only high-value speaking gaps, and preserve the result as verifiable learning history. Voice analysis is evidence, not authority: never invent a transcript, recurrence, mastery, or FSRS result.

## Establish the workspace

Before reading or writing learning data, resolve these locations from the current workspace or the user's explicit configuration:

- `vault_root`: the Obsidian vault root.
- `project_dir`: the English-learning folder. Recommend `<vault_root>/English Speaking` only when no established folder exists.
- `sessions_dir`: `<project_dir>/Sessions`.
- `queue_file`: `<project_dir>/English Speaking Review Queue.md`.
- `coach_file`: `<project_dir>/ChatGPT Voice Project Instructions.md`.

Never assume a username, home directory, vault name, or private project path. Search for an existing queue and session notes before creating a parallel structure. Create or edit files only when the user asks to set up, process, save, or refresh the workflow.

For first-time setup, read [references/setup.md](references/setup.md). Use [assets/voice-project-instructions.md](assets/voice-project-instructions.md) as a template, adapting only the clearly marked learner profile fields.

## Choose the mode

### Voice coaching

Use when the user asks to start English speaking practice.

1. If configured session history exists, run the read-only scanner:

   `python3 scripts/scan_fsrs_cards.py "<sessions_dir>"`

2. Refresh the derived queue from scanner output and session evidence. If scanning fails, continue with the existing queue and report the warning in the handoff.
3. Read `coach_file` and `queue_file` when available.
4. Follow the coaching contract: short turns, one question at a time, no unsolicited mid-conversation corrections, and at most two silent review targets.
5. On `review session`, identify evidence-backed gaps and guide at most two re-says.
6. On `handoff to codex`, process the v2 handoff directly when local file access exists. Otherwise return exactly one fenced JSON object for a file-capable agent.

### Handoff processing

Use when the user supplies a v1/v2 handoff or Voice coaching reaches `handoff to codex`.

Read [references/handoff-and-note-format.md](references/handoff-and-note-format.md), then:

1. Parse the handoff and preserve uncertainty, missing values, empty re-says, and transcript warnings.
2. Inspect existing sessions for the proposed Chunk, semantic equivalents, cue intent, grammar evidence, and prior transfer evidence. String matching is only a lead.
3. Give each Track A gap one final state: `discard`, `card`, or `deepen`.
4. Normalize Track B labels from quoted evidence. Keep ambiguous claims as observations.
5. For v2 review results, accept `independent` only when the learner attempted the target before Voice revealed or strongly hinted at it.
6. Save one concise session note. Add zero to two production cards; zero is valid.
7. Run the scanner and rebuild the bounded queue from session history plus the scan.
8. Re-read the saved files and verify paths, frontmatter, card syntax, source links, and the absence of unrelated edits.

## Learning decisions

### Discard

Discard when evidence is unclear, the original wording already worked, the suggestion is merely stylistic or too narrow, the cue is ambiguous, an equivalent card exists, or later independent use shows the item no longer needs active Voice testing. Preserve the historical evidence but create no card.

### Card

Create a card only when the gap materially blocked the intended meaning, the target is a reusable spoken Chunk (normally 2–6 words), the learner is likely to need it again, one concrete cue can elicit one main answer, and no active semantic equivalent exists. Ground the example in the learner's real context.

### Deepen

Use `deepen` only when ordinary review has plausibly failed or near-term stakes justify practice. Evidence may include the same gap in two distinct sessions, the same confirmed grammar problem in three sessions within 30 days, recall without conversational transfer, three recent Again/Hard results, or an imminent high-stakes situation.

An Activation Target is optional and belongs only to `deepen`. Routine queue retrieval is not an Activation Target.

## Queue rules

The queue is derived state; session notes and FSRS metadata are sources of truth.

- Active Review Targets: maximum 8. Rank overdue, due now, then unscheduled new cards. Exclude future-scheduled cards unless they qualify for Deepen.
- Deepen Targets: maximum 5. Require evidence under the Deepen rule.
- Grammar Watch: maximum 5. Include only grounded patterns still worth observing.
- Recently Demonstrated: maximum 8. Include recent independent transfer and remove those items from Active Review Targets.

Voice selects at most two active targets per session and must not reveal an answer before the learner attempts it. The scanner never writes or synthesizes `<!--SR:...-->` comments. Conversational transfer and FSRS recall are separate signals.

## Safe file behavior

- Use `YYYY-MM-DD English Speaking.md` for the first session of a day and increment a suffix for a genuinely separate session.
- Compare before writing so the same handoff is not recorded twice.
- Preserve existing note structure, links, tags, frontmatter, and scheduler comments.
- Do not expose other vault content to Voice or a bridge. Scope access to `project_dir`.
- After writing, report the saved note, cards added, items discarded or deepened, normalized grammar labels, and remaining uncertainty.
