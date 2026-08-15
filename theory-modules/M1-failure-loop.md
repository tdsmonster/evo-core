# M1 Failure Closed-Loop Module

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