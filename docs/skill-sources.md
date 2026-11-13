# 技能来源映射

维护者向索引：记录 NexusKit 各部分的上游来源与本地改动。执行技能的 Agent 不需要读本文件。

## 上游与同步点

- 技能主体：[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)，同步点 `aeac41d`（v0.6.13）；另已回填 v0.6.14/0.6.15 及后续 `301b02b`（PR #736）的可翻译内容（见下；docs、evals、hooks、scripts 不在 vendor 范围）。
- 早期简体中文译本：[vinvcn/addyosmani-agent-skills-zh](https://github.com/vinvcn/addyosmani-agent-skills-zh)（本地副本 `.upstream/addyosmani-agent-skills-zh`，已停更；已 gitignore，不随包分发）。现以 `.upstream/addyosmani-agent-skills` 直接对照英文上游，术语与翻译规范见 [glossary.md](glossary.md)。
- 引入方式：vendor，小修小补；技能名、目录名与 H1 保持上游原样。逐技能的改动点见 [v0.4.0 计划](plans/2026-10-29-v0.4.0-osmani-vendor-plan.md) 的逐技能审阅表。
- 归属与许可证见 [NOTICE](../NOTICE) 与 [LICENSE.upstream](../LICENSE.upstream)。

## Skills

25 个技能位于 `skills/<name>/SKILL.md`，与上游同名同路径。来源按以下几类记录：

- **正文原样**：`using-agent-skills`、`api-and-interface-design`、`browser-testing-with-devtools`、`code-review-and-quality`、`frontend-ui-engineering`、`git-workflow-and-versioning`、`interview-me`、`observability-and-instrumentation`、`shipping-and-launch`、`test-driven-development`。这些技能只随统一项调整标题与 description。
- **统一项（适用于全部 25 个）**：H1 用上游英文标题；frontmatter `description` 用上游英文原文（作者按触发率调校过）；「Red Flags」统一为「危险信号」；合理化表列头与部分小节标题按本仓术语标准统一（现已收敛至 [glossary.md](glossary.md)）。具体范围见计划的 D3–D6。
- **正文小修**：`ci-cd-and-automation`、`code-simplification`、`constraint-driven-development`、`context-engineering`、`debugging-and-error-recovery`、`deprecation-and-migration`、`documentation-and-adrs`、`incremental-implementation`、`performance-optimization`、`planning-and-task-breakdown`、`security-and-hardening`、`source-driven-development`、`spec-driven-development`。改动包括回填上游后续修正、修正交叉引用、把规则文件表述统一为 `CLAUDE.md`/`AGENTS.md`，以及命令名 nk 化。
- **NK 改写**：
  - `doubt-driven-development`：跨模型复审段改为派发内置子智能体并按项目约定指定 `model`；DOUBT 步骤优先派发 `doubt-challenger`。
  - `idea-refine`：去掉命令专用的 `$ARGUMENTS` 占位；保存落点改为项目规则文件优先，默认 `docs/ideas/`。
  - `spec-driven-development`：多模块 spec 落点改为 `spec/`（`spec/capability-map.md` + `spec/SPEC-<id>.md`），与 `/nk-build` 的查找路径一致；阶段 4 的路径引用改为公开技能名。

## 已回填的上游修正（v0.6.14 – `301b02b`）

- `code-review-and-quality`（`301b02b` / PR #736）：第 4 步补充报告发现前先对照可达调用方、守卫条件与测试核实并剔除误报、区分原有缺陷与新引入回归、接受零发现作为有效结果。
- `security-and-hardening`：暂存密钥检查改为 `git diff --cached -i -G'…' --name-only`，只列文件名、不回显值；ownership 检查前先返回 404；description 补 `session cookies`。同改动也落在 `references/security-checklist.md`。
- `constraint-driven-development`：新增 `scripts/quality-gate.mjs`，让 Semgrep/axe 的 high/critical 发现真正使 CI 失败；同步 gitleaks `dir` 调用、`check:security`/`check:a11y` 映射，以及「用故意违规验证门禁」的验收项；`references/floor-guard.md` 识别表格单元格内的方向词。
- `.claude/commands/nk-*.md`：与上游一致加 `disable-model-invocation: true`，命令仅用户可调用；`/nk-init` 原本即为此形态。
- 其余技能与 references：回填 0.6.14/0.6.15 的示例修正与触发词更新，涉及 `api-and-interface-design`、`browser-testing-with-devtools`、`code-simplification`、`context-engineering`、`debugging-and-error-recovery`、`deprecation-and-migration`、`documentation-and-adrs`、`doubt-driven-development`、`frontend-ui-engineering`、`git-workflow-and-versioning`、`shipping-and-launch`、`source-driven-development`、`spec-driven-development`、`test-driven-development`，以及 `references/` 下的 accessibility、performance、testing 三份清单。`ci-cd-and-automation` 与 `performance-optimization` 的对应修正此前已在发布批回填。

## Commands

`.claude/commands/` 下的 9 个上游命令来自同版本 `.claude/commands/*.md`，改动只有：

- 移除 `agent-skills:` 前缀，改指本包技能名。
- slash 名加 `nk-` 前缀，正文中的自称与交叉引用同步。
- `/nk-ship` 的 subagent 派发说明按 Claude Code 的 Agent tool 与 scope 规则调整；`/nk-webperf` 保留上游 Claude Code 形态的输入说明。

`/nk-init` 为 NK 扩展：[入口](../.claude/commands/nk-init.md) 的探测、逐项确认、草稿确认与幂等写入骨架参考 Matt `skills/engineering/setup-matt-pocock-skills/SKILL.md` 的 `Explore`、`Present findings and ask`、`Confirm and edit`、`Write`；七项配置对象（规则文件、idea/ADR/spec/task 落点、外置工具、子智能体模型与覆盖层级）为 NK 设计。

## Agents

- `code-reviewer`、`security-auditor`、`test-engineer`、`web-performance-auditor`：来自上游 `agents/` 同名文件，补 `model` 字段，并按 nk 命令名调整引用。
- `doubt-challenger`：NK 新增，对抗式证伪子智能体，工具限只读，默认 `model: sonnet`。

## References

`references/` 下 7 份检查清单来自上游同路径，内容未改；`issue-graph.md` 为 NK 新增，给出 issue tracker 的建图规则（工作单元、三种边、checkpoint、审查与关闭），上游没有对应文件。它同时是模板与兜底：`/nk-init` 把全文写进项目的 `docs/agents/issue-tracker.md`，规则文件只留一行指针；`planning-and-task-breakdown` 优先按项目那份建图，项目没初始化时才用插件里这份。载体形式参考 Matt `setup-matt-pocock-skills` 的 `docs/agents/`。技能按需引用；仓库级共享，不存在单技能安装断链。

## 未 vendor

上游的 `hooks/`、`scripts/`、`evals/`、`docs/`、`commands/*.toml`、`.gemini/`、`.opencode/`、`.codex-plugin/` 不在 Claude Code 插件的运行面内，未引入。取舍见计划的 D9。