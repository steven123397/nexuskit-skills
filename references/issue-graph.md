# Issue Graph（issue 图结构）

一个 plan 落到 issue tracker 时，怎么建层级、怎么连边。以 beads 为基线（它的层级与关联最完整），Linear / GitHub Issues 按末尾的映射表使用。

## 为什么需要规则

没有约定时，图很常见地会变成这样：主 epic 直属几十张子票，层级深度只有两三层；phase 只用 label 表达；checkpoint 同时被当成门和容器；review 修复散落在多个不同挂载点；还有一批票没有父节点。图建得出来，但读不出计划。

四个根因：用 label 表达阶段、容器与 gate 混用、review 没有固定挂载点、新发现的工作没有默认归属。

## 层级模型

```text
Root epic（一个 plan / 一个版本）
├── Phase epic（阶段）
│   ├── Workstream epic（可选；子票超过约 10 张时）
│   │   └── Task（可执行切片）
│   ├── Checkpoint task（gate，叶子）
│   └── Review epic / task（挂在被审的层级）
│       └── Finding / fix
└── Program epic（跨 phase 的横切工作）
```

| 层级 | 类型 | 职责 |
|---|---|---|
| Root epic | epic | 一个 plan 的整体目标与验收 |
| Phase epic | epic | 一个阶段的容器，承载该阶段全部工作 |
| Workstream epic | epic | 可选；阶段内按模块或职责再分一层 |
| Task | task / bug / feature / chore | 可独立交付、可独立验证的切片 |
| Checkpoint | task | 叶子 gate，用 `blocks` 依赖本 phase 全部工作流 |
| Review | epic 或 task | 审查容器，挂在被审的 phase / workstream 下 |
| Finding / fix | task / bug | review 的发现，挂在该 review 下 |

## 规则

1. **一个 plan 一个 root epic。** root 下只放 phase epic 和 program epic，不放执行任务。
2. **phase 必须是 issue，不能只是 label。** `phase-N` label 只用于筛选，不承担层级。
3. **容器和 gate 分开。** phase 是容器；checkpoint 是 phase 下的叶子任务，用 `blocks` 依赖本 phase 的全部工作流，绝不当父节点。
4. **容器子票上限约 10 张。** 超过就加 workstream 层，否则 phase 会变成新的 51 张。
5. **review 是挂在被审层级的一等 issue。** phase 审查挂 phase 下，workstream 审查挂 workstream 下，横切审查挂对应 program epic。finding 是 review 的子票，不要直接挂 checkpoint 或 phase。
6. **phase 关闭条件。** checkpoint 通过，且 review 的所有 finding 已关闭或明确 defer（写明理由）。review issue 的验收标准必须包含这一条。
7. **除 root epic 外，每张票必须有父。** 不允许 root 级散票。新发现的工作默认挂当前 phase 的 review，或挂对应的 program epic。
8. **parent-child 表达「组成」，blocks 表达「先后」。** 不要用父子关系表达顺序。典型顺序边：phase 内任务 → checkpoint → 下一 phase；review findings → phase 关闭。
9. **横切工作单独建 program epic。** 视觉打磨、性能 / CI、发布收口、文档、专项简化等挂 root epic 下，不散成 root。
10. **一票是一个可执行批次，不是一条 finding。** file:line 留在 review 报告里，确认后再建执行票。
11. **按风险分档，一票只做一档：**
    - **A 档：** 纯去重或降复杂度，不改行为、不改契约，可直接执行；
    - **B 档：** 改行为或数据契约，先写 ADR、Ask-first，再执行；
    - **C 档：** 低收益 backlog，不承诺本轮交付。
12. **不静默丢 finding。** 不修的 finding 必须在 review issue 里记录理由和后续去向，遵守 CONSTRAINTS 的「不静默降级」。

## 命名与 label

- `Phase N: <name>` + label `phase-N`
- `Checkpoint N: <name>` + label `checkpoint`
- `Review: Phase N <scope>` + label `review`
- review finding + label `review-fix`
- 横切容器：`Program: <name>`

label 名称可按项目调整；层级不依赖 label。

## 建图流程

1. 写 plan，建 root epic。
2. 按阶段建 phase epic，每个 phase 建一张 checkpoint 叶子，连好 `blocks` 边。
3. 评估子票数量：超过约 10 张就建 workstream epic。
4. 建执行任务，全部挂到 workstream 或 phase 下；触发审查时在被审层级建 review issue，发现的问题作为 review 子票。
5. checkpoint 通过且 finding 关闭或 defer 后关闭 phase epic；横切工作建 program epic，不属于当前 phase 的新发现挂 program，不留在 root。

## 建票前检查清单

- [ ] 这张票有父吗？（root epic 除外）
- [ ] 它是容器还是叶子？容器是否 ≤10 张子票？
- [ ] phase 是否已经是真实 issue，而不是只有 label？
- [ ] checkpoint 是否被当成了父节点？（不应）
- [ ] 如果是 review，是否挂在被审的层级？
- [ ] finding 是否挂在 review 下，而不是 checkpoint 或 phase 下？
- [ ] 顺序关系是否用 `blocks` 表达，而不是 parent-child？
- [ ] 这张票是不是一个可执行批次，而不是一条微发现？
- [ ] 是否只属于 A/B/C 中的一档？B 档是否已登记 ADR / Ask-first？
- [ ] 不修的 finding 是否记录了理由？

## 映射到其他 tracker

| 概念 | beads | Linear | GitHub Issues |
|---|---|---|---|
| root / phase / workstream | epic | parent issue 或 Project | parent issue |
| 组成关系 | parent-child | parent issue | sub-issue |
| 先后关系 | `blocks` 依赖 | blocked-by 关系 | issue dependency（blocked by） |
| 筛选 | label | label | label |
| checkpoint gate | task + `blocks` | task + blocked-by | task + dependency |

层级较弱的 tracker 至少要保住两条：每张票有父，顺序用依赖而不是父子表达。

## 迁移

已有图不批量重写。只给无父的 root 票和错挂的 review 票补父节点，新规则从下一个 plan 起严格执行。