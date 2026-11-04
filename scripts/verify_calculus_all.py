"""
《微积分》题库全部章节解答验算汇总入口。

Requirements:
    - sympy

Usage:

    ```bash
    python scripts/verify_calculus_all.py          # 跑全部章节
    python scripts/verify_calculus_chap5.py        # 只跑某一章
    ```

    每章一个 verify_calculus_chapN.py, 本脚本依次调用并汇总退出码。
    脚本内编码的是各题的"标准答案"而非解析 rst 文件, 因此能守住数学正确性;
    若修改了题库中的解答, 请同步更新对应检查项。

"""

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
scripts = sorted(HERE.glob("verify_calculus_chap*.py"))

if not scripts:
    print("未找到 verify_calculus_chap*.py")
    sys.exit(1)

failed = []
for script in scripts:
    result = subprocess.run([sys.executable, str(script)], capture_output=True, text=True)
    status = "OK  " if result.returncode == 0 else "FAIL"
    print(f"[{status}] {script.name}")
    if result.returncode != 0:
        failed.append(script.name)
        sys.stdout.write(result.stdout)
        sys.stderr.write(result.stderr)

print(f"\n{len(scripts) - len(failed)}/{len(scripts)} 章通过")
sys.exit(1 if failed else 0)
