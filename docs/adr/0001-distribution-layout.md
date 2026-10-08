# 三形态分发共用同一 skills/ 布局

仓库布局即分发布局：`skills/engineering/`、`skills/productivity/` 分组平铺，Kimi 插件、Codex 插件与 npx skills CLI 三种形态共用同一棵树。三形态对"共享内容如何到达用户机器"的处理能力不同，平级布局让三者的相对几何一致、零引用改写；代价是正式支持整套安装，不支持单技能独立安装。放弃的两个备选：构建期把共享内容内联进各技能（引入生成管线与漂移面）、改引用深度为更深层相对路径（junction 加载侧与插件侧深度不一致，必有一侧失效）。

关键事实：skills CLI 只安装含合规 SKILL.md 的目录，且按 frontmatter `name` 命名安装目录、平铺到 `.agents/skills/`。因此 `name` 必须与目录同名、description 中的 `: ` 必须加引号（严格 YAML 消费方存在），两项均由 run_checks 锁定。Codex 市场安装的必需文件是 `.agents/plugins/marketplace.json`（不是 `.codex-plugin/plugin.json`，后者是插件清单），缺它报 "marketplace root does not contain a supported manifest"。

旧版曾让 `skills/conventions/` 带最小 SKILL.md 作为第 18 个可安装单元随套件分发，供各技能相对引用。集中 conventions 已随 STE-30 退役：技能就近持有材料，跨技能走公开入口，不再有该安装单元。已知环境问题：Kimi 的 GitHub URL 安装在 Windows 上最后一步临时目录 rename 可能 EPERM（Defender 对带 Mark-of-the-Web 文件的瞬态锁），与网络、清单无关，同一 URL 在 WSL 安装成功；兜底是本地路径安装或重试。

初版 2026-09-26（原文在 Git 历史 `docs/solutions/architecture-decisions/2026-09-26-distribution-layout.md`），conventions 部分随骨架重写修订。目录与加载边界见 [ADR-0002](0002-skill-layout.md)。设计依据：[STE-16](https://linear.app/steven-liang/issue/STE-16)、[STE-30](https://linear.app/steven-liang/issue/STE-30)。
