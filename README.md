# Daily Chitchat

An evidence-first Codex Skill for spoken-English practice with ChatGPT Voice and Obsidian.

Daily Chitchat turns a short conversation into a durable learning loop:

```text
Obsidian review queue
        ↓
ChatGPT Voice conversation
        ↓
review session → re-say 1–2 useful gaps
        ↓
structured handoff
        ↓
Codex checks history → session note + cards + refreshed queue
```

The important bit is the historical check. Voice can suggest corrections, but it cannot reliably decide that a problem is recurring, that a phrase deserves a card, or that a learner has mastered it. Daily Chitchat treats the transcript as evidence and makes those decisions against the learner's saved history.

## What it does

- Runs low-interruption English conversation practice.
- Silently creates natural opportunities to reuse up to two past expressions.
- Reviews communication-blocking gaps instead of polishing every sentence.
- Uses a versioned JSON handoff between Voice and a file-capable Codex task.
- Saves source-traceable Obsidian session notes.
- Creates zero to two production flashcards only when justified.
- Keeps a bounded review queue for the next conversation.
- Reads common Obsidian FSRS scheduling comments without modifying them.

## What it does not do

- It does not expose an entire Obsidian vault to ChatGPT Voice.
- It does not pretend that a Voice transcript is verbatim.
- It does not manufacture spaced-repetition scheduling metadata.
- It does not create cards to hit a quota.
- It does not require a manual “word of the day” for normal sessions.

## Install

### Codex Skills CLI

```bash
npx skills add mikkoxu2311/daily-chitchat
```

### Manual install

Clone the repository into your Codex skills directory:

```bash
git clone https://github.com/mikkoxu2311/daily-chitchat.git ~/.codex/skills/daily-chitchat
```

Restart or open a new Codex task so the Skill is discovered.

## Requirements

- Codex or another Skill-compatible, file-capable coding agent.
- An Obsidian vault.
- ChatGPT Voice for the conversation.
- Python 3.10+ for the optional read-only FSRS scanner.
- Optional: an Obsidian spaced-repetition plugin that writes `<!--SR:!fsrs,...-->` comments.

You can use the core workflow without a spaced-repetition plugin. New cards will simply appear as `new_unscheduled` in the scan.

## First-time setup

Open your Obsidian vault as the Codex workspace and ask:

```text
Use $daily-chitchat to set up my English speaking workflow in this vault.
```

The Skill will reuse an existing English-learning folder when one exists. Otherwise it recommends this minimal layout:

```text
English Speaking/
├── Sessions/
├── ChatGPT Voice Project Instructions.md
└── English Speaking Review Queue.md
```

It copies and customizes [`assets/voice-project-instructions.md`](assets/voice-project-instructions.md) for the learner. The template contains explicit placeholders and no personal data.

### If Voice cannot access local files

This is the most portable setup:

1. Create a ChatGPT Project for English speaking.
2. Put the customized Voice instructions into the Project Instructions.
3. Add the current `English Speaking Review Queue.md` as a Project Source.
4. Start a Voice chat and speak normally.
5. Say `review session` and complete the guided re-say.
6. Say `handoff to codex`.
7. Paste the returned JSON into a Codex task opened on your vault.
8. Replace the Project Source after Codex refreshes the queue.

If Voice and the Skill share local file access, step 7 can happen directly.

## Daily use

Start with:

```text
Let's start our English speaking session.
```

During the session you can optionally use:

- `scenario: checking into a hotel` — role-play a specific situation.
- `activation target: push back on` — manually prioritize a high-stakes expression.
- `review session` — stop the conversation and review evidence-backed gaps.
- `handoff to codex` — produce or directly process the structured handoff.

Activation Targets are exceptional, not required daily state. Normal retrieval comes from the review queue.

## The decision model

Every expression gap ends in one of three states:

| State | Meaning |
| --- | --- |
| `discard` | Unclear, stylistic, narrow, duplicated, or already demonstrated naturally. Keep the history; make no card. |
| `card` | A reusable Chunk that materially blocked communication and can be prompted with one concrete cue. |
| `deepen` | Repeated failure, recall without transfer, repeated Again/Hard results, or a near-term high-stakes need. |

This prevents a common failure mode: a giant deck full of elegant phrases the learner never needed to say.

## Review queue

The queue is deliberately bounded:

- 8 Active Review Targets
- 5 Deepen Targets
- 5 Grammar Watch patterns
- 8 Recently Demonstrated items

The ordering is overdue → due now → new unscheduled. Future-scheduled cards stay out unless they qualify for deeper transfer practice. Recent independent use removes an item from active Voice testing without deleting its card or scheduler history.

## FSRS scanner

Run it directly with:

```bash
python3 scripts/scan_fsrs_cards.py "/absolute/path/to/English Speaking/Sessions"
```

For deterministic tests:

```bash
python3 scripts/scan_fsrs_cards.py "/absolute/path/to/Sessions" \
  --now "2026-01-15T09:00:00+00:00"
```

The scanner prints JSON and never edits notes. It classifies cards as:

- `new_unscheduled`
- `overdue`
- `due_later_today`
- `scheduled_future`

## Repository structure

```text
.
├── SKILL.md
├── agents/openai.yaml
├── assets/voice-project-instructions.md
├── references/
│   ├── handoff-and-note-format.md
│   ├── handoff-v2.schema.json
│   └── setup.md
├── scripts/scan_fsrs_cards.py
└── tests/test_scan_fsrs_cards.py
```

## Privacy and safety

- Keep the Voice integration scoped to the English project folder, not the full vault.
- Review the learner profile before uploading Project Instructions.
- Do not commit real session notes, queue contents, transcripts, or vault paths to this repository.
- A copied Voice transcript may be imperfect. Preserve uncertainty and never invent missing speech.

## Development

Run the unit test:

```bash
python3 -m unittest discover -s tests -v
```

Validate the Skill structure with Codex's `quick_validate.py` from the bundled `skill-creator` Skill.

## License

[MIT](LICENSE)
