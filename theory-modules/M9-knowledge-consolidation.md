# M9 Compile-Time Knowledge Consolidation & Conflict Elimination

> **EVO-CORE X Engine**: `Engine 2: Knowledge Engine`  
> **Source Papers**: Trace2Skill (arXiv:2603.25158) + PlugMem (arXiv:2603.03296)  
> **Dependencies**: M2 (Memory & RAG), M3 (Skill Lifecycle)  
> **Applicability**: All Tiers

---

## Core Claims

- **Compile-Time Elimination over Runtime Arbitration**: Resolving thousands of dynamic skill conflicts at runtime causes combinatorial latency spikes and deadlock. Knowledge conflicts must be resolved at compilation/consolidation time.
- **Hierarchical Experience Compression**: Raw traces must be compacted through 5 stages: `Raw Trace -> Episode -> Pattern -> Skill -> Mental Policy`.

---

## AI-Parseable Core

### ① Knowledge Hierarchy Funnel

```text
[Raw Events (10,000s)]
         │
         ▼ (Consolidation)
[Episodic Memory (1,000s)]
         │
         ▼ (Pattern Extraction)
[Compact Skills (100s)]
         │
         ▼ (Axiomatic Distillation)
[Core Policies / Mental Models (10s)]
```

### ② Capability Contracts

1. **Contract 1: Strict Deduplication & Merge**: When a new skill overlaps > 70% with existing skills, system must trigger compilation-time merge rather than coexisting in active retrieval indices.
2. **Contract 2: Sub-Zero Drift Guarantee**: Obsolete rules must be superseded by explicit deprecation trees, preventing contradictory guidance in active prompt injection.
