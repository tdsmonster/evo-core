import os, re
from pathlib import Path
import subprocess

base_dir = Path("/Users/csw924818/projects/evo-core")

# --- 1. RENAME CHINESE FILES ---
rename_targets = [
    "docs/evo-core-framework.md",
    "docs/evo-tier-a-lite.md",
    "docs/15-PAPERS-MAPPING.md",
    "theory-modules/README.md",
    "theory-modules/M1-failure-loop.md",
    "theory-modules/M2-memory-retrieval.md",
    "theory-modules/M3-skill-lifecycle.md",
    "theory-modules/M4-observability-rollback.md",
    "theory-modules/M5-capability-match.md",
    "theory-modules/M6-self-healing.md"
]

for f in rename_targets:
    old_file = base_dir / f
    new_file = base_dir / f.replace(".md", "_CN.md")
    if old_file.exists():
        old_file.rename(new_file)

# --- 2. FIX LINKS IN CN FILES ---
cn_files = list(base_dir.rglob("*_CN.md")) + [base_dir / "README_CN.md"]
for f in cn_files:
    if not f.exists(): continue
    text = f.read_text(encoding="utf-8")
    text = text.replace("evo-core-framework.md", "evo-core-framework_CN.md")
    text = text.replace("evo-tier-a-lite.md", "evo-tier-a-lite_CN.md")
    text = text.replace("15-PAPERS-MAPPING.md", "15-PAPERS-MAPPING_CN.md")
    text = text.replace("theory-modules/README.md", "theory-modules/README_CN.md")
    text = re.sub(r'(M[1-6]-[a-zA-Z0-9-]+)\.md', r'\1_CN.md', text)
    text = text.replace("_CN_CN.md", "_CN.md")  # Safety cleanup
    f.write_text(text, encoding="utf-8")

# --- 3. GENERATE ENGLISH FILES ---

en_files = {}

en_files["docs/evo-core-framework.md"] = """# EVO-CORE Architecture Specification: Underlying Core Framework (v1.0)

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
"""

en_files["docs/evo-tier-a-lite.md"] = """# EVO-Tier A | EVO-Lite (Solo Developer Blueprint v1.0)

> **Hierarchy**: Based on `evo-core-framework.md` (Skeleton) + `theory-modules/` (Component Library)
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
"""

en_files["theory-modules/README.md"] = """# Theory Modules Library

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
"""

en_files["theory-modules/M1-failure-loop.md"] = """# M1 Failure Closed-Loop Module

> **Source Papers**: APO/ProTeGi (arXiv:2305.03495, EMNLP 2023) + SkillForge (arXiv:2604.08618, SIGIR 2026)
> **Dependencies**: None
> **Applicability**: All Tiers (Foundational module, highly recommended as the first selection)

---

## Core Claims

- **APO/ProTeGi**: Introduces a 4-step loop: Failure Sample → Textual Criticism (Textual Gradient) → Directional Rewrite → Verification. The rewrite targets external states (rules/SOPs), freezing model weights.
- **SkillForge**: Enterprise practice reveals that failures predominantly stem from "lack of clarification" and "style non-compliance" rather than model capability shortcomings. Failures must be attributed across 4 dimensions.

## AI-Parseable Core

### ① Capability Contract for Failure Governance

> EVO-CORE remains neutral on specific tooling but mandates three strict capability contracts:

1. **Contract 1: Structured Recording**: Failure logs must adhere to a fixed column structure. The parser must strictly validate column counts; rows with missing/extra columns must trigger an alert and be skipped to prevent format drift from causing cascading statistical corruption.
2. **Contract 2: Root-Cause Attribution**: Every failure must be attributed to one and only one of 4 dimensions (`[Knowledge]/[Tool]/[Clarification]/[Style]`). This ensures failure distributions are quantifiable and direct targeted improvements.
3. **Contract 3: Recurrence Measurability**: Must track whether identical issues recur post-patch. A recurrence rate exceeding a hard threshold (e.g., 30%) triggers a mandatory quality review of previous patches.

---

### ② Implementation Spectrum

| Tier | Scenario | Typical Reference Carrier (For Inspiration, Not Mandatory) |
|---|---|---|
| **Minimal** | Standalone machine, human-readable, millisecond `grep` | Pipe-separated plain text (`fail_log.txt`) |
| **Standard** | Edge device, requires 4D stats & recurrence tracking | Structured single file + local diagnostic scripts |
| **Advanced** | Enterprise, high concurrency, distributed | Distributed tracing (OpenTelemetry/Sentry/ELK) + Grafana dashboards |

---

### ③ Log Format (9 Columns, Pipe-Separated)

```text
| Date | Task | Failure Fact | Root Cause (4D Prefix) | Solution | Status | Recurrence Count | Risk Level | Source |
```

- **Status Enum**: open / patched / verified / recurs / legacy
- **Risk Level Enum**: L1 (Env fluctuation) / L2 (Single occurrence) / L3 (Recurrence ≥ 2) / L4 (Critical: Credentials/Financial/Irreversible)
- **Source Enum**: manual / cron / user-correction / legacy

### ④ 4D Attribution Rules (Strictly One Prefix per Root Cause)

| Prefix | Condition |
|---|---|
| `[Knowledge]` | Missing/outdated knowledge: Information unfound or factually incorrect |
| `[Tool]` | Tool/Parameter/Parsing error: API failure, format mismatch, path error |
| `[Clarification]` | Lack of clarification: Assumptions made without verification, executed in ambiguous context |
| `[Style]` | Style non-compliance: SOP not loaded, format drift, failure to follow procedural steps |

### ⑤ Metrics and Thresholds

- **4D Distribution**: Calculated via Counter on the root cause prefixes.
- **Recurrence Rate**: Recurred Count / (Patched + Verified + Recurred Count) × 100%
- **Alert Threshold**: Recurrence Rate > 30% triggers a patch quality review.

### ⑥ Parser Hard Constraints

- **Strict 9-column validation** is mandatory.
- Recurrence count must be extracted as a pure integer (to prevent conflating risk level `L1` with 1 recurrence).
"""

en_files["theory-modules/M2-memory-retrieval.md"] = """# M2 Memory & Retrieval Module

> **Source Paper**: PlugMem (arXiv:2603.03296, ICML 2026)
> **Dependencies**: None
> **Applicability**: Tier 2/3 (Tier 1 can use pure keyword search without vectors)

---

## Core Claims
- **Retrieval > Structure > Reasoning**: The bottleneck in memory systems is retrieval availability, followed by structure, and lastly reasoning overhead.
- Propositional knowledge (knowing-that) and prescriptive knowledge (knowing-how) must be stored hierarchically.
- **RAG's Dual Mission**: RAG serves not only user Q&A but provides **deterministic context injection for Edge Small Models (M5)** to eliminate hallucination during tagging/classification.

## AI-Parseable Core

### ① Capability Contract for Retrieval
> EVO-CORE remains neutral on specific tooling but mandates three strict capability contracts:

1. **Contract 1: Dual-Retrieval**: Pipeline must combine exact term matching (keywords/IDs) and semantic matching (intent), preventing single-method weaknesses.
2. **Contract 2: Size Bound for Small Models**: Top-K context fed to small models (M5) must be strictly budgeted (e.g., 1K~2K tokens) to prevent prefill memory overflow.
3. **Contract 3: Self-Inspection**: Must auto-check index availability, freshness, and orphan fragment rate.

---

### ② Implementation Spectrum

| Tier | Scenario | Typical Reference Carrier (For Inspiration, Not Mandatory) |
|---|---|---|
| **Minimal** | ≤8GB RAM, text notes, zero external dependencies | `ripgrep` / `fzf` / Regex |
| **Hybrid** | 16~32GB, local small model | BM25 + Local Embedding + RRF (SQLite/Chroma/Faiss) |
| **Advanced** | Cloud production, millions of docs | Qdrant/Milvus + Cross-Encoder + GraphRAG |

---

### ③ Standard Hybrid Retrieval Flow (RRF Implementation)
```text
Query → ① Keyword Search (Top-K1) 
      → ② Vector Search (Top-K2)
      → ③ RRF Fusion: score(d) = Σ 1/(60 + rank_i(d))
      → ④ Output Top-N context for M5 injection
```

### ④ Health Inspection Metrics (Daily)
| Metric | Condition |
|---|---|
| DB Availability | Openable, queryable |
| Freshness | Last indexed < 24h |
| Orphan Rate | DB files vs real files diff < 5% |

### ⑤ Unicode Normalization Rule
- For file/path matching, apply `unicodedata.normalize('NFC')` to prevent duplicates (e.g., macOS defaults to NFD).

### ⑥ Memory Decay Rule
- Context injection limits (e.g., 4000 chars); stale facts demoted to archive, leaving only pointers in hot memory.
"""

en_files["theory-modules/M3-skill-lifecycle.md"] = """# M3 Skill Lifecycle Module

> **Source Papers**: SkillX (arXiv:2604.04804) + Trace2Skill (arXiv:2603.25158)
> **Dependencies**: M1 (Logs as raw material)
> **Applicability**: Tier 2/3 (High repetitive SOP scenarios)

---

## Core Claims
- **SkillX**: Skills should follow a 3-tier hierarchy: Strategic (Long-term) → Functional (SOPs) → Atomic (Robust actions).
- **Trace2Skill**: Both successes and failures must be distilled. Static compact catalogs outperform massive dynamic retrieval databases.

## AI-Parseable Core

### ① 3-Tier Organization Rule
| Tier | Role | Example |
|---|---|---|
| Strategic | Multi-step planning | E2E delivery, data pipelines |
| Functional | Composite SOPs | Login → Query → Export |
| Atomic | Robust single actions | API call, Regex parse |

### ② Bi-directional Distillation
- **Failure**: Log to M1 (9 columns).
- **Success**: Log complex wins (Task/Challenge/Solution/Gains) for reuse.

### ③ Anti-Overfitting Threshold (Critical)
```text
Single Failure → Log only, do not alter core rules
Recurring (≥2~3 times) → Upgrade to universal rule/SOP
```
> Goal: Prevent overfitting system rules to isolated noise.

### ④ Static Catalog Priority
- Store skills/rules in a static, searchable markdown directory rather than a bloated vector DB.
"""

en_files["theory-modules/M4-observability-rollback.md"] = """# M4 Observability & Rollback Module

> **Source Papers**: AHE (arXiv:2604.25850) + Meta-Harness (arXiv:2603.28052)
> **Dependencies**: M1 (For regression baselines)
> **Applicability**: Tier 2/3 (Frequent modifications)

---

## Core Claims
- **AHE**: The bottleneck of self-evolution is observability and rollback capability.
- **Meta-Harness**: The system harness wrapping the model can be autonomously rewritten using file systems and trajectory diagnostics.

## AI-Parseable Core

### ① Capability Contract for Observability & Rollback
1. **Contract 1: Component Observability**: Rules/Memory/Skills must be stored in decoupled files, never a giant prompt.
2. **Contract 2: Decision Observability**: Core changes must document "Evidence / Root Cause / Goal / Prediction".
3. **Contract 3: Regression Gate**: Any change to core components must pass a regression test; failures block merges.

---

### ② Implementation Spectrum
| Tier | Scenario | Typical Reference Carrier (For Inspiration, Not Mandatory) |
|---|---|---|
| **Minimal** | Single machine, rare changes | Manual `.bak` backup + local scripts |
| **Standard** | Edge device, frequent changes | 15s local bash regression (`harness_check.sh`) + Git revert |
| **Advanced** | Production CI/CD | GitHub Actions / GitLab CI + Codecov + Docker Rollback |

---

### ③ Decision Observability (Change Contract)
```text
Evidence: Triggering failure/need
Root Cause: Inferred reason
Goal: Expected fix
Prediction: Potential regressions to monitor
```

### ④ Regression Gate
```text
Post-modification → Run Regression:
  ① Port/Service Liveness
  ② Health Check (Score = 100)
  ③ M1 Log Format Check + Recurrence ≤ 30%
Any failure → Block Merge
```

### ⑤ Backup Hard Rule
- Force `.bak` snapshot before mutating critical files.
"""

en_files["theory-modules/M5-capability-match.md"] = """# M5 Capability-Aware Module

> **Source Papers**: Skill0.5 (arXiv:2605.28424) + Continual Harness (arXiv:2605.09998)
> **Dependencies**: M2 (RAG is a prerequisite for small model tagging)
> **Applicability**: Tier 2/3 (Multi-model architectures)

---

## Core Claims
- **Skill0.5**: Joint Dual-Track for internalized behaviors vs. externalized skills.
- **Continual Harness**: "Capability Floor Effect" — weak models perform worse with overly complex self-evolution components.

## AI-Parseable Core

### ① RAG Prerequisite for Edge Models
- Local small models (2B~27B) lack internal knowledge. **Running them bare for tagging is prohibited.**
- **Supply before Reasoning**: Before extracting entities or tagging, M2 (RAG) must inject deterministic evidence into the Prompt.

### ② Capability Matching Rule
```text
High-Tier Model (Cloud) → Full components (deep details, branching SOPs)
Low-Tier Model (Edge) → Trimmed components (Deterministic Context + Single Responsibility Prompt)
```

### ③ Trimming Principle
- Trim only the supply/instructions the model actually consumes.
- Do not blindly dismantle complex SOPs used by cloud models.
- Provide summary versions of long docs for edge models.

### ④ Counterfactual Verification
- Periodically remove external skills to check if performance degrades.
- Track deviations from injected constraints. Deviation > 10% triggers strict prompt reinforcement.

### ⑤ Dynamic/Static Layering
- General intuitions (internalized/system prompts) vs Volatile tasks (RAG-loaded external skills).
"""

en_files["theory-modules/M6-self-healing.md"] = """# M6 Environment Self-Healing Module

> **Source Papers**: Continual Harness (arXiv:2605.09998) + SkVM (arXiv:2604.03088v3)
> **Dependencies**: None
> **Applicability**: All Tiers (Daemon/service scenarios)

---

## Core Claims
- **Continual Harness**: Zero-downtime hot-patching; online healing for deadlocks.
- **SkVM**: Ahead-Of-Time (AOT) dependency binding to prevent runtime crashes.

## AI-Parseable Core

### ① Capability Contract for Environment Healing
1. **Contract 1: AOT Preflight**: Idempotent checks for CLI/Packages/Ports/Env before executing complex capabilities.
2. **Contract 2: Backoff Healing**: Auto-restart crashed daemons with dynamic backoff to prevent alert storms.
3. **Contract 3: Observable Boundary**: Distinguish between "service crash" (auto-heal) and "manual kill" (do not heal).

---

### ② Implementation Spectrum
| Tier | Scenario | Typical Reference Carrier (For Inspiration, Not Mandatory) |
|---|---|---|
| **Minimal** | Single machine | Native daemon (`LaunchAgent` / `systemd`) |
| **Standard** | Edge device | KeepAlive + Backoff (30s→60s→120s) |
| **Advanced** | Production | K8s Liveness/Readiness probes + HPA |

---

### ③ AOT Preflight Matrix
| Item | Check |
|---|---|
| CLI | `shutil.which(cmd)` |
| Python Libs | `importlib.util.find_spec(pkg)` |
| Ports | TCP connect success |
| Env Vars | Present & non-empty |
- Missing dependency → Block runtime execution, prompt installation.

### ④ Watchdog Backoff
```text
Failure → Dynamic Backoff: 30s → 60s → 120s → 300s
Alert → Cooldown period
```

### ⑤ Background Consistency
- Ensure background daemons use absolute paths to match terminal environments.
"""

en_files["docs/15-PAPERS-MAPPING.md"] = """# Comprehensive 15-Papers Core Elements Distillation & EVO-CORE Mapping

> **Generated**: 2026-08-16
> **Purpose**: Trace the academic origins of the EVO-CORE framework and its modules, ensuring 100% alignment between theoretical literature and engineering implementation.

---

## Mapping Matrix

| Paper | Academic Contribution | EVO-CORE Framework | EVO-CORE Module / Status |
|---|---|---|---|
| **1. APO / ProTeGi** | Textual gradients driven by error samples | **Framework 1 (Feedback Loop)** | **M1 Failure Closed-Loop** (✅ Deployed) |
| **2. TextGrad** | Textual backpropagation on complex Agent computation graphs | **Framework 1 (Feedback Loop)** | **M1 Foundation** (✅ Deployed) |
| **3. PlugMem** | Retrieval availability priority + knowledge stratification | **Framework 3 (Knowledge Stratification)** | **M2 Memory & Retrieval** (✅ Deployed) |
| **4. SkillX** | 3-tier skill pyramid organization (Strategic/Functional/Atomic) | **Framework 4 (Skill Lifecycle)** | **M3 Skill Lifecycle** (✅ Deployed) |
| **5. Trace2Skill** | Dual analysts + Static compact catalogs outperform dynamic retrieval | **Framework 4 (Skill Lifecycle)** | **M3 Skill Lifecycle** (✅ Deployed) |
| **6. SkillClaw** | Collective skill pools + Agentic Evolver | **Constraint Matrix (Scale)** | **M8 Multi-User** (⏳ ROADMAP) |
| **7. SKILL0** | Skills as RL scaffolding $\\to$ Parametric Internalization | **Constraint Matrix (Compute)** | **M7 Internalization** (⏳ ROADMAP) |
| **8. Skill0.5** | Joint Dual-Track (Internalization + Externalization) & Counterfactuals | **Framework 6 (Capability Awareness)**| **M5 Capability Awareness** (✅ Deployed) |
| **9. Skill1** | Unified End-to-End RL skill lifecycle | **Constraint Matrix (Compute)** | **M7 Internalization** (⏳ ROADMAP) |
| **10. SkillForge** | 4D attribution radar (Knowledge/Tool/Clarification/Style) | **Framework 1 (Feedback Loop)** | **M1 Failure Closed-Loop** (✅ Deployed) |
| **11. SkVM** | AOT preflight checks + JIT deterministic code specialization | **Framework 6 (JIT) / M6 (AOT)** | **M6 Self-Healing** (✅ Deployed) |
| **12. Meta-Harness** | Autonomous rewriting of harness/middleware layers | **Framework 2 (External State)** | **M4 Observability** (✅ Deployed) |
| **13. AHE** | 3D Observability + Change Contracts + Regression Gates | **Framework 5 (Observability)** | **M4 Observability** (✅ Deployed) |
| **14. Continual Harness**| Online self-healing + Capability Floor Effect | **Framework 6 (Floor) / M6 (Healing)**| **M5 / M6 Modules** (✅ Deployed) |
| **15. Task as Training** | Philosophy: External states are the entities being continuously trained | **Framework 2 (External State)** | **Global Philosophy** (✅ Deployed) |

---

## Verification Conclusion
1. **Complete Coverage**: All 15 core elements are comprehensively synthesized into EVO-CORE without omission.
2. **Strict Demarcation**: Papers relying on heavy RL and multi-GPU setups (SKILL0/Skill1) and multi-user environments (SkillClaw) are strictly confined to the M7/M8 ROADMAP, preserving the purity of the Edge/Local external-state evolution architecture.
"""

for path_str, content in en_files.items():
    (base_dir / path_str).write_text(content.strip(), encoding="utf-8")

# --- 4. GIT PUSH ---
subprocess.run(["git", "add", "."], cwd=base_dir)
subprocess.run(["git", "commit", "-m", "feat(i18n): full internationalization rollout - academic English as primary specification, Chinese as secondary mirror"], cwd=base_dir)
subprocess.run(["git", "push", "origin", "main"], cwd=base_dir)
print("✅ I18N Transformation and Deployment Complete!")
