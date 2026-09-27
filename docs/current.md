# 当前状态

- **所在分支**：`feat/skill-deep-audit`（技能深读审计轮，plan 已就位）
- **HEAD**：`425e670`（v0.1.1 发布提交；本文件随其后的规划提交入库）
- **版本/里程碑**：v0.1.1 已发布（2026-09-27，Issue 生命周期迭代，release notes 见 [`releases/v0.1.1.md`](releases/v0.1.1.md)）。版本规则：v1.0.0 前均为试用版；大迭代走 minor，小迭代走 patch。发布与收尾已解耦——收尾锚定分支生命周期，发布是 main 上打 tag + release notes 的纯事件。
- **已具备能力**：18 个 `nk-*` 技能 + 共享约定 `skills/conventions/`（选用见 [`../README.md`](../README.md) 路由表）；三形态分发——Kimi 插件、Codex 插件、npx skills CLI；五项机械检查 + 双平台 CI。本次迭代新增/变更：
  - `nk-grill`：手动触发的盘问微技能（豁免单轮 3 问上限，理由见其正文与 `docs/skill-sources.md`）；
  - Issue 全生命周期规则成文于 `skills/conventions/issue-writing.md`（标签最小化、容器中立认领、三个关闭时机、可选完成定义）；
  - 收尾锚定分支生命周期（`nk-close` 两种触发 + 发布日扫尾；R6 降级路径保留）；
  - PR 描述规范 `skills/nk-close/references/pr-description.md`（`Fixes #N` 闭环接入 Issue 生命周期）；
  - Kimi 插件清单迁至 `.kimi-plugin/plugin.json`（目录形态，与 `.codex-plugin/` 对齐）；
  - 新建 `CONCEPTS.md` 术语表并挂入 `AGENTS.md` 知识入口。
- **加载模型**：本仓库是半成品工作区，客户端消费发布快照；细节见 `AGENTS.md`。
- **验证结果**：
  - `python tests/run_checks.py` 五项全绿（每个交付提交均复跑）；PR #7 双平台 CI 通过。
  - `npx skills@1.5.23 add <本仓库> --list` 发现列表含 18 个 nk-* 技能（含 nk-grill）与 conventions。
  - Issue #4、#5、#6 已带提交哈希评论关闭。
  - Kimi 本地路径重装实装 ✅：`.kimi-plugin/plugin.json` 目录形态识别正常，`/nk-grill` 已在可调用列表。
  - 安装实装四通道全绿：Kimi 本地路径 ✅、Kimi GitHub ✅、Codex marketplace（自更新跟随 main）✅、npx `--list` ✅。
  - 新版 `nk-close` 在上一分支完成首次真实收尾，发现的 5 处摩擦已修复（`a7199ad`）。
  - 未验证：真实项目端到端使用（paper-30min 迁移验收，排在技能审计轮之后）。

## 阻断与已知缺口

- [Issue #1](https://github.com/steven123397/nexuskit-skills/issues/1)：提示词副本终局——触发时机为"首次需要跨副本同步修订"，很可能在审计轮中出现。
- [Issue #2](https://github.com/steven123397/nexuskit-skills/issues/2)：中文 description 触发可靠性——审计轮逐技能实跑时顺带收集案例。
- [Issue #3](https://github.com/steven123397/nexuskit-skills/issues/3)：增强泊车场（未拍板，随时可逐项处理）。

## 下一步

- [ ] **技能深读审计轮**（新会话进行）：plan 在 [`plans/2026-09-27-1525-test-skill-deep-audit-plan.md`](plans/2026-09-27-1525-test-skill-deep-audit-plan.md)，从 U1（沙盒脚手架）开始；阅读与实跑顺序见 plan 附录 A。
- [ ] 审计结论汇总后，用户口述 v0.2.0 的更大安排。
- [ ] paper-30min 迁移验收（审计轮之后）。
