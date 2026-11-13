---
name: documentation-and-adrs
description: Records decisions and documentation. Use when you need to document an architecture decision (ADR) or the reasoning behind a design choice, when changing public APIs, shipping features, or when you need to record context that future engineers and agents will need to understand the codebase.
---

# Documentation and ADRs

## 概览

记录技术决策，而不只是罗列代码。最有价值的文档在于沉淀 *why*（为什么）——即促成这项决策背后的上下文、约束条件与权衡取舍。代码只展示了构建了 *what*（什么）；而文档要解释清楚**为什么这样构建**，以及**当时权衡过哪些备选方案**。这些背景信息，对未来在代码库中工作的工程师和 agent 都至关重要。

## 何时使用

- 做出重大架构决策
- 在多个备选方案之间做选型权衡
- 新增或变更公开 API
- 发布会改变用户可见行为的功能
- 让新团队成员（或 agent）熟悉项目
- 当你发现自己反复解释同一件事时

**何时不要使用：** 不要记录显而易见的代码；不要添加只是复述代码本身的注释；不要为用完即扔的一次性原型编写文档。

## Architecture Decision Records (ADRs，架构决策记录)

ADR 用来沉淀重大技术决策背后的推理过程。它们是你能写出的最高价值文档。

### 何时编写 ADR

- 选择框架、库或主要依赖
- 设计数据模型或数据库 schema
- 选择认证策略
- 决定 API 架构（REST vs. GraphQL vs. tRPC）
- 在构建工具、托管平台或基础设施之间做选型
- 任何逆转成本高昂的决策

### 优先匹配现有约定

在创建 ADR 之前，先结合当前可读取的仓库上下文，检查是否已有既定规范——包括现存 ADR、项目规则/指令文件，以及与 ADR 相关的配置或工具（例如 `.adr-dir` 文件）。一旦已有既定约定，就优先沿用既有约定，覆盖下面的默认格式：

- **存放位置和格式** — 例如 `docs/adr/*.md`、`Documentation/Decisions/*.rst`、MADR 布局，或 `adr-tools` 配置。匹配现有目录、文件扩展名和标记语言（Markdown 还是 reStructuredText）。
- **编号和命名** — 延续现有序号递增规则和文件名模式（`ADR-004-Title.rst`、`0004-title.md` 等）；不要擅自重新从 001 起编，也不要另起第二套方案。
- **章节标题** — 复用项目现有的标题集合，不要强加本模板里的标题。

如果现有线索彼此冲突，先把冲突亮出来，而不是悄悄再引入一套新方案。只有在完全无法确立约定时，才套用下面的默认模板。

### ADR 模板

将 ADR 存放在 `docs/decisions/` 目录并采用连续编号（除非项目已使用其他位置——见上文）：

```markdown
# ADR-001: Use PostgreSQL for primary database

## Status
Proposed | Accepted | Superseded by ADR-XXX | Deprecated

## Date
2025-01-15

## Context
We need a primary database for the task management application. Key requirements:
- Relational data model (users, tasks, teams with relationships)
- ACID transactions for task state changes
- Support for full-text search on task content
- Managed hosting available (for small team, limited ops capacity)

## Decision
Use PostgreSQL with Prisma ORM.

## Alternatives Considered

### MongoDB
- Pros: Flexible schema, easy to start with
- Cons: Our data is inherently relational; would need to manage relationships manually
- Rejected: Relational data in a document store leads to complex joins or data duplication

### SQLite
- Pros: Zero configuration, embedded, fast for reads
- Cons: Limited concurrent write support, no managed hosting for production
- Rejected: Not suitable for multi-user web application in production

### MySQL
- Pros: Mature, widely supported
- Cons: PostgreSQL has better JSON support, full-text search, and ecosystem tooling
- Rejected: PostgreSQL is the better fit for our feature requirements

## Consequences
- Prisma provides type-safe database access and migration management
- We can use PostgreSQL's full-text search instead of adding Elasticsearch
- Team needs PostgreSQL knowledge (standard skill, low risk)
- Hosting on managed service (Supabase, Neon, or RDS)
```

### ADR 生命周期

```
PROPOSED → ACCEPTED → (SUPERSEDED or DEPRECATED)
```

- **不要删除旧 ADR。** 它们承载着历史上下文。
- 当决策发生变化时，写一份新的 ADR，在其中引用并取代（supersede）旧 ADR。

## 行内文档

### 何时写注释

注释解释 *why*，而不是 *what*：

```typescript
// BAD: Restates the code
// Increment counter by 1
counter += 1;

// GOOD: Explains non-obvious intent
// Rate limit uses a fixed window that opens on the first request after the
// previous one expires, not on a clock schedule. Known gap: a client can spend
// the full limit just before a reset and again just after (2x in a moment)
if (now - windowStart > WINDOW_SIZE_MS) {
  counter = 0;
  windowStart = now;
}
```

### 何时不要写注释

```typescript
// Don't comment self-explanatory code
function calculateTotal(items: CartItem[]): number {
  return items.reduce((sum, item) => sum + item.price * item.quantity, 0);
}

// Don't leave TODO comments for things you should just do now
// TODO: add error handling  ← Just add it

// Don't leave commented-out code
// const oldImplementation = () => { ... }  ← Delete it, git has history
```

### 记录已知陷阱

```typescript
/**
 * IMPORTANT: This function must be called before the first render.
 * If called after hydration, it causes a flash of unstyled content
 * because the theme context isn't available during SSR.
 *
 * See ADR-003 for the full design rationale.
 */
export function initializeTheme(theme: Theme): void {
  // ...
}
```

## API 文档

对于公开 API（REST、GraphQL、库接口）：

### 与类型定义写在一起（TypeScript 首选）

```typescript
/**
 * Creates a new task.
 *
 * @param input - Task creation data (title required, description optional)
 * @returns The created task with server-generated ID and timestamps
 * @throws {ValidationError} If title is empty or exceeds 200 characters
 * @throws {AuthenticationError} If the user is not authenticated
 *
 * @example
 * const task = await createTask({ title: 'Buy groceries' });
 * console.log(task.id); // "task_abc123"
 */
export async function createTask(input: CreateTaskInput): Promise<Task> {
  // ...
}
```

### REST API 使用 OpenAPI / Swagger

```yaml
paths:
  /api/tasks:
    post:
      summary: Create a task
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateTaskInput'
      responses:
        '201':
          description: Task created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Task'
        '422':
          description: Validation error
```

## README 结构

每个项目都应该有一份 README，覆盖：

```markdown
# Project Name

One-paragraph description of what this project does.

## Quick Start
1. Clone the repo
2. Install dependencies: `npm install`
3. Set up environment: `cp .env.example .env`
4. Run the dev server: `npm run dev`

## Commands
| Command | Description |
|---------|-------------|
| `npm run dev` | Start development server |
| `npm test` | Run tests |
| `npm run build` | Production build |
| `npm run lint` | Run linter |

## Architecture
Brief overview of the project structure and key design decisions.
Link to ADRs for details.

## Contributing
How to contribute, coding standards, PR process.
```

## Changelog 维护

对于已发布功能：

```markdown
# Changelog

## [1.2.0] - 2025-01-20
### Added
- Task sharing: users can share tasks with team members (#123)
- Email notifications for task assignments (#124)

### Fixed
- Duplicate tasks appearing when rapidly clicking create button (#125)

### Changed
- Task list now loads 50 items per page (was 20) for better UX (#126)
```

## 面向 Agent 的文档

需要特别考虑 AI agent 的上下文：

- **CLAUDE.md / AGENTS.md 等项目规则文件** — 记录项目约定，让 agent 遵循它们
- **Spec files** — 保持 spec 持续更新，确保 agent 按正确目标构建
- **ADRs** — 帮助 agent 理解过往决策的原因（避免反复推翻重议）
- **行内陷阱提示（Inline gotchas）** — 防止 agent 掉入已知陷阱

## 文字审阅

技术内容核对无误之后，再站在未来读者的视角审阅文字。注意：更清晰的措辞绝不能改变决策本身或其适用边界。

1. 先标出修改过程中必须保留下来的关键细节：名称、数值与单位、命令、路径、链接、条件、权衡取舍，以及尚未敲定的不确定之处。逐一对照可用的代码和决策上下文核对；凡是你无法证实的，一律标记出来。
2. 用读者真正需要的具体信息，替换掉套话式开场白、宣传腔形容词和重复的总结。不要为了填补缺乏依据的说法，而凭空编造示例或给出更满的保证；同时保留必要的技术性重复，以及项目既有的术语。
3. 把改后的文档与原文及其来源做对比。恢复任何不小心丢失的限定语或注意事项，验证命令和代码示例仍能按文档所述工作，并如实解释任何未解决的事实存疑，而不是用文字润色把它粉饰掩盖过去。

## 常见合理化借口

| 合理化借口 | 现实 |
|---|---|
| “代码是自解释的” | 代码只展示 what，不展示 why、当初拒绝了哪些替代方案，也不体现适用的约束边界。 |
| “等 API 稳定后再写文档” | 当你着手记录 API 时，API 往往会更快稳定下来。文档本身就是对设计的第一轮检验。 |
| “没人读文档” | Agent 会读，未来的工程师会读，三个月后的你自己也会读。 |
| “ADR 是额外负担” | 一份花 10 分钟写完的 ADR，能避免半年后团队围绕同一决策争论两小时。 |
| “注释会过时” | 解释 *why* 的注释是稳定的；复述 *what* 的注释才会过时，所以只写前者。 |

## 危险信号

- 架构决策没有书面理由
- 公开 API 没有文档或类型说明
- README 没有写明如何运行项目
- 用注释掉的代码代替直接删除
- TODO 注释已经滞留数周无人处理
- 有重大架构选择的项目中却没有 ADR
- 文档只是复述代码本身，而不是解释设计意图

## 验证

完成文档后：

- [ ] 所有重大架构决策都有对应的 ADR
- [ ] README 覆盖快速上手（quick start）、常用命令和架构概览
- [ ] API 函数配有参数和返回类型的文档说明
- [ ] 已知陷阱已在关键位置通过行内注释记录清楚
- [ ] 代码中不再保留被注释掉的代码
- [ ] 项目规则文件（CLAUDE.md / AGENTS.md 等）保持最新且准确
- [ ] 文字修改保留了来源细节、决策取舍与限定条件，且没有添加缺乏依据的保证
