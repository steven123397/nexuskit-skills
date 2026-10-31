<h1 align="center">NexusKit</h1>

<p align="center"><strong>面向 AI 编程 Agent 的工程技能工具箱</strong></p>
<p align="center">以 addyosmani/agent-skills 简体中文版为核心，覆盖从想法到交付的完整开发流程。</p>

<p align="center">
  <a href="https://github.com/steven123397/nexuskit-skills/releases"><img src="https://img.shields.io/github/v/release/steven123397/nexuskit-skills?include_prereleases&amp;style=flat-square&amp;color=6366f1" alt="最新版本（含预发布）"></a>
  <a href="https://github.com/steven123397/nexuskit-skills/actions/workflows/checks.yml"><img src="https://img.shields.io/github/actions/workflow/status/steven123397/nexuskit-skills/checks.yml?branch=main&amp;style=flat-square&amp;label=checks" alt="main 分支检查状态"></a>
  <a href="https://github.com/steven123397/nexuskit-skills/blob/main/LICENSE"><img src="https://img.shields.io/github/license/steven123397/nexuskit-skills?style=flat-square&amp;color=0d9488" alt="MIT 许可证"></a>
</p>

<p align="center">
  <a href="#安装">安装</a> ·
  <a href="#命令">命令</a> ·
  <a href="#技能一览">技能一览</a> ·
  <a href="#子智能体">子智能体</a> ·
  <a href="https://github.com/steven123397/nexuskit-skills/releases">版本记录</a> ·
  <a href="https://github.com/steven123397/nexuskit-skills/issues">问题反馈</a>
</p>

---

NexusKit 以 [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) 的简体中文版为技能主体，保留上游的技能名、目录与工作流，并在其上提供 10 个 `nk-` 前缀的入口命令和 5 个专用子智能体。技能按需调用，不强制走完整流水线。

当前为 [v0.4.0-beta.1](docs/releases/v0.4.0-beta.1.md)（预发布）：技能主体完成 vendor 与逐技能审阅，命令层与项目接入命令已就位。旧版 `nk-*` 技能已归档，是否提回待 beta 试用后裁定。

## 安装

### Claude Code（推荐）

本仓库同时是 Claude Code 插件市场。添加市场后安装插件：

```text
/plugin marketplace add steven123397/nexuskit-skills
/plugin install nexuskit@nexuskit-skills
```

安装后获得 25 个技能、10 个 `nk-` 命令和 5 个子智能体。清单见 [.claude-plugin/plugin.json](.claude-plugin/plugin.json)。

本地开发或试用未发布改动：

```text
/plugins install D:\codex_project\nexuskit
```

### skills CLI

只安装技能，不含命令与子智能体：

```bash
npx skills add steven123397/nexuskit-skills
```

技能统一从 `skills/` 下发现；只有 `SKILL.md` 是入口，目录占位和旧稿不是技能。安装后的客户端使用安装快照，仓库改动不会自动更新已安装版本。

> v0.4.0 暂不提供 Kimi 插件；Codex 安装方式因 vendored 技能超出其读取上限已废止。

## 命令

| 命令 | 用途 |
|---|---|
| `/nk-init` | 首次接入项目：确认规则文件、idea/ADR/spec/task 落点、外置工具与子智能体模型，写入项目约定。仅手动调用 |
| `/nk-spec` | 写代码前先编写结构化 spec |
| `/nk-plan` | 把 spec 拆成带验收标准和依赖顺序的 task |
| `/nk-build` | 增量实现下一个 task；`/nk-build auto` 在一次获批后跑完整个 plan |
| `/nk-test` | 按 TDD 工作流写失败测试、实现、验证 |
| `/nk-constraints` | 定义并执行项目质量标准，写入 CONSTRAINTS.md |
| `/nk-review` | 五轴代码审查：正确性、可读性、架构、安全、性能 |
| `/nk-webperf` | 通过 web-performance-auditor 运行 Web 性能审计 |
| `/nk-code-simplify` | 行为不变的前提下简化代码 |
| `/nk-ship` | 发布前并行派发 specialist personas，汇总 go/no-go |

## 技能一览

<!-- installable-skills -->
**Meta**

- [using-agent-skills](skills/using-agent-skills/SKILL.md)：把当前工作映射到合适的技能工作流，并给出共享操作规则。

**Define — 澄清要构建什么**

- [interview-me](skills/interview-me/SKILL.md)：一次一问，挖掘用户真正想要的东西，直到约 95% 置信度。
- [idea-refine](skills/idea-refine/SKILL.md)：用结构化发散/收敛把模糊想法磨成可执行提案。
- [spec-driven-development](skills/spec-driven-development/SKILL.md)：写代码前先写覆盖目标、结构、测试与边界的 spec。
- [constraint-driven-development](skills/constraint-driven-development/SKILL.md)：通过访谈定下质量标准的数值与工具，写入 CONSTRAINTS.md 并守住。

**Plan — 拆解任务**

- [planning-and-task-breakdown](skills/planning-and-task-breakdown/SKILL.md)：把 spec 拆成带验收标准和依赖顺序的小型可验证 task。

**Build — 编写代码**

- [incremental-implementation](skills/incremental-implementation/SKILL.md)：薄垂直切片：实现、测试、验证、提交，便于回滚。
- [test-driven-development](skills/test-driven-development/SKILL.md)：Red-Green-Refactor、测试金字塔、DAMP over DRY、浏览器测试。
- [context-engineering](skills/context-engineering/SKILL.md)：在正确的时间把正确的信息交给 agent：规则文件、上下文打包、MCP。
- [source-driven-development](skills/source-driven-development/SKILL.md)：让实现决策基于官方文档，标注来源与未验证内容。
- [doubt-driven-development](skills/doubt-driven-development/SKILL.md)：对非平凡决策做对抗式 fresh-context 复审。
- [frontend-ui-engineering](skills/frontend-ui-engineering/SKILL.md)：组件架构、设计系统、状态管理、响应式与 WCAG 2.1 AA。
- [api-and-interface-design](skills/api-and-interface-design/SKILL.md)：契约优先、Hyrum's Law、错误语义与边界校验。

**Verify — 证明它能工作**

- [browser-testing-with-devtools](skills/browser-testing-with-devtools/SKILL.md)：用 Chrome DevTools MCP 获取 DOM、console、network 与性能数据。
- [debugging-and-error-recovery](skills/debugging-and-error-recovery/SKILL.md)：五步分诊：复现、定位、缩小、修复、防回归。

**Review — 合并前质量门禁**

- [code-review-and-quality](skills/code-review-and-quality/SKILL.md)：五轴审查、变更规模、严重度标签与拆分策略。
- [code-simplification](skills/code-simplification/SKILL.md)：在行为不变的前提下降低复杂度。
- [security-and-hardening](skills/security-and-hardening/SKILL.md)：OWASP Top 10、认证、密钥管理、依赖审计与三层边界。
- [performance-optimization](skills/performance-optimization/SKILL.md)：先测量再优化：Core Web Vitals、profiling、bundle 分析。

**Ship — 有信心地发布**

- [git-workflow-and-versioning](skills/git-workflow-and-versioning/SKILL.md)：trunk-based、原子提交、变更规模与提交即保存点。
- [ci-cd-and-automation](skills/ci-cd-and-automation/SKILL.md)：Shift Left、质量门禁流水线、feature flag 与失败反馈回路。
- [deprecation-and-migration](skills/deprecation-and-migration/SKILL.md)：代码即负债、强制/建议式弃用、迁移模式与僵尸代码清理。
- [documentation-and-adrs](skills/documentation-and-adrs/SKILL.md)：ADR、API 文档与行内文档标准，记录 why。
- [observability-and-instrumentation](skills/observability-and-instrumentation/SKILL.md)：结构化日志、RED 指标、OpenTelemetry、基于症状的告警。
- [shipping-and-launch](skills/shipping-and-launch/SKILL.md)：发布前 checklist、feature flag 生命周期、灰度与回滚。
<!-- /installable-skills -->

以上为全部 25 个技能。逐技能的本地改动点见 [v0.4.0 计划](docs/plans/2026-10-29-v0.4.0-osmani-vendor-plan.md) 的审阅表；来源对应见 [技能来源](docs/skill-sources.md)。

## 子智能体

| 子智能体 | 角色 |
|---|---|
| [code-reviewer](agents/code-reviewer.md) | 五轴代码审查，按 staff engineer 会批准吗的标准 |
| [security-auditor](agents/security-auditor.md) | 漏洞检测、威胁建模与 OWASP assessment |
| [test-engineer](agents/test-engineer.md) | 测试策略、覆盖率分析与 Prove-It pattern |
| [web-performance-auditor](agents/web-performance-auditor.md) | Core Web Vitals 审计，Quick/Deep 模式 |
| [doubt-challenger](agents/doubt-challenger.md) | 对抗式证伪复审，只读检查假设与失败模式 |

模型选择由 `/nk-init` 在项目接入时确认；默认不改文件，派发时显式传 `model`。

## 参考清单

技能按需拉取的共享材料：

- [definition-of-done.md](references/definition-of-done.md)：每个变更都要过的项目级常驻标准。
- [testing-patterns.md](references/testing-patterns.md)：测试结构、命名、mock 与反模式。
- [security-checklist.md](references/security-checklist.md)：提交前检查、认证、输入校验、OWASP Top 10。
- [performance-checklist.md](references/performance-checklist.md)：Core Web Vitals、前后端检查清单与测量命令。
- [accessibility-checklist.md](references/accessibility-checklist.md)：键盘导航、屏幕阅读器、视觉设计与 ARIA。
- [observability-checklist.md](references/observability-checklist.md)：日志、RED/USE 指标、trace 与告警。
- [orchestration-patterns.md](references/orchestration-patterns.md)：多人格编排模式与反模式。

## 仓库结构

```text
skills/            25 个技能，平铺目录
.claude/commands/  10 个 nk- 前缀命令
agents/            5 个子智能体
references/        仓库级共享检查清单
.claude-plugin/    Claude Code 插件与市场清单
tests/             链接、引用、分发、frontmatter、artifact 路径检查
docs/              ADR、计划、版本说明与来源映射
```

本仓库是插件市场源与开发目录，不是客户端实时加载源。客户端消费的是安装快照；仓库改动不会自动更新已安装版本。

## 鸣谢

技能主体来自 [Addy Osmani 的 agent-skills](https://github.com/addyosmani/agent-skills)，经由 [vinvcn 的简体中文本地化](https://github.com/vinvcn/addyosmani-agent-skills-zh) vendor。NexusKit 在此基础上做小修、命令封装与子智能体扩展。`/nk-init` 的交互骨架参考 [Matt Pocock 的 Skills](https://github.com/mattpocock/skills)。具体对应见 [技能来源](docs/skill-sources.md)，版权与许可证见 [NOTICE](NOTICE)。

## 许可证

[MIT](LICENSE)。上游归属见 [NOTICE](NOTICE) 与 [LICENSE.upstream](LICENSE.upstream)。