# M8 Counterfactual Evaluation Module

> **EVO-CORE X Engine**: `Engine 3: Evidence Engine` (Sandboxed Verification)  
> **Source Papers**: Skill0.5 (arXiv:2605.28424) + Task as Training (2026)  
> **Dependencies**: Engine 1 (World Model Sandbox), M3 (Skill Lifecycle)  
> **Applicability**: Standard / Enterprise Tiers

---

## Core Claims

- **Beyond Single-Instance Success**: A skill must not be declared valid merely because it resolved one isolated failure.
- **Counterfactual Robustness**: Verify whether the skill truly cures the root cause by evaluating it across perturbed boundary conditions (e.g., modified ports, altered formats, simulated network failures) inside an isolated sandbox.

---

## AI-Parseable Core

### ① Counterfactual Test Matrix

```text
[Baseline Task] ──► [Perturbed Input / Env] ──► [Sandbox Test] ──► [Score Matrix]
```

### ② Capability Contracts

1. **Contract 1: Synthetic Perturbation**: Automatically generate at least 3 counterfactual variants (e.g., inverted arguments, non-standard outputs, degraded bandwidth) before declaring a skill `stable`.
2. **Contract 2: Negative Assertion (Ablation Check)**: Temporarily ablate (disable) the newly evolved rule/skill on historical benchmark tasks to prove that system performance strictly improves with the rule enabled.
