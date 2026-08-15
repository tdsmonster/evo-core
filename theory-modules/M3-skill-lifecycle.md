# M3 Skill Lifecycle Module

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