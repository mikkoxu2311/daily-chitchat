# Save, evidence, and note format

Load for Save/import, not ordinary conversation. Durable notes may retain Chinese summaries and optional Chinese card cues; all Voice-facing output remains English.

## Handoff

Create `english-speaking-session-handoff/v3`; accept v1/v2 without rewriting their original history. V3 separates speaking state from cards, selected from incidental targets, and records review completion. This minimal envelope permits empty arrays and null:

```json
{
  "schema": "english-speaking-session-handoff/v3",
  "session_id": "stable-id-for-this-practice",
  "date": "YYYY-MM-DD",
  "duration_minutes": null,
  "mode": "daily",
  "topic": "",
  "summary_zh": "",
  "review_status": "not_started",
  "review_context": {
    "source_status": "missing",
    "selected_targets": [],
    "announced_targets": [],
    "incidental_targets": [],
    "warnings": []
  },
  "activation_target": null,
  "track_a": [],
  "track_b": [],
  "candidate_cards": [],
  "transcript_warnings": []
}
```

- `review_status`: completed, partial, skipped, not_started. `source_status`: read, missing, stale, unavailable; it describes preparation, not a source first read at Save.
- Optional transfer fields on target entries: source_learning_session, check_context, cue_type (none/context/meaning/source_memory/answer), answer_disclosed_before_attempt, retirement_reason (transfer_pass/user_choice/null), retired_on. These extend v3 without rewriting old handoffs.
- Target entries: target, type (chunk/grammar), source_session, context, result (independent/prompted/transfer_pass/incorrect/not_used/alternative_used/uncertain), evidence, coach_revealed_before_attempt (boolean/null), transcript_confidence. Quote the first attempt, not the polished re-say. A transfer pass requires wording, a prior learning session, a new context and pre-answer-disclosure chronology; context/meaning/source-memory cues are allowed.
- `review_context.announced_targets`: expressions explicitly named in the opening reminder. Later same-session use of these expressions has coach_revealed_before_attempt: true; do not treat it as independent retrieval. Empty/absent in historical handoffs does not prove no hint occurred.
- Track A: intended_meaning_zh, user_attempt, transcript_confidence, suggested_chunk, explanation_zh, resay_actual, resay_result (successful/partial/unsuccessful/not_attempted), provisional_status, status_reason_zh.
- Track B: pattern_id, incorrect, corrected, context, current_session_count (number/null), confidence, provisional_status.
- Candidate cards: cue_zh, chunk, example, source_track_a_index. Maximum two final cards; zero is valid.
- Legacy v2 review_context.targets does not prove preselection; preserve unknown provenance. Infer missing dates from reliable practice timestamps and the configured timezone, never silently from an old session's save date. Repair syntax from available evidence; ask only for an essential missing fact, not a complete replacement handoff.

## Decisions: separate speaking from cards

For each Track A item record speaking_action (keep/deepen/discard) independently of card_action (add/existing/none). A duplicate card does not remove an unmastered speaking target.

Keep reusable expressions addressing a real retrieval/meaning gap likely to recur. Discard stylistic polish, unclear evidence, and very narrow vocabulary from active practice while retaining history. Add a card only for a worthwhile target with a concrete production cue and no equivalent card. Usually use a 2–6 word chunk and a real-context example; do not demand one exact wording for communicative success.

Deepen is a short contextual intervention for the same genuine gap in two distinct sessions, difficulty transferring a learned expression, or an explicit near-term high-stakes need. Grammar deepening requires the same confirmed error in three distinct sessions within 30 days. Counts are a lead; inspect context. Mass-noun `material` is not wrong merely because it describes multiple pieces; `gymnastic/gymnastics` is a word-form issue, not proof of a countability deficit. Uncertainty stays in Sessions, not confirmed Grammar Watch. No grammar flashcards; FSRS ratings never trigger deepening.

Apply learning, ready_to_check and retired in voice-coaching.md. One later-session new-context retrieval without answer disclosure retires the expression. Record retirement_reason (transfer_pass/user_choice), retirement date, source learning session, check context and cue_type. Prompted/independent remain attempt results, not states. Preserve explicit user activation targets; otherwise activation_target and next_activation_target remain null unless a contextual deepen intervention is justified.

## Session record

Use `YYYY-MM-DD English Speaking.md`; increment ` 2`, ` 3` only for genuinely separate same-day practices. Generate a stable session_id once per practice (task ID plus practice-start ID/time if available, otherwise generate once). Reuse it on retry. For old records without IDs compare date and source conversation/evidence, not topic alone. Partial saves resume the same note. Preserve existing FSRS comments when merging.

Frontmatter:

```yaml
ai_authored: true
ai_author: Codex
created: YYYY-MM-DD
human_reviewed: false
type: english-speaking-session
date: YYYY-MM-DD
session_id: "stable-id-for-this-practice"
handoff_schema: english-speaking-session-handoff/v3
mode: daily
topic: "Short topic"
duration_minutes: null
review_status: completed
review_source_status: read
selected_targets: []
incidental_targets: []
grammar_gaps: []
grammar_observations: []
cards_added: 0
activation_target: null
next_activation_target: null
tags: [english-speaking, flashcards/english/speaking]
```

Body: Session (summary, provenance, warnings); Speaking Evidence (selected/incidental, actual words, prompt chronology, context, result, state before/after and source); Track A · Expression Gaps; Track B · Form Observations; Re-say only when useful; Flashcards. Do not repeat quotations across sections. A local Evidence correction supersedes a mistaken historical interpretation without changing what was said. Do not reformat unrelated old records.

Optional cards retain this plugin-compatible shape:

```markdown
## Flashcards

### Card 1 · target chunk

一个具体的中文情境和交际意图
?
**Chunk:** target chunk
**Example:** A natural sentence in the learner's context.
```

Keep ? on its own line. cards_added equals the cards in the note. Zero cards means no placeholder card. Quote ambiguous YAML strings. Do not add/modify `<!--SR:...-->` scheduling comments; optional Obsidian review alone manages FSRS.

## Speaking Queue

Keep `English Speaking Review Queue - AI Draft.md`. Use English meanings, context questions and coaching data, without card scores or due dates. Frontmatter: AI authorship, type: english-speaking-review-queue, queue_schema: english-speaking-queue/v4, updated, last_processed_session, source_sessions, and source_fingerprint from session_context.py check (hash ignores FSRS comments).

Sections: Active Review Targets (max 8), Deepen Targets (max 5), Grammar Watch (max 5), Retired Expressions (max 8 displayed), Coach Selection Rules. The snapshot is bounded; omitted history remains in Sessions. Rotation is not mastery. Recover neglected/relevant targets through targeted history lookup at Save when needed.

Each target includes state, English meaning, priority, last selected date/session, latest result, missed-opportunity streak, actual evidence/source, and a natural question that does not reveal the target. Use unknown for unestablished historical timing/selection; never invent counters. Two consecutive selected sessions with no opportunity means rotate out for the next session without changing state, then reconsider when relevant.

Update after Save from latest Queue plus new evidence and relevant history. Rebuild only if missing, unusable or materially stale; do not block conversation on a rebuild. Never retire from prompted evidence alone or turn uncertain grammar into confirmed facts. Validate note names and exact heading anchors. Keep retired history in Sessions even when it leaves the displayed snapshot.

## Completion and retry

Write Session, update Queue, then read back/check both. Verify changed evidence semantically, exact paths, card count/syntax and source links. The read-only helper checks structure, not language judgments. Ordinary saves need no broad vault-wide tests or repeated UI checks. If files change concurrently, reread and merge before replacement.

Only say both saved when both checks succeed. If Queue fails, report Session saved/Queue pending and reuse the same Session on retry. Repeated Save without new evidence returns the existing note and repairs only incomplete work. On permission failure explain the concrete path in English; do not loop approvals or imply skill instructions bypass host permissions.
