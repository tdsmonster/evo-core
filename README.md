# EVO-CORE X: Autonomous Cognitive & Evidence Architecture (v2.0)

> **A Constraint-Driven, Four-Engine Cognitive & Evidence Architecture for Autonomous Agents**  
> Core Framework (Four Autonomous Cognitive Engines + Heterogeneous Compute Matrix + Evidence Gates) + Modular Theory Library (M1-M6) + Tiered Blueprints.

[English (Main)](README.md) | [中文说明 (Chinese)](README_CN.md)

---

## 📌 What is EVO-CORE X?

**EVO-CORE X** is a universal architecture specification designed for autonomous AI agents to achieve **safe, non-parametric continuous evolution, heterogeneous compute scheduling, and machine-verifiable execution**.

Instead of relying on monolithic prompt loops or unconstrained tool calls, EVO-CORE X establishes a strict **Four-Engine Decentralized Architecture**:

```
┌────────────────────────────────────────────────────────────────────────┐
│ ① EVO-CORE X Core Specification (docs/evo-core-x-framework.md)         │
│    World Model · Knowledge Engine · Evidence Engine · Alignment Engine │
│    Heterogeneous Compute Matrix (Arbiter / Distiller / Worker)         │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│ ② Modular Theory Library (theory-modules/ M0-M10) ★ Configurable       │
│    M0: Governor · M1: Failure Loop · M2: Memory/RAG · M3: Skill Life   │
│    M4: Observability · M5: Capability · M6: Self-Healing · M7: Provenance
│    M8: Counterfactual · M9: Consolidation · M10: Cost Controller       │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│ ③ Tiered Blueprints (Recommended Presets)                              │
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
│   ├── evo-core-x-framework.md    # ★ EVO-CORE X Architecture Specification (English)
│   ├── evo-core-x-framework_CN.md # ★ EVO-CORE X 次世代架构规范 (中文版)
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
    ├── evidence_sandbox_runner_template.py # ★ EVO-CORE X Ephemeral sandbox & unit test gate
    ├── failure_closed_loop_template.py    # Failure parsing & 4D taxonomy
    ├── regression_gate_template.sh        # Full-stack automated regression gate
    └── aot_deps_check_template.py         # Ahead-Of-Time dependency preflight check
```

---

## 🚀 Quick Start (3 Steps)

```bash
# 1. Clone the repository
git clone https://github.com/tdsmonster/evo-core.git
cd evo-core

# 2. Explore the EVO-CORE X Framework Specification
#    → docs/evo-core-x-framework.md (Four Engines & Evidence Pipeline)

# 3. Select modules and apply reference templates
#    → docs/evo-tier-a-lite.md (Recommended preset for your hardware tier)
#    → theory-modules/ (AI-parseable specifications)
#    → templates/ (Adaptable code skeletons)
```

---

## 🧠 Core Design Principles

1. **Evidence-Driven over Persona-Driven**: System designs are determined by objective constraints and non-fungible machine assertions, not arbitrary human self-reports.
2. **Skeleton & Component Separation**: The base architecture provides an unchangeable theoretical skeleton; theory modules and execution pools serve as pluggable components.
3. **Zero-Leakage Ephemeral Sandboxes**: High-throughput execution is strictly bounded within isolated environments and destroyed immediately upon verification.
4. **AI-Parseable Precision**: Every module provides exact data structures, parsing rules, and threshold metrics so that AI agents can execute them deterministically.
