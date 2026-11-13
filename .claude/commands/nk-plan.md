---
description: 将工作拆解为带验收标准（acceptance criteria）和依赖顺序的小型可验证任务
disable-model-invocation: true
---

调用 planning-and-task-breakdown skill。

阅读现有 spec（SPEC.md 或等效文件）以及相关 codebase 部分。然后：

1. 进入 plan mode —— 只读，不做代码变更
2. 梳理组件（components）之间的依赖关系图（dependency graph）
3. 垂直切分工作（每个 task 是一条完整路径，而不是按水平分层）
4. 编写带验收标准（acceptance criteria）和验证步骤的 tasks
5. 在各个 phases 之间添加检查点（checkpoints）
6. 将 plan 提交给人工审阅（review）

将 plan 保存到 tasks/plan.md，将 task list 保存到 tasks/todo.md。

如果 tasks/plan.md 或 tasks/todo.md 已经存在，且其中带有针对另一项工作的未完成 tasks，停止并在写入前询问 — 绝不静默覆盖一份未完成的 plan。
