# M2 Memory & Retrieval Module

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