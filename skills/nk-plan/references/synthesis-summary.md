# 规划的范围综述

先按 [范围综述](../../conventions/scope-synthesis.md) 整理和呈现，使用“规划综述”预算。这里确认范围与规划期决定，不预告写 plan 时才确定的实施单元、提交顺序、工作量、文件路径和测试命令。

## 两种调用目的

- **独立规划（0.7）**：没有上游 Product Contract，调研前确认问题、预期行为、成功标准与范围。开头“根据你的请求”，确实问答过才加“以及我们的讨论”；下一步是调研。
- **承接上游（5.1.5）**：调研后、写 plan 前，只确认相对已定产品范围的规划覆盖、实现取舍、测试范围和相邻重构。上游已确认内容简短承接，不重新开启产品决定；下一步是写 plan。

输出顺序为范围说明、必要的“延续”、待确认点和实际下一步。关键取舍与排除融入范围说明，不另造重复栏目。详细理由进入关键技术决策。

## 本阶段何时等待

- Lightweight 且没有待确认点：说明范围和下一步后直接继续。
- Standard / Deep 或仍有待确认点：等待明确确认。
- 用户已要求不用确认：任何深度都直接继续，仍说明范围；未经验证的推断记入 Assumptions。
- 无人值守：不发确认或说明，内部整理直接写入对应位置；推断进入 Assumptions。

需要等待的路径发生修订后，按共享方法重新呈现并确认；同一决定反复修改时，“继续”对应本次实际的调研或写 plan。

用户改道时停止当前流程：产品范围不对回到 nk-brainstorm，直接实施用 nk-work，需要排查用 nk-debug；提议在本会话加载，不争辩。

## 写入 plan 的去向

确认后（或止损问题选择继续后），内部草稿按下表融入 plan，不单设 `## Synthesis` 章节，只有第 2 阶段的摘要写进 Product Contract 的 `### Summary`：

| 草稿内容 | 写入位置 |
| :-- | :-- |
| 第 2 阶段摘要 | Product Contract `### Summary`（1–3 行，前瞻性）。独立变体：规划的范围；承接变体：实施做法 |
| 已陈述 | Product Contract `### Requirements`（R-ID），需要时写进 `### Problem Frame` 作为背景 |
| 推断 | Planning Contract 的关键技术决策（带理由），驱动结构选择时体现在实施单元中。无人值守或跳过确认时改放 Planning Contract `### Assumptions`，明确标为未经验证的 Agent 假设 |
| 范围外 | Product Contract `### Scope Boundaries`，需要时含 `#### Deferred to Follow-Up Work` |
| 成功信号 | Product Contract `### Success Criteria`（替代而非叠加上面两行）。已陈述总是写入；推断只在交互确认过的情况下写入，否则放 `### Assumptions` |
| 已定的产品决策 | Product Contract `### Key Decisions`，带 `session-settled:` 标注和 `Governs R…` 链接；已定的技术决策进关键技术决策 |

在交互确认过的 plan 中，两类推断内容即使没通过待确认点保留测试也要写入：从意图外推的成功标准（进 `### Success Criteria`）和用户没点明的范围边界（进 `### Scope Boundaries`）。保留测试决定问不问用户，不决定产品范围是否写进文档。

Summary 与 Problem Frame 分工不同：Summary 回答"这个 plan 提议做什么"（前瞻，1–3 行）；Problem Frame 回答"为什么要做"（回顾，段落）。互不重复。
