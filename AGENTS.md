# AGENTS.md

本仓库是 NexusKit 技能开发目录。v0.4.0 起技能位于 `skills/` 平铺目录：主体为 vendored 的 addyosmani/agent-skills 简体中文版（技能名保留原样），`nk-*` 前缀目录为自有扩展（从 `archive/v0.3.x-nk-skills` 分支择优提回中）。客户端以 Claude Code 插件为主体（`.claude-plugin/` 清单，仓库即单插件市场），仓库不是实时加载源。

## 工作入口

本轮（v0.4.0）不用 Linear：任务与进度以 [docs/plans/2026-10-29-v0.4.0-osmani-vendor-plan.md](docs/plans/2026-10-29-v0.4.0-osmani-vendor-plan.md) 的工作表为准，从 Git/PR 核对实际改动；需要背景、历史理由或经验时检索 OpenViking。术语见 [CONCEPTS.md](CONCEPTS.md)，上游通用术语的统一译法见 [context.md](context.md)，重要设计见 [docs/adr/](docs/adr/)，来源对应见 [docs/skill-sources.md](docs/skill-sources.md)。

旧 `docs/solutions/` 与发想、讨论材料已按 STE-13 迁移：背景与经验归 OpenViking，正式决定归 `docs/adr/`，发布证据保留在 `docs/plans/` 与 `docs/reviews/`。不恢复 current 或重复交接文档。

## 技能组织

- 上游技能以 vendor 方式引入并保持可同步：改动走小修小补，改动点记录于计划文档的逐技能审阅表；不做大型重写，不与上游无谓分叉。同步源为 `.upstream/addyosmani-agent-skills-zh`（本地克隆，已 gitignore），它自身跟踪上游 addyosmani/agent-skills。
- `SKILL.md` 放完整主流程，模板、提示词、脚本等按实际需要就近放置。跨技能调用公开入口，不读取其他技能的私有文件。仓库级共享检查清单位于 `references/`（整包分发，不存在单技能安装断链问题）。
- nk 旧技能不设 legacy 副本：整体封存于 `archive/v0.3.x-nk-skills` 分支，提回时逐个裁定（提回 / 不提回 / 并入），结果记录于计划文档的提回裁定表。新增技能以 `.gitkeep` 保留目录，不创建可安装的空壳。
- frontmatter 的 `description` 采用上游英文原文（作者按触发率调校过，译文属二次加工）；正文可用中文。修改来源对应时更新 skill-sources，说明具体部分来自何处，不记进度、日期或验证流水账。

## 修改与验证

- 不直接修改或提交主分支。原检出目录正常切换工作分支，不建立额外主工作树。需要并行写入或原型隔离时才开工作树，默认放在仓库同级 `<项目名>-worktrees/<用途>`；优先沿用宿主管理方式，并明确绝对路径、分支与用途。
- 保留其他会话的未提交工作。成果承接后及时清理闲置工作树，清理前核对活跃使用者、未提交及忽略文件，不删除原工作目录或其他任务资源。
- 技能或基础检查修改后运行 `python tests/run_checks.py`；检查器修改另跑 `python -m unittest discover -s tests -p "test_*.py"`。首次安装依赖用 `python -m pip install -r tests/requirements.txt`。
- nk-wizard 提回后，其模板修改执行 `bash -n skills/nk-wizard/assets/template.sh`。CI 覆盖 Windows/Linux，版本 tag 还检查版本号和 release notes。
- 检查覆盖链接、技能引用、大小、分发与 frontmatter；机械检查不证明真实客户端执行效果。使用仓库的 YAML 校验器，不为通过外部 skill-creator 校验器删掉合法字段。
- 提交按仓库历史的 conventional commits 惯例手动执行。没有明确提交安排时保留可审阅改动，不把骨架搭建当成整轮技能完成。
- 新建技能目录不创建加载链接。即时试用需手动重装本地插件；临时 junction 用 PowerShell 创建，删除 junction 用 `[IO.Directory]::Delete()`，不递归删除目标。
