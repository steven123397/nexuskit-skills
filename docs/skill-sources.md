# 技能来源映射

维护者向索引：记录 NexusKit 各部分的上游来源与本地改动。执行技能的 Agent 不需要读本文件。

## 上游与同步点

- 技能主体：[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)，同步点 `aeac41d`（v0.6.13）。
- 简体中文译本：[vinvcn/addyosmani-agent-skills-zh](https://github.com/vinvcn/addyosmani-agent-skills-zh)，本地同步源 `.upstream/addyosmani-agent-skills-zh`（已 gitignore，不随包分发）。
- 引入方式：vendor，小修小补；技能名、目录名与 H1 保持上游原样。逐技能的改动点见 [v0.4.0 计划](plans/2026-10-29-v0.4.0-osmani-vendor-plan.md) 的逐技能审阅表。
- 归属与许可证见 [NOTICE](../NOTICE) 与 [LICENSE.upstream](../LICENSE.upstream)。

## Skills

25 个技能位于 `skills/<name>/SKILL.md`，与上游同名同路径。来源按以下几类记录：

- **正文原样**：`using-agent-skills`、`api-and-interface-design`、`browser-testing-with-devtools`、`code-review-and-quality`、`frontend-ui-engineering`、`git-workflow-and-versioning`、`interview-me`、`observability-and-instrumentation`、`shipping-and-launch`、`test-driven-development`。这些技能只随统一项调整标题与 description。
- **统一项（适用于全部 25 个）**：H1 用上游英文标题；frontmatter `description` 用上游英文原文（作者按触发率调校过）；「Red Flags」统一为「危险信号」；合理化表列头与部分小节标题按上游术语表统一。具体范围见计划的 D3–D6。
- **正文小修**：`ci-cd-and-automation`、`code-simplification`、`constraint-driven-development`、`context-engineering`、`debugging-and-error-recovery`、`deprecation-and-migration`、`documentation-and-adrs`、`incremental-implementation`、`performance-optimization`、`planning-and-task-breakdown`、`security-and-hardening`、`source-driven-development`、`spec-driven-development`。改动包括回填上游后续修正、修正交叉引用、把规则文件表述统一为 `CLAUDE.md`/`AGENTS.md`，以及命令名 nk 化。
- **NK 改写**：
  - `doubt-driven-development`：跨模型复审段改为派发内置子智能体并按项目约定指定 `model`；DOUBT 步骤优先派发 `doubt-challenger`。
  - `idea-refine`：去掉命令专用的 `$ARGUMENTS` 占位；保存落点改为项目规则文件优先，默认 `docs/ideas/`。
  - `spec-driven-development`：多模块 spec 落点改为 `spec/`（`spec/capability-map.md` + `spec/SPEC-<id>.md`），与 `/nk-build` 的查找路径一致；阶段 4 的路径引用改为公开技能名。

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

`references/` 下 7 份检查清单来自上游同路径，内容未改。技能按需引用；仓库级共享，不存在单技能安装断链。

## 未 vendor

上游的 `hooks/`、`scripts/`、`evals/`、`docs/`、`commands/*.toml`、`.gemini/`、`.opencode/`、`.codex-plugin/` 不在 Claude Code 插件的运行面内，未引入。取舍见计划的 D9。