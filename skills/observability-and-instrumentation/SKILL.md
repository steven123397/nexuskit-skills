---
name: observability-and-instrumentation
description: Instruments code so production behavior is visible and diagnosable. Use when adding logging, metrics, tracing, or alerting. Use when shipping any feature that runs in production and you need evidence it works. Use when production issues are reported but you can't tell what happened from the available data.
---

# Observability and Instrumentation

## 概览

观测不到的代码，就谈不上运维。可观测性（observability）是指：借助代码发出的 telemetry（遥测数据），从系统外部回答“系统正在做什么、为什么”。埋点不是上线后的附加项——它和功能代码一起写，就像写测试一样。如果一个功能在没有 telemetry 的情况下直接上线，第一个用户上报的 bug 就会变成翻日志考古，而不是一条查询就能定位的问题。

## 何时使用

- 构建任何会跑在生产环境的功能
- 新增服务、endpoint、后台 job 或外部集成
- 一次生产事故花了太久才定位清楚（当时“根本看不出到底发生了什么”）
- 建立或评审告警规则
- 评审包含新增 I/O、重试、队列或跨服务调用的 PR

**不适用于：**
- 诊断正在发生的故障——请用 `debugging-and-error-recovery` skill（可观测性正是让下次排障能跑得快的前提）
- 对已测出的慢做 profiling 和调优——请用 `performance-optimization` skill
- 发布日的监控 checklist 与回滚触发器——见 `shipping-and-launch` skill；本 skill 覆盖的是为它们提供数据支撑的那层埋点

## 流程

### 1. 先定义“能工作”，再埋点

没有预设问题支撑的 telemetry 全是噪音。在添加任何埋点之前，先写下 on-call 工程师针对这个功能一定会问的 2–4 个问题：

```
FEATURE: checkout payment retry
QUESTIONS ON-CALL WILL ASK:
1. What fraction of payments succeed on first attempt vs after retry?
2. When a payment fails permanently, why? (provider error? timeout? validation?)
3. Is the payment provider slower than usual?
→ Every signal below must help answer one of these.
```

如果连这些问题都说不出来，说明你还没准备好动手埋点——你会把一切都写进日志，然后什么也捞不到。

### 2. 为每个问题选对信号

| 信号 | 回答的问题 | 成本特征 | 例子 |
|---|---|---|---|
| **结构化日志** | “这个具体请求里到底发生了什么？” | 按事件量计；随流量增长 | 带 provider 错误码的 `payment_failed` |
| **指标（Metrics）** | “聚合来看，发生得多频繁 / 跑得多快？” | 每个 series 固定开销；查询便宜 | provider 调用的 p99 延迟 |
| **Trace（链路追踪）** | “时间都花在了跨服务的哪一环？” | 按请求量计；通常会采样 | 一次变慢的 checkout，按每一跳（hop）拆开看 |

经验法则：指标告诉你**出了**什么问题，trace 告诉你问题出在**哪里**，日志则告诉你**为什么**。

### 3. 结构化日志

记录事件，不要写流水账。每一行日志都是一个 JSON object，带有稳定的事件名和机器可读的字段：

```typescript
// BAD: string interpolation — unqueryable, inconsistent
logger.info(`Payment ${id} failed for user ${userId} after ${n} retries`);

// GOOD: stable event name + structured fields
logger.warn({
  event: 'payment_failed',
  paymentId: id,
  provider: 'stripe',
  errorCode: err.code,
  attempt: n,
}, 'payment failed');
```

**日志级别——保持语义一致：**

| 级别 | 含义 | On-call 的动作 |
|---|---|---|
| `error` | 不变量被破坏；可能需要人工介入处理 | 立即调查 |
| `warn` | 出现降级但已妥善处理（如重试成功、用了 fallback） | 留意趋势 |
| `info` | 重要的业务事件（如下单完成、job 结束） | 无需处理 |
| `debug` | 用于排查的诊断细节 | 生产环境默认关闭 |

**Correlation ID 是强制要求。** 在系统入口边界生成（或沿用传入的）一个 request ID，并把它附加到每一行日志、每个 span 和每次对外调用上。没有它，面对多线程、多实例交错的日志，你根本无法还原出单次请求的完整轨迹：

```typescript
// Express: child logger per request, ID propagated downstream
app.use((req, res, next) => {
  req.id = req.headers['x-request-id'] ?? crypto.randomUUID();
  req.log = logger.child({ requestId: req.id });
  res.setHeader('x-request-id', req.id);
  next();
});
```

**多个入口写同一份日志流时，务必标出入口点（entry point）。** Correlation ID 标识“这一次运行”，却说不出是哪条代码路径发起了它。同一个 job 如果既可能被定时调度器（scheduler）、replay endpoint，也可能由人工通过 CLI 触发，它们往同一个日志汇集目标（sink）写入的日志行就会混在一起、外观毫无二致；于是查归属时只能靠排除法——交叉翻查调度器的历史记录、进程表或部署日志——而这种推断也只有在那些外围记录当时恰好尚未被清理的前提下才能成立。在任务启动的源头处、紧挨着 correlation ID 给入口点打标记，并让这两个字段沿同样的方式传播：

```typescript
// One helper for every entry point: the run's own logger carries both fields.
// `entryPoint`, not `source` — ECS reserves `source.*` for network fields.
export const runLog = (entryPoint: 'scheduler' | 'replay_endpoint' | 'cli', runId: string) =>
  logger.child({ entryPoint, requestId: runId });

// scheduler tick        -> runLog('scheduler', crypto.randomUUID())
// POST /jobs/:id/replay -> runLog('replay_endpoint', req.id)
// CLI invocation        -> runLog('cli', process.env.RUN_ID ?? crypto.randomUUID())
```

这两个字段必须随着 correlation ID 一起穿过同样的跨边界通道——队列 metadata、HTTP headers——否则下游 worker 要想知道入口点就只能重新推断、靠猜。一个仅仅和某类入口存在相关性的字段只能算线索，算不上归因凭证：只要是任何能触发这个 job 的调用方，都能复现出这个特征。

**绝不要记录 secret、token、密码或完整 PII。** 这是来自 `security-and-hardening` skill 的一条硬性规则——telemetry pipeline 是一条经典的数据泄露路径。按 allowlist 挑选要记录的字段；不要整包打印 request body。

### 4. 指标

对于请求驱动的服务，在每个 endpoint 和每个外部依赖上按 **RED** 埋点：**R**ate（请求/秒）、**E**rrors（失败率）、**D**uration（延迟 histogram，不要只算平均值）。对于资源（队列、连接池、主机），用 **USE**：**U**tilization（利用率）、**S**aturation（饱和度）、**E**rrors（错误数）。

和 tracing 一样，厂商中立的标准路径是 OpenTelemetry metrics API（与第 5 步使用同一套 SDK 和 context）。下面的例子用的是 Prometheus 的 `prom-client`——一种常见后端选择，并非唯一选择；无论哪种路径，RED/USE 模型和 cardinality 控制规则都完全相同。

```typescript
import { Histogram } from 'prom-client';

const httpDuration = new Histogram({
  name: 'http_request_duration_seconds',
  help: 'HTTP request duration',
  labelNames: ['method', 'route', 'status_class'],  // '2xx', not '200'
  buckets: [0.05, 0.1, 0.25, 0.5, 1, 2.5, 5],
});
```

**基数爆炸（Cardinality）是常见的故障元凶。** 每一组唯一的 label 组合都会生成一条独立的 time series。Label 必须取自小而固定的有限集合（route template、status class、provider 名称）。绝不要把 user ID、原始 URL、完整错误消息或其他无界值当作 label——那些信息属于日志和 trace。

```
OK as label:    route="/api/tasks/:id"   status_class="5xx"   provider="stripe"
NEVER a label:  user_id, email, request_id, full URL, error message text
```

永远不要只追踪平均值，务必追踪百分位数：平均值会掩盖那 1% 体验极差的用户。用 histogram 记录分布，读取 p50/p95/p99。

### 5. 分布式 tracing

采用 OpenTelemetry——它是厂商中立的开放标准，其 auto-instrumentation 几乎无需手写代码就能覆盖 HTTP、gRPC 和常见数据库客户端：

```typescript
// tracing.ts — must be imported before anything else
import { NodeSDK } from '@opentelemetry/sdk-node';
import { getNodeAutoInstrumentations } from '@opentelemetry/auto-instrumentations-node';

const sdk = new NodeSDK({
  serviceName: 'checkout-service',
  instrumentations: [getNodeAutoInstrumentations()],
});
sdk.start();
```

只在有意义的内部工作单元周围（例如 `applyDiscounts`、`chargeProvider`）添加手动 span，并附上 on-call 排查时用来过滤的 attributes。让 context 跨越每一个异步边界传播——HTTP headers、队列消息 metadata——否则 trace 会在断点处中断。默认以低比例做 head-based 采样；如果你的后端支持 tail sampling，对错误请求保留 100% 采样。

### 6. 告警

针对**用户能感受到的症状**告警，而不是针对原因：

```
SYMPTOM (page-worthy):           CAUSE (dashboard, not a page):
error rate > 1% for 5 min        CPU at 85%
p99 latency > 2s                 one pod restarted
queue age > 10 min               disk at 70%
```

基于原因的告警会在什么都没出错时误报，并漏掉你没预测到的故障；而基于症状的告警恰好能在用户受影响时触发，无论背后的诱因是什么。

你创建的每条告警都必须遵守以下规则：

1. **必须可行动（actionable）。** 如果应对方式是“忽略它，它会自愈”，直接删掉这条告警。
2. **必须链接到一个 runbook**——哪怕只有三行：说明意味着什么、第一个该跑的查询、升级路径。
3. **必须有阈值和持续时间**，依据是 SLO 或历史数据，不是拍脑袋。
4. 只用两个严重级别：**page**（直接影响用户，立即行动）和 **ticket**（存在降级，本周内行动）。第三档只会变成噪音，把人训成“无视一切告警”。

#### 编写 Runbook

上面第 2 条规则要求每条告警都链接到一个 runbook。Runbook 的职责是在不需要读者动脑推理的情况下回答三个问题：正在发生什么、先检查什么、如果这解决不了该找谁。存放在 `docs/runbooks/`，以告警命名。

**最小可用 runbook（三行）：**

```markdown
# Runbook: High Error Rate on /api/tasks
**Means:** DB connection pool likely exhausted, or a bad deploy.
**First check:** `SELECT count(*) FROM pg_stat_activity WHERE backend_type = 'client backend';`
  — if count > pool limit, see Step 2. (Swap in the equivalent for your database.)
**Escalate to:** #db-oncall or engineering on-call rotation.
```

**什么时候值得在三行之上扩充：** 只有当第一个检查本身不足以做出判断时，才补充步骤。一份覆盖三个最常见原因的五步 runbook，远胜过一份覆盖所有边缘情况、然后被人跳着扫读的二十步长文档。

**让 runbook 保持最新。** 把更新 runbook 作为关闭每一次用过它的事故的必做环节——过时的 runbook 只会制造虚假的安全感。如果某一步写错了或缺失了，在把事故标记为 resolved 之前就修好它。

### 7. 验证 telemetry 本身

埋点本质上也是代码，同样会出错。在宣布完工之前，先主动触发这些路径，去看实际的输出：

- 在 staging 人为制造一个错误 → 用 `requestId` 在日志里找到它，确认字段是结构化的（不是 `[object Object]`）
- 发送测试流量 → 确认 metric series 以预期的 label 和合理数值正确上报
- 在 tracing UI 里跨服务跟随一个请求 → 没有断裂的 span
- 让每条新告警试触发一次（临时调低阈值）→ 确认它到达正确的告警渠道，且 runbook 链接可用

## 常见合理化借口

| 合理化借口 | 现实 |
|---|---|
| “等它能工作了我再加日志” | “等之后”最后往往变成“等第一次事故之后”，而那是发现自己两眼一抹黑时最昂贵的时刻。边构建边埋点。 |
| “日志越多 = 越可观测” | 非结构化的噪音让事故排查更慢而不是更快。三条可查询的事件胜过三百行流水账。 |
| “console.log 目前够用” | 非结构化输出没法过滤、关联或告警。接入结构化 logger 只需一次性多花五分钟。 |
| “等出了问题我们看 dashboard 就行” | 没有带着预设问题建设的 dashboard 会把除了答案之外的一切都展示给你。一切从 on-call 问题出发。 |
| “先把重要的都加上告警，以后再调优” | 吵闹的寻呼（pager）会把人训成习惯性无视。日后调优永远不会发生，被漏掉的真实告警倒是迟早会发生。 |
| “把 User ID 做成 metric label 调试更方便” | 它同时也会让你的 metrics 后端轰然倒下。高 cardinality 的查找属于日志和 trace。 |
| “我们才两个服务，tracing 是杀鸡用牛刀” | 两个服务就已经意味着存在纯靠日志回答不了的跨服务延迟问题。Auto-instrumentation 让接入成本微乎其微。 |

## 危险信号

- 一个带重试、队列或外部调用的功能 PR，却没有新增任何 telemetry
- 用字符串插值而不是结构化字段拼接出来的日志行
- 没有 correlation/request ID——每行日志都是孤立碎片
- 一条日志流同时被 scheduler、webhook 和手动任务写入，却没有任何字段说明这行是谁产生的
- 用 user ID、原始 URL 或错误消息文本做 label 的指标（cardinality 炸弹）
- 延迟只用平均值追踪，没有百分位
- 每天触发、被人确认却毫无后续动作的告警
- 一边让基于底层原因（CPU、内存）的告警半夜叫醒真人，一边面向用户的错误率却无人监控
- 日志里出现 secret、token 或完整的 request body
- 把生产功能健康的证据寄托在“在我本地机器上是好的（It works on my machine）”上

## 验证

给一个功能埋点之后，确认：

- [ ] 这个功能的 on-call 问题已写下来，且每个信号都对应其中一问
- [ ] 所有日志输出均为结构化 JSON，有稳定的事件名，且每行都带 correlation ID
- [ ] 每个被多个入口写入的日志 sink 都带一个入口点字段：在运行启动处设置、随 correlation ID 一起传播，而不是在下游反推
- [ ] 任何一行日志里没有 secret、token 或未脱敏的 PII（抽查实际输出）
- [ ] 每个新 endpoint 和每个外部依赖都有 RED 指标，且 label 集合有界
- [ ] 延迟采用 histogram 记录；p95/p99 可查询
- [ ] 单个请求可以在 tracing UI 里端到端跟踪，没有断裂的 span
- [ ] 每条新告警都基于症状、有 runbook 链接，并已试触发验证过一次
- [ ] 在 staging 人为制造的故障，仅凭 telemetry 就能定位，无需读源码

这份清单的速览版本（含发布前埋点 gate）见 `../../references/observability-checklist.md`。
