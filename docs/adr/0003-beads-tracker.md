# 内部跟踪由 Linear 切换为 beads

内部需求与状态跟踪从 Linear 切换到 beads（`bd`），仓库内 `.beads/` 为唯一来源，不再向 Linear 写入。旧票不做映射或导入，beads 以空库为全新基底；旧票号（STE-*）只在 ADR 与历史发布说明中作为索引保留，不再指向可访问的票。

切换的理由是跟踪数据与代码同仓库、依赖与阻塞关系由工具原生表达、CLI 可离线读写且 agent 能直接操作，不必依赖外部 SaaS 与 MCP 会话。代价是失去 Linear 的跨项目看板与 Web 协作界面，对外反馈仍由 GitHub Issues 承接。

配置层面，`bd init` 建立 `.beads/`（embedded Dolt，Dolt 远端随 `origin` 同步），agent profile 设为 team-maintainer，仅在明确授权时由 agent 完成收尾提交；`no-git-ops` 关闭。AGENTS.md 的「项目约定」记录 task 位置与唯一来源。

不做的事：旧票迁移、Linear 双写、保留本地副本。Linear 层旧技能（nk-to-spec、nk-to-tickets、nk-to-issue、nk-wayfinder）的票流职责由 plan 与 beads 承接。

初版 2026-11-01。