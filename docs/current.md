# 当前状态

- 所在分支：`codex/nexuskit-v0.3.0`；核对基点：`05a2941`。
- 正式版仍为 [v0.2.0](releases/v0.2.0.md)，尚未推送或发布本轮重写。
- 本轮按 [STE-16](https://linear.app/steven-liang/issue/STE-16) 已确认的轻量架构逐技能重写；当前处理 [STE-11](https://linear.app/steven-liang/issue/STE-11)。Matt 相近内容按原文结构译成中文，description 保持英文；逐技能汇报直接迁移与补充内容，完成一个后停下等维护者审阅。
- `nk-grill` 已按 Matt grilling 重写，补充实际用法澄清与无子代理时自行查证；来源见 [技能来源](skill-sources.md)。
- 验证：`python tests/run_checks.py` 五项全绿；`git diff --check` 通过。仅确认机械检查与原文对照，不代表客户端实跑。

## 阻断与已知缺口

- STE-11 其余技能尚未重写，新旧流程仍处于迁移中。
- 新架构将取消 current 与集中 conventions 运行依赖；本文件暂按仓库现行维护规则保留，不作为新版技能的运行依赖。
- 旧 [验证记录](reviews/feat-skill-deep-audit.md) 仅证明 v0.2.0 的既有覆盖，不外推到本轮。旧 solutions 在 STE-13 完成迁移与验证前保留。

## 下一步

等待维护者审阅 `nk-grill`；确认后继续 STE-11 的下一份技能。

## 工作区未提交改动

原有 `tests/__pycache__/` 未跟踪缓存保留，不纳入提交。
