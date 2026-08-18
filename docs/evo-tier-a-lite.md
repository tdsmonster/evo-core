# EVO-Tier A | EVO-Lite (Solo Developer Blueprint v1.0)

> **Hierarchy**: Based on `docs/evo-core-x-framework.md` (Skeleton) + `theory-modules/` (Component Library)
> **Constraint Targeting**: Compute = Edge/Constrained · Cost = Zero/Low · Scale = Solo · Reliability = Personal Tolerance
> **Positioning**: This blueprint serves as a **recommended preset**, not a strict mandate.

---

## 1. Hardware Compute Profiling

| Compute Profile | Hardware Persona | Architecture Baseline |
|---|---|---|
| **Type 1: Minimal (Low-Spec)** | ≤8GB RAM / Raspberry Pi | Cloud APIs + Local Pure Rule Engine (No local LLM) |
| **Type 2: Edge Hybrid (Mid-Spec / Typical)** | 16~32GB Unified Memory / Entry GPU | **M2 RAG Context Injection + Local Small Model (Tagging/Classification) + Cloud Large Model (Complex Reasoning)** |
| **Type 3: Local Geek (High-Spec)** | ≥64GB RAM / Workstation | Fully local quantized mid/large models (Zero external dependencies) |

---

## 2. Recommended Configuration Table

| Compute Tier | Recommended Modules | Rationale & Dataflow |
|---|---|---|
| **Type 1** (≤8GB) | **M1 (Failure Loop) + M6 (Self-Healing)** | Rule engine + state logging + auto-healing. No local model required. |
| **Type 2** (16~32GB) | **M1 + M2 + M3 + M5 + M6** (+M4 Optional) | **Crucial Loop**: M2 (RAG) feeds context to M5 (Small Model) for cheap tagging; M3 extracts SOPs; M6 guards daemons. |
| **Type 3** (≥64GB) | **M1-M6 (All)** | Sufficient compute to realize a full-stack local autonomous evolution pipeline. |

**Selection Principles**:
- M1 (Failure Loop) is the foundation for all setups; **highly recommended**.
- M2/M3 require local model/KB support; downgrade if compute is insufficient.

---

## 3. Implementation Directions (See Templates for Details)

| Direction | Recommendation |
|---|---|
| **Failure Loop** | 9-column failure log → Strict field validation → Track recurrence rate. |
| **Retrieval** | Keyword + Vector hybrid search → Daily health checks → NFC Unicode normalization. |
| **Skill Evolution** | 3-Tier organization → Bi-directional distillation → Anti-overfitting threshold. |
| **Self-Healing** | Daemon watchdogs → Dynamic backoff → Alert cooldowns. |
| **Regression Gate** | Run automated regressions after core script changes (Liveness/Health/Recurrence). |

---

## 4. Explicit Exclusions
- ❌ **RL Training / Parametric Internalization (SKILL0/Skill1)**: Belongs to the parametric optimization route. Not empirically validated locally (See M7 Roadmap).
- ❌ **Multi-User Sync (SkillClaw)**: Unnecessary for solo user environments.
- ❌ **Heavy Architectures**: Graph databases/complex enterprise observability are overkill for this tier.