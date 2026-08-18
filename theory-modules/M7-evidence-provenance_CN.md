# M7 证据链与技能溯源模块 (Evidence & Provenance)

> **EVO-CORE X 引擎归属**: `引擎 3: 证据引擎 (Evidence Engine)`  
> **学术渊源**: AHE (arXiv:2604.25850) + Meta-Harness (arXiv:2603.28052)  
> **依赖关系**: M1 (失败闭环), M3 (技能生命周期)  
> **适用范围**: 标准及以上级别 (生产与严肃工程)

---

## 核心主张

- **不可篡改的知识血统**：每一个 Skill 和全局规则必须明确回答：*“这个规则从何而来？基于哪些真实失败样本？在什么环境下完成了验证？由谁批准合入？”*
- **杜绝孤儿规则与经验幻觉**：禁止无源规则凭空注入；所有演进资产必须绑定唯一的机器溯源锚点。

---

## AI-Parseable 形式化规范

### ① 溯源元数据结构 (Provenance Schema)

每个 Skill 必须包含标准头部元数据：

```yaml
provenance:
  skill_id: "docker-port-conflict-resolver-v2"
  source_failures:
    - "trace_20260817_port_8080_bind_err"
    - "trace_20260818_tcp_reuse_collision"
  validation_evidence:
    reproduced_count: 5
    successful_sandbox_fixes: 5
    counterfactual_score: 0.98
  created_at: "2026-08-18T10:00:00Z"
  arbiter_signature: "alignment_engine_tier1_verified"
  status: "stable" # draft / candidate / stable / deprecated
```

### ② 能力契约

1. **契约 1: 零孤儿规则**：没有绑定真实 trace / 证据样本的经验严禁直接提升为全局规则。
2. **契约 2: 毫秒级因果溯源**：系统必须支持基于元数据索引秒级追溯任意规则的诞生背景与历史单测通过记录。
