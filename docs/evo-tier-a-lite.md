# EVO-Tier A | EVO-Lite (Solo & Edge Deployment Blueprint v2.0)

> **Hierarchy**: Based on `docs/evo-core-x-framework.md` (Four Autonomous Engines Skeleton) + `theory-modules/` (M0-M10 Component Library)  
> **Constraint Targeting**: Compute = Edge / Constrained Hybrid · Cost = Zero ~ Low Budget · Scale = Solo Developer / Single Workstation · Reliability = Non-fungible Evidence & Machine Testing  
> **Positioning**: Practical deployment blueprint for individual developers and edge workstations based on EVO-CORE X architecture.

---

## 0. EVO-CORE X Architecture Alignment

Under the EVO-CORE X specification, agent execution and evolution are governed cooperatively by **Four Decentralized Cognitive Engines**:

```
[World Model (M6)] ➔ Real-time topology and environment health probing
[Knowledge Engine (M2, M3, M9)] ➔ 5-layer experience compression & compile-time conflict elimination
[Evidence Engine (M1, M4, M7, M8)] ➔ Ephemeral sandboxing + Zero-LLM deterministic unit test assertions
[Alignment Engine (M0, M5, M10)] ➔ Tri-tier heterogeneous compute scheduling & cost boundaries
```

---

## 1. Heterogeneous Compute Profiles

| Profile | Hardware Topology | EVO-CORE X Compute Division Strategy |
|---|---|---|
| **Type 1: Low-Spec** | RAM ≤ 8GB / Raspberry Pi / Free Containers | Cloud API as Decision Arbiter (Tier 1) + Local deterministic rule execution & sandboxed test assertions (Tier 3) |
| **Type 2: Mid-Spec (Mainstream Standard)** | RAM 16~32GB Unified Memory / Entry GPU | **Cloud Frontier Arbiter (Tier 1) + Local SLM (7B~35B) Distiller (Tier 2) + High-Throughput Stateless Worker Pool (Tier 3)** |
| **Type 3: High-Spec** | RAM ≥ 64GB / Dedicated Multi-GPU | Fully local sovereign deployment, offline sandboxing, and autonomous counterfactual testing |

---

## 2. Recommended Module Presets (M0 ~ M10 Selection Matrix)

| Compute Tier | Recommended Modules | Rationale & Closed Dataflow |
|---|---|---|
| **Type 1** (≤8GB) | **M0 + M1 + M6 + M10** | Minimal overhead: M0 Governor + M1 Failure Logging + M6 Process Watchdogs + M10 Hard Token Budgets. |
| **Type 2** (16~32GB) | **Full M0 ~ M10 Matrix** | **Golden Loop**: M2 RAG feeds deterministic context ➔ M5 schedules local SLM for M9 compression ➔ Ephemeral sandbox spins up workers for code generation ➔ M1/M4/M7/M8 unit test gates assert validity ➔ 0 memory leakage destruction. |
| **Type 3** (≥64GB) | **Full M0 ~ M10 Matrix** | Fully offline sovereign setup with deep counterfactual perturbations (M8). |

---

## 3. Core Operational Rules (EVO-CORE X Invariants)

1. **Evidence Gate First**: Untested code is strictly forbidden from merging into production without passing deterministic `unittest` assertions.
2. **Ephemeral Sandbox & Zero Retention**: Heavy worker generations must remain in temporary sandboxes and destroyed immediately upon assertion.
3. **Compile-Time Knowledge Safety**: Skill conflicts and deduplication must be resolved during consolidation, not dynamic prompt runtime.
