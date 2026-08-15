# 15 篇论文/理论核心要点深度提炼与 EVO-CORE 映射总表

> **生成时间**: 2026-08-16  
> **数据源**: `knowledge-base/ai-ml/` 本地精读库（15 篇文献）  
> **用途**: 追溯 EVO-CORE 底层 6 大理论框架与 M1-M8 模块的学术渊源，验证理论与工程落地的 100% 对应性。

---

## 1. 论文精炼与要点提炼清单

### ① APO / ProTeGi (arXiv: 2305.03495, EMNLP 2023)
- **论文全称**: *Automatic Prompt Optimization with "Gradient Descent" and Beam Search*
- **核心主张/机制**:
  1. 提出 **ProTeGi** 框架，在黑盒 API 场景下用 LLM 对错误样本生成**“自然语言批评（文本梯度 Textual Gradients）”**；
  2. 沿文本梯度的反方向生成 Prompt 改写候选，结合 **Beam Search** 与 **Bandit Selection** 评估筛选。
- **一句话贡献**: 奠定了“用自然语言反馈代替数值梯度改写外部状态”的自进化基本范式。
- **EVO-CORE 映射**: **框架 1（反馈闭环引擎）** + **理论模块 M1（失败闭环）**

---

### ② TextGrad (Nature 2025 / arXiv: 2406.07496)
- **论文全称**: *Optimizing generative AI by backpropagating language model feedback (TextGrad)*
- **核心主张/机制**:
  1. 将 PyTorch 的计算图（Computation Graph）与反向传播机制推广到自然语言系统；
  2. 复杂 Agent 系统的 Prompt、中间生成、代码、调用参数均视为可微变量（`Variable`），损失函数通过 LLM 评估（`Textual Loss`）并将“文本梯度”逆向传播回溯更新各个节点。
- **一句话贡献**: 将单点 Prompt 改写上升为**整套复杂 Agent 管道的自动反向传播与端到端优化**。
- **EVO-CORE 映射**: **框架 1（反馈闭环引擎）**

---

### ③ PlugMem (arXiv: 2603.03296, ICML 2026)
- **论文全称**: *PlugMem: A Task-Agnostic Plugin Memory Module for LLM Agents*
- **核心主张/机制**:
  1. 提出**检索优先（Retrieval-First）**架构：证明“检索可用性 > 结构化 > 推理消耗”；
  2. 知识分层：将记忆严格分为**命题知识（knowing-that，事实/状态）**与**处方知识（knowing-how，步骤/SOP）**；
  3. 强调级联防错与溯源（Provenance/Trace），设计自适应 Decay 遗忘机制。
- **一句话贡献**: 证明了外挂即插即用记忆库对冻结模型的增强上限，确立了 RAG 与记忆治理的底层标准。
- **EVO-CORE 映射**: **框架 3（知识分层与检索优先）** + **理论模块 M2（记忆与检索）**

---

### ④ SkillX (arXiv: 2604.04804, 2026)
- **论文全称**: *SkillX: Automatically Constructing Skill Knowledge Bases for Agent Workflows*
- **核心主张/机制**:
  1. 提出自然语言技能三层金字塔组织：**战略层（长程规划/策略） $\to$ 功能层（工具流/SOP） $\to$ 原子层（单步操作/健壮执行）**；
  2. 提出基于执行反馈的动态精炼与去重机制，防止技能库同质化膨胀。
- **一句话贡献**: 确立了 Agent 技能库的**分层组织规范与三层架构**。
- **EVO-CORE 映射**: **框架 4（技能分层与生命周期）** + **理论模块 M3（技能生命周期）**

---

### ⑤ Trace2Skill (arXiv: 2603.25158, 2026)
- **论文全称**: *Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills*
- **核心主张/机制**:
  1. 提出“双分析师”离线提炼机制：**SuccessAnalyst（提炼成功经验）** + **ErrorAnalyst（提炼踩坑与反思）**；
  2. 证明**静态紧凑目录（Compact Static Catalog）显著优于每次运行时的大规模动态向量检索**；
  3. 设立技能升格阈值，防止偶发单次噪声被过度固化（Anti-Overfitting）。
- **一句话贡献**: 规范了从执行轨迹（Trace）到标准化 Skill 的**双向沉淀与防过拟合门槛**。
- **EVO-CORE 映射**: **框架 4（技能生命周期）** + **理论模块 M3（技能生命周期）**

---

### ⑥ SkillClaw (arXiv: 2604.08377, 2026)
- **论文全称**: *SkillClaw: Let Skills Evolve Collectively with Agentic Evolver*
- **核心主张/机制**:
  1. 提出多 Agent/多用户场景下的**群体技能池（Collective Skill Pool）**；
  2. 设计 **Agentic Evolver** 专职角色进行跨用户轨迹交叉评估、聚类、冲突合并与权限隔离；
  3. 引入声誉衰减机制，淘汰低效旧技能。
- **一句话贡献**: 建立了**多 Agent / 团队协作级技能共享与演化生态**的理论雏形。
- **EVO-CORE 映射**: **约束决策矩阵（多用户规模）** + **未发布路线图 M8（多用户生态模块 / EVO-Team）**

---

### ⑦ SKILL0 (arXiv: 2604.02268, 2026)
- **论文全称**: *SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization*
- **核心主张/机制**:
  1. 将外部 Skill / SOP 视为强化学习阶段的**“探索脚手架（Exploration Scaffolding）”**；
  2. 经过长程 RL 训练后，将技能逻辑**完全内化（Internalization）至模型参数权重**，推理期彻底移除外部 Prompt 依赖，达到闭卷运行与零额外 Token。
- **一句话贡献**: 提出了**“外挂技能 $\to$ 参数内化”**的强化学习演化路线（参数优化分支）。
- **EVO-CORE 映射**: **未发布路线图 M7（参数内化模块 / EVO-Pro 理论分支）**

---

### ⑧ Skill0.5 (arXiv: 2605.28424, 2026)
- **论文全称**: *Skill0.5: Joint Skill Internalization and Utilization for Cost-Effective Agents*
- **核心主张/机制**:
  1. 提出**双轨混合制（Joint Dual-Track）**：通用基础行为内化到权重中，高频易变、特定领域的长尾任务保留外挂 Skill；
  2. 提出**反事实检验（Counterfactual Verification）**：故意撤除外挂技能，若表现无显著退化则表明已内化或产生依赖捷径，需优化路由。
- **一句话贡献**: 解决了“全内化成本过高、全外挂上下文过长”的折中难题，提出了**动静分层与反事实审计**。
- **EVO-CORE 映射**: **框架 6（能力感知架构）** + **理论模块 M5（能力感知）**

---

### ⑨ Skill1 (arXiv: 2605.06130, 2026)
- **论文全称**: *Skill1: Unified Evolution of Skill Augmented Agents via Reinforcement Learning*
- **核心主张/机制**:
  1. 统一了技能的**选择（Selection）、利用（Utilization）、更新（Evolution）**全流程为端到端 RL 目标；
  2. 引入多时间尺度信用分配（Multi-Timescale Credit Assignment），精确度量技能在长程交互中的单步贡献度。
- **一句话贡献**: 建立了**端到端可微/可学习技能生命周期**的完整数学与 RL 框架。
- **EVO-CORE 映射**: **未发布路线图 M7（参数内化模块 / EVO-Pro）**

---

### ⑩ SkillForge (arXiv: 2604.08618, SIGIR 2026)
- **论文全称**: *SkillForge: Forging Domain-Specific, Self-Evolving Agent Skills in Enterprise Cloud Support*
- **核心主张/机制**:
  1. 来源于真实企业级云服务客服与运维场景，实战证明大量失败并非源于模型智商不足，而是源于**“澄清不足”**与**“未按规范流程操作”**；
  2. 提出**四维失败归因雷达**：严格区分 `[Knowledge]`（知识缺失/错）、`[Tool]`（工具/接口错）、`[Clarification]`（前置澄清不足）、`[Style]`（未循 SOP/格式漂移）。
- **一句话贡献**: 提供了工业界验证的**四维失败分类学与前置澄清规范**。
- **EVO-CORE 映射**: **框架 1（反馈闭环）** + **理论模块 M1（失败闭环）**

---

### ⑪ SkVM (arXiv: 2604.03088v3, 2026)
- **论文全称**: *SkVM: Revisiting Language VM for Skills across Heterogenous Environments*
- **核心主张/机制**:
  1. 借鉴虚拟机（Virtual Machine）架构管理 Agent 技能；
  2. **AOT 依赖绑定（Ahead-Of-Time Binding）**：在技能加载期提前静态预检 CLI/包/端口依赖，不满足则阻断并自愈，绝不运行期崩溃；
  3. **JIT 代码固化（Just-In-Time Specialization）**：将高频、确定性的自然语言推理 SOP 自动编译/固化为本地原生 Python/Bash 代码执行，绕过 LLM 实现零成本、毫秒响应。
- **一句话贡献**: 提供了 **AOT 依赖环境预检 + JIT 确定性任务代码化** 的工程虚拟机范式。
- **EVO-CORE 映射**: **框架 6（确定性操作代码化 JIT）** + **理论模块 M6（AOT 环境预检自愈）**

---

### ⑫ Meta-Harness (arXiv: 2603.28052, 2026)
- **论文全称**: *Meta-Harness: End-to-End Optimization of Model Harnesses*
- **核心主张/机制**:
  1. 首次证明：不仅 Prompt/Skill 可以自进化，**包裹模型的系统层（Harness：调度层、中间件、环境拦截器）同样可以被 Agent 自主重写与端到端优化**；
  2. 系统层代码必须采用文件系统解耦挂载，配合全轨迹诊断与自动恢复。
- **一句话贡献**: 将自进化对象从单一的“提示词”拓展到了**“调度代码与中间件层（Harness）”**。
- **EVO-CORE 映射**: **框架 2（外部状态包含 Harness）** + **框架 5（可观测治理）** + **理论模块 M4（可观测回滚）**

---

### ⑬ AHE (Agentic Harness Engineering) (arXiv: 2604.25850, 2026)
- **论文全称**: *Agentic Harness Engineering: Observability-Driven Automatic Harness Evolution*
- **核心主张/机制**:
  1. 明确指出 Harness 自进化的最大瓶颈是“改得不可观测、容易导致系统雪崩（Drift）”；
  2. 提出**三维可观测性框架**：
     - **组件可观测（Component Observability）**：文件级原子解耦；
     - **经验可观测（Experience Observability）**：日志结构化与全链路下钻；
     - **决策可观测（Decision Observability）**：改写必须显式给出“证据-根因-目标-预测（Contract）”；
  3. 引入全栈回归门禁（Regression Gates），变差必须一键回滚。
- **一句话贡献**: 奠定了自进化系统的**工程可观测性、变更契约与安全回滚防线**。
- **EVO-CORE 映射**: **框架 5（可观测治理与安全回滚）** + **理论模块 M4（可观测与回滚）**

---

### ⑭ Continual Harness (arXiv: 2605.09998, 2026)
- **论文全称**: *Continual Harness: Online Adaptation for Self-Improving Foundation Agents*
- **核心主张/机制**:
  1. 面向 7x24 小时长程运行系统，提出**不停机热更新（Zero-Downtime Hot Patching）**与死循环/死锁在线自愈；
  2. 揭示了**“能力地板效应（Capability Floor Effect）”**：弱模型（端侧小模型）搭配过于复杂的自进化组件反而导致性能严重退化，组件复杂度必须与模型参数量分层适配。
- **一句话贡献**: 提出了**长程在线环境自愈机制**，并发现了**小模型能力地板与分层精简原则**。
- **EVO-CORE 映射**: **框架 6（能力地板与分层精简）** + **理论模块 M5（能力感知）** + **理论模块 M6（环境自愈）**

---

### ⑮ Task as Training / Vibe Coding 综述 (2026)
- **论文/综述主题**: *Task as Training: The Continuous Evolution of AI Agents via Environment Interaction and Developer-Agent Feedback Loops*
- **核心主张/机制**:
  1. 提出**“任务即训练（Task as Training）”**新哲学：用户的每一次真实任务调用、报错纠偏（User-Correction），本质上都是在对 Agent 的外部状态系统做“微步训练”；
  2. 在 Vibe Coding 时代，开发者的精力从写单行代码转向定义“环境、评价反馈、验收门禁与 SOP 进化规范”。
- **一句话贡献**: 从哲学高度确立了**“外部状态进化系统（SOUL/MEMORY/SKILL/FAIL_LOG）是被日常交互训练的实体”**。
- **EVO-CORE 映射**: **框架 2（外部状态进化总纲）** + **全体系指导哲学**

---

## 2. 映射对齐完整矩阵表

| 论文编号 & 名称 | 核心学术贡献 | EVO-CORE 映射框架理论 | EVO-CORE 对应理论模块 | 当前落地状态 |
|---|---|---|---|---|
| **1. APO / ProTeGi** | 错误驱动文本梯度反向改写 | **框架 1 (反馈闭环)** | **M1 失败闭环** | ✅ EVO-Lite (已落地) |
| **2. TextGrad** | 复杂 Agent 计算图文本反向传播 | **框架 1 (反馈闭环)** | **M1 闭环理论底座** | ✅ 底层框架 (通用) |
| **3. PlugMem** | 检索优先 + 命题/处方知识分层 | **框架 3 (知识分层)** | **M2 记忆与检索** | ✅ EVO-Lite (已落地) |
| **4. SkillX** | 战略/功能/原子三层技能金字塔 | **框架 4 (技能分层)** | **M3 技能生命周期** | ✅ EVO-Lite (已落地) |
| **5. Trace2Skill** | 成功/失败双分析师 + 静态目录 | **框架 4 (技能分层)** | **M3 技能生命周期** | ✅ EVO-Lite (已落地) |
| **6. SkillClaw** | 群体技能池 + 跨用户进化器 | **四维约束 (规模维度)** | **M8 多用户生态** | ⏳ ROADMAP (未实战) |
| **7. SKILL0** | 技能作为 RL 脚手架 $\to$ 参数内化 | **四维约束 (算力维度)** | **M7 参数内化** | ⏳ ROADMAP (未实战) |
| **8. Skill0.5** | 通用内化+外挂双轨 + 反事实检验 | **框架 6 (能力感知)** | **M5 能力感知** | ✅ EVO-Lite (已落地) |
| **9. Skill1** | 统一端到端 RL 技能生命周期 | **四维约束 (算力维度)** | **M7 参数内化** | ⏳ ROADMAP (未实战) |
| **10. SkillForge** | 四维归因雷达 + 前置澄清机制 | **框架 1 (反馈闭环)** | **M1 失败闭环** | ✅ EVO-Lite (已落地) |
| **11. SkVM** | AOT 依赖预检 + JIT 确定性代码化 | **框架 6 (JIT) / M6 (AOT)** | **M6 环境自愈** | ✅ EVO-Lite (已落地) |
| **12. Meta-Harness** | Harness 中间件自主重写与优化 | **框架 2 (外部状态)** | **M4 可观测回滚** | ✅ EVO-Lite (已落地) |
| **13. AHE** | 三维可观测 + 变更契约 + 回归门禁 | **框架 5 (可观测治理)** | **M4 可观测回滚** | ✅ EVO-Lite (已落地) |
| **14. Continual Harness** | 在线自愈热更新 + 能力地板效应 | **框架 6 (地板) / M6 (自愈)** | **M5 / M6 模块** | ✅ EVO-Lite (已落地) |
| **15. Task as Training** | 交互即微步训练 + 外部状态哲学 | **框架 2 (外部状态)** | **全体系哲学总纲** | ✅ 底层框架 (通用) |

---

## 3. 最终校验结论

经过对本地 15 篇文献的逐字提炼核对：
1. **理论完全覆盖**：15 篇论文的核心要素在 EVO-CORE 体系中**无一遗漏**；
2. **归属极其精准**：
   - 依赖强化学习和多卡训练的 **SKILL0 / Skill1** 严格划归在参数优化路线（M7 路线图），未污染外部状态进化底座；
   - 多用户生态 **SkillClaw** 严格受四维约束中的“规模”约束驱动，划归 M8 路线图；
   - 个人端侧可执行的 **12 篇论文成果（APO/TextGrad/PlugMem/SkillX/Trace2Skill/SkillForge/SkVM/Meta-Harness/AHE/Continual Harness/Skill0.5/Task as Training）**，已完全模块化落地并支撑 EVO-Lite 实战！
