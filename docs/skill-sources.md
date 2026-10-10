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

- [入口](../skills/productivity/nk-ask-ljq/SKILL.md) 的路由地图骨架（主线 idea → 交付 + 其他入口 + 独立工具表 + 词汇层 + 首次使用前置 init）、"先回答眼前的问题"（一个首选入口、理由、材料与预期结果；分叉才解释；推荐不等于调用、问路不产生授权）、主线各步的衔接语义：Matt `skills/engineering/ask-matt/SKILL.md`（`6fd9479`）的 `The main flow: idea → ship`、`On-ramps`、`Standalone` 结构中文重写。
- 地图内容按 NK 最终 23 技能边界重画：主线为 grill → prototype/research → to-spec/to-tickets → implement/odyssey → spec-close/pr → retro；grill-with-docs/grill-me 合并为 nk-grill、ICA 与 teach、to-questionnaire 不收（已定决定）；词汇层为 nk-codecraft/nk-tdd/nk-domain-modeling；上下文来源改为信息归属原则（Linear/Git-PR/OpenViking/CONCEPTS+ADR），不迁移 Matt 的 smart zone 与 phase boundaries 理论。
- 工具箱不是流水线、小改动不必先写 spec、问路不自动启动流程：沿旧稿定位。
- 旧稿的 nk-ideate/brainstorm/plan/work/close/simplify/handoff/compound 路由、current.md 与 solutions 接续、外部 PR 维护者流程及"给一位朋友的小彩蛋"（2026-10-08 经用户决定移除）不迁移。

## nk-codecraft

- [入口](../skills/engineering/nk-codecraft/SKILL.md) 的受控词汇（模块、接口、实现、适配器、深度、接缝、杠杆、局部性与反词表）、删除测试、一适配器等于假想接缝、接口即测试面：Matt `skills/engineering/codebase-design/SKILL.md`（`6fd9479`）正文的中文迁移与压缩。
- 七条纪律（完整实现不预支、先理解已有代码、抽象减负、契约与真实失败、可读性、行为验证、收束）：STE-6/STE-8 调研的代码规范七条；按用户决定与架构词汇融合为单一参考，不分开成两个技能。
- 不迁移 DEEPENING.md 与 DESIGN-IT-TWICE.md（design-it-twice 属 improve-codebase-architecture 场景，该技能经用户决定不收，to-questionnaire 亦不收）；可测试性三则中与测试重叠的部分归 nk-tdd。定位为 model-invoked 纪律参考：nk-implement 实施时调用、nk-review 审查时对照、接口形状讨论时查阅。

## nk-commit

- [入口](../skills/engineering/nk-commit/SKILL.md) 的范围与风格核对、按逻辑变化提交、具名路径暂存、提交消息文件、路径限定提交、命令逐条执行与提交后核对：CE `skills/ce-commit/SKILL.md` 的 `Context`、`Workflow`。
- 提交单位（一个经过验证的变化）、未确认未共享不改写历史、必要证据核对、中文 Conventional Commits 说明格式、主分支停止并报告：NK 原创；current、U-ID、R1–R6 提交节奏与 handoff/收尾耦合随 STE-22 退役。
- 中文提交文案的类型、动宾主题、动机与不兼容标记：原来源记录归于本地 `C:/Users/29617/.codex/skills/chinese-commit-conventions/SKILL.md`；该文件现已不存在，无法核对具体章节。

## nk-domain-modeling

- [入口](../skills/engineering/nk-domain-modeling/SKILL.md) 的主动建模定位（改变模型才用、读词汇不归本技能）、惰性创建、讨论四动作（对照术语表质疑、锤炼模糊语言、具体场景压边界、与代码互证）、敲定即写不攒批、有主见的选词与 Avoid、只收领域专属概念、ADR 三条件（难以逆转、没上下文会惊讶、真实取舍）、短段落格式及与词条格式呈现一致的可照抄模板块：Matt `skills/engineering/domain-modeling/SKILL.md` 及 `GLOSSARY-FORMAT.md`、`ADR-FORMAT.md`（`6fd9479`）正文的中文迁移与压缩；例句按原文方式译写。
- 多上下文机制（根 `CONCEPTS-MAP.md` 列各域职责与域词汇表路径、域间关系按事件流与共享契约记录、域内 `CONCEPTS.md` 与域内 ADR、结构推断与“不清楚时问”、map 惰性创建）：Matt `GLOSSARY-FORMAT.md` 的 Single vs multi-context repos 节中文迁移（2026-10-08 经用户决定补上，因存在真实的多域项目），文件名按 NK 实践用 CONCEPTS 前缀。
- 文件名按 NK 实践改为 `CONCEPTS.md`；ADR 沿 Matt 原式（2026-10-08 经用户决定）：目录 `docs/adr/`、文件名 `0000-{短名}.md`、新建取最大编号 +1、被替代时标注后继编号，存量两份决定按初版时间追编 0001、0002；不沿用 GLOSSARY.md 与 GLOSSARY-MAP 多上下文机制。“什么是合格 ADR 对象”的清单压缩自 Matt 的 What qualifies。
- 词条可选的行为规则次段、五条维护规则（新增、完善、合并、净化、退役）、退役需正面业务证据（代码删除不算理由）、存量项目初建路径（读 schema、核心类型、主模型与顶层领域文档，不漫游不凑数）、术语表更新随对应交付提交：承接旧集中约定的 `concepts-vocabulary.md` 必要内容，按 STE-16 归入本技能；compound 增量捕获、close 收尾提炼等绑定旧流程的触发点不迁移。

## nk-debug

- [入口](../skills/engineering/nk-debug/SKILL.md) 的调查主线（分诊输入含 Issue 正文与评论、建立可重复观测、环境与在途改动核对、沿真实调用链回溯根因、可证伪假设与单变量探针、卡点自诊）与修复主线（测试归属五分流、先见失败再修复、原始场景回归、探针清理与交付证据）：CE `skills/ce-debug/SKILL.md` 的 `Execution Flow` 及 `references/investigate.md`、`fix.md` 压缩迁移；`references/investigate.md` 就近合入的反模式源于 CE `references/anti-patterns.md`。
- 复现回路优先（先建对准本缺陷的通过/失败信号再谈理论、手段选择清单、收紧回路三问、偶发缺陷提高复现率、性能先建数值基线、无法复现如实说）：Matt `skills/engineering/diagnosing-bugs/SKILL.md`（`6fd9479`）Phase 1 的精神与清单中文压缩；旧 `references/reproduction.md` 的回路手段表与最小化并入正文。
- 证实根因写进提交说明：Matt Phase 6 的 Cleanup 要求。
- [调查技术](../skills/engineering/nk-debug/references/investigation-techniques.md)、[分层防御](../skills/engineering/nk-debug/references/defense-in-depth.md) 保留为按需 references，源自 CE 同名文件，措辞未改；`investigate.md`、`fix.md`、`reproduction.md` 的内容并入 SKILL.md 后删除。
- 仅诊断出口与四种授权分流、修复推翻有意设计时的分歧出口、调用新版 nk-review（发现处理短链路）与 nk-commit（轻量提交）、回归测试纪律对照 nk-tdd、证据脱敏、范围外发现经 nk-to-issue 记录：NK 原创；旧稿的 current、nk-compound 沉淀、artifact-lifecycle/subagent-results 约定引用随 STE-24 退役，历史调查经验改检索 OpenViking。

## nk-grill

- [入口](../skills/engineering/nk-grill/SKILL.md) 的设计树、前沿轮次、提问格式、推荐答案、Agent 事实查证与确认共同理解后再行动：Matt `skills/productivity/grilling/SKILL.md`（`6fd9479`）正文的中文迁移。
- 手动盘问入口：Matt `skills/productivity/grill-me/SKILL.md`（`6fd9479`）调用 `grilling`；NK 将入口与盘问正文合并，保留显式调用设置。
- 盘问时同时调用领域建模：Matt `skills/engineering/grill-with-docs/SKILL.md`（`6fd9479`）同时调用 `grilling` 和 `domain-modeling`；NK 合并到同一入口，在讨论项目领域设计时调用 `nk-domain-modeling`。领域建模方法由独立技能持有。
- 模块用途、实际用法与预期行为的澄清要求，以及无子代理时自行查证：NK 补充。

## nk-implement

- [入口](../skills/engineering/nk-implement/SKILL.md) 的按 spec/tickets 实施、定期类型检查与单测、收尾全量测试、完成后审查、提交到当前分支：Matt `skills/engineering/implement/SKILL.md`（`6fd9479`）正文主干的中文迁移。
- Matt 的 `tdd` 调用改为调用 `nk-tdd`（按项目测试规范改写的纪律参考）；验证节奏（类型检查与单测随改随跑、全量一次）保留在 implement 正文。
- Linear ticket 生命周期（认领设进行中、验收后完成、推进解锁票）、调用 nk-review 三轴审查与发现处理短链路、提交走 nk-commit、禁止主分支直接改动与不默认开工作树、受阻出口与范围外发现交用户、非代码交付的验证替代：NK 适配。
- 实施标准与根因层修复出自 STE-6/STE-8 代码规范七条，已与 Matt codebase-design 架构词汇融合为 nk-codecraft（STE-32），implement 调用该技能；交付前 diff 自检与收束保留在本技能流程。
- 旧 nk-work 的条件分支 references（intake、tdd-loop、ui-work、non-code、out-of-repo-state、subagents）不迁移：必要能力并入正文，Plan/U-ID/current/nk-compound 等旧机制随骨架退役，可从 Git 历史查阅。

## nk-init

- [入口](../skills/engineering/nk-init/SKILL.md) 的探测（读 git remote 与指令文件现状，不凭空发问）、展示并确认（逐项带推荐答案，探测已定的直接说明不提问）、选文件规则（`CLAUDE.md` 存在则编辑它、否则 `AGENTS.md`、都不存在问用户不代选；已有配置块就地更新不追加重复，不覆盖周边编辑）、幂等与重跑语义（只在更换去向时需要）：Matt `skills/engineering/setup-matt-pocock-skills/SKILL.md`（`6fd9479`）`Process` 下 `Explore`、`Present findings and ask`、`Confirm and edit`、`Write` 的中文迁移。
- 配置对象按 NK 边界重定：Linear 团队与项目（to-spec/to-tickets/odyssey/spec-close 读取）、GitHub 外部问题去向（to-issue，无远端降级 docs/backlog.md）、导航指针指向 CONCEPTS.md 与 docs/adr/；不迁移 Matt 的 triage 标签体系（nk-to-issue 用 bug/enhancement）、issue-tracker 选项表与 GLOSSARY-MAP 多上下文（domain-modeling 已定单文件默认）。
- 惰性创建（CONCEPTS.md 由第一个词条建、docs/adr/ 由第一个决定建、不预建空目录与 backlog）、初始化产物经 nk-commit 入库、收尾告知哪些技能读哪些配置：NK 适配。按用户决定，配置文件固定为 `docs/agents/issue-tracker.md`，消费者 nk-to-spec / nk-to-tickets / nk-odyssey / nk-wayfinder 固定读取，nk-to-issue 的无远端降级位置同源。
- 旧稿的 docs/current.md 创建、current-md/artifact-lifecycle/concepts-vocabulary 约定引用与"知识入口"体系随 STE-28 退役；Matt 的 triage 标签体系（to-issue 用 bug/enhancement，分诊队列随"外部 Issue 只记录"定位取消）与 issue-tracker 选项表（Linear+GitHub 已选型）不迁移；多域信号探测（workspace 清单、packages/*、多个域目录）与多上下文导航指针随 GLOSSARY-MAP 机制补回（2026-10-08），布局归 nk-domain-modeling 持有，init 只探测与指路；docs/agents/domain.md 不另建（消费规则由 nk-domain-modeling 持有，避免双源）。
- Orca 探测与接入（CLI 与 `orca-cli` 外挂技能探测、是否使用的询问、`.gitignore` 追加 `/.orca/`、指令文件简短声明）：NK 原创，依据 STE-33 的 Orca 调研（2026-10-09）；`orca-cli` 为唯一刚需外挂技能，不随本体系分发。

## nk-odyssey

- [入口](../skills/engineering/nk-odyssey/SKILL.md) 的任务图与前沿、上下文指针稀疏通信、实施子代理后台并行、流程主干（读图、可选探索子代理与仓库外记录、集成分支与 draft PR、子代理独立工作树并确认基点、合并子代理合入、前沿推进、验收、PR ready 或按 tracker 关票、清理工作树）：Matt `skills/engineering/implement-spec/SKILL.md`（`6fd9479`）正文的中文迁移。
- 实施子代理按 nk-implement 纪律（含 nk-tdd、单票适用审查、nk-commit 提交）而非仅调用 tdd；整体验收交给 nk-spec-close（STE-17），不内置第二套验收方法，收尾审查由 spec-close 调用 nk-review；独立研究走 nk-research；解锁票推进 Todo；交付与 PR 收尾接 nk-pr：NK 适配。
- 原名 implement-spec，更名 odyssey：NK 决定。
- 执行底座分流（开工前确认 Orca 声明与可用性、走 Orca 时工作树与实施/合并子代理创建改用 Orca 方式、探索与审查子代理仍走原生、两路径下票状态流转与验收不变）：NK 原创，依据 STE-33 的 Orca 调研（2026-10-09）。

## nk-orca-guide

- [入口](../skills/engineering/nk-orca-guide/SKILL.md) 全部内容为 NK 原创，依据两类材料：2026-10-09 本机实测（codex / kimi / opencode 三 agent 的派发、交互、读屏、完工确认与清理）；Orca 官方技能指南（stablyai/orca 仓库的 `skill-guides/orca-cli.md`、`skill-guides/orchestration/` 与 `skill-stubs/`，只取命令语义与差异事实，不迁移其协调协议）。
- Orca 技能总表与"orchestration 不采用、多票调度归 nk-odyssey"的划分：STE-33 调研结论。

## nk-pr

- [入口](../skills/engineering/nk-pr/SKILL.md) 的 PR 描述最小视图（伪代码、调用树、文件树或 diff 按话题选形）、验证证据前后对比、单向门（one-way door）与波及面：Matt `skills/engineering/pr/SKILL.md`（`6fd9479`，其源头为 Humanlayer show-me）的模板精华压缩；Matt 版是纯 PR body 写作模板，NK 将其并入分支交付全流程技能。
- 描述写 diff 看不出来的东西、长度随决策成本伸缩（含三类画像写法）、残余不确定性如实写、项目 PR 模板与约定优先、关联 Issue 的关闭语义纪律（Fixes/Closes 与 Related 区分、不确定按不关闭处理）：旧 nk-close `references/pr-description.md` 的核心原则迁移；关闭语义与 Linear/GitHub 的分工对齐（spec 走 nk-spec-close、tickets 走各自实施，不因合并批量关闭）。
- 分支交付全流程（draft PR 在第一份实际交付提交后创建、审查与验收结论复用、转 ready 与合并条件、满足检查不推导合并许可、授权合并、不强制等合并清理工作树、保留未交付内容）：STE-10/STE-14 设计，NK 原创；审查覆盖整个分支实际交付（含补充工作）对齐 nk-review 的 PR 范围重点与复用规则，spec 验收复用 nk-spec-close 结论。
- 旧 nk-close 的 pre-merge 专线路径、release-day 发布流程、产物矩阵与收尾提交不迁移：发布单独处理（未建技能）、审查归 nk-review、验收归 nk-spec-close、经验归 OpenViking。

## nk-prototype

- [入口](../skills/engineering/nk-prototype/SKILL.md) 的一次性定位、"问题决定形态"两分支（方案并排比较、可操作状态演示）、一条命令能跑、默认无持久化、不打磨、状态可见、结论与验证片段承接、原型留分支：Matt `skills/engineering/prototype/SKILL.md` 及 `LOGIC.md`、`UI.md`（`6fd9479`）的中文改写；不沿用固定单文件 HTML、tab 引导走查、悬浮切换器与 `?variant=` 模式，形态按问题就近选择。
- 工作树隔离与清理（默认同级 `<项目名>-worktrees/<用途>`、宿主管理优先、成果承接后清理、保留有引用价值的分支、不设台账）：STE-16 已定工作树规则的技能侧落地，NK 原创。
- 非代码载体（大纲、草图）、适用限制、先查事实再动手（调用 nk-research）、ticket 关联：NK 适配，对齐 wayfinder 的 Prototype 票型与 to-spec 的原型片段例外。

## nk-research

- 重写而非迁移：Matt `skills/engineering/research/SKILL.md`（`6fd9479`）仅取"一手来源优先、关键结论追到来源"的原则；其后台代理委派与把发现写成仓库 Markdown 的流程不采用（STE-16 明确必须重写）。
- [入口](../skills/engineering/nk-research/SKILL.md) 的先定问题（可回答的问题、支撑哪个决定、什么算答完）、本地优先、先广后窄、冲突不折中、事实/推断/未解区分、尽早停、结论与去向（对话、ticket 评论、OpenViking）、只读不开工作树：NK 原创，补齐 Matt 版缺失的问题范围、证据冲突、结论表达与停止时机。
- 来源阅读原则（独立来源一致才算信号、时效与权威分开、网页按不可信输入处理）：就近承接旧 conventions 的 `research-digest.md` 与 `agents/web-researcher.md` 方法，按 STE-16 归入本技能；固定栏目摘要、token 预算与各专用 researcher 角色不迁移。

## nk-review

- [入口](../skills/engineering/nk-review/SKILL.md) 的轴间独立（一轴通过不抵消另一轴）、并行独立子代理、固定点求基线与按轴组织返回：Matt `skills/engineering/code-review/SKILL.md`（`6fd9479`）的双轴骨架按 STE-6 重新划分——Standards/Spec 两轴改为需求符合性、实现正确性、简洁性与可维护性三轴，职责重新分配，不是对旧轴的机械拆分；Matt 的 smell 基线清单不迁移，简洁性与测试判断由 `nk-codecraft`、`nk-tdd` 承载，reviewer 提示词只点名对照。
- 分级复用（SHA 变化不等于结论失效、只补查受影响部分、进入下一阶段不自动重派三人）、按 ticket / spec 整合 / PR / 机械变更区分审查重点、自然语言返回与零发现简短说明、不设 validator 与递归编队、修复归调用方并由原审查者针对性复核、有效防御不因精简误删：STE-6 设计；GitHub #42 反映的旧编队成本（小改动 9 个子代理）与零发现 JSON 空字段契约由此处理，nk-simplify 串联随之取消。
- 快照一致性（实际内容或指纹、分析期间不改被审内容）、未跟踪文件的纳入与排除、意图摘要与已有验证证据随任务给出、外部 PR 只读取数不 checkout：旧稿必要能力保留；CE 的风险编队（select-and-route、personas）、validator 复核、JSON 返回契约、`docs/reviews/` 审查台账与 pre-merge 独立路径随 STE-6/STE-12 退役，PR 场景并入“按范围定重点”。
- 简洁性发现的真实收益与行为等价依据：Ponytail `skills/ponytail-review/SKILL.md` 的 `Format` 分类沿旧稿承接，限定于删减建议。
- reviewer 只读不占工作树、始终由主会话原生派发不走 Orca：NK 原创，依据 STE-33 调研（Orca 派发仅用于落工作树的实施类工作）。

## nk-spec-close

- [入口](../skills/engineering/nk-spec-close/SKILL.md) 为 NK 原创，无上游对应技能：整体验收（沿 spec 的使用场景走完整用户流程、跨 ticket 衔接、遗漏与误解）、验收对象与测试决定取自 nk-to-spec 的 spec 模板、证据复用与受影响补查、验收通过即关闭 Linear spec 不等 PR 合并、不实施修复缺口交实施方（区分已满足/未满足/未验证）、验收结论随交付载体不建台账：STE-10/STE-16/STE-17 设计。
- 整合范围的审查派发对齐 nk-review 的"spec 整合与整体交付"重点（跨 ticket 组合、累计影响、完整用户流程）与其复用规则；调用方约定（用户直接调用、nk-odyssey 整合完成后调用、PR 收尾按需补充）来自 STE-16 职责划分。
- 临时工作树清理（git worktree list 查现状、成果已承接且无活跃使用者、宿主优先、不删原目录与在用分支、不建台账）：STE-16 工作树规则的本技能侧落地；PR 剩余交付资源清理归 nk-pr。
- 旧 nk-close 的轻量合并前检查、遗留与知识沉淀（compound）、产物矩阵与收尾提交不迁移：PR 场景归 nk-pr 与 nk-review，经验归 OpenViking，产物生命周期约定已随骨架退役。

## nk-tdd

- [入口](../skills/engineering/nk-tdd/SKILL.md) 的好测试标准、只在确认的测试接口上测、反模式（实现耦合、同义反复、横向切片与纵向切片替代）、先见失败再实现、一次一个切片、重构归审查：Matt `skills/engineering/tdd/SKILL.md`（`6fd9479`）正文的中文迁移，按项目测试规范改写。
- 测试接口确认时说明各接口能发现与无法覆盖的问题：Matt `skills/engineering/tdd/SKILL.md`（`3f59913`）的接口取舍说明，融入“测试写在哪”。
- 数量纪律（新增须带来新验证价值、复用优先、不为形式新增、不多层重复断言、不堆假想场景）：项目已定测试编写规范；mock 系统边界规则浓缩自 Matt `skills/engineering/tdd/mocking.md` 的一句，tests.md 不整份迁移；不设 codebase-design 词汇联动（NK 无对应技能）。
- 定位为 model-invoked 纪律参考：nk-implement、nk-odyssey 实施时调用，nk-review 重写时引用。

## nk-to-spec

- [入口](../skills/engineering/nk-to-spec/SKILL.md) 的对话综合、不重新访谈、仓库与领域术语核对、测试接口选择及确认、spec 模板结构、实现决定与原型片段例外：Matt `skills/engineering/to-spec/SKILL.md`（`6fd9479`）的 `Process` 与 `<spec-template>`，按原文结构迁移为中文。
- “使用场景与预期行为”替换长篇 User Stories：NK 已确认的模板调整；问题价值、重要行为与边界、不在范围内容及可选补充说明按该决定表达。
- 固定使用 Linear、缺少配置时询问、沿用项目标签与状态、更新已有 spec，以及不重复确认已有测试决定：NK 适配；不沿用 Matt 的固定 `ready-for-agent` 标签与 setup 入口。

## nk-to-issue

- [入口](../skills/engineering/nk-to-issue/SKILL.md) 的事实核实、已有实现与历史否决检查、已知与缺口的表达：Matt `skills/engineering/triage/SKILL.md` 的 `Triage a specific issue or PR` 第 1、3 步、`Needs-info template`、`Resuming a previous session`。
- 写作原则（持久性优于精确、行为而非步骤、可独立验证的完成定义、范围边界）与条目格式、`bug`/`enhancement` 标签约定：就近承接旧集中约定的 `issue-writing.md` GitHub 部分，按 STE-16 归入本技能；认领与关闭时机、wayfinder 标签例外随旧机制退役，不迁移。
- 授权语义与写入目标核对、建票/更新分流、无远端降级与失败处理、纳入 Linear 时的最小关联边界：NK 原创。

## nk-to-tickets

- [入口](../skills/engineering/nk-to-tickets/SKILL.md) 的收集上下文、可选代码库探索与预重构、纵向切片规则、宽范围重构的扩展–收缩排序、与用户确认拆分、按依赖顺序创建并连原生阻塞、子 issue、前沿开工、避免路径与代码片段及原型例外：Matt `skills/engineering/to-tickets/SKILL.md`（`6fd9479`）的 `Process` 与模板，按原文结构迁移为中文。
- 固定使用 Linear、沿用项目标签与状态（不沿用 ready-for-agent）、依赖与状态走原生字段不在正文重复、去掉本地文件 tracker 路径：NK 适配。ticket 模板按 STE-5 定稿：所属 spec、交付什么、验收条件；依赖走原生阻塞关系，正文不设该节。创建即按就绪度设状态：无阻塞的进 Todo，被阻塞的留在 Backlog，解锁后由实施会话推进。
- 承接 wayfinder 的 map 作为输入引用：NK 适配。

## nk-wait-what

- [入口](../skills/productivity/nk-wait-what/SKILL.md) 的重新解释、补上下文、简单语言与项目术语：Matt `skills/productivity/wait-what/SKILL.md` 正文；其 `GLOSSARY.md`/`GLOSSARY-MAP.md` 术语来源映射为 NK 的 `CONCEPTS.md`。
- 中文表达适配、事实/推断/待决定的区分与待对齐项的汇报：NK 原创适配。

## nk-wayfinder

- [入口](../skills/engineering/nk-wayfinder/SKILL.md) 的规划定位、名称引用、索引与子 tickets、四种票型、依赖、未成形问题与范围区分、两种使用方式：Matt `skills/engineering/wayfinder/SKILL.md`（`6fd9479`）的 `Plan, don't do`、`Refer by name`、`The Map`、`Ticket Types`、`Fog of war`、`Out of scope`、`Invocation`。沿用结构，Map 保留英文 map（`wayfinder:map` 索引 issue，与 spec、ticket 同类），Destination、Frontier 译为目的地、前沿（前沿与 nk-grill 一致）；Fog of war 不直译比喻，表述为未成形的问题，对应章节 Not yet specified 译作“未成形”。通用术语译法见 [context.md](../context.md)。
- Linear 原生状态与依赖、认领时区分同账号会话、取消依赖后核对影响、通过 nk-grill 承接领域建模、模块实际用法澄清、接入 nk-to-spec / nk-to-tickets：NK 适配。
- 独立问题可并行研究或同轮讨论，取消上游每会话只解决一张非研究票的限制；研究结果记录到 Linear，不固定开研究分支；探索以决策为产出，不保留上游 Notes 扩展为正式实施的选项：NK 已定职责调整。

## nk-retro

- [入口](../skills/productivity/nk-retro/SKILL.md) 的环境复盘定位（改进 Agent 工作环境而非重审代码）、读会话原始材料且默认当前会话、改进候选方向（导航、自动检查、编码标准、指令文件、工具经济、信息可达）、按严重度交付候选：Matt `skills/engineering/retro/SKILL.md`（`6fd9479`）正文的中文迁移与压缩；其 Global AGENTS.md 与 No-ops 两类合并为"指令文件"一类，Files 参考节压缩为 AGENTS.md 克制导航指针一句。
- 机械违规交确定性检查、判断类才写文档规则、未接线的既有检查本身就是发现、无护栏仓库本身是发现：Matt 原文的规则迁移；CODING_STANDARDS.md 专指改为通用文档规则表述，审查侧承担标准（Implementation vs Review）压成一句指向 `nk-review`。
- 接受用户指定会话/问题/经验为复盘对象、总结直接对话交付、按请求写入或修订 OpenViking 可写位置并读回验证、区分建议与已执行修改、不宣称操控自动提炼、不恢复 compound/solutions 流程：STE-7/STE-23 决定，NK 原创。
- Matt 的 `writing-for-agents` 写作风格调用改为调用 `nk-prose`。

## nk-prose

- [入口](../skills/productivity/nk-prose/SKILL.md) 的事实保真约束、润色/起草/检查三种用法、幂等润色、读者分档、句子标准与不动代码块等边界：CE `skills/ce-noslop/SKILL.md` 正文的中文改写；英文模式清单（`references/patterns.md`）与术语参考（`references/terminology.md`）不迁入。
- 中文表达与排版（中英文与数字空格、全半角标点、术语保留与中英对照、欧化句式与机翻味规避）：本机 `C:/Users/29617/.codex/skills/chinese-documentation/SKILL.md` 要点收敛；API 文档与 README 长模板不迁入。
- 套话与机械 User Story 的处理方向、面向 Agent 指令文档的排除边界：NK 原创。Matt `skills/productivity/writing-for-agents/SKILL.md` 是指令写作参考，不是本技能来源。

## nk-wizard

- [入口](../skills/productivity/nk-wizard/SKILL.md) 的分阶段人工向导与 [Bash 模板](../skills/productivity/nk-wizard/assets/template.sh)：Matt `skills/engineering/wizard/SKILL.md` 与同目录 `template.sh`（`49dd158`）；模板采用其 Readline 输入、EOF 处理、文件权限与符号链接保留、浏览器提示、清屏回退及 `run_wizard` 包装，生成来源注释改为 nk-wizard，并保留 NK 的跳过项未完成提示。未采用上游引号编码与解码：Shell 拼接式单引号转义不兼容 dotenv 消费器，保留原始单行 KEY=VALUE 格式。
- Git Bash 说明、跳过项不算全部完成、目的地与凭据边界、静态验证及提交接口：NK 原创适配；旧稿的集中知识库调用改为按用户决定记入 OpenViking。
