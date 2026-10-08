# NexusKit (`nk-*`)

面向 AI 编程 Agent 的个人工程技能工具箱，以 Matt Pocock 式简洁组织为基础。技能按实际需要调用，主流程直接写在入口中。

当前正式版仍为 [v0.2.0](docs/releases/v0.2.0.md)。本工作分支正在重写下一版；下面展示开发结构，不代表完整新版已经可用。

## 可安装入口

<!-- installable-skills -->
- [nk-grill](skills/engineering/nk-grill/SKILL.md)：追问设计和需求，达成共同理解。
- [nk-wayfinder](skills/engineering/nk-wayfinder/SKILL.md)：在 Linear 中组织大型目标的待定问题，按依赖推进讨论与研究。
- [nk-research](skills/engineering/nk-research/SKILL.md)：围绕明确的研究问题取证，形成有来源、能支撑取舍的结论。
- [nk-prototype](skills/engineering/nk-prototype/SKILL.md)：用可操作的一次性原型回答设计问题，记录结论与适用限制。
- [nk-to-tickets](skills/engineering/nk-to-tickets/SKILL.md)：把 spec 或对话拆成带依赖的纵向切片 tickets，发布到 Linear。
- [nk-init](skills/engineering/nk-init/SKILL.md)：项目首次接入：探测现状、配置 Linear 与 GitHub 去向、幂等写入导航指针与工作流配置。
- [nk-implement](skills/engineering/nk-implement/SKILL.md)：完成单个 ticket 或任务：实施、验证、审查处理与提交。
- [nk-odyssey](skills/engineering/nk-odyssey/SKILL.md)：接住已明确的 spec，在集成分支上协调并行实施与集成，交付整体验收。
- [nk-spec-close](skills/engineering/nk-spec-close/SKILL.md)：spec 整体验收与关闭：走完整使用场景、查跨 ticket 衔接，通过即关票不等合并，并清理临时工作树。
- [nk-pr](skills/engineering/nk-pr/SKILL.md)：分支交付收尾：draft PR 创建与更新、审查与验收结论复用、合并条件确认、授权合并与交付资源清理。
- [nk-tdd](skills/engineering/nk-tdd/SKILL.md)：测试纪律：好测试标准、反模式与数量控制；由实施与审查流程自动调用。
- [nk-codecraft](skills/engineering/nk-codecraft/SKILL.md)：代码纪律：七条规范融合深模块词汇与判据；由实施与审查流程自动调用。
- [nk-to-spec](skills/engineering/nk-to-spec/SKILL.md)：将已讨论的内容整理为 spec，发布到 Linear。
- [nk-review](skills/engineering/nk-review/SKILL.md)：三轴独立审查：需求符合性、实现正确性、简洁性与可维护性；返回发现不修复，未受影响的结论直接复用。
- [nk-debug](skills/engineering/nk-debug/SKILL.md)：诊断与修复：先建复现回路再追根因，仅诊断或授权修复都走通，修复后过审查轻量提交。
- [nk-commit](skills/engineering/nk-commit/SKILL.md)：本地提交统一入口：核对范围、保护无关工作、执行必要检查并按约定写提交说明。
- [nk-domain-modeling](skills/engineering/nk-domain-modeling/SKILL.md)：领域建模：澄清与锤炼术语、压测概念边界、把敲定的术语与关键决定落成简短文档。
- [nk-to-issue](skills/engineering/nk-to-issue/SKILL.md)：核实发现并记录为 GitHub Issue（bug/enhancement），查重与证据先行；记录不安排执行。
- [nk-prose](skills/productivity/nk-prose/SKILL.md)：面向人的中文技术文本写作与润色：自然、准确、易读，事实一字不丢。
- [nk-wait-what](skills/productivity/nk-wait-what/SKILL.md)：解释没讲清楚的部分：用平实语言和项目术语重述目标、结论、依据与待对齐项。
- [nk-wizard](skills/productivity/nk-wizard/SKILL.md)：生成交互式 bash 向导，带人走完只有人能执行的手动流程（凭据、provisioning、cutover）。
- [nk-ask-ljq](skills/productivity/nk-ask-ljq/SKILL.md)：场景路由：说出卡在哪里，给一个首选入口与预期结果；不强制固定流程。
- [nk-retro](skills/productivity/nk-retro/SKILL.md)：复盘 Agent 工作环境与协作：基于真实记录总结可行动改进；按请求写入 OpenViking 并验证。
<!-- /installable-skills -->

以上为全部 23 个技能的真实入口。整轮重写已完成正文与清单，尚未做真实客户端的整体验收与发布（见 STE-15）。

## 目录

```text
skills/
  engineering/
    nk-init/             nk-grill/            nk-wayfinder/
    nk-domain-modeling/  nk-research/         nk-prototype/
    nk-to-spec/          nk-to-tickets/       nk-implement/
    nk-odyssey/          nk-review/           nk-spec-close/
    nk-commit/           nk-pr/               nk-debug/
    nk-to-issue/
  productivity/
    nk-retro/            nk-prose/            nk-wait-what/
    nk-wizard/           nk-ask-ljq/
```

每个可用技能以 `SKILL.md` 为入口；模板、示例、审查提示词、脚本和资产按实际需要就近放置。没有集中式 conventions 运行依赖，跨技能使用公开技能名，不读取另一个技能的私有文件。

- [AGENTS.md](AGENTS.md)：本仓库的开发和验证约定。
- [CONCEPTS.md](CONCEPTS.md)：领域术语。
- [docs/adr/](docs/adr/)：关键架构决定。
- [技能来源](docs/skill-sources.md)：采用的上游材料。
- [docs/releases/](docs/releases/)：版本说明。

内部 spec、ticket 和进度在 Linear，外部反馈在 GitHub Issues，背景与经验在 OpenViking，代码与合入事实在 Git/PR。仓库不再维护实时状态文档。旧 solutions 与发想、讨论材料已按 STE-13 迁移（背景归 OpenViking，正式决定归 [docs/adr/](docs/adr/)），v0.2.0 发布证据保留在 docs/plans 与 docs/reviews。

## 安装

正式版仍通过已有分发方式安装；重装当前开发分支只会发现上面列出的入口，不会恢复完整的 v0.2.0 工具箱。

### Kimi Code

```text
/plugins install https://github.com/steven123397/nexuskit-skills
```

清单见 [.kimi-plugin/plugin.json](.kimi-plugin/plugin.json)。

### Codex

```bash
codex plugin marketplace add steven123397/nexuskit-skills
codex plugin add nexuskit@nexuskit-skills
```

清单见 [.codex-plugin/plugin.json](.codex-plugin/plugin.json)，市场入口见 [.agents/plugins/marketplace.json](.agents/plugins/marketplace.json)。

### skills CLI

```bash
npx skills add steven123397/nexuskit-skills
```

技能统一从 `skills/` 下发现；只有 `SKILL.md` 是入口，目录占位和旧稿不是技能。安装后的客户端使用安装快照，仓库改动不会自动更新已安装版本。

## 许可证

[MIT](LICENSE)。上游归属见 [NOTICE](NOTICE)。
