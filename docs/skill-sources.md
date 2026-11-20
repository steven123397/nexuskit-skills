# 技能来源映射

维护者向索引：记录 NexusKit 各部分的上游来源与本地改动。执行技能的 Agent 不需要读本文件。

## 上游与同步点

- 技能主体：[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)，同步点 `8c99fa3`（v0.6.17）；基于 v0.6.13 基底持续回填 v0.6.14–v0.6.17 的可翻译内容（见下；docs、evals、hooks、仓库级 scripts 不在 vendor 范围）。
- 早期简体中文译本：[vinvcn/addyosmani-agent-skills-zh](https://github.com/vinvcn/addyosmani-agent-skills-zh)（本地副本 `.upstream/addyosmani-agent-skills-zh`，已停更；已 gitignore，不随包分发）。现以 `.upstream/addyosmani-agent-skills` 直接对照英文上游，术语与翻译规范见 [glossary.md](glossary.md)。
- 引入方式：vendor，小修小补；技能名、目录名与 H1 保持上游原样。逐技能的本地改动按本文件的来源分类与说明记录，历史审阅过程可从 Git 历史核对。
- 归属与许可证见 [NOTICE](../NOTICE) 与 [LICENSE.upstream](../LICENSE.upstream)。

## Skills

26 个技能位于 `skills/<name>/SKILL.md`，与上游同名同路径。来源按以下几类记录：

- **无额外行为改写**：`using-agent-skills`、`accessibility-engineering`、`api-and-interface-design`、`browser-testing-with-devtools`、`frontend-ui-engineering`、`git-workflow-and-versioning`、`interview-me`、`observability-and-instrumentation`、`shipping-and-launch`、`test-driven-development`。除统一项、跨技能引用改用公开技能名与中文精修外，这些技能未引入额外的 NexusKit 行为改写（`accessibility-engineering` 附带上游原样脚本 `scripts/audit-a11y.sh`）。
- **统一项（适用于全部 26 个）**：H1 用上游英文标题；frontmatter `description` 用上游英文原文（作者按触发率调校过）；「Red Flags」统一为「危险信号」；合理化表列头与部分小节标题按本仓术语标准统一（现已收敛至 [glossary.md](glossary.md)）。
- **正文小修**：`ci-cd-and-automation`、`code-review-and-quality`、`code-simplification`、`constraint-driven-development`、`context-engineering`、`debugging-and-error-recovery`、`deprecation-and-migration`、`documentation-and-adrs`、`incremental-implementation`、`performance-optimization`、`planning-and-task-breakdown`、`security-and-hardening`、`source-driven-development`、`spec-driven-development`。改动包括回填上游后续修正、修正交叉引用、把规则文件表述统一为 `CLAUDE.md`/`AGENTS.md`，以及命令名 nk 化。
- **NK 改写**：
  - `doubt-driven-development`：跨模型复审段改为派发内置子智能体并按项目约定指定 `model`；DOUBT 步骤优先派发 `doubt-challenger`。
  - `idea-refine`：去掉命令专用的 `$ARGUMENTS` 占位；保存落点改为项目规则文件优先，默认 `docs/ideas/`。
  - `spec-driven-development`：阶段 4 的路径引用改为公开技能名（多模块 `spec/capability-map.md` + `spec/SPEC-<id>.md` 落点已于上游 v0.6.17 PR #797 趋同）。

## 已回填的上游修正（v0.6.14 – v0.6.17 / `8c99fa3`）

- `accessibility-engineering` 套件（v0.6.17 / PR #261）：引入 `skills/accessibility-engineering/SKILL.md` 及 `scripts/audit-a11y.sh`、`agents/accessibility-auditor.md`（补 `model: sonnet`）、`.claude/commands/nk-a11y.md`；同步更新 `using-agent-skills` 路由与 `references/accessibility-checklist.md`（升级至 WCAG 2.2 AA、SC 2.5.8 触控目标 24×24 CSS px 及固定版本的 `@axe-core/cli@4.13.0`、`pa11y@9.1.1`）。
- Spec 演进与 Delta Spec（v0.6.16 / PR #383、v0.6.17 / PR #797）：`spec-driven-development` 新增版本标题 `— V[N]`、`Out of Scope (Deferred)` 与根级 delta spec（`SPEC-<change>.md` + `Status:` 生命周期）；`planning-and-task-breakdown` 模板补 `Source spec:`；`/nk-spec` 分流新建与 delta spec；`/nk-build` 优先识别未实现的 `SPEC-<change>.md`，并针对外部 tracker（如 beads）精简了 `tasks/plan.md` 段落。
- `documentation-and-adrs`（v0.6.16 / PR #514）：`description` 补充漂移触发词；新增「文档漂移（Documentation Drift）」小节（git 祖先判断、无法判定时报 `"can't tell"`、变更日志只追加不改写）。
- `security-and-hardening` 与 `references/security-checklist.md`（v0.6.14–0.6.16 / PR #785, #787）：暂存密钥检查改为 `git diff --cached -i -G'…' --name-only`；ownership 检查前先返回 404；OWASP Top 10 升级至 2025 版编号并注明年份；`hardening-patterns.md` 补充 `SESSION_SECRET` 启动校验。
- `code-review-and-quality`（PR #736、v0.6.16 #763、v0.6.17 #795）：第 4 步核实发现并接受零发现；第 5 步补充自跑测试前核对工作区干净且位于待审 ref；`description` 覆盖内联 diff 触发。
- `frontend-ui-engineering`（v0.6.16 / PR #732）：新增「使用项目现有工具验证」约束与 WAI-ARIA APG 模式引用。
- `constraint-driven-development`（v0.6.15 #694、v0.6.16 #786）：新增 `scripts/quality-gate.mjs`、gitleaks `dir` 与 `check:security`/`check:a11y`；架构门禁命令由 `depcruise --validate src` 修正为 `depcruise src`；`references/floor-guard.md` 识别表格单元格内方向词。
- `ci-cd-and-automation`（v0.6.17 / PR #799）：Vercel 回滚 workflow 补 `VERCEL_TOKEN` 与 `--token "$VERCEL_TOKEN" --yes`。
- 其余技能与命令：`debugging-and-error-recovery`、`test-driven-development` 同步 v0.6.16 路由 `description`；`.claude/commands/nk-*.md` 全部配置 `disable-model-invocation: true`；其余 v0.6.14/0.6.15 示例修正与 `references/` 更新均已回填。

## Commands

`.claude/commands/` 下的 10 个上游命令来自同版本 `.claude/commands/*.md`，结构性改动包括：

- 移除 `agent-skills:` 前缀，改指本包技能名。
- slash 名加 `nk-` 前缀（含新增 `/nk-a11y`），正文中的自称与交叉引用同步。
- `/nk-ship` 的 subagent 派发说明按 Claude Code 的 Agent tool 与 scope 规则调整；`/nk-webperf` 与 `/nk-a11y` 保留上游 Claude Code 形态的 Quick/Deep 输入说明；`/nk-build` 步骤 3 针对外部 tracker（如 beads）做了精简适配。

`/nk-init` 为 NK 扩展：[入口](../.claude/commands/nk-init.md) 的探测、逐项确认、草稿确认与幂等写入骨架参考 Matt `skills/engineering/setup-matt-pocock-skills/SKILL.md` 的 `Explore`、`Present findings and ask`、`Confirm and edit`、`Write`；七项配置对象（规则文件、idea/ADR/spec/task 落点、外置工具、子智能体模型与覆盖层级）为 NK 设计。

## Agents

- `accessibility-auditor`、`code-reviewer`、`security-auditor`、`test-engineer`、`web-performance-auditor`：来自上游 `agents/` 同名文件，补 `model` 字段，并按 nk 命令名与 `references/orchestration-patterns.md` 调整引用。
- `doubt-challenger`：NK 新增，对抗式证伪子智能体，工具限只读，默认 `model: sonnet`。

## References

`references/` 下 7 份检查清单以英文上游同路径为基底，经过中文精修、上游修正回填与本仓命令名适配；`issue-graph.md` 为 NK 新增，给出 issue tracker 的建图规则（工作单元、三种边、checkpoint、审查与关闭），上游没有对应文件。它同时是模板与兜底：`/nk-init` 把全文写进项目的 `docs/agents/issue-tracker.md`，规则文件只留一行指针；`planning-and-task-breakdown` 优先按项目那份建图，项目没初始化时才用插件里这份。载体形式参考 Matt `setup-matt-pocock-skills` 的 `docs/agents/`。技能按需引用；仓库级共享，不存在单技能安装断链。

## 未 vendor

上游的 `hooks/`、`scripts/`、`evals/`、`docs/`、`commands/*.toml`、`.gemini/`、`.opencode/`、`.codex-plugin/` 不在 Claude Code 插件的运行面内，未引入。取舍以本文件、v0.4.0 发布说明与 Git 历史为准。