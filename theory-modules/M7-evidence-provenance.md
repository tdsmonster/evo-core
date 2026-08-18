# M7 Evidence & Provenance Module

> **EVO-CORE X Engine**: `Engine 3: Evidence Engine`  
> **Source Papers**: AHE (arXiv:2604.25850) + Meta-Harness (arXiv:2603.28052)  
> **Dependencies**: M1 (Failure Loop), M3 (Skill Lifecycle)  
> **Applicability**: Standard / Enterprise Tiers

---

## Core Claims

- **Non-Fungible Knowledge Lineage**: Every skill and rule must answer: *Where did it originate? Which verified failures justify its creation? In what environment was it validated?*
- **Audit Traceability**: Prevent skill bloating and orphaned rules by tying every evolutionary artifact to an explicit provenance record.

---

## AI-Parseable Core

### ① Provenance Schema

Every skill/rule metadata must expose a verifiable lineage header:

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

### ② Provenance Capability Contracts

1. **Contract 1: Non-Orphaned Rule Creation**: Rules cannot be minted without at least one reproducible trace/evidence anchor.
2. **Contract 2: Lineage Queryability**: System must be capable of answering "why does rule X exist?" within sub-second query latency via deterministic metadata indexing.
