# 技能来源与差异记录 (Skill Sources)

> 维护者向文档：每个技能改写自哪些上游、做了什么取舍、为什么。执行技能的 Agent 不需要读它；修改技能或考虑吸收上游更新时来这里查。由 `AGENTS.md` 指向本文件。
>
> 上游正式克隆（只读参考，不入本仓库）：`D:\codex_project\upstreams\compound-engineering-plugin` 与 `D:\codex_project\upstreams\matt-pocock-skills`。

---

2026-09-28 提交与现场归属调整：nk-commit 的 R1–R6 统一覆盖已验证交付、中途记录、遗漏补记、场景、提交前 current 更新和独立变化。常规提交携 current 一次完成，取消固定的提交后 handoff/amend 链；复用适用的审查与验证证据。同步 work、debug、plan、brainstorm、close、compound、init、simplify、wizard 的提交接口，以及 ideate、review、to-issue、wayfinder、ask-ljq 的暂留和结束说明。这些是跨技能接口迁移，不代表所有技能主体已重写完成。

nk-handoff 改为仅用户显式调用：保留 `disable-model-invocation: true`，新增 Codex 的 `agents/openai.yaml` 中 `policy.allow_implicit_invocation: false`；正文不重复元数据和 description 已表达的调用限制。current 的字段仍由共享契约维护，handoff 仅补充未完成现场。客户端实际触发与读取效果留待统一沙盒验证。

2026-09-28 路径引用清理：删除技能入口及 references 中重复的路径解析声明。执行材料和跨技能入口采用可解析的相对 Markdown 链接，适用于全局和项目内安装；示例、通配模式及目标项目产物路径不伪装成技能资源链接。子代理收到材料时保留来源路径。此轮只调整引用，不改变其他技能的工作流程。

## nk-brainstorm

2026-09-29 联合重构（用户确认后落实）：主流程、条件加载、范围检查点与交接归入口；interaction-rules 的短底线进入受控片段，具体提问与产品压力测试并入 dialogue；侦察、声明核实与模型分档集中到 evidence；术语细节分归对话和成文，需求自查归 sections。删除已被完整承接的本地 handoff、synthesis-summary、terminology、model-tiers、interaction-rules、product-pressure-test 文件，保持视觉、盲区与非软件分支独立。

保留 CE 的产品压力测试、方案比较、声明核实和 Ready for Planning Check；对照本地 CE `a763b392`，不引回平台配置、强制重读或菜单完成契约。规模按范围、风险和依赖判断，详细输入不自动升档；只补缺失证据，明确续作与改后继续不重复授权，视觉表达沿用会话偏好。已有决定与证据继续交给 plan；即时术语及已定标注规则不变。四段短底线由原共享约定维护，测试校验两个入口副本。实际行为仍待 U3。

#3 收口：读取复用和证据回传使用共享约定；复用证据、补查现状的阶段责任保持不变。

当前证据复用决定（2026-09-27 用户采纳）：ideate 交来的证据按主题、来源与现状核对；只补缺失、失效及新需求涉及的部分，保留其余有效证据。复用充分时不再无条件搜索或建立新侦察目录；仍保留具体断言的核实责任。

2026-09-27 方案 C：范围综述的共同整理、呈现与修订方法移至 conventions/scope-synthesis.md；本地保留产品范围目的、Path A/B 和文档落点；approaches、dialogue 与已定决策约定同步使用“延续 / 待确认点”。阶段 0 与 handoff 仍是需求阶段独立流程，纳入本地职责登记。

2026-09-27 续审：reference 读取改为缺失或变更时补读，移除综述重复示例，保留 Path A/B 与确认边界。综述落盘遵循 plan-format：行为需求留在 R，Key Decisions 只索引来源与理由，Success Criteria 不替代行为验收条件；草图和盲区分支的决策选项与共享规则对齐。

2026-09-27 减重审计：优先复用 ideate 传来的相关证据档案，按现状补缺而不重跑整轮侦察，并继续向 plan 传递索引；合并 Goal Capsule 与 Summary/Problem Frame 的重复解释。需求文件统一遵守 plan-format 的 R-ID 和必有章节；修正检查章节号、无仓库时的分类跳转与决策选项数量，区分探索备选和决策提问。保留范围确认的双信号分流、声明核实与术语维护。

主要参考：CE `ce-brainstorm` (2026-09)、Matt `domain-modeling`（术语即时质疑、用具体场景压力测试概念边界）、Matt `to-spec`（上下文已充分时不访谈、直接综合）。
与 CE 的主要差异及原因：
* 术语在对话中敲定即写入 `CONCEPTS.md`，文件不存在时新建：CE 只在写完 plan 后、且文件已存在时才补录，规划期敲定的术语因此流失。
* 互不依赖的问题合并为一轮提问（最多 3 个）：CE 规定每轮一问，交互轮数过多；合并规则见 `../conventions/decision-autonomy.md`。
* 只输出 Markdown；可视化探针改为对话内的 mermaid/文字草图，不启动本地网页服务。
* 去掉跨模型提权、Compound Packs、Slack 调研、Bake-off、CE 配置层与 `lfg`/pipeline 调用模式：本体系不使用这些基础设施。
* 指向 `ce-pov`、`ce-prototype`、`ce-doc-review`、`ce-proof` 等技能的分流改为内联原则或交接选项：NexusKit 没有这些技能。
* 完成的仓库内规划产物交给 `nk-commit`，携带已有证据与下一步并同步 current；仍在澄清的草稿暂留。

## nk-close

2026-09-28（#9 回归）：Issue 引用提取管道显式标注 Bash / Git Bash 前提，与 README 的通用命令及平台脚本边界一致。

2026-09-27 人工审计采纳：收尾按产物生命周期约定第二章补查本分支变化涉及的项目指导，修复有依据的遗漏与失效；不是全仓规范生成。指导文件及索引更新纳入同一次收尾提交。

主要参考：NexusKit 共享约定 [`../conventions/artifact-lifecycle.md`](../skills/conventions/artifact-lifecycle.md)（本技能为其第五章的可执行展开）
关键设计决定：
* 未消费发想记录与推迟 plan 逐项询问用户、每轮最多 3 个——用户 2026-09-25 拍板；无人值守时采用推荐默认并在 `docs/current.md` 登记 `[待确认]`。
* 在六步法前增加第 0 步前置检查（单元提交核对、工作区清点、验证证据核对）：证据缺失时警告用户而非放行，依据原提交约定的通用纪律补入（现归 nk-commit 第 3 步）。
* 提炼的判断细则下沉到 `references/harvest.md`，SKILL.md 保持聚焦"怎么做"。
* `docs/reviews/` 目录不存在时跳过并说明（项目可能尚未运行过 `nk-review`）。
* 收尾提交显式限定本技能涉及的文件路径：收尾时工作区可能仍有后续版本的半成品，防止混入提交。
* 提交信息风格遵循项目惯例而不写死格式：与 nk-commit、nk-handoff 的口径一致。

* 2026-09-27 起收尾锚点从"版本合并"改为分支生命周期（plan U3，用户拍板）：两种触发（分支合并前全量扫 / 单分支项目按 plan 小范围扫）+ 发布日扫尾小节（漏网检查 + release notes + 打 tag，不做提炼删除）；发布与收尾解耦为纯事件。第 1 步纳入 Issue 兜底扫描，指针引用 `issue-writing.md` 第四节不重述。
* 新增 `references/pr-description.md`（plan U4）：蒸馏自 CE `ce-commit-push-pr/references/pr-description-writing.md`（208 行 → 约 50 行），保留 value-first 原则、按决策成本伸缩的分级、`Fixes #N` / `Related: #N` 语义与"项目约定优先"；裁掉 base 解析机制、stack/多 PR 叙事、概念教学归档（概念与决策的沉淀由 `CONCEPTS.md` / `docs/solutions/` 在更早阶段接住）、branding、session-settled provenance；标题不写死 conventional commits，与 nk-commit "风格遵循项目惯例" 口径一致。
* 首次实战后修订（2026-09-27，本仓库自身分支收尾）：Issue 兜底扫描补机械方法（grep 收集引用 + `gh issue view` 核对，原条文只说不做）；"用户决策点"章节前置到执行步骤之前（第 1/3 步引用它，原先放在文末阅读顺序颠倒）；发布日扫尾去重——原则归约定第五章，技能只留操作展开；补 `git rm` 已暂存删除的提示；发现"首次创建 CONCEPTS.md 时挂 AGENTS.md 入口"无触发点，已补进生命周期约定第二章与第 2 步。

## nk-commit

2026-09-28（#11、#9 回归）：R5 后续已调整为每次提交前核对 current 并按需同次入库；README 集中说明跨平台命令边界，入口保留就近的逐条执行与 revision 引号提醒。

主要参考：CE `ce-commit` (2026-09)、原 NexusKit 提交节奏约定、本地 `chinese-commit-conventions` 技能（2026-09-28 读取）。
与 CE 的主要差异及原因：
* 按"交付变化 / 状态记录"而非文件类型判定提交类型：文档本身也可能是交付物（例如本仓库的技能文件）。
* 不在默认分支上自动建分支：个人项目常直接在 main 上工作，分支策略交给项目工作流文档。
* 验证证据写进提交正文：证据随提交永久保存，不需要额外文档。
* 2026-09-27 审计修订：上游分支判定示例给 `@{u}` 加引号，确保 PowerShell 与 bash 均可解析。

* 2026-09-28 重构：提交时机 R1–R6 内化到 nk-commit，入口按范围、节奏、证据、说明、执行、返回顺序组织；不再运行时读取 commit-cadence 或 artifact-lifecycle。旧引用已迁往公开入口，commit-cadence.md 已删除。所有本地提交统一经过公开入口；调用方引用已迁移；最终核对同步修正 handoff、compound、ask-ljq 和 current-md 的旧 amend 条件及纯文档限制，保留各自场景与文件范围，将提交判断交回 nk-commit。
* 提交文案从本地 `C:/Users/29617/.codex/skills/chinese-commit-conventions/SKILL.md` 提炼类型、动宾主题、正文动机、破坏性变更与 Issue 关联；保留项目风格优先，不引入工具安装、changelog 配置或固定中文 scope。仅实际不兼容才标记 BREAKING CHANGE，不照搬所有 Schema 改动都标记的规则。
* 有效验证证据直接复用；仅相关内容变化、证据缺失或项目要求时补查。amend 不以无 upstream 推断未推送；首次提交、混合文件改动及 hooks 修改需按实际状态处理。独立技能实跑留待全部重写后统一验证。

## nk-compound

#3 收口：阶段间复用已掌握的 capture 原文，修订建议按共享结果体量规则直接回传。

2026-09-27 方案 C：6 个角色复用 conventions/agents，文档校验目的保留在 capture.md 的选择处，返回紧凑修订意见，不扩为产品代码修改或全仓审计。

主要参考：CE `ce-compound` / `ce-compound-refresh` (2026-09)、NexusKit 共享约定
与 CE 的主要差异及原因：
* refresh 并入为审计模式而非独立技能：同一知识库的写入与维护收拢在一个入口，`refresh` 参数切换。
* scripts/ 整体删除：两份校验脚本转写为 `references/frontmatter-checklist.md` 与 `references/claims-checklist.md` 的人工核对清单；session-history 脚本组删除，改用当前会话上下文 + `git log` 定位刚解决的问题，依赖脚本的 session-historian 提示词随之删除。
* CE 基础设施删除：`docs_root` / `.compound-engineering` 配置层、Compound Packs、Proof 发布、Slack、auto-memory 与浏览器相关步骤。
* 模式裁剪：去掉 mode/depth token 体系（interactive/non-interactive、full/lightweight），沉淀走单一流程；无人值守场景由 `../conventions/decision-autonomy.md` 统一覆盖。
* 提交交给 nk-commit R3/R4：相关沉淀随交付，遗漏补记须符合完整 amend 条件，独立且已验证的知识成果可正常提交，未完成部分暂留；不自动建分支。
* 可见性检查并入首运行职责：按 artifact-lifecycle 第二章补 `AGENTS.md` 指引，而非每次运行单独征询。
* 术语表规则归 `../conventions/concepts-vocabulary.md`：本技能沉淀模式只做 Add/Refine，Fold/Retire/Scrub 与整库初建归审计模式。

## nk-debug

2026-09-28 按 CE 阶段结构重写。对照本地 CE 快照 `a763b392`（2026-09-25）的 `ce-debug/SKILL.md`、investigate、fix、anti-patterns 与 post-fix-handoff，以及 Matt 的 `diagnosing-bugs` 原文。

- **主流程归 CE**：保留调查、诊断后决定是否修复、测试先行修复和交付的阶段分工。入口持有阶段边界，investigate 与 fix 各自给出完整执行材料；不为减少文件强行合成一份大循环。
- **Matt 方法按需增强**：复现构造、收紧及最小化保留为条件材料；已有回路直接复用。去掉固定 3～5 个假设、秒级和固定复现率等硬门槛，保留精确症状、可检验预测与真实观测。无法复现可以继续补证，试修需有对应授权且不得冒充已确认根因。
- **反模式就近合入**：把预测质量、确认偏误、混杂实验和无信息重试合入调查/修复动作，删除独立 anti-patterns；reference 不再互相转读或引用 nk-work 私有 tdd-loop。测试规则以调试目的组织，明确不得通过改变既定行为契约让测试通过。
- **恢复有效出口**：仅诊断可正常完成；明确修复请求不重复授权。受阻时报告证据、缺口及可选下一步，由用户选择，不自动更新 current 或调用 handoff。
- **保留 NexusKit 边界**：分支遵循项目规则，所有提交交给 nk-commit；提交前调用 nk-review 获取报告，由 nk-debug 直接修复查证成立的问题，补做相关验证与针对性复核。不移植 CE 的模式令牌、固定返回体、默认 PR、branding、自动精简和审查编排，也不移植 Matt 的 HITL 脚本；人工复现用步骤与观测承接。
- **证据与现场**：工作区对比按需隔离，stash 不是默认动作；结果只支持关联，不能直接当作根因证明。保留先前失败、历史检索、日志脱敏、原始场景回归和只读子代理证据边界；不新增子代理固定编队。
- **条件技术**：保留竞态、性能、间歇性故障、边界调查等方法，入口按症状选章节。分层防御按实际复发路径和后果选择，不按文件数量或四层清单凑动作。

本轮核对为文本、来源与机械检查，真实调试效果仍待全部技能重写后的统一沙盒实测。没有因本轮静态改写关闭需要实跑证据的 Issue。

## nk-grill

#3 结果体量收口：事实查证子代理引用共享结果体量规则，只回传结论、来源和未决事实。

主要参考：Matt `grilling`（2026-08 备份，28 行全文骨架：设计树、前沿轮次、每问带推荐答案、事实查证归 Agent、前沿清空且用户确认为完成标志）。
与上游的主要差异及原因：
* 正文改写为中文并套用 NexusKit 体例：问题/推荐格式去 emoji 改纯文本。
* `disable-model-invocation: true`，仅手动触发：D6 当年否决的是强制盘问，本技能是用户主动召唤的盘问入口（2026-09-27 深化拍板，见 `plans/2026-09-26-2246-feat-issue-lifecycle-branch-close-plan.md` KTD3/KTD3a）。
* 豁免 `../conventions/decision-autonomy.md` 的"单轮最多 3 个问题"上限：该上限针对 Agent 主动打断的场景，用户主动召唤盘问时带宽已预留，"一轮问完整个前沿"正是目标体验；全局规则不动，留待 grill 实战检验后回看。超过客户端提问工具上限时退回对话内编号列表。
* 事实查证的子代理措辞中性化（客户端中立），不绑定具体工具名。
* 不强制文档产物（用户拍板）；收尾只给一句转向 `nk-brainstorm` / `nk-plan` 的轻指针。

## nk-handoff

2026-09-28（#19）：主流程收敛为核对、更新检查、委托提交、汇报四步；完整字段只由 current-md 格式契约持有，保留无实施单元时的技能与产物路径分支。补充旧信息保留、非代码残留、核对基点与最终提交的区分；交接可携带归属明确且已满足入库条件的文档工件。删除生命周期规范必读与重复提交判定。

主要参考：CE `ce-handoff` (2026-09)、Matt `handoff`、NexusKit 共享约定 [`../conventions/current-md.md`](../skills/conventions/current-md.md)
与 CE 的主要差异及原因：
* 交接载体是仓库内单例 `docs/current.md`，而不是临时目录中的独立文件：不堆积、不丢失，新会话经 `AGENTS.md` 自动找到。
* 没有 resume 模式：会话开始时的核对由 `nk-work` 第 0 步负责。
* 交接提交统一交给 nk-commit 判定；满足其 R3 的本会话交付补记才 amend，不自行判断未推送。
* 2026-09-27 审计修订：交接中的上游判定示例与提交节奏约定统一使用带引号的 `@{u}`。

## nk-ideate

#3 收口：读取复用和子代理结果体量分别引用 resource-loading.md 与 subagent-results.md；候选全量卡片与现有领域适配保持不变。

当前减重决定（2026-09-27 用户采纳）：非软件 reference 只保留领域评价与快速/标准内联、完整独立派发的差异，生成、核查、筛选和收尾共用主流程。数量与核实预算集中到 divergent-ideation.md：常规采用原软件路径 6~8、tactical 3~4 的参考量，取消硬凑数和去重后目标；非软件快速留存仍为 3~5。组合与补轴只有上限，用户原始总数不被额外补量扩大。研究返回结论与来源，长材料按需落到已有临时目录；所有候选仍以紧凑卡片参与统一批判，不用摘要丢掉候选或反证。

2026-09-27 方案 C：learnings/web 研究员改用 conventions/agents 的唯一方法源，发想目的、关注点与直接返回方式留在 grounding.md；网络摘要使用共享 research-digest.md。保留空经验库短路、缓存及证据交接的既有修订。

2026-09-27 续审：reference 原文在上下文完整且未变时复用；空经验库先短路，术语仍按需读取。缓存限定本会话已知路径并核对时效，失败结果不缓存；指令材料只复制适用规则原文。合并 Issue 回退复述，修正 Issue 统计总数表达、固定年份与旧客户端工具限制，保留只读追踪器边界。

2026-09-27 减重审计：入口及非软件分支删除重复菜单，非软件拆轴复用已有结果与 decomposition 规则；缩短收尾自查，保留直接依据核实、覆盖缺口与降级披露。向 brainstorm 交接相关证据档案索引；修正必读数量、日期与输出路径说明。该轮保留六视角与原有预算；后续统一数量与执行差异见本节当前决定。

主要参考：CE `ce-ideate` (2026-09)、NexusKit 共享约定 [`../conventions/`](../skills/conventions/)
与 CE 的主要差异及原因：
* 只输出 Markdown，去掉 HTML 渲染、浏览器打开与 Proof 发布：用户选择统一使用 Markdown，发想记录由人和 Agent 都直接读文件。
* 去掉 `.compound-engineering` 配置层与 `docs_root`：NexusKit 不使用 CE 配置文件，产物位置固定在 `docs/ideation/`。
* 去掉 Slack 调研：用户不使用 Slack 作为信息来源。
* 临时目录改为不依赖 bash 的中立描述：技能需要在 PowerShell 等多种 shell 与客户端中运行。
* 提问改为批量规则（每轮最多 3 个）：遵循 NexusKit 的决策自主约定；"累计超过 3 个问题说明选错流程"的原则保留。
* 下一步可深入 brainstorm、继续讨论或结束；发想记录写入文件但不自动提交，用户需要时自行调用 nk-commit。丢弃仅适用于本次新建且未提交的草稿，不自动调用 handoff。
* 保留六视角、独立依据核查和 tactical / `go deep` 的质量取舍；当前减重只统一数量口径与共用流程，不额外缩小编队。

## nk-plan

2026-09-29 联合重构（用户确认后落实）：入口持有路线、范围确认位置、深化判断、自检、提交与交付；本地 handoff 与 synthesis-summary 的方法和落点已归入口、共享综述与 structure，删除薄包装文件。final-review 只检查并写入，deepening-workflow 只补强选中章节后返回；research-roles 保留共享角色目的和结果规则，不复制角色库。

输入承接区分明确续作与仅发现相关文档，旧文档不自动扩大任务；最新已授权意图修订只替换冲突部分。调研按上游证据覆盖补缺，保留 CE 的技术决定、稳定 U-ID、具体测试场景、置信度评分与自检视角；不把浅层侦察当成完整技术研究。深化无修改只有在已有自检仍有效时才能复用，无证据须自检。图中已定设计约束与说明性伪代码的效力只在 structure 定义，图文冲突须修正。

规划交付完成与用户选择后续动作分开；合格仓库产物经 nk-commit 提交，只有授权实施才调用 nk-work。非代码交付按实际用途区分聊天答案、用户使用的计划和 execution: knowledge-work 做法 Plan，通过 work 公开入口承接，移除私有 reference 链接。依据为本地 CE `a763b392` 与已采纳组织范式；不改变 description 语言策略，不宣称实跑通过。

2026-09-28 用户实用反馈：Plan 往往在主分支完成后才开实施分支，因此完成的 Plan 必须通过 nk-commit 入库；ideate 没有这一前置要求，不设置自动提交或提交询问步骤。

#3 处置：按 resource-loading.md 复用规则原文，阶段 0 各分支写明触发条件（已定决策可与输出档位叠加）；调研与深化按 subagent-results.md 回传结论、反证与路径，按需读片段。固定状态返回行不采纳：没有实际消费方，且 D11 已否决返回编排契约。

2026-09-27 方案 C：10 个复用角色移至 conventions/agents，规划目的集中在 research-roles.md，研究与深化共用该映射而各自持有返回方式。范围综述引用共享方法；阶段 0 与 handoff 保留规划职责。此次全体系迁移已覆盖这些内容，不再等第 6 节点处理副本。

2026-09-27 关联修正：核对 web-researcher 的 ideate 同名副本后，同步把固定年份改为环境日期与当前年份占位；规划研究的任务目的、方法和输出契约不变。后续由本节方案 C 记录接续；第 6 阅读节点仍审核其余规划流程。

主要参考：CE `ce-plan`（2026-09，含 `references/agents/` 研究员与深化视角）、CE `ce-doc-review` 的审阅视角（并入写后自检）、Matt `codebase-design`（Design It Twice、依赖分类）。
与 CE 的主要差异及原因：
* 只输出 Markdown：`nk-work` 按标题定位 plan 章节，单一格式最稳；HTML 渲染规则和预览脚本不再需要。
* 不调用 `ce-doc-review`，改为写后自检：保留其连贯性、可行性、范围、安全、设计、产品、对抗性视角的检查要点，由主会话执行，避免依赖一个单独的审阅技能和强制多代理审查。
* 去掉模型提权、跨模型调度脚本、Compound Packs、Slack 调研、`docs_root` 等 CE 配置层与流水线模式：这些依赖 CE 专有的基础设施或编排方，本体系不使用。研究员与深化视角的子代理规模保持 CE 原样。
* Bake-off 改为设计对比（取自 Matt 的 Design It Twice）：不依赖单独的竞赛技能，同样用于后果重大、难以推翻的"怎么做"。
* 提问从"每轮一个问题"改为批量提问：按 `decision-autonomy.md` 减少一问一答的往返。
* 规划中即时写入术语，而不是只在术语表已存在时补漏：让规划期诞生的术语不流失。
* 收尾菜单改为 NexusKit 流程：完成的 Plan 通过 nk-commit 携 current 入库，新会话可用 `nk-work` 接手，不额外触发 handoff；去掉 `/goal`、原型和浏览器打开选项。

## nk-review

2026-09-28（#11、#9 回归）：统一收尾术语；范围探针改为逐条 Git 命令与输出哈希占位符，去掉 Bash 赋值及链式回退，保持现有基线选择逻辑。

2026-09-28 吸收 Ponytail 的复杂度审查理念：复用现有 maintainability 角色，按实际重复实现、依赖或扩展层的证据触发，报告可删除内容、具体替代及行为等价依据；不新增独立审查流水线。移除按文件越过 1000 行直接判 P1 的门槛，改为职责与维护影响；单个实现或调用方不自动构成过度设计。

#3 / #22 处置：取消 50/200 行编队阈值，改以结构、状态、信任边界、补偿路径和静默放行机制的具体 diff 证据判定；配置按行为而非扩展名分类。读取复用及返回体量使用共享约定，保留完整 JSON 和证据契约。

2026-09-27 方案 C：learnings、migration、deployment 方法共享，审查目的与 JSON 结果契约由 reviewer-prompt.md 唯一持有；派发包含完整契约和选中角色说明。移除 agent-native 的独立 Markdown 报告要求，保留其检查方法。部署角色不再返回另一套检查单或使用上游角色名。

主要参考：CE `ce-code-review`（2026-09，意图摘要、风险编队、personas 与复核机制）、NexusKit 共享约定。

2026-09-28 联合重构：支持单元、修复与分支范围，复用调用方定界；主会话直接派发独立叶子 reviewer，必需代理不可用时不声称完成。simplify 负责精简机会，maintainability 聚焦结构边界风险；统一契约、语义去重与独立 validator 复核，保留 nk-close 消费的状态词和编号。不自动登记 current、建票或提交。

2026-09-28 归因修正：不采用 Matt `code-review` 的 Standards / Spec 双轴编排与分轴报告；当前流程本就按风险编队并统一合并发现，移除原先“双轴思想”的来源表述。变更意图与项目规则仍作为 CE 式审查上下文，固定范围与空 diff 早停保留为基础检查。review 向 simplify 传递已确定的范围和快照，由主会话直接派发三个精简分析子代理，与风险审查并行，统一复核汇报。
与 CE 的主要差异及原因：
* 产出从临时运行目录与报告改为目标仓库 `docs/reviews/` 的状态化条目：审查记录是本体系的短期生命周期产物，由 `nk-close` 消费。
* 删除全部脚本（范围信号、findings 机制、跨模型调度、运行日志等）：规则性内容转写为 references 中的 Markdown 条款，编排与跨模型对抗审查不内置（可一句话建议用另一个客户端复核）。
* 删除 mode:agent JSON 输出、本地修复（apply）与 autofix 路由字段：本技能只产出报告，修复和分流归调用方或用户；work 与 debug 在各自入口处理。
* 深度闸门（lite/focused/full）简化为范围信号 + 后果判断：个人项目规模下三档编排的收益不抵复杂度；保留基于具体行为的静默放行守卫，取消行数阈值。
* PR 路径降级为可选：保留只读取数与 previous-comments persona 的适用条件，不切换分支。
* reviewer 返回紧凑 JSON、由主会话渲染条目：persona 提示词保持英文原文，条目格式集中在 entry-format.md 单处维护。
* 2026-09-27 审计修订：范围收集示例拆为独立命令，遵循跨 PowerShell 的单命令纪律。

## nk-simplify

2026-09-28 与 nk-review 联合重构：独立调用须用户明确触发，review 可显式加载公开入口，直接复用其范围与快照。主会话派发复用、质量、效率三个叶子子代理，与风险审查并行；无子代理则报告未完成，不以内联角色替代。

主要参考：CE `ce-simplify-code`（2026-09，三个分析视角）、Ponytail 的删减优先与原生能力复用、NexusKit 的已定决策及结果体量约定。

- 与 CE 的自动应用不同：默认只分析；单独调用先报告，后续按用户决定执行；嵌入 review 时只返回发现，由 review 统一独立复核和成文。
- 不自动提交，不串联另一次 review 或 handoff。获准修复后针对性验证，复用仍有效的证据。
- 保留行为等价、安全与有效隔离边界的证据要求，不以净删行数、一个调用方或一个实现决定删除。
- 不移植 CE 平台特定的模型档位、调度脚本或代理生命周期 API；受限容量通过主会话分批派发处理。

## nk-to-issue

主要参考：Matt `triage`（核实与 brief 部分）、NexusKit 共享约定 [`../conventions/issue-writing.md`](../skills/conventions/issue-writing.md)
与 Matt `triage` 的主要差异及原因：
* **不是状态机形态**：Matt 围绕 maintainer 的 labels/buckets/state roles（needs-triage、ready-for-agent 等）组织批量分诊；NexusKit 是个人项目、用户自己就是 maintainer，没有"分诊队列"，本技能只处理单条"开发中冒出的发现"，状态流转交给 Issue 平台自身。
* 删除 external PR surface、AI disclaimer 与 setup 配置探测：个人项目无外部贡献者分诊需求，产物位置由 artifact-lifecycle 约定固定。
* 删除 grilling 循环：需求澄清按 decision-autonomy 的批量提问规则进行；用户主动想被盘问时可另行调用 `nk-grill`（2026-09 新增）。
* 保留第 1 步的查重与冗余检查、第 3 步"按步骤复现后再落档"，以及 triage notes 的"已确认事实/还缺什么"二分——后者转写为 issue-writing 约定中 Evidence 小节的核实结论与缺口写法。
* `.out-of-scope/` 知识库未引入：其"曾被否决的请求"在本体系中的对应物是 `docs/ideation/` 未选中方向、已关闭 Issue 与 `docs/solutions/`（见第 3 步）。

## nk-wait-what

主要参考：Matt `wait-what`。差异：术语表从 `CONTEXT.md` 换成 `CONCEPTS.md`；ASD-STE100 的硬性要求放宽为"简单直接、没有歧义"（中文协作场景）。

## nk-wayfinder

#3 结果体量收口：research 回传引用共享约定，同时保留 ticket 对持久研究成果的链接，不用临时路径代替跨会话依据。

主要参考：Matt `wayfinder`（2026-08 本地备份，128 行全文）。
与 Matt 版的主要差异及原因：
* Tracker 固定为 GitHub Issues（`gh` CLI），label 缺失时用 `gh label create` 创建；删除 tracker 配置探测与安装引导步骤：体系不需要多 tracker 抽象。
* 无远端时明确不可用并建议改用 `nk-plan`/`nk-brainstorm`：wayfinder 的价值在 tracker 的查询与可视化，不发明本地降级格式。
* `/grilling` → 按 `decision-autonomy.md` 提问规则进行 HITL 对话：体系有意移除了强制盘问；用户主动发起的盘问由 `nk-grill`（2026-09 新增，仅手动触发）承载。
* `/domain-modeling` → 术语即时写入 `CONCEPTS.md`，规则在 `concepts-vocabulary.md`。
* `/research` subagent → 中性写法：支持子代理则派发，否则主会话内联完成；去掉一次性 research branch 约定（客户端无关性，findings 直接从 ticket 链接）。
* `/prototype` → 一句话内联：构建廉价粗糙的具体产物辅助讨论，不依赖技能。
* 删除 `agents/openai.yaml`：客户端专有配置。
* 新增与 `nk-compound`、`nk-plan`/`nk-work` 的衔接说明；结束只汇报，不自动 handoff，以及无人值守下 HITL ticket 的登记规则。

## nk-wizard

主要参考：Matt `wizard`（2026-08 备份，`skills/wizard/`）
与上游的差异及原因：
* 正文改写为中文并套用 NexusKit 体例（执行步骤编号、"Done when" 判据原义保留）；上游描述段精简为适用场景说明。
* `template.sh` 逐字节保留为 `assets/template.sh`，不翻译不精简：上游明确 library 部分永不手改，一致性正是重点；该文件是技能交付物的模板资产，不是技能自身的自动化设施，不违反体系"纯 Markdown 无脚本"原则。
* 删除 `agents/openai.yaml`：客户端专用配置，NexusKit 客户端中立。
* 新增两处衔接：Windows 下用 Git Bash 运行的说明；入库例外明确指向 nk-commit R1，并提示用 `nk-compound` 沉淀过程中发现的非显性知识。

## nk-init

2026-09-28：随 current-md 契约调整，将初始状态中的 HEAD 描述改为核对基点，不要求记录尚未产生的交接提交哈希。

主要参考：Matt `setup-matt-pocock-skills`（2026-08 备份；仅借鉴骨架）

关键设计决定：
* 保留"探测 → 展示确认 → 幂等写入"的三段 explore-first 骨架与"探测已确定答案的不提问"；不移植 Matt 专有的 issue tracker 选择、triage label 词汇表、CONTEXT.md/ADR 布局等配置面——那些是 Matt 体系的配置，与 NexusKit 产物矩阵无关。
* 写入对象是 NexusKit 自有产物：全局指令文件的知识入口指引（artifact-lifecycle 第二章）、`docs/current.md`、无远端时的 `docs/backlog.md` 降级。
* 负向清单写进流程：不建 `CONCEPTS.md`（由第一个合格词条创建）、不建空目录（git 不跟踪空目录）。
* 带 `disable-model-invocation: true`（手动技能）；提交通过 nk-commit。

## nk-ask-ljq

2026-09-28（#11）：收尾用词按 CONCEPTS 统一，R4 摘要与 README、nk-commit 的四类场景对齐；后续提交政策随 nk-commit 的 current 归属调整同步。

#26 安装语义窄修：明确整套安装后的独立入口，不再暗示单技能安装；其余引导内容仍留到全套阅读后重写。

主要参考：Matt `ask-matt`（2026-08 备份）

关键设计决定：
* 名字含作者缩写 ljq（个人元素）；曾定名无前缀的 `ask-ljq`，后统一回 `nk-` 前缀保持命名一致。
* Matt 的"main flow + on-ramps"单主线结构改为"工具箱宣言 → 参考路径 → 按场景入口"：落实 D1（工具箱不是流水线），路由而不规训，明说每步可单独用、可跳过、可从中间进入。
* 保留"问我就行"的作者口吻与语境卫生建议（`docs/current.md` 接手、完成单元后停止、凭 current 接手；不估算上下文阈值触发交接）。
* 新增 R1–R6 提交节奏一句话版（细节路由给 `nk-commit`）；删去 phase boundaries 决策树、prototype/triage/vocabulary layer 等 NexusKit 无对应物的内容。

## nk-work

2026-09-28 表述修订：六份执行 reference 的开头改为直接说明适用场景和下一步动作；拆开子代理开头的使用条件与选择依据，保持原有规则含义。

2026-09-28 边界修订：一次调用只执行已确认的一个实施单元，完成或形成不可自行解除的阻断后汇报结束，不再根据估计的上下文余量顺延。子代理返回、主会话验收与 Git 提交分别判断：逐项核对结果，整合后亲自验证，按完整的交付变化提交，不按代理数量或结束时机切分提交。

2026-09-28 试点修订：委派恢复由 Agent 自主选择（遵守用户、项目与客户端限制），不要求用户先点名。对照本地 CE `ce-work/references/implementation-loop.md` 与重构前版本，补回真实调用链、既有模式、测试发现、具体因果检查、持续测试、构建/typecheck/lint 和验收核对；仍保持一个完整执行 reference，不恢复递归读取。仓库外状态必须实际观察，不能由 Git 或 Mock 结果推断。

#3 处置：结果体量引用 conventions/subagent-results.md，保留改动与真实验证证据。实施子代理一单元一上下文，同单元修正可续用；验收后不跨单元复用，不要求客户端关闭 API。委派仍可选。固定状态返回行不采纳，沿用 D11 与自然语言汇报。

2026-09-27 人工审计采纳：项目指导随相关变化维护，单元提交前引用产物生命周期约定第二章检查；与 `nk-close` 的收尾补漏衔接。规则由共享约定唯一持有，保留 `nk-init` 的最小初始化定位，不把每条经验自动升级为项目规则。

主要参考：CE `ce-work` (2026-09)、Matt `tdd` / `implement`、NexusKit 共享约定

与 CE 的主要差异及原因：
* 未移植调度脚本、跨模型执行与默认并行波次：本体系是一个会话串行推进、主对话提交，不需要这层编排。
* 进度以带 U-ID 的提交为准，不为记进度修改 plan：plan 的每次改动都应是有意义的范围或决策变化。
* 一次调用一个单元、完成后停止：不估计自身上下文余量；提交时由 nk-commit 同步 current，下一单元由后续调用接手，不自动 handoff。
* 接手时"一致则继续，不一致才停"：`current.md` 是本仓库的单例文件，不像 CE 的交接文档那样来源不可信。
* 脏文件分两类：`current.md` 登记的半成品由本会话接管，其余一律不暂存。
* 提交前调用 nk-review 获取报告，由 nk-work 直接修复查证成立的单元内问题；超出单元的问题走阻断出口，转 Issue 或 handoff 等后续由用户决定。修复后针对性验证与复核，复用仍有效的证据。
* 测试 seam 由 Agent 自选（改写 Matt `tdd` 的"先与用户确认"）：测试结构属于自主决断区。


## Ponytail 理念适配（2026-09-28）

参考本地 `D:/codex_project/upstreams/ponytail` 的 `AGENTS.md`、`skills/ponytail/SKILL.md` 与 `skills/ponytail-review/SKILL.md`，快照 `e3ba2aa`（v4.10.0，2026-09-14）。上游为 DietrichGebert/ponytail，MIT；归属及许可证见根目录 NOTICE。

采纳“先理解真实流程，再用更少自维护代码满足同一需求”：不建设推测功能，先找仓库已有能力、标准库/原生平台与已装依赖，尽量在根因层修复，保留必要质量底线。按阶段分别适配到 work 的方案选择、review 的证据判断和 simplify 的行为保持删减；阶段动作各有职责，不新增互相引用的共享执行文档。

不移植持久激活、强度档位、hooks、MCP、单行输出、强行一行实现、净删行评分、最多一个测试或“先交付简化版再质疑需求”的策略。保留 NexusKit 的真实验证、范围、用户已定决策和各技能分工。上游 benchmark 未在本仓库复跑，不把其降幅当作本次效果证据。

质量核对是文本与规则层面的比较：本轮补回上次压缩遗漏的执行动作；CE 的自动精简、交付审查回执及发布流程仍与 NexusKit 的独立 simplify/review 分工不同，不声称两者整条交付流程等价。

## nk-work 架构试点（2026-09-28）

本轮将 `nk-work` 的正常实施路径收敛为入口 + 一个完整的 `references/tdd-loop.md`；`intake.md`、UI、非代码、仓库外状态和子代理是由入口直接选择的叶子材料。删除 `implementation-loop.md` 与 `testing.md` 的递归拆分，避免正常代码路径在实施规则与测试规则之间跳转。

入口内的四个执行底线以 `skills/conventions/work-guardrails.md` 为维护源，修改时同步源与副本，并由 `tests/run_checks.py` 检查一致性：验证证据、已定决策、升级确认和子代理提交边界。当前没有同步生成脚本；客户端直接消费 `nk-work/SKILL.md` 中已同步的片段。

本试点不禁止资料性链接，不改变整套安装模型，也不把跨技能协作改成隐含的自动编排；提交委托 `nk-commit`，`nk-handoff` 仅由用户显式调用。真实客户端执行效果尚未验证，需在沙盒中比较正常代码、非代码、UI、外部状态和委派路径的实际读取与完成证据。

提交接口与 `nk-commit` 保持一致：仅在有 U-ID 时传入并附加到提交主题，Issue 或直接需求没有 U-ID 时不要求补造编号。

2026-09-28 后续调整：nk-work 提交前必须完成审查，具体方式及与 nk-review 的衔接留待该技能重构；向 nk-commit 传递审查结论与可复用的验证证据，不将测试通过等同于审查通过。

用户已认可这一组织方式作为后续逐技能整理的范式。设计理由、取舍和适用边界集中记录于 [技能组织决定](solutions/architecture-decisions/2026-09-28-skill-execution-locality.md)；review 的触发安排留待该技能审查时决定。

## 共享方法（方案 C，2026-09-27）

正典方法位于 [conventions/agents](../skills/conventions/agents/)，来源沿用原角色的 CE 方法及 NexusKit 运行时适配；没有新增构建期 overlay 或独立技能。调用方提供目的、范围、结果格式与交付方式，文件中的相对引用以方法文件的实际路径解析。网络研究摘要、范围综述分别由 [research-digest.md](../skills/conventions/research-digest.md) 和 [scope-synthesis.md](../skills/conventions/scope-synthesis.md) 持有，按需读取。

本次 13 组评审结果（维护依据，不是问题或进度清单）：

| 原同名组 | 归并判断与保留差异 |
| :-- | :-- |
| best-practices-researcher | 共用研究方法；规划关注实施约束，沉淀关注引用、预防与过度泛化修正；合入仅使用实际可用技能的兼容说明 |
| framework-docs-researcher | 共用版本、API 与官方资料核实；规划输出实现影响，沉淀输出经验依据和适用版本 |
| data-integrity-guardian | 共用迁移、事务、隐私与一致性检查；规划给要求，沉淀核实修复原理和复用前提 |
| pattern-recognition-specialist | 共用模式与重复检查；规划给参照写法，沉淀识别可推广的经验类别 |
| performance-oracle | 共用性能分析；规划给测量与扩展要求，沉淀核实改进证据，不另写固定报告 |
| security-sentinel | 共用可信攻击路径分析；规划给控制与验证要求，沉淀核实漏洞原理和预防范围 |
| learnings-researcher | 共用检索与适用性方法，合入 architecture_decision、applies_when、淘汰状态处理；发想、规划、审查目的分别在调用方；删除散文消费假设 |
| web-researcher | 共用来源判断、调研方法和环境日期；发想优先方向，规划优先决策依据；摘要体量单独共享，直接/文件返回归调用方 |
| data-migration-reviewer | 共用漂移、迁移和回滚分析；审查置信度、严重性及 JSON 归 review；规划要求归 plan；无 diff 不假装查过漂移 |
| deployment-verification-agent | 共用上线检查方法与示例；规划给就绪要求，审查给有证据的缺口；示例不授权执行部署 |
| phase-0 | 职责独立：需求分类续作与规划产物分流；保留本地文件，不因同名强行合并 |
| handoff | 职责独立：产品范围交给规划、可实施计划交给 work；提交和产物生命周期仍引用已有约定 |
| synthesis-summary | 共用整理、术语、呈现与修订；本地保留阶段目的、确认入口和文档落点；两类预算计数对象不同，集中定义而不混为一个数字 |

开发源没有可编辑副本。`tests/shared-resources.json` 登记唯一来源、调用点和独立流程职责；检查覆盖 references 根层、嵌套引用、同名及完全相同的改名副本。回归测试搬迁完整分发目录并注入缺文件、旧路径、意外副本等失败；这验证目录完整性，不等同于客户端安装或真实代理行为测试。

2026-09-28 共享约定修订（#30）：settled-decisions 的适用范围改为所有记录或承接已定决策的引用技能，移除只列 brainstorm/plan/work 的不完整归属说明；判定与标注方法保持不变。
