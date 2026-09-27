# CONCEPTS.md — NexusKit 领域术语表

## 收尾与发布

### 分支收尾
工作分支合并进 main 前的六步闭环（转移遗留、提炼、删除已交付工件、覆写 current.md、单次收尾提交、可选 PR 摘要），由 `nk-close` 承载，规则全文在 `skills/conventions/artifact-lifecycle.md` 第五章。收尾锚定在分支生命周期而非版本发布；分支不对应发布版本。
*Avoid: 版本收尾*

### 发布日扫尾
在 main 上打 tag 发布时的轻量动作：漏网检查 + release notes + 打 tag，不做提炼与删除（那是分支收尾的职责）。发现漏网项时不带病发布。单分支项目中与任何 plan 无关的产物（如未消费的发想记录）由发布日扫尾兜底。

### 降级路径
单分支项目（不使用工作分支）的收尾触发方式：某 plan 全部实施单元交付后，对该 plan 及其关联产物跑一次小范围分支收尾。它是单分支工作流的兜底规则，不是对在 main 上做 plan 级开发的鼓励。

## Issue 生命周期

### 容器中立认领
Issue 在被纳入任何工作容器的时刻即被认领——`nk-brainstorm` 把它作为需求来源、`nk-plan` 把它纳入范围、`nk-work` 直接认领，三条路径同一机制（设 assignee + 评论指向承载产物）。认领后决定不做须退回：取消 assignee 并评论说明，Issue 保持 open。规则全文在 `skills/conventions/issue-writing.md` 第三节。

## 盘问

### 前沿轮次
`nk-grill` 的提问组织方式：把主题映射为设计树（每个决策分叉出挂在它下面的子决策），每轮问完**前沿**——前提已全部敲定、现在就能问的决策集合；每问带推荐答案，答完重算前沿再开下一轮。用户主动召唤场景，不适用 decision-autonomy 的单轮 3 问上限。
