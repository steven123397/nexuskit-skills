---
name: deprecation-and-migration
description: Manages deprecation and migration. Use when removing old systems, APIs, or features. Use when migrating users from one implementation to another. Use when migrating a database schema in production, such as renaming or dropping a column without downtime (expand/contract). Use when deciding whether to maintain or sunset existing code.
---

# Deprecation and Migration

## 概览

代码是一种负债，而不是资产。每一行代码都有持续的维护成本：需要修复 bug、更新依赖、打安全补丁，还要帮新入职的工程师上手理解。弃用（deprecation）是一套移除“不再值得继续维护的代码”的工程纪律，而迁移（migration）则是把使用方安全地从旧系统平稳过渡到新系统的过程。

大多数工程组织都擅长构建新东西，但很少擅长体面地移除旧东西。这个 skill 正是为了弥补这个缺口。

## 何时使用

- 用新系统、新 API 或新库替换旧实现
- 下线不再需要的功能
- 合并重复的实现逻辑
- 移除没人认领维护、却人人都在依赖的死代码
- 规划新系统的全生命周期（弃用规划从设计阶段就要开始）
- 判断是继续维护遗留系统，还是投入迁移

## 核心原则

### 代码是一种负债

每一行代码都在持续产生成本：它需要配套的测试、文档、安全补丁、依赖更新，也会给周边修改代码的每个人带来理解负担。代码的价值在于它提供的功能，而不在于代码本身。当同样的功能可以用更少的代码、更低的复杂度或更好的抽象来提供时，旧代码就该退场。

### Hyrum 定律让移除变得困难

只要使用方足够多，系统里每一种可观察到的行为都会有人依赖，包括 bug、时序怪癖和未写入文档的副作用。正因如此，弃用必须伴随主动迁移，而不只是发一纸公告。只要旧系统里被依赖的行为在替代方案中没有被复现，用户就没法简单地“直接切换”。

### 弃用规划从设计阶段开始

构建新东西时，就要问一句：“三年后如果要下线它，我们该如何移除？”带有清晰接口、feature flag 和最小暴露面的系统，远比四处泄漏实现细节的系统更容易弃用。

## 弃用决策

弃用任何东西之前，先回答这些问题：

```
1. Does this system still provide unique value?
   → If yes, maintain it. If no, proceed.

2. How many users/consumers depend on it?
   → Quantify the migration scope.

3. Does a replacement exist?
   → If no, build the replacement first. Don't deprecate without an alternative.

4. What's the migration cost for each consumer?
   → If trivially automated, do it. If manual and high-effort, weigh against maintenance cost.

5. What's the ongoing maintenance cost of NOT deprecating?
   → Security risk, engineer time, opportunity cost of complexity.
```

## 强制弃用与建议弃用

| 类型 | 何时使用 | 机制 |
|------|-------------|-----------|
| **建议弃用（Advisory）** | 迁移是可选的，旧系统运行稳定 | 警告、文档、引导提示。使用方按自己的节奏择机迁移。 |
| **强制弃用（Compulsory）** | 旧系统存在安全隐患、阻碍后续演进，或维护成本不可持续 | 明确下线截止日期。旧系统将在日期 X 被彻底移除，并提供配套迁移工具。 |

**默认采取建议弃用。** 只有当维护成本或风险足以证明非强制迁移不可时，才采用强制弃用。启动强制弃用时，必须提供迁移工具、文档与支持——不能只甩出一个截止日期了事。

## 迁移流程

### 步骤 1: 构建替代方案

没有可用替代方案时不要急着弃用。替代方案必须满足：

- 覆盖旧系统的全部关键使用场景
- 配有完备文档和迁移指南
- 已在生产环境中被证明可行，而不只是“理论上更好”

### 步骤 2: 公告并记录

```markdown
## Deprecation Notice: OldService

**Status:** Deprecated as of 2025-03-01
**Replacement:** NewService (see migration guide below)
**Removal date:** Advisory — no hard deadline yet
**Reason:** OldService requires manual scaling and lacks observability.
            NewService handles both automatically.

### Migration Guide
1. Replace `import { client } from 'old-service'` with `import { client } from 'new-service'`
2. Update configuration (see examples below)
3. Run the migration verification script: `npx migrate-check`
```

### 步骤 3: 增量迁移

一次迁移一个使用方（consumer），不要试图一次性全量切换。对每个使用方按以下步骤推进：

```
1. Identify all touchpoints with the deprecated system
2. Update to use the replacement
3. Verify behavior matches (tests, integration checks)
4. Remove references to the old system
5. Confirm no regressions
```

**The Churn Rule（迁移兜底原则）：** 如果你负责维护正在被弃用的基础设施，你就有责任协助把使用方迁移过去，或者提供无需改动即可向后兼容的更新。不要发个弃用公告就撒手不管，让使用方自己摸索。

### 步骤 4: 移除旧系统

只有在所有使用方都完成迁移之后：

```
1. Verify zero active usage (metrics, logs, dependency analysis)
2. Remove the code
3. Remove associated tests, documentation, and configuration
4. Remove the deprecation notices
5. Celebrate — removing code is an achievement
```

## 迁移模式

### Strangler Pattern（绞杀者模式）

并行运行新旧两套系统，逐步把流量从旧系统切到新系统。当旧系统承载 0% 流量时，即可将其移除。

```
Phase 1: New system handles 0%, old handles 100%
Phase 2: New system handles 10% (canary)
Phase 3: New system handles 50%
Phase 4: New system handles 100%, old system idle
Phase 5: Remove old system
```

### Adapter Pattern（适配器模式）

创建一个适配器，把旧接口调用转换到新实现。在迁移后端实现期间，调用方仍然可以继续使用旧接口。

```typescript
// Adapter: old interface, new implementation
class LegacyTaskService implements OldTaskAPI {
  constructor(private newService: NewTaskService) {}

  // Old method signature, delegates to new implementation
  getTask(id: number): OldTask {
    const task = this.newService.findById(String(id));
    return this.toOldFormat(task);
  }

  // Translate the new shape back into what old consumers expect
  private toOldFormat(task: Task): OldTask {
    return { id: Number(task.id), title: task.title, done: task.status === 'done' };
  }
}
```

### Feature Flag Migration（功能开关迁移）

使用 feature flags 逐个将使用方从旧系统切换到新系统：

```typescript
function getTaskService(userId: string): TaskService {
  if (featureFlags.isEnabled('new-task-service', { userId })) {
    return new NewTaskService();
  }
  return new OldTaskService();
}
```

### 数据库 Schema 迁移（Expand/Contract）

Schema 变更是风险最高的迁移，因为数据是唯一无法通过回滚应用部署来还原的东西。它的典型失败模式是把 schema 变更和代码变更绑在一起发布：如果在代码开始使用新列名的同一个 release 里重命名列，那么在发布滚动窗口期内（新旧代码同时在线运行），必然有一方去查询一个不存在的列。解法是**永远不要原地修改列**，而是按增量兼容（additive）阶段分步迁移，确保每一步里新旧代码都能与当前 schema 兼容运行。

```
EXPAND ──────────────→ MIGRATE ──────────────→ CONTRACT
add the new column,    backfill existing rows,  once no code reads the
nullable, alongside    dual-write old+new from  old column, drop it in
the old one            the app                  a later, separate deploy
```

**完整示例——把 `name` 重命名为 `full_name`：**

1. **Expand（扩展）。** 以 nullable（可为空）方式新增 `full_name` 列并部署。（旧代码会忽略它，什么都不会破坏。）
2. **Dual-write（双写）。** 应用在每次 insert/update 时同时写入 `name` 和 `full_name` 并部署。
3. **Backfill（回填）。** 分批把已有数据的 `name → full_name` 复制过去，避免锁表。
4. **Switch reads（切换读取）。** 让应用改读 `full_name`，同时保持双写。部署并上线观察一段时间（bake）。
5. **Contract（收缩）。** 停止写入 `name`，随后——在一次*独立的、更晚的*部署里——删除旧的 `name` 列。

每一步都可以独立部署、独立回滚：如果第 4 步出问题，回滚代码即可，`full_name` 依然在持续写入数据。把每个阶段当作一条薄的垂直切片——参见 `incremental-implementation` skill。

**规则：**
- **先做增量兼容（additive），破坏性变更（destructive）留到最后单独做。** 新增操作（nullable 新列、新表、新索引）在任何部署中都是安全的；删列（drop）和重命名（rename）必须等到*再无任何代码引用旧结构之后*，再单独走一次独立部署。
- **每个迁移都要有经过测试的回滚路径（down path）。** 无法逆转的迁移，就是一次无法回滚的部署。合并之前先写好并跑通 `down` 脚本。
- **Backfill 要分批进行，避开核心热路径。** 对上百万行执行单条 `UPDATE` 会直接锁表；必须分块并限流执行。
- **构建大索引时不要阻塞写入**（例如 Postgres 的 `CREATE INDEX CONCURRENTLY`）。
- **当切换（cutover）风险较高时，用 feature flag 与代码部署解耦**，做法与上面的 Feature Flag Migration 模式完全一致。

## Zombie Code（僵尸代码）

Zombie code（僵尸代码）指没人负责维护、却人人都在依赖的代码。它长期得不到主动维护、没有明确 owner，并不断积累安全漏洞与兼容性问题。典型迹象包括：

- 超过 6 个月没有任何 commit，但仍有活跃使用方
- 没有明确的维护者或归属团队
- 存在失败测试却没人修复
- 依赖包含已知漏洞却没人升级
- 文档引用了早已下线的系统

**应对方式：** 要么指定 owner 并妥善维护，要么制定具体的迁移计划将其弃用下线。Zombie code 不能一直悬在半空中——它要么获得正常维护投入，要么被彻底移除。

## 常见合理化借口

| 合理化借口 | 现实 |
|---|---|
| “它还能用，为什么要移除？” | 无人维护的可用代码会悄然积累安全债与复杂度，维护成本正是在不知不觉中越滚越大。 |
| “以后可能有人会需要它” | 如果以后真需要，届时可以重建。为了“以防万一”保留未使用的旧代码，成本通常高于重建。 |
| “迁移太贵了” | 把迁移成本和未来 2-3 年的持续维护成本算笔账：长期来看，迁移几乎总是更便宜。 |
| “等新系统完成后再弃用它” | 弃用规划从设计阶段就要开始。等新系统做完时，你早就被新的优先级推着走了。现在就规划。 |
| “用户会自己迁移” | 他们不会主动迁的。提供迁移工具、文档和激励机制，或者自己动手完成迁移（The Churn Rule）。 |
| “我们可以无限期维护两个系统” | 两套系统做同一件事，意味着维护、测试、文档和新人上手成本统统翻倍。 |
| “只是重命名一列，就一行代码” | 发布滚动期间新旧代码同时运行，必有一方会去查询一个已不存在的列。必须走 expand/contract，绝不要原地重命名。 |
| “我在同一个迁移里加新列并删掉旧列” | 这会把一个安全的增量新增和一个破坏性的删列耦合在一起。删列必须有自己独立的部署，且发生在没有任何代码引用旧结构之后。 |
| “等需要时再写回滚” | 没有 down path 的迁移，就是一次无法逆转的部署。合并之前先写好并跑通 `down`。 |

## 危险信号

- 已弃用系统没有可用替代方案
- 发了弃用公告却没有配套的迁移工具或文档
- 所谓“软性”建议弃用拖了多年却毫无进展
- 没有 owner 的僵尸代码（zombie code）仍有活跃使用方
- 还在给已弃用系统添加新功能（应当把精力投到替代方案上）
- 未先度量当前使用情况就直接启动弃用
- 未确认活跃使用方已清零就贸然移除代码
- Schema 变更与依赖它的代码变更混在同一次部署中上线
- 列被原地重命名或删除，而未走 expand/contract 流程
- 迁移已合并却没有经过测试的 down path，或 backfill 操作直接锁表

## 验证

完成一次弃用后：

- [ ] 替代方案已在生产环境中得到验证，并覆盖全部关键使用场景
- [ ] 迁移指南已就绪，且包含具体步骤与示例
- [ ] 所有活跃使用方均已完成迁移（已通过指标/日志核实）
- [ ] 旧代码、相关测试、文档和配置已彻底移除
- [ ] 代码库中已不再残留对已弃用系统的引用
- [ ] 弃用通知已清理移除（它们已完成使命）

完成一次数据库 schema 迁移后：

- [ ] 变更按增量兼容阶段发布（expand → backfill → contract），而非一次原地改动
- [ ] 在每一步部署状态下，新旧代码都能与当前 schema 兼容运行
- [ ] 每次迁移都有经过实测的 down path；backfill 以限流批次运行
- [ ] 破坏性步骤（drop/rename）只在没有任何代码引用旧结构之后，通过单独的部署发布
