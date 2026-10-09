---
name: nk-spec-close
description: "Accept and close a spec: read the spec, its tickets, and the delivered work; verify complete usage scenarios and cross-ticket integration, reusing valid evidence and re-checking only what later changes affected. Dispatches nk-review for code-level review of the integration scope; returns satisfied, missing, and unverified parts to the implementer. Closes the Linear spec on acceptance without waiting for PR merge, then cleans up temporary worktrees this spec no longer needs."
argument-hint: "[spec 的 Linear URL 或编号]"
disable-model-invocation: true
---

验收并关闭一份 spec：读取 spec 与实际交付，检查完整使用场景与跨 ticket 整合，处理缺口。审查方法归 `nk-review`，本技能组织整合视角、持有 spec 的关闭。用户可直接调用；`nk-odyssey` 在 tickets 整合完成后调用，PR 收尾按需补充调用。验收通过即关闭 Linear spec，不等待 PR 合并；本技能不合并 PR、不实施修复。

## 读取 spec 与交付

1. 读 spec 正文与全部 tickets：交付内容、验收条件、状态与关联提交。ticket 未完成时如实报告，验收停在缺口，不给部分通过的结论；实际范围与 spec 不一致的调整要有记录，未记录的按遗漏处理。
2. 收集已有验证结论：各 ticket 的验证证据、单元审查结论与测试结果。仍对应当前交付的证据直接复用；后续改动只重查受影响部分，不重跑已覆盖且未受影响的验证。
3. 核对实际交付所在分支与提交。验收对照 spec 负责；分支内 spec 之外的补充工作不在本验收范围，由 PR 交付时的审查覆盖。

## 整体验收

- 沿 spec 的**使用场景与预期行为**走完整使用场景：真实用户流程从头到尾，不是对验收条件清单打勾。
- **跨 ticket 衔接**：单元间接口、状态与数据流是否真正接通；组合是否遗漏——迁移与启动接线、旧入口、发布配置、文档契约。
- **遗漏与误解**：spec 要求但缺失或只做一半的；实现偏离已定决定的；混入"不在范围内"边界的。
- 需要代码层面的审查时调用 `nk-review`，传入整合范围（跨 ticket 组合、累计影响、完整用户流程）与已有单元结论；它复用未受影响的结论，只补查受影响部分，spec-close 不复制审查方法。
- 按 spec 的测试决定补做必要的整体验证：完整场景对应的测试与检查实际运行，无法运行的写清未验证项，不把单元通过记为整体通过。
- 验收中的小核对自行完成；发现的问题**不自行修复**——缺口交回实施方处理。

## 出口

- **通过**：全部验收条件已满足（含已记录的范围调整），证据完整。把 Linear spec 置为 Done——ticket 已由各自实施关闭，这里不重复。汇报已满足项、复用的证据与补做的验证。
- **未通过**：明确未完成内容，区分**已满足 / 未满足 / 未验证**三部分，交实施方处理缺口；spec 保持 open。缺口归属已有 ticket 的记回对应 ticket，遗漏的新工作由调用方决定是否开票。
- 验收结论随调用方的交付载体（汇报、提交说明、PR）保留，能识别 spec 与交付版本即可，不建验收台账。

## 清理临时工作树

验收通过后，清理本 spec 已不再需要的临时工作树：先 `git worktree list` 查现状；逐个确认成果已承接（已合入集成分支或交付物已保存）、无活跃使用者、未提交与忽略文件无遗漏；未承接内容保留并说明。宿主管理的工作树走宿主入口——Orca 工作树按 `nk-orca-guide` 的删除与清理（先关终端再 `worktree rm`）；普通工作树用 `git worktree remove`；不删除原工作目录、仍在使用的分支或其他任务资源，不建台账。PR 收尾的剩余交付资源清理归 `nk-pr`。
