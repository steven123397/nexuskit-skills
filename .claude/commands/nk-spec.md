---
description: 启动 spec-driven development — 写代码前先编写结构化 specification
disable-model-invocation: true
---

调用 spec-driven-development skill。

先检查项目根目录是否已存在 `SPEC.md`——这决定了接下来走哪条流程。

**新建 spec**（尚无 `SPEC.md`，或本次需求与现有 `SPEC.md` 描述的内容无关）：先理解用户想构建什么。围绕以下内容提出澄清问题（clarifying questions）：
1. 目标（objective）与目标用户
2. 核心功能与验收标准（acceptance criteria）
3. 技术栈偏好与约束条件
4. 已知边界（哪些事始终要做、哪些事需先询问确认、哪些事绝不能做）

然后生成结构化 spec，覆盖六个核心领域：objective、commands、project structure、code style、testing strategy 和 boundaries。

如果请求捆绑了多个可独立测试的能力模块（capabilities），先按该 skill 的阶段 0 提出一份 capability map（module ids、依赖方向、构建顺序）并获得批准，然后再按依赖顺序为每个模块编写 spec。

将 spec 保存为项目根目录中的 `SPEC.md`，并在继续前与用户确认。

**Delta spec**（`SPEC.md` 已存在，且本次需求是对其中内容的变更）：不要覆盖原 `SPEC.md`——按该 skill 的「Spec 演进」一节单写一份 delta spec（例如 `SPEC-<change-slug>.md`），只覆盖发生变化的部分，并在继续前与用户确认。

若 AGENTS.md/CLAUDE.md 声明了外部 spec 工具，按该工具的目录与格式产出，不另建 `SPEC.md`。
