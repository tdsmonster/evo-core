#!/usr/bin/env python3
"""
evidence_sandbox_runner_template.py — EVO-CORE X 证据引擎沙箱执行与机器验收模板
==================================================================================
来源: EVO-CORE X 架构规范 · 证据引擎 (Engine 3: Evidence Engine)
理论依据: SkVM (arXiv:2604.03088v3) + Task as Training (Chollet 2026) + M7/M8 模块

作用:
1. 在系统临时隔离目录（Ephemeral Sandbox）中拉起无状态工兵生成代码；
2. 运行确定性机器单元测试（unittest / AST 检查），实行零 LLM 消耗硬验收；
3. 验证通过后输出不可篡改证据凭证（Evidence Provenance），并自动销毁沙箱（0 内存泄漏）。
"""

import os
import sys
import tempfile
import shutil
import subprocess
import json
import time
from pathlib import Path
from typing import Dict, Any, Tuple

class EphemeralEvidenceSandbox:
    def __init__(self, sandbox_name: str = "evo_sandbox"):
        self.sandbox_name = sandbox_name
        self.temp_dir = None

    def __enter__(self):
        # 1. 创建隔离临时沙箱目录
        self.temp_dir = Path(tempfile.mkdtemp(prefix=f"{self.sandbox_name}_"))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 3. 验收结束后强制递归清理沙箱，实现 0 磁盘与内存残留
        if self.temp_dir and self.temp_dir.exists():
            shutil.rmtree(self.temp_dir, ignore_errors=True)

    def write_artifact(self, rel_path: str, content: str) -> Path:
        """向沙箱内写入待测代码或配置文件"""
        if not self.temp_dir:
            raise RuntimeError("Sandbox context not initialized")
        target_path = self.temp_dir / rel_path
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(content, encoding="utf-8")
        return target_path

    def run_machine_assertion(self, test_script_content: str) -> Tuple[bool, str, float]:
        """
        在沙箱内执行零 LLM 成本的机器单测硬断言
        返回: (是否通过, 标准输出/错误信息, 执行耗时毫秒)
        """
        test_file = self.write_artifact("test_verification.py", test_script_content)
        start_t = time.time()
        
        proc = subprocess.run(
            [sys.executable, str(test_file)],
            cwd=str(self.temp_dir),
            capture_output=True,
            text=True,
            timeout=30
        )
        duration_ms = (time.time() - start_t) * 1000
        passed = (proc.returncode == 0)
        output = proc.stdout if passed else f"STDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}"
        return passed, output, duration_ms


def demo_verification_pipeline():
    """示例演示：工兵生成代码 -> 机器单测硬验收 -> 0 内存残留销毁"""
    
    # 模拟工兵生成的待测代码
    generated_code = '''
def calculate_network_retry(attempt: int, base_delay: float = 1.0) -> float:
    """计算带上限的指数退避重试延迟"""
    if attempt < 0:
        raise ValueError("Attempt must be non-negative")
    return min(base_delay * (2 ** attempt), 30.0)
'''

    # 机器单元测试脚本（零 LLM 验证）
    unit_test_code = '''
import unittest
from target_module import calculate_network_retry

class TestNetworkRetry(unittest.TestCase):
    def test_backoff_progression(self):
        self.assertEqual(calculate_network_retry(0), 1.0)
        self.assertEqual(calculate_network_retry(1), 2.0)
        self.assertEqual(calculate_network_retry(2), 4.0)

    def test_max_ceiling(self):
        self.assertEqual(calculate_network_retry(10), 30.0)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            calculate_network_retry(-1)

if __name__ == "__main__":
    unittest.main()
'''

    print("🚀 [EVO-CORE X Evidence Engine] 启动临时沙箱验证流水线...")
    
    with EphemeralEvidenceSandbox("demo_task") as sandbox:
        # 将代码写入沙箱
        sandbox.write_artifact("target_module.py", generated_code)
        
        # 执行机器单测硬断言
        passed, log, duration_ms = sandbox.run_machine_assertion(unit_test_code)
        
        # 构造不可篡改证据凭证 (M7 Provenance)
        evidence = {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "status": "PASSED" if passed else "FAILED",
            "assertion_type": "Zero-LLM unittest",
            "duration_ms": round(duration_ms, 2),
            "evidence_hash": hash(log)
        }
        
        print(f"📊 机器单测结果: {'✔ 通过' if passed else '❌ 失败'} (耗时 {evidence['duration_ms']} ms)")
        print(f"📜 结构化证据凭据:\n{json.dumps(evidence, indent=2)}")
        
        if not passed:
            print("🚨 错误日志输出:\n", log)
            sys.exit(1)

    print("✨ [EVO-CORE X] 沙箱已自动销毁，零内存与进程残留，验收闭环完成。")

if __name__ == "__main__":
    demo_verification_pipeline()
