---
name: nk-orca-guide
description: "Operating guide for Orca as the execution substrate: resolve the CLI, create worktrees, dispatch and interact with agent workers, confirm completion, and clean up, with per-agent caveats. Load when a project has declared Orca usage and work needs Orca-managed worktrees or agents."
argument-hint: "[可选：要查的主题，如 完工确认 / 读屏 / 删除]"
---

Orca 是可选的执行底座：它托管工作树与 agent 终端，让派出的 worker 在真实目录里工作、对用户可见、对协调方可控。本指南只覆盖本体系用到的部分；完整命令面以 `orca <命令> --help` 与外挂技能 `orca-cli` 的版本匹配指南为准。

前提：项目已在指令文件中声明使用 Orca。未声明时不要把工作转到 Orca。

## 解析 CLI

按顺序解析一次，之后复用：

1. 环境变量 `ORCA_CLI_COMMAND`（Orca 托管会话会注入）；
2. PATH 上的 `orca`；
3. 都不可用时明确报告缺少 Orca，不猜测其他路径。

`ORCA` 在下文是这个可执行文件的占位符，运行前替换，不要照抄。命令默认加 `--json`。

## 建工作树并派发 agent

```text
ORCA worktree create --name <任务名> --agent <codex|claude|kimi|opencode> --prompt "<任务简报>" --json
```

- `--agent` 会把 agent 直接放进第一个终端，返回 `startupTerminal.handle`——之后只用这个 handle 寻址，不要再 `terminal create` 重复启动同一个 agent。
- 默认基于仓库默认分支、以当前上下文为父；独立顶层工作加 `--no-parent`，不要把基线悄悄压在当前特性分支上。
- 已有工作树（含手工 `git worktree add` 的）可直接挂 agent：`ORCA terminal create --worktree branch:<分支名> --command "<agent>"`。Orca 对工作树的感知不依赖谁来创建。
- 派发即用，不等完工；完工确认见下节。

## 与 worker 交互

等待与确认是两件事：`wait` 只是闹钟，完工要用可机读状态确认。

- **发送**：`terminal send --terminal <handle> --text ... --enter`。回执 `input_accepted` 只证明字节进了终端；`turn_started`（确已开工）目前仅 claude / codex / antigravity 有，kimi 与 opencode 需要读屏确认开工。
- **等待**：`terminal wait --for tui-idle --timeout-ms <ms>` 对 kimi / codex 可靠；对 opencode 会过早报 idle，改为轮询 `terminal read` 直到内容稳定。`exit` 只用于跑完即退的命令。
- **读屏差异**：codex 默认读屏即见对话；opencode 最干净；kimi 默认只回可视区（常只剩输入框），需 `--cursor 0` 读全流，流里含 spinner 动画帧，取结论要过滤噪音。
- 首次门槛：codex 首次会拦"hooks 信任"提示，远程选信任一次即可；kimi 对每棵新工作树拦一次"文件夹信任"，可按项目预置信任记录免除。

## 完工确认

派发时在 prompt 里写死完工标记，主代理醒后查标记而不是读屏幕散文：

1. worker 完工前自翻卡片：`ORCA worktree set --worktree active --workspace-status in-review`；主代理用 `worktree show --json` 读回。
2. 或走 Linear（装了 `orca-linear` 或者有linear mcp时）：worker 推票状态，主代理查票。`--current` 只在 Orca 终端内有效，普通 shell 里 cd 进去无效。
3. 物证兜底：`git log` 确认 worker 分支上的提交真实存在。

## 删除与清理

- `terminal close --terminal <handle>` 关单个终端；`terminal close --worktree <选择器> --all` 清整棵工作树的终端。
- `worktree rm --worktree <选择器>` 删工作树并尝试删其分支：**能证明已合并的分支会被一并删除**，早于工作树存在的分支会保留。想保分支先推送。
- 工作树默认落在 `<repo>/.orca/worktrees/`，项目应已在 `.gitignore` 忽略 `/.orca/`（nk-init 写入）。

## Agent 差异速查

| | codex | kimi | opencode |
|---|---|---|---|
| 开工回执 `turn_started` | 有 | 无 | 无 |
| `tui-idle` 等待 | 可靠 | 可靠 | 过早，轮询读屏替代 |
| 默认读屏 | 可见对话 | 只剩输入框，需 `--cursor 0` | 干净完整 |
| 首次门槛 | hooks 信任一次 | 每棵新工作树信任一次 | 无 |

## 已知坑

- `orca linear --json` 对含 ASCII 双引号的 CJK 正文会发射非法 JSON：正文引号用「」，调用方解析失败时回退纯文本输出，写入后一律读回验证。
- PowerShell 终端里调用带空格路径的 CLI 要用 `& "..."` 调用运算符。
- Orca 卡片与谱系是 Orca 侧元数据，不进 git 与 Linear，随时可改可清。

## Orca 技能总表

以下技能由 Orca 分发（`npx skills add stablyai/orca` 或从 `orca skills list` 查看），不属于本体系：

| 技能                       | 用途                                     |
| ------------------------ | -------------------------------------- |
| `orca-cli`               | 唯一刚需外挂：worktree / 终端 / 交接 / 内嵌浏览器的完整指南 |
| `orca-linear`            | Linear 工单读写（认领、状态、评论、阻塞关系、挂 PR）        |
| `computer-use`           | 本机 GUI 窗口操作；kimi、codex 会话用自带等价能力即可     |
| `orca-emulator-android`  | adb 安卓设备/模拟器控制                         |
| `orca-emulator`          | iOS 模拟器，仅 macOS                        |
| `orca-per-workspace-env` | 每 workspace 一次性云环境配方                   |
| `orchestration`          | Orca 原生监督协议；本体系不采用，多票调度归 nk-odyssey    |
| `linear-tickets`         | orca-linear 的旧名，兼容别名                   |
