# 技能目录与加载边界

采用 Matt Pocock 式轻量组织：`skills/engineering/` 放工程技能，`skills/productivity/` 放协作工具。每个技能的完整主流程在自己的 `SKILL.md`，其他材料按实际用途就近组织。

这样可以先稳定目录、技能边界和分发方式，再逐个讨论正文，避免为了保留旧 conventions 而反复增加适配。跨技能使用公开入口，不互读私有材料；不统一规定 references 层或文件数量。

待重写旧稿以 `SKILL.legacy.md` 保留在目标技能目录，新增能力仅预留目录。只有实际 `SKILL.md` 参与技能发现和运行检查。旧稿中的方法与链接属于历史版本，重写时按新职责判断是否采用，不要求继续运行旧流程。

已取消的 brainstorm、ideate、plan、work、handoff、compound、close、simplify 入口以及集中 conventions 从技能树移除；原始材料可从 Git 历史查阅。旧 solutions 单独迁移，核对来源和目标可用性后再清理。

仓库文档保存术语、关键决定、来源与必要说明。Linear 管内部需求和状态，GitHub Issues 管外部反馈，OpenViking 管背景和经验，Git/PR 管交付事实，不再维护实时状态文档。

spec 与分支生命周期独立。spec 整体验收通过即可关闭；PR 负责分支交付收尾，复用有效验收。分支可没有 spec，但不直接修改主分支。

设计依据：[STE-16](https://linear.app/steven-liang/issue/STE-16)。技能正文随对应实施票逐项完善。分发形态与布局事实见 [ADR-0001](0001-distribution-layout.md)。
