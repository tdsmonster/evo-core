# M5 Capability-Aware Module

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