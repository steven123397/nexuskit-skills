---
name: nk-init
description: "First-time per-repo setup for NexusKit: explore what exists, confirm the Linear team/project and GitHub wiring, then idempotently write the navigation pointers and workflow config the other skills read. Run once before first use of the other skills; no current.md, no state documents."
argument-hint: "[可选：项目根目录；默认当前目录]"
disable-model-invocation: true
---

在目标仓库首次启用 NexusKit 时运行一次，把仓库变成"体系就绪"：其他技能读的配置就位（Linear 团队与项目、外部问题的 GitHub 去向），Agent 能从全局指令文件找到术语与关键决策。全程幂等，重复运行只报告现状；已存在的内容一律跳过并说明，不覆盖既有内容。

## 1. 探测

先读仓库，不凭空发问：

- `git remote -v` 与 `gh` 可用性：有无 GitHub 远端，决定外部问题记录走 GitHub Issues 还是降级 `docs/backlog.md`。
- 根目录的 `AGENTS.md` / `CLAUDE.md`：哪个存在，是否已有技能配置块或指向 `CONCEPTS.md`、`docs/adr/` 的指引。
- `CONCEPTS.md`（或 `CONCEPTS-MAP.md`）与 `docs/adr/` 是否已存在；多域信号（workspace 清单、有独立 `src/` 的 `packages/*`、多个自成体系的域目录）——存在时按多上下文组织；`docs/agents/issue-tracker.md` 是否已有配置记录（或导航块指向的替代位置）。
- Orca 可用性：自身是否运行在 Orca 托管终端中（`ORCA_CLI_COMMAND`、`ORCA_PANE_KEY` 等环境变量），PATH 上是否有 `orca` CLI（`command -v orca`），外挂技能 `orca-cli` 是否可读。只探测，不安装。

## 2. 展示并确认

汇总已有与缺失，然后逐项确认；每项带推荐答案，探测已能确定的直接说明不提问：

- **Linear 团队与项目**：spec 与 tickets 的去向，`nk-to-spec`、`nk-to-tickets`、`nk-odyssey` 都读它。这无法探测，需要用户提供团队名与项目名。
- **外部问题记录**：有 GitHub 远端且 `gh` 可用时推荐 GitHub Issues（`nk-to-issue` 的目标）；无远端时降级 `docs/backlog.md` 并说明。
- **配置落点**：默认写 `docs/agents/issue-tracker.md`——`nk-to-spec`、`nk-to-tickets`、`nk-odyssey`、`nk-wayfinder` 固定读它。项目已有自己的工作流文档时从其约定，导航指针指向实际位置。
- **是否使用 Orca**：CLI 与 `orca-cli` 技能都探测到时才提问，询问本项目开发是否用 Orca 管理工作树与 agent 派发；`orca-cli` 缺失但 CLI 可用时，提示用户用 `npx skills add stablyai/orca --skill orca-cli` 安装，再决定是否启用。CLI 都不可用时按不使用处理并说明，不提问。

## 3. 写入

- **选文件**：`CLAUDE.md` 存在则编辑它，否则用 `AGENTS.md`；两者都不存在时问用户建哪个，不代选。已有配置块就地更新，不追加重复，不覆盖用户对周边内容的编辑。
- **导航块**指向术语、关键决定与工作流配置——形如"术语见 `CONCEPTS.md`（多上下文项目指 `CONCEPTS-MAP.md`，布局机制归 `nk-domain-modeling`），关键决定见 `docs/adr/`，工作流配置见 `<配置落点>`"。保持克制的指针，不把细则堆进常驻上下文。
- **配置文件** `docs/agents/issue-tracker.md`：记录 Linear 团队与项目、GitHub 仓库与降级路径，一段平实说明即可。项目约定了别的位置时写那里，导航块指过去。
- **Orca 接入**（仅当用户确认使用且探测齐备）：`.gitignore` 追加 `/.orca/`（已覆盖则跳过）；按选文件规则在指令文件中简短声明——本项目开发使用 Orca 管理工作树与 agent 派发，用法见 `nk-orca-guide`。声明保持一两句，不复述指南内容。
- **惰性创建**：不预建 `CONCEPTS.md`（第一个合格词条创建，归 `nk-domain-modeling`）、不预建空的 `docs/adr/`（第一个决定创建）、不预建降级 `docs/backlog.md`（无远端且需要时才建）。git 不跟踪空目录，产物由使用产生。
- 不生成状态文档或通用约定加载层；不迁移既有产物（历史材料迁移是单独工作）；不修改项目代码。

## 4. 提交与收尾

初始化产物是本次交付物，提交走 `nk-commit`（配置文件与指令文件改动同次入库）。没有可交付改动则直接报告现状。

收尾告知：哪些技能现在会读这些配置——`nk-to-spec` / `nk-to-tickets` / `nk-odyssey` / `nk-wayfinder` 读 Linear 配置，`nk-to-issue` 读 GitHub 去向，`nk-domain-modeling` 维护术语与 `docs/adr/`。之后可直接编辑这些文件；重跑本技能只在更换去向或从头再来时需要。可以从 `nk-ask-ljq`（场景路由）或直接描述任务开始。
