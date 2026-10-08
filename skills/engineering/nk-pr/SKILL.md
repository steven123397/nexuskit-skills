---
name: nk-pr
description: "Deliver a work branch through a PR: create the draft PR after the first real delivery commit, keep it updated, confirm review and merge conditions, merge under explicit authorization, and clean up delivery resources. Review method belongs to nk-review and spec acceptance to nk-spec-close; this skill reuses their conclusions and only fills gaps. A branch may have no spec at all."
argument-hint: "[可选：PR 编号/URL 或分支名；默认当前分支]"
disable-model-invocation: true
---

把工作分支交付为 PR：创建与更新、审查与验收状态衔接、合并条件确认、授权合并与合并后清理。审查方法归 `nk-review`，spec 整体验收归 `nk-spec-close`——本技能复用两者的结论、只补缺口，不复制它们的方法。spec 与分支独立：分支可以完全没有 spec（仅解决外部 Issue），无 spec 不阻碍 PR 交付。分支行为由使用者决定，禁止在主分支上直接改动或提交。

## 创建与更新

- 分支上有**第一份实际交付提交**后创建 draft PR，不是骨架或占位提交。目标分支按项目工作流文档或用户指示，默认主分支。后续交付继续推到分支并更新 PR，不重复创建。
- PR 描述写 **diff 看不出来的东西**：什么从不可能变成可能、什么从坏变好——读者能从 diff 自己重建的句子一句不写。长度随**决策成本**伸缩，不随 diff 行数：小改动一两句话；中大型开头一两句自含完整想法，每个小节回答一个评审者无法从 diff 得到的疑问。验证写实际跑过的命令与结果，不写"tests passed"空话；残余不确定性如实写，蓄意推迟的范围一句话声明。
- 描述可用一个最小视图讲清要点——伪代码、调用树、文件树或 diff——按话题选形；验证证据给前后对比。破坏性或难以逆转的改动标明**单向门**与波及面，便宜的回滚是低风险。
- 项目自己的 PR 模板与贡献约定永远赢过本节的写法建议。
- 关联事项用准确语义：真正完整解决的写关闭语义（`Fixes`/`Closes`），相关的用 `Related`，不确定按不关闭处理。spec 的关闭走 `nk-spec-close`、tickets 走各自实施，**不因合并批量关闭关联事项**。

## 转正与合并条件

draft 转 ready 前确认：

- 审查覆盖**整个分支的实际交付**，包括 spec 之外的补充工作与临时纳入的修复。已有单元与整合审查结论仍适用的直接复用；新增提交、冲突解决或目标分支变化只补查受影响部分——按 `nk-review` 的复用规则，需要时按 PR 范围调用它。
- 有 spec 时：整体验收结论已由 `nk-spec-close` 给出（它不等合并即关票）；结论缺失或后续改动使其失效时补调用一次。spec 以使用场景和整体用途验收，不是数已完成的 tickets。
- CI 与项目要求的合并条件满足，冲突已解决。
- **满足检查条件不推导合并许可**：合并按用户或项目授权执行。未获授权时停在 ready 并报告状态，不自动合并。

## 合并与清理

- 明确授权后按项目约定的方式（merge/squash/rebase）执行合并。合并动作本身走远端操作，不重写已共享的历史。
- 清理本分支交付后剩余且可安全清理的资源，**不强制等待合并**才清理已用完的临时工作树：`git worktree list` 查现状，确认成果已承接、无活跃使用者、未提交与忽略文件无遗漏；宿主管理的工作树走宿主入口，普通工作树用 `git worktree remove`。保留未交付内容；不删除原工作目录、仍在使用的分支或其他任务资源。
- 合并后的分支删除与产物处置按授权与项目约定执行，不自动删。不产生独立的规划或审查文档收尾流程——审查与验收结论已随交付载体保留。

收尾汇报：PR 状态与链接、复用的结论与补查的部分、合并状态、清理了什么、保留了什么及原因。
