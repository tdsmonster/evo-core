#!/usr/bin/env python3
"""
failure_closed_loop_template.py — 失败闭环解析/诊断模板
=====================================================
来源: EVO-CORE 框架1（反馈闭环引擎）· 框架5（可观测治理与安全回滚）
理论依据: APO/ProTeGi 文本梯度 · SkillForge 四维失败归因 · AHE 可观测性

作用: 解析结构化失败日志 → 严格字段校验 → 复发率统计 → 四维失败分类。
这是「参考实现骨架」，请按你的环境修改 LOG_FILE 路径、字段定义后使用。

参考实现说明: 本模板为通用参考骨架，不包含任何具体业务/环境信息。
"""

import sys
import json
import re
from pathlib import Path
from collections import Counter

# ============ 按环境配置 ============
LOG_FILE = Path("fail_log.txt")  # 你的失败日志路径
FIELD_COUNT = 9                  # 结构化日志列数
# 四维失败分类（SkillForge）: 失败归因的四个维度
DIMENSIONS = ["Knowledge", "Tool", "Clarification", "Style"]
RECURS_THRESHOLD = 30.0          # 复发率告警阈值(%)
# ====================================

def parse_log():
    """解析结构化日志，严格校验字段数（防格式漂移导致级联污染）"""
    if not LOG_FILE.exists():
        return [], []
    entries, malformed = [], []
    for idx, line in enumerate(LOG_FILE.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
        line_clean = line.strip()
        if not line_clean.startswith("|"):  # 只处理管道数据行
            continue
        parts = [p.strip() for p in line.split("|")]
        valid_parts = [p for p in parts if p != ""]
        # ⚠️ 严格校验: 必须正好 N 列，否则跳过并告警（防错位污染统计）
        if len(valid_parts) != FIELD_COUNT:
            malformed.append((idx, len(valid_parts), line_clean[:30]))
            continue
        entries.append(valid_parts)
    return entries, malformed

def analyze(entries):
    """状态统计 + 四维分类 + 复发率"""
    if not entries:
        return {}
    status = Counter(e[5] for e in entries)          # 处置状态列
    dimensions = Counter()
    for e in entries:
        cause = e[3]                                  # 根因列
        m = re.match(r"\[(" + "|".join(DIMENSIONS) + r")\]", cause)
        dimensions[m.group(1) if m else "Untagged"] += 1

    # 复发率: 复发标记数 / (已处置 + 复发)
    recurs = sum(1 for e in entries if e[6].isdigit() and int(e[6]) > 0)
    handled = status.get("patched", 0) + status.get("verified", 0)
    recurs_rate = recurs / (handled + recurs) * 100 if (handled + recurs) else 0.0

    return {
        "total": len(entries),
        "status": dict(status),
        "dimensions": dict(dimensions),
        "recurs_rate": round(recurs_rate, 1),
        "alert": recurs_rate > RECURS_THRESHOLD,
    }

def main():
    entries, malformed = parse_log()
    for idx, cnt, prev in malformed:
        print(f"⚠️ 格式异常: 第{idx}行 {cnt}列(应{FIELD_COUNT}列) → {prev}")
    stats = analyze(entries)
    if "--json" in sys.argv:
        print(json.dumps(stats, ensure_ascii=False, indent=2))
        return
    print(f"=== 失败闭环诊断 (共 {stats.get('total', 0)} 条) ===")
    print(f"• 处置状态: {stats.get('status')}")
    print(f"• 四维分类 [Knowledge/Tool/Clarification/Style]: {stats.get('dimensions')}")
    print(f"• 复发率: {stats.get('recurs_rate')}% "
          + ("🚨 超阈值!" if stats.get("alert") else "✅ 受控"))

if __name__ == "__main__":
    main()
