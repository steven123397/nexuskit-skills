# 当前状态

- 所在分支：`feat/skill-deep-audit`；核对基点：`d643287`（2026-09-29 交接时 HEAD）。
- 工作范围：[技能深读计划](plans/2026-09-27-1525-test-skill-deep-audit-plan.md) U2；下一项为 nk-plan。
- 已提交：nk-work 范式、nk-commit 统一入口与 current 归属、nk-handoff 显式调用边界。
- 本次交付：nk-debug 阶段重构、simplify/review 联合重构、work/debug 审查接入、全技能路径声明与链接清理、Issue 核对及 Plan 分区；随本次交接入库。
- 验证：最近一次 `python -B -X utf8 tests/run_checks.py` 五项与 `git diff --check` 通过；review/simplify 经 PyYAML 解析及必要字段核对通过。此后仅整理交接文档，未重复跑技能测试。

## 接手必读与重构理念

先读 [组织范式](solutions/architecture-decisions/2026-09-28-skill-execution-locality.md)、上述 Plan 的逐技能任务与联合设计，再按需读 [来源与取舍](skill-sources.md) 对应章节。当前技能与用户后续决定优先于历史来源描述。

- 主流程直接写执行顺序；同阶段必需方法集中成完整材料，条件分支按需读完返回，不递归拼装。共享源单处维护，短底线可受控复制；跨技能通过公开入口。精简不等于删质量要求，也不照搬 work 的文件数量。
- 保留具体方法、证据与真实行为边界，避免繁琐仪式、重复确认、重复读取和重复验证；非代码路径不额外堆规则。引用写实际 Markdown 链接，已删除反复出现的路径解析声明，不恢复。
- review/debug 主要采用 CE 的流程与方法；Ponytail 只借鉴减少自维护复杂度和复用原生能力，不追求删行数。review 不采用 Matt 的规范/意图双轴；这不否定其他技能适用的 Matt 方法。
- review 手动或嵌入均只产报告；simplify 独立调用由用户明确发起，只分析，获授权才修。review 复用其分析能力并传入已定范围；主会话直接派三个精简叶子代理与风险 reviewer 并行，容量不足分批，无管理代理层。两者分析必须派子代理，无能力就明确未完成；review 独立 validator 复核后统一报告。
- work 调用 review 后直接修复查证成立的单元内问题；超出单元则阻断，由用户决定 Issue、handoff 等后续。debug 直接修复查证成立的问题。修后针对性验证与复核，复用仍有效证据。review/simplify 不自动提交。
- 所有提交经 nk-commit，提交前按需更新 current；plan 落成须提交，ideate 不自动提交。handoff 仅用户显式调用，不猜措辞、不自动触发。受阻无提交时不强制更新 current；#40 为用户否决的误判。

## 阻断与已知缺口

无编辑阻断。全部技能重构完毕后才由用户统一安排独立会话沙盒实测，本会话不执行受测技能；静态审查、机械检查和提交同步均不等于运行验证。Issue 关闭也不代表实跑通过。

PyYAML 已安装；外部 quick_validate 的字段白名单不接受 argument-hint / disable-model-invocation，勿为此删除字段或改外部安装文件。处理边界见 [AGENTS.md](../AGENTS.md)；仓库真正 YAML 解析仍由 #13 跟踪。

## 下一步

继续上述 Plan 的 U2，从 `skills/nk-plan/SKILL.md` 及 references 开始：读取实际内容与对应 CE 来源，先与用户讨论结构和取舍，再改写；只读核对表内开放 Issue，别重开已关闭项。用户下一会话继续逐技能重构，不自动扩至其余技能。所有技能完成后进入 U3。

## 交接范围与残留

本轮已知技能、约定、入口文档、Plan、来源说明和本交接记录一起入库，无计划暂留文件。其他技能多数仅做路径说明删除/链接修正，不代表主体重构完成；debug 的 anti-patterns.md 已合并删除，simplify 的显式调用策略已新增。用户已明确授权此次 handoff 提交，先前“暂不提交”限制已解除；不自动推送。提交钩子的沙盒同步不代表技能实测。
