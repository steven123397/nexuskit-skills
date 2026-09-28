---
name: nk-plan
description: "Create or enrich a technical implementation plan (HOW) for multi-step work, including non-software tasks: research, key technical decisions, implementation units, verification. Use when asked to plan, break down implementation, plan from a brainstorm/requirements doc, or deepen an existing plan; prefer nk-brainstorm for exploratory scoping. 技术规划、实施计划、拆分实施单元、补全需求文档、深化 plan。"
argument-hint: "[需求描述、需求阶段 plan 路径、要深化的 plan 路径，或任何要规划的任务]"
---

# /nk-plan

[nk-brainstorm](../nk-brainstorm/SKILL.md) 定义**做什么**，`nk-plan` 规划**怎么做**，[nk-work](../nk-work/SKILL.md) 执行。上游 brainstorm 不是必需的。

**完成标志**：产出一份能指导执行和验证的 plan，保留约定的结果和约束；技术选择以证据为依据，已经足够的说明不改动。Durable 路线要到收尾菜单的所选动作真正执行后才算完成；Direct 与 Chat brief 在聊天中给出结果和交接提议即完成。

**只调研、决策、写 plan，不实现。** 不写生产代码、不运行测试、不从执行结果中学习。方向性的伪代码或语法草图可以用来表达设计。

**plan 文件的结构契约是 [`../conventions/plan-format.md`](../conventions/plan-format.md)**：章节标题、ID 规则、frontmatter 都以它为准，本技能的 references 只补充"怎么写好"。

## 提问方式

按 [`../conventions/decision-autonomy.md`](../conventions/decision-autonomy.md)：可逆、局部、有惯例可循的事自己定并写明理由；只有答案会实质影响架构、范围、顺序或风险、又无法合理推断时才问。互不依赖的问题合并为一轮（至多 3 个），每个给 2–3 个选项并标出 `(Recommended)`；有依赖关系时才分轮。有选择题工具就用，没有时在聊天中列编号选项，不悄悄跳过必要的问题。无人值守时采用推荐项，推断项写进 plan 的 `### Assumptions`，需要确认的事项在 `docs/current.md` 登记 `[待确认]`。

没有给出要规划的内容时，先问要规划什么。

## 术语

规划中敲定了新的领域术语、或发现用词与 `CONCEPTS.md` 冲突时，按 [`../conventions/concepts-vocabulary.md`](../conventions/concepts-vocabulary.md) 当场处理：冲突当面指出并对齐，合格的新术语立即写入 `CONCEPTS.md`。

## 流程

各阶段依次执行，选定其他路线时按该路线继续。阶段规则的读取与复用遵循 [`../conventions/resource-loading.md`](../conventions/resource-loading.md)：只加载命中路线；完整且未变的原文直接复用，缺失或变化时补读。

| 阶段 | 先读 | 内容 |
| :-- | :-- | :-- |
| 0 续写、分流、定界 | [references/phase-0.md](references/phase-0.md) | 核心原则与质量底线；续写与深化快速通道；做法层规划与非软件分流；查找上游 Product Contract（含 `topic:` 识别）并就地补全；规划引导；阻塞处理；输出档位（Direct / Chat brief / Durable）与规划深度；独立规划的范围确认 |
| 0.1a 做法层规划 | [references/approach-altitude.md](references/approach-altitude.md) | 明确要求先规划做法，或用户接受该提议时读取；转入此路线 |
| 0.1b 非软件路线 | [references/universal-planning.md](references/universal-planning.md) | 非软件任务，或深化不带 frontmatter 的非软件 plan 时读取；跳过软件阶段 |
| 0.2 已定决策 | [`../conventions/settled-decisions.md`](../conventions/settled-decisions.md) | 软件路线需要判定和承接本会话决策时读取；此规则可与后续输出档位叠加 |
| 0.6 聊天输出 | [references/output-contracts.md](references/output-contracts.md) | 选定 Direct / Chat brief 后读取；Durable 不读此文件 |
| 范围确认（0.7 / 5.1.5） | [references/synthesis-summary.md](references/synthesis-summary.md) | 内部三分草稿、待确认点保留测试、确认模板、写入 plan 的去向 |
| 1 调研 | [references/research.md](references/research.md) | 本地研究员、Agent 原生能力评估、执行方向、外部调研决策与派出、整合、升档、行为追踪、流程分析、设计对比入口 |
| 1.6 设计对比（按需） | [references/design-alternatives.md](references/design-alternatives.md) | 后果重大的"怎么做"未定时，并行展开截然不同的设计并比较 |
| 2–4 问题、结构、成文 | [references/structure.md](references/structure.md) | 规划问题归类与提问；单元划分与字段；高层设计触发条件；行文与 Markdown 写法；规划规则 |
| 5.1–5.3 写前检查、写入、深化判断 | [references/final-review.md](references/final-review.md) | 写前清单；承接上游的范围确认；写入 plan；置信度检查与是否深化 |
| 5.3.3–5.3.7 深化（按需） | [references/deepening-workflow.md](references/deepening-workflow.md) | 章节打分、章节到子代理的对应、执行方式、交互审阅、整合 |
| 5.3.8 写后自检 | [references/self-review.md](references/self-review.md) | 连贯性与可行性（总是）、范围守护、安全、设计、产品、对抗性（按信号） |
| 5.4 收尾 | [references/handoff.md](references/handoff.md) | 能否交给实施；自检结果；NexusKit 收尾菜单与执行 |

调研与深化的共享角色及任务说明见 [`references/research-roles.md`](references/research-roles.md)，本技能专用角色在 `references/agents/`，是提示词资产而不是可按名字调用的 Agent：读取文件内容，用它初始化一个通用子代理。支持子代理的客户端并行派出；不支持时在主会话中依次完成。

## 始终成立的规则

* **先写文件，再给选项**：Durable 路线在展示收尾菜单前 plan 已写入 `docs/plans/`。
* **一个需求一个文件**：已有 [nk-brainstorm](../nk-brainstorm/SKILL.md) 产出的需求阶段 plan 时，就地补全同一文件，保留 Product Contract 的含义、稳定 ID、`topic:` 字段和 `<!-- nk-section: ... -->` 标记。
* **plan 不记执行进度**：没有 `status` 字段，不加复选框；进度以带 U-ID 的提交为准。
* **plan 吸收既有 Issue 即认领**：assignee 与溯源评论按 [`../conventions/issue-writing.md`](../conventions/issue-writing.md) 第三节执行，规则不重述。
* **不重问已定决策**；已定标注也不压制缺陷证据。
* **提交**：达到本阶段交付标准的仓库内 Plan 及术语交给 [nk-commit](../nk-commit/SKILL.md)，同时提供验证证据、阻断和下一步，由其维护 current 并入库；草稿暂留，无文件则不制造提交。不自动调用 handoff。
