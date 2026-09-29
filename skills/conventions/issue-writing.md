# Issue 生命周期与写作规范 (Issue Writing)

> **定位：** Issue 全生命周期规则的唯一持有者：去向、标签、认领、关闭时机、写作格式。Issue 是跨 plan 事务的载体（D5），它可能在 backlog 里躺上数周，然后被一个毫无现场上下文的 Agent 或会话认领（[nk-work](../nk-work/SKILL.md) 的合法输入之一）——写作质量直接决定接手质量。
> **生产者与消费者：** [nk-to-issue](../nk-to-issue/SKILL.md) 负责核实、查重与落档；work / debug / close 决定分流并传入已有证据及落档授权，review 只返回发现而不自行建票。brainstorm / plan / work 是认领方；wayfinder 的专用格式见第七节。各技能引用本规范，不另造字段或生命周期；分流时机见 [artifact-lifecycle.md](artifact-lifecycle.md) 第四章。

---

## 一、去向

1. **有 GitHub 远端**：用 `gh issue create` 落档，标题与正文按本规范。
2. **无远端**：写入 `docs/backlog.md`，每条一个条目，格式与 Issue 正文同构；文件改动不单独提交，随下一次相关交付或用户显式调用 nk-handoff 时的现场保存入库（[nk-commit](../nk-commit/SKILL.md) R2/R4）。无远端时第三、四节的 assignee 与评论机制不适用，认领与关闭只在 `docs/current.md` 登记。

## 二、标签约定

1. 只用 GitHub 默认标签表达类型（`bug` / `enhancement`）。
2. **不设状态标签**（如 in-progress、ready）：状态由 Issue 的 open/closed 与 `docs/current.md` 承载，多一处真相必然漂移。
3. 唯一例外：[nk-wayfinder](../nk-wayfinder/SKILL.md) 的 `wayfinder:*` 前缀标签，其 map / decision ticket 机制依赖它（见第七节）。

## 三、认领

认领发生在 Issue 被纳入任何工作容器的时刻。三条路径做同两件事：**设 assignee**（`gh issue edit <N> --add-assignee @me`）+ **在 Issue 下评论指向承载它的产物**（plan 文件路径，或注明由 [nk-work](../nk-work/SKILL.md) 直接认领）。

- **[nk-brainstorm](../nk-brainstorm/SKILL.md)**：把 Issue 作为需求来源时认领。
- **[nk-plan](../nk-plan/SKILL.md)**：把既有 Issue 纳入 plan 范围的那一刻认领；对应单元交付后按第四节关闭。
- **[nk-work](../nk-work/SKILL.md)**：直接认领时除上述两件事外，还在 `docs/current.md` 登记——这是写文件，不是单独提交，由 [nk-commit](../nk-commit/SKILL.md) 在提交前核对并与交付入库；没有交付时暂留，用户显式保存现场时按 R4 处理。

**路由判断**：需求类 Issue 未澄清范围与成功标准时先经 [nk-brainstorm](../nk-brainstorm/SKILL.md)；已写清行为与完成定义的可直接进 [nk-plan](../nk-plan/SKILL.md) 或 [nk-work](../nk-work/SKILL.md)。

**退回**：认领后决定不做（如 brainstorm 否决了方向）时，取消 assignee 并评论说明原因，Issue 保持 open。

## 四、关闭时机

三个合法时机，先到先得：

1. **[nk-work](../nk-work/SKILL.md) 单元交付**：提交覆盖该 Issue 时关闭，评论注明单元编号与提交哈希。
2. **PR 合并**：PR 描述中写 `Fixes #N`，合并时自动关闭（需要描述时经 [nk-close](../nk-close/SKILL.md) 的可选 PR 描述入口处理）。
3. **[nk-close](../nk-close/SKILL.md) 兜底扫描**：分支收尾时扫描本分支引用过而未关闭的 Issue，逐条处理（评论关闭或说明遗留原因）。

## 五、写作四原则（吸收自 Matt `AGENT-BRIEF`）

1. **持久性优于精确**：Issue 落档后代码会继续演化。定位用接口、类型、行为契约的名字，**不引用文件路径和行号**——它们会过期（这与 `docs/reviews/` 里的短期审查条目相反，后者用 `file:line` 是因为活不过一个版本）。
2. **行为而非步骤**：描述系统应该做什么，不写实现步骤。接手的 Agent 会重新探索代码库并自行决定实现方式。
3. **完成定义可独立验证**：若提供完成定义，每条单独可测，让接手者知道什么时候算完成。
4. **范围边界明确**：写清不做什么，防止接手者镀金或误伤相邻功能。

## 六、条目格式

```markdown
**Category**：bug / enhancement

**Current behavior**：（现状；bug 写损坏的行为，enhancement 写现状基础）

**Desired behavior**：（完成后的预期行为，含边界与错误情况）

**Key interfaces**：（涉及的接口/类型/配置形状及需要的改变；不知道就省略本节）

**Done definition**（可选）：每条可独立验证，纯文本 bullet，不用 checkbox。

**Out of scope**：（明确排除的相邻工作）

**Evidence**（bug 必填）：核实结论（已确认 / 未能复现）、复现步骤、脱敏后的报错摘要。
未能复现时写明还缺什么信息。

**Source**：（一行溯源：来自哪个 plan / 审查条目编号 / 会话，及日期）
```

小节标题用英文锚点；正文语言随项目惯例。构想/需求描述类 Issue 整体豁免 Done definition 小节。琐碎小项（一句话能说清的待办）可以只写标题加一句 Desired behavior，不强套全格式。

## 七、例外

[nk-wayfinder](../nk-wayfinder/SKILL.md) 的 map 与 decision ticket 有自己的专用格式（Destination / Question / Decisions so far）与 `wayfinder:*` 标签，由该技能自行定义，不适用本规范。
