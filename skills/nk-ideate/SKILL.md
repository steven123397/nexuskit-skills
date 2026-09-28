---
name: nk-ideate
description: "Generate and critique grounded ideas before choosing what to build: many candidates from six lenses, adversarial filtering, ranked survivors saved to docs/ideation/. Use when the user wants ideas, improvements, or surprising directions. Not for refining an idea they already have (nk-brainstorm). 发想、找改进方向、有什么值得做、给点点子。"
argument-hint: "[主题、关注点或约束，可选；可带 'go deep'、'quick wins'、'top 3' 等]"
---

# /nk-ideate

文档日期与近期判断使用当前环境的日期。

`nk-ideate` 在 [nk-brainstorm](../nk-brainstorm/SKILL.md) 之前使用：它回答"哪些想法值得探索"；[nk-brainstorm](../nk-brainstorm/SKILL.md) 回答"选中的那个想法具体做成什么样"；[nk-plan](../nk-plan/SKILL.md) 回答"怎么做"。

**完成标志：** 一份排好序的发想记录已写入目标仓库 `docs/ideation/`（非仓库主题写入系统临时目录）；每个候选想法都经过批判，留下的想法都说明了理由，被淘汰的都写了原因；用户面前是下一步菜单。本技能不产出需求、plan 或代码。

## 基本原则

1. **先扎根再发想。** 不给脱离仓库或用户材料的泛泛建议。
2. **先大量生成，再全部批判，只解释留下的。** 完整候选清单生成之后才开始批判；淘汰要明说并附理由，不做乐观排序。
3. **要落地就交给 brainstorm。** 不从发想结果直接跳到 plan 或实施。
4. **主题不明确时不派发子代理。** 先问清楚"发想什么"，问法见 [references/scope-gates.md](references/scope-gates.md)。"给我惊喜"（Surprise me）始终是正式选项，同时提供干净退出的"取消"。不问方案方向、约束、受众、语气或成功标准，这些归 [nk-brainstorm](../nk-brainstorm/SKILL.md)。发想阶段累计超过 3 个问题，说明这件事不该用发想流程。
5. **内部分类标签不外露。** `repo-grounded`、`elsewhere-software`、`elsewhere-non-software` 只用于决定派发哪些代理；对用户用主题本身的词描述模式。
6. **扎根失败时提示并继续**，不阻断运行。
7. **派发前先告诉用户成本构成**（见 [references/scope-gates.md](references/scope-gates.md) 0.6）。

提问方式遵循 [`../conventions/decision-autonomy.md`](../conventions/decision-autonomy.md)：有提问工具就用，没有就在对话中给编号选项；互不依赖的问题合并一轮（最多 3 个），带推荐项；无人值守时采用推荐项继续，并在结束时说明。

本次调用附带的主题或约束文字称为**关注点**（focus hint），下文记作 `{focus_hint}`。

## 输出格式

只输出 Markdown。文件名：`docs/ideation/YYYY-MM-DD-<topic>-ideation.md`（无关注点时为 `YYYY-MM-DD-open-ideation.md`）。生命周期见 [`../conventions/artifact-lifecycle.md`](../conventions/artifact-lifecycle.md) 的发想记录一行：30 天内同主题再次发想时更新原文件，不新建。

## 子代理

本技能的质量来自并行的扎根代理、发想代理和独立的依据核查代理，保持 CE 原有规模：默认 5 个发想代理覆盖 6 个视角。支持子代理时按各 reference 派发；不支持时由主会话依次内联完成同样的步骤，并在成本提示中告诉用户：内联时各视角共享同一上下文，想法的多样性和依据核查的独立性都会下降。子代理不修改仓库文件，不执行 git 操作。

## 参考文件读取

阶段规则的读取与复用遵循 [`../conventions/resource-loading.md`](../conventions/resource-loading.md)：只加载命中路线；完整且未变的原文直接复用，缺失或变化时补读。

## Phase 0：续作检查与范围

先读 [references/scope-gates.md](references/scope-gates.md)：它负责续作检查、主题与模式识别、材料检查、规模解读和成本提示；主题已明确时也检查续作与规模。

主题不是软件相关时（命名、叙事、个人决策、非数字化商业策略等），Phase 1 走仓库外扎根，然后改读 [references/universal-ideation.md](references/universal-ideation.md)，由它定义非软件生成、筛选及交接的差异；发想记录仍自动写入。

## Phase 1：按模式扎根

派发任何扎根代理之前读 [references/grounding.md](references/grounding.md)。它定义临时目录、各模式的派发集合与提示词、网络调研、用户提供的调研材料的处理、合并后的扎根摘要以及模型档位。扎根代理并行、在前台运行（后续阶段需要结果）。

## Phase 1.5：主题拆轴

派发视角代理之前，把主题拆成 3~5 条互相正交的**轴**（要思考主题的哪些方面）。读 [references/decomposition.md](references/decomposition.md)；只有 Surprise me 模式跳过这一阶段。主题是否小到不值得拆，由那份文件的标准判断。把轴列表或跳过原因追加到扎根摘要的 `Topic axes` 下。证据侦察只在仓库模式运行。

## Phase 2：发散生成

构建任何派发提示词之前读 [references/divergent-ideation.md](references/divergent-ideation.md)。代理编队、六个视角和生成规则只在那里定义。合并、交叉组合和轴覆盖检查完成后，接着读 [references/post-ideation-workflow.md](references/post-ideation-workflow.md)。

## Phase 3~5：批判、写入、下一步

按 [references/post-ideation-workflow.md](references/post-ideation-workflow.md) 执行依据核查、筛选、写入与下一步交接；非软件路线的差异以 [references/universal-ideation.md](references/universal-ideation.md) 为准。写入时再读 [references/ideation-sections.md](references/ideation-sections.md)。本技能只写入发想记录，不自动提交或调用 handoff。
