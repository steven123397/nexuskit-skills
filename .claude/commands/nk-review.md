---
description: 执行五轴 code review — correctness、readability、architecture、security、performance
disable-model-invocation: true
---

调用 code-review-and-quality skill。

围绕全部五个轴 review 当前变更（staged 或 recent commits）：

1. **Correctness** — 是否符合 spec？边界情况（edge cases）是否已处理？测试是否充分？
2. **Readability** — 命名是否清晰？控制逻辑是否直接？代码组织是否合理？
3. **Architecture** — 是否遵循现有 patterns？边界（boundaries）是否清晰？抽象层级（abstraction level）是否合适？
4. **Security** — 输入是否校验？secrets 是否安全？鉴权（auth）是否已检查？（配合 security-and-hardening skill）
5. **Performance** — 是否避免了 N+1 查询？是否避免了无界操作（unbounded ops）？（配合 performance-optimization skill）

将 findings 分类为 Critical、Required、Optional 或 Nit。
输出结构化 review 报告，包含具体 file:line 引用位置和修复建议。
