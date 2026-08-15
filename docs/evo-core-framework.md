# EVO-CORE Architecture Specification: Underlying Core Framework (v1.0)

> **Official Name**: **EVO-CORE: An Observability-Driven, Multi-Tiered Self-Evolution Architecture for Autonomous Agents**
> **Positioning**: Universal methodology foundation (pure theoretical skeleton, environment-agnostic, not bound to any specific hardware, user, or proprietary information).
> **Usage**: This framework serves as the baseline specification. Upper-level blueprints (EVO-Lite / EVO-Pro / EVO-Team) are derived from this framework based on the Constraint Decision Matrix.
> **Associated Literature**: APO · TextGrad · PlugMem · SkillX · Trace2Skill · Skill0.5 · SkillForge · SkVM · Meta-Harness · AHE · Continual Harness · Task as Training

---

## 0. Constraint Decision Matrix (Entry Point)

> **Core Philosophy**: System designs are determined by objective constraints, not by human labels. Identify your 4D constraints first, then apply the theory to determine the solution.

### 4D Constraints
| Dimension | Key Values | Decisive Impact on Solution |
|---|---|---|
| **Compute** | Edge (No GPU) / Cloud Scalable / Hybrid | Edge → Exclude RL internalization; Cloud → Allows parametric optimization |
| **Cost** | Zero Budget / Limited / Abundant | Zero → Rule engine priority; Abundant → Paid API tiers |
| **Scale** | Solo User / Single Team / Multi-User | Multi-User → Introduce skill sharing & access isolation |
| **Reliability**| Personal Tolerance / Production / Collab | Production → Observability + Auditing + Regression Gates |

### Decision Flow
`① Identify 4D Constraints → ② Map to Matrix to "Include/Exclude Theories" → ③ Generate Tiered Blueprint`

---

## I. Six Core Framework Theories (Universal)

### Framework 1 | Textual Gradient Loop (Feedback Engine)
**Sources**: APO/ProTeGi · TextGrad · SkillForge
**One-liner**: Agent self-evolution relies on a 4-step cycle: `Failure Sample → Textual Criticism → Directional Rewrite → Verification`.
- **Textual Gradients**: "Readable failure diagnostics" explaining what went wrong and how to fix it, rather than numerical derivatives.
- **Non-parametric Evolution**: Modifies external states (prompts/skills/memory), leaving model weights frozen.

### Framework 2 | Non-parametric Evolution
**Sources**: Permeates all 12 papers
**One-liner**: Agent Capability = Model Weights (Frozen) + External State (Evolvable).
- **Core Insight**: In constrained environments (no GPU/training budget), evolving the external state is the **only viable** path to self-improvement.

### Framework 3 | Memory Hierarchy & Retrieval Priority
**Sources**: PlugMem
**One-liner**: **Retrieval > Structure > Reasoning** — The bottleneck is retrieval availability.
- Separates Propositional knowledge (facts) from Prescriptive knowledge (SOPs).
- **Cascading Error Prevention**: Retrieval errors amplify downstream; traceability is required.

### Framework 4 | Skill Lifecycle & Stratification
**Sources**: SkillX · Trace2Skill
**One-liner**: Skills are "natural language programs" requiring full-lifecycle management.
- **3-Tier Hierarchy**: Strategic (Planning) → Functional (SOPs) → Atomic (Robust actions).
- **Anti-Overfitting Threshold**: Single failures are merely logged. Only high-frequency recurrences (≥2~3 times) trigger global rule upgrades.

### Framework 5 | Observability Governance & Safe Rollback
**Sources**: AHE · Meta-Harness
**One-liner**: The bottleneck isn't "how to change," but "whether the change is observable and reversible."
- **3D Observability**: Component (file decoupling), Experience (log drill-down), Decision (evidence/root-cause documentation).
- **Regression Gates**: Modifications must pass regression tests before merging.

### Framework 6 | Capability-Aware Architecture
**Sources**: Skill0.5 · Continual Harness · SkVM
**One-liner**: Component complexity must match the base model's capabilities ("Capability Floor Effect").
- **JIT Specialization**: Deterministic tasks should be compiled into native code (Python/Bash) to bypass the LLM entirely (zero token, zero latency).
- **Counterfactual Verification**: Temporarily remove a skill to verify if performance actually degrades, preventing dependency shortcuts.

---

## II. Applicability Boundaries
- ✅ **Applicable**: Any agent system utilizing the "Frozen Model, Evolving External State" paradigm.
- ❌ **Not Applicable**: Scenarios requiring RL training/parametric internalization (this belongs to the Parametric Optimization branch, which is a fundamentally different technical route).

---

## III. Blueprint Stacking Rules (Module Selection Mechanism)
1. **6 Core Theories = Mandatory Foundation**.
2. **Theory Modules = Selected by Constraints** (M1-M6) from `theory-modules/`.
3. **Engineering Practices = Delegated to Tiered Blueprints**, keeping the underlying framework purely environment-agnostic.