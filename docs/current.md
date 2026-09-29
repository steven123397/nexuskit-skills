# 当前状态

- 所在分支：`feat/skill-deep-audit`；核对基点：`3f1cb55`（2026-09-29 本轮整理时 HEAD）。
- 工作范围：[技能深读计划](plans/2026-09-27-1525-test-skill-deep-audit-plan.md) U2。前十一项已交付；本次为 nk-compound，下一项为 nk-close。
- 本次成果：compound 保留沉淀 / 审计双模式，新增条件性协作复盘；入口持有路由、授权、术语、可见性、最终两项自检与提交。work / debug 默认建议、授权后调用，成果返回统一提交。
- 共享规则：决策与实践分开准入，stale 不覆盖决策生命周期；空库不阻塞术语初建。补齐经验消费契约：项目入口标明检索时机，work / debug 复用或补查，子代理交接携带原始来源及任务影响；init / close 的最小入口维护同步，主体重构仍待后续。
- 验证：`python -B -X utf8 tests/run_checks.py` 五项通过；`python -B -X utf8 -m unittest discover -s tests -p test_*.py` 14 项通过；四个改动入口 PyYAML 解析通过；`git diff --check` 通过。主会话已核对方法保留、调用关系、经验消费与 Issue 范围，未执行受测技能。

## 接手依据与边界

先读 [组织范式](solutions/architecture-decisions/2026-09-28-skill-execution-locality.md)、Plan 的逐技能顺序及联合设计，按需读 [来源与取舍](skill-sources.md)。当前技能与用户后续决定优先于历史来源描述。

- 主流程直接写执行顺序；阶段材料连续可读，条件分支返回入口，共享方法按需复用。精简不删质量要求，不以文件数或字节减少证明实际收益。
- review/debug 主要采用 CE 方法；review 与 simplify 均产分析结果，review 主会话直接派精简叶子与风险 reviewer，再由独立 validator 复核，不引入管理代理层。
- work 修复查证成立的单元内问题，范围外阻断交给用户；debug 修复查证成立的问题。修后针对性验证与复核，复用有效证据。
- ideate、brainstorm、plan 保留无子代理时的内联路径，不把内联称为独立核实。grill 仅由用户主动召唤；共识不等于写入、规划或实施授权。
- 所有提交经 nk-commit，current 随完整交付按需一起维护；同一交付遗漏补记按 R3 核实后 amend。handoff 仅显式调用。ideate 不自动提交或维护 current；合格需求/实施 Plan 交给 nk-commit，实施仍须授权。

## 阻断与已知缺口

无编辑阻断。全部技能重构后才由用户统一安排独立会话沙盒实测，本会话不执行受测技能。提交钩子同步、机械检查和 Issue 关闭均不代表行为验证。

本轮 #15 已按文本修复关闭，前十一项无未关闭的节点关联问题；真实效果仍纳入 U3。#2 的客户端语言实验保留。历史 Issue 处置见 Plan，#21 不新增 reference 总量硬阈值，#40 保持否决。

PyYAML 已可用；全仓 frontmatter 检查仍为基础检查，真正解析由 #13 跟踪。外部 quick_validate 字段限制按 AGENTS.md 处理，不改有效字段或外部安装文件。

## 下一步

继续上述 Plan 的 U2，下一项 nk-close：读实际入口、引用和来源，讨论收尾结构及 compound 公共接口，核对 #16、#18。全部技能完成后进入 U3。

## 工作区未提交改动

本轮技能、共享规范、来源、检查登记、Plan 与 current 一起提交，预期无本轮残留；不自动推送。
