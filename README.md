# Daily Chitchat

English speaking practice with ChatGPT Voice, a local Codex host, and source-linked Obsidian notes.

## Install and setup

```bash
npx skills add mikkoxu2311/daily-chitchat
```

Requires Python 3.9+ and a local English project containing `Sessions/`. Configure `local.json` beside SKILL.md with your own absolute `project_root` and IANA `timezone`. This file is private and ignored by Git. See [setup](references/project-setup.md).

Open the English project as a Codex workspace. In Remote Voice, use an existing task with write access to that project where supported. Generic new Voice tasks may not inherit extra writable directories; Skill instructions do not grant host permissions. Actual startup and saving must be checked on your host.

## Daily use

Say: **Use the daily chitchat skill and start our daily session.**

The host loads the Queue and coaching rules. It selects at most two targets, including at most one transfer check. Learning expressions can be announced; a check begins with a new scenario without revealing its English answer. Continue the conversation, say **Review Session**, then **Save Session**. Saving writes a Session, updates Queue and verifies both. Partial practice can be saved; repeat Save reuses the same record.

## Three speaking states

| State | Meaning | Next step |
|---|---|---|
| learning | No supported correct use yet | Explain, model and practice |
| ready_to_check | Can use it after help, or later-context evidence is incomplete | Arrange a new situation in a later session |
| retired | One successful later-session transfer check, or explicit user removal | Leave routine review; reopen for real difficulty or user request |

The coach creates the opportunity instead of waiting for a coincidental topic. Context and meaning cues are allowed. After a correct alternative, one reminder to recall another previously learned expression is allowed. English wording, initials and model answers must remain hidden until the attempt. A short Chinese scenario cue is allowed when useful; other Voice output remains English. Correct alternatives are successful communication, but do not prove retrieval of the target.

Record `transfer_pass` or `user_choice` as the retirement reason. Same-session repetition after an answer disclosure cannot retire a target. Retirement means leaving routine practice, not permanent mastery. No opportunity does not count as failure.

Queue schema is `english-speaking-queue/v4`; handoffs remain v3 with added optional transfer evidence fields. Old handoffs and Session evidence remain readable. Migrate old states by checked evidence, preserving original historical notes. See [coaching](references/voice-coaching.md) and [saving](references/handoff-and-note-format.md). The retained handoff-v2 schema is legacy import documentation only.

## Session notes

New notes use ten default properties: `ai_authored`, `ai_author`, `created`, `human_reviewed`, `type`, `date`, `session_id`, `topic`, `review_status`, and `tags`. Learning content comes first: a short recap, expression practice, grammar feedback, old-expression review, and optional flashcards. Detailed evidence lives in a collapsed callout at the end. Original attempts, hint chronology, source links and speaking states remain available for later review.

The internal handoff remains v3; its fields are not all copied into note properties. Card counts are derived from the body. Legacy notes remain supported, including count verification when `cards_added` is present. Reformatting preserves the session ID, referenced headings, card text and FSRS comments; refresh the Queue fingerprint after reconciling any Session edits.

## Flashcards

Save may add zero to two useful, nonduplicate expression cards inside the Session note. Cards have a concrete production cue and example. Speaking state and card decisions are separate. Obsidian alone manages FSRS scheduling and ratings; these never drive Queue priority or retirement. The scanner is read-only and optional.

## Verification

```bash
python3 scripts/session_context.py prepare --project /absolute/path/to/English
python3 scripts/session_context.py check --project /absolute/path/to/English
python3 -m unittest discover -s tests -v
```

The helper checks structure and source links, not language judgment or live host behavior. Queue limits: 8 active, 5 deepen, 5 grammar observations and 8 displayed retired expressions. Sessions preserve omitted history.

## Privacy

Publish only portable Skill files. Never publish local.json, learner preferences, actual Sessions, Queue or private paths. No mandatory flashcard plugin or custom API key is required by the Skill.

## License

[MIT](LICENSE)
