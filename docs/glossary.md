# NexusKit 术语与翻译词汇表

维护者向参考文档：**执行技能的 Agent 不需要读取本文件**。

v0.4.0 起，原 `CONCEPTS.md`（v0.3.x 领域术语）与 `context.md`（Matt Pocock / CE 译法表）合并收敛为本文件。由于早期简体中文上游 `vinvcn/addyosmani-agent-skills-zh` 已长期停更，后续版本跟进直接以 `.upstream/addyosmani-agent-skills`（跟踪英文上游 [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills)）为准；同期增量与校对中遇到的新术语与译法统一收口至此，保持 25 个技能、`references/`、`agents/` 与 `.claude/commands/` 前后一致。

---

## 一、翻译与行文总则

1. **自然中英混排，禁止杂糅英文语法**：中文程序员日常交流高频使用的专业英文词汇可直接保留英文（如 `skill`、`agent`、`spec`、`plan`、`task`、`PR`、`diff`、`commit`、`endpoint`、`API`、`harness`、`fallback`、`no-op`、`lockfile`、`semver`、`codemods` 等），但不把英文动词屈折、分词或生硬词序塞进中文句式（避免“来 exploiting”、“一个 failing 的测试”等写法）。
2. **关键或首次概念括注**：需要中文语义定锚、或仅看英文易产生歧义的术语，采用「中文（English）」形式首次说明（如 `边界情况（edge cases）`、`灰度（Canary）`、`应急开关（kill switch）`、`增量兼容（additive）`）；同文后续出现直接沿用其中一种并保持一致性，不必句句重复括号。
3. **保留英文不变的位点**：
   - 25 个上游技能的目录名、公开技能名、H1 标题（例如 `# Code Review and Quality`）与 frontmatter `description` 原文（`description` 按触发率调校过，不译）。
   - 给 Agent 读取或机器匹配的模板结构标题与状态值（例如 `Objective`、`Tech Stack`、`Task List`、`Problem Statement`、`ARTIFACT` / `CONTRACT`、`Status: PROPOSED | ACCEPTED`、`Review: [PR/Change title]`、`GO | NO-GO`）。
   - 工具名、CLI 参数、协议/标准缩写与固定名称（如 `OWASP Top 10`、`STRIDE`、`WCAG 2.1 AA`、`Core Web Vitals` / `LCP` / `INP` / `CLS` / `TTFB` / `LoAF`、`RED` / `USE`、`SLO`、`PII`、`IDOR`、`SSRF`、`Semgrep`、`gitleaks`、`osv-scanner`、`axe-core`、`Lighthouse`）。
4. **NexusKit 本地化规则**：
   - 上游 slash 命令名统一加 `nk-` 前缀：`/spec` → `/nk-spec`、`/plan` → `/nk-plan`、`/build` → `/nk-build`、`/test` → `/nk-test`、`/review` → `/nk-review`、`/ship` → `/nk-ship`、`/constraints` → `/nk-constraints`、`/code-simplify` → `/nk-code-simplify`、`/webperf` → `/nk-webperf`；移除 `agent-skills:` 命名空间前缀。
   - 宿主规则文件统一表述为「项目的 agent 规则文件（`CLAUDE.md` / `AGENTS.md`）」或「`CLAUDE.md` / `AGENTS.md`」，不单独写死为单一客户端（明确讨论 Claude Code 平台特性的段落除外）。
   - 跨技能引用使用公开技能名（如 `` `code-review-and-quality` ``），不跨技能引用私有路径；共享检查清单位于 `../../references/*.md`。
5. **标点、格式与文风**：
   - 中文正文使用中文全角标点；说明性破折号优先双字破折号 `——`；数值范围用 `–`（如 `1–3 天`、`2–4 个`）。
   - 提示块标签译作 `> **注意：**`，不用 `> **Note:**`。
   - 去掉 AI 套话与英文直译腔（如「验证叙事」「彻底破坏」等）；将冗长被动句改为地道中文主动表达，同时严格保留原句的否定词、限定条件与数值边界。

---

## 二、标准化结构标题与列头

### 1. 25 技能通用结构

| 英文原文 | NexusKit 统一写法 | 备注 |
|---|---|---|
| H1 技能标题 | 保留英文原题 | 25/25 技能 H1 与英文上游逐字一致 |
| `description` (SKILL.md frontmatter) | 保留英文原文 | `agents/*.md` 与 `.claude/commands/*.md` 则用简体中文 |
| `Overview` | `## 概览` | 25/25 技能统一（规划模板代码块内 `## Overview` 例外，属输出格式原文） |
| `When to Use` | `## 何时使用` | 24/25 技能统一（`using-agent-skills` 无此节） |
| `When NOT to Use` | `**何时不使用：**` | 部分既有译文写作 `何时不要使用：`，新改写优先统一用 `何时不使用：` |
| `Core Principles` | `## 核心原则` | |
| `Workflow` | `## 流程` | |
| `Common Rationalizations` | `## 常见合理化借口` | 24/25 技能统一 |
| `\| Rationalization \| Reality \|` | `\| 合理化借口 \| 现实 \|` | 24/25 技能合理化表列头完全统一 |
| `Red Flags` | `## 危险信号` | 24/25 技能统一；**禁止译作「红旗」** |
| `Verification` | `## 验证` | 24/25 技能统一（测试计划模板子节 `### Verification` 保留英文） |
| `See Also` | `## 另见` | |
| `Interaction with Other Skills` | `## 与其他 skill 的关系` | |
| `Dead Code Hygiene` | `## 死代码清理` | `code-review-and-quality`（不用「死代码卫生」） |

### 2. 步骤与阶段标题

| 原文 | 现状与规范 | 注意事项 |
|---|---|---|
| `Stage 0` – `Stage 4` | `### 阶段 N：...` | `spec-driven-development`、`idea-refine/examples.md` |
| `Step N` | 既有文件并存三种：`### 步骤 N：...`（`planning`、`tdd`、`performance`、`code-simplification`、`deprecation`）、`### 第 N 步：...`（`code-review`、`debugging`、`source-driven`）、`### Step N: ...`（`interview-me`、`constraint`、`doubt-driven`） | 校对既有文件时顺应其内部编号风格，不跨文件强改；修改标题文字时须同步检查同文件的 `#anchor` 链接（可通过 `python tests/run_checks.py` 验证） |
| `agents/*.md` 收尾 | `## 输出格式`、`## 规则`、`## 组合方式` | 五个子智能体对齐一致（`doubt-challenger` 无输出模板与组合方式，只含 `输入`、`审查重点`、`规则`） |

---

## 三、英文上游核心词汇表

### A. 技能体系与 Agent 编排

| 英文原词 | NexusKit 译法 / 处理 | 说明与避坑 |
|---|---|---|
| `skill(s)` | 正文多保留 `skill(s)`；泛指概念或总量时可用「技能」 | 避免在同一句混称且指代不明 |
| `agent(s)` | 保留 `agent(s)`；指代插件定义实体时可用「子智能体」 | 例如「5 个子智能体」 |
| `subagent(s)` / `sub-agent(s)` | 正文多保留 `subagent(s)`；配对中文用「子智能体」 | **不再译作「子代理」**；新增文档尽量用 `subagent` 不带连字符 |
| `persona(s)` | 保留 `persona(s)`，必要时说明「专精 persona / 专精视角」 | **不译作「人格」** |
| `teammate(s)` | 保留 `teammate(s)` | Claude Code Agent Teams 术语 |
| `orchestrator` / `orchestration` | `orchestrator` / `编排（orchestration）` | |
| `harness` | `宿主环境（harness）` 或保留 `harness` | 指 Claude Code 等运行宿主 |
| `rules file` | `规则文件` | 具体指 `CLAUDE.md` / `AGENTS.md` |
| `turn` | `回合（turn）` | 如「在同一个 assistant 回合（turn）中」 |
| `hand-off` / `handoff` | `交接（hand-off）` | |
| `fan-out` | 保留 `fan-out` | 如「并行 fan-out」 |
| `digest` | `摘要（digest）` | 研究隔离模式下只读探索返回的精简结果 |
| `drift` | `漂移` / `偏差（drift）` | 如「上下文漂移」 |
| `paraphrasing hops` | `转述中转（paraphrasing hops）` | |
| `user agency` / `agency` | `用户主导权（agency）` | |
| `context window` / `fresh context` | 保留 `context window` / `全新上下文（fresh context）` | |
| `The Brain Dump` / `The Selective Include` / `The Hierarchical Summary` | `全量背景交底（The Brain Dump）` / `选择性包含（The Selective Include）` / `分层摘要（The Hierarchical Summary）` | `context-engineering` 上下文打包三策略 |
| `confusion management` | `困惑管理` | `context-engineering` |

### B. 需求、规划、实现与通用工程

| 英文原词 | NexusKit 译法 / 处理 | 说明与避坑 |
|---|---|---|
| `spec` / `specification` | 保留 `spec`（产物实体）；泛指可作 `specification` / `规格` | |
| `capability map` | 保留 `capability map` | 多模块拆分索引文件 `spec/capability-map.md` |
| `plan` / `task` | 保留 `plan` / `task`（通用语境亦可作「计划 / 任务」） | |
| `acceptance criteria` | `验收标准（acceptance criteria）` | |
| `vertical slice` | `垂直切片` | **不再译作「纵向切片」或「曳光弹 / tracer bullet」** |
| `checkpoint` | 保留 `checkpoint` 或 `检查点` | `issue-graph.md` 节点名统一用 `checkpoint` |
| `artifact` | `产物` 或保留 `artifact` | `doubt-challenger` 中专用大写 `ARTIFACT` |
| `contract` | `契约` 或保留 `contract` | `doubt-challenger` 中专用大写 `CONTRACT` |
| `boundary` / `boundaries` | `边界` / `已知边界` | |
| `Floor` / `Ratchet` | `Floor`（可作 `Floor 基线` / `底线（floor）`）/ `Ratchet（棘轮）` | `CONSTRAINTS.md` 模板小节名保持英文 |
| `baseline` | `基线` 或保留 `baseline` | |
| `scope` / `scope discipline` | `范围（scope）` / `范围纪律` | |
| `edge case(s)` | `边界情况（edge cases）` | 统一用「边界情况」，避免「边缘情况」 |
| `fallback` | 保留 `fallback`，或按语境作 `降级方案` / `回退` / `兜底` | |
| `workaround` | `权宜方案` / `临时绕过方案`（或保留 `workaround`） | |
| `trade-off` | `权衡取舍` / `权衡` | |
| `no-op` | 保留 `no-op` | |
| `stub` | `占位桩（stub）` 或保留 `stub(s)` | |
| `consumer` / `caller` | `使用方（consumer）` / `调用方（caller）` | `deprecation` 与 `api-design` 优先统一用「使用方」 |
| `design tokens` | 保留 `design tokens` | |

### C. 测试、调试与验证

| 英文原词 | NexusKit 译法 / 处理 | 说明与避坑 |
|---|---|---|
| `Red-Green-Refactor` | 保留 `Red-Green-Refactor` / `RED → GREEN → REFACTOR` | |
| `Prove-It pattern` | 保留 `Prove-It pattern` | Bug 修复先写失败测试再修；不用中文生造词 |
| `DAMP over DRY` | `DAMP 优于 DRY` / 保留 `DAMP over DRY` | 测试代码可读性优先原则 |
| `test suite` / `unit test` / `integration test` / `E2E test` | `测试套件` / `单元测试` / `集成测试` / `E2E 测试`，亦可保留英文 | |
| `flaky test(s)` | `不稳定的测试（flaky tests）` | |
| `mock` / `fixture` | 保留 `mock` / `fixture` | |
| `mutation testing` / `mutation score` | `变异测试（mutation testing）` / `变异得分（mutation score）` | |
| `regression` | `回归（问题）` 或 `regression` | |
| `triage` | `分诊（triage）` | |
| `Stop-the-Line` | 保留 `Stop-the-Line` | 如 `## Stop-the-Line 规则` |
| `git bisect` | `二分定位（git bisect）` | |
| `minimal reproduction` | `最小复现（minimal reproduction）` | |

### D. 审查、简化、安全与性能

| 英文原词 | NexusKit 译法 / 处理 | 说明与避坑 |
|---|---|---|
| `five-axis review` | `五轴审查` / `五轴 code review` | 五轴名保持 `Correctness`、`Readability`、`Architecture`、`Security`、`Performance` |
| `finding(s)` | `发现` 或保留 `findings` | **不译作「审查结果/发现项」之外的生僻词** |
| `severity`: `Critical` / `Required` / `Optional` (`Consider`) / `Nit` | 保留英文分级标签 | `nit` 首次可括注 `小问题（nit）`；安全/性能审计用 `Critical / High / Medium / Low / Info` |
| `blocking` / `non-blocking` / `blocker` | 保留 `blocking` / `non-blocking`；`阻塞项（blocker）` | |
| `verdict` | `定论` / `放行判断（verdict）` | |
| `presumptive blocker` | `推定阻塞项（presumptive blockers）` | |
| `Chesterton's Fence` | 保留 `Chesterton's Fence` | 简化/删改前先搞清既有代码存在原因 |
| `Hyrum's Law` | 保留 `Hyrum's Law` / `Hyrum 定律` | |
| `guard clause` | `卫语句（guard clauses）` | |
| `dead code` / `zombie code` | `死代码` / `Zombie Code（僵尸代码）` | |
| `shim` / `codemod` | 保留 `shim` / `codemod(s)` | |
| `churn` | 语境区分：code churn 作 `无意义的代码折腾（churn）`；`The Churn Rule` 作 `迁移兜底原则` | 避免把两种不同意思混用 |
| `allowlist` / `ownership` / `provenance` / `typosquatting` | `白名单（allowlist）` / `维护者归属（ownership）` / `构建溯源（provenance）` / `仿冒包名（typosquatting）` | 弃用旧“whitelist”习惯，统一 `allowlist` |
| `trust boundary` / `least privilege` / `defense-in-depth` | `信任边界（trust boundaries）` / `最小权限原则` / `纵深防御（defense-in-depth）` | |
| `threat modeling` | `威胁建模` | `STRIDE`、`IDOR`、`SSRF`、`prompt injection`、`excessive agency` 保留英文 |
| `Quick 模式` / `Deep 模式` / `Metric-Honesty` | 保留 `Quick 模式`、`Deep 模式`、`Metric-Honesty` | `Field (CrUX)` 与 `Lab (Lighthouse)` 严格区分，禁止混为一谈 |
| `facade` / `layout thrashing` | `轻量占位门面（facade）` / `layout thrashing` | `Core Web Vitals` / `LCP` / `INP` / `CLS` / `TTFB` / `LoAF` 保留英文 |

### E. 版本管理、CI/CD、弃用、观测与发布

| 英文原词 | NexusKit 译法 / 处理 | 说明与避坑 |
|---|---|---|
| `trunk-based development` / `atomic commit` / `worktree` | 保留英文 | |
| `force-push` / `stage` / `revert` | `强推（force-push）` / `暂存（stage）` / `回退（revert）` | |
| `Shift Left` / `Faster is Safer` | `质量左移（Shift Left）` / `小步快跑更安全（Faster is Safer）` | |
| `pipeline` / `quality gate` | `pipeline`（或 `流水线`）/ `质量门禁` | |
| `semver` / `breaking change` / `changelog` / `release` / `tag` | 保留英文术语（`breaking change` 可作 `破坏性变更`） | |
| `deprecation` / `migration` | `弃用（deprecation）` / `迁移（migration）` | |
| `Advisory` / `Compulsory` (deprecation) | `建议弃用（Advisory）` / `强制弃用（Compulsory）` | |
| `Expand–Contract` / `additive` / `destructive` / `backfill` / `bake` / `cutover` / `down path` | `Expand–Contract` / `增量兼容（additive）` / `破坏性变更（destructive）` / `回填（backfill）` / `上线观察（bake）` / `切换（cutover）` / `回滚路径（down path）` | Schema 五步：`Expand（扩展）→ Dual-write（双写）→ Backfill（回填）→ Switch reads（切换读取）→ Contract（收缩）` |
| `feature flag` / `canary` / `kill switch` / `preview deployment` / `big-bang release` | 保留 `feature flag` / `灰度（Canary）` / `应急开关（kill switch）` / `preview deployment（预览部署）` / `一次性全量发布（Big-bang releases）` | **`canary` 统一作「灰度」，不译「金丝雀」** |
| `rollback` | `回滚（rollback）` | |
| `observability` / `telemetry` / `instrumentation` | `可观测性（observability）` / `telemetry（遥测数据）` / `埋点` | |
| `RED` / `USE` / `correlation ID` / `span` / `histogram` / `cardinality` | 缩写与术语保留英文；`基数爆炸（Cardinality）` | `RED` = Rate/Errors/Duration；`USE` = Utilization/Saturation/Errors |
| `SLO` / `error budget` / `burn rate` / `on-call` / `pager` / `runbook` | 保留英文，仅在首次必要处括注 `寻呼（pager）` | |
| `actionable` / `Hold` | `可行动（actionable）` / `暂停（Hold）` | 发布决策阈值三态：Go / Hold / Rollback |

---

## 四、NexusKit 自有概念与架构约定

### 1. 命令与插件入口

- **10 个 `nk-` 命令**（全部配置 `disable-model-invocation: true`，仅用户显式调用）：`/nk-init`（NexusKit 自研项目接入入口）以及 9 个上游派生入口 `/nk-spec`、`/nk-plan`、`/nk-build`、`/nk-test`、`/nk-constraints`、`/nk-review`、`/nk-webperf`、`/nk-code-simplify`、`/nk-ship`。
- **仓库不是实时加载源**：Claude Code 等客户端读取的是安装快照；校验清单与路径一致性通过 `python tests/run_checks.py`（6 项检查：`link-integrity`、`references`、`byte-budget`、`distribution`、`artifact-paths`、`frontmatter`）守护。

### 2. 项目接入与「项目约定」（`/nk-init`）

目标仓库首次接入 NexusKit 时，`/nk-init` 按“探测现状 → 逐项确认 → 展示草稿 → 幂等写入”确认七项决策并写入规则文件（`AGENTS.md` 或 `CLAUDE.md`）的 `## 项目约定` 小节（不预建空目录、不自动提交）：

1. 规则文件落点（`AGENTS.md` / `CLAUDE.md`）
2. `idea` 落点（默认 `docs/ideas/`，一想法一文件）
3. 决策记录位置（默认 `docs/adr/`，连续编号，不删旧）
4. `spec` 落点与外部工具（默认单份 `SPEC.md`，兼容 `docs/SPEC.md`；多模块 `spec/capability-map.md` + `spec/SPEC-<id>.md`；外部工具或本地单源，不双写）
5. `task` 落点与外部 tracker（默认 `tasks/plan.md` + `tasks/todo.md`；或选用 beads / Linear / GitHub Issues 之一作唯一来源，并写入项目内 `docs/agents/issue-tracker.md`）
6. 五个子智能体默认模型（`code-reviewer`、`security-auditor` 用 `opus`；`doubt-challenger`、`test-engineer`、`web-performance-auditor` 用 `sonnet`）
7. 模型覆盖层级（推荐在规则文件中约定由调用方显式传 `model`，避免复制文件冻结提示词）

### 3. 子智能体与编排边界

- **五个内置子智能体**：4 个上游派生专业视角（`code-reviewer`、`security-auditor`、`test-engineer`、`web-performance-auditor`）+ 1 个 NK 新增（`doubt-challenger`，对抗式证伪者，工具限只读）。
- **对抗式证伪（`doubt-challenger`）**：在 `CONTRACT` 下挑战 `ARTIFACT`，**只输出问题**（含位置、原文证据、失败理由、`blocking / non-blocking` 严重度），不输出“整体不错”等验证式总结；彻底核查无误时明确回答未发现问题，不凑数。
- **单层编排治理规则**（`references/orchestration-patterns.md`）：**用户或 slash command 是 orchestrator，persona 不调用其他 persona**；需要多方互相反驳定因时用 Agent Teams，常规并行业务审计用 `/nk-ship` 的同回合并行 fan-out。

### 4. Issue Graph 建图规则（`references/issue-graph.md`）

选用外部 issue tracker 时通用以下结构概念（本仓库自身使用 `beads` / `bd`）：

| 概念 | 含义与规则 |
|---|---|
| **工作单元（unit）** | 顶层单元（如 `v0.1.0 Phase 1 <name>`），**不设 root epic**，只允许一层 `parent-child` |
| **`parent-child` 边** | 表达组成关系：子 → 父 |
| **`blocks` 边** | 表达调度先后：被阻塞者 → 阻塞者（唯一影响 `ready` 的边）；禁跨单元直连 task、禁加冗余传递边 |
| **`provenance` 边** | 表达来源追溯：新票 → 来源票（beads 中用 `-t discovered-from`）；修 finding 的执行票不挂父，仅连 provenance |
| **`checkpoint`** | 单元末尾的真实验证闸门（e2e、预算测量、契约核对、一轮审查）；**只允许入边，不许出边**，不可提前强关 |
| **收口（milestone）** | 版本级里程碑收口节点，被各 phase 阻塞 |
| **不删票原则** | 历史记录不可删除，纠正采用 `supersede` 或 `reparent` |

---

## 五、已退役的 v0.3.x 概念（仅作历史索引）

以下术语见于旧版 `CONCEPTS.md` / `context.md` 与 `archive/v0.3.x-nk-skills` 分支、早期 ADR/发布说明中，自 v0.4.0 起**已随旧技能归档而退役，不再用于现行技能与文档**：

- **分支收尾 / 发布日扫尾**（原 `nk-spec-close` / `nk-pr`）：拆解与验收职能现由 `code-review-and-quality`、`shipping-and-launch` 与 `/nk-ship` 承接。
- **ticket 认领 / 容器中立认领**（原 `nk-implement` / Linear 旧工作流）：见 [ADR-0003](adr/0003-beads-tracker.md)，现行体系改用 plan 规则或外部 tracker 原生状态。
- **前沿轮次（frontier） / 设计树（design tree） / 未成形的问题（fog of war）**（原 `nk-grill` / `nk-wayfinder`）：由 `interview-me` 与 `spec-driven-development` 替代。
- **纵向切片 / 曳光弹（tracer bullet）**（原 `nk-to-tickets`）：现行体系统一译作 **垂直切片（vertical slice）**。
- **子代理（sub-agent） / 人格（persona）**：现行正文统一保留 **subagent / 子智能体** 与 **persona**，不再使用「子代理」「人格」。
- **降级路径**（旧 STE-16 前单分支兜底）：随开发工作流变更与新版技能替换而下线。
