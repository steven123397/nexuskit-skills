---
name: nk-work
description: "Execute one implementation unit from a plan, an Issue, or a clear request: orient from docs/current.md, test-first implementation, verification evidence, cadence-compliant commits. Use nk-debug for open-ended bugs. 执行实施单元、按计划实现、测试先行。"
---

# /nk-work

执行并验证一个实施单元。在满足已定需求、正确性、安全性和可读性的前提下，优先用更少的自维护代码完成同样的工作。主流程安排必需材料与条件分支；reference 读完回到主流程，不递归寻找规则。技能资源相对于本技能目录解析，项目文件相对于目标仓库解析。

## 执行底线

<!-- fragment: work/verification -->
未在终端实际运行的测试、检查或走查，不记为通过；无法运行的项目明确标为“未验证”。
<!-- /fragment -->

<!-- fragment: work/settled-decisions -->
Plan 或需求中已标注为用户敲定的决定，执行时不得擅自推翻；若事实证明不可行或有破坏性，停下报告证据。
<!-- /fragment -->

<!-- fragment: work/escalate -->
只有范围外溢、不可逆或破坏外部契约、用户可见行为分歧、安全权限变更、或外部硬阻断需要向用户确认；局部、可逆、有惯例的实现细节由 Agent 自行决定并说明理由。
<!-- /fragment -->

<!-- fragment: work/subagents -->
子代理不提交 Git；返回结果不触发提交。主会话核对并整合实际改动，亲自验证待交付状态后，按已验证的交付变化调用 `/nk-commit`。
<!-- /fragment -->

## 0. 定位现场

1. 读取目标仓库 `docs/current.md`（若有）和 `AGENTS.md` 指向的项目流程，了解能力、阻断与下一步。
2. 核对分支、`git status --short --untracked-files=all` 和 `git rev-parse --short HEAD`；已登记的半成品由本次接管，外来脏文件不暂存。
3. 现场与交接记录不一致时报告差异；没有直接阻碍仍可继续。

## 1. 接收输入与确定范围

读取 [`references/intake.md`](references/intake.md)，完成输入分流、Plan 充分性和开工前检查。确认一个明确的实施单元、文件范围和完成条件后再写入。

## 2. 执行正常实施循环

先核实目标是否已由当前代码或工件满足；已有能力仍需实际验证，不重复实现。代码路径读取 [`references/tdd-loop.md`](references/tdd-loop.md)，执行现状核验、最小方案选择、测试发现、Red → Green、系统级检查和实际验证。纯非代码交付走下面的非代码路径，不机械套用代码 TDD。

按实际条件选择适用路径；多个条件可以同时命中：

- UI、前端或页面布局：读取 [`references/ui-work.md`](references/ui-work.md)。
- 配置、CI、文档或其他非代码工件：读取 [`references/non-code.md`](references/non-code.md)。
- 完成标志依赖云服务、控制台、远程数据库或其他仓库外状态：读取 [`references/out-of-repo-state.md`](references/out-of-repo-state.md)。
- 客户端支持且当前指令允许子代理时，Agent 自行选择主线执行或委派，无需等待用户点名；决定委派时读取 [`references/subagents.md`](references/subagents.md)。不强制派发，不为使用代理而拆任务；用户明确要求或禁止、项目限制及客户端能力优先。

条件路径读完即回到本流程；不命中就不读。已在上下文中且完整、未变的规则直接复用，只在缺失或变化时补读。

## 3. 执行中新发现的分流

- 影响当前 Plan 的范围或做法：直接修改当前 Plan，并把变更理由随本单元提交。
- 当前单元暴露的显而易见小缺陷：补测试后随本单元修复。
- 独立新需求、跨 Plan 疑难 Bug 或待排期事项：转为 GitHub Issue；无远端时写入 `docs/backlog.md`，不要扩大当前单元。

## 4. 单元完成与提交

1. 若改动影响项目构建、测试命令、目录职责、开发约束或发布流程，检查项目指导并随交付变化维护；没有相关变化不扩写。
2. 核对实际验证证据和未验证边界；有子代理参与时，以主会话整合后的实际文件状态为验证对象，不能仅汇总子代理各自通过的结果。
3. 提交边界按已验证的交付变化确定，与子代理数量、返回顺序和结束时机无关。同一变化的实现、测试和配套文档一并交付；独立变化可分别提交，无交付改动不制造提交。将待提交的文件范围、验证命令和结果交给 `/nk-commit`；有 U-ID 时一并传入，并在提交主题末尾附带 `(U-ID)`。正文记录 1–3 行真实验证证据。`nk-work` 不复制提交技能的完整规则。
4. 若本单元修复审查条目，随同交付更新条目状态；只改该条目要求的字段，不读取 review 的其他内部流程。

## 5. 结束与交接

本次调用只执行已确认的一个实施单元，不自动顺延到下一单元，也不以估计的上下文余量决定是否继续。当前单元完成，或出现无法在当前授权与环境内解除的阻断时，读取 [`../nk-handoff/SKILL.md`](../nk-handoff/SKILL.md) 完成交接并结束本次调用。交接记录下一单元或解除阻断所需条件；下一单元由后续调用接手。

## 完成标志

目标已实现，验证命令实际通过，未验证项已明确记录，相关文档同行维护，且提交或交接边界已经清楚。
