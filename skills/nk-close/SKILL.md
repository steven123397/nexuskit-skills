---
name: nk-close
description: "Close a work branch before merge (or one delivered plan on single-branch projects): transfer leftovers, harvest decisions and terms, delete delivered artifacts, rewrite docs/current.md, make the single R4 close commit; release-day sweep is leak-check + tag only. 分支收尾、合并前清理、发布日扫尾、提炼删除 plan、close version。"
disable-model-invocation: true
---

# /nk-close

工作分支的一揽子工作交付完成、合并进 main 之前执行：把过程工件的长期价值提炼进知识库，清理已交付工件，让仓库干净地进入下一段工作。本技能是 [`../conventions/artifact-lifecycle.md`](../conventions/artifact-lifecycle.md) 第五章"分支收尾六步法"的可执行展开，规则以约定为准。

**两种触发（同一套六步）：**
1. **分支收尾（主路径）**：工作分支合并进 main 之前，范围为分支上的全部产物。
2. **降级路径（直推 main）**：单分支项目中某 plan 全部单元交付后，对该 plan 执行，范围收窄为该 plan 及其关联产物；无归属产物留待发布日扫尾。

**完成标志：** 遗留项与用户决策点全部处置完毕，有价值内容已提炼，已交付的 plan/审查记录已删除，范围内引用的 Issue 已兜底处置，`docs/current.md` 覆写为收尾后状态，以上改动合为一次 R4 收尾提交入库。
**工作原则：** 提炼先于删除；只删已交付完成的工件；收尾提交只含本技能涉及的文件。

---

## 用户决策点（先读，第 1/3 步会用到）

对以下两类产物**逐项询问用户**，遵循 [`../conventions/decision-autonomy.md`](../conventions/decision-autonomy.md) 第三节的批量提问规则（选项驱动、标注 `(Recommended)`、互不依赖合并为一轮、每轮最多 3 个）：

1. **未被消费的发想记录**（`docs/ideation/` 中方向未进入任何 plan 的；被长期文档如 `AGENTS.md` 引用的视为已消费，不问）：
   * 选项：保留 / 转为 Issue / 删除；推荐项按内容质量判断——仍有辨识度且可能复用则保留，值得排期则转 Issue，已被取代或无信息量则删除。
2. **推迟的 plan**：转为 GitHub Issue（Recommended，可追踪）/ 移至后续工作分支 / 其他。

无人值守时按推荐默认推进，并在 `docs/current.md` 阻断/缺口章节逐项登记 `[待确认]`。无 GitHub 远端时 Issue 降级为 `docs/backlog.md` 条目。

---

## 执行步骤

### 0. 前置检查
前提不成立时列出缺口并停下问用户，不放行：

1. **单元交付核对**：对范围内每个 plan 的每个实施单元，用 `git log --oneline --grep "(U<编号>)"` 确认存在带单元编号的验证提交（进度以提交为准，见 [`../nk-commit/SKILL.md`](../nk-commit/SKILL.md) R1）。
2. **工作区清点**：`git status` 中不应有未交代的半成品；有则先处置——能收尾的随最后单元提交，不能的登记进 `docs/current.md` 并向用户说明。
3. **验证证据核对**：交付声明必须由实际运行过的测试或走查支撑；未运行的记为未验证而非通过（证据规则见 nk-commit 第 3 步）。证据缺失时警告用户，由用户决定是否继续收尾。

### 1. 遗留项转移与甄别
范围为分支（或降级路径下该 plan）上的**全部**产物，含顺带小修产生的决策点：

* 检查 `docs/reviews/` 遗留条目（由 [nk-review](../nk-review/SKILL.md) 产生，状态标记见 [`../nk-review/references/entry-format.md`](../nk-review/references/entry-format.md)；目录不存在则跳过并说明），以及 `docs/plans/` 各 plan 的未完成待办。
* **未完成或推迟的 plan 不随本技能删除**，逐项转入"用户决策点"流程；审查记录遗留项转为 Issue。
* **Issue 兜底扫描**：处置规则见 [`../conventions/issue-writing.md`](../conventions/issue-writing.md) 第四节（逐条关闭注明提交哈希，或评论说明遗留原因）。Bash / Git Bash 下的机械方法（不直接复制到 PowerShell）：`git log <base>..HEAD --format=%B | grep -oE '#[0-9]+' | sort -u`（分支模式 base 为合并目标；降级路径取该 plan 起点），加上范围内 plan/文档中的 `#N` 引用去重，逐个 `gh issue view <N> --json state` 核对仍 open 的。

### 2. 价值提炼 (Harvest)
从即将删除的 plan 与审查记录中提炼长期价值内容，细则见 [`references/harvest.md`](references/harvest.md)：

* 架构选型与踩坑因果：先过 [`../conventions/solution-schema.md`](../conventions/solution-schema.md) 的双轨准入门槛，合格才写入 `docs/solutions/`，平庸内容不建档；
* 新稳定领域术语：按 [`../conventions/concepts-vocabulary.md`](../conventions/concepts-vocabulary.md) 写入根目录 `CONCEPTS.md`；
* 按生命周期约定第二章检查知识入口及本范围项目指导的遗漏、失效，补齐有依据的更新。

### 3. 清理已交付工件
确认第 1 步无遗留、第 2 步提炼完成后，用 `git rm` 删除本次**已交付完成**的 plan 与审查记录（`git rm` 已暂存删除，后续提交无需再 add）。只删已交付的：推迟的已转走，未消费发想记录按用户决策点处置，均不在此删除。完整设计演进由 Git 历史保留。

### 4. 准备收尾状态
整理收尾后的已具备能力、已有验证、阻断、残留与下一步，交给第 5 步的 nk-commit 统一维护 current；不在此重复覆写。

### 5. 单个收尾提交（R4）
读取 [`../nk-commit/SKILL.md`](../nk-commit/SKILL.md) 并遵循其规则：

* 本次属于 R4 规定的"分支收尾点"，允许且只发起**一次**纯文档收尾提交；
* **显式暂存并限定路径**：只含本技能涉及的文件——`docs/solutions/` 新增、`CONCEPTS.md`、`docs/current.md`、被 `git rm` 的 plan/审查记录（已暂存）、可能新增的 `docs/backlog.md`、本范围内项目指导及其索引更新。不使用 `git add -A`；
* 提交信息风格遵循项目既有惯例，不写死格式。

### 6. PR 摘要（可选）
项目走 PR 流程且用户要求时，按 [`references/pr-description.md`](references/pr-description.md) 生成 PR 描述（写 diff 看不出来的东西、长度随决策成本伸缩；对应 Issue 用 `Fixes #N` 闭环）；用户没要求则跳过。release notes 不属于本步，归发布日扫尾。

---

## 发布日扫尾（Release Day）

触发与原则（发布与收尾解耦、不做提炼删除、不带病发布）以生命周期约定第五章末节为准，此处只展开操作：

1. **漏网检查**：已交付但未删除的 plan/审查记录、未处置的发想记录、被引用但仍 open 的 Issue（核对方法同第 1 步兜底扫描）。发现漏网项：能当场补一次六步收尾的补收尾，来不及的转 Issue 并在 release notes 中说明。
2. **Release notes**：写入 `docs/releases/`。
3. **打 tag**：按项目工作流文档的版本规则执行。

本小节改动（release notes 等）允许发起一次纯文档提交（R4 分支收尾点含发布日扫尾）。
