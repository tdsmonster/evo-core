#!/usr/bin/env bash
# ==============================================================================
# regression_gate_template.sh — 全栈回归门禁模板
# ==============================================================================
# 来源: EVO-CORE 框架5（可观测治理与安全回滚）
# 理论依据: AHE 决策可观测与防回归 · Meta-Harness 端到端验证
#
# 作用: 每次修改核心组件后一键全栈回归，防"拆东墙补西墙"。
# 这是「参考实现骨架」，请按你的环境修改:
#   - PORTS:     你的核心服务端口列表
#   - HEALTH_CMD: 你的健康检查命令（需输出分数，如 "xx/100"）
#   - DIAG_CMD:   你的失败诊断命令（需输出复发率数字）
#   - EVAL_CMD:   你的评估命令（需输出命中率百分比，可选）
# ==============================================================================

set -uo pipefail

# ============ 按环境配置 ============
PORTS=(8000 9000 9200)                  # 核心服务端口（示例，按你的服务修改）
HEALTH_CMD="bash health_check.sh"       # 健康检查命令（输出 "xx/100"）
DIAG_CMD="python3 fail_diagnosis.py"    # 失败诊断命令（输出复发率）
EVAL_CMD="python3 eval.py"              # 评估命令（输出 "xx%"）可选
FULL_EVAL=false
[ "${1:-}" == "--full" ] && FULL_EVAL=true
RECURS_LIMIT=30.0                       # 复发率红线(%)
EVAL_LIMIT=80.0                         # 命中率底线(%)
# ====================================

ERRORS=0

echo "========================================================"
echo "🚀 全栈回归门禁测试 (模式: $([ $FULL_EVAL = true ] && echo FULL || echo FAST))"
echo "========================================================"

# --- 检查 1: 核心端口 ---
echo "[1/3] 核心端口监听检测..."
for port in "${PORTS[@]}"; do
    if lsof -iTCP:"$port" -sTCP:LISTEN -P >/dev/null 2>&1; then
        echo "  ✅ Port $port: 正常监听"
    else
        echo "  ❌ Port $port: 未监听!"
        ERRORS=$((ERRORS + 1))
    fi
done

# --- 检查 2: 健康检查 (严格匹配满分，防宽松误判) ---
echo "[2/3] 健康检查..."
HEALTH_OUT=$(eval "$HEALTH_CMD" 2>/dev/null | head -1)
echo "  • $HEALTH_OUT"
# ⚠️ 严格提取 "数字/100"，禁止字符串宽松匹配（防止 90/100 误判达标）
SCORE=$(echo "$HEALTH_OUT" | grep -oE '[0-9]+/100' | head -1 | cut -d'/' -f1)
if [ -n "$SCORE" ] && [ "$SCORE" -ge 100 ]; then
    echo "  ✅ 健康分满分"
else
    echo "  ❌ 健康分未达满分: $HEALTH_OUT"
    ERRORS=$((ERRORS + 1))
fi

# --- 检查 3: 失败闭环 + 评估 ---
echo "[3/3] 失败闭环诊断..."
DIAG_OUT=$(eval "$DIAG_CMD" 2>/dev/null)
RATE=$(echo "$DIAG_OUT" | grep -oE '[0-9]+(\.[0-9]+)?' | head -1)
if [ -n "$RATE" ]; then
    # ⚠️ 浮点数比较，禁止截断（防止 30.5% 被截断为 30 误判受控）
    if awk "BEGIN{exit !($RATE > $RECURS_LIMIT)}"; then
        echo "  ❌ 复发率超标: ${RATE}%"
        ERRORS=$((ERRORS + 1))
    else
        echo "  ✅ 复发率受控: ${RATE}%"
    fi
fi

if [ "$FULL_EVAL" = true ]; then
    EVAL_OUT=$(eval "$EVAL_CMD" 2>/dev/null | head -1)
    EVAL_SCORE=$(echo "$EVAL_OUT" | grep -oE '[0-9]+(\.[0-9]+)?%' | head -1 | tr -d '%')
    if [ -n "$EVAL_SCORE" ] && awk "BEGIN{exit !($EVAL_SCORE >= $EVAL_LIMIT)}"; then
        echo "  ✅ 评估达标: ${EVAL_SCORE}%"
    else
        echo "  ❌ 评估未达底线: ${EVAL_OUT:-无输出}"
        ERRORS=$((ERRORS + 1))
    fi
else
    echo "  ⚡ 快速模式跳过评估（--full 全量评估）"
fi

echo "========================================================"
if [ "$ERRORS" -eq 0 ]; then
    echo "🎉 [PASS] 回归门禁全部通过"
    exit 0
else
    echo "🚨 [FAIL] 发现 $ERRORS 处异常，禁止合并!"
    exit 1
fi
