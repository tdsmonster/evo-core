# M4 Observability & Rollback Module

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