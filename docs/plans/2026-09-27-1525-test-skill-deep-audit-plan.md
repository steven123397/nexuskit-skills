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

（待填。格式：技能名 → 边界与重叠观察 → token 观测（读入文件与字节）→ 触发可靠性 → 绊脚点/空缺点 → 处置（已修 commit / Issue #N / 不修及理由）。）
