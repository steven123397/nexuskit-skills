---
description: 启动 spec-driven development — 写代码前先编写结构化 specification
disable-model-invocation: true
---

调用 spec-driven-development skill。

先理解用户想构建什么。围绕以下内容提出澄清问题（clarifying questions）：
1. 目标（objective）与目标用户
2. 核心功能与验收标准（acceptance criteria）
3. 技术栈偏好与约束条件
4. 已知边界（哪些事始终要做、哪些事需先询问确认、哪些事绝不能做）

然后生成结构化 spec，覆盖六个核心领域：objective、commands、project structure、code style、testing strategy 和 boundaries。

如果请求捆绑了多个可独立测试的能力模块（capabilities），先按该 skill 的 Phase 0 提出一份 capability map（module ids、依赖方向、构建顺序）并获得批准，然后再按依赖顺序为每个模块编写 spec。

将 spec 保存为项目根目录中的 SPEC.md，并在继续前与用户确认。

若 AGENTS.md/CLAUDE.md 声明了外部 spec 工具，按该工具的目录与格式产出，不另建 `SPEC.md`。
