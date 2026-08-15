# M6 Environment Self-Healing Module

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