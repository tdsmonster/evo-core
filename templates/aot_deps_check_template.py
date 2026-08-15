#!/usr/bin/env python3
"""
aot_deps_check_template.py — 技能 AOT (Ahead-Of-Time) 环境依赖预检模板
======================================================================
来源: EVO-CORE 理论模块 M6（环境自愈）
理论依据: SkVM (arXiv:2604.03088v3) AOT 依赖绑定原则

作用: 在调用特定复杂技能/工具前，自动进行幂等依赖自检（CLI命令、Python包、后台端口、环境变量），
      在装配期拦截依赖缺失，杜绝运行期静默崩溃。
这是「参考实现骨架」，请按你的实际技能工具清单配置 SKILL_DEPS 字典。
"""

import sys
import shutil
import importlib.util
import socket
import os
from typing import Dict, List, Any

# ============ 按你的技能环境配置依赖清单 ============
# 示例结构：技能名称 -> 需要的前置依赖
SKILL_DEPS: Dict[str, Dict[str, Any]] = {
    "gui-automation-tool": {
        "description": "桌面 GUI 自动化与屏幕像素定位示例",
        "commands": ["cliclick"],           # 依赖的系统 CLI 命令
        "python_packages": ["PIL"],          # 依赖的 Python 库 (Pillow)
        "ports": [],                         # 依赖的后台端口
        "env_vars": ["DISPLAY", "PATH"]      # 依赖的环境变量
    },
    "cdp-browser-automation": {
        "description": "Headless/CDP 浏览器自动化示例",
        "commands": [],
        "python_packages": ["playwright"],
        "ports": [9200],                     # Chrome 调试端口 (示例)
        "env_vars": []
    },
    "local-rag-search": {
        "description": "本地 RAG 混合检索管道示例",
        "commands": ["rg"],                  # ripgrep
        "python_packages": ["sentence_transformers", "torch"],
        "ports": [8000],                     # 本地 Embedding/LLM 推理服务端口 (示例)
        "env_vars": []
    }
}
# ====================================================

def check_command(cmd: str) -> bool:
    """检查 CLI 命令是否存在于 PATH 中"""
    return shutil.which(cmd) is not None

def check_python_package(pkg: str) -> bool:
    """检查 Python 模块/包是否已安装且可导入"""
    return importlib.util.find_spec(pkg) is not None

def check_port(port: int, host: str = "127.0.0.1") -> bool:
    """检查目标 TCP 端口是否正常监听"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        return s.connect_ex((host, port)) == 0

def check_skill(skill_name: str) -> Dict[str, Any]:
    """执行单个技能的 AOT 依赖自检"""
    if skill_name not in SKILL_DEPS:
        return {"status": "unknown", "message": f"未登记 AOT 依赖清单的技能: {skill_name}"}
    
    deps = SKILL_DEPS[skill_name]
    missing = {
        "commands": [],
        "python_packages": [],
        "ports": [],
        "env_vars": []
    }
    
    for cmd in deps.get("commands", []):
        if not check_command(cmd):
            missing["commands"].append(cmd)
            
    for pkg in deps.get("python_packages", []):
        if not check_python_package(pkg):
            missing["python_packages"].append(pkg)
            
    for port in deps.get("ports", []):
        if not check_port(port):
            missing["ports"].append(port)
            
    for env in deps.get("env_vars", []):
        if env not in os.environ or not os.environ[env]:
            missing["env_vars"].append(env)
            
    has_missing = any(len(v) > 0 for v in missing.values())
    return {
        "status": "fail" if has_missing else "pass",
        "skill": skill_name,
        "description": deps.get("description", ""),
        "missing": missing
    }

def main():
    if len(sys.argv) > 1:
        target = sys.argv[1]
        if target == "--all":
            all_pass = True
            print("🔍 正在执行全量 Skill AOT 环境依赖预检 (SkVM 规范)...")
            for name in SKILL_DEPS:
                res = check_skill(name)
                if res["status"] == "pass":
                    print(f"  ✅ [{name}] 依赖完全就绪 ({res['description']})")
                else:
                    all_pass = False
                    print(f"  ❌ [{name}] 缺少依赖! ({res['description']}) -> {res['missing']}")
            sys.exit(0 if all_pass else 1)
        else:
            res = check_skill(target)
            if res["status"] == "pass":
                print(f"✅ 技能 [{target}] AOT 依赖自检通过！")
                sys.exit(0)
            elif res["status"] == "fail":
                print(f"❌ 技能 [{target}] 缺少运行依赖: {res['missing']}")
                sys.exit(1)
            else:
                print(f"⚠️ {res['message']}")
                sys.exit(0)
    else:
        print("用法:")
        print("  python3 aot_deps_check_template.py <skill_name>   # 检查特定技能依赖")
        print("  python3 aot_deps_check_template.py --all          # 扫描所有已注册技能")

if __name__ == "__main__":
    main()
