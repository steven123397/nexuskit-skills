# AGENTS.md

本仓库是 NexusKit 技能开发目录。技能位于 `skills/engineering/nk-*/` 和 `skills/productivity/nk-*/`，客户端通过插件或 skills CLI 消费安装快照，仓库不是实时加载源。

## 工作入口

从 Linear 确认任务与已定范围，从 Git/PR 核对实际改动；需要背景、历史理由或经验时检索 OpenViking。术语见 [CONCEPTS.md](CONCEPTS.md)，重要设计见 [docs/decisions/](docs/decisions/)，来源对应见 [docs/skill-sources.md](docs/skill-sources.md)。

旧 `docs/solutions/` 和历史计划、审查、讨论材料等待迁移，不作为当前执行规则，也不要求新会话通读。删除旧知识来源前，按 STE-13 验证新位置可读取和检索。不恢复 current 或重复交接文档。

## 技能组织

- `SKILL.md` 放完整主流程，模板、提示词、脚本等按实际需要就近放置。跨技能调用公开入口，不读取其他技能的私有文件，不恢复集中 conventions 或共享片段副本机制。
- 待重写的旧入口保留为 `SKILL.legacy.md`，只供维护者对照，不是可执行技能。其旧链接按迁移前版本理解，缺失材料可在 Git 历史中查阅。新增技能以 `.gitkeep` 保留目录，不创建可安装的空壳。
- 逐技能按新职责重写，再对照旧稿检查必要能力；完成一份后供维护者审阅。启用时移除旧稿或占位文件，更新 README 可安装入口和插件描述中的清单。init、ask-ljq 最后重写。
- frontmatter 的 `description` 用英文；正文可用中文。修改来源对应时更新 skill-sources，说明具体部分来自何处，不记进度、日期或验证流水账。

## 修改与验证

- 不直接修改或提交主分支。原检出目录正常切换工作分支，不建立额外主工作树。需要并行写入或原型隔离时才开工作树，默认放在仓库同级 `<项目名>-worktrees/<用途>`；优先沿用宿主管理方式，并明确绝对路径、分支与用途。
- 保留其他会话的未提交工作。成果承接后及时清理闲置工作树，清理前核对活跃使用者、未提交及忽略文件，不删除原工作目录或其他任务资源。
- 技能或基础检查修改后运行 `python tests/run_checks.py`；检查器修改另跑 `python -m unittest discover -s tests -p "test_*.py"`。首次安装依赖用 `python -m pip install -r tests/requirements.txt`。
- wizard 模板修改后执行 `bash -n skills/productivity/nk-wizard/assets/template.sh`。CI 覆盖 Windows/Linux，版本 tag 还检查版本号和 release notes。
- 检查覆盖链接、技能引用、大小、分发与 frontmatter；机械检查不证明真实客户端执行效果。使用仓库的 YAML 校验器，不为通过外部 skill-creator 校验器删掉合法字段。
- 提交通过 nk-commit；迁移期间旧稿位于 [SKILL.legacy.md](skills/engineering/nk-commit/SKILL.legacy.md)，其中已经退役的 current、Plan、U-ID 等要求不适用。没有明确提交安排时保留可审阅改动，不把骨架搭建当成整轮技能完成。
- 新建技能目录不创建加载链接。即时试用需手动重装本地插件；临时 junction 用 PowerShell 创建，删除 junction 用 `[IO.Directory]::Delete()`，不递归删除目标。
