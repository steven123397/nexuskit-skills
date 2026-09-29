---
name: nk-brainstorm
description: "Clarify what to build through dialogue: goals, product behavior, scope, and success criteria. Produce a requirements-stage Plan for nk-plan to complete. Use for an existing idea that needs definition; use nk-ideate to find ideas, nk-plan to plan implementation, or nk-work to execute specified work."
---

# /nk-brainstorm

明确目标、范围和成功标准；技术本身是讨论对象时可深入，其他实现选择留给 [nk-plan](../nk-plan/SKILL.md)。不写代码，交付聊天结论或需求阶段 Plan。

完成条件：结果不需规划者发明产品行为；文件通过规划就绪检查，术语已维护，合格仓库产物已提交，下一步已说明。不以用户选择后续技能作为完成前提。

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

维护源：[提问](../conventions/decision-autonomy.md)、[已定决策](../conventions/settled-decisions.md)、[术语](../conventions/concepts-vocabulary.md)、[读取](../conventions/resource-loading.md)。完整分类、标注和词条格式按需加载。用宿主提问工具或编号列表；无人值守记假设与待确认项，不伪造确认或解除产品阻塞。

## 1. 定位输入与路线

没有需求描述先问主题。读 [phase-0.md](references/phase-0.md) 定位已有需求、当前意图、工作规模与单一成果；只补缺失的分级依据。

- 简单求助、事实问题、单步任务：直接回答结束。
- 非软件探索：读 [universal-brainstorming.md](references/universal-brainstorming.md)，替代以下软件流程。
- 需求已明确：复用现状，跳过重复访谈和侦察，进入第 3 步综述；尚有局部问题只补那部分。
- Lightweight：有限阅读和必要澄清后进入第 3 步，通常在聊天交付，不派侦察、不生成方案菜单。
- 其余软件探索：进入第 2 步。Standard/Deep 可用宿主任务跟踪展示进展，无此能力不模拟清单。

以 Issue 为需求来源时，按 [issue-writing.md](../conventions/issue-writing.md) 第三节认领；方向否决时退回，不把认领当成实施完成。

## 2. 探索需求与方案

读 [dialogue.md](references/dialogue.md)，按当前规模做产品压力测试、对话和组合后果检查。已有充分答案不再追问。需要补仓库证据时，读 [evidence.md](references/evidence.md) 的侦察方法；支持且允许子代理时派发，否则内联完成。对话、取舍与需求决定由主会话负责。

条件材料在需要时由此加载，完成后回到当前讨论：

- 用户无法评估陌生领域的选择：读 [blindspot-pass.md](references/blindspot-pass.md)，征得同意后梳理决策地图。
- 形状、布局、状态或关系决定：读 [visual-probes.md](references/visual-probes.md)，沿用已有表达偏好，按判断需要给轻量草图。
- 决定推翻代价高，且对话或草图无法判断真实手感、动效、数据表现：提议先以一次性原型消除未知，再规划依赖它的工作，不在这里实施；用户拒绝且问题未变不再提议。

对话出口满足后，仍有合理的产品方向可比较时读 [approaches.md](references/approaches.md)。先展示差异再评价，推荐简单而有价值的方向；没有真实备选不凑菜单。

## 3. 综述范围并核实声明

按 [scope-synthesis.md](../conventions/scope-synthesis.md) 的“产品需求综述”整理。所有软件规模都走此步，只确认产品范围；实现做法留给规划。

- Lightweight 且之前未问阻塞问题：一段话说明决定及去处，直接继续。
- 其余情况：呈现范围、取舍、排除和必要待确认点。尚无覆盖本次写入或继续动作的授权时等待整体确认；已有明确授权且无新分歧则说明后继续。修订按共享方法处理，不自动再要一次批准。
- 用户改换目标或流程时，停止沿用冲突范围；按最新意图继续澄清或建议其他公开技能入口。

将写入可检查的仓库断言、且属于非轻量宣告路径时，用 [evidence.md](references/evidence.md) 的声明核实方法。可与用户确认并行，但写入前必须消费结果；没有等待环节也不跳过应有核实。

## 4. 形成结果并检查

按 [sections.md](references/sections.md) 判断是否需要文件。需要文件时，同时加载 [plan-format.md](../conventions/plan-format.md) 与 [已定标注](../conventions/settled-decisions.md)，写入或更新同一需求文件。仅写 Goal Capsule 与 Product Contract，不建空实施章节。

修正驳斥项、标明未核实假设并核对术语。对实际文件做四项规划就绪检查，修改后复查受影响项。Resolve Before Planning 未解决则草稿暂留并报告阻塞；用户要求继续须逐项确定假设或规划期问题，不能只改标签。

无需文件时直接交付范围、关键决定和成功信号，不制造文件或提交。即时术语改动若没有本阶段文件可一并交付，说明暂留。

## 5. 提交与交付

合格仓库内需求产物及相关术语交给 [nk-commit](../nk-commit/SKILL.md)，提供范围、检查证据、阻断和下一步，由其维护 current 并提交。草稿不提交；切换技能或后续结束时不重复提交，不自动调用 nk-handoff。

汇报决定、文件绝对路径、提交或暂留状态及下一步，空项省略。已有下一步授权就直接执行；否则简短提供适用选择：继续规划、继续澄清、结束，有文件时还可选择需求自查。交付后即可结束。

- 继续规划且无产品阻塞：加载 [nk-plan](../nk-plan/SKILL.md)，传 Plan 路径或聊天决定、有效证据路径与覆盖摘要；档案缺失如实说明，不为交接重跑侦察。
- 继续澄清：回到第 2 步，更新受影响结果与检查。
- 需求自查：读 sections 的自查方法及 evidence 的派发方法，核实修改后复查受影响项，交付新增变化。
- 仍有阻塞或用户暂停：报告剩余问题及恢复方式，保留有效产物，不自动保存现场或调用其他技能。
