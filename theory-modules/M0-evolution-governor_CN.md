# M0 进化总控与调度模块 (Evolution Governor)

> **EVO-CORE X 引擎归属**: `引擎 4: 对齐引擎 (Alignment Engine)` (全局协调中枢)  
> **学术渊源**: Continual Harness (arXiv:2605.09998) + Task as Training (Chollet 2026)  
> **依赖关系**: 统筹调用四大引擎 (World Model / Knowledge / Evidence / Alignment)  
> **适用范围**: 全级别架构 (系统级总控)

---

## 核心主张

- **集中式状态协调 vs 解耦式分布式执行**：系统的自我进化绝不能是混乱无序的副作用，必须由显式的 Governor 统筹触发时机、假设验证、沙箱派发与状态合入。
- **闭环演进状态机**：严格遵循生命周期：`触发检测 -> 演进假设 -> 沙箱执行 -> 机器证据断言 -> 知识编译期固化 -> 安全回滚防线`。

---

## AI-Parseable 形式化规范

### ① 能力契约

1. **契约 1: 确定性状态流转**：进化状态机必须在显式状态间迁移（`IDLE`, `HYPOTHESIS`, `SANDBOX_TEST`, `EVALUATING`, `COMMITTED`, `ROLLED_BACK`），杜绝模糊中间态。
2. **契约 2: 任务非干涉性**：演进分析与修补动作必须在后台或隔离沙箱中异步进行，严禁抢占阻塞用户前台任务。
3. **契约 3: 硬性步数熔断**：单次演进目标设定硬性重试上限（默认 3 次），杜绝死循环消耗算力。

### ② 状态流转矩阵

```text
[空闲 (IDLE)] ──(检测到高频失败/规则漂移)──► [提出假设 (HYPOTHESIS)]
                                                  │
[合入系统 (COMMITTED)] ◄──(证据门禁通过)── [沙箱验证 (SANDBOX_TEST)]
       │                                          │
       │                                (断言失败 > 重试上限)
       ▼                                          ▼
[持续监控 (MONITORING)]                    [安全回滚 (ROLLED_BACK)]
```

### ③ 配置参数与门限

```yaml
evolution_governor:
  max_retry_budget: 3          # 单次演进最大尝试轮数
  cooldown_seconds: 300        # 连续演进防抖冷却时间 (秒)
  sandbox_backend: "ephemeral" # 隔离沙箱类型 (ephemeral / container)
  audit_logging: true          # 全量审计日志
  auto_rollback: true          # 门禁失败强制自动回滚
```
