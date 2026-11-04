"""
《微积分》题库第 3 章解答验算脚本（配套 Calculus/source/chap3.rst）。

Requirements:
    - sympy

Usage:

    ```bash
    python scripts/verify_calculus_chap3.py
    ```

    退出码 0 表示全部通过。求导类答案用 sympy.diff 逐项验证；隐函数/参数方程求导用
    "残差在曲线上为零"的方式验证（隐函数检查 F_x + F_y * y' = 0，或沿曲线参数化作数值比对）。

"""

import sys

import sympy as sp

x = sp.Symbol("x", real=True)
t = sp.Symbol("t", real=True)
tt = sp.Symbol("tt", positive=True)
a = sp.Symbol("a", positive=True)
b = sp.Symbol("b", positive=True)
pi = sp.pi
yy = sp.Function("yy")(x)

FAIL = []


def chk(name, got, want):
    if sp.simplify(got - want) != 0:
        FAIL.append(f"{name}: diff={sp.simplify(got - want)}")


def chk_true(name, cond):
    if not cond:
        FAIL.append(name)


def implicit_ok(F, yp):
    """验证 y' = yp 是 F(x, y)=0 确定的隐函数的导数: dF/dx 代入 y' = yp 后恒为零."""
    return sp.simplify(sp.diff(F, x).subs(sp.Derivative(yy, x), yp)) == 0


# ---- 3.1 题10: 三角形面积 -> a = 64 ----
# 切线 y = a^{-1/2} - (x - a)/(2 a^{3/2}): 横截距 3a, 纵截距 3/(2 sqrt(a))
line = (x - a) / (2 * a ** sp.Rational(3, 2))
chk_true("3.1-10 横截距 3a", sp.solve(sp.Eq(a ** -sp.Rational(1, 2) - line, 0), x) == [3 * a])
chk("3.1-10 面积公式", sp.Rational(9, 4) * sp.sqrt(sp.Integer(64)), sp.Integer(18))

# ---- 3.1 题11: f' = 2x sin(1/x) - cos(1/x) ----
chk("3.1-11", sp.diff(x**2 * sp.sin(1 / x), x), 2 * x * sp.sin(1 / x) - sp.cos(1 / x))

# ---- 3.2 题2: 隐函数 y'|_{x=0} = 1 ----
chk_true("3.2-2", implicit_ok(yy * sp.sin(x) + sp.exp(yy) - x - 1, (1 - yy * sp.cos(x)) / (sp.sin(x) + sp.exp(yy))))

# ---- 3.2 题3: y' = -y^2/(xy+1) ----
chk_true("3.2-3", implicit_ok(x * yy + sp.log(yy) - 1, -(yy**2) / (x * yy + 1)))

# ---- 3.2 题4: 参数方程求导 ----
chk("3.2-4(1)", sp.diff(sp.sin(t) ** 4, t) / sp.diff(sp.cos(t) ** 4, t), -sp.tan(t) ** 2)
chk("3.2-4(2)", sp.diff((1 - t) / (1 + t), t) / sp.diff(t / (1 + t), t), -2)

# ---- 3.2 题8: 四个隐函数导数 ----
chk_true("3.2-8(1)", implicit_ok(yy**2 - 2 * x * yy + 9, yy / (yy - x)))
chk_true("3.2-8(2)", implicit_ok(x**3 + yy**3 - 3 * x * yy, (yy - x**2) / (yy**2 - x)))
# (3) 需代入约束 e^{x+y} = xy 后化简
yp3 = yy * (x - 1) / (x * (1 - yy))
d3 = sp.diff(x * yy - sp.exp(x + yy), x).subs(sp.Derivative(yy, x), yp3).subs(sp.exp(x + yy), x * yy)
chk_true("3.2-8(3)", sp.simplify(d3) == 0)
chk_true("3.2-8(4)", implicit_ok(yy - 1 + x * sp.exp(yy), -sp.exp(yy) / (1 + x * sp.exp(yy))))

# ---- 3.3 题1: 二阶导数 ----
chk("3.3-1(2)", sp.diff(x**2 * sp.sin(x), x, 2), 2 * sp.sin(x) + 4 * x * sp.cos(x) - x**2 * sp.sin(x))
chk("3.3-1(3)", sp.diff(x**2 * sp.exp(x), x, 2), (x**2 + 4 * x + 2) * sp.exp(x))
chk("3.3-1(4)", sp.diff(sp.log(x) / x, x, 2), (2 * sp.log(x) - 3) / x**3)

# ---- 3.3 题3: 莱布尼茨公式 y^(n) = (sqrt 2)^n e^x sin(x + n pi/4), 验 n = 1..4 ----
yf = sp.exp(x) * sp.sin(x)
chk_true(
    "3.3-3 莱布尼茨",
    all(sp.simplify(sp.diff(yf, x, k) - sp.sqrt(2) ** k * sp.exp(x) * sp.sin(x + k * pi / 4)) == 0 for k in range(1, 5)),
)

# ---- 3.3 题4(1): y'' = 2/(2+cos y) + 4x^2 sin y/(2+cos y)^3 (链式代入 yy'=yp) ----
yp1 = 2 * x / (2 + sp.cos(yy))
ypp1 = 2 / (2 + sp.cos(yy)) + 4 * x**2 * sp.sin(yy) / (2 + sp.cos(yy)) ** 3
chk_true("3.3-4(1)", sp.simplify(sp.diff(yp1, x).subs(sp.Derivative(yy, x), yp1) - ypp1) == 0)

# ---- 3.3 题4(2): 笛卡尔叶形线, 沿曲线参数化 y = tx 数值验证 ----
xt = 3 * tt / (1 + tt**3)
yt = 3 * tt**2 / (1 + tt**3)
yx_expr = sp.diff(yt, tt) / sp.diff(xt, tt)
formula_yx = (yt - xt**2) / (yt**2 - xt)
formula_yxx = -2 * xt * yt / (yt**2 - xt) ** 3
yxx_expr = sp.diff(yx_expr, tt) / sp.diff(xt, tt)
for v in [0.5, 2.0]:
    a1 = float(yx_expr.subs(tt, v))
    b1 = float(formula_yx.subs(tt, v))
    c1 = float(yxx_expr.subs(tt, v))
    d1 = float(formula_yxx.subs(tt, v))
    chk_true(f"3.3-4(2) y'(t={v})", abs(a1 - b1) < 1e-9)
    chk_true(f"3.3-4(2) y''(t={v})", abs(c1 - d1) < 1e-9)

# ---- 3.3 题5: 参数方程二阶导 ----
dydx = sp.diff(b * t**3, t) / sp.diff(a * t**2, t)
chk("3.3-5(1)", sp.diff(dydx, t) / (2 * a * t), 3 * b / (4 * a**2 * t))
dydx = sp.diff(sp.sqrt(1 - t), t) / sp.diff(sp.sqrt(1 + t), t)
chk("3.3-5(2)", sp.diff(dydx, t) / sp.diff(sp.sqrt(1 + t), t), -2 / (1 - t) ** sp.Rational(3, 2))
dydx = sp.diff(sp.cos(t), t) / sp.diff(sp.sin(t), t)
chk("3.3-5(3)", sp.diff(dydx, t) / sp.cos(t), -1 / sp.cos(t) ** 3)

# ---- 3.4 题1(2): dy = -dx/(2 sqrt(x(1-x))) (数值取样) ----
f34 = sp.diff(sp.asin(sp.sqrt(1 - x)), x) + 1 / (2 * sp.sqrt(x * (1 - x)))
chk_true("3.4-1(2)", all(abs(float(f34.subs(x, v))) < 1e-9 for v in [0.13, 0.5, 0.87]))

# ---- 总习题2: 左右导数均为 1 ----
chk("总2 左导数", sp.limit((x + sp.sin(x**2)) / x, x, 0, dir="-"), 1)
chk("总2 右导数", sp.limit(sp.log(1 + x) / x, x, 0, dir="+"), 1)

# ---- 总习题7(2): y'' = -x/(1+x^2)^{3/2} ----
chk("总7(2)", sp.diff(sp.log(x + sp.sqrt(1 + x**2)), x, 2), -x / (1 + x**2) ** sp.Rational(3, 2))

# ---- 总习题8(2): (ln x / x)^(n) 公式, 验 n = 1..4 ----
yf = sp.log(x) / x
chk_true(
    "总8(2) n 阶导公式",
    all(
        sp.simplify(
            sp.diff(yf, x, k)
            - (-1) ** (k - 1) * sp.factorial(k) / x ** (k + 1) * (sum(sp.Rational(1, j) for j in range(1, k + 1)) - sp.log(x))
        )
        == 0
        for k in range(1, 5)
    ),
)

# ---- 总习题11: y(1) = -2, y(12/5) = 1/24, y(3) = 0, 驻点 12/5 ----
y11 = (x - 2) * (3 - x) / x**2
chk_true(
    "总11 端值",
    y11.subs(x, 1) == -2 and y11.subs(x, 3) == 0 and sp.simplify(y11.subs(x, sp.Rational(12, 5))) == sp.Rational(1, 24),
)
chk_true("总11 驻点", sp.solve(sp.diff(y11, x), x) == [sp.Rational(12, 5)])

if FAIL:
    print("chap3: FAIL")
    for item in FAIL:
        print("  -", item)
    sys.exit(1)
print("chap3: all checks passed")
