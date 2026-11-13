---
name: incremental-implementation
description: Delivers changes incrementally in thin, verifiable slices. Use when implementing any feature or change that touches more than one file, or when picking up the next task from a plan. Use when rolling a change out behind a feature flag, when you're about to write a large amount of code at once, or when a task feels too big to land in one step.
---

# Incremental Implementation

## 概览

按小粒度的垂直切片逐步推进：先实现一小块，测试它、验证它，然后再向外扩展。避免一口气写完整个功能。每次增量交付都应该让系统保持在可运行、可测试的状态。正是这套执行纪律，让复杂的大功能变得可控。

## 何时使用

- 实现任何多文件变更
- 从任务拆解中构建新功能
- 重构现有代码
- 任何你想在测试前写超过约 100 行代码的时候

**何时不要使用：** 范围已经足够小的单文件、单函数变更。

## 增量循环

```
┌──────────────────────────────────────┐
│                                      │
│   Implement ──→ Test ──→ Verify ──┐  │
│       ▲                           │  │
│       └───── Commit ◄─────────────┘  │
│              │                       │
│              ▼                       │
│          Next slice                  │
│                                      │
└──────────────────────────────────────┘
```

对每个切片：

1. **Implement**：实现最小且完整可用的功能片段
2. **Test**：运行测试套件（如尚无测试，则补写测试）
3. **Verify**：确认当前切片按预期工作（测试通过、构建成功、人工核验）
4. **Commit**：用描述清晰的 commit message 保存进度（原子提交规范见 `git-workflow-and-versioning`）
5. **Move to the next slice**：在既有成果上推进到下一切片，不要推倒重来

## 切片策略

### 垂直切片（优先）

构建一条贯穿整个技术栈的完整路径：

```
Slice 1: Create a task (DB + API + basic UI)
    → Tests pass, user can create a task via the UI

Slice 2: List tasks (query + API + UI)
    → Tests pass, user can see their tasks

Slice 3: Edit a task (update + API + UI)
    → Tests pass, user can modify tasks

Slice 4: Delete a task (delete + API + UI + confirmation)
    → Tests pass, full CRUD complete
```

每个切片都交付可工作的端到端功能。

### 契约优先切片

当后端和前端需要并行开发时：

```
Slice 0: Define the API contract (types, interfaces, OpenAPI spec)
Slice 1a: Implement backend against the contract + API tests
Slice 1b: Implement frontend against mock data matching the contract
Slice 2: Integrate and test end-to-end
```

### 风险优先切片

先处理风险最高或最不确定的部分：

```
Slice 1: Prove the WebSocket connection works (highest risk)
Slice 2: Build real-time task updates on the proven connection
Slice 3: Add offline support and reconnection
```

如果 Slice 1 走不通，你在把精力投入 Slice 2 和 3 之前就能及早暴露问题。

## 实现规则

### 规则 0：简单优先

写任何代码之前，先问：“最简单能工作的东西是什么？”

写完代码后，用这些检查审视它：
- 能用更少代码完成吗？
- 这些抽象真的物有所值，还是白白增加了复杂度？
- staff engineer 看了会不会说“为什么不直接……”？
- 我是在为假想的未来需求构建，还是为当前任务构建？

```
SIMPLICITY CHECK:
✗ Generic EventBus with middleware pipeline for one notification
✓ Simple function call

✗ Abstract factory pattern for two similar components
✓ Two straightforward components with shared utilities

✗ Config-driven form builder for three forms
✓ Three form components
```

宁可先留三行相似代码，也别过早做抽象。先写出直白、一眼就能看懂其正确性的版本，等测试证明逻辑无误后再考虑优化。

### 规则 0.5：范围纪律

只触碰任务需要的内容。

不要：
- 顺手“清理”改动位置旁边的无关代码
- 在本身不需要改动的文件里重构 imports
- 删掉你并没有完全理解用途的注释
- 因为“看着挺有用”就擅自加入 spec 之外的功能
- 顺手把你只是阅读过的文件升级成新语法

如果你注意到任务范围外值得改进的东西，记录下来，不要修：

```
NOTICED BUT NOT TOUCHING:
- src/utils/format.ts has an unused import (unrelated to this task)
- The auth middleware could use better error messages (separate task)
→ Want me to create tasks for these?
```

### 规则 1：一次只做一件事

每个增量只改变一件逻辑事情。不要混合关注点：

**坏例：** 一个 commit 同时添加新组件、重构现有组件，并更新构建配置。

**好例：** 三个独立 commits，每个对应一个变更。

### 规则 2：保持可编译

每次增量结束后，项目必须能顺利构建，且现有测试必须全部通过。不要在两次切片之间把代码库留在构建或测试挂掉的状态。

### 规则 3：为未完成功能使用 Feature Flags

如果功能尚未准备好给用户使用，但你需要合并增量：

```typescript
// Feature flag for work-in-progress
const ENABLE_TASK_SHARING = process.env.FEATURE_TASK_SHARING === 'true';

if (ENABLE_TASK_SHARING) {
  // New sharing UI
}
```

这样你就能把小步增量合入 main branch，同时不把尚未完成的功能暴露给用户。

### 规则 4：安全默认值

新代码应该默认采用安全、保守行为：

```typescript
// Safe: disabled by default, opt-in
export function createTask(data: TaskInput, options?: { notify?: boolean }) {
  const shouldNotify = options?.notify ?? false;
  // ...
}
```

### 规则 5：便于回滚

每个增量都应能独立 revert：

- 增量式变更（新文件、新函数）容易 revert
- 对现有代码的修改应最小且聚焦
- 数据库迁移应有对应 rollback migration
- 避免在同一个 commit 中既删掉旧实现又直接写入新替换，把这两步拆开提交

## 与 Agents 协作

指导 agent 增量实现时：

```
"Let's implement Task 3 from the plan.

Start with just the database schema change and the API endpoint.
Don't touch the UI yet — we'll do that in the next increment.

After implementing, run the repository's test and build commands to
verify nothing is broken."
```

明确说明每个增量的范围内是什么，范围外是什么。

## 增量检查清单

每个增量后，用仓库自己的命令验证（见 test-driven-development 技能的「先发现技术栈」一节）：

- [ ] 本次变更只聚焦一件事，且已完整收尾
- [ ] 所有现有测试仍然通过（使用仓库自己的测试命令：`npm test`、`./gradlew test`、`pytest` 等）
- [ ] 构建成功（仓库的构建命令）
- [ ] 如果该技术栈支持类型检查，确保类型检查通过（`npx tsc --noEmit`、`mypy` 等）
- [ ] lint 检查通过（仓库的 lint 命令）
- [ ] 新功能按预期正常工作
- [ ] 变更已使用描述清晰的 commit message 提交

**注意：** 每次改动可能影响验证结果后，运行对应的验证命令。一旦成功跑过一遍，除非代码之后又改了，否则别再重复跑同一条命令——在代码未改动时重复运行并不会提供任何新信息。

## 常见合理化借口

| 合理化借口 | 现实 |
|---|---|
| “我最后一起测试” | bug 会叠加放大。Slice 1 留下的 bug 会把后面的 Slice 2-5 全带偏。每个切片都必须测。 |
| “一次性全做完更快” | *感觉上*是更快，直到某处突然崩了，你却得在 500 行改动里大海捞针找问题。 |
| “这些变更太小，不值得分开提交” | 拆小 commit 几乎零成本。巨大的 commit 只会掩盖 bug，还会让回滚痛苦不堪。 |
| “我之后再加 feature flag” | 如果功能还没做完，本来就不该让用户看见。现在就把 flag 加上。 |
| “这个重构足够小，可以一起带上” | 把重构和功能改动混在一起，会让两者都更难评审和排查。请拆开提交。 |
| “我再跑一次构建命令确认一下” | 跑通一遍后，只要代码没动过，重跑同一命令就毫无意义。等下次改代码后再跑，别只为图心理安慰多跑一遍。 |

## 危险信号

- 写了超过 100 行代码却没有运行测试
- 单个增量包含多个无关变更
- 抱着“既然改到这里了，干脆顺手加上这个”的心态导致范围蔓延
- 为求快而跳过 test/verify 步骤
- 两次增量之间让构建或测试处于失败状态
- 大量未提交的改动越积越多
- 还没出现第三个真实复用场景，就急着搭建抽象层
- 抱着“来都来了”的心态去触碰任务范围以外的文件
- 为一次性操作创建新的 utility 文件
- 没有任何代码变更却连续两次运行同一个 build/test 命令

## 验证

完成一个任务的所有增量后：

- [ ] 每个增量都已单独测试并提交
- [ ] 完整测试套件通过
- [ ] 构建干净
- [ ] 功能按 spec 端到端工作
- [ ] 没有未提交变更

## 另见

单次增量的验证只是局部阶段性检查。在正式宣布任务完成之前，必须用项目级的 Definition of Done 作为最终卡点来把关——那是无论做什么任务、每次增量最终都必须迈过的硬性基线。见 `../../references/definition-of-done.md`。
