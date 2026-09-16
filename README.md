# Daily Chitchat

English speaking practice with ChatGPT Voice, a local Codex host, and source-linked Obsidian notes.

## 第一次使用：从安装到保存第一篇练习记录

这套流程适用于能在 Codex 中使用 Voice 的环境。Skill 负责练习规则与学习记录；安装它不会开通 Voice，也不会让普通 ChatGPT 网页自动获得本地文件访问能力。

### 1. 准备环境，选择学习文件夹

- **Codex 与 Voice**：先确认自己的应用和账号能进入语音交流。没有语音入口时，先解决入口问题；也可以先用文字检查配置和保存。
- **Python 3.9+**：本地检查脚本需要它。可以让 Codex 检查是否已安装。
- **Node.js/npm 与 Git**：下面的安装方式使用 `npx` 并从 GitHub 获取文件；需要联网。缺少工具时，让 Codex 根据你的系统引导安装，再继续。
- **Obsidian 可选**：想在 Obsidian 中查看记录，就在已有 Vault 内建立一个 `English` 文件夹；也可以使用普通本地文件夹。卡片插件不影响主流程。

在 Codex 中打开你选择的 `English` 文件夹作为项目。学习记录以后都保存在这里。首次先在电脑上完成，手机 Remote 可在最后配置。

### 2. 把 Skill 安装到这个项目

在电脑终端进入该文件夹，或在 Codex 中直接发送：

> 请在当前英语项目目录运行下面的命令，将 daily-chitchat 安装到当前项目的 Codex。先检查 Node.js/npm、Git 和 Python 是否可用；缺少时告诉我具体缺什么。已有安装时先说明情况，保留学习记录和本机配置。
>
> `npx skills add mikkoxu2311/daily-chitchat --agent codex --skill daily-chitchat`

终端用户可以直接运行：

```bash
npx skills add mikkoxu2311/daily-chitchat --agent codex --skill daily-chitchat
```

如果 `npx` 询问是否下载 `skills` 工具，确认包名后继续；安装目标已限定为 Codex 和 daily-chitchat。此命令默认安装到**当前项目**，不带 `--global`。不要在无关文件夹中运行。

安装器显示完成后，在这个英语项目中新开一个 Codex 文字任务，再进行下一步。仅从 GitHub 下载 ZIP 不代表已安装。安装参数说明见 [skills 官方文档](https://github.com/vercel-labs/skills#options)。

### 3. 复制这段话，完成首次配置

下面这段发给 Codex 即可。你不需要手工编辑 JSON 或 YAML。

```text
请使用 daily-chitchat 帮我完成首次配置，现在先不要开始口语练习。

请先读取已安装 Skill 的 references/project-setup.md 和当前保存规范。
将当前打开的英语项目文件夹作为学习记录目录；如果当前目录不明确，先问我。
确认我的时区，不要直接假设。询问我的练习目标、常聊话题和希望的难度；
我可以跳过偏好设置，先从简单的日常聊天开始。

请保留已有文件和学习历史，只创建缺少的 Sessions/、空 Speaking Queue、
简短的项目 AGENTS.md，并配置 Skill 的本机 local.json。
学习偏好写入项目的偏好文件，不复制整份教练规则。

我授权在这个英语项目中保存日常 Session、更新 Queue，
以及用一个独立临时文件检查写入、读回并清理该测试文件。
不要扩大到其他目录，不要关闭全局审批，不要生成虚构的练习记录。
如果宿主权限不允许，请告诉我需要在应用中授权哪个目录。

完成后运行 Skill 的 prepare 和 check：新项目应为 0 篇 Session、
没有旧复习目标；初始化 Queue 的来源指纹，确认没有缺失结构或来源警告。
已有项目沿用真实历史，不清空 Queue 或重置学习状态。
最后告诉我学习文件夹的位置、读写检查结果和开始练习的那句话。
```

**配置成功应该看到：** Codex 能识别 Skill、返回你选定的学习路径、通过目录读写和 Queue 检查。第一次显示“没有历史复习目标”是正常的；显示“目录不存在”“Queue 缺失或过期”则需要先修复配置。

已有用户重复发送这段配置请求，应保留原有 Session、卡片、Queue 和本机配置中的其他设置；只有明确选择了新目录或偏好时才更新对应项。

### 4. 完成第一次练习

在这个项目对应的任务中进入 Voice（以你的客户端提供的入口为准），说：

> **Use the daily chitchat skill and start our daily session.**

第一次没有旧表达，就直接聊工作、生活或你正在做的事。以后会根据已保存的记录，安排最多两个目标，其中最多一个是不提前报出英文答案的新情境验证。

聊完依次说：

> **Review Session.**
>
> **Save Session.**

复盘会挑值得继续练的表达和语法，按需请你重说。保存后应返回一篇 Session 的链接，并明确 Queue 是否更新成功。打开链接确认能看到刚才的实际内容。没有值得制卡的表达时，不生成卡片也正常。

部分完成的练习也能保存。保存失败时先解决权限或连接问题，再重试同一次保存；不要把聊天中出现的笔记文本当成已经写入文件。

### 5. 确认下一次能接上

再次开始练习，确认它能读取已有记录。有待练表达时，应提醒学习目标或安排新情境；没有合适目标时正常聊天。如果它声称没有历史，而文件已经存在，请让 Codex 检查当前项目、local.json 和 Queue 来源。

**整个流程跑通的标志：第一次能保存真实记录，下一次能读取这些记录。** 安装成功或一次脚本检查通过，不能代替实际语音与保存验证。

### 可选：手机 Remote 与 Obsidian 卡片

电脑端跑通后，再按应用提供的方式将手机 Remote 连接到电脑宿主，并确认电脑和学习目录可访问。尽可能进入已有的英语任务；不同入口未必继承相同目录权限。先实测开场能加载 Queue，再实测保存。

希望额外用卡片复习时，再安装和配置 Obsidian Spaced Repetition。Voice 是主要练习入口，卡片是补充，不需要先积累卡片才能开始。

### 遇到问题先看这里

| 现象 | 下一步 |
|---|---|
| `npx` 或 `python3` 找不到 | 让 Codex 检查对应运行环境及命令路径，安装缺少的工具后重新打开终端或任务。 |
| 找不到 daily-chitchat | 确认安装命令是在英语项目里执行，安装目标是 Codex；在同一项目中新开任务，让它检查安装位置。 |
| 提示目录不存在或缺少 Sessions | 返回第 3 步完成配置；单独打开空文件夹还不够。 |
| Queue 缺失、过期或结构检查失败 | 让 Codex 按保存规范检查、修复 Queue，并重新运行 check；保留 Session 原始证据。 |
| Voice 直接聊天，没有确认加载历史 | 明确点名 daily-chitchat，要求先准备本次练习；检查同一任务的文字记录是否真的运行了 prepare。无法调用后台时，先在文字任务准备，不假定语音已拿到上下文。 |
| Save 后没有笔记，或提示无写权限 | 确认实际保存路径和当前任务对该目录的权限。授权后重试 Save，沿用同一次记录。 |
| Session 保存了，Queue 没更新 | 要求继续完成这次 Queue 更新，不另建一篇 Session。 |
| 手机可聊天，但不能读写学习目录 | 检查宿主连接和 Remote 任务的实际权限；先回到已验证可读写的电脑任务处理保存。 |

## 日常使用速记

完成首次配置后，只需要：**开始练习 → Review Session → Save Session**。不用每次重新配置，也不用手动搬运上次的表达。

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
