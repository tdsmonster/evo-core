# Theory Modules Library

> **Positioning**: EVO-CORE's "Composable Component Library". The framework provides the skeleton; this library provides modularized theories based on specific papers.
> **Usage**: Select modules based on 4D constraints (Compute/Cost/Scale/Reliability).
> **Structure**: Source Paper → Core Claim → **AI-Parseable Core** (Rules/Formats/Metrics) → Dependencies.

## Module Index

| Module | Name | Source Papers | Dependencies | Core Capability |
|---|---|---|---|---|
| **M1** | Failure Closed-Loop | APO/ProTeGi + SkillForge | None | Failure logging, 4D attribution, recurrence monitoring |
| **M2** | Memory & Retrieval | PlugMem | None | Hybrid RRF, health checks, small model context injection |
| **M3** | Skill Lifecycle | SkillX + Trace2Skill | M1 | Stratification, bi-directional distillation, anti-overfitting |
| **M4** | Observability & Rollback | AHE + Meta-Harness | M1 | File decoupling, regression gates, safe rollbacks |
| **M5** | Capability-Awareness | Skill0.5 + Continual Harness | M2 | Floor effect, RAG-driven tagging, counterfactual verification |
| **M6** | Environment Self-Healing| Continual Harness + SkVM | None | AOT preflight checks, backoff healing, daemons |

## Quick Selection Guide

```text
Compute-Constrained (≤8GB)  → M1 + M6 (Rule-based & healing only)
Edge Hybrid (16-32GB)       → M1 + M2 + M3 + M5 + M6 (+M4 optional)
Local Geek (≥64GB)          → M1-M6 (Full suite)
Production (Cloud)          → M1-M6 + Parametric Internalization (M7)
Multi-User (Team)           → M1-M6 + Experience Sharing (M8)
```
> Note: M7 and M8 remain theoretical and are solely tracked in the ROADMAP.