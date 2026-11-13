---
name: frontend-ui-engineering
description: Builds production-quality, accessible, responsive user-facing UIs. Use when building or modifying interfaces and pages, creating components, implementing layouts, meeting WCAG accessibility requirements, managing state, or when the output needs to look and feel production-quality rather than AI-generated.
---

# Frontend UI Engineering

## 概览

打造具备无障碍可访问性、高性能且视觉打磨到位的生产级用户界面。目标很明确：让界面看起来像是顶级团队里懂设计的工程师亲手打造的作品，而不是 AI 一键生成的大路货。这意味着真正落地设计系统、落实无障碍规范、设计周全的交互细节，彻底摆脱那种千篇一律的 “AI 味审美（AI aesthetic）”。

## 何时使用

- 构建新的 UI 组件或页面
- 修改现有面向用户的界面
- 实现响应式布局
- 添加交互或状态管理
- 修复视觉或 UX 问题

## 组件架构

### 文件结构

把所有与组件相关的东西放在一起（colocate）：

```
src/components/
  TaskList/
    TaskList.tsx          # Component implementation
    TaskList.test.tsx     # Tests
    TaskList.stories.tsx  # Storybook stories (if using)
    use-task-list.ts      # Custom hook (if complex state)
    types.ts              # Component-specific types (if needed)
```

### 组件模式

**优先组合而非配置：**

```tsx
// Good: Composable
<Card>
  <CardHeader>
    <CardTitle>Tasks</CardTitle>
  </CardHeader>
  <CardBody>
    <TaskList tasks={tasks} />
  </CardBody>
</Card>

// Avoid: Over-configured
<Card
  title="Tasks"
  headerVariant="large"
  bodyPadding="md"
  content={<TaskList tasks={tasks} />}
/>
```

**保持组件职责聚焦：**

```tsx
// Good: Does one thing
export function TaskItem({ task, onToggle, onDelete }: TaskItemProps) {
  return (
    <li className="flex items-center gap-3 p-3">
      <Checkbox checked={task.done} onChange={() => onToggle(task.id)} />
      <span className={task.done ? 'line-through text-muted' : ''}>{task.title}</span>
      <Button variant="ghost" size="sm" onClick={() => onDelete(task.id)}>
        <TrashIcon />
      </Button>
    </li>
  );
}
```

**数据获取与展示分离：**

```tsx
// Container: handles data
export function TaskListContainer() {
  const { tasks, isLoading, error, refetch, toggleTask, deleteTask } = useTasks();

  if (isLoading) return <TaskListSkeleton />;
  if (error) return <ErrorState message="Failed to load tasks" retry={refetch} />;
  if (tasks.length === 0) return <EmptyState message="No tasks yet" />;

  return <TaskList tasks={tasks} onToggle={toggleTask} onDelete={deleteTask} />;
}

// Presentation: handles rendering
export function TaskList({ tasks, onToggle, onDelete }: { tasks: Task[] } & Pick<TaskItemProps, 'onToggle' | 'onDelete'>) {
  return (
    <ul role="list" className="divide-y">
      {tasks.map(task => <TaskItem key={task.id} task={task} onToggle={onToggle} onDelete={onDelete} />)}
    </ul>
  );
}
```

## 状态管理

**选择能工作的最简单方案：**

```
Local state (useState)           → Component-specific UI state
Lifted state                     → Shared between 2-3 sibling components
Context                          → Theme, auth, locale (read-heavy, write-rare)
URL state (searchParams)         → Filters, pagination, shareable UI state
Server state (React Query, SWR)  → Remote data with caching
Global store (Zustand, Redux)    → Complex client state shared app-wide
```

**不要让 props 穿透超过 3 层。** 如果你在不使用这些 props 的组件之间层层传递，就引入 context 或重构组件树。

## 遵循设计系统

### 参考驱动的 UI 质量

当产品需要一种独特的视觉方向时，先收集证据，再选定布局：

1. 查阅一份可信的设计参考库，或直接使用产品团队提供的参考案例。
2. 仔细拆解两到三个相关界面，记录下关于视觉层级、信息密度、导航方式、交互控件、响应式行为及各种交互状态的决策。
3. 在动手写代码之前，把这些决策浓缩成一份简短的设计契约：写明这个界面的核心职责、主操作路径、必需状态、响应式规则，以及明确要规避的坏模式。
4. 用产品自有的组件、design tokens、文案内容与视觉语言，重构并吸收其中真正管用的布局结构。绝不照搬其他产品的品牌标识、专有文案、图片资产或像素级抄袭布局。

把参考当作证据，而不是模板。如果拿不到参考，把你的假设记录下来，并对照产品既有的设计系统验证结果。

### 避开 AI 审美

AI 生成的 UI 有可辨识的套路。把它们全部避开：

| AI 默认做法 | 为什么是问题 | 生产级水准 |
|---|---|---|
| 满屏紫色/靛蓝 | 模型默认选用视觉上"安全"的配色，让每个 app 看起来都一样 | 使用项目实际的调色板 |
| 滥用渐变 | 渐变增加视觉噪音，且与多数设计系统冲突 | 与设计系统匹配的扁平或克制的渐变 |
| 万物圆角（rounded-2xl） | 一味拉满大圆角看似“亲切友好”，却破坏了真实设计中圆角半径应有的层级比例 | 严格遵循设计系统中一致的 border-radius 规范 |
| 千篇一律的 hero 区块 | 套模板式布局，与实际业务内容和用户核心诉求毫无关联 | 采用内容优先的布局结构 |
| Lorem ipsum 式假文案 | 假占位文案会掩盖真实内容才会暴露出的排版问题（如长度、换行、文本溢出） | 使用贴近真实业务场景的占位内容 |
| 到处都是过大的 padding | 处处留出均等且过宽的内边距，会彻底毁掉视觉层级并浪费屏幕空间 | 使用统一的间距刻度 |
| 样板化的均等卡片网格 | 千篇一律的均质卡片网格只是布局偷懒的捷径，无视信息优先级与用户的视觉扫视路径 | 采用目标驱动的差异化布局 |
| 滥用重阴影设计 | 层层堆叠的重阴影制造出的多余景深会与正文争抢注意力，还会拖慢低端设备的渲染性能 | 除非设计系统明确指定，否则使用克制阴影或无阴影 |

### 间距与布局

使用一致的间距刻度，不要凭空发明数值：

```css
/* Use the scale: 0.25rem increments (or whatever the project uses) */
/* Good */  padding: 1rem;      /* 16px */
/* Good */  gap: 0.75rem;       /* 12px */
/* Bad */   padding: 13px;      /* Not on any scale */
/* Bad */   margin-top: 2.3rem; /* Not on any scale */
```

### 排版

尊重标题层级：

```
h1 → Page title (one per page)
h2 → Section title
h3 → Subsection title
body → Default text
small → Secondary/helper text
```

不要跳过标题层级。不要给非标题内容使用标题样式。

### 颜色

- 使用语义化颜色 token：`text-primary`、`bg-surface`、`border-default`，而不是原始 hex 值
- 确保足够对比度（正文 4.5:1，大字号文本 3:1）
- 不要只靠颜色传达信息（同时使用图标、文本或图案）

## 可访问性（WCAG 2.1 AA）

每个组件都必须达到这些标准：

### 键盘导航

```tsx
// Every interactive element must be keyboard accessible
<button onClick={handleClick}>Click me</button>        // ✓ Focusable by default
<div onClick={handleClick}>Click me</div>               // ✗ Not focusable
<div role="button" tabIndex={0} onClick={handleClick}    // ✓ But prefer <button>
     onKeyDown={e => {
       if (e.key === 'Enter') handleClick();
       if (e.key === ' ') e.preventDefault();
     }}
     onKeyUp={e => {
       if (e.key === ' ') handleClick();
     }}>
  Click me
</div>
```

### ARIA 标签

```tsx
// Label interactive elements that lack visible text
<button aria-label="Close dialog"><XIcon /></button>

// Label form inputs
<label htmlFor="email">Email</label>
<input id="email" type="email" />

// Or use aria-label when no visible label exists
<input aria-label="Search tasks" type="search" />
```

### 焦点管理

```tsx
// Move focus when content changes
function Dialog({ isOpen, onClose }: DialogProps) {
  const closeRef = useRef<HTMLButtonElement>(null);

  useEffect(() => {
    if (isOpen) closeRef.current?.focus();
  }, [isOpen]);

  // Trap focus inside dialog when open
  return (
    <dialog open={isOpen}>
      <button ref={closeRef} onClick={onClose}>Close</button>
      {/* dialog content */}
    </dialog>
  );
}
```

### 有意义的空状态和错误状态

```tsx
// Don't show blank screens
function TaskList({ tasks, onCreateTask }: { tasks: Task[]; onCreateTask: () => void }) {
  if (tasks.length === 0) {
    return (
      <div role="status" className="text-center py-12">
        <TasksEmptyIcon className="mx-auto h-12 w-12 text-muted" />
        <h3 className="mt-2 text-sm font-medium">No tasks</h3>
        <p className="mt-1 text-sm text-muted">Get started by creating a new task.</p>
        <Button className="mt-4" onClick={onCreateTask}>Create Task</Button>
      </div>
    );
  }

  return <ul role="list">...</ul>;
}
```

## 响应式设计

移动优先设计，再向大屏扩展：

```tsx
// Tailwind: mobile-first responsive
<div className="
  grid grid-cols-1      /* Mobile: single column */
  sm:grid-cols-2        /* Small: 2 columns */
  lg:grid-cols-3        /* Large: 3 columns */
  gap-4
">
```

在这些断点测试：320px、768px、1024px、1440px。

## 加载与过渡

```tsx
// Skeleton loading (not spinners for content)
function TaskListSkeleton() {
  return (
    <div className="space-y-3" role="status" aria-busy="true" aria-label="Loading tasks">
      {Array.from({ length: 3 }).map((_, i) => (
        <div key={i} className="h-12 bg-muted animate-pulse rounded" />
      ))}
    </div>
  );
}

// Optimistic updates for perceived speed
function useToggleTask() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: toggleTask,
    onMutate: async (taskId) => {
      await queryClient.cancelQueries({ queryKey: ['tasks'] });
      const previous = queryClient.getQueryData(['tasks']);

      queryClient.setQueryData(['tasks'], (old: Task[]) =>
        old.map(t => t.id === taskId ? { ...t, done: !t.done } : t)
      );

      return { previous };
    },
    onError: (_err, _taskId, context) => {
      queryClient.setQueryData(['tasks'], context?.previous);
    },
  });
}
```

## 另见

详细的可访问性要求和测试工具见 `../../references/accessibility-checklist.md`。

## 常见合理化借口

| 合理化借口 | 现实 |
|---|---|
| "可访问性是锦上添花" | 在许多国家和地区它是法定合规要求，也是硬性的工程质量标准。 |
| "我们以后再做成响应式的" | 事后硬补响应式设计的难度是从一开始就按响应式编写的 3 倍。 |
| "设计还没定稿，先跳过样式" | 先采用设计系统的默认样式。毫无样式的半成品 UI 会给审阅者留下“页面坏掉了”的第一印象。 |
| "这只是个原型" | 原型迟早会演变成生产代码，从一开始就要把地基打对。 |
| "AI 审美暂时没问题" | 这种套模板观感会直接给人粗制滥造的低质量印象。一开始就该接入项目真实的设计系统。 |

## 危险信号

- 超过 200 行的庞大组件（拆小它）
- 随手写死的内联样式或拍脑袋凑出来的像素值
- 缺少错误状态、加载状态或空状态
- 没有做过键盘导航测试
- 把颜色作为状态的唯一标识（仅靠红/绿区分，没有配文字或图标）
- 千篇一律的 “AI 味” 外观（满屏紫蓝渐变、超大圆角卡片、样板化堆砌布局）

## 验证

构建完 UI 后：

- [ ] 组件渲染时 console 无报错
- [ ] 所有可交互元素都支持键盘访问（用 Tab 键遍历页面）
- [ ] 屏幕阅读器能传达页面的内容和结构
- [ ] 响应式：在 320px、768px、1024px、1440px 均正常
- [ ] 加载、空状态、错误、成功和权限状态在适用时全部处理
- [ ] 遵循项目的设计系统（间距、颜色、排版）
- [ ] 最终渲染结果通过一次 UI 专属的收尾审查（finish-gate review）
- [ ] dev tools 或 axe-core 中没有可访问性告警
