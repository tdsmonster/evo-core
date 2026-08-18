# EVO-CORE · Architecture Specification for Agent Self-Evolution & Execution

> **A Constraint-Driven, Multi-Tiered Self-Evolution & Evidence Architecture for Autonomous Agents**  
> Core Frameworks (v1.0 Classical & v2.0 EVO-CORE X Next-Gen) + Modular Theory Library (M1-M6) + Tiered Blueprints.

[English (Main)](README.md) | [中文说明 (Chinese)](README_CN.md)

---

## ⚡ What's New: EVO-CORE X (v2.0) Architecture Release

We are proud to introduce **EVO-CORE X**, a major generational paradigm shift from single-agent prompt mutation to a **Decentralized Four-Engine Cognitive Architecture** with **Heterogeneous Compute Scheduling** and **Machine-Verifiable Evidence Gates (0 LLM Cost)**:

* 📖 **Read the Full Specification**: [`docs/evo-core-x-framework.md`](docs/evo-core-x-framework.md) ([中文版](docs/evo-core-x-framework_CN.md))
* 🧠 **Four Autonomous Cognitive Engines**: *World Model Engine*, *Knowledge Engine*, *Evidence Engine*, and *Alignment Engine*.
* 🚀 **Heterogeneous Compute Scheduling**: Cloud Frontier Arbiter + Edge Offline Distiller + High-Throughput Stateless Worker Pool.
* 🛡️ **Zero-Leakage Ephemeral Sandboxes**: JIT worker generation with deterministic `unittest` verification and zero runtime memory retention.

---

## 📌 Architecture Overview

```
┌────────────────────────────────────────────────────────────────────────┐
│ ① EVO-CORE X Core Specification (docs/evo-core-x-framework.md)         │
│    Four Decentralized Engines · Heterogeneous Compute · Evidence Gates │
├────────────────────────────────────────────────────────────────────────┤
│ ② Classic Core Framework (docs/evo-core-framework.md)                  │
│    Theoretical foundation synthesized from 15 academic papers.        │
│    6 Core Theories + 4D Constraint Matrix (Compute/Cost/Scale/Reliab.) │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│ ③ Modular Theory Library (theory-modules/ M1-M6) ★ Configurable        │
│    M1: Failure Loop · M2: Memory/RAG · M3: Skill Lifecycle             │
│    M4: Observability · M5: Capability Match · M6: Self-Healing Checks  │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│ ④ Tiered Blueprints (Recommended Presets)                              │
│    EVO-Lite  → 3-tier compute presets for solo developers (Validated)  │
│    EVO-Pro / EVO-Team → Theory-stage only (See ROADMAP)                │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 📁 Repository Structure

```
evo-core/
├── README.md               # English Main Overview
├── README_CN.md            # Chinese Main Overview
├── LICENSE                 # MIT License
├── REFERENCES.md           # Citations & contributions of 15 foundational papers
├── ROADMAP.md              # Milestones & unreleased modules
├── docs/
│   ├── evo-core-x-framework.md    # ★ EVO-CORE X Next-Gen Specification (v2.0)
│   ├── evo-core-x-framework_CN.md # ★ EVO-CORE X 次世代架构规范 (中文版)
│   ├── evo-core-framework.md      # Base Classic Framework (v1.0)
│   ├── evo-core-framework_CN.md   # 底层经典核心框架 (中文版)
│   └── evo-tier-a-lite.md         # EVO-Lite Blueprint (3-tier compute presets)
├── theory-modules/                # ★ Modular Theory Library
│   ├── README.md                  # Module index & selection guide
│   ├── M1-failure-loop.md         # Closed-loop failure analysis (APO + SkillForge)
│   ├── M2-memory-retrieval.md     # Memory & retrieval priority (PlugMem)
│   ├── M3-skill-lifecycle.md      # Skill lifecycle & anti-overfitting (SkillX + Trace2Skill)
│   ├── M4-observability-rollback.md # Observability & CI regression (AHE + Meta-Harness)
│   ├── M5-capability-match.md     # Capability matching & floor effect (Skill0.5)
│   └── M6-self-healing.md         # Environment self-healing & AOT checks (SkVM)
└── templates/                    # Reference implementation templates (Sanitized)
    ├── failure_closed_loop_template.py # Failure parsing & 4D taxonomy
    ├── regression_gate_template.sh     # Full-stack automated regression gate
    └── aot_deps_check_template.py      # Ahead-Of-Time dependency preflight check
```

---

## 🚀 Quick Start (3 Steps)

```bash
# 1. Clone the repository
git clone https://github.com/tdsmonster/evo-core.git
cd evo-core

# 2. Explore the EVO-CORE X Paradigm & 4D Matrix
#    → docs/evo-core-x-framework.md (Four-Engine Execution)
#    → docs/evo-core-framework.md (§0 Decision Matrix)

# 3. Select modules and apply reference templates
#    → docs/evo-tier-a-lite.md (Recommended preset for your hardware tier)
#    → theory-modules/ (AI-parseable specifications)
#    → templates/ (Adaptable code skeletons)
```

---

## 🧠 Core Design Principles

1. **Evidence-Driven over Persona-Driven**: System designs are determined by objective constraints and non-fungible machine assertions, not arbitrary human self-reports.
2. **Skeleton & Component Separation**: The base architecture provides an unchangeable theoretical skeleton; theory modules and execution pools serve as pluggable components.
3. **Zero-Leakage Sandboxing**: High-throughput execution is strictly bounded within ephemeral environments and destroyed immediately upon verification.
4. **AI-Parseable Precision**: Every module provides exact data structures, parsing rules, and threshold metrics so that AI agents can execute them deterministically.
