# Handoff and note format

Read this reference whenever processing a ChatGPT Voice handoff.

## Accepted handoff

Accept `english-speaking-session-handoff/v1` and `/v2`. Required top-level fields are `schema`, `date`, and enough session evidence to make a reliable record. Missing optional fields are not errors. If the JSON is malformed or lacks reliable evidence, request the complete handoff rather than fabricating it.

The machine-readable v2 contract is [handoff-v2.schema.json](handoff-v2.schema.json). Use it for structural validation when a JSON Schema validator is available; semantic evidence checks still require session-history review.

Version 2 adds `review_context`:

```json
{
  "schema": "english-speaking-session-handoff/v2",
  "review_context": {
    "source_file": "English Speaking Review Queue.md",
    "source_updated": "YYYY-MM-DD",
    "source_status": "read",
    "targets": [
      {
        "target": "build on",
        "type": "chunk",
        "source_session": "YYYY-MM-DD English Speaking",
        "result": "independent",
        "evidence": "Exact transcript evidence"
      }
    ],
    "warnings": []
  }
}
```

Allowed review source states are `read`, `missing`, `stale`, and `unavailable`. Target results are `independent`, `prompted`, `incorrect`, and `not_used`.

## Session note

Use the vault's existing metadata conventions when present. Otherwise use:

```markdown
---
type: english-speaking-session
date: YYYY-MM-DD
mode: daily
duration_minutes: null
topic: "Short topic"
handoff_schema: english-speaking-session-handoff/v2
review_source_status: read
review_targets: []
grammar_gaps: []
grammar_observations: []
cards_added: 0
activation_target: null
next_activation_target: null
tags:
  - english-speaking
  - flashcards/english/speaking
---

# English Speaking — YYYY-MM-DD

## Session

- **Mode:** Daily conversation
- **Topic:** Short topic
- **Summary:** Concise summary grounded in the handoff.

## Review Target Results

### target chunk

- **Source:** Source session or queue
- **Result:** `independent`, `prompted`, `incorrect`, or `not_used`
- **Evidence:** Exact evidence or `insufficient evidence`
- **Queue decision:** Remove, keep active, or deepen, with a short reason

## Track A · Expression Gaps

### 1. Intended meaning

- **Intended meaning:** Preserve the handoff's wording
- **Learner attempt:** Exact attempt or state that it is absent
- **Voice suggestion:** Suggested expression
- **Actual re-say:** Exact attempt or `not attempted`
- **Final decision:** `discard`, `card`, or `deepen`, with a short reason

## Track B · Form Observations

### canonical-pattern-id

- **Voice evidence:** Incorrect → corrected
- **Session count:** Number or unknown
- **Status:** `observe`, `confirmed`, or `deepen`
- **Reason:** Evidence-based explanation, including relabeling or uncertainty

## Flashcards

### Card 1 · target chunk

A concrete situation and communicative intention that points to one answer
?
**Chunk:** reusable target chunk
**Example:** One natural sentence grounded in the learner's context.
```

## Invariants

- Keep `?` on its own line for multiline Obsidian flashcards.
- A cue is concrete and production-oriented, not a dictionary definition.
- `cards_added` equals the cards physically present in the note.
- Confirmed canonical IDs go in `grammar_gaps`; uncertainty goes in `grammar_observations`.
- Preserve exact learner evidence when available and label non-verbatim transcript warnings.
- Do not claim an Obsidian rendering or plugin check unless it was actually performed.

## Review queue

Include metadata for `updated`, `fsrs_scanned_at`, `last_processed_session`, and linked source sessions when compatible with the vault. Each active target should preserve its meaning, cue, priority, transfer status, FSRS state/due time, a natural opportunity, a do-not-reveal instruction, and a session source link.

Replace the queue as derived state. Never consolidate or overwrite source session notes, and never write scheduler metadata on the plugin's behalf.
