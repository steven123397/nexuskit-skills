---
name: planning-and-task-breakdown
description: Breaks work into ordered tasks. Use when you have a spec or clear requirements and need to break work into implementable tasks. Use when a task feels too large to start, when you need to estimate scope, or when parallel work is possible.
---

# Planning and Task Breakdown

## 概览

把工作拆解成小而可验证的任务，并为每个任务写明验收标准。一个 agent 是能稳健交付成果，还是产出一团乱麻的烂摊子，关键就看任务拆解得好不好。每个任务都应当足够小，能在单次专注会话内完成实现、测试与验证。

## 何时使用

- 你已有 spec，需要把它拆成可落地的实现单元
- 某个任务显得太大或太模糊，难以直接下手
- 工作需要跨多个 agents 或会话并行推进
- 你需要向合作者（或需求方）对齐任务范围
- 实现顺序并不明显

**何时不要使用：** 范围显而易见的单文件变更，或 spec 已经包含定义良好的任务。

## 计划流程

### 步骤 1：进入 Plan Mode

写任何代码之前，以只读模式运行：

- 阅读 spec 和相关代码库区域
- 识别现有模式和约定
- 映射组件之间的依赖
- 记录风险和未知项

**规划期间不要写代码。** 输出是一份保存到 `tasks/plan.md` 的计划文档，以及记录在 task list target 中的任务列表（见「输出文件」一节；默认 `tasks/todo.md`），而不是实现。

### 步骤 2：识别依赖图

映射什么依赖什么：

```
Database schema
    │
    ├── API models/types
    │       │
    │       ├── API endpoints
    │       │       │
    │       │       └── Frontend API client
    │       │               │
    │       │               └── UI components
    │       │
    │       └── Validation logic
    │
    └── Seed data / migrations
```

实现顺序沿依赖图自底向上：先构建基础。

### 步骤 3：垂直切片

不要先构建全部数据库、再构建全部 API、再构建全部 UI。一次构建一条完整功能路径：

**坏例（水平切片）：**
```
Task 1: Build entire database schema
Task 2: Build all API endpoints
Task 3: Build all UI components
Task 4: Connect everything
```

**好例（垂直切片）：**
```
Task 1: User can create an account (schema + API + UI for registration)
Task 2: User can log in (auth schema + API + UI for login)
Task 3: User can create a task (task schema + API + UI for creation)
Task 4: User can view task list (query + API + UI for list view)
```

每个垂直切片都交付可工作的、可测试的功能。

### 步骤 4：编写任务

无论任务最终落盘到 markdown 任务列表，还是作为外部 tracker 中的一条工单，都遵循这一结构（见「输出文件」一节）：

```markdown
## Task [N]: [Short descriptive title]

**Description:** One paragraph explaining what this task accomplishes.

**Acceptance criteria:**
- [ ] [Specific, testable condition]
- [ ] [Specific, testable condition]

**Verification:**
- [ ] Tests pass: [the repository's focused-test command]
- [ ] Build succeeds: [the repository's build command]
- [ ] Manual check: [description of what to verify]

**Dependencies:** [Task numbers this depends on, or "None"]

**Files likely touched:**
- `src/path/to/file.ts`
- `tests/path/to/test.ts`

**Estimated scope:** [Small: 1-2 files | Medium: 3-5 files | Large: 5+ files]
```

### 步骤 5：排序并设置检查点

安排任务时确保：

1. 依赖已满足（先构建基础）
2. 每个任务结束时系统仍处于可工作状态
3. 每 2-3 个任务后出现验证检查点
4. 高风险任务靠前（快速失败）

在 task list target 中添加明确检查点：

```markdown
## Checkpoint: After Tasks 1-3
- [ ] All tests pass
- [ ] Application builds without errors
- [ ] Core user flow works end-to-end
- [ ] `code-review-and-quality` skill run
- [ ] Review with human before proceeding
```

每个检查点都会先触发一轮 agent 审查（即上文的 `code-review-and-quality`），人工评审则建立在此基础上。

## 任务大小指南

| 大小 | 文件数 | 范围 | 示例 |
|------|-------|-------|---------|
| **XS** | 1 | 单个函数或配置变更 | 添加一条验证规则 |
| **S** | 1-2 | 一个组件或 endpoint | 添加一个新 API endpoint |
| **M** | 3-5 | 一个功能切片 | 用户注册流程 |
| **L** | 5-8 | 多组件功能 | 带过滤和分页的搜索 |
| **XL** | 8+ | **太大，需要进一步拆解** | — |

如果任务是 L 或更大，就应该拆成更小任务。agent 在 S 和 M 任务上表现最好。

**何时进一步拆分任务：**
- 它会超过一次专注会话（约 2+ 小时 agent 工作）
- 用 3 条以内的要点都说不清它的验收标准
- 它触及两个或更多独立子系统（例如 auth 和 billing）
- 你发现任务标题里出现了 “and” 或“和/并”（这通常说明它其实该拆成两个任务）

## 输出文件

- **计划文档：** 把实现计划保存到 `tasks/plan.md`。它始终是一个 markdown 文件——设计决策、风险和未决问题很难工整地拆进单条 tracker issue 中。
- **任务列表：** 把每个任务记录到 **task list target**（定义见下文）。

如果 `tasks/` 目录不存在则创建。

**绝不覆盖未完成的计划。** 在写 `tasks/plan.md` 或 `tasks/todo.md` 之前，检查它们是否已经存在且仍包含未勾选的任务：

- 对同一份工作重新规划（用户要求修订或扩展这个计划）→ 就地更新现有文件。
- 不同的工作 → **停下来询问。** 那些未勾选的任务可能正由另一个会话实现到一半。不要自行删除、覆盖或重命名现有文件；请把冲突直接列出来让用户决定（先收尾旧计划、明确废弃它，还是由用户指定新计划另存位置）。

同样的规则适用于外部 task list target：绝不为了给新任务腾位置，而批量关闭或删除其他计划的未关闭 tracker items。

### 任务清单存放位置（task list target）

Task list target 是记录任务和检查点的位置。它的定义只出现一次，就在这里；这个 skill 中的其他所有引用都以此为准。

- **默认：位于 `tasks/todo.md` 的 checklist 风格 markdown 文件。** 这是 `/nk-build` 命令和其他下游工具期望的约定。除非项目另有说明，否则使用它。
- **外部 tracker：** 如果项目的 agent 规则（`CLAUDE.md`、`AGENTS.md` 等）或用户指定了 issue tracker（例如 GitHub Issues、Jira、Linear、`bd`/beads），把每个任务建成 tracker item，而不是写 `tasks/todo.md`。

  步骤 4 的每一项都必须落进票里，一条都不能省：现状与证据（file:line、命令、输出）写入描述，验收标准写入正文或 tracker 的 acceptance 字段，验证命令写入验证步骤，依赖关系建为 tracker 的 blocked-by 关联。只写「实现 X」、缺少验收条件的票不算建完。

  图结构：phase 建成顶层工作单元，标题带版本身份，任务挂在它下，**只允许一层嵌套**；没有 plan 的维护轮次，整轮就是一个工作单元。步骤 5 的检查点建成该 phase 的最后一张子票。完整规则见项目里的 `docs/agents/issue-tracker.md`（`/nk-init` 生成）；项目没有这份文件时，用本插件的 `references/issue-graph.md`。

使用外部 tracker 时，在 `tasks/plan.md` 中注明（例如 “Tasks tracked in Linear project FOO”），让下游步骤和未来的会话知道去哪里查找；并把计划文档的 Task List 章节保留为 tracker item ID 或链接的有序索引，而不是重复的 checklist。

## 计划文档模板

```markdown
# Implementation Plan: [Feature/Project Name]

## Overview
[One paragraph summary of what we're building]

## Architecture Decisions
- [Key decision 1 and rationale]
- [Key decision 2 and rationale]

## Task List

### Phase 1: Foundation
- [ ] Task 1: ...
- [ ] Task 2: ...

### Checkpoint: Foundation
- [ ] Tests pass, builds clean

### Phase 2: Core Features
- [ ] Task 3: ...
- [ ] Task 4: ...

### Checkpoint: Core Features
- [ ] End-to-end flow works

### Phase 3: Polish
- [ ] Task 5: ...
- [ ] Task 6: ...

### Checkpoint: Complete
- [ ] All acceptance criteria met
- [ ] Ready for review

## Risks and Mitigations
| Risk | Impact | Mitigation |
|------|--------|------------|
| [Risk] | [High/Med/Low] | [Strategy] |

## Open Questions
- [Question needing human input]
```

当任务存放在外部 tracker 中时，把上面的 Task List 章节保留为 tracker item ID 或链接的有序索引，而不是重复的 checklist。

## 并行机会

当多个 agents 或会话可用时：

- **可以安全并行：** 独立功能切片、已实现功能的测试、文档
- **必须顺序执行：** 数据库迁移、共享状态变更、依赖链
- **需要协调：** 共享 API 契约的功能（先定义契约，再并行）

## 常见合理化借口

| 合理化借口 | 现实 |
|---|---|
| “我边做边想” | 这只会让你陷入一团乱麻和无尽返工。花 10 分钟规划能省下数小时。 |
| “任务很明显” | 照样写下来。显式列出的任务会提前暴露出隐藏依赖和容易漏掉的边界情况。 |
| “规划是额外开销” | 规划本身就是工作的一部分。没规划就直接写代码，纯粹是在盲目敲键盘。 |
| “我可以全都记在脑子里” | 上下文窗口容量有限。写下来的书面计划才能跨越会话边界和上下文压缩持续保留。 |
| “旧的 `tasks/plan.md` 过时了，我直接替换掉” | 未勾选的任务可能正由另一个会话执行到一半。直接覆盖会把仅保存在该文件中的工作进度彻底抹掉。务必停下来询问。 |

## 危险信号

- 没有书面任务列表就开始实现
- 未经询问就覆盖仍包含不同工作未勾选任务的 `tasks/plan.md` 或 `tasks/todo.md`
- 项目已指定外部 tracker 却仍然去写 `tasks/todo.md`（或把任务同时分散记录在两处）
- 任务只写“实现功能”，没有验收标准
- 计划中没有验证步骤
- 所有任务都是 XL 大小
- 任务之间没有检查点
- 没有考虑依赖顺序

## 验证

开始实现前，确认：

- [ ] 每个任务都有验收标准
- [ ] 每个任务都有验证步骤
- [ ] 任务依赖已识别并正确排序
- [ ] 任务已记录到 task list target（默认 `tasks/todo.md`）
- [ ] 没有在未获得用户明确确认的情况下覆盖既有未完成的计划
- [ ] 没有任务触及超过约 5 个文件
- [ ] 主要阶段之间存在检查点
- [ ] 人工已评审并批准计划

## 另见

验收标准按任务逐一制定，回答的是“我们做出来的东西对不对？”。它建立在项目级 Definition of Done（完成定义）之上——后者是所有任务在宣布完成前都必须达到的通用底线。参见 `../../references/definition-of-done.md`。
