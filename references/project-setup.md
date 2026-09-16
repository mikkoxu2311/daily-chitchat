# One-time setup and sharing

This skill runs on the Codex desktop host. It needs Python 3 and an authorized local English project containing `Sessions/`. The host must be reachable for Remote. Obsidian need not be open for the main file-based Voice loop; its Spaced Repetition plugin is optional and separate.

Store machine-local `local.json` beside SKILL.md:

```json
{"project_root": "/absolute/path/to/your/English/project", "timezone": "Asia/Shanghai"}
```

The helper accepts `--project` as an explicit override; otherwise it uses local.json, then the current folder if it already contains Sessions/. Never guess among multiple vaults. Missing configuration calls for a one-time path choice, not for learning history every session.

When asked to set up, create Sessions/ and an empty v4 Queue with documented sections and AI-authorship frontmatter. Empty history is valid. Add a short project AGENTS.md routing practice to this skill, English-only Voice, and the read-only prepare command. Preserve existing instructions. Optional learner preferences live in `ChatGPT Voice Project Instructions - AI Draft.md`; do not duplicate canonical coaching rules there. No Master Prompt is needed.

Open this project in Codex and grant folder access. Select a task model explicitly if desired; the skill does not pin one. Pair Remote with the desktop host using the current app UI; availability varies by account/version. Starting inside this project is more reliable than a generic new-chat workspace. Discovering an external configured path does not grant write permission. When the user explicitly grants ongoing writes to that English directory, record the bounded authorization and configure that exact path using the host's supported additional-writable-root setting. Do not disable approvals globally or expand access to the entire vault. A global additional root applies to host sessions using that config, not just one skill; limit actual writes to authorized tasks. Existing tasks may retain earlier permission snapshots. Verify effective permissions from a fresh task/config render and, where available, an actual sandbox write probe.

For the first check, ask in text: `Use $daily-chitchat to prepare my English session.` Confirm preparation succeeds, then start Voice in that task where supported. For everyday Remote Voice, say “Use the daily chitchat skill and start our daily session.” This includes loading the Queue and announcing learning reminders or a short transfer scenario, with the check answer withheld; no extra spoken instruction is needed. Natural English-start requests remain recognized when routed to Codex, but the generic Voice entry failed to delegate them in a live test. Actual Voice routing remains controlled by the host. When the user wants this behavior across generic new-chat workspaces, add a short global AGENTS.md route to this installed Skill; keep detailed coaching in the Skill. If an existing task cannot start Voice, use the supported new-Voice entry and explicitly request daily-chitchat; verify preparation rather than assume project inheritance.

For sharing, distribute SKILL.md, agents/, references/, and scripts/. Exclude local.json, learner preferences, Sessions, Queue, and private vault contents. Viewers configure their own project. No custom API key, FSRS write bridge, cloud Queue upload, or mandatory flashcard plugin is required by this skill. Do not publish or push without the user's request.
