# EVO-CORE · Architecture Specification for Agent Self-Evolution

> **A Constraint-Driven, Multi-Tiered Self-Evolution Architecture for Autonomous Agents**  
> Core Framework (15 foundational papers synthesized) + Modular Theory Library (freely configurable) + Tiered Blueprints (recommended presets).

[English (Main)](./README.md) | [中文说明 (Chinese)](./README_CN.md)

---

## 📌 What is EVO-CORE?

EVO-CORE is a formal methodology and engineering specification that guides **how an AI Agent autonomously evolves over time without fine-tuning model weights**. It follows a clear three-tier architecture:

```
┌──────────────────────────────────────────────────────────┐
│ ① Core Framework (docs/evo-core-framework.md)            │
│    Theoretical foundation synthesized from 15 papers.    │
│    6 Core Theories + 4D Constraint Matrix (Compute/Cost/ │
│    Scale/Reliability). Environment-agnostic.             │
└───────────────────────┬──────────────────────────────────┘
                        │
┌───────────────────────▼──────────────────────────────────┐
│ ② Theory Modules (theory-modules/ M1-M6) ★ Configurable  │
│    Modularized agent evolution components. Each module:  │
│    Paper Basis + AI-Parseable Core (Rules/Formats/Gates) │
└───────────────────────┬──────────────────────────────────┘
                        │ Blueprints provide recommended presets
┌───────────────────────▼──────────────────────────────────┐
│ ③ Tiered Blueprints (Recommended Presets)                │
│    EVO-Lite → 3-tier compute presets for solo developers │
│               ★ Validated in real-world environments     │
│    EVO-Pro / EVO-Team → Theory-stage only (See ROADMAP)  │
└──────────────────────────────────────────────────────────┘
```

---

## 📁 Repository Structure

```
evo-core/
├── README.md               # Chinese Main Overview
├── README_EN.md            # English Main Overview
├── LICENSE                 # MIT License
├── REFERENCES.md           # Citations & contributions of 15 papers
├── ROADMAP.md              # Milestones & unreleased modules
├── docs/
│   ├── evo-core-framework.md   # Base Framework (6 Theories + Constraint Matrix)
│   └── evo-tier-a-lite.md      # EVO-Lite Blueprint (3-tier compute presets)
├── theory-modules/              # ★ Modular Theory Library
│   ├── README.md                # Module index & selection guide
│   ├── M1-failure-loop.md       # Closed-loop failure analysis (APO + SkillForge)
│   ├── M2-memory-retrieval.md   # Memory & retrieval priority (PlugMem)
│   ├── M3-skill-lifecycle.md    # Skill lifecycle & anti-overfitting (SkillX + Trace2Skill)
│   ├── M4-observability-rollback.md # Observability & CI regression (AHE + Meta-Harness)
│   ├── M5-capability-match.md   # Capability matching & floor effect (Skill0.5 + Continual Harness)
│   └── M6-self-healing.md       # Environment self-healing & AOT checks (Continual Harness + SkVM)
└── templates/                  # Reference implementation templates (Sanitized)
    ├── failure_closed_loop_template.py # Failure parsing & 4D taxonomy
    ├── regression_gate_template.sh     # Full-stack automated regression gate
    └── aot_deps_check_template.py      # Ahead-Of-Time dependency preflight check
```

---

## 🚀 Quick Start (3 Steps)

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/evo-core.git
cd evo-core

# 2. Identify your constraints using the 4D Matrix
#    → docs/evo-core-framework.md (§0 Decision Matrix)

# 3. Select modules and apply reference templates
#    → docs/evo-tier-a-lite.md (Recommended preset for your hardware tier)
#    → theory-modules/ (AI-parseable specifications)
#    → templates/ (Adaptable code skeletons)
```

**Quick Match Guide (30 Seconds)**:

| Your Target Environment | Recommended Module Combination |
|---|---|
| Edge Device $\le$ 8GB RAM / Raspberry Pi / Free Cloud Containers | **M1 (Failure Loop) + M6 (Self-Healing)** |
| Edge Workstation 16GB ~ 32GB Unified Memory / Entry-level GPU | **M1 + M2 + M3 + M6 (+ M4 Optional)** |
| High-Spec Server $\ge$ 64GB RAM / Dedicated Workstations | **Full M1 through M6** |
| Production / Cloud Enterprise | Planned in EVO-Pro (Includes Parametric Distillation) |
| Multi-User Teams / Studios | Planned in EVO-Team (Includes Skill Sharing) |

---

## 🧠 Core Design Principles

1. **Constraint-Driven, Not Persona-Driven**: System designs are determined by four objective boundaries (*Compute, Cost, Scale, Reliability*), not arbitrary human labels.
2. **Skeleton & Modules Separation**: The base framework provides an unchangeable theoretical skeleton; theory modules serve as pluggable components.
3. **Release Only What Is Validated**: Theoretical models without empirical validation remain in the ROADMAP and are excluded from the core release.
4. **AI-Parseable Precision**: Every module provides exact data structures, parsing rules, and threshold metrics so that AI agents can execute them without ambiguous prompt interpretation.

---

## 📜 License

Distributed under the [MIT License](LICENSE). Free for academic, personal, and commercial use.
