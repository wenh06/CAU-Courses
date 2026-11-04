"""
《微积分》题库第 4 章解答验算脚本（配套 Calculus/source/chap4.rst）。

Requirements:
    - sympy

Usage:

    ```bash
    python scripts/verify_calculus_chap4.py
    ```

    退出码 0 表示全部通过。洛必达极限逐题验证；泰勒多项式按定义验证与原函数各阶导数在展开点一致；
    极值/最值/凹凸与应用题验证临界点与取值；中值定理类证明题只验可计算成分
    (如 4.1 题1 的 xi=2 满足 f'(2)=0、总习题12 用具体 f, g 验证结论)。

"""

import random
import sys

import sympy as sp

x = sp.Symbol("x", real=True)
a = sp.Symbol("a", positive=True)
V = sp.Symbol("V", positive=True)
bb = sp.Symbol("b", positive=True)
cc = sp.Symbol("c", positive=True)
pi = sp.pi
oo = sp.oo

FAIL = []


def chk(name, got, want):
    if sp.simplify(got - want) != 0:
        FAIL.append(f"{name}: diff={sp.simplify(got - want)}")


def chk_close(name, got, want, tol):
    if abs(float(sp.N(got - want))) > tol:
        FAIL.append(f"{name}: {got} vs {want}")


def chk_true(name, cond):
    if not cond:
        FAIL.append(name)


L = sp.limit

# ---- 4.1 题1: 罗尔定理 xi = 2 (证明题的可计算成分) ----
f = x * sp.sqrt(3 - x)
chk_true("4.1-1 f'(2)=0", sp.simplify(sp.diff(f, x).subs(x, 2)) == 0)
chk_true("4.1-1 f' 公式", sp.simplify(sp.diff(f, x) - (6 - 3 * x) / (2 * sp.sqrt(3 - x))) == 0)

# ---- 4.1 题2: f'(x)=0 恰有 3 个实根, 分别在 (2,3),(3,4),(4,5) ----
fp = sp.diff((x - 2) * (x - 3) * (x - 4) * (x - 5), x)
roots = sorted(sp.nroots(fp))
chk_true(
    "4.1-2 三个实根位置",
    len(roots) == 3
    and all(abs(sp.im(r)) < 1e-12 for r in roots)
    and all(2 + i < sp.re(r) < 3 + i for i, r in enumerate(roots)),
)

# ---- 4.2 题1: 洛必达极限 (1)-(8) ----
chk("4.2-1(1)", L(sp.log(1 + x) / x, x, 0), 1)
chk("4.2-1(2)", L((sp.exp(x) - sp.exp(-x)) / sp.sin(x), x, 0), 2)
chk("4.2-1(3)", L((sp.tan(x) - x) / (x - sp.sin(x)), x, 0), 2)
chk("4.2-1(4)", L(sp.sin(3 * x) / sp.tan(5 * x), x, 0), sp.Rational(3, 5))
chk("4.2-1(5)", L((x**3 - 8) / (x**2 - 4), x, 2), 3)  # m=3, n=2, a=2: (m/n) a^{m-n} = 3
chk("4.2-1(6)", L(2 / (x**2 - 1) - 1 / (x - 1), x, 1), -sp.Rational(1, 2))
chk("4.2-1(7)", L((1 + 2 / x) ** x, x, oo), sp.E**2)  # a=2 代表
chk("4.2-1(8)", L(x ** sp.sin(x), x, 0), 1)
chk_true("4.2-2 极限存在", L((x + sp.sin(x)) / x, x, oo) == 1)

# ---- 4.3 题2/3: 泰勒多项式与 f 在 x0=pi 的各阶导数一致 ----
f = sp.sin(x) + x**2
P3 = pi**2 + (2 * pi - 1) * (x - pi) + (x - pi) ** 2 + (x - pi) ** 3 / 6
chk_true(
    "4.3-2/3 泰勒多项式",
    all(sp.simplify(sp.diff(P3, x, k).subs(x, pi) - sp.diff(f, x, k).subs(x, pi)) == 0 for k in range(4)),
)

# ---- 4.3 题5: 三次多项式泰勒展开是精确的 (f''(2)=12, 二次项系数 6) ----
chk_true("4.3-5", sp.expand((x**3 + 6 * x - 1) - (19 + 18 * (x - 2) + 6 * (x - 2) ** 2 + (x - 2) ** 3)) == 0)

# ---- 4.3 题6: (1+x)^a 麦克劳林系数 ----
chk("4.3-6", sp.diff((1 + x) ** a, x, 3).subs(x, 0) / 6, a * (a - 1) * (a - 2) / 6)

# ---- 4.3 题7: 1957/720, 误差 < 1e-3 ----
chk_close("4.3-7 近似值", sp.Rational(1957, 720).evalf(12), sp.E.evalf(12), tol=1e-3)
chk_true("4.3-7 余项估计", float(3 / sp.factorial(7)) < 1e-3)

# ---- 4.4 题2: 驻点 1, 2 ----
f = 2 * x**3 - 9 * x**2 + 12 * x - 3
chk_true("4.4-2 驻点", sorted(sp.solve(sp.diff(f, x), x)) == [1, 2])

# ---- 4.5 题1: 各小题极值 ----
y1 = x**3 - 3 * x**2 - 9 * x + 5
chk_true("4.5-1(1)", sorted(sp.solve(sp.diff(y1, x), x)) == [-1, 3] and y1.subs(x, -1) == 10 and y1.subs(x, 3) == -22)
y2 = (x - 1) * x ** sp.Rational(2, 3)
chk_true(
    "4.5-1(2)",
    sp.simplify(y2.subs(x, sp.Rational(2, 5)) + sp.Rational(3, 5) * (sp.Rational(4, 25)) ** sp.Rational(1, 3)) == 0
    and y2.subs(x, 0) == 0,
)
y3 = x - 2 * sp.sin(x)
chk_true(
    "4.5-1(3)",
    sp.simplify(y3.subs(x, pi / 3) - (pi / 3 - sp.sqrt(3))) == 0
    and sp.simplify(y3.subs(x, 5 * pi / 3) - (5 * pi / 3 + sp.sqrt(3))) == 0,
)
y4 = x + sp.sqrt(1 - x)
chk_true("4.5-1(4)", sp.simplify(y4.subs(x, sp.Rational(3, 4)) - sp.Rational(5, 4)) == 0)
y5 = x**2 * sp.log(x)
chk_true("4.5-1(5)", sp.simplify(y5.subs(x, sp.exp(-sp.Rational(1, 2))) + sp.Rational(1, 2) / sp.E) == 0)
y6 = sp.log(x) ** 2 / x
chk_true("4.5-1(6)", y6.subs(x, 1) == 0 and sp.simplify(y6.subs(x, sp.exp(2)) - 4 / sp.exp(2)) == 0)

# ---- 4.5 题2: 最值 (1)(2)(4)(5) ----
chk_true("4.5-2(1)", (x**4 - 8 * x**2 + 6).subs(x, 3) == 15 and (x**4 - 8 * x**2 + 6).subs(x, 2) == -10)
chk_true("4.5-2(2)", sp.simplify((x + sp.sqrt(1 - x)).subs(x, sp.Rational(3, 4)) - sp.Rational(5, 4)) == 0)
chk_true(
    "4.5-2(4)",
    abs(x**2 + 3 * x + 2).subs(x, -sp.Rational(3, 2)) == sp.Rational(1, 4) and abs(x**2 + 3 * x + 2).subs(x, 3) == 20,
)
f5 = sp.sqrt(x) * sp.log(x)
chk_true(
    "4.5-2(5)", sp.simplify(f5.subs(x, sp.exp(-2)) + 2 / sp.E) == 0 and sp.simplify(sp.diff(f5, x).subs(x, sp.exp(-2))) == 0
)

# ---- 4.5 题3: a = -6 时 y'(1)=0, y''(1)=12>0 ----
f3 = 2 * x**3 - 6 * x + 3
chk_true("4.5-3", f3.diff(x).subs(x, 1) == 0 and f3.diff(x, 2).subs(x, 1) == 12)

# ---- 4.5 题4/5 ----
chk_true("4.5-4", sp.solve(sp.diff(x**2 - 54 / x, x), x) == [-3] and (x**2 - 54 / x).subs(x, -3) == 27)
chk_true("4.5-5", sp.solve(sp.diff(x / (1 + x**2), x), x) == [-1, 1] and (x / (1 + x**2)).subs(x, 1) == sp.Rational(1, 2))

# ---- 4.5 题7: 箱子 S = 4x^2 + 216/x, x=3 最小, S=108 ----
S = 4 * x**2 + 216 / x
chk_true("4.5-7", sp.solve(sp.diff(S, x), x) == [3] and S.subs(x, 3) == 108)

# ---- 4.5 题8: V = x(a-2x)^2 在 x = a/6 最大, V = 2a^3/27 ----
Vbox = x * (a - 2 * x) ** 2
chk_true(
    "4.5-8",
    sp.solve(sp.diff(Vbox, x), x) == [a / 6, a / 2] and sp.simplify(Vbox.subs(x, a / 6) - sp.Rational(2, 27) * a**3) == 0,
)

# ---- 4.5 题9: 圆柱 r = (V/2pi)^{1/3}, h = 2r, S_min = 3 (2 pi V^2)^{1/3} ----
r0 = (V / (2 * pi)) ** sp.Rational(1, 3)
S = 2 * pi * r0**2 + 2 * V / r0
chk_true(
    "4.5-9", sp.simplify(S - 3 * (2 * pi * V**2) ** sp.Rational(1, 3)) == 0 and sp.simplify(V / (pi * r0**2) - 2 * r0) == 0
)

# ---- 4.5 题10: x* = sqrt(2ab/c), P(x*) = sqrt(2abc) (取正根) ----
P = a * bb / x + cc * x / 2
roots = sp.solve(sp.diff(P, x), x)
xs = [r for r in roots if r.is_positive][0]
chk_true(
    "4.5-10", sp.simplify(xs - sp.sqrt(2 * a * bb / cc)) == 0 and sp.simplify(P.subs(x, xs) - sp.sqrt(2 * a * bb * cc)) == 0
)

# ---- 4.6 题2: g'' = 48x^2 - 18x + 4 > 0 ----
g = 4 * x**4 - 3 * x**3 + 2 * x**2
chk_true("4.6-2", sp.simplify(sp.diff(g, x, 2) - (48 * x**2 - 18 * x + 4)) == 0 and sp.diff(g, x, 2).subs(x, 0) > 0)

# ---- 4.6 题4: 反例 e^{-x^2} 在 0 处二阶导为负 ----
chk_true("4.6-4 反例", sp.diff(sp.exp(-(x**2)), x, 2).subs(x, 0) == -2)

# ---- 4.6 题5: AM-GM 与 ln x <= x-1 数值实例 (证明题的可计算成分) ----
vals = [sp.Rational(str(v)) for v in [random.uniform(0.1, 20) for _ in range(5)]]
chk_true("4.6-5(1) AM>=GM", sum(vals) / 5 >= sp.prod(vals) ** sp.Rational(1, 5))
chk_true("4.6-5(2)", all(sp.log(sp.Rational(str(v))) <= v - 1 for v in [0.05, 0.5, 1.0, 3.7]))

# ---- 4.6 题6(2): 斜渐近线 y = x - 2 ----
f62 = x**3 / (x**2 + 2 * x - 3)
chk_true("4.6-6(2)", sp.simplify(L(f62 / x, x, oo) - 1) == 0 and sp.simplify(L(f62 - x, x, oo) + 2) == 0)

# ---- 4.7 题1: 因式分解与特征值 ----
f71 = x**3 - x**2 - x + 1
chk_true(
    "4.7-1",
    sp.factor(f71) == (x - 1) ** 2 * (x + 1) and sp.simplify(f71.subs(x, -sp.Rational(1, 3)) - sp.Rational(32, 27)) == 0,
)

# ---- 总习题1: 五个极限 ----
chk("z1(1)", L((sp.exp(x) - sp.exp(-x)) / sp.sin(x), x, 0), 2)
chk("z1(2)", L((sp.tan(x) - x) / x**3, x, 0), sp.Rational(1, 3))
chk("z1(3)", L(sp.log(sp.cos(x)) / x**2, x, 0), -sp.Rational(1, 2))
chk("z1(4)", L((2**x - 1) / (3 * x), x, 0), sp.log(2) / 3)
chk("z1(5)", L(x**2 * sp.log(1 + 1 / x) - x, x, oo), -sp.Rational(1, 2))

# ---- 总习题3: arctan 不等式数值实例 ----
chk_true("z3 不等式", all(float(x0 / (1 + x0**2)) < float(sp.atan(x0)) < x0 for x0 in [0.1, 0.7, 2.3]))

# ---- 总习题6: 最大 1/4, 最小 0 ----
f6 = 4 * x**2 * (1 - x) ** 2
chk_true("z6", f6.subs(x, sp.Rational(1, 2)) == sp.Rational(1, 4) and f6.subs(x, 0) == 0 and f6.subs(x, 1) == 0)


# ---- 总习题8: 方程 ln x - x/e + 1 = 0 恰两根 (数值扫描) ----
def fv(v):
    return float(sp.log(v) - v / sp.E + 1)


grid = [0.02 + i * (30 - 0.02) / 4000 for i in range(4001)]
vals = [fv(v) for v in grid]
crossings = sum(1 for i in range(len(grid) - 1) if vals[i] * vals[i + 1] < 0)
chk_true("z8 两根", crossings == 2 and fv(2.718281828459045) > 0)

# ---- 总习题9/10: 极值与拐点 ----
y9 = x**3 - 3 * x**2 - 1
chk_true("z9", y9.subs(x, 0) == -1 and y9.subs(x, 2) == -5 and y9.subs(x, 1) == -3 and sp.diff(y9, x, 2).subs(x, 1) == 0)
y10 = sp.log(1 + x**2)
chk_true("z10", y10.subs(x, 1) == sp.log(2) and sp.simplify(sp.diff(y10, x, 2).subs(x, 1)) == 0)

# ---- 总习题11: 驻点与端值 ----
y11 = (x - 2) * (3 - x) / x**2
chk_true(
    "z11",
    y11.subs(x, 1) == -2 and sp.simplify(y11.subs(x, sp.Rational(12, 5)) - sp.Rational(1, 24)) == 0 and y11.subs(x, 3) == 0,
)

# ---- 总习题12: 具体实例验证 (f = 2-x, g = 1+x, 区间 [0,1]: f(0)=g(1)=2, f(1)=g(0)=1) ----
fz = 2 - x
gz = 1 + x
xi = sp.Rational(1, 2)  # h = fz*gz 的罗尔中值点: h'(x) = 1-2x = 0
chk_true(
    "z12 实例",
    fz.subs(x, 0) == gz.subs(x, 1) and fz.subs(x, 1) == gz.subs(x, 0) and sp.simplify(sp.diff(fz * gz, x).subs(x, xi)) == 0,
)

if FAIL:
    print("chap4: FAIL")
    for item in FAIL:
        print("  -", item)
    sys.exit(1)
print("chap4: all checks passed")
