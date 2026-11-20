---
description: 通过 accessibility-auditor persona 运行无障碍审计
disable-model-invocation: true
---

调用 accessibility-engineering skill。

`/nk-a11y` 运行一次专用的无障碍审计，检查键盘导航、屏幕阅读器支持、色彩对比度、表单标签以及结构性 WCAG 2.2 AA 合规性。

## 确定模式

**Deep 模式** —— 以下任意一项可用时激活：
- 一份 axe-core 或 pa11y JSON 报告文件（可通过 `bash skills/accessibility-engineering/scripts/audit-a11y.sh url <url> --json` 生成）
- 一个可访问的线上 URL —— agent 可以指导用户运行上述审计脚本
- Chrome DevTools MCP（用于实时 DOM 检查、对比度校验与渲染分析）

**Quick 模式** —— 没有工具输出时的默认模式。扫描源代码中的结构性反模式（缺少标签、用 `div` 当按钮、缺少 `alt` 文本、标题跳级等）。

## 运行审计

启动 `accessibility-auditor` subagent。显式传入以下信息：

- 待审查的文件、组件或 diff
- 任何产物路径（axe-core JSON、pa11y JSON、审计脚本输出）
- 已知时的目标 URL 或组件名称
- 说明你期望使用哪种模式（Quick 或 Deep），这样若原本意图是 Deep，agent 会主动指出缺少的输入

该 subagent 返回一份 WCAG scorecard、按严重度排序的 findings 列表、正面观察，以及带代码示例的修复建议。

## 输出

把完整的审计报告返回给用户。不需要综合或合并步骤 —— 这是一个单 persona 命令。
