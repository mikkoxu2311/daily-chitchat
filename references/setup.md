# Setup

Read this reference only for first-time installation or when paths have changed.

## Requirements

- A file-capable Codex session or another agent that can read and write the chosen Obsidian vault.
- Python 3.10 or newer for the optional FSRS scanner.
- ChatGPT Voice for the conversational stage.
- Optional: an Obsidian spaced-repetition plugin that stores FSRS comments in the form `<!--SR:!fsrs,...-->`.

The core handoff and session-history workflow works without the optional plugin. Cards without scheduler metadata are reported as `new_unscheduled`.

## Initial layout

Prefer an established English-learning folder. If none exists and the user authorizes setup, create:

```text
English Speaking/
├── Sessions/
├── ChatGPT Voice Project Instructions.md
└── English Speaking Review Queue.md
```

Copy `assets/voice-project-instructions.md` into the project folder and replace the learner-profile placeholders. Do not publish or copy unrelated personal context.

Create an empty queue with these sections:

1. Active Review Targets
2. Deepen Targets
3. Grammar Watch
4. Recently Demonstrated
5. Coach Selection Rules

The queue should identify itself as derived state and point readers to Session notes as the learning source of truth.

## ChatGPT Project setup

When Voice cannot access local files directly:

1. Create a ChatGPT Project for speaking practice.
2. Paste the customized coach file into Project Instructions.
3. Add the current Review Queue as a Project Source.
4. Start a Voice conversation.
5. Say `review session`, complete the guided re-say, then say `Save Session` (capitalization does not matter).
6. Paste the returned JSON into a Codex task that has access to the vault.
7. Replace or re-upload the queue source after Codex refreshes it.

When Voice and the Skill share local file access, the final handoff can be processed directly without copying JSON.

## Smoke test

Run:

```bash
python3 scripts/scan_fsrs_cards.py "/absolute/path/to/English Speaking/Sessions" --now "2026-01-15T09:00:00+00:00"
```

Confirm that the command prints JSON, does not alter any note, and reports unscheduled cards as `new_unscheduled`.
