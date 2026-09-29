---
name: nk-simplify
description: "Analyze opportunities to simplify code while preserving behavior, covering reuse, quality, and efficiency. Available through explicit user invocation or analysis embedded by nk-review. Return actionable recommendations without automatically editing code or committing."
disable-model-invocation: true
---

# /nk-simplify

分析已定型代码中的复用、质量和效率改进，产出有证据的精简建议。独立使用由用户明确调用；也可由 [nk-review](../nk-review/SKILL.md) 显式加载本入口，复用分析能力。

**完成标志：** 三个视角完成分析，发现经核对、去重后交回调用方或报告用户；无发现也是有效结果。只分析，不自动修改代码、提交或交接。

## 1. 接收范围

**review 嵌入调用：** 直接消费调用方确定的仓库、基线与被审快照、文件清单和 diff（或材料路径，含未跟踪文件的纳入/排除决定），以及意图与项目约束。不重新定界、寻找基线或重复询问用户；只核对材料可读且对应被审快照，缺失或不一致就返回调用方补齐，不自行扩围。

**用户单独调用：** 用户指定的范围优先；否则取当前分支相对项目基线的改动，无可用基线时取 `git diff HEAD`；无 diff 时取用户指定或本会话编辑的文件。纳入明确属于本次范围的未跟踪新文件，外来文件排除并说明。仍无非空范围时询问用户，不猜测。

记录被审版本；工作区内容不能仅用 HEAD 标识，保留实际 diff 与相关文件内容或指纹，以便确认分析期间没有变化。只有文档、生成物、vendored 依赖、锁文件或机械性改动时，报告无可精简，不派发空任务。

## 2. 派发三个分析子代理

由当前主会话直接派发以下三个叶子子代理；与 review 联用时，和其风险审查子代理在同一快照上并行。容量有限可分批，不新增 simplify 管理子代理。无法使用子代理时报告分析未完成，不以内联扮演替代。

- [复用视角](references/personas/code-reuse-reviewer.md)：已有仓库能力、标准库、平台与现有依赖能否替代自维护实现。
- [质量视角](references/personas/code-quality-reviewer.md)：冗余状态、重复实现、死代码与无用抽象。
- [效率视角](references/personas/efficiency-reviewer.md)：可消除的重复工作与资源开销；真实回归同样报告，不为保持分类而漏报。

每份提示词包含选中 persona 的完整原文、范围材料、意图、项目约束和以下共同要求：

- 只读分析，不修改文件、不提交、不再派发代理；各自独立分析，不读取其他 reviewer 的发现。
- 先理解真实调用和需求，再寻找更少自维护代码的方案。只报告当前范围内可定位且有实际收益的建议；可以读范围外调用方补证，不扩展审查对象。
- 保持输出、错误、副作用、顺序、兼容性与必要性能；保留安全、无障碍、测试和有效的隔离边界。一个调用方或实现不等于抽象无用，净删行数不作指标。
- 遵守 [已定决策](../conventions/settled-decisions.md)，不借精简改变需求。无法证明行为等价的建议注明缺口，不当作可直接应用的结论。
- 按 [结果体量约定](../conventions/subagent-results.md) 返回位置、问题、具体删除或替代方案、收益、行为保持证据与待验证项。review 提供统一结果契约时按该契约返回，persona 的自然语言格式让位于调用方契约；无发现明确返回空结果。

分析期间不修改被审内容。快照变化时由主会话重新确定受影响范围，失效结果重做；失败的视角须补齐，无法补齐则报告覆盖不完整。

## 3. 汇总与报告

**review 嵌入调用：** 三个子代理结果直接交由 review 合并、独立复核并形成统一报告；本技能不另出菜单、不重复复核或汇报。

**独立调用：** 主会话核对证据，合并相同根因与冲突建议，排除误报和无实际收益的建议；无法证实的内容标明缺失证据。按复用、质量、效率汇报位置、建议、收益、行为保持依据和验证缺口，说明哪些视角完成及无发现结果。由用户决定就地修复、转 Issue 或显式调用 [nk-handoff](../nk-handoff/SKILL.md)；已有明确的修复授权可继续执行，不再重复询问。

获准修复后只处理已确认范围，补跑受影响的检查并复核行为保持情况，复用仍适用的已有证据；无法运行的检查标为未验证。修复完成后汇报，不自动提交；用户需要提交时通过 [nk-commit](../nk-commit/SKILL.md)。
