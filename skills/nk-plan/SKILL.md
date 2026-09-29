---
name: nk-plan
description: "Create or enrich a technical implementation plan (HOW) for multi-step work, including non-software tasks: research, key technical decisions, implementation units, verification. Use when asked to plan, break down implementation, plan from a brainstorm/requirements doc, or deepen an existing plan; prefer nk-brainstorm for exploratory scoping. 技术规划、实施计划、拆分实施单元、补全需求文档、深化 plan。"
argument-hint: "[需求描述、需求阶段 plan 路径、要深化的 plan 路径，或任何要规划的任务]"
---

# /nk-plan

规划如何实施和验证。[nk-brainstorm](../nk-brainstorm/SKILL.md) 可提供需求但不是前置条件。只调研、决策、写 Plan，不写生产代码、不运行测试。

完成条件：对应结果已交付；Durable Plan 已成文、完成必要深化和自检，合格仓库产物已提交，阻断与下一步已说明。等待后续选择不影响规划完成；只有已有实施授权才继续实施。

## 全程底线

<!-- fragment: planning-autonomy -->
能从现状或已有决定推断的局部选择自行处理并说明理由；只有尚未授权、会实质改变范围、顺序、风险或外部契约的分歧才问。独立问题合并，每轮至多 3 个；决策给 2–3 个选项与推荐，事实和意图允许开放提问。明确续作或“改后继续”的授权仍有效，范围未变不重复确认。
<!-- /fragment -->

<!-- fragment: planning-settled -->
用户看过取舍后选定的决定直接承接；未经检验的指示只在相关阶段检验一次，Agent 自己的推断不冒充已定。最新明确修订替换冲突的旧内容，保留其余有效决定。已定不压制反证：次优但可行则沿用，证据表明不可行、偏离目标或有破坏性时说明并阻断。
<!-- /fragment -->

<!-- fragment: planning-terms -->
使用 CONCEPTS.md 的规范名称；冲突影响决定时当场对齐，用具体场景检验概念边界。领域专属且独立的术语敲定即新增或完善，一句话定义，必要时加别名和行为规则；不收实现细节。文件缺失可为本次术语创建，不扩成全仓初建；不在需求与规划中合并、退役或删除词条。
<!-- /fragment -->

<!-- fragment: planning-reading -->
只加载本次路线和选中角色所需材料。上下文中完整、适用且未变的原文直接复用，缺失或变化才补读；阶段切换不触发重读。必需材料缺失且无降级路径时，停在其管辖动作之前。
<!-- /fragment -->

维护源：[提问](../conventions/decision-autonomy.md)、[已定决策](../conventions/settled-decisions.md)、[术语](../conventions/concepts-vocabulary.md)、[读取](../conventions/resource-loading.md)。完整分类、标注和词条格式按需加载。无人值守推断进 Assumptions；反证使已定决定失效则阻断，不以假设覆盖。

## 1. 承接输入并选路线

无输入先问规划什么。读 [phase-0.md](references/phase-0.md) 定位目标、上游产物与阻塞，并确定路线。相关文档不自动扩大范围或升档。

- 重新深化完整软件 Plan：加载第 3 步的成文材料，进入第 5 步交互深化。
- 先规划做法：读 [approach-altitude.md](references/approach-altitude.md)，停在做法检查点，已授权下一步则继续。
- 非软件任务：读 [universal-planning.md](references/universal-planning.md)，按该路线交付。
- Direct / Chat brief：读 [output-contracts.md](references/output-contracts.md)，在聊天交付，跳过 Durable 流程。
- Durable：按以下步骤继续。需求阶段 Plan 就地补全；独立规划新建完整 Plan。

纳入既有 Issue 时按 [issue-writing.md](../conventions/issue-writing.md) 第三节认领。Plan 不记执行进度，不设 status 或复选框；进度由带 U-ID 的提交承载。

## 2. 定界并补齐规划证据

独立规划在调研前呈现范围；承接上游时在第 4 步写前呈现规划覆盖和取舍，避免两处重复确认。续写与深化不重复完整综述。

综述直接读 [scope-synthesis.md](../conventions/scope-synthesis.md)，使用“规划综述”预算。Lightweight 无待确认点时说明后继续；其余情况保留整体确认检查点，但已有覆盖当前动作的明确授权且无新分歧时不重复等待。用户跳过确认或无人值守时，未经确认的推断记为 Assumptions。

读 [research.md](references/research.md)，先接收上游证据，按规划缺口补本地、经验和必要的外部研究。派发时读 [research-roles.md](references/research-roles.md) 及选中方法，深化时复用。支持且允许委派才派发，否则内联并说明。

需要比较后果重大、难以推翻的技术做法时，由本入口加载 [design-alternatives.md](references/design-alternatives.md)，比较后返回第 3 步。调研无此信号就直接继续。

## 3. 决定做法与实施单元

读 [structure.md](references/structure.md) 形成技术决定、依赖顺序、单元、测试场景和验证方式。同时加载 [Plan 格式](../conventions/plan-format.md)；记录已定来源时加载 [标注规则](../conventions/settled-decisions.md)。

保留上游含义、稳定 ID、topic 与语义标记；落实已授权修订，其他产品变化先解决。独立规划补齐 Product Contract。单元追溯需求，写明文件、测试场景及验证；实现期未知明确推迟。

## 4. 检查并写入

读 [final-review.md](references/final-review.md) 核对写前条件与写入要求。承接上游时在此按第 2 步方法确认规划覆盖，不重新打开已定产品问题。通过后写入同一文件或新建完整 Plan；先写文件再交付结果。

修改后复查受影响项，图与草图效力按 structure 判断。

## 5. 按需深化与写后自检

评估深度、依据及认证、支付、迁移、外部集成、隐私、多端和发布风险。轻量通常不深化，其余按缺口加强。本地依据薄弱触发外部研究，或外部发现实质塑造 Plan 时，必须进入章节评分，但不强制产生深化任务。

需要评分或用户要求深化时读 [deepening-workflow.md](references/deepening-workflow.md)，复用或加载第 2 步角色任务材料；生成时自动整合，重新深化时交互接受/拒绝。只补选中章节，返回变化、依据和未决项；无缺口则继续。

对实际 Plan 按 [self-review.md](references/self-review.md) 做写后自检：连贯性与可行性始终检查，其他视角按信号选择。已有自检仍有效且此次未改文件时复用；没有有效自检则补做，不能因深化无发现而默认通过。修正后只复查受影响部分，留下真正需要用户决定的事项。

## 6. 提交并交付

合格 Plan 与术语经 [nk-commit](../nk-commit/SKILL.md) 携证据、阻断和下一步提交，由其维护 current。草稿暂留，不自动调用 nk-handoff。

用一行说明自检结果，给出 Plan 绝对路径、已有提交、开工阻断和首个可执行单元。未满足开工前置条件时不提供实施选项。

- 已授权下一步：直接执行；用户要求规划后停下则结束。
- 无后续授权：可建议新会话接手（默认）、本会话实施、处理遗留决定或继续深化；交付后结束，用户选择时再继续，不强制菜单往返。
- 本会话实施：确认无开工阻断后加载 [nk-work](../nk-work/SKILL.md)，传 Plan 路径与首个单元；非代码交付按 execution: knowledge-work 承接。无法调用则说明未开始并提供交接说明。
- 修改或深化：返回对应步骤并复查，仅新增完整变化再次提交。

仅清理本轮专有、已消费且不再引用的临时材料，保留上游档案；无法清理则说明位置。
