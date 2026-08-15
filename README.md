# EVO-CORE · Agent 自进化架构规范

> **约束驱动的 Agent 分层自进化架构** —— 底层核心框架（15 篇论文核心要素提炼）+ 理论模块库（可自由选配）+ 分层蓝图（推荐配置）。

**EVO-CORE: Observability-Driven, Multi-Tiered Self-Evolution Architecture for Autonomous Agents**

---

## 📌 这是什么？

一套**「怎么让 Agent 自己进化」的方法论体系**，三层结构：

```
┌──────────────────────────────────────────────────────────┐
│ ① 底层核心框架  docs/evo-core-framework.md               │
│    15 篇论文的核心要素提炼（环境无关的理论骨架）          │
│    6 大框架理论 + 四维约束决策矩阵（算力×成本×规模×可靠性）│
└───────────────────────┬──────────────────────────────────┘
                        │
┌───────────────────────▼──────────────────────────────────┐
│ ② 理论模块库  theory-modules/（M1-M6）★ 可自由选配       │
│    其余论文理论按主题模块化，每模块 = 论文依据            │
│    + AI 可解析核心（判定规则/格式/统计口径/阈值）         │
└───────────────────────┬──────────────────────────────────┘
                        │ 蓝图给出推荐组合，也可自由组合
┌───────────────────────▼──────────────────────────────────┐
│ ③ 分层蓝图（推荐配置）                                   │
│    EVO-Lite → 个人开发者按 3 档算力推荐模块组合 ★ 已发布 │
│    EVO-Pro / EVO-Team → 理论推演，未实战验证（ROADMAP）  │
└──────────────────────────────────────────────────────────┘
```

---

## 📁 目录结构

```
evo-core/
├── README.md
├── LICENSE
├── REFERENCES.md           # 15 篇论文引用（理论来源）
├── ROADMAP.md              # 版本与未来方向
├── docs/
│   ├── evo-core-framework.md   # 底层核心框架（6理论 + 约束矩阵）
│   └── evo-tier-a-lite.md      # EVO-Lite 蓝图（3档算力推荐配置）
├── theory-modules/              # ★ 理论模块库（可自由选配）
│   ├── README.md                # 模块索引与快速选配指引
│   ├── M1-failure-loop.md       # 失败闭环（APO + SkillForge）
│   ├── M2-memory-retrieval.md   # 记忆与检索（PlugMem）
│   ├── M3-skill-lifecycle.md    # 技能生命周期（SkillX + Trace2Skill）
│   ├── M4-observability-rollback.md  # 可观测与回滚（AHE + Meta-Harness）
│   ├── M5-capability-match.md   # 能力感知（Skill0.5 + Continual Harness）
│   └── M6-self-healing.md       # 环境自愈（Continual Harness + SkVM）
└── templates/                  # 参考实现骨架（脱敏，按环境适配）
    ├── failure_closed_loop_template.py
    ├── regression_gate_template.sh
    └── aot_deps_check_template.py
```

---

## 🚀 快速开始（3 步）

```bash
# 1. 克隆
git clone https://github.com/<your-name>/evo-core.git
cd evo-core

# 2. 读底层框架，判你的约束（四维约束矩阵）
#    → docs/evo-core-framework.md

# 3. 按你的档位选配模块（或自由组合）
#    → docs/evo-tier-a-lite.md（个人开发者推荐配置）
#    → theory-modules/（查看各模块 AI 可解析定义）
#    → templates/（参考实现骨架，可选）
```

**快速选配自查**（30 秒定位）：

| 你的环境 | 推荐组合 |
|---|---|
| 端侧 ≤8GB / 树莓派 / 免费云容器 | M1 + M6 |
| 端侧 16~32GB / 轻量显卡 | M1 + M2 + M3 + M6（+M4 可选） |
| 端侧 ≥64GB / 工作站 | M1-M6 全选 |
| 生产级 / 云端 | 待 EVO-Pro 发布（含参数内化） |
| 多用户 / 团队 | 待 EVO-Team 发布（含经验共享） |

---

## 🧠 设计原则

1. **约束驱动，而非人群标签**：决定方案的不是"你是什么人"，而是"你有什么约束"。
2. **骨架与零件分离**：底层框架是骨架，理论模块是可组合的零件，蓝图是推荐配置。
3. **只发布实战验证**：未经验证的理论不入库（M7 参数内化 / M8 多用户生态仅在路线图）。
4. **AI 可解析**：每个模块的核心定义精确到能被 AI 转化为规则/代码，杜绝模糊表述。

---

## 📜 许可证

[MIT](LICENSE) —— 可自由使用、修改、商用，保留版权声明即可。

## 🤝 贡献

欢迎通过 Issue / PR 反馈实战经验与改进建议（详见 ROADMAP）。
