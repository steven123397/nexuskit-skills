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
- [nk-implement](skills/engineering/nk-implement/SKILL.md)：完成单个 ticket 或任务：实施、验证、审查处理与提交。
- [nk-tdd](skills/engineering/nk-tdd/SKILL.md)：测试纪律：好测试标准、反模式与数量控制；由实施与审查流程自动调用。
- [nk-to-spec](skills/engineering/nk-to-spec/SKILL.md)：将已讨论的内容整理为 spec，发布到 Linear。
- [nk-commit](skills/engineering/nk-commit/SKILL.md)：本地提交统一入口：核对范围、保护无关工作、执行必要检查并按约定写提交说明。
- [nk-write](skills/productivity/nk-write/SKILL.md)：面向人的中文技术文本写作与润色：自然、准确、易读，事实一字不丢。
<!-- /installable-skills -->

以上仅表示已有真实入口文件，不表示本轮整体已验收或发布。其他目录暂不暴露技能入口：已有旧稿保留为 `SKILL.legacy.md`，新技能只有目录占位。后续逐项讨论正文、审阅后再启用。

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
    nk-retro/            nk-write/            nk-wait-what/
    nk-wizard/           nk-ask-ljq/
```

每个可用技能以 `SKILL.md` 为入口；模板、示例、审查提示词、脚本和资产按实际需要就近放置。没有集中式 conventions 运行依赖，跨技能使用公开技能名，不读取另一个技能的私有文件。

- [AGENTS.md](AGENTS.md)：本仓库的开发和验证约定。
- [CONCEPTS.md](CONCEPTS.md)：领域术语。
- [docs/decisions/](docs/decisions/)：关键架构决定。
- [技能来源](docs/skill-sources.md)：采用的上游材料。
- [docs/releases/](docs/releases/)：版本说明。

内部 spec、ticket 和进度在 Linear，外部反馈在 GitHub Issues，背景与经验在 OpenViking，代码与合入事实在 Git/PR。仓库不再维护实时状态文档。旧 solutions 及其他历史材料暂保留供迁移，不是新版执行规则。

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
