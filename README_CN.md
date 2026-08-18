# EVO-CORE · 智能体自进化与机器证据架构规范

> **面向自主智能体的约束驱动、多级自进化与客观证据架构**  
> 核心框架（v1.0 经典理论 + v2.0 EVO-CORE X 次世代规范）+ 模块化理论库 (M1-M6) + 分级实施蓝图。

[English (Main)](README.md) | [中文说明 (Chinese)](README_CN.md)

---

## ⚡ 重磅发布: EVO-CORE X (v2.0) 架构规范

我们正式推出 **EVO-CORE X** 次世代架构规范。它标志着从“单体 Agent 提示词与记忆自迭代”向**「四大自主认知引擎解耦架构」**、**「三层异构算力协作矩阵」**与**「零 LLM 成本客观机器证据硬验收门禁」**的重大范式跃迁：

* 📖 **完整架构规范文档**: [`docs/evo-core-x-framework_CN.md`](docs/evo-core-x-framework_CN.md) ([English](docs/evo-core-x-framework.md))
* 🧠 **四大解耦自主认知引擎**: **世界模型引擎 (World Model)**、**知识引擎 (Knowledge)**、**证据引擎 (Evidence)**、**对齐引擎 (Alignment)**。
* 🚀 **三层异构算力协同**: 云端高阶决策裁判 (Arbiter) + 边缘私有离线提炼 (Distiller) + 高吞吐无状态工兵集群 (Worker)。
* 🛡️ **短生命周期零泄漏沙箱**: 工兵代码生成限定于隔离沙箱内，通过确定性 `unittest` 机器验收后立即销毁，保障 0 进程与内存泄漏。

---

## 📌 架构全景图

```
┌────────────────────────────────────────────────────────────────────────┐
│ ① EVO-CORE X 次世代架构规范 (docs/evo-core-x-framework_CN.md)          │
│    四大自主引擎 · 异构算力调度矩阵 · 零 LLM 消耗机器证据门禁            │
├────────────────────────────────────────────────────────────────────────┤
│ ② 经典底层核心框架 (docs/evo-core-framework_CN.md)                     │
│    15 篇顶级前沿学术论文提炼；6 大核心理论 + 4D 约束决策矩阵            │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│ ③ 模块化理论库 (theory-modules/ M1-M6) ★ 自由选配                      │
│    M1: 失败闭环 · M2: 记忆检索 · M3: 技能生命周期                      │
│    M4: 可观测与回滚 · M5: 能力感知匹配 · M6: 环境自愈与 AOT 检查        │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│ ④ 分级实施蓝图 (推荐预设)                                              │
│    EVO-Lite  → 个人开发者 3 档算力推荐预设 (已实战严苛验证)            │
│    EVO-Pro / EVO-Team → 理论推演阶段 (详见 ROADMAP)                    │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 📁 仓库目录结构

```
evo-core/
├── README.md               # 英文主说明文档 (English Overview)
├── README_CN.md            # 中文主说明文档 (Chinese Overview)
├── LICENSE                 # MIT 开源许可证
├── REFERENCES.md           # 15 篇基础学术论文引用与贡献映射
├── ROADMAP.md              # 路线图与演进规划
├── docs/
│   ├── evo-core-x-framework_CN.md # ★ EVO-CORE X 次世代架构规范 (中文版)
│   ├── evo-core-x-framework.md    # ★ EVO-CORE X Next-Gen Specification (English)
│   ├── evo-core-framework_CN.md   # 底层经典核心框架 (中文版)
│   ├── evo-core-framework.md      # Base Classic Framework (English)
│   └── evo-tier-a-lite_CN.md      # EVO-Lite 实施蓝图 (3 档算力预设)
├── theory-modules/                # ★ 模块化理论库 (AI-Parseable 形式化规范)
│   ├── README_CN.md               # 模块索引与选配指南
│   ├── M1-failure-loop_CN.md      # 失败闭环分析 (APO + SkillForge)
│   ├── M2-memory-retrieval_CN.md  # 记忆分层与检索优先 (PlugMem)
│   ├── M3-skill-lifecycle_CN.md   # 技能生命周期与防过拟合 (SkillX + Trace2Skill)
│   ├── M4-observability-rollback_CN.md # 可观测性治理与安全回滚 (AHE + Meta-Harness)
│   ├── M5-capability-match_CN.md  # 能力感知匹配与底线效应 (Skill0.5)
│   └── M6-self-healing_CN.md      # 环境自愈与 AOT 预检 (SkVM)
└── templates/                    # 参考实现模板 (已脱敏通用代码)
    ├── failure_closed_loop_template.py # 失败归因解析器与 4D 分类法
    ├── regression_gate_template.sh     # 全栈自动化回归门禁脚本
    └── aot_deps_check_template.py      # AOT 运行前依赖预检脚手架
```

---

## 🚀 快速上手 (3 步)

```bash
# 1. 克隆代码仓库
git clone https://github.com/tdsmonster/evo-core.git
cd evo-core

# 2. 查阅 EVO-CORE X 范式与 4D 约束矩阵
#    → docs/evo-core-x-framework_CN.md (四大引擎执行体系)
#    → docs/evo-core-framework_CN.md (§0 决策矩阵)

# 3. 按需选配模块并应用工程模板
#    → docs/evo-tier-a-lite_CN.md (根据硬件档位选择预设)
#    → theory-modules/ (AI 可直接解析的规范契约)
#    → templates/ (可直接改造的无依赖代码骨架)
```

---

## 🧠 核心设计原则

1. **客观证据驱动，而非人设立场驱动**：系统的架构设计由客观硬件边界与不可篡改的机器单测断言决定，而非大模型模糊的主观自我陈述。
2. **骨架与零件彻底解耦**：底层框架提供不可变的方法论骨架；理论模块与算力工兵池作为即插即用的执行零件。
3. **零泄漏沙箱生命周期**：高吞吐无状态工兵限定于隔离沙箱内，验收完成立即销毁，彻底杜绝内存与进程残留。
4. **机器可解析的精准度**：每个模块均提供形式化的数据结构、解析规则与阈值指标，确保 AI Agent 在执行中零模糊解读。
