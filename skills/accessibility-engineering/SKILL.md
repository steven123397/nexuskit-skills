---
name: accessibility-engineering
description: Audits existing interfaces for WCAG 2.2 AA conformance and remediates the violations found. Use when auditing a page or component for accessibility, running axe-core or pa11y, triaging a11y violations, or checking screen reader and contrast issues before shipping.
---

# Accessibility Engineering

## 概览

无障碍（Accessibility）不是上线前的润色步骤——在许多司法辖区它是法定合规要求，也是硬性的工程质量标准和发布前提。本 skill 用于审计现有界面、对发现的违规项进行分诊（triage），并修复已确认的问题。目标是借助自动化工具与人工测试，达成 WCAG 2.2 AA 合规。

## 何时使用

- 发布需要无障碍审计的用户侧界面变更之前
- 收到 a11y 问题反馈时（例如“屏幕阅读器读不出来”“键盘导航坏了”）
- 对现有界面执行合规审计时
- 对 axe-core 或 pa11y 报告的违规项做分诊时
- 修复已确认的无障碍违规项时

**何时不使用：** 从零构建新的 UI 组件时，请使用 `frontend-ui-engineering` 获取组件构建指南。不适用于纯后端变更、CLI 工具或无 UI 输出的库代码。

## 流程

### 阶段 1：将新建 UI 路由到前端构建 skill

组件构建、交互模式与焦点管理指南请直接使用 `frontend-ui-engineering` skill，不要在这里重复。待界面已存在、需要审计或修复时，再回到本流程。

### 阶段 2：运行自动化审计

按以下顺序执行自动化无障碍检查：

```bash
# 通过固定版本的 @axe-core/cli 运行 axe-core 规则（axe-core 包本身不带 CLI）
npx --yes @axe-core/cli@4.13.0 http://localhost:3000 --exit

# 保存 JSON 报告供 accessibility-auditor 使用
npx --yes @axe-core/cli@4.13.0 http://localhost:3000 --dir ./a11y-reports --save axe.json

# 使用固定版本的 pa11y 进行 HTML 校验（通过 HTML_CodeSniffer 执行 WCAG2AA 规则）
npx --yes pa11y@9.1.1 http://localhost:3000
```

如需合并报告，运行 `bash skills/accessibility-engineering/scripts/audit-a11y.sh url <url> --json`。该脚本会依次调用上述两个固定版本工具、记录各自状态与版本；只要任一工具未能产出有效报告，脚本会直接失败退出，而不是误报“零违规”。

按严重度分组审阅违规项：
- **Critical** —— 完全阻断屏幕阅读器访问（信息类图片缺少 `alt`、空按钮）
- **Serious** —— 导致内容难以或无法访问（对比度不足、表单缺少标签）
- **Moderate** —— 造成困惑或额外操作成本（标题跳级、冗余 ARIA）
- **Minor** —— 外观细节或渐进增强项（内嵌元素缺少 `lang` 属性）

对每条违规项，在浏览器中检查对应元素，确认是真实问题而非误报。

### 阶段 3：人工测试

自动化检查只是冒烟测试，不能证明完全合规。必须完成以下人工审计。

**键盘审计：**
1. 用 Tab 遍历每个交互元素——能否清楚看到当前焦点位置？
2. 用 Enter / Space 激活按钮和链接
3. 用 Escape 关闭模态框
4. 用方向键浏览列表
5. 确认不存在键盘陷阱（keyboard traps）

**屏幕阅读器审计（macOS 用 VoiceOver，Windows 用 NVDA）：**
1. 按标题导航（VoiceOver：`Ctrl+Option+Cmd+H`）——标题结构是否符合逻辑？
2. 按地标（landmark）导航（`Ctrl+Option+U` 打开转子并选择 Landmarks）——各区域是否有清晰标签？
3. 按链接导航（`Ctrl+Option+U` 打开转子并选择 Links）——脱离上下文后链接文案是否仍能看懂？
4. 操作表单——标签是否正确播报？错误提示是否会被读出？
5. 触发动态内容更新——变化是否被播报？

**视觉审计：**
1. 核对色彩对比度（正文 4.5:1、大字号文本 3:1、UI 组件 3:1）
2. 放大至 200%——布局是否错乱或重叠？
3. 在强制配色 / 高对比度模式（Windows High Contrast）下测试
4. 开启减弱动态效果（`prefers-reduced-motion`）——动画是否被抑制或关闭？
5. 检查焦点可见性——焦点环（focus ring）在各类背景下是否都清晰可见？

### 阶段 4：修复违规项

对每个发现按以下顺序修复：

1. **修复根因** —— 把 `<div>` 换成 `<button>`、补齐 `<label>`、设置 `alt` 文本
2. **用 ARIA 搭桥** —— 仅在原生 HTML 无法表达该交互模式时，再补充 ARIA 属性
3. **验证修复** —— 重新运行自动化检查并做人工验证

以无障碍检查清单（`../../references/accessibility-checklist.md`）作为最低基线。

## 常见合理化借口

| 合理化借口 | 现实 |
|---|---|
| “无障碍以后再补” | 推迟修复会在组件间不断叠加债务，并可能带来法律风险。发布前就该审计。 |
| “自动化工具已经把问题都抓出来了” | 自动化检查无法证明键盘操作和屏幕阅读器体验。人工测试是必选项。 |
| “屏幕阅读器用户只占极少数” | 无障碍是硬性要求，不是按用户占比算账。键盘导航、字幕和清晰结构同样惠及各类场景下的用户。 |
| “这是内部工具，不需要做 a11y” | 内部工具同样受法规约束，残障员工和外包合作方同样需要正常使用。 |
| “我到处加上 aria-label 就行了” | ARIA 是桥梁，不是地基。语义化 HTML 永远优先。滥用 ARIA 会增加维护负担，甚至让体验更糟。 |
| “设计系统已经处理好无障碍了” | 设计系统只提供无障碍基础原语，最终产物是否无障碍取决于你如何组合它们。 |
| “axe-core 已经通过了，收工” | 把 axe-core 当作冒烟测试，之后仍需用屏幕阅读器和键盘实测。Lighthouse 全绿不代表真正过关。 |

## 危险信号

- 看起来可点击、但无法通过键盘聚焦的元素
- 仅靠颜色传达状态（红表错误、绿表成功）
- 移除了焦点轮廓（focus outline）却未提供可见替代样式
- 表单输入框缺少标签
- 没有标题层级或出现跳级
- 空的或未标注名称的按钮和链接
- 模态框打开时不锁定焦点，或关闭时不恢复焦点
- 有意义的图片缺少 `alt` 文本（或装饰性图片漏写 `alt=""`）
- 触控目标未达到 SC 2.5.8 的 24×24 CSS px 尺寸或间距要求，且不符合例外规则（AA；44×44 为 AAA 目标，SC 2.5.5）
- 自动播放且没有控制按钮的视频或音频
- 低对比度文本（尤其是 hover、disabled 状态和 placeholder）

## 另见

- `../../references/accessibility-checklist.md` —— WCAG 2.2 AA 快速检查清单
- `frontend-ui-engineering` —— 从一开始就构建无障碍组件
- `accessibility-auditor`（`agents/accessibility-auditor.md`）—— 用于深度审查的专用 a11y 审计 persona

## 验证

完成无障碍审计与修复流程后：

- [ ] 自动化审计通过，无 Critical 或 Serious 违规项
- [ ] 所有可交互元素均支持键盘操作（Tab、Enter、Escape、方向键）
- [ ] 已使用具名的浏览器 + 辅助技术（AT）组合验证按标题、地标和链接的屏幕阅读器导航（若未实测则标记为 `manual` 且未测试，绝不报告为已验证）
- [ ] 焦点顺序与视觉顺序一致
- [ ] 色彩对比度达标（正文 4.5:1 / 大字号文本 3:1 / UI 组件 3:1）
- [ ] 所有表单输入框均有关联标签
- [ ] 所有图片均有恰当的 `alt` 文本
- [ ] 动态内容变化会被播报（`aria-live`）
- [ ] 页面放大至 200% 时仍可正常使用且无内容丢失
- [ ] 触控目标满足 SC 2.5.8 的 24×24 CSS px 尺寸或间距要求，或符合规范例外（AA）；44×44 为增强级 AAA 目标（SC 2.5.5）
