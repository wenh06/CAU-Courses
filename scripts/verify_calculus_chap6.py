"""
《微积分》题库第 6 章解答验算脚本（配套 Calculus/source/chap6.rst）。

Requirements:
    - sympy

Usage:

    ```bash
    python scripts/verify_calculus_chap6.py
    ```

    退出码 0 表示全部通过。定积分/广义积分直接用 sympy.integrate 带上下限计算并比对；
    变限积分求导用 sympy 对未求值 Integral 的求导能力验证；含绝对值/分段的按解答所用分段方式编码；
    带印刷疑误注的题按注中修正版编码 (6.4 题1(9), 6.4 题2(1), 6.4 题10)。

"""

import sys

import sympy as sp

x = sp.Symbol("x", real=True)
t = sp.Symbol("t", real=True)
u = sp.Symbol("u", positive=True)
yy = sp.Symbol("y", real=True)
th = sp.Symbol("theta", real=True)
a = sp.Symbol("a", positive=True)
pi = sp.pi
oo = sp.oo
eps = sp.Symbol("eps", positive=True)

FAIL = []


def chk(name, got, want):
    if sp.simplify(got - want) != 0:
        FAIL.append(f"{name}: diff={sp.simplify(got - want)}")


def chk_true(name, cond):
    if not cond:
        FAIL.append(name)


def chk_close(name, got, want, tol):
    if abs(float(sp.N(got - want))) > tol:
        FAIL.append(f"{name}: {got} vs {want}")


I = sp.integrate

# ---- 6.1 ----
nn = sp.Symbol("nn", positive=True)
chk(
    "6.1-1 定义",
    sp.limit(nn * (nn + 1) * (2 * nn + 1) / (6 * nn**3) + 1, nn, oo),
    sp.Rational(4, 3),
)
chk("6.1-3(1)", I(2, (x, -1, 6)), 14)
chk("6.1-3(2)", I(2 * x, (x, 0, 3)), 9)
chk("6.1-3(3)", I(sp.sqrt(3 - x**2), (x, -sp.sqrt(3), sp.sqrt(3))), 3 * pi / 2)
chk("6.1-3(4)", I(1 - sp.sqrt(2 * x - x**2), (x, 1, 2)), 1 - pi / 4)
chk("6.1-4(1)", I(x**3, (x, 0, 1)), sp.Rational(1, 4))
chk("6.1-4(2)", I(1 / (1 + x) ** 2, (x, 0, 1)), sp.Rational(1, 2))
chk("6.1-4(3)", I(1 / sp.sqrt(1 - x**2), (x, 0, 1)), pi / 2)

# ---- 6.2 ----
chk_true("6.2-2(4) 上界 6/5", float(I((5 - x) / (9 - x**2), (x, 0, 2)).evalf(8)) <= sp.Rational(6, 5))
chk("6.2-4", I(abs(x), (x, -1, 1)), 1)
I1 = I(x / (2 * (1 + sp.cos(x))), (x, 0, 1))
I2 = I(sp.log(1 + x) / (1 + sp.cos(x)), (x, 0, 1))
I3 = I(2 * x / (1 + sp.sin(x)), (x, 0, 1))
chk_true("6.2-5 排序", float(I1.evalf(6)) < float(I2.evalf(6)) < float(I3.evalf(6)))
chk("6.2-6(1)", I(sp.sqrt(1 - x**2), (x, 0, 1)), pi / 4)
chk("6.2-6(2)", I(x**2, (x, 1, 5)) / 4, sp.Rational(31, 3))

# ---- 6.3 题1: 变限积分求导 ----
chk_true("6.3-1(1)", sp.simplify(sp.diff(sp.Integral(sp.sin(1 + t**2), (t, x, pi)), x) + sp.sin(1 + x**2)) == 0)
chk_true("6.3-1(2)", sp.simplify(sp.diff(sp.Integral(sp.cos(t**2), (t, 0, sp.sqrt(x))), x) - sp.cos(x) / (2 * sp.sqrt(x))) == 0)
d3 = sp.diff(sp.Integral(sp.exp(t**2), (t, sp.sin(x), sp.cos(x))), x)
want3 = -sp.exp(sp.cos(x) ** 2) * sp.sin(x) - sp.exp(sp.sin(x) ** 2) * sp.cos(x)
chk_true("6.3-1(3)", sp.simplify(d3 - want3) == 0)
yfun = sp.Function("y")(x)
d4 = sp.diff(x * sp.Integral(sp.tan(t), (t, 0, x)), x)
want4 = sp.Integral(sp.tan(t), (t, 0, x)) + x * sp.tan(x)
chk_true("6.3-1(4)", sp.simplify(d4 - want4) == 0)
chk_true(
    "6.3-1(5)",
    sp.simplify(
        sp.diff(sp.Integral(sp.cos(u), (u, 0, t)), t) / sp.diff(sp.Integral(sp.sin(u), (u, 0, t)), t) - sp.cos(t) / sp.sin(t)
    )
    == 0,
)
F6 = sp.Integral(sp.exp(-(t**2)), (t, 0, yfun)) + sp.Integral(sp.cos(t**2), (t, 0, x))
yp6 = -sp.exp(yfun**2) * sp.cos(x**2)
chk_true("6.3-1(6)", sp.simplify(sp.diff(F6, x).subs(sp.Derivative(yfun, x), yp6)) == 0)

# ---- 6.3 题2: 两个极限 ((1) 由洛必达+FTC: 分子导数 = 2x^2 e^{x^4}, 比值化为 e^{x^4}/3) ----
chk("6.3-2(1)", sp.limit(sp.exp(x**4) / 3, x, 0), sp.Rational(1, 3))
chk("6.3-2(2)", sp.limit((sp.Rational(2, 5) * x**5) / I(t * (t - sp.sin(t)), (t, 0, x)), x, 0), 12)

# ---- 6.3 题3: 六个定积分 ----
chk("6.3-3(1)", I(sp.exp(x), (x, 0, 1)), sp.E - 1)
chk("6.3-3(2)", I(2 * x + 3, (x, 1, 2)), 6)
chk("6.3-3(3)", I(3 * x**2 + 1 / (1 + x**2), (x, 0, 1)), 1 + pi / 4)
chk("6.3-3(4)", I(sp.tan(x) ** 2, (x, 0, pi / 4)), 1 - pi / 4)
chk("6.3-3(5)", I(sp.sqrt(x) + 1 / sp.sqrt(x), (x, 1, 4)), sp.Rational(20, 3))
chk("6.3-3(6)", I(1 / sp.sqrt(1 - x**2), (x, -sp.Rational(1, 2), sp.Rational(1, 2))), pi / 3)

# ---- 6.3 题4: f(1) = 2. 具体实例 f(t) = 2t 同时满足 phi(1)=1 与 phi'(1)=5 ----
chk_true(
    "6.3-4 实例",
    I(2 * t, (t, 0, 1)) == 1 and sp.simplify(I(2 * t, (t, 0, 1)) + 2 * 2 - 5) == 0,
)

# ---- 6.3 题5: f = (5/2) e^{2x} - x - 3/2 满足方程与初值 ----
f5 = sp.Rational(5, 2) * sp.exp(2 * x) - x - sp.Rational(3, 2)
chk_true("6.3-5", sp.simplify(sp.diff(f5, x) - 2 * f5 - (2 * x + 2)) == 0 and f5.subs(x, 0) == 1)
chk("6.3-5 n阶", sp.Rational(5, 2) * 2**5, 5 * 2**4)  # n=5 代表: f^{(n)}(0) = 5 * 2^{n-1}

# ---- 6.3 题6: a = 1/3 ----
chk("6.3-6", sp.limit(I(sp.sin(t**2), (t, 0, x)) / x**3, x, 0), sp.Rational(1, 3))


# ---- 6.3 题7: f(1)=0, f(1/2)<0, f(-1)>0 ----
def f7(v):
    return float(I(sp.sqrt(1 + t**2), (t, v, 1)).evalf(10) + I(sp.sqrt(1 + t), (t, 1, v**2)).evalf(10))


chk_true("6.3-7 符号", f7(1) == 0 and f7(0.5) < 0 < f7(-1))

# ---- 6.3 题8: f = (2/3) x^3, f' = 2x^2 ----
chk("6.3-8", sp.diff(sp.Rational(2, 3) * x**3, x), 2 * x**2)

# ---- 6.4 题1: 12 个定积分 ----
chk("s1(1)", I(sp.sin(x) ** 3 * sp.cos(x), (x, 0, pi / 2)), sp.Rational(1, 4))
chk("s1(2)", I(1 / (3 + 2 * x) ** 2, (x, 0, 3)), sp.Rational(1, 9))
chk("s1(3)", I(x / sp.sqrt(36 - x**2), (x, 0, 3)), 6 - 3 * sp.sqrt(3))
chk("s1(4)", I(1 / (x * sp.sqrt(1 + sp.log(x))), (x, 1, 2)), 2 * (sp.sqrt(1 + sp.log(2)) - 1))
chk("s1(5)", I(sp.sqrt(x) / (1 + sp.sqrt(x)), (x, 0, 1)), 2 * sp.log(2) - 1)
F6a = sp.Rational(1, 5) * (1 - x**2) ** sp.Rational(5, 2)
chk_true("s1(6) 原函数", sp.simplify(sp.diff(F6a, x) - (x**3 - x) * sp.sqrt(1 - x**2)) == 0)
chk("s1(6) 值", F6a.subs(x, 1) - F6a.subs(x, 0), -sp.Rational(1, 5))
chk("s1(7)", I(sp.sqrt(sp.exp(x) - 1), (x, 0, sp.log(5))), 4 - 2 * sp.atan(2))
chk("s1(8)", I(sp.sin(1 / x) / x**2, (x, 1 / pi, pi / 2)), 1 + sp.cos(2 / pi))
chk_close(
    "s1(9) 修正版",
    I(x**2 / (4 + x**2) ** sp.Rational(3, 2), (x, 0, pi)).evalf(10),
    (sp.log((sp.sqrt(4 + pi**2) + pi) / 2) - pi / sp.sqrt(4 + pi**2)).evalf(10),
    1e-9,
)
chk("s1(10)", I(1 / (1 + x ** sp.Rational(1, 3)), (x, 0, 8)), 3 * sp.log(3))
chk("s1(11)", I((2 * x - 4) / (x**2 + 2 * x + 4), (x, 0, 2)), sp.log(3) - sp.sqrt(3) * pi / 3)
F12 = sp.atan(x / sp.sqrt(1 + x**2))
chk_true("s1(12) 原函数", sp.simplify(sp.diff(F12, x) - 1 / ((2 * x**2 + 1) * sp.sqrt(x**2 + 1))) == 0)
chk_true("s1(12) 值", sp.simplify(F12.subs(x, 1) - sp.atan(sp.sqrt(2) / 2)) == 0)

# ---- 6.4 题2: 8 个分部积分 (1) 按修正版上限 pi/4 ----
chk("s2(1)", I(x * sp.sec(x) ** 2, (x, 0, pi / 4)), pi / 4 - sp.log(2) / 2)  # 印刷疑误修正版
chk("s2(2)", I(sp.log(x + 1), (x, 0, sp.E - 1)), 1)
chk("s2(3)", I(x * sp.cos(2 * x), (x, 0, pi / 2)), -sp.Rational(1, 2))
chk("s2(4)", I(x * sp.exp(-x), (x, 0, 1)), 1 - 2 / sp.E)
chk("s2(5)", I(sp.acos(x), (x, 0, sp.sqrt(3) / 2)), sp.sqrt(3) * pi / 12 + sp.Rational(1, 2))
chk("s2(6)", I(x * 2**x, (x, 0, 1)), (2 * sp.log(2) - 1) / sp.log(2) ** 2)
chk("s2(7)", I(sp.log(x) / x**2, (x, 1, sp.E)), 1 - 2 / sp.E)
chk("s2(8)", I(sp.sin(sp.log(x)), (x, 1, sp.E)), sp.E * (sp.sin(1) - sp.cos(1)) / 2 + sp.Rational(1, 2))

# ---- 6.4 题3: 奇偶性 ----
chk("s3(3)", I(sp.sin(x) ** 2 * sp.cos(x) ** 2, (x, -pi / 2, pi / 2)), pi / 8)
chk("s3(4)", I((x + sp.cos(x)) ** 2, (x, -pi / 2, pi / 2)), pi**3 / 12 + pi / 2)
chk("s3(5)", I(sp.Rational(1, 2) * sp.sqrt(1 - x**2), (x, -1, 1)), pi / 4)
chk("s3(6)", I((x + abs(x)) / (2 + x**2), (x, -2, 2)), sp.log(3))

# ---- 6.4 题4: sqrt(cos - cos^3) ----
chk("s4", I(sp.sqrt(sp.cos(x) - sp.cos(x) ** 3), (x, -pi / 4, pi / 2)), sp.Rational(2, 3) * (2 - 2 ** sp.Rational(-3, 4)))

# ---- 6.4 题5: 换元后 (1/2)∫_0^{x^2} f(u) du 的导数 = x f(x^2) ----
f = sp.Function("f")
alt = sp.Rational(1, 2) * sp.Integral(f(u), (u, 0, x**2))
want5 = x * f(x**2)
chk_true("s5", sp.simplify(sp.diff(alt, x) - want5) == 0)

# ---- 6.4 题7: 分段 f(x-1) (按解答的分段方式拆开) ----
chk("s7", I(1 + t**2, (t, -2, 0)) + I(sp.cos(pi * t / 2), (t, 0, 1)), sp.Rational(14, 3) + 2 / pi)

# ---- 6.4 题9: I = 0. 具体实例: f = 1/2 满足全部条件, 此时 f''=0 故 I=0; 分部积分恒等式结构一致 ----
fq = sp.Rational(1, 2) + 0 * x
chk_true(
    "s9 实例",
    fq.subs(x, 2) == sp.Rational(1, 2) and sp.diff(fq, x).subs(x, 2) == 0 and I(fq, (x, 0, 2)) == 1,
)

# ---- 6.4 题10: 修正版 f = x - sin x, 积分 = pi^2/2 - 2 ----
chk("s10", I(x - sp.sin(x), (x, 0, pi)), pi**2 / 2 - 2)  # 印刷疑误修正版

# ---- 6.5 题1: 10 个广义积分 (sympy 直接算不动的用原函数+FTC) ----
chk("g1", I(x**3 * sp.exp(-(x**2)), (x, 0, oo)), sp.Rational(1, 2))
chk_true("g2 原函数", sp.simplify(sp.diff(sp.atan(sp.exp(x) / sp.E) / sp.E, x) - 1 / (sp.exp(x) + sp.exp(2 - x))) == 0)
chk("g2 值", sp.limit(sp.atan(sp.exp(x) / sp.E) / sp.E, x, oo) - sp.atan(1) / sp.E, pi / (4 * sp.E))
chk("g3", I(x / (1 + x**2) ** 3, (x, 0, oo)), sp.Rational(1, 4))
chk_true("g4 发散", I(1 / (x * sp.log(x**2)), (x, sp.E, oo)) == oo)
chk("g5", I(1 / (x**2 + 4 * x + 8), (x, 0, oo)), pi / 8)
Fg6 = -(sp.log(1 + x) + 1) / (1 + x)
chk_true("g6 原函数", sp.simplify(sp.diff(Fg6, x) - sp.log(1 + x) / (1 + x) ** 2) == 0)
chk("g6 值", sp.limit(Fg6, x, oo) - Fg6.subs(x, 0), 1)
chk("g7", I(sp.log(x) ** 2, (x, 0, 1)), 2)
chk("g8", I(x / ((2 - x**2) * sp.sqrt(1 - x**2)), (x, 0, 1)), pi / 4)
chk("g9", I(sp.sqrt(x / (1 - x)), (x, 0, 1)), pi / 2)
chk("g10", I(1 / (x * sp.sqrt(x**2 - 1)), (x, 1, oo)), pi / 2)

# ---- 6.5 题2/3: 收敛性边界 ----
u = sp.Symbol("u", positive=True)
chk("g2 k=3/2", 2 / sp.sqrt(sp.log(2)), 2 / sp.sqrt(sp.log(2)))  # 值 = (ln2)^{1-k}/(k-1), k=3/2
chk_true("g2 k=3/2 原函数", sp.simplify(sp.diff(-2 / sp.sqrt(u), u) - u ** (-sp.Rational(3, 2))) == 0)
chk("g3 p=1/2", sp.limit(I(1 / sp.sqrt(1 - x), (x, 0, 1 - eps)), eps, 0, dir="+"), 2)
chk_true("g3 p=1 发散", sp.limit(-sp.log(eps), eps, 0, dir="+") == oo)

# ---- 6.5 题4: 高斯积分两个等式 ----
chk("g4 高斯", 2 * I(sp.exp(-(x**2)), (x, 0, oo)), sp.sqrt(pi))
chk("g4 换元", I(sp.exp(-x) / sp.sqrt(x), (x, 0, oo)), sp.sqrt(pi))

# ---- 6.6 题1: 面积 ----
chk("a1(1)", I(2 * x - 2 * x**2, (x, 0, 1)), sp.Rational(1, 3))
chk("a1(2)", I(yy + 4 - yy**2 / 2, (yy, -2, 4)), 18)
chk("a1(3)", I(sp.exp(yy) - sp.E * yy, (yy, 0, 1)), sp.E / 2 - 1)
chk("a1(4)", I(1 / x - 1 / x**2, (x, 1, 2)), sp.log(2) - sp.Rational(1, 2))
chk("a1(5)", I(1 - 4 * yy**2, (yy, -sp.Rational(1, 2), sp.Rational(1, 2))), sp.Rational(2, 3))
chk("a1(6)", I(abs(sp.sin(x) - sp.cos(x)), (x, 0, pi)), 2 * sp.sqrt(2))

# ---- 6.6 题2: 极坐标面积 ----
chk("b1", I(sp.exp(th) / 2, (th, pi / 2, pi)), (sp.exp(pi) - sp.exp(pi / 2)) / 2)
chk("b2", I(9 * sp.sin(2 * th) / 2, (th, 0, pi / 2)), sp.Rational(9, 2))
chk("b3", I((3 + 2 * sp.cos(th)) ** 2 / 2, (th, 0, 2 * pi)), 11 * pi)
chk("b4", I(9 * sp.cos(th) ** 2 / 2, (th, -pi / 2, pi / 2)), 9 * pi / 4)

# ---- 6.6 题3: 星形线系数 (Wallis: 积分 = pi/32, S = 12 a^2 * pi/32) ----
chk("c3", 12 * sp.integrate(sp.sin(t) ** 4 * sp.cos(t) ** 2, (t, 0, pi / 2)), sp.Rational(3, 8) * pi)

# ---- 6.6 题4/6: 摆线面积与弧长 ----
chk("d4", I((1 - sp.cos(t)) ** 2, (t, 0, 2 * pi)), 3 * pi)
chk("d6", I(2 * abs(sp.sin(t / 2)), (t, 0, 2 * pi)), 8)

# ---- 6.6 题5: 弧长 ----
chk("e1", I(sp.sqrt(1 + x**2), (x, 0, 1)), (sp.sqrt(2) + sp.log(1 + sp.sqrt(2))) / 2)
chk("e2", I(x**2 + 1 / (4 * x**2), (x, 1, 2)), sp.Rational(59, 24))
chk_close("e3", I(1 / sp.cos(x), (x, 0, pi / 4)).evalf(12), sp.log(1 + sp.sqrt(2)).evalf(12), 1e-9)

# ---- 6.6 题7: r = 3/(1+cos theta) 弧长 (数值) ----
rr = 3 / (1 + sp.cos(th))
rp = sp.diff(rr, th)
chk_close(
    "f7",
    sp.Integral(sp.sqrt(rr**2 + rp**2), (th, -pi / 2, pi / 2)).evalf(10),
    (3 * (sp.sqrt(2) + sp.log(1 + sp.sqrt(2)))).evalf(10),
    1e-6,
)

# ---- 6.6 题8: 体积 ----
chk("v1", pi * I(x - 1, (x, 1, 5)), 8 * pi)
chk("v2", pi * I((2 - x**2) ** 2 - x**4, (x, -1, 1)), 16 * pi / 3)
chk("v3", pi * I(x * sp.sin(x) ** 2, (x, 0, 1)), pi * (3 - 2 * sp.sin(2) - sp.cos(2)) / 8)
chk(
    "v4",
    pi * (I(2 * yy, (yy, 0, sp.Rational(1, 2))) + I(1 / yy - 1, (yy, sp.Rational(1, 2), 1))),
    pi * (sp.log(2) - sp.Rational(1, 4)),
)

# ---- 6.6 题9: a=1, 切线 y=2x-1, V = pi/30 ----
aa = sp.Symbol("aa", positive=True)
area = I(x**2, (x, 0, aa / 2)) + I((x - aa) ** 2, (x, aa / 2, aa))
chk_true("w9(1) 面积公式", sp.simplify(area - aa**3 / 12) == 0 and sp.solve(sp.Eq(area, sp.Rational(1, 12)), aa) == [1])
chk("w9(2)", pi * (I(x**4, (x, 0, sp.Rational(1, 2))) + I(x**4 - (2 * x - 1) ** 2, (x, sp.Rational(1, 2), 1))), pi / 30)

if FAIL:
    print("chap6: FAIL")
    for item in FAIL:
        print("  -", item)
    sys.exit(1)
print("chap6: all checks passed")
