---
description: 简化代码以提升清晰度和可维护性 — 在不改变行为的前提下降低复杂度
disable-model-invocation: true
---

调用 code-simplification skill。

在精确保留行为的前提下，简化最近变更的代码（或指定 scope）：

1. 阅读 CLAUDE.md/AGENTS.md 并学习项目约定
2. 确定目标代码 —— 除非指定了更广范围（scope），否则默认为最近变更
3. 修改前理解代码目的、调用方（callers）、边界情况（edge cases）与测试覆盖（test coverage）
4. 扫描可简化的地方：
   - 深层嵌套 → 改用卫语句（guard clauses）或提取辅助函数（extracted helpers）
   - 过长函数 → 按职责拆分
   - 嵌套三元表达式 → 改用 if/else 或 switch
   - 泛化命名 → 改为更具描述性的命名
   - 重复逻辑 → 提取为共享函数
   - 死代码 → 确认无用后移除
5. 增量应用每项简化 —— 每次变更后运行 tests
6. 验证所有 tests 通过、build 成功且 diff 干净

如果简化后 tests 失败，回退（revert）该变更并重新权衡。使用 `code-review-and-quality` review 结果。
