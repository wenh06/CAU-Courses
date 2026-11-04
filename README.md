# CAU-Courses

Math courses at CAU

## 项目结构

- `Calculus/` —— 《微积分》课后习题解答 (Sphinx; 题库在 `source/chap1-6.rst`, `make html` 构建)
- `RealAnalysis/` —— 《实变函数》课后习题解答 (Sphinx; `source/chapter*/`)
- `MathematicalAnalysis/` —— 《数学分析》
- `scripts/` —— 工具脚本: 成绩计算、图像处理、以及题库解答验算 `verify_calculus_*.py`
  (逐题机器验算, `python scripts/verify_calculus_all.py` 一键重跑; 修改解答后应同步更新对应检查项)

## 待办

- [ ] (2026-11-03) 试验在 Calculus 书页中嵌入可交互代码 cell (`jupyterlite-sphinx`, Pyodide/WASM 在浏览器内运行, 无需服务器)。
      动构建配置前需老师确认: 需引入 node 构建链, HTML 产物约 +10 MB WASM 资产, webapp 部署需同步调整。
      当前替代方案: `scripts/verify_calculus_*.py` 仓库内验算脚本。
