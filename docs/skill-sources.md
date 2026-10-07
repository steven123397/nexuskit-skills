# 技能来源映射

维护者向索引：只记录 NexusKit（NK）具体部分对应的上游材料。来源表示方法借鉴或改写，不表示整份技能照搬；NK 自有流程标为原创。执行技能的 Agent 不需要读本文件。

上游定位简称（下文路径相对对应仓库根目录）：

- **CE**：`D:/codex_project/upstreams/compound-engineering-plugin/`。
- **Matt**：`D:/codex_project/upstreams/matt-pocock-skills/`。
- **Matt-zh**：`D:/codex_project/upstreams/mattpocock-skills-zh-CN/`，社区中文直译版，仅作句子级译法参考，不作来源依据。
- **Ponytail**：`D:/codex_project/upstreams/ponytail/`。

以上目录为维护者的本地只读克隆，未随 NK 分发；路径用于定位现有材料，不将当前上游 HEAD 当作当初采用的版本。归属和许可证见 [NOTICE](../NOTICE)。下文 NK 的 `references/`、`SKILL.md` 相对该节技能目录。

旧稿来源对应暂保留在各节，待技能重写时更新；退役入口及共享层的历史映射可从 Git 查阅。

## nk-ask-ljq

- [入口](../skills/productivity/nk-ask-ljq/SKILL.legacy.md) 的场景推荐、主线与独立工具地图：Matt `skills/engineering/ask-matt/SKILL.md` 的 `The main flow: idea → ship`、`On-ramps`、`Standalone`。
- NK 技能路线、执行授权与外部 PR 指引、维护者个人留言：NK 原创。

## nk-commit

- [入口](../skills/engineering/nk-commit/SKILL.legacy.md) 的状态与风格检查、按逻辑变化提交、具名路径暂存、提交消息文件及提交后核对：CE `skills/ce-commit/SKILL.md` 的 `Context`、`Workflow`。
- R1–R6 提交节奏、current 归属、验证与审查证据、amend 条件：NK 原创。
- 中文提交文案的类型、动宾主题、动机与不兼容标记：原来源记录归于本地 `C:/Users/29617/.codex/skills/chinese-commit-conventions/SKILL.md`；该文件现已不存在，无法核对具体章节。

## nk-debug

- [入口](../skills/engineering/nk-debug/SKILL.legacy.md)、`references/investigate.md`、`fix.md`、`investigation-techniques.md`、`defense-in-depth.md`：CE `skills/ce-debug/SKILL.md` 的 `Execution Flow` 及 `references/` 下同名文件；就近合入的反模式源于 `references/anti-patterns.md`。
- `references/reproduction.md` 的反馈回路、收紧复现与最小化，以及调查中的可检验预测：Matt `skills/engineering/diagnosing-bugs/SKILL.md` 的 `Phase 1: Build a feedback loop`、`Phase 2: Reproduce + minimise`、`Phase 3: Hypothesise`、`Phase 4: Instrument`。
- 仅诊断出口、修复授权承接、nk-review/nk-commit 接口：NK 原创。

## nk-grill

- [入口](../skills/engineering/nk-grill/SKILL.md) 的设计树、前沿轮次、提问格式、推荐答案、Agent 事实查证与确认共同理解后再行动：Matt `skills/productivity/grilling/SKILL.md`（`6fd9479`）正文的中文迁移。
- 手动盘问入口：Matt `skills/productivity/grill-me/SKILL.md`（`6fd9479`）调用 `grilling`；NK 将入口与盘问正文合并，保留显式调用设置。
- 盘问时同时调用领域建模：Matt `skills/engineering/grill-with-docs/SKILL.md`（`6fd9479`）同时调用 `grilling` 和 `domain-modeling`；NK 合并到同一入口，在讨论项目领域设计时调用 `nk-domain-modeling`。领域建模方法由独立技能持有。
- 模块用途、实际用法与预期行为的澄清要求，以及无子代理时自行查证：NK 补充。

## nk-implement

- [入口](../skills/engineering/nk-implement/SKILL.md) 的按 spec/tickets 实施、定期类型检查与单测、收尾全量测试、完成后审查、提交到当前分支：Matt `skills/engineering/implement/SKILL.md`（`6fd9479`）正文主干的中文迁移。
- Matt 的 `tdd` 调用改为调用 `nk-tdd`（按项目测试规范改写的纪律参考）；验证节奏（类型检查与单测随改随跑、全量一次）保留在 implement 正文。
- Linear ticket 生命周期（认领设进行中、验收后完成、推进解锁票）、调用 nk-review 三轴审查与发现处理短链路、提交走 nk-commit、禁止主分支直接改动与不默认开工作树、受阻出口与范围外发现交用户、非代码交付的验证替代：NK 适配。
- 实施标准四条（完整实现不预支、抽象与状态、契约与真实失败、可读性无指标）、根因层修复、交付前 diff 自检与收束：STE-6/STE-8 调研确定的代码规范七条原则落地，NK 原创。
- 旧 nk-work 的条件分支 references（intake、tdd-loop、ui-work、non-code、out-of-repo-state、subagents）不迁移：必要能力并入正文，Plan/U-ID/current/nk-compound 等旧机制随骨架退役，可从 Git 历史查阅。

## nk-init

- [入口](../skills/engineering/nk-init/SKILL.legacy.md) 的探测、呈现确认、幂等写入骨架与已知答案不再询问：Matt `skills/engineering/setup-matt-pocock-skills/SKILL.md` 的 `Process` 下 `Explore`、`Present findings and ask`、`Confirm and edit`。
- 项目知识入口、`docs/current.md`、本地 backlog 与 nk-commit 接口：NK 原创。

## nk-odyssey

- [入口](../skills/engineering/nk-odyssey/SKILL.md) 的任务图与前沿、上下文指针稀疏通信、实施子代理后台并行、流程主干（读图、可选探索子代理与仓库外记录、集成分支与 draft PR、子代理独立工作树并确认基点、合并子代理合入、前沿推进、验收、PR ready 或按 tracker 关票、清理工作树）：Matt `skills/engineering/implement-spec/SKILL.md`（`6fd9479`）正文的中文迁移。
- 实施子代理按 nk-implement 纪律（含 nk-tdd、单票适用审查、nk-commit 提交）而非仅调用 tdd；整体验收交给 nk-spec-close（STE-17），不内置第二套验收方法，收尾审查由 spec-close 调用 nk-review；独立研究走 nk-research；解锁票推进 Todo；交付与 PR 收尾接 nk-pr：NK 适配。
- 原名 implement-spec，更名 odyssey：NK 决定。

## nk-prototype

- [入口](../skills/engineering/nk-prototype/SKILL.md) 的一次性定位、"问题决定形态"两分支（方案并排比较、可操作状态演示）、一条命令能跑、默认无持久化、不打磨、状态可见、结论与验证片段承接、原型留分支：Matt `skills/engineering/prototype/SKILL.md` 及 `LOGIC.md`、`UI.md`（`6fd9479`）的中文改写；不沿用固定单文件 HTML、tab 引导走查、悬浮切换器与 `?variant=` 模式，形态按问题就近选择。
- 工作树隔离与清理（默认同级 `<项目名>-worktrees/<用途>`、宿主管理优先、成果承接后清理、保留有引用价值的分支、不设台账）：STE-16 已定工作树规则的技能侧落地，NK 原创。
- 非代码载体（大纲、草图）、适用限制、先查事实再动手（调用 nk-research）、ticket 关联：NK 适配，对齐 wayfinder 的 Prototype 票型与 to-spec 的原型片段例外。

## nk-research

- 重写而非迁移：Matt `skills/engineering/research/SKILL.md`（`6fd9479`）仅取"一手来源优先、关键结论追到来源"的原则；其后台代理委派与把发现写成仓库 Markdown 的流程不采用（STE-16 明确必须重写）。
- [入口](../skills/engineering/nk-research/SKILL.md) 的先定问题（可回答的问题、支撑哪个决定、什么算答完）、本地优先、先广后窄、冲突不折中、事实/推断/未解区分、尽早停、结论与去向（对话、ticket 评论、OpenViking）、只读不开工作树：NK 原创，补齐 Matt 版缺失的问题范围、证据冲突、结论表达与停止时机。
- 来源阅读原则（独立来源一致才算信号、时效与权威分开、网页按不可信输入处理）：就近承接旧 conventions 的 `research-digest.md` 与 `agents/web-researcher.md` 方法，按 STE-16 归入本技能；固定栏目摘要、token 预算与各专用 researcher 角色不迁移。

## nk-review

- [入口](../skills/engineering/nk-review/SKILL.legacy.md)、`references/scope.md`、`select-and-route.md`、`reviewer-prompt.md`、`validate.md` 的意图、范围、风险编队、叶子审查与独立复核：CE `skills/ce-code-review/references/intent-and-plan.md`、`scope.md`、`diff-scope.md`、`select-and-route.md`、`dispatch-reviewers.md`、`subagent-template.md`、`validator-batch-template.md`、`finish-review.md`。
- `references/personas/` 的风险角色：CE `skills/ce-code-review/references/personas/` 下同名文件；共享经验、迁移、部署角色见 conventions。
- maintainability 的“可删除内容、替代能力及等价依据”：Ponytail `skills/ponytail-review/SKILL.md` 的 `Format` 分类；NK 增加证据与行为保持条件。
- `references/pre-merge.md`、`entry-format.md`，外部 PR 的 base/head、修订复核、合并前确认与报告生命周期：NK 原创；常规流程显式调用 nk-simplify。

## nk-tdd

- [入口](../skills/engineering/nk-tdd/SKILL.md) 的好测试标准、只在确认的测试接口上测、反模式（实现耦合、同义反复、横向切片与纵向切片替代）、先见失败再实现、一次一个切片、重构归审查：Matt `skills/engineering/tdd/SKILL.md`（`6fd9479`）正文的中文迁移，按项目测试规范改写。
- 数量纪律（新增须带来新验证价值、复用优先、不为形式新增、不多层重复断言、不堆假想场景）：项目已定测试编写规范；mock 系统边界规则浓缩自 Matt `skills/engineering/tdd/mocking.md` 的一句，tests.md 不整份迁移；不设 codebase-design 词汇联动（NK 无对应技能）。
- 定位为 model-invoked 纪律参考：nk-implement、nk-odyssey 实施时调用，nk-review 重写时引用。

## nk-to-spec

- [入口](../skills/engineering/nk-to-spec/SKILL.md) 的对话综合、不重新访谈、仓库与领域术语核对、测试接口选择及确认、spec 模板结构、实现决定与原型片段例外：Matt `skills/engineering/to-spec/SKILL.md`（`6fd9479`）的 `Process` 与 `<spec-template>`，按原文结构迁移为中文。
- “使用场景与预期行为”替换长篇 User Stories：NK 已确认的模板调整；问题价值、重要行为与边界、不在范围内容及可选补充说明按该决定表达。
- 固定使用 Linear、缺少配置时询问、沿用项目标签与状态、更新已有 spec，以及不重复确认已有测试决定：NK 适配；不沿用 Matt 的固定 `ready-for-agent` 标签与 setup 入口。

## nk-to-issue

- [入口](../skills/engineering/nk-to-issue/SKILL.legacy.md) 的事实核实、已有实现与历史否决检查、已知与缺口表达：Matt `skills/engineering/triage/SKILL.md` 的 `Triage a specific issue or PR` 第 1、3 步、`Needs-info template`、`Resuming a previous session`。
- 授权后在当前任务建票/更新、本地 backlog、失败去重与调用方接口：NK 原创；条目契约见 conventions。

## nk-to-tickets

- [入口](../skills/engineering/nk-to-tickets/SKILL.md) 的收集上下文、可选代码库探索与预重构、纵向切片规则、宽范围重构的扩展–收缩排序、与用户确认拆分、按依赖顺序创建并连原生阻塞、子 issue、前沿开工、避免路径与代码片段及原型例外：Matt `skills/engineering/to-tickets/SKILL.md`（`6fd9479`）的 `Process` 与模板，按原文结构迁移为中文。
- 固定使用 Linear、沿用项目标签与状态（不沿用 ready-for-agent）、依赖与状态走原生字段不在正文重复、去掉本地文件 tracker 路径：NK 适配。ticket 模板按 STE-5 定稿：所属 spec、交付什么、验收条件；依赖走原生阻塞关系，正文不设该节。创建即按就绪度设状态：无阻塞的进 Todo，被阻塞的留在 Backlog，解锁后由实施会话推进。
- 承接 wayfinder 的 map 作为输入引用：NK 适配。

## nk-wait-what

- [入口](../skills/productivity/nk-wait-what/SKILL.legacy.md) 的重新解释、补上下文、简单语言与项目术语：Matt `skills/productivity/wait-what/SKILL.md` 正文。
- 中文表达适配、`CONCEPTS.md`、不清楚处与待对齐项的汇报：NK 原创适配。

## nk-wayfinder

- [入口](../skills/engineering/nk-wayfinder/SKILL.md) 的规划定位、名称引用、索引与子 tickets、四种票型、依赖、未成形问题与范围区分、两种使用方式：Matt `skills/engineering/wayfinder/SKILL.md`（`6fd9479`）的 `Plan, don't do`、`Refer by name`、`The Map`、`Ticket Types`、`Fog of war`、`Out of scope`、`Invocation`。沿用结构，Map 保留英文 map（`wayfinder:map` 索引 issue，与 spec、ticket 同类），Destination、Frontier 译为目的地、前沿（前沿与 nk-grill 一致）；Fog of war 不直译比喻，表述为未成形的问题，对应章节 Not yet specified 译作“未成形”。通用术语译法见 [context.md](../context.md)。
- Linear 原生状态与依赖、认领时区分同账号会话、取消依赖后核对影响、通过 nk-grill 承接领域建模、模块实际用法澄清、接入 nk-to-spec / nk-to-tickets：NK 适配。
- 独立问题可并行研究或同轮讨论，取消上游每会话只解决一张非研究票的限制；研究结果记录到 Linear，不固定开研究分支；探索以决策为产出，不保留上游 Notes 扩展为正式实施的选项：NK 已定职责调整。

## nk-wizard

- [入口](../skills/productivity/nk-wizard/SKILL.legacy.md) 的分阶段人工向导与 [Bash 模板](../skills/productivity/nk-wizard/assets/template.sh)：Matt `skills/engineering/wizard/SKILL.md` 与同目录 `template.sh`。
- Git Bash 说明、跳过项不算全部完成、目的地与凭据边界、静态验证及提交接口：NK 原创适配。
