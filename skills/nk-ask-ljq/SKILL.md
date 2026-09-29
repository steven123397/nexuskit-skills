---
name: nk-ask-ljq
description: "User-invoked guide for choosing a NexusKit entry point. Recommend a skill for the current situation, explain its inputs and expected result, and show how work moves between skills without imposing a fixed pipeline."
disable-model-invocation: true
---

# Ask ljq

不需要记住所有技能，告诉我你现在卡在哪里。

这是一张工作地图。整套安装后，任意技能都能作为入口；已有需求、Plan 或代码，就从对应位置开始。小改动不必先发想，缺陷不必先写完整 Plan，问路也不会自动启动一整条流程。

## 先回答眼前的问题

根据当前请求和已有上下文，给出**一个首选入口、一句话理由、需要带入的材料和预期结果**。只有两条路线会产生实质不同的结果时才解释分叉；信息不足以选择时，问一个能区分路线的问题。不要每次把整张地图复述给用户。

接手仓库时按需看 `docs/current.md` 和项目指导；已经知道现场就直接复用。只为选路读取必要信息，不先加载所有技能或展开全仓调查。

用户只问怎么用，就推荐后结束。用户已要求执行某项工作，选定后读取该技能的公开入口，携带原请求、范围、已有决定、证据和授权继续；遵守目标技能的调用边界。推荐一个手动技能不等于用户已调用它，问路不产生写入、提交或发布授权。

## 从想法到分支收尾

常见功能开发沿这条路走，前面已有的成果直接接上：

1. **找值得做的方向** → [nk-ideate](../nk-ideate/SKILL.md)。从项目现状发想、筛选，形成候选方向和发想记录。已有具体想法就跳过。
2. **明确做什么** → [nk-brainstorm](../nk-brainstorm/SKILL.md)。澄清目标、范围、行为和成功标准，形成需求阶段 Plan。
3. **决定怎么做** → [nk-plan](../nk-plan/SKILL.md)。补全同一份 Plan 的技术决定、实施单元和验证方式；也能直接承接清楚的请求或深化已有 Plan，不强制先 brainstorm。
4. **逐单元实现** → [nk-work](../nk-work/SKILL.md)。传入可实施 Plan 与本次 U-ID；也可承接清楚的 Issue 或有边界的请求。一次调用完成一个确认单元，验证、提交前审查和提交由它调度，汇报后结束；下一单元由后续调用启动。
5. **累计工作全部交付后收尾** → 用户调用 [nk-close](../nk-close/SKILL.md)。覆盖 Plan、关联 Issue 与临时纳入的工作，做轻量合并前检查、遗留处置、知识承接和产物清理，再协调收尾提交。收尾不等于合并或发布。

项目需要工作分支时，按项目流程从已提交 Plan 所在的最新基点进入实施。这里不另定分支或发布规则。

例如：“按这份 Plan 实现 U2。”直接交给 nk-work。它负责审查、修复单元内成立的问题，并通过 nk-commit 提交；不需要用户再依次调用 commit、simplify、review。仍有阻断就报告未完成，不能靠补跑一次提交绕过去。

## 另外几条入口

- **目标巨大、未知相互牵连，连需要决定什么都说不清** → 用户调用 [nk-wayfinder](../nk-wayfinder/SKILL.md)。用 GitHub Map 与决策 tickets 逐步探索；范围收敛后把已定决定和证据交给 nk-plan，产出同规格的可实施 Plan，再进入 work。它是一条替代探索路线，无须先经过 ideate / brainstorm，也不直接把探索 ticket 当作实施单元。
- **出错、回归、异常慢，需要查明原因或修复** → [nk-debug](../nk-debug/SKILL.md)。从复现和证据定位根因；仅诊断就交付结论，已授权修复则完成验证、审查和提交。无需为排障先走需求规划。
- **工作中发现独立需求或缺陷，先记下以后做** → [nk-to-issue](../nk-to-issue/SKILL.md)。在当前会话复用证据、核实查重，按落档授权创建或补充 Issue 后返回原任务；记录问题不等于开始实现它。

## 随时单独拿出来用的工具

| 你现在想做什么 | 入口与结果 |
| :-- | :-- |
| 首次让仓库接入 NexusKit | 用户调用 [nk-init](../nk-init/SKILL.md)，探测并补最小项目指引和 current；已有配置直接复用 |
| “这个模块我没想清楚，详细问我” | 用户调用 [nk-grill](../nk-grill/SKILL.md)，严格追问直到理解对齐；共识不自动变成 Plan 或实施授权 |
| “你刚才说的我没跟上” | 用户调用 [nk-wait-what](../nk-wait-what/SKILL.md)，由 Agent 补上下文重新解释 |
| 审查当前改动、分支或 PR | [nk-review](../nk-review/SKILL.md)，返回发现与覆盖边界，不直接修复产品代码 |
| 单独找代码精简机会 | 用户调用 [nk-simplify](../nk-simplify/SKILL.md)，分析复用、质量与效率，返回建议，不自动改代码 |
| 已有完整改动，需要提交 | [nk-commit](../nk-commit/SKILL.md)，核对范围和证据、按需同步 current 并提交；它是直接提交入口，也被其他技能调用 |
| 显式保存未完成现场 | 用户调用 [nk-handoff](../nk-handoff/SKILL.md)，保存可接手的现状；普通交付提交后不必再跑一次 |
| 留下一条可复用经验或已采纳决策 | [nk-compound](../nk-compound/SKILL.md)，检索已有知识并沉淀到 solutions；明确要求复盘时先分析，明确要求 refresh 时审计知识库 |
| 一串只能人完成的配置或操作 | 用户调用 [nk-wizard](../nk-wizard/SKILL.md)，生成交互式 Bash 向导交给人运行；脚本生成不代表操作完成 |

常规 review 已包含精简分析与独立复核；成立的问题由 work / debug 或获授权的修复工作处理。close 调用 review 的 **pre-merge** 路径检查累计成果能否一起交付，默认主会话、至多两个只读专项子代理，不重复全套常规审查。只想做这项检查时也可直接请求 `nk-review pre-merge`。

## 会话与产物怎么接上

规划阶段可以在当前会话连续推进；单元完成后可以换会话，也可以后续调用继续。不按上下文余量自动续作，不要求为了落档或下一轮探索另开会话。

接手时从 `docs/current.md` 找到实际状态，再读对应 Plan 单元及必要证据。current 的维护随提交由 nk-commit 负责；需要额外保存未完成现场时才显式调用 handoff。提交规则只由 nk-commit 持有，这里不维护副本。

Plan 承载本次交付，solutions 保存长期经验，CONCEPTS.md 保存领域术语。遇到非琐碎设计或排障时定向检索已有经验，不为了检索自动启动沉淀或全库审计。分支收尾由 close 按生命周期处理已消费产物，仍被其他工作使用的材料保留。
