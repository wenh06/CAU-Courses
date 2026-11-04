"""
《微积分》题库第 5 章解答验算脚本（配套 Calculus/source/chap5.rst）。

Requirements:
    - sympy

Usage:

    ```bash
    python scripts/verify_calculus_chap5.py
    ```

    退出码 0 表示全部通过。不定积分逐个验证: 对给出的原函数求导、化简后与被积函数比对为零。
    个别带根式/立方根的项依赖 sympy 主值分支约定，与解答采用同一表达式形式，故求导恒等式严格成立。

"""

import sys

import sympy as sp

x = sp.Symbol("x", positive=True)
t = sp.Symbol("t", positive=True)
a = sp.Symbol("a", positive=True)
b = sp.Symbol("b", positive=True)
om = sp.Symbol("omega", positive=True)
ph = sp.Symbol("phi", positive=True)

FAIL = []


def chk(name, F, integrand):
    d = sp.simplify(sp.together(sp.diff(F, x) - integrand))
    if d != 0:
        FAIL.append(f"{name}: diff={d}")


def chk_true(name, cond):
    if not cond:
        FAIL.append(name)


def chk_t(name, F, integrand):
    d = sp.simplify(sp.together(sp.diff(F, t) - integrand))
    if d != 0:
        FAIL.append(f"{name}: diff={d}")


# ---- 5.1 题1: 12 个小积分 ----
chk("1(1)", -2 / (3 * x ** sp.Rational(3, 2)), x ** (-sp.Rational(5, 2)))
chk("1(2)", x**3 / 3 - 3 * x**2 / 2 + 2 * x, x**2 - 3 * x + 2)
chk(
    "1(3)",
    2 * x ** sp.Rational(1, 2) - sp.Rational(4, 3) * x ** sp.Rational(3, 2) + sp.Rational(2, 5) * x ** sp.Rational(5, 2),
    (1 - x) ** 2 / x ** sp.Rational(1, 2),
)
chk("1(4)", 2 * sp.exp(x) + 3 * sp.log(x), 2 * sp.exp(x) + 3 / x)
chk("1(5)", 3 * sp.atan(x) - 2 * sp.asin(x), 3 / (1 + x**2) - 2 / sp.sqrt(1 - x**2))
chk("1(6)", sp.tan(x) - sp.sec(x), sp.sec(x) ** 2 - sp.sec(x) * sp.tan(x))
chk("1(7)", x / 2 + sp.sin(x) / 2, (1 + sp.cos(x)) / 2)
chk("1(8)", sp.tan(x) / 2, 1 / (1 + sp.cos(2 * x)))
chk("1(9)", x**3 - x + sp.atan(x), (3 * x**4 + 2 * x**2) / (x**2 + 1))
chk("1(10)", -1 / (3 * x**3) + 1 / x + sp.atan(x), 1 / (x**4 + x**6))
chk("1(11)", 2 * sp.asin(x), 2 / sp.sqrt(1 - x**2))
chk("1(12)", sp.tan(x) / 2 + x / 2, (1 + sp.cos(x) ** 2) / (1 + sp.cos(2 * x)))

# ---- 5.1 题2 ----
chk_true("1.1-2", sp.simplify(x * (-1 / (x * sp.sqrt(1 - x**2))) - sp.diff(sp.acos(x), x)) == 0)

# ---- 5.1 题4: y = ln x + 1 ----
chk_true("1.1-4", sp.simplify(sp.diff(sp.log(x) + 1, x) - 1 / x) == 0)

# ---- 5.1 题5: s = t^3 ----
chk_true("1.1-5", sp.simplify(sp.diff(t**3, t) - 3 * t**2) == 0)

# ---- 5.2 题1: 16 个凑微分系数 (c * d(phi) 求导后应还原原式左端 lhs) ----
coeffs = {
    1: (x, 1 / a, a * x, 1),
    2: (x, sp.Rational(1, 7), 7 * x - 3, 1),
    3: (x, sp.Rational(1, 2), x**2, x),
    4: (x, sp.Rational(1, 10), 5 * x**2, x),
    5: (x, -sp.Rational(1, 2), 1 - x**2, x),
    6: (x, sp.Rational(1, 12), 3 * x**4 - 2, x**3),
    7: (x, sp.Rational(1, 2), sp.exp(2 * x), sp.exp(2 * x)),
    8: (x, -2, 1 + sp.exp(-x / 2), sp.exp(-x / 2)),
    9: (x, -sp.Rational(2, 3), sp.cos(3 * x / 2), sp.sin(3 * x / 2)),
    10: (x, sp.Rational(1, 5), 5 * sp.log(x), 1 / x),
    11: (x, -sp.Rational(1, 5), 3 - 5 * sp.log(x), 1 / x),
    12: (x, sp.Rational(1, 3), sp.atan(3 * x), 1 / (1 + 9 * x**2)),
    13: (x, -1, 1 - sp.asin(x), 1 / sp.sqrt(1 - x**2)),
    14: (x, -1, sp.sqrt(1 - x**2), x / sp.sqrt(1 - x**2)),
    15: (t, 2, sp.sqrt(t), 1 / sp.sqrt(t)),
    16: (x, sp.Rational(1, 2), sp.tan(2 * x), 1 / sp.cos(2 * x) ** 2),
}
for key, (var, c, phi, lhs) in coeffs.items():
    d = sp.simplify(sp.diff(c * phi, var) - lhs)
    if d != 0:
        FAIL.append(f"5.2-1({key}): diff={d}")

# ---- 5.2 题2: 34 个小积分 ----
chk("s2(1)", sp.exp(5 * x) / 5, sp.exp(5 * x))
chk("s2(2)", -((3 - 2 * x) ** 4) / 8, (3 - 2 * x) ** 3)
chk("s2(3)", -sp.log(1 - 2 * x) / 2, 1 / (1 - 2 * x))
chk("s2(4)", -((2 - 3 * x) ** sp.Rational(2, 3)) / 2, (2 - 3 * x) ** (-sp.Rational(1, 3)))
chk("s2(5)", -sp.cos(a * x) / a - b * sp.exp(x / b), sp.sin(a * x) - sp.exp(x / b))
chk_t("s2(6)", -2 * sp.cos(sp.sqrt(t)), sp.sin(sp.sqrt(t)) / sp.sqrt(t))
chk("s2(7)", -sp.exp(-(x**2)) / 2, x * sp.exp(-(x**2)))
chk("s2(8)", sp.sin(x**2) / 2, x * sp.cos(x**2))
chk("s2(9)", -sp.sqrt(2 - 3 * x**2) / 3, x / sp.sqrt(2 - 3 * x**2))
chk("s2(10)", -sp.Rational(3, 4) * sp.log(1 - x**4), 3 * x**3 / (1 - x**4))
chk("s2(11)", sp.log(x**2 + 2 * x + 5) / 2, (x + 1) / (x**2 + 2 * x + 5))
chk("s2(12)", 1 / (2 * sp.cos(x) ** 2), sp.sin(x) / sp.cos(x) ** 3)
chk(
    "s2(13)",
    sp.Rational(3, 2) * (sp.sin(x) - sp.cos(x)) ** sp.Rational(2, 3),
    (sp.sin(x) + sp.cos(x)) / (sp.sin(x) - sp.cos(x)) ** sp.Rational(1, 3),
)
chk("s2(14)", sp.tan(x) ** 11 / 11, sp.tan(x) ** 10 * sp.sec(x) ** 2)
chk("s2(15)", -1 / sp.asin(x), 1 / (sp.asin(x) ** 2 * sp.sqrt(1 - x**2)))
chk("s2(16)", -sp.log(sp.cos(sp.sqrt(1 + x**2))), sp.tan(sp.sqrt(1 + x**2)) * x / sp.sqrt(1 + x**2))
chk("s2(17)", sp.atan(sp.sqrt(x)) ** 2, sp.atan(sp.sqrt(x)) / (sp.sqrt(x) * (1 + x)))
chk("s2(18)", -1 / (x * sp.log(x)), (1 + sp.log(x)) / (x * sp.log(x)) ** 2)
chk("s2(19)", sp.log(sp.tan(x)), 1 / (sp.sin(x) * sp.cos(x)))
chk("s2(20)", sp.log(sp.tan(x)) ** 2 / 2, sp.log(sp.tan(x)) / (sp.cos(x) * sp.sin(x)))
chk("s2(21)", sp.sin(x) - sp.sin(x) ** 3 / 3, sp.cos(x) ** 3)
chk_t("s2(22)", t / 2 + sp.sin(2 * om * t + 2 * ph) / (4 * om), sp.cos(om * t + ph) ** 2)
chk("s2(23)", sp.sec(x) ** 3 / 3 - sp.sec(x), sp.tan(x) ** 3 * sp.sec(x))
chk("s2(24)", sp.atan(sp.exp(x)), 1 / (sp.exp(x) + sp.exp(-x)))
chk("s2(25)", sp.asin(2 * x / 3) / 2 + sp.sqrt(9 - 4 * x**2) / 4, (1 - x) / sp.sqrt(9 - 4 * x**2))
chk("s2(26)", x**2 / 2 - sp.Rational(9, 2) * sp.log(9 + x**2), x**3 / (9 + x**2))
chk("s2(27)", a**2 / 2 * sp.asin(x / a) - x * sp.sqrt(a**2 - x**2) / 2, x**2 / sp.sqrt(a**2 - x**2))
chk("s2(28)", x / sp.sqrt(1 + x**2), 1 / (x**2 + 1) ** sp.Rational(3, 2))
chk("s2(29)", sp.sqrt(2 * x) - sp.log(1 + sp.sqrt(2 * x)), 1 / (1 + sp.sqrt(2 * x)))
chk("s2(30)", sp.asin(x) + (sp.sqrt(1 - x**2) - 1) / x, 1 / (1 + sp.sqrt(1 - x**2)))
chk("s2(31)", sp.log(x**2 + 2 * x + 3) / 2 - sp.sqrt(2) * sp.atan((x + 1) / sp.sqrt(2)), (x - 1) / (x**2 + 2 * x + 3))
chk("s2(32)", sp.acos(1 / x), 1 / (x * sp.sqrt(x**2 - 1)))
chk("s2(33)", sp.sqrt(x**2 - 9) - 3 * sp.acos(3 / x), sp.sqrt(x**2 - 9) / x)
chk("s2(34)", sp.log(x**2 + 1) / 2 + sp.atan(x) / 2 + (x + 1) / (2 * (x**2 + 1)), (x**3 + 1) / (x**2 + 1) ** 2)

# ---- 5.3 题1: 10 个分部积分 ----
chk("p1(1)", sp.sin(x) - x * sp.cos(x), x * sp.sin(x))
chk("p1(2)", -(sp.log(x) + 1) / x, sp.log(x) / x**2)
chk("p1(3)", sp.log(x) * (sp.log(sp.log(x)) - 1), sp.log(sp.log(x)) / x)
chk("p1(4)", x**2 * sp.sin(x) + 2 * x * sp.cos(x) - 2 * sp.sin(x), x**2 * sp.cos(x))
y_ = sp.Symbol("y", positive=True)
F5 = -(2 * y_ + 1) * sp.exp(-2 * y_) / 4
if sp.simplify(sp.diff(F5, y_) - y_ * sp.exp(-2 * y_)) != 0:
    FAIL.append("p1(5)")
chk("p1(6)", x * sp.asin(x) + sp.sqrt(1 - x**2), sp.asin(x))
chk("p1(7)", x * sp.asin(x) ** 2 + 2 * sp.sqrt(1 - x**2) * sp.asin(x) - 2 * x, sp.asin(x) ** 2)
chk("p1(8)", x * sp.tan(x) + sp.log(sp.cos(x)) - x**2 / 2, x * sp.tan(x) ** 2)
chk("p1(9)", x * sp.acos(x) ** 2 - 2 * sp.sqrt(1 - x**2) * sp.acos(x) - 2 * x, sp.acos(x) ** 2)
chk("p1(10)", sp.tan(x) * sp.log(sp.cos(x)) + sp.tan(x) - x, sp.log(sp.cos(x)) / sp.cos(x) ** 2)


# ---- 5.4 题1: 8 个小积分 ((1)(5) 带分支问题, 数值取样验证) ----
def Fnum(v):
    return -1.5 * ((v + 1) / (v - 1)) ** (1.0 / 3.0)


def gnum(v):
    return ((v + 1) ** 2 * (v - 1) ** 4) ** (-1.0 / 3.0)


chk_true(
    "s4(1) 数值",
    all(abs((Fnum(v + 1e-7) - Fnum(v - 1e-7)) / 2e-7 - gnum(v)) < 1e-5 for v in [2.0, 3.0, 1.5]),
)
chk("s4(2)", x**4 / 4 - 2 * x**3 / 3 + 2 * x**2 - 8 * x + 16 * sp.log(x + 2), x**4 / (x + 2))
chk("s4(3)", x**4 / 4 - sp.log(x**4 + 2) / 2, x**7 / (x**4 + 2))
chk("s4(4)", x / 5 + sp.Rational(2, 5) * sp.log(2 * sp.sin(x) + sp.cos(x)), sp.cos(x) / (2 * sp.sin(x) + sp.cos(x)))


def F5num(v):
    return 0.5 * sp.atan(2 * sp.tan(v / 2))


chk_true(
    "s4(5) 数值",
    all(
        abs(float((F5num(v + 1e-7) - F5num(v - 1e-7)) / 2e-7) - float(1 / (5 - 3 * sp.cos(v)))) < 1e-5 for v in [0.3, 0.8, 1.2]
    ),
)
chk("s4(6)", -1 / (3 * sp.sin(x) ** 3) + 2 / sp.sin(x) + sp.sin(x), sp.cos(x) ** 5 / sp.sin(x) ** 4)
# (7): F(q) = 12/7 (1+q)^{7/3} - 3 (1+q)^{4/3}, q = x^{1/4}
q = sp.Symbol("q", positive=True)
F7 = sp.Rational(12, 7) * (1 + q) ** sp.Rational(7, 3) - 3 * (1 + q) ** sp.Rational(4, 3)
d7 = sp.simplify(
    sp.diff(F7, q).subs(q, x ** sp.Rational(1, 4)) * sp.Rational(1, 4) * x ** (-sp.Rational(3, 4))
    - (1 + x ** sp.Rational(1, 4)) ** sp.Rational(1, 3) / x ** sp.Rational(1, 2)
)
if d7 != 0:
    FAIL.append(f"s4(7): diff={d7}")
chk("s4(8)", sp.atan(x / sp.sqrt(1 + x**2)), 1 / ((2 * x**2 + 1) * sp.sqrt(x**2 + 1)))

# ---- 5.4 题3: 2 sqrt(f(u)) 对 u = ln x 复合, d/du = f'/sqrt(f) ----
u = sp.Symbol("u")
f = sp.Function("f")
F3 = 2 * sp.sqrt(f(u))
d3 = sp.simplify(sp.diff(F3, u) - f(u).diff(u) / sp.sqrt(f(u)))
if d3 != 0:
    FAIL.append(f"5.4-3: diff={d3}")

if FAIL:
    print("chap5: FAIL")
    for item in FAIL:
        print("  -", item)
    sys.exit(1)
print("chap5: all checks passed")
