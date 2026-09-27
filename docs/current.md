# 当前状态

- **所在分支**：`main`
- **HEAD**：`c5392f6`（Issue 生命周期迭代已合并入库，PR [#7](https://github.com/steven123397/nexuskit-skills/pull/7)，双平台 CI 通过）
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
  - 新版 `nk-close` 在上一分支完成首次真实收尾，发现的 5 处摩擦已修复（`a7199ad`）。
  - 未验证：Codex / WSL Kimi 的 GitHub 安装路径（合并后用户实测）；真实项目端到端使用（paper-30min 迁移验收，v0.2.0 目标）。

## 阻断与已知缺口

- [Issue #1](https://github.com/steven123397/nexuskit-skills/issues/1)：提示词副本终局——触发时机为"首次需要跨副本同步修订"。
- [Issue #2](https://github.com/steven123397/nexuskit-skills/issues/2)：中文 description 触发可靠性（v1.1.0）。
- [Issue #3](https://github.com/steven123397/nexuskit-skills/issues/3)：增强泊车场（未拍板，随时可逐项处理）。

## 下一步

- [ ] 用户在 Codex 与 WSL Kimi 侧通过 GitHub 安装实测（main 已含本次迭代）。
- [ ] 日常使用中观察各客户端触发情况，案例喂给 Issue #2。
- [ ] paper-30min 迁移验收（v0.2.0 目标），实战检验分支收尾规则。
