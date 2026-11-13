# 编排模式

本仓库认可的 agent 编排模式参考目录，以及需要避免的反模式。添加会协调多个 personas 的新 slash command 前，或引入一个“包装”现有 personas 的新 persona 前，请先阅读本目录。

治理规则：**用户（或 slash command）是 orchestrator。Personas 不调用其他 personas。** Skills 是 persona 工作流中的必经环节。

---

## 认可模式

### 1. 直接调用（无编排）

单个 persona、单一视角、单个产物。默认选择，也是成本最低的选择。

```
user → code-reviewer → report → user
```

**适用场景：** 任务只从单一视角审视单个产物，并且可以用一句话描述。

**示例：**
- "审查这个 PR" → `code-reviewer`
- "查找 `auth.ts` 中的安全问题" → `security-auditor`
- "checkout flow 缺少哪些测试？" → `test-engineer`

**成本：** 一次往返。评估任何编排模式时，都应以此作为对比基线。

---

### 2. 单 persona slash command

用一个 slash command 把单个 persona 和项目 skills 封装起来，让用户不必每次都重新解释工作流。

```
/review → code-reviewer (with code-review-and-quality skill) → report
```

**适用场景：** 同一个单 persona 调用会以相同设置反复发生。

**本仓库示例：** `/review`、`/test`、`/code-simplify`。

**成本：** 与直接调用相同。slash command 只是保存好的 prompt。

**反信号：** 如果 slash command 的主体主要是“决定要调用哪个 persona”，删除它，让用户直接调用 persona。

---

### 3. 并行 fan-out 后合并

多个 personas 同时处理同一个输入，各自产生独立报告。合并步骤（在 main agent 的上下文中）将它们综合成一个决策。

```
                    ┌─→ code-reviewer    ─┐
/ship → fan out  ───┼─→ security-auditor ─┤→ merge → go/no-go + rollback
                    └─→ test-engineer    ─┘
```

**适用场景：**
- 子任务真正独立（没有共享可变状态，没有顺序依赖）
- 每个 sub-agent 都能从自己的 context window 中受益
- 合并步骤足够小，可以留在 main context 中完成
- 端到端等待耗时（wall-clock latency）很关键

**本仓库示例：** `/ship`。

**成本：** N 个并行 sub-agent contexts + 一个 merge turn。成本高于直接调用，但端到端等待时间更短，报告质量也更好，因为每个 sub-agent 都专注于自己的单一视角。

**采用该模式前的验证清单：**
- [ ] 我能否同时运行所有 sub-agents，且没有顺序依赖问题？
- [ ] 每个 persona 是否产生不同*类型*的发现，而不是从不同角度重复同一发现？
- [ ] 合并步骤是否能放进 main agent 剩余的 context？
- [ ] 用户等待时间是否足够长，长到并行执行确实能带来可感知收益？

如果任何答案是“否”，退回直接调用或单 persona command。

---

### 4. 由用户驱动的顺序 slash command pipeline

用户按定义好的顺序运行 slash commands，在步骤之间携带 context（或 commit history）。没有 orchestrator agent —— 用户**就是** orchestrator。

```
user runs:  /spec  →  /plan  →  /build  →  /test  →  /review  →  /ship
```

**适用场景：** 工作流存在依赖（每一步都需要前一步的输出），并且步骤之间的人工判断有价值。

**本仓库示例：** 完整的 DEFINE → PLAN → BUILD → VERIFY → REVIEW → SHIP 生命周期。

**成本：** 每一步一个 sub-agent context。编排层零额外开销，因为没有 orchestrator agent。

**为什么不自动化：** LLM “lifecycle orchestrator” 会 (a) 因交接时必须做摘要而丢失步骤间的微妙细节，(b) 跳过能及早发现方向跑偏的人工检查点，(c) 通过转述回合使 token 成本翻倍。

---

### 5. 研究隔离（保留 context）

当任务需要阅读大量不应污染 main context 的材料时，启动一个 research sub-agent，只返回摘要（digest）。

```
main agent → research sub-agent (reads 50 files) → digest → main agent continues
```

**适用场景：**
- 主会话需要专注于下游任务
- 调查结果远小于它消费的输入
- 调查完成后，main agent 留有充足思考空间能提升决策质量

**示例：** “在 monorepo 中找到这个 deprecated API 的每个调用点”，“总结这 30 个 ADRs 对缓存的说明”。

**成本：** 一个隔离的 sub-agent context。只要替代方案是把数百个文件加载进 main context，就值得使用。

**在 Claude Code 中，使用内置 `Explore` subagent**，不要定义自定义 research persona。`Explore` 运行在 Haiku 上，被禁用了 write/edit tools，并且专为该模式构建。只有当 `Explore` 不适合时（例如你需要模型无法自行推断的领域专属 system prompt），才定义自定义 research subagent。

---

## Claude Code 兼容性

本目录本身不绑定特定宿主工具（harness），但大多数读者会在 Claude Code 中运行。下面说明每种模式如何映射到 Claude Code 的原语机制（primitives），以及平台在哪些地方替我们强制执行规则。

### Personas 存放位置

Plugin subagents 放在 plugin 根目录的 `agents/` 中。本仓库是一个 plugin（`.claude-plugin/plugin.json`），因此启用 plugin 后会自动发现 `agents/code-reviewer.md`、`agents/security-auditor.md` 和 `agents/test-engineer.md`。不需要配置路径。

### Subagents vs. Agent Teams

Claude Code 有两种并行 primitive。模式 3（并行 fan-out 后合并）映射到 **subagents**。如果需要能彼此交谈的 teammates，请改用 **Agent Teams**。

| | Subagents | Agent Teams |
|--|-----------|-------------|
| 协调方式 | Main agent 做 fan-out 派发，sub-agents 只向其汇报结果 | Teammates 互相发消息，共享 task list |
| Context | 每个 subagent 自己的 context window | 每个 teammate 自己的 context window |
| 何时使用 | 产生报告的独立任务 | 需要讨论的协作工作 |
| 状态 | 稳定 | 实验性 —— 需要 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` |
| 成本 | 较低 | 较高 —— 每个 teammate 都是一个独立 Claude instance |

**本仓库中的 personas 可在两种模式下工作。** 作为 subagents 派发时（例如由 `/ship` 拉起），它们向 main session 汇报 findings。作为 teammates 拉起时（`Spawn a teammate using the security-auditor agent type…`），它们可以直接挑战彼此的 findings。Persona 定义相同，只有启动上下文（spawning context）不同。

一个细节：persona 中的 `skills` 和 `mcpServers` frontmatter 字段在作为 subagent 运行时会生效，但**作为 teammate 运行时会被忽略** —— teammates 会像普通会话一样从你的项目和用户设置中加载 skills 和 MCP servers。如果某个 persona 依赖特定 skill 或 MCP server 已加载，请在会话级别（session level）配置，使其在两种模式下都可用。

### 平台强制执行的规则

本目录中的两条规则不只是约定 —— Claude Code 会强制执行它们：

- **"Subagents cannot spawn other subagents"**（来自官方文档的原文）。反模式 B（persona 调用 persona）和反模式 D（深层 persona trees）在 Claude Code 上从机制构造上就无法成立。
- **"No nested teams"** —— teammates 不能 spawn 自己的 teams。同样的反模式在 team 层级也会被阻断。

这意味着你可以放心采用本目录中的模式，而不必担心贡献者不小心写出这些反模式——一旦误写，根本加载不起来。

### 需要了解的内置 subagents

定义自定义 subagent 前，检查这些是否已经覆盖对应角色：

| 内置 subagent | 用途 |
|---|---|
| `Explore` | 只读代码库检索与分析。用于模式 5（研究隔离）。 |
| `Plan` | plan mode 中的只读调研。 |
| `general-purpose` | 需要探索和修改的多步任务。 |

不要重新定义这些内置角色。在它们之上叠加你的专业视角 personas（`code-reviewer`、`security-auditor`、`test-engineer`）。

### Plugin agents 的 frontmatter 限制

Plugin subagents **不**支持 `hooks`、`mcpServers` 或 `permissionMode` frontmatter 字段 —— 这些字段会被静默忽略。如果未来某个 persona 需要其中任一字段，用户必须把文件复制到 `.claude/agents/` 或 `~/.claude/agents/`。

Plugin agents 中可用的字段包括：`name`、`description`、`tools`、`disallowedTools`、`model`、`maxTurns`、`skills`、`memory`、`background`、`effort`、`isolation`、`color`、`initialPrompt`。如果想优化成本，可以按 persona 使用 `model`（例如 Haiku 用于 `test-engineer` coverage scans，Sonnet 用于 `code-reviewer`，Opus 用于 `security-auditor`）。

### 并行 spawn 多个 subagents

在 Claude Code 中，并行 fan-out（模式 3）需要在**同一个 assistant 回合（turn）中发出多个 Agent tool calls**。跨回合顺序调用会串行化执行。`/ship` 明确指出了这一点。任何新的编排命令（orchestrator command）也应如此。

---

## 实战示例：用 Agent Teams 做竞争假设调试

这个示例展示何时应该使用 **Agent Teams**，而不是 `/ship` 的 subagent fan-out。两种模式表面上看很像 —— 都会启动同样的三个 personas —— 但各自发挥价值的方式完全不同。

### 场景

> *Checkout 偶尔会在完成前卡住约 30 秒。大约每 50 个 sessions 发生一次。日志中没有错误。问题从上周发布后开始。*

可能的根因（互斥，且都符合症状）：

1. 新 payment-confirmation flow 中的竞态条件（race condition）
2. 一个 auth check 偶尔回落到慢速同步网络调用
3. 某个查询缺少索引，随购物车规模扩大而变慢
4. 某个不稳定的第三方 API，SDK 在超时前静默重试

单个 agent 会选中第一个看起来合理的理论，然后停止调查。`/ship` 风格的 subagent fan-out 会让每个 persona 独立汇报 —— 但彼此无法互通结果，因此无法相互排除错误假设。

这正是 Agent Teams 官方文档描述的场景：*“当多个独立调查者主动尝试反驳彼此时，经受住考验留存下来的理论更可能是真正的根因。”*

### 为什么这*不是* `/ship` 的工作

| | `/ship` (subagents) | Agent Teams |
|--|--------------------|-------------|
| Sub-agents 看到 | 同一个 diff，不同视角 | 一个共享 task list，以及彼此的 messages |
| 输出 | 三份独立报告 → 一次合并 | 对抗式辩论 → 共识根因 |
| 适合场景 | 你想对已知产物下定论 | 你想在多个假设中*锁定*问题所在 |

`/ship` 负责下定论（verdict）；Agent Teams 负责排查定位（investigation）。

### 设置（每个环境一次）

Agent Teams 处于实验阶段。在 `~/.claude/settings.json` 中：

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

需要 Claude Code v2.1.32 或更高版本。本仓库中的 personas 会自动识别加载 —— 不需要手写 team-config 文件。

### 触发 prompt

在 lead session 中用自然语言输入：

```
Users report checkout hangs for ~30 seconds intermittently after last
week's release. No errors in logs.

Create an agent team to debug this with competing hypotheses. Spawn
three teammates using the existing agent types:

  - code-reviewer  — investigate race conditions and blocking calls
                     in the checkout code path
  - security-auditor — investigate auth checks, session handling,
                       and any synchronous network calls added recently
  - test-engineer  — propose tests that would distinguish between the
                     hypotheses and check coverage gaps in checkout

Have them message each other directly to challenge each other's
theories. Update findings as consensus emerges. Only converge when
two teammates agree they can disprove the others'.
```

Lead 会引用现有 persona 名称拉起三个 teammates。每个 persona 的正文会作为附加指令**追加**到对应 teammate 的 system prompt（位于 lead 下发的团队协作指令之上）；上面的触发 prompt 会成为它们的任务。

### 会发生什么

1. 每个 teammate 在自己的 context window 中运行，从各自视角探索 codebase。
2. Teammates 使用 `message` 直接互相发送 findings。Lead 不需要中转。
3. 共享 task list 显示谁在调查什么 —— 可随时用 `Ctrl+T`（in-process mode）或 tmux pane（split mode）查看。
4. 当 `code-reviewer` 发现一个本应顺序执行的 `Promise.all` 时，它会发消息给 `security-auditor`，确认 auth call 是否不属于该竞态。`security-auditor` 检查并回复 —— 要么确认竞态就是真正问题，要么提供反证。
5. `test-engineer` 为当前最站得住脚的理论提出一个聚焦的集成测试，团队用它在宣布共识前先验证。
6. Lead 综合收敛后的发现并呈现给你。

你可以通过 `Shift+Down` 切换到任意 teammate 并输入内容来随时打断 —— 当某个调查方向走偏时，可以用这种方式及时纠偏。

### 何时清理

当调查锁定某个根因后，告诉 lead：

```
Clean up the team
```

始终通过 lead 来清理（cleanup），而不是通过 teammate（按文档说明：teammates 缺少完整 team 上下文，无法执行清理）。

### 成本预期

三个 Sonnet teammates 运行约 10–15 分钟调查，成本会明显高于由 `/ship` 以 subagents 方式启动同样三个 personas。理由是*结论质量* —— 在生产环境排障中，修错方向的代价高昂，多花的 tokens 很划算。对于常规 PR review，坚持使用 `/ship`。

### 这个场景中的反模式

**不要**把它重建成 fan out subagents 的 `/debug` slash command。Subagents 不能互相发消息 —— 你会失去让该模式成立的对抗式辩论。如果某个工作流反复出现，把上面的触发 prompt 记录为可复用片段（snippet），而不是包装成误用 subagents 的 slash command。

### 什么时候*不*使用 Agent Teams

- 对已知 diff 做上线前的放行判断（verdict） → 使用 `/ship` (subagents)。
- 对一个产物做单个专精视角审视 → 直接调用 persona。
- 顺序生命周期（spec → plan → build） → 用户驱动的 slash commands（模式 4）。
- 大量读取、只需小摘要（digest）的调研 → 内置 `Explore` subagent。

只有当 teammates **需要**互相挑战才能得出正确答案时，才使用 Agent Teams。

---

## 反模式

### A. Router persona（“meta-orchestrator”）

一个 persona 的职责是决定要调用哪个其他 persona。

```
/work → router-persona → "this needs a review" → code-reviewer → router (paraphrases) → user
```

**失败原因：**
- 纯路由层（routing），没有领域价值
- 多出两次转述中转（paraphrasing hops） → 信息损失 + 约 2× token 成本
- 用户已经知道自己想要 review；他们本可以直接调用 `/review`
- 重复了 slash commands 和 `AGENTS.md` 中意图映射（intent mapping）已经做过的工作

**替代做法：** 添加或改进 slash commands。在 `AGENTS.md` 中记录 intent → command 映射。

---

### B. 调用另一个 persona 的 persona

一个 `code-reviewer` 在看到 auth code 时内部调用 `security-auditor`。

**失败原因：**
- Personas 被设计为产生单一视角；串联它们会破坏这一点
- 调用 persona 传递的摘要会丢失被调用 persona 需要的 context
- Failure modes 成倍增加（哪个 persona 的 output format 获胜？谁的规则适用？）
- 对用户隐藏成本

**替代做法：** 让调用 persona 在报告中*建议*后续 audit。由用户或 slash command 运行第二轮。

---

### C. 会转述的顺序 orchestrator

一个 agent 代表用户调用 `/spec`，再调用 `/plan`，再调用 `/build`，依此类推。

**失败原因：**
- 丢失能及早发现方向跑偏的人工检查点
- 每次 hand-off 都会摘要 context —— 长 pipeline 中会不断累积偏差（drift）
- Token 成本翻倍：每一步都有 orchestrator 回合 + sub-agent 回合
- 恰好在最需要判断的节点剥夺了用户主导权（agency）

**替代做法：** 保持用户作为 orchestrator。在 `README.md` 中记录推荐顺序，让用户调用它。

---

### D. 深层 persona trees

`/ship` 调用一个 `pre-ship-coordinator`，后者调用 `quality-coordinator`，后者再调用 `code-reviewer`。

**失败原因：**
- 每一层都增加延迟和 token 消耗，却没有决策价值
- 调试会变成多层级的调查追查
- 末端的叶子 personas 会因多层摘要传递而丢失上下文

**替代做法：** 将编排深度控制在最多 1 层（slash command → personas）。合并在 main agent 中完成。

---

## 决策流程

考虑新的编排 workflow 时，按这个流程走：

```
Is the work one perspective on one artifact?
├── Yes → Direct invocation. Stop.
└── No  → Will the same composition repeat?
         ├── No  → Direct invocation, ad hoc. Stop.
         └── Yes → Are sub-tasks independent?
                  ├── No  → Sequential slash commands run by user (Pattern 4).
                  └── Yes → Parallel fan-out with merge (Pattern 3).
                           Validate against the checklist above.
                           If any check fails → fall back to single-persona command (Pattern 2).
```

---

## 何时向本目录添加新模式

只有满足以下条件后，才添加新条目：

1. 你已经在真实工作中至少使用过该模式两次
2. 你能指出本仓库中展示该模式的具体 artifact
3. 你能解释为什么现有模式无法胜任
4. 你能描述它的反面误用情形（人们最容易把它错建成什么）

过早收进目录的条目会变成没人遵守的一纸空谈（愿望式文档）。
