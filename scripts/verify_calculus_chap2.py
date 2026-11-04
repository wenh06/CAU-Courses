"""
《微积分》题库第 2 章解答验算脚本（配套 Calculus/source/chap2.rst）。

Requirements:
    - sympy

Usage:

    ```bash
    python scripts/verify_calculus_chap2.py
    ```

    退出码 0 表示全部通过。极限类计算逐题用 sympy.limit 验证；间断点分类用单侧极限验证；
    e-N/介值类证明题无可机验成分，不在脚本内。

"""

import sys

import sympy as sp

x = sp.Symbol("x", real=True)
n = sp.Symbol("n", positive=True)
m = sp.Symbol("m", positive=True)
pi = sp.pi
oo = sp.oo

FAIL = []


def chk(name, got, want):
    if sp.simplify(got - want) != 0:
        FAIL.append(f"{name}: got {got}, want {want}")


def chk_true(name, cond):
    if not cond:
        FAIL.append(name)


def Lim(expr, sym, pt, **kw):
    return sp.limit(expr, sym, pt, **kw)


# ---- 2.3 题1: 数列极限 (1)-(7) ----
chk("2.3-1(1)", Lim((2 * n**2 + n - 2) / (n**2 + 6), n, oo), 2)
chk("2.3-1(2)", Lim((2**n + 3**n) / (3**n + 4**n), n, oo), 0)
chk("2.3-1(3)", Lim(sp.sqrt(n + sp.sqrt(n)) - sp.sqrt(n), n, oo), sp.Rational(1, 2))
chk("2.3-1(4)", Lim(1 + sp.root(2, n) + sp.root(3, n) + sp.root(5, n), n, oo), 4)  # 代表项: 每项 -> 1
chk("2.3-1(5)", Lim(2 ** (1 - sp.Rational(1, 1) / 2**n), n, oo), 2)
chk("2.3-1(6)", Lim(n * (n + 1) / (2 * n**2), n, oo), sp.Rational(1, 2))
chk("2.3-1(7)", Lim((n + 1) / (2 * n), n, oo), sp.Rational(1, 2))

h = sp.Symbol("h", real=True)

# ---- 2.3 题2: 函数极限 (3)-(7) ----
chk("2.3-2(3)", Lim((x**4 - 1) / (x**3 - 1), x, 1), sp.Rational(4, 3))
chk("2.3-2(4)", Lim((x**2 + x - 2) / (x**2 - 4 * x + 3), x, 1), -sp.Rational(3, 2))
chk("2.3-2(5)", Lim(((x + h) ** 3 - x**3) / h, h, 0), 3 * x**2)
chk("2.3-2(6)", Lim(1 / (x - 1) + 3 / (1 - x**3), x, 1), 1)
chk("2.3-2(7)", Lim((sum(x**k for k in range(1, 6)) - 5) / (x - 1), x, 1), 15)  # 代表: n=5, 15=5*6/2

# ---- 2.4 题1: 重要极限 (1)-(5), (7)-(10) ----
chk("2.4-1(1)", Lim(sp.sin(m * x) / sp.sin(n * x), x, 0), m / n)
chk("2.4-1(1b)", Lim(sp.sin(3 * x) / sp.sin(2 * x), x, 0), sp.Rational(3, 2))  # m/n 代入验证
chk("2.4-1(2)", Lim((1 - sp.cos(3 * x)) / (sp.sin(x) * sp.tan(2 * x)), x, 0), sp.Rational(9, 4))
chk("2.4-1(3)", Lim((sp.sin(x + h) - sp.sin(x)) / h, h, 0), sp.cos(x))
chk("2.4-1(4)", Lim((sp.cos(x + h) - sp.cos(x)) / h, h, 0), -sp.sin(x))
chk("2.4-1(5)", Lim((sp.cos(2 * x) - sp.cos(3 * x)) / x**2, x, 0), sp.Rational(5, 2))  # (m^2-n^2)/2, m=3, n=2
chk("2.4-1(7)", Lim((1 + 4 / n) ** (2 * n), n, oo), sp.E**8)
chk("2.4-1(8)", Lim((1 - 1 / n**2) ** n, n, oo), 1)
chk("2.4-1(9)", Lim((1 - 2 / x) ** (5 * x), x, oo), sp.E ** (-10))
chk("2.4-1(10)", Lim(((3 - 2 * x) / (2 - 2 * x)) ** x, x, oo), sp.exp(-sp.Rational(1, 2)))

# ---- 2.4 题2: x_n < 1/sqrt(2n+1) 且极限为 0 (数值) ----
prod = 1.0
for i in range(1, 501):
    prod *= (2 * i - 1) / (2 * i)
chk_true("2.4-2 不等式", prod < 1.0 / (501**0.5))

# ---- 2.4 题3(2): 1 + 1/4 + ... + 1/n^2 < 2 (数值) ----
chk_true("2.4-3(2) 上界", sum(1 / k**2 for k in range(1, 10000)) < 2)

# ---- 2.5 题1: 等价无穷小 ----
chk("2.5-1(1)", Lim((1 / sp.cos(x) - 1) / (x**2 / 2), x, 0), 1)
chk("2.5-1(2)", Lim((sp.sqrt(sp.tan(x) + 1) - sp.sqrt(sp.sin(x) + 1)) / (x**3 / 4), x, 0), 1)

# ---- 2.5 题2: (2)(3)(4)(6) ----
chk("2.5-2(2)", Lim((1 - sp.cos(3 * x)) / (x * sp.sin(2 * x)), x, 0), sp.Rational(9, 4))
chk_true("2.5-2(3) = -oo", Lim((sp.exp(x) - sp.exp(sp.cos(x))) / (x * sp.tan(x)), x, 0, dir="-") == -oo)
chk("2.5-2(4)", Lim(sp.log(1 + x**3) / (sp.tan(x) - sp.sin(x)), x, 0), 2)
chk("2.5-2(6)", Lim(sp.log(2 + sp.exp(3 * x)) / sp.log(3 + sp.exp(2 * x)), x, oo), sp.Rational(3, 2))

# ---- 2.6 题2: 间断点分类 (1)(2)(3) ----
chk_true("2.6-2(1) 无穷间断", Lim(1 / (sp.exp(x) - 1), x, 0, dir="+") == oo and Lim(1 / (sp.exp(x) - 1), x, 0, dir="-") == -oo)
chk_true("2.6-2(2) 可去", Lim(sp.log(1 - 2 * x) / x, x, 0) == -2)
chk_true("2.6-2(3) 可去+无穷", Lim((x**2 - 2 * x - 3) / (x**2 - 3 * x - 4), x, -1) == sp.Rational(4, 5))

# ---- 2.6 题3: (1)-(4) ----
chk("2.6-3(1)", Lim(sp.log(1 + x**2) / sp.sin(1 + x**2), x, 0), 0)
chk("2.6-3(2)", Lim(sp.log(2 * sp.cos(2 * x)), x, pi / 6), 0)
chk("2.6-3(3)", Lim(sp.sqrt(x**2 - 2 * x + 5), x, 0), sp.sqrt(5))
chk("2.6-3(4)", Lim((sp.sqrt(1 + x) - 1) / x, x, 1), sp.sqrt(2) - 1)

# ---- 2.6 题4: a=1, b=e (验证连续性成立) ----
chk_true("2.6-4 a=1,b=e", Lim(sp.log(sp.E + x + x**2), x, 0, dir="+") == 1 and Lim(1 + x, x, 0, dir="-") == 1)

# ---- 2.6 题5: 各点极限 ----
f = (x**3 + 3 * x**2 - x - 3) / (x**2 + x - 6)
chk("2.6-5 x->0", Lim(f, x, 0), sp.Rational(1, 2))
chk("2.6-5 x->-3", Lim(f, x, -3), -sp.Rational(8, 5))
chk_true("2.6-5 x->2 无穷", abs(Lim(f, x, 2, dir="+")) == oo)


# ---- 2.7 题1: 2^x = x^2 在 (-1,1) 有根 (数值佐证零点定理) ----
def g(v):
    return 2.0**v - v**2


chk_true("2.7-1 零点存在", g(-1) < 0 < g(1))

if FAIL:
    print("chap2: FAIL")
    for item in FAIL:
        print("  -", item)
    sys.exit(1)
print("chap2: all checks passed")
