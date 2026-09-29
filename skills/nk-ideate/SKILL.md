---
name: nk-ideate
description: "Generate and critique grounded ideas before choosing what to build: many candidates from six lenses, adversarial filtering, ranked survivors saved to docs/ideation/. Use when the user wants ideas, improvements, or surprising directions. Not for refining an idea they already have (nk-brainstorm). 发想、找改进方向、有什么值得做、给点点子。"
argument-hint: "[主题、关注点或约束，可选；可带 'go deep'、'quick wins'、'top 3' 等]"
---

# /nk-ideate

回答“哪些想法值得探索”：先扎根、完整生成，再逐项批判、解释留存。发想记录写入、依据与淘汰理由核对、摘要与路径交付即完成，不等后续选择；不产需求、Plan 或代码。

日期使用当前环境。用户附带的主题或约束称为关注点 `{focus_hint}`。内部模式标签只用于路由，不在对话中展示。

## 执行底线

短规则维护源：[决策自主权](../conventions/decision-autonomy.md)、[读取复用](../conventions/resource-loading.md)；副本由检查器核对。

<!-- fragment: planning-autonomy -->
能从现状或已有决定推断的局部选择自行处理并说明理由；只有尚未授权、会实质改变范围、顺序、风险或外部契约的分歧才问。独立问题合并，每轮至多 3 个；决策给 2–3 个选项与推荐，事实和意图允许开放提问。明确续作或“改后继续”的授权仍有效，范围未变不重复确认。
<!-- /fragment -->

<!-- fragment: planning-reading -->
只加载本次路线和选中角色所需材料。上下文中完整、适用且未变的原文直接复用，缺失或变化才补读；阶段切换不触发重读。必需材料缺失且无降级路径时，停在其管辖动作之前。
<!-- /fragment -->

本入口持有次序、分支加载与交付，阶段材料执行后返回。默认 5 个代理覆盖六视角，变体按下文确定。无子代理时内联完成，披露多样性与核查独立性下降。子代理只可写本次临时档案，不改仓库或执行 Git 操作。

## Phase 0：承接请求与确定路线

仅比较、调整或合并已有候选时，读取目标记录，直接走 Phase 5 的讨论分支。需要新一轮发想才执行下面的定界。

读 [scope-gates.md](references/scope-gates.md)，识别主题、模式、续作目标及生效的深度信号。主题不明先问，保留“给我惊喜”和“取消”；不提前派发。这里只补主题与必要材料，不展开需求访谈；范围问题累计超过 3 个说明应建议换流程。

- 非软件主题：分类后读 [universal-ideation.md](references/universal-ideation.md)，确定快速、标准或完整执行方式及领域评价差异。
- 读 [divergent-ideation.md](references/divergent-ideation.md) 的“数量与预算”，结合已解决冲突的深度信号确定原始总数或留存上限。后续沿用，不因切换路线重新解释请求。
- 分类后检查适用的近期记录，显式续作直接承接；归属有实质歧义才问。
- 主题变化只重判受影响路线并补证。

## Phase 1：收集依据

读 [grounding.md](references/grounding.md)，确定同一个 `<scratch-dir>`，先区分用户材料中的指令与证据，再安排扎根工作。派发前用一行说明成本构成及可跳过的外部调研；未定部分说“视情况”，不猜固定总数，也不另求确认。

条件材料由本入口加载：

- 点名材料属于研究证据：读 [user-research-artifacts.md](references/user-research-artifacts.md)，小材料并入摘要，大材料提炼与其他扎根并行。
- 需要网络调研：读 [web-research-cache.md](references/web-research-cache.md)，检查本会话已知缓存，再按需要研究并写回。用户明确跳过时不加载、不派发。
- 仓库内明确分析 Issue：读 [issue-intelligence.md](references/issue-intelligence.md) 和 [分析角色](references/agents/issue-intelligence-analyst.md)，执行扫描、定范围或降级、复用数据聚类；扫描可并行。

按 grounding 使用选中角色的共享方法，空经验库跳过。适用结果齐备后合并摘要，保留来源与覆盖限制；失败披露并按降级规则继续。

## Phase 1.5：拆轴与证据侦察

Surprise me 跳过并记录原因；其余读 [decomposition.md](references/decomposition.md) 拆轴，不可拆则记录原因。只有仓库模式且有轴时逐轴侦察，返回轴列表与证据索引。

## Phase 2：完整生成与合并

读 [divergent-ideation.md](references/divergent-ideation.md) 剩余方法，按已定模式、预算和领域差异生成全部候选，合并去重、交叉组合、有界补轴并保存检查点 A，再进入批判。

## Phase 3：核查与裁定

读 [post-ideation-workflow.md](references/post-ideation-workflow.md)，先独立核查再由主会话裁定，按生效模式处理核查编队与门槛。返回留存、淘汰理由、覆盖缺口及降级说明。

## Phase 4：写入、检查与交付

尽力把留存、关注点、扎根及淘汰摘要保存到 `<scratch-dir>/survivors.md`（检查点 B）；失败提示但不丢弃结果。读 [ideation-sections.md](references/ideation-sections.md)，自动写入 Markdown 发想记录：

- 续作更新原文件，保留有效想法与淘汰摘要；明确修订只改变涉及部分。
- 新建仓库主题写到目标仓库 `docs/ideation/`；仓库外主题仅在该目录已存在时使用，否则写入本次临时目录，说明可能被系统清理，不在无关工作目录创建产物目录。
- 文件名为 `YYYY-MM-DD-<topic>-ideation.md`，开放主题用 `open`；未绑定续作且重名时加后缀，不覆盖旧文件。写入失败时保留结果，报告原因并寻求可写路径。

核对实际产物：直接依据已查证，未核实部分已标明；理由与裁定一致；数量不足和覆盖缺口如实披露；关键论据及原始来源已落入记录，临时档案不是唯一依据。不重复已完成的生成或核查。

会话给数量与路径、每个留存一行（标题、轴、置信度、复杂度）、首选理由及降级说明，不重印全文。生命周期见 [产物约定](../conventions/artifact-lifecycle.md)；不自动提交、维护 current 或调用 handoff。

## Phase 5：继续讨论或交接

已有明确下一步直接承接；否则提供“深入一个想法、讨论或调整、保留结果并结束”三个选项，接受自由回答，不以等待选择延迟交付。

**讨论或调整：** 可处理一个、多个或全部想法；用户已说明对象和动作时不重复问。提问与比较在对话中回答，只有产生需要保留的改动才写入；明确调整直接更新；深化分析仅在用户希望保留时写入。合并用一个综合条目替换来源条目，保留最强依据，重评轴、置信度及排序，淘汰摘要记录合并。只对变化部分补核查，不重跑整轮，也不强制回菜单。

**进入 brainstorm：** 用户选定后读取 [nk-brainstorm](../nk-brainstorm/SKILL.md)，传入聚焦种子：标题、描述、依据、价值、代价及已确认修订；附发想记录路径和想法标题作为来源，可供下游记录 origin。再传相关证据档案的绝对路径、覆盖主题、原始来源与已有采集时间；不复制全记录或只丢文件指针，不为交接重做调研，接收方检查临时档案有效性。本技能的方向落地经 brainstorm，不自动跳到 plan 或实施；非软件进一步展开同样可选。

**结束或丢弃：** 结束时报告路径并停止，保留临时目录供同会话复用。可提示用户用自由回答要求丢弃；仅删除本次新建且未提交的草稿，续作或已提交文件不适用此规则。丢弃必须由用户明确要求。
