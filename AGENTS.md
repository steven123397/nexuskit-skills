# AGENTS.md

本仓库是 NexusKit 技能开发目录。v0.4.0 起技能位于 `skills/` 平铺目录：主体为 vendored 的 addyosmani/agent-skills 简体中文版（技能名保留原样），`nk-*` 前缀目录为自有扩展（从 `archive/v0.3.x-nk-skills` 分支择优提回中）。客户端以 Claude Code 插件为主体（`.claude-plugin/` 清单，仓库即单插件市场），仓库不是实时加载源。

## 工作入口

任务跟踪已由 Linear 切换到 beads（仓库内 `.beads/`，见下方「项目约定」），存量票尚未迁入。迁移完成前，v0.4.0 的任务与进度仍以 [docs/plans/2026-10-29-v0.4.0-osmani-vendor-plan.md](docs/plans/2026-10-29-v0.4.0-osmani-vendor-plan.md) 的工作表为准，从 Git/PR 核对实际改动；需要背景、历史理由或经验时检索 OpenViking。术语见 [CONCEPTS.md](CONCEPTS.md)，上游通用术语的统一译法见 [context.md](context.md)，重要设计见 [docs/adr/](docs/adr/)，来源对应见 [docs/skill-sources.md](docs/skill-sources.md)。

旧 `docs/solutions/` 与发想、讨论材料已按 STE-13 迁移：背景与经验归 OpenViking，正式决定归 `docs/adr/`，发布证据保留在 `docs/plans/` 与 `docs/releases/`；更早的审查记录已删除，Git 历史可查。不恢复 current 或重复交接文档。

## 技能组织

- 上游技能以 vendor 方式引入并保持可同步：改动走小修小补，改动点记录于计划文档的逐技能审阅表；不做大型重写，不与上游无谓分叉。同步源为 `.upstream/addyosmani-agent-skills-zh`（本地克隆，已 gitignore），它自身跟踪上游 addyosmani/agent-skills。
- `SKILL.md` 放完整主流程，模板、提示词、脚本等按实际需要就近放置。跨技能调用公开入口，不读取其他技能的私有文件。仓库级共享检查清单位于 `references/`（整包分发，不存在单技能安装断链问题）。
- nk 旧技能不设 legacy 副本：整体封存于 `archive/v0.3.x-nk-skills` 分支，提回时逐个裁定（提回 / 不提回 / 并入），结果记录于计划文档的提回裁定表。新增技能以 `.gitkeep` 保留目录，不创建可安装的空壳。
- frontmatter 的 `description` 采用上游英文原文（作者按触发率调校过，译文属二次加工）；正文可用中文。修改来源对应时更新 skill-sources，说明具体部分来自何处，不记进度、日期或验证流水账。

## 修改与验证

- 默认直接在主分支开发与提交，不再为每项工作新建分支；只有需要并行写入、原型隔离或高风险试验时才开分支或工作树。工作树默认放在仓库同级 `<项目名>-worktrees/<用途>`；优先沿用宿主管理方式，并明确绝对路径、分支与用途。发布仍走 PR 或版本 tag 的既有流程。
- 保留其他会话的未提交工作。成果承接后及时清理闲置工作树，清理前核对活跃使用者、未提交及忽略文件，不删除原工作目录或其他任务资源。
- 技能或基础检查修改后运行 `python tests/run_checks.py`；检查器修改另跑 `python -m unittest discover -s tests -p "test_*.py"`。首次安装依赖用 `python -m pip install -r tests/requirements.txt`。
- nk-wizard 提回后，其模板修改执行 `bash -n skills/nk-wizard/assets/template.sh`。CI 覆盖 Windows/Linux，版本 tag 还检查版本号和 release notes。
- 检查覆盖链接、技能引用、大小、分发与 frontmatter；机械检查不证明真实客户端执行效果。使用仓库的 YAML 校验器，不为通过外部 skill-creator 校验器删掉合法字段。
- 提交按仓库历史的 conventional commits 惯例手动执行。没有明确提交安排时保留可审阅改动，不把骨架搭建当成整轮技能完成。
- 新建技能目录不创建加载链接。即时试用需手动重装本地插件；临时 junction 用 PowerShell 创建，删除 junction 用 `[IO.Directory]::Delete()`，不递归删除目标。

## 项目约定

- idea：`docs/ideas/`，一个想法一个文件
- 决策记录：`docs/adr/`，编号递增，不删旧
- 规格：`SPEC.md`；外部工具：无
- task：beads，仓库内 `.beads/`（`bd init` 初始化），beads 为唯一来源；不再用 `tasks/plan.md` + `tasks/todo.md`
- issue 图：`references/issue-graph.md`
- 子智能体模型：派发时显式传 `model` —— code-reviewer、security-auditor 用 opus；doubt-challenger、test-engineer、web-performance-auditor 用 sonnet
- 以上文件在第一次真正产出时创建，不预建空目录

<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:46cd31e7 -->
## Beads Issue Tracker

This project uses **bd (beads)** for issue tracking. Run `bd prime` to see full workflow context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Rules

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown TODO lists
- Run `bd prime` for detailed command reference and session close protocol
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

**Architecture in one line:** issues live in a local Dolt DB; sync uses `refs/dolt/data` on your git remote; `.beads/issues.jsonl` is a passive export. See https://github.com/gastownhall/beads/blob/main/docs/core-concepts/sync-concepts.md for details and anti-patterns.

## Agent Context Profiles

The managed Beads block is task-tracking guidance, not permission to override repository, user, or orchestrator instructions.

- **Conservative (default)**: Use `bd` for task tracking. Do not run git commits, git pushes, or Dolt remote sync unless explicitly asked. At handoff, report changed files, validation, and suggested next commands.
- **Minimal**: Keep tool instruction files as pointers to `bd prime`; use the same conservative git policy unless active instructions say otherwise.
- **Team-maintainer**: Only when the repository explicitly opts in, agents may close beads, run quality gates, commit, and push as part of session close. A current "do not commit" or "do not push" instruction still wins.

## Session Completion

This protocol applies when ending a Beads implementation workflow. It is subordinate to explicit user, repository, and orchestrator instructions.

1. **File issues for remaining work** - Create beads for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **Handle git/sync by active profile**:
   ```bash
   # Conservative/minimal/default: report status and proposed commands; wait for approval.
   git status

   # Team-maintainer opt-in only, unless current instructions forbid it:
   git pull --rebase
   bd dolt push
   git push
   git status
   ```
5. **Hand off** - Summarize changes, validation, issue status, and any blocked sync/commit/push step

**Critical rules:**
- Explicit user or orchestrator instructions override this Beads block.
- Do not commit or push without clear authority from the active profile or the current user request.
- If a required sync or push is blocked, stop and report the exact command and error.
<!-- END BEADS INTEGRATION -->

<!-- BEGIN BEADS CODEX SETUP: generated by bd setup codex -->
## Beads Issue Tracker

Use Beads (`bd`) for durable task tracking in repositories that include it. Use the `beads` skill at `.agents/skills/beads/SKILL.md` (project install) or `~/.agents/skills/beads/SKILL.md` (global install) for Beads workflow guidance, then use the `bd` CLI for issue operations.

### Quick Reference

```bash
bd ready                # Find available work
bd show <id>            # View issue details
bd update <id> --claim  # Claim work
bd close <id>           # Complete work
bd prime                # Refresh Beads context
```

### Rules

- Use `bd` for all task tracking; do not create markdown TODO lists.
- Run `bd prime` when Beads context is missing or stale. Codex 0.129.0+ can load Beads context automatically through native hooks; use `/hooks` to inspect or toggle them.
- Keep persistent project memory in Beads via `bd remember`; do not create ad hoc memory files.

**Architecture in one line:** issues live in a local Dolt DB; sync uses `refs/dolt/data` on your git remote; `.beads/issues.jsonl` is a passive export. See https://github.com/gastownhall/beads/blob/main/docs/core-concepts/sync-concepts.md for details and anti-patterns.
<!-- END BEADS CODEX SETUP -->
