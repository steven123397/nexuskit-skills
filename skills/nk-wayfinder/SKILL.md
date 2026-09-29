---
name: nk-wayfinder
description: "User-invoked exploration of a large, uncertain goal through a shared GitHub decision map and tickets. Resolve questions until scope and decisions are ready for planning, then hand evidence to nk-plan for a standard implementation Plan. Explore the route rather than deliver the implementation."
argument-hint: "[可选：map issue URL 或编号；留空则带着新想法 chart]"
disable-model-invocation: true
---

# /nk-wayfinder

一个松散想法出现了：它太大，单个会话装不下，而且被 fog 包围，通往 **destination** 的路还看不见。Wayfinding 的目标是找到这条路，而不是朝 destination 猛冲：把路径绘制成 issue tracker 上的 **shared map**，逐个解决 **decision tickets**——它们承载需要决策才能解决的问题，而不是要执行的 build slice——直到路线清晰。

**完成标志：** 目标、关键范围和产品取舍足以进入实施规划，剩余未知已区分为规划期解决、实施期验证或真正阻断。Charting 完成指 map 与首批 tickets 已建立，研究的完成、进行中与未启动状态已说明；派发不等于研究完成。**工作原则：** map 是索引不是 store；ticket 服务于 decision；每轮调用默认处理一个非 research ticket；fog 不预切成 tickets。

## 前置条件：GitHub tracker

Tracker 固定为 GitHub Issues，通过 `gh` CLI 操作。开始前确认仓库有 GitHub 远端且 `gh` 可用（`gh repo view`）。Wayfinder 强依赖 tracker 的查询与可视化能力，**无远端时本技能不可用**：不要发明本地降级格式，改用 [`../nk-brainstorm/SKILL.md`](../nk-brainstorm/SKILL.md)（澄清目标）或 [`../nk-plan/SKILL.md`](../nk-plan/SKILL.md)（直接规划）。所需 label 不存在时用 `gh label create` 创建。Map、child tickets、blocking 与 frontier 查询的具体操作见 [`references/tracker-operations.md`](references/tracker-operations.md)。

## Plan, don't do

Wayfinder 负责探索目标与决策路径。Research、廉价 prototype 和解锁 decision 所需的 task 可以执行，正式交付统一进入 Plan → work。Map 的 Notes 记录背景和偏好，不覆盖技能职责、手动调用边界或外部操作授权。

## The Map

Map 是带 `wayfinder:map` label 的单个 issue，是 canonical artifact；tickets 是它的 child issues。Map 是 **index**，不是 store：只列已做 decisions 的一行 gist 与链接，细节只存在 ticket 一处；open tickets 不列在 map body 里，通过查询找到。**Refer by name**：每张 map 和每个 ticket 的 name 就是它的 title，所有给人看的内容都用 name 加链接引用，不单独写裸编号——一堵 `#42, #43, #44` 很难读，name 一眼能懂。

### Map body

```markdown
## Destination
<走到 map 尽头是什么样子——要找的 spec、decision 或 change。一两行；每个会话选 ticket 前先向它对齐。>

## Notes
<领域背景；每个会话应查阅的技能与资料；本 effort 的常备偏好>

## Decisions so far
- [<closed ticket title>](link) — <答案的一行 gist；细节 zoom 进 ticket 看>

## Not yet specified
<在 scope 内但还说不清的 fog；frontier 推进时升级为 ticket>

## Out of scope
<被有意识排除在 destination 之外的工作；关闭，永不升级>
```

### Tickets

每个 ticket 是 map 的 child issue；body 是一节 `## Question`，写清这个 ticket 要解决的 decision 或 investigation，大小控制在单个会话能装下。每个 ticket 带一个 `wayfinder:<type>` label；四种类型与 HITL/AFK 判定细则见 [`references/ticket-types.md`](references/ticket-types.md)。

- **Claim**：开始工作前读取归属并 assign 给自己，再核对；open 且 unassigned 才算 unclaimed。Assignee 不是原子锁，同账号多会话须明确分工，不能宣称仅凭 assign 已排除竞争。
- **Blocking**：优先用 GitHub 原生依赖关系，确认不支持才退回 body 约定。核对 blockers 的实际解决结果，不能把作废关闭当作依赖已满足；**frontier** = open + unblocked + unclaimed 的 tickets，也就是已知世界的边缘。
- 答案不写进 body，在 resolution 时以 comment 记录；解决中产生的 assets 从 issue 链接出去，不粘贴进 body。

## Fog of war 与 Out of scope

Map 是**有意**不完整的：不描绘还看不见的东西；判定与维护细则见 [`references/fog-and-scope.md`](references/fog-and-scope.md)。还说不清的问题写进 **Not yet specified**，不预切成 tickets——判定标准是"现在能不能把问题说清楚"，不是"能不能回答"。超出 destination 的工作进 **Out of scope**，永不升级；已有 ticket 被发现出界时 close 它，并在该节留一行 gist、原因与链接，不计入 Decisions so far。

## 术语与提问

HITL 对话按 [`../conventions/decision-autonomy.md`](../conventions/decision-autonomy.md) 的提问规则进行：互不依赖的问题合并一轮（至多 3 个）、选项驱动并标注推荐项；HITL ticket 的答案只能来自人类，Agent 不替人类回答。解决过程中敲定的新领域术语、或发现用词与 `CONCEPTS.md` 冲突时，按 [`../conventions/concepts-vocabulary.md`](../conventions/concepts-vocabulary.md) 当场处理并即时写入。

## 两种模式

按输入选择模式并读取 [modes.md](references/modes.md)：新目标先 chart map，已有 map 则选择、认领并处理一个 frontier ticket，记录答案后维护 map。完成本轮后汇报；用户要求继续可在同一会话开始下一轮，不强制换会话。独立 research 可批量处理。

## 收敛并交接 Plan

每轮维护后核对 destination、fog 与全部相关 tickets。Frontier 为空不等于完成：仍可能有阻塞或他人正在处理的 ticket。已关闭也不自动代表已采纳决定；区分事实、用户确认的取舍与作废项。真正阻断未解决时说明卡点，不宣称可开工。

范围足够清楚后，向 [nk-plan](../nk-plan/SKILL.md) 交接目标、范围与非目标、已定决定及理由、排除方案、成功标准、研究证据、剩余未知及 Map/ticket 链接。无需再经过 ideate 或 brainstorm。已有继续规划授权就调用公开入口；否则汇报已可规划并停止。没有可调用入口时提供同样的交接材料，不冒充已生成 Plan。

由 nk-plan 整理 Product Contract 并交付统一规格的可实施 Plan；软件 Plan 使用 `nk-plan/v1` 与 `product_contract_source: nk-plan`，复用已定决定，只补缺口。非软件任务遵循 nk-plan 对应路线。Map 保留为探索依据，不充当实施容器；Plan 交付后在 Map 记录路径与提交等可追溯位置、交接范围和残留，不把探索完成称为实施完成。只有完整 Plan 且已有实施授权才进入 nk-work，不从 ticket 直接跳入实施。

## 与体系衔接

- ticket 解决中沉淀出非显而易见的经验或决策理由 → [`../nk-compound/SKILL.md`](../nk-compound/SKILL.md)。
- 结束时汇报现场，不自动调用 nk-handoff 或维护 current。HITL ticket 无人响应时保留未解决状态、记录卡点；本轮无法继续且无保留认领约定时释放自己的 claim。涉及合格仓库产物提交时交给 nk-commit，由其维护 current。
