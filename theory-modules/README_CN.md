# EVO-CORE X 模块化理论库 (M0 ~ M10)

> **架构核心定位**: 本模块库是 **EVO-CORE X 四大自主认知引擎** (`docs/evo-core-x-framework_CN.md`) 的即插即用形式化零件库。

---

## 📌 完整模块矩阵 (M0 ~ M10)

| 模块编号 | 模块名称 | 归属 EVO-CORE X 引擎 | 基础文献与理论来源 |
|---|---|---|---|
| **M0** | **[进化总控与调度 (Governor)](M0-evolution-governor_CN.md)** | `引擎 4: 对齐引擎 (Alignment)` | Continual Harness / Task as Training |
| **M1** | **[失败闭环与文本梯度 (Failure Loop)](M1-failure-loop_CN.md)** | `引擎 3: 证据引擎 (Evidence)` | APO / ProTeGi / SkillForge |
| **M2** | **[分层记忆与检索优先 (Memory & RAG)](M2-memory-retrieval_CN.md)** | `引擎 2: 知识引擎 (Knowledge)` | PlugMem |
| **M3** | **[技能生命周期管理 (Skill Lifecycle)](M3-skill-lifecycle_CN.md)** | `引擎 2: 知识引擎 (Knowledge)` | SkillX / Trace2Skill |
| **M4** | **[可观测性治理与安全回滚 (Observability)](M4-observability-rollback_CN.md)** | `引擎 3: 证据引擎 (Evidence)` | AHE / Meta-Harness |
| **M5** | **[能力感知与算力匹配 (Capability Match)](M5-capability-match_CN.md)** | `引擎 4: 对齐引擎 (Alignment)` | Skill0.5 / Continual Harness |
| **M6** | **[环境自愈与 AOT 预检 (Self-Healing)](M6-self-healing_CN.md)** | `引擎 1: 世界模型 (World Model)`| Continual Harness / SkVM |
| **M7** | **[证据链与技能溯源 (Evidence & Provenance)](M7-evidence-provenance_CN.md)** | `引擎 3: 证据引擎 (Evidence)` | AHE / Meta-Harness |
| **M8** | **[反事实鲁棒性评估 (Counterfactual Eval)](M8-counterfactual-eval_CN.md)** | `引擎 3: 证据引擎 (Evidence)` | Skill0.5 / Task as Training |
| **M9** | **[编译期经验压缩与冲突消灭 (Consolidation)](M9-knowledge-consolidation_CN.md)** | `引擎 2: 知识引擎 (Knowledge)` | Trace2Skill / PlugMem |
| **M10**| **[进化成本与资源控制 (Cost Controller)](M10-cost-controller_CN.md)** | `引擎 4: 对齐引擎 (Alignment)` | Skill1 / APO |

---

## 🛠️ 按四大核心引擎映射选配

### 1. 引擎 1 | 世界模型引擎 (World Model Engine)
* **M6 (环境自愈)**：主动状态探针、健康守护进程与 AOT 依赖运行前预检。

### 2. 引擎 2 | 知识引擎 (Knowledge Engine)
* **M2 (分层记忆)**：确定性上下文前置注入，陈述性知识 vs 程序性知识解耦。
* **M3 (技能生命周期)**：Skill 状态机迁移 (`draft` -> `candidate` -> `stable` -> `deprecated`)。
* **M9 (经验压缩与消歧)**：编译期去重合并，5 级漏斗提炼，彻底消灭运行时规则漂移。

### 3. 引擎 3 | 证据引擎 (Evidence Engine)
* **M1 (失败闭环)**：文本梯度反向传播，4D 归因分类 (`[Knowledge]/[Tool]/[Clarification]/[Style]`)。
* **M4 (可观测与回滚)**：三维可观测性（组件/经历/决策）与自动化回归门禁。
* **M7 (证据与溯源)**：不可篡改知识血统，强制绑定真实失败样本与测试记录。
* **M8 (反事实评估)**：边界扰动测试，隔离沙箱消融断言。

### 4. 引擎 4 | 对齐引擎 (Alignment Engine)
* **M0 (进化总控)**：演进生命周期统一状态机协调与调度。
* **M5 (能力感知匹配)**：三层异构算力分流与任务难度路由。
* **M10 (成本与资源控制)**：内存硬上限约束、Token 额度预算与 ROI 演进门禁。
