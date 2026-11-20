---
name: spec-driven-development
description: Creates specs before coding. Use when starting a new project, feature, or significant change and no specification exists yet. Use when drafting a PRD or requirements document with objectives and scope, or when requirements are unclear, ambiguous, or only exist as a vague idea. Use when a single requirement spans several independently testable capabilities and needs decomposing into a capability map of modules before specifying. Use when evolving a shipped spec — scoping a V1, deferring ideas to a V2 backlog, or writing a follow-up spec for a change to an existing feature.
---

# Spec-Driven Development

## 概览

在编写任何代码之前，先写一份结构化规格说明。spec 是你和人类工程师之间共享的事实来源，它定义我们要构建什么、为什么构建，以及如何知道它完成了。没有 spec 的代码就是猜测。

## 何时使用

- 开始一个新项目或功能
- 需求有歧义或不完整
- 变更触及多个文件或模块
- 你即将做出架构决策
- 任务实现需要超过 30 分钟

**何时不要使用：** 单行修复、拼写更正，或需求明确且自包含的变更。

## 门控工作流

Spec-driven development 包含四个阶段，前面还有一个前置范围检查（阶段 0），它只在单次需求包含多个可独立测试的能力时才会激活。当前阶段未经过验证之前，不要进入下一阶段。

```
SPECIFY ──→ PLAN ──→ TASKS ──→ IMPLEMENT
   │          │        │          │
   ▼          ▼        ▼          ▼
 Human      Human    Human      Human
 reviews    reviews  reviews    reviews
```

### 阶段 0：范围检查（Scope Check）

大多数请求只描述一个能力。如果当前的请求也是如此，跳过这个阶段，直接进入 Specify。阶段 0 是为例外情况存在的，不是常规；它不会给单能力功能强加层级结构。

**检测。** 当单次需求包含多个可独立测试的能力时，先拆解模块再编写 spec：

- 需求点名了多个各有自己的消费者或数据的独立能力（例如 identity、billing、notifications、reporting）
- 验收标准聚成可以分别交付和验证的组
- 砍掉或替换某一个能力，不需要重写其他能力的要求

**在写任何 spec 之前，先提交一份能力地图（capability map）。** 篇幅要小、方便评审：一张模块表加上一个构建顺序即可，不要写成项目计划：

```markdown
# Capability Map: [Initiative Name]

| Module id | Responsibility | Depends on |
|---|---|---|
| identity | Accounts, sessions, SSO | — |
| billing | Plans, invoices, payments | identity |
| notifications | Email and webhook fan-out | identity |
| reporting | Usage dashboards | billing, notifications |

Build order: identity → billing, notifications → reporting
```

- **稳定的模块 id。** 采用 kebab-case 命名，一旦确定，在整个推进期间绝不重命名。Specs、计划和下游命令都通过这些 id 来定位并选取工作，而不是靠猜哪份 spec 当前生效。
- **依赖有方向，无环。** 箭头只指向一个方向。如果两个模块互相依赖，它们其实是一个模块。
- **接口位于边界上。** 地图记录 `billing` 依赖 `identity`；两者之间的契约属于提供方模块的 spec（设计方法见 `api-and-interface-design`）。

**能力地图和其他阶段一样设有门禁。** 在写任何模块 spec 之前，先由人工评审模块边界、依赖方向和构建顺序。把地图划错的代价很高，而评审十来行表格的成本却微乎其微。

**然后按模块逐个递归推进。** 按照依赖顺序，为每个模块依次执行 Specify → Plan → Tasks → Implement。每个模块都有各自独立的 spec，范围严格限定在该模块的目标、边界与成功标准内。将批准后的能力地图保存在 `spec/` 目录（`spec/capability-map.md`），各模块的 spec 与之同目录存放，并按模块 id 命名（`spec/SPEC-identity.md`、`spec/SPEC-billing.md`）；如果是单份 spec，则仍保存在项目根目录的 `SPEC.md`。真正起到索引作用的是这张地图，而不是靠猜文件名。

### 阶段 1：Specify

从高层愿景开始。向人类提出澄清问题，直到需求具体。

**立即暴露假设。** 在写任何 spec 内容之前，列出你的假设：

```
ASSUMPTIONS I'M MAKING:
1. This is a web application (not native mobile)
2. Authentication uses session-based cookies (not JWT)
3. The database is PostgreSQL (based on existing Prisma schema)
4. We're targeting modern browsers only (no IE11)
→ Correct me now or I'll proceed with these.
```

不要默默补全含糊需求。spec 的全部目的，就是在代码写出来*之前*暴露误解；假设是最危险的一种误解。

**写一份覆盖这六个核心区域的 spec 文档：**

1. **Objective**：我们在构建什么，为什么？用户是谁？成功是什么样子？

2. **Commands**：完整可执行命令，包含 flags，而不只是工具名。
   ```
   Build: npm run build
   Test: npm test -- --coverage
   Lint: npm run lint -- --fix
   Dev: npm run dev
   ```

3. **Project Structure**：源代码在哪里，测试放哪里，文档属于哪里。
   ```
   src/           → Application source code
   src/components → React components
   src/lib        → Shared utilities
   tests/         → Unit and integration tests
   e2e/           → End-to-end tests
   docs/          → Documentation
   ```

4. **Code Style**：一个真实代码片段展示风格，胜过三段描述。包含命名约定、格式规则和优秀输出示例。

5. **Testing Strategy**：使用什么框架、测试放在哪里、覆盖率期望、哪些关注点对应哪些测试层级。

6. **Boundaries**：三层系统：
   - **Always do:** 运行测试后再提交、遵循命名约定、验证输入
   - **Ask first:** 数据库 schema 变更、添加依赖、修改 CI 配置
   - **Never do:** 提交 secrets、编辑 vendor 目录、未经批准移除失败测试

**Spec 模板：**

```markdown
# Spec: [Project/Feature Name] — V[N]

## Objective
[What we're building and why. User stories or acceptance criteria.]

## Tech Stack
[Framework, language, key dependencies with versions]

## Commands
[Build, test, lint, dev — full commands]

## Project Structure
[Directory layout with descriptions]

## Code Style
[Example snippet + key conventions]

## Testing Strategy
[Framework, test locations, coverage requirements, test levels]

## Boundaries
- Always: [...]
- Ask first: [...]
- Never: [...]

## Success Criteria
[How we'll know this is done — specific, testable conditions]

## Out of Scope (Deferred)
[Ideas explicitly excluded from this version — the V2 backlog. One line each: what, and why it's deferred.]

## Open Questions
[Anything unresolved that needs human input]
```

**外部 spec 工具：** 这套工作流与具体格式无关。如果项目已经在使用 OpenSpec 或其他规格管理系统，请沿用该系统原有的产物格式与存储约定，不要再重复创建一份 `SPEC.md`。本 skill 负责需求澄清、内容产出与批准门禁；外部工具则负责已批准 spec 的实际呈现与存储形式。

**把指令重新框定为成功标准。** 收到模糊需求时，把它们翻译成具体条件：

```
REQUIREMENT: "Make the dashboard faster"

REFRAMED SUCCESS CRITERIA:
- Dashboard LCP < 2.5s on 4G connection
- Initial data load completes in < 500ms
- No layout shift during load (CLS < 0.1)
→ Are these the right targets?
```

这样你就能围绕清晰目标进行循环、重试和解决问题，而不是猜测 “faster” 是什么意思。

**写完 spec 后立即停止（CRITICAL）。** spec 一旦保存：

1. 总结它，并列出所有 Open Questions。
2. 请人类批准它，或提出修改意见。
3. **立即停止你的回合。** 不要在本回合进入阶段 2、调用 `planning-and-task-breakdown` 或写代码。只有在人类于后续某个回合批准 spec 之后，规划才开始。

### 阶段 2：Plan

在 spec 已验证后，生成技术实现计划：

1. 识别主要组件及其依赖
2. 确定实现顺序（必须先构建什么）
3. 记录风险和缓解策略
4. 识别哪些可以并行构建，哪些必须顺序执行
5. 定义阶段之间的验证检查点

> 这些步骤背后的依赖图映射和垂直切片机制，遵循 `planning-and-task-breakdown`；它是权威来源。上面的要点只是轻量摘要；两者若出现分歧，以 `planning-and-task-breakdown` 为准。
>
> **输出约定：** 默认把计划保存到 `tasks/plan.md`，并把任务列表记录到 `planning-and-task-breakdown` 定义的 task list target（默认 `tasks/todo.md`）；使用外部 tracker 时，按该 skill 的多 phase 布局写入顶层工作单元，不创建 Markdown 镜像。只有使用 `tasks/` 时才创建该目录。下游命令（`/nk-build` 等）依赖这些约定。

计划应该可评审：人类读完后应该能说“对，这是正确做法”或“不，修改 X”。

### 阶段 3：Tasks

把计划拆解为离散、可实现的任务：

- 每个任务都应能在一次专注会话中完成
- 每个任务都有明确验收标准
- 每个任务都包含验证步骤（测试、构建、手动检查）
- 任务按依赖排序，而不是按感知重要性排序
- 任何任务都不应需要修改超过约 5 个文件

> 完整的任务大小划分和依赖排序机制，遵循 `planning-and-task-breakdown`；它是权威来源。下面的模板只是轻量内联形式；两者若出现分歧，以 `planning-and-task-breakdown` 为准。

**任务模板：**
```markdown
- [ ] Task: [Description]
  - Acceptance: [What must be true when done]
  - Verify: [How to confirm — test command, build, manual check]
  - Files: [Which files will be touched]
```

### 阶段 4：Implement

一次执行一个任务，并遵循 `incremental-implementation` 和 `test-driven-development`。使用 `context-engineering` 在每一步加载正确的 spec 章节和源文件，而不是把整个 spec 都塞给 agent。

## 让 Spec 保持鲜活

spec 是一份活文档，不是一次性工件：

- **决策变化时更新**：如果你发现数据模型需要改变，先更新 spec，再实现。
- **范围变化时更新**：新增或砍掉的功能应该反映在 spec 中。
- **提交 spec**：spec 应该和代码一起进入版本控制。
- **在 PR 中引用 spec**：链接回每个 PR 实现的 spec 章节。

## Spec 演进：V1 范围界定与后续变更

一份 spec 只描述当前这一个版本的工作。新冒出来的想法和上线后的变更需求，不该直接塞进当前 spec——它们应该排在后面等待下一轮。

### 明确界定每个版本的范围

在 spec 标题里标明它对应的版本（例如 `# Spec: Invoice Pipeline — V1`）。每当一份已上线的增量 spec（delta spec）合入主 spec 后，就递增版本号——这样标题始终能明确说明这份 spec 描述的是系统的哪个版本，也让“这是 V2 的想法”成为客观判断，而不是开发到一半时拍脑袋的决定。

在 Specify 阶段，本版本不纳入的想法统一收进 **Out of Scope (Deferred)**——记下来，不丢掉。这让 V1 的范围边界真正可执行：实现期间，凡是不在需求列表里的内容都不做，哪怕它就写在同一个文件的 Deferred 列表里。开发途中冒出新点子，直接记到 Deferred 列表里继续当前工作；范围调整发生在版本之间，而不是版本开发过程中。

### 后续变更单写一份 delta spec

一旦某份 spec 已经上线，新需求——例如切换存储引擎、把人工步骤替换成 OCR、或者把某个延后的 V2 条目提上日程——应该单写一份小巧的 delta spec，而不是直接手动改写已上线的原 spec。Delta spec 只写发生变化的部分：

```markdown
# Spec Delta: [Change Name]

Status: proposed

## Objective
[The change and why. Which deferred item or new requirement this implements.]

## Current Behavior
[What exists today — link the relevant section of the original spec.]

## New Behavior
[What will be true after the change.]

## Success Criteria
[Specific, testable conditions — including what must NOT change.]

## Boundaries
[Only deltas from the original spec's boundaries; everything else inherits.]
```

将它保存在原 spec 同级目录（例如与 `SPEC.md` 同级的 `SPEC-postgres-migration.md`），走同一套门控流程：人工评审，再进入 Plan、Tasks、Implement。下游命令都认这个约定——`/nk-build auto` 会把根目录的 `SPEC-<change>.md` 识别为后续变更的 spec，并在建立干净 baseline 时将其视作合法的规划产物。每份 delta spec 只承载一个变更，这样每一轮 plan/build 循环都足够小、易于审查。

变更上线后，把最终结果合回原 spec（见「让 Spec 保持鲜活」），让原 spec 始终作为系统现状的唯一事实来源，并把 delta spec 的 `Status:` 行改为 `Status: implemented`。原 spec 永远描述系统当前是什么样，delta spec 描述的是状态跃迁。

## 常见合理化借口

| 合理化借口 | 现实 |
|---|---|
| “这很简单，我不需要 spec” | 简单任务不需要*长* spec，但仍然需要验收标准。两行 spec 可以。 |
| “我写完代码后再补 spec” | 那是文档，不是规格说明。spec 的价值在于在代码之前强制澄清。 |
| “spec 会拖慢我们” | 15 分钟 spec 可以避免数小时返工。15 分钟的 waterfall 胜过 15 小时的调试。 |
| “需求反正会变” | 这正是 spec 是活文档的原因。过时的 spec 仍然好过没有 spec。 |
| “用户知道自己想要什么” | 即使清晰请求也有隐含假设。spec 会暴露这些假设。 |
| “这个想法挺好，我顺手加进当前 spec 吧” | 开发中途膨胀范围，正是 V1 延期的根源。把它放进 Out of Scope (Deferred)——既留档了，又不会撑大当前周期。 |
| “这个功能已经有 spec 了，我直接在上面改吧” | 已上线的 spec 描述的是现有系统。Delta spec 让这次变更可以独立评审；原 spec 要等变更上线后再合入更新，而不是事前改写。 |
| “这是一个大功能，拆开它是额外开销” | 只要验收标准能聚合成可独立测试的模块组，写成一份单体 spec 就会迫使每个下游任务都得背着整份完整契约做推理。相比之下，十行的能力地图是成本低得多的替代方案。 |
| “我会在规划时再分解” | 规划阶段做的是在单个 spec 内部拆分任务。真到那一步，那份体量过大的单体产物早就写出来了——模块边界与依赖方向必须在写 spec 之前定好，而不是之后再补救。 |

## 危险信号

- 在没有任何书面需求的情况下开始写代码
- 在还没澄清“完成”具体指什么之前，就问“要我直接开始写吗？”
- 实现任何 spec 或任务列表中未提及的功能
- 在没有记录的情况下做出架构决策
- 因为“要构建什么很明显”而跳过 spec
- 实现中途把新想法直接写进当前 spec，导致 V1 需求不断膨胀
- 因为“这个功能已经有 spec 了”，修改已上线功能时不再为这次变更编写 spec
- 写完 spec 后，在同一回合就开始做计划或写代码
- 一份 spec 的需求横跨多个可独立测试的能力
- 因为没有事先批准能力地图，模块边界或构建顺序在实现期间被隐式决定

## 验证

进入实现前，确认：

- [ ] spec 覆盖全部六个核心区域（完整 spec 如此；delta spec 只覆盖变更涉及的区域——至少包含 objective、success criteria 和 boundary deltas，其余继承自原 spec）
- [ ] 人类已评审并批准 spec
- [ ] 回合在保存 spec 后即结束；批准发生在后续某个回合
- [ ] 成功标准具体且可测试
- [ ] Boundaries（Always/Ask First/Never）已定义
- [ ] spec 已保存到仓库中的文件
- [ ] 从本版本砍掉的想法已记录在 Out of Scope (Deferred) 下，既没有悄悄丢掉，也没有悄悄塞进实现
- [ ] 如果这是对已上线 spec 的变更，已编写引用原 spec 的 delta spec，而非直接重写原 spec
- [ ] 如果单次需求包含多个可独立测试的能力，已在写任何模块 spec 之前取得能力地图（模块 id、依赖方向、构建顺序）的批准
- [ ] 每份模块 spec 都能追溯到已批准地图中的某个模块 id
