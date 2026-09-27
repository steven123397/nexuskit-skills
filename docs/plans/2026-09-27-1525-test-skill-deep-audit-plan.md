---
title: "技能逐个深读审计与微项目实跑 - Plan"
type: test
date: 2026-09-27
plan_contract: nk-plan/v1
product_contract_source: nk-plan
topic: skill-deep-audit
---

# 技能逐个深读审计与微项目实跑 - Plan

## Goal Capsule

- **Objective**：用户对 18 个 `nk-*` 技能完成逐字深读，每个技能在受控微项目中真实触发至少一次；绊脚点、空缺点、token 浪费与重复输入全部浮出水面并被归置（小修直接改、大修落 Issue）。
- **Means**：附录 A 的"阅读顺序=实跑顺序"叙事表 + 仓库外沙盒微项目（KTD2）；审计对话常开，发现按 R3 分级处置。
- **权威顺序与停止条件**：用户现场判断为最高权威；发现需要推翻已定决策（settled decisions）或大规模重写冲动时，停下报告，不在审计会话中直接动手。

## Product Contract

### Summary

v0.1.1 之后的质量回看轮。动机有二：用户尚未逐字深读过各技能全文，凭印象迭代已有"逻辑堆砌而非优化"的征兆（nk-close 字节顶格、规则一度双处重复）；全部技能从未在受控小项目中完整实跑过。本轮以"删和合并"为默认姿势，产出作为 v0.2.0 方向的输入。

### Problem Frame

技能体系由多轮增量迭代堆成，单轮看每步都合理，整体看可能有冗余、重复与空转。paper-30min 迁移开发周期长、技能覆盖不全，不适合做技能测试床；需要一个极小的、可快速重启的沙盒项目把 18 个技能全部真实跑一遍。

### Requirements

R1. 逐技能四问审计：边界是否与相邻技能/约定重叠、token 成本（SKILL.md 注入字节 + references 按需加载是否真按需）、触发可靠性、实战绊脚点。阅读顺序与实跑顺序一致，按附录 A 表执行。
R2. 微项目沙盒承载实跑：仓库外独立目录、自身 git 仓库；先无远端跑一段（验证 `docs/backlog.md` 降级路径），后挂私有 GitHub 远端（验证 gh 链路、Issue 闭环、nk-wayfinder）。
R3. 发现分级处置：小问题在审计会话中直接修（修 `skills/` 后必跑 `python tests/run_checks.py`）；够分量的落 Issue；疑似推翻已定决策的停下报告。
R4. 每个技能留一段审计结论（写在哪见 KTD5）；最终汇总为下一轮迭代的输入。
R5. 顺带收集：Issue #2 的中文触发观察案例（每个技能触发成功与否随手记）；若审计中产生修订重复提示词的需要，Issue #1 的触发时机即到达，当场评估终局方案。

### Success Criteria

- 18 个技能全部完成"深读 + 沙盒真实触发 + 一段结论"三件套。
- 每个技能的 token 观测有记录：触发后实际读入了哪些文件、各多少字节。
- 所有发现均有归处：修复提交（带验证）或 Issue。
- `python tests/run_checks.py` 全绿贯穿全程。

### Scope Boundaries

- 不做大规模重写与体系级重构——审计产出的改进方向是下一轮的事。
- paper-30min 迁移验收不在本轮范围。
- `tests/run_checks.py` 本身不改，除非审计发现它有 bug。
- 中文 description 只观察收集，不修改（修改归 Issue #2 拍板后）。

### Sources

- 用户 2026-09-27 会话拍板的本轮安排。
- Issue [#1](https://github.com/steven123397/nexuskit-skills/issues/1)、[#2](https://github.com/steven123397/nexuskit-skills/issues/2)。

## Planning Contract

### 关键技术决策

KTD1. **阅读顺序 = 实跑顺序**，按"一次完整功能开发"的叙事排布（附录 A）：沙盒从 `nk-init` 起步，经历发想→澄清→盘问→规划→实施→调试→精简→审查→沉淀→收尾→交接的完整循环，`nk-wayfinder` 与 `nk-wizard` 两个独立场景放在末位。理由：叙事连贯，沙盒的 git 历史与 docs 产物自然长成，nk-close/nk-handoff 到点时才有真实材料可消费。 (session-settled: user-approved)

KTD2. **沙盒位置在仓库外**：`D:\codex_project\nexuskit-audit-sandbox\`，独立 git 仓库，不挂本仓库。理由：`tests/run_checks.py` 全仓 glob `**/*.md`，沙盒内置会污染链接与引用检查；沙盒是一次性产物；插件按用户安装，任意目录都能消费技能。

KTD3. **远端两段式**：沙盒先以无远端状态运行前半程（覆盖 `docs/backlog.md` 降级路径），挂上私有 GitHub 沙盒仓后跑 nk-wayfinder、Issue 闭环、PR 流程。一次审计同时覆盖两条链路。

KTD4. **token 观测方法**：每个技能触发后记录实际读入上下文的文件清单与字节数（SKILL.md 本体 + 被拉入的 references 层数），主对话载入与子代理派发分别记录。数据记在审计记录里，不追求精确计量，追求发现"谁把谁不必要地拉了进来"。

KTD5. **审计结论的落点**：每个技能的结论直接以追加段落的形式写在本 plan 的附录 B（一段技能一节）。审计是短期产物，本 plan 在分支收尾时按生命周期删除——需要长期保留的改进方向届时转入 Issue 或 v0.2.0 规划，不靠本 plan 留存。

### 假设

- 审计在新会话进行；本会话只产出本 plan 与分支。
- 微项目主题为极简软件小工具（如一个几十行的 CLI），够用即可，不追求功能完整。
- 沙盒目录 `D:\codex_project\nexuskit-audit-sandbox` 可用；私有 GitHub 沙盒仓在跑到第 17 步前创建即可。

## Implementation Units

### U1. 沙盒脚手架与微项目骨架

- **Goal**：沙盒目录可用，微项目有一个能被后续 16 个技能反复折腾的最小载体。
- **Requirements**：R2（KTD2、KTD3 前半段）。
- **Files**：仓库外 `D:\codex_project\nexuskit-audit-sandbox\`（不入本仓库）；微项目骨架（用户选定的极简 CLI）。
- **Approach**：`git init`；放一个故意带一个小 bug、一个可精简点的最小代码文件；无远端起步。
- **Test scenarios**：沙盒在 Kimi Code / Codex 中打开后技能列表可见（正常路径）；`nk-init` 能跑通（集成，U2 第 1 步正式消费）。
- **Verification**：沙盒目录存在、git 仓库可提交、客户端能看到 nk-* 技能。

### U2. 逐技能审计与实跑（滚动单元）

- **Goal**：按附录 A 顺序完成 18 个技能的三件套（深读、实跑、结论）。
- **Requirements**：R1、R2、R3、R5（KTD1、KTD3、KTD4、KTD5）。
- **Dependencies**：U1。
- **Files**：被修订的技能正文（`skills/` 下，小修直接改）；本 plan 附录 B（结论）。
- **Approach**：每个技能一轮——先逐字读正文与被引用的约定/references（记录读入字节），再在沙盒真实触发一遍，四问过一遍，结论写附录 B；小修当场改并跑检查；够分量的落 Issue。一个会话跑 2~4 个技能为宜，会话间用 `nk-handoff` 交接。
- **Test scenarios**：每技能的实跑即测试；改动 `skills/` 后 `python tests/run_checks.py` 全绿（正常路径）；Issue #2 触发案例持续收集（边界）。
- **Verification**：附录 B 满 18 节；token 观测记录完整。

### U3. 汇总与下一轮输入

- **Goal**：审计结论收敛为明确的改进方向清单。
- **Requirements**：R4。
- **Dependencies**：U2。
- **Files**：本 plan 附录 B 定稿；必要的 Issue 落档。
- **Approach**：通读附录 B，把同类问题合并成主题；每个主题给出"下轮修 / 落 Issue / 不修"的判定；为用户口述 v0.2.0 安排做准备。
- **Test scenarios**：无（知识工作）。
- **Verification**：用户确认汇总结论。

## Verification Contract

- `python tests/run_checks.py`：任何 `skills/` 或 `skills/conventions/` 改动后必跑，全绿。
- 沙盒侧无机械检查；以"每个技能真实触发过"的用户确认为准。

## Definition of Done

- 附录 B 满 18 节，token 观测齐全。
- 发现全部归置：小修已提交（带 run_checks 证据），大修已落 Issue。
- Issue #2 攒到若干真实触发案例；Issue #1 若触发则有当场评估记录。
- U3 汇总经用户确认；分支收尾（nk-close）时本 plan 提炼后删除。

## Appendix

### A. 阅读与实跑顺序表（叙事序）

| # | 技能 | 沙盒场景 | 环境门槛 |
| :-- | :-- | :-- | :-- |
| 1 | `nk-init` | 沙盒首次启用体系：建 AGENTS.md 指引、current.md | 无 |
| 2 | `nk-ask-ljq` | 问路由："我想给这个小工具加功能，该怎么走" | 无 |
| 3 | `nk-ideate` | 对微项目发想改进方向，产出 `docs/ideation/` | 无 |
| 4 | `nk-brainstorm` | 挑一个方向澄清需求（观察术语即时写入） | 无 |
| 5 | `nk-grill` | 对刚产出的需求/plan 手动盘问，体验豁免上限后的前沿轮次 | 用户坐对面 |
| 6 | `nk-plan` | 补全实施部分（观察研究员/深化派发与 token 消耗） | 无 |
| 7 | `nk-work` | 执行实施单元（测试先行、提交携带 U-ID） | 无 |
| 8 | `nk-commit` | 随 nk-work 观察提交节奏执行 | 无（伴随观察） |
| 9 | `nk-to-issue` | 实施中制造一个发现，落档（此时无远端 → 验证 `docs/backlog.md` 降级） | 无远端（刻意） |
| 10 | `nk-debug` | 修骨架里故意埋的 bug（复现优先硬关卡） | 无 |
| 11 | `nk-simplify` | 实施后精简 | 无 |
| 12 | `nk-wait-what` | 故意让 Agent 发散（或长对话后）重对齐 | 无 |
| 13 | `nk-review` | 对沙盒分支 diff 审查，产出 `docs/reviews/` | 无 |
| 14 | `nk-compound` | 沉淀一条踩坑/决策；可顺带跑一次审计模式 | 无 |
| 15 | `nk-close` | 分支收尾六步（此时沙盒已有 plan/review/backlog 全套材料） | 无 |
| 16 | `nk-handoff` | 会话交接（审计跨会话时自然多次使用） | 无（伴随使用） |
| 17 | `nk-wayfinder` | 挂私有 GitHub 远端后，给一个偏大的目标跑决策地图 | 需 GitHub 远端 + gh |
| 18 | `nk-wizard` | 定义一个手动操作流程（如改环境变量 + 重启验证）走一遍 | 无 |

注：17 之后再补一轮 nk-to-issue / nk-close 的 Issue 闭环（有远端后 `gh` 路径），验证 R3 的关闭时机与 `Fixes #N`。

### B. 审计结论（每技能一节，滚动追加）

### 1. `nk-init`

- **边界与重叠观察**：职责清晰，负责首次启用与最小初始化；`nk-work` 的 Orient 只读取既有状态，不应重复初始化。
- **Token 观测**：本次实际读取 `skills/nk-init/SKILL.md`（4,916 B）、`skills/conventions/current-md.md`（5,245 B）和 `skills/nk-commit/SKILL.md`（6,618 B），合计 16,779 UTF-8 字节；未读取不存在的 `references/` 目录。
- **触发可靠性**：技能标注 `disable-model-invocation: true`，手动调用路径明确。沙盒无远端、`gh` 可用，按规则无需询问远端选择，实际创建 `AGENTS.md`、`docs/current.md` 与 `docs/backlog.md` 并提交。
- **绊脚点/空缺点**：初始化提交后 `docs/current.md` 的 HEAD 只能记录提交前哈希，否则再次改写会造成自指循环；这是状态文档约定的正常边界。沙盒已有 `.audit-probes/` 未跟踪材料，技能只暂存初始化产物，未误纳入提交。
- **处置**：不修。U1 沙盒提交 `4474f70`；本次初始化提交 `f5e0688`（工作区保留审计探针未跟踪文件）。

### 2. `nk-ask-ljq`

- **边界与重叠观察**：它只做场景路由与体系入口说明，不承接需求澄清或实现；“工具箱而非流水线”的总规则与各场景入口集中在此，和 README 路由表存在维护同步风险。
- **Token 观测**：本次读取 `skills/nk-ask-ljq/SKILL.md`（4,937 B）；未拉入 references。
- **触发可靠性**：技能标注 `disable-model-invocation: true`，对“给这个小工具加功能，该怎么走”可稳定路由到 `/nk-brainstorm`（若没有具体想法则先 `/nk-ideate`）。实际用沙盒 notes CLI 场景完成了该路由判断。
- **绊脚点/空缺点**：路由图把 `/nk-commit` 列为独立步骤，但 `nk-work` 已要求按提交节奏执行，初次使用者可能重复调用；正文虽说明可跳过，但没有在该节点给出“随 nk-work 观察即可”的明确提示。
- **处置**：不修。后续审计 README 与该正文时一并核对；若发现文案漂移再落 Issue。

### 3. `nk-brainstorm`

- **边界与重叠观察**：与 `nk-plan` 的分界由 Product Contract / Planning Contract 明确；但轻量、需求已清晰时，规则允许只在对话中对齐，若仓库已有 Product Contract 又会被 `nk-plan` 的阶段判断拉入 Durable 路径，存在“已有产物改变路线”的隐性耦合。
- **Token 观测**：规划探针记录了 27 个实际读取文件，去重合计 172,937 UTF-8 字节；其中本技能正文与 references 按文件记录在沙盒 `.audit-probes/planning/execution-log.md`。该轮为模型模拟，未由客户端自动触发。
- **触发可靠性**：未做客户端触发；模拟对“给 notes CLI 加可选标签”能判为 Lightweight，并能生成需求方向。
- **绊脚点/空缺点**：轻量请求遇到预存 Product Contract 时，阶段路由没有把“继续已有产物”与“重新判断规模”的优先级写成单一规则。
- **处置**：Issue 候选，暂不改动；需要在后续真实会话确认是否稳定复现。

### 4. `nk-plan`

- **边界与重叠观察**：Planning Contract、Implementation Units 和 Verification Contract 的分层完整；与 `nk-work` 的交接点依赖 plan 是否已经“可实施”，但该判定分散在 phase-0、structure、final-review 多份 reference 中。
- **Token 观测**：规划探针完整读取本技能相关文件，修正后的去重总量为 172,937 UTF-8 字节（见 `.audit-probes/planning/execution-log.md`）；本轮未进行客户端真实触发。
- **触发可靠性**：模拟可沿预存 Product Contract 继续生成 plan；`session-settled` 标记能被继承，但没有证据表明客户端会自动完成所要求的一次挑战。
- **绊脚点/空缺点**：`session-settled` 只记录来源，不记录挑战发生的日期、阶段或证据，后续 Agent 难以判断“一次挑战”是否已经完成。
- **处置**：Issue 候选，暂不改动；需要用户确认该审计结论后再决定是否扩展 settled-decision schema。

### 5. Issue #9：提交节奏命令的 PowerShell 兼容性

- **复现**：在 Windows PowerShell 执行未加引号的 `git rev-parse --abbrev-ref @{u}`，解析阶段报 `Missing '=' operator after key in hash literal`；执行 `git rev-parse --abbrev-ref '@{u}'` 正常返回 `origin/feat/skill-deep-audit`。
- **根因**：`@{u}` 同时是 Git revision 语法和 PowerShell 哈希表字面量前缀，技能与共享约定的示例没有保护该 token；`nk-review` 范围探针还使用 `&&` 链式命令，与“每条命令独立执行”的纪律冲突。
- **处置**：统一为 `git rev-parse --abbrev-ref '@{u}'`、`git log '@{u}..HEAD'`，并拆开审查范围探针中的链式命令；不改变提交节奏判定逻辑。修复后运行 PowerShell 复现命令、`python -X utf8 tests/run_checks.py`，并关闭 Issue #9。

### 6. `nk-wait-what`

- **边界与重叠观察**：技能只负责重新对齐，不替代 `nk-brainstorm` 或 `nk-plan` 的需求/规划流程。
- **Token 观测**：正文 575 UTF-8 字节；模拟时同时读取项目术语表与当前对话输入，未做客户端上下文计量。
- **触发可靠性**：未做客户端自动触发；模拟输入“这不对，我没说要标签功能；重新来”能够得到重新表述提示。
- **绊脚点/空缺点**：没有明确清理已生成 Product Contract 的分支，也没有把“用户纠正”与“回答当前确认问题”分流；重新对齐后可能继续消费过期产物。
- **处置**：Issue 候选，暂不改动；需在真实 brainstorm → wait-what 连续会话中复现后定级。
