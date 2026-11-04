"""
《微积分》题库第 1 章解答验算脚本（配套 Calculus/source/chap1.rst）。

Requirements:
    - sympy

Usage:

    ```bash
    python scripts/verify_calculus_chap1.py
    ```

    退出码 0 表示全部通过。凡是可以机器验算的计算题（反函数、奇偶性、极坐标互化、参数方程消参等）均逐题验证；
    证明题只验其"可计算成分"（具体实例、数值样例），结构性论证本身不在此列。

"""

import sys

import sympy as sp

x = sp.Symbol("x", real=True)
u = sp.Symbol("u", real=True)
t = sp.Symbol("t", real=True)
th = sp.Symbol("theta", real=True)
pi = sp.pi

FAIL = []


def chk_true(name, cond):
    if not cond:
        FAIL.append(name)


# ---- 1.1 题3: 奇偶性 (2)(3) ----
f = (sp.exp(x) - sp.exp(-x)) / (sp.exp(x) + sp.exp(-x))
chk_true("1.1-3(2) 奇函数", sp.simplify(f.subs(x, -x) + f) == 0)
f = sp.log(sp.sqrt(1 + x**2) - x)
chk_true(
    "1.1-3(3) 奇函数",
    all(abs(float(f.subs(x, v) + f.subs(x, -v))) < 1e-12 for v in [0.3, 1.2, 2.5]),
)

# ---- 1.1 题3(4): 3^x x 非奇非偶 (数值取样) ----
f = 3**x * x
chk_true("1.1-3(4) 非奇非偶", any(abs(float(f.subs(x, v) + f.subs(x, -v))) > 1e-6 for v in [0.3, 1.1]))

# ---- 1.1 题6(2): |x/(x^2+1)| <= 1/2 ----
chk_true("1.1-6(2) 有界性", sp.maximum(sp.Abs(x / (x**2 + 1)), x, sp.S.Reals) == sp.Rational(1, 2))

# ---- 1.2 题1: 反函数复合互验 ----
f = (2 - u) / (2 + u)
finv = (2 - 2 * u) / (1 + u)
chk_true("1.2-1(2) 反函数", sp.simplify(f.subs(u, finv) - u) == 0 and sp.simplify(finv.subs(u, f) - u) == 0)
chk_true("1.2-1(3) 反函数", sp.simplify(sp.sin(sp.asin(x / 3)) - x / 3) == 0)
chk_true("1.2-1(4) 反函数", sp.simplify(2 + sp.log(sp.exp(x - 2) - 1 + 1) - x) == 0)

# ---- 1.3 题3: sinh 的反函数 (数值) ----
inv = sp.log(x + sp.sqrt(x**2 + 1))
d = (sp.exp(inv) - sp.exp(-inv)) / 2 - x
chk_true(
    "1.3-3 sinh 反函数",
    all(abs(float(d.subs(x, v))) < 1e-12 for v in [-3.7, -0.5, 1.2, 5.0]),
)

# ---- 1.4 题1: 极坐标 -> 直角坐标 ----
pts = [
    (2, pi / 6, sp.sqrt(3), 1),
    (3, pi / 2, 0, 3),
    (1, -pi / 4, sp.sqrt(2) / 2, -sp.sqrt(2) / 2),
    (4, 5 * pi / 4, -2 * sp.sqrt(2), -2 * sp.sqrt(2)),
]
for i, (r, angle, px, py) in enumerate(pts, start=1):
    ok = sp.simplify(r * sp.cos(angle) - px) == 0 and sp.simplify(r * sp.sin(angle) - py) == 0
    chk_true(f"1.4-1 点{i}", ok)

# ---- 1.4 题2: 直角坐标 -> 极坐标 (反验) ----
pts2 = [
    (1, sp.sqrt(3), 2, pi / 3),
    (-sp.sqrt(3), 1, 2, 5 * pi / 6),
    (-1, sp.sqrt(3), 2, 2 * pi / 3),
    (sp.sqrt(3), -1, 2, -pi / 6),
]
for i, (px, py, r, angle) in enumerate(pts2, start=1):
    ok = sp.simplify(r * sp.cos(angle) - px) == 0 and sp.simplify(r * sp.sin(angle) - py) == 0
    chk_true(f"1.4-2 点{i}", ok)

# ---- 1.4 题3(3): r = 2cos(theta) 即 (x-1)^2 + y^2 = 1 ----
xx = 2 * sp.cos(th) * sp.cos(th)
yy = 2 * sp.cos(th) * sp.sin(th)
chk_true("1.4-3(3) 圆", sp.simplify((xx - 1) ** 2 + yy**2 - 1) == 0)

# ---- 1.4 题5(2): x^2 - y^2 = 4 (数值) ----
chk_true(
    "1.4-5(2) 双曲线",
    all(abs((v + 1 / v) ** 2 - (v - 1 / v) ** 2 - 4) < 1e-12 for v in [0.3, 2.0, -1.7]),
)

# ---- 总习题1 题1: B 选项 f 在 x=2 无定义 (选项结论的人工核对辅助) ----
chk_true("总1-B: (x^2-4)/(x-2) 在 x=2 无定义", sp.sympify((x**2 - 4) / (x - 2)).subs(x, 2) is sp.nan)

if FAIL:
    print("chap1: FAIL")
    for item in FAIL:
        print("  -", item)
    sys.exit(1)
print("chap1: all checks passed")
