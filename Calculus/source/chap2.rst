第二章  导数与微分
^^^^^^^^^^^^^^^^^^^^^^^^^

..  contents:: :local:


课后习题解答
=================

§2.1 函数的导数
--------------------------------

2. 设 :math:`f(x) = ax^2 + bx + c`, 用定义求 :math:`f'(x)`.

.. proof:solution::

    .. math::

        f'(x) &= \lim_{\Delta x \to 0} \frac{f(x + \Delta x) - f(x)}{\Delta x} \\
              &= \lim_{\Delta x \to 0} \frac{a(x + \Delta x)^2 + b(x + \Delta x) + c - (ax^2 + bx + c)}{\Delta x} \\
              &= \lim_{\Delta x \to 0} \frac{a(x^2 + 2x\Delta x + \Delta x^2) + bx + b\Delta x + c - ax^2 - bx - c}{\Delta x} \\
              &= \lim_{\Delta x \to 0} \frac{2ax\Delta x + a\Delta x^2 + b\Delta x}{\Delta x} \\
              &= \lim_{\Delta x \to 0} 2ax + a\Delta x + b \\
              &= 2ax + b

4. 求曲线 :math:`y = 2^x` 在点 :math:`(1, 2)` 处的切线方程和法线方程.

.. proof:solution::

    :math:`y = 2^x` 的导函数为 :math:`y' = 2^x \ln 2`, 所以在点 :math:`(1, 2)` 处切线斜率，即该点处的导数值为 :math:`y'|_{x=1} = 2 \ln 2`.
    所以切线方程为 :math:`y - 2 = 2 \ln 2 (x - 1)`, 即 :math:`y = 2 \ln 2 x - 2 \ln 2 + 2`.

    法线的斜率为 :math:`-\frac{1}{2 \ln 2}`, 所以法线方程为 :math:`y - 2 = -\frac{1}{2 \ln 2} (x - 1)`, 即 :math:`y = -\frac{1}{2 \ln 2} x + \frac{1}{2 \ln 2} + 2`.

5. 函数 :math:`f(x) = \begin{cases} a \sin x, & x \le 0 \\ e^x + b, & x > 0 \end{cases}` 可导, 求 :math:`a, b`.

.. proof:solution::

    :math:`f(x)` 在 :math:`x = 0` 处可导, 所以 :math:`f(x)` 在 :math:`x = 0` 处连续, 即 :math:`a \sin 0 = e^0 + b`, 解得 :math:`b = -1`.

    :math:`f'_{-}(0) = a \cos 0 = a`, :math:`f'_{+}(0) = e^0 = 1`, 所以 :math:`a = 1`.

6. 已知函数可导，将下列极限用导数表示出来：

(3). 设 :math:`f(0) = 0`, 求 :math:`\lim_{h \to 0} \frac{f(h)}{h}`.

.. proof:solution::

    .. math::

        \lim_{h \to 0} \frac{f(h)}{h} = \lim_{h \to 0} \frac{f(h) - f(0)}{h - 0} = f'(0)

7. 讨论函数在 :math:`x = 0` 处的可导性：

(2). :math:`f(x) = \begin{cases} x^2 \cos \dfrac{1}{x}, & x \ne 0 \\ 0, & x = 0 \end{cases}`.

.. proof:solution::

    首先， :math:`f(x)` 在 :math:`x = 0` 处连续，因为 :math:`\lim_{x \to 0} f(x) = \lim_{x \to 0} x^2 \cos \dfrac{1}{x} = 0 = f(0)`.
    接下来考虑 :math:`f(x)` 在 :math:`x = 0` 处的左右导数是否相等：

    .. math::

        f'_{-}(0) &= \lim_{h \to 0^{-}} \dfrac{f(0 + h) - f(0)}{h} = \lim_{h \to 0^{-}} \dfrac{h^2 \cos \dfrac{1}{h}}{h} \\
                  &= \lim_{h \to 0^{-}} h \cos \dfrac{1}{h} \\
                  &= 0

    .. math::

        f'_{+}(0) &= \lim_{h \to 0^{+}} \dfrac{f(0 + h) - f(0)}{h} = \lim_{h \to 0^{+}} \dfrac{h^2 \cos \dfrac{1}{h}}{h} \\
                  &= \lim_{h \to 0^{+}} h \cos \dfrac{1}{h} \\
                  &= 0

    所以 :math:`f'(0) = 0`, :math:`f(x)` 在 :math:`x = 0` 处可导.

§2.2 函数的求导法则
--------------------------------

1. 求下列函数的导数：

(2). :math:`y = x^5 \left( \dfrac{1}{x} + \sqrt{x} \right)`; (4) :math:`y = (1 + \tan x) \ln x`;

(6). :math:`y = e^x (x^3 - 3x^2 + 6x - 6)`; (8). :math:`y = \dfrac{\cos x}{1 + \ln x}`;

(10). :math:`y = \dfrac{1 + \ln x}{x^2}`; (12). :math:`y = \dfrac{1 - x}{1 + x}`;

(14). :math:`y = \dfrac{2\sec x}{1 + x^2}`.

.. proof:solution::

    (2).

    .. math::

        y' &= 5x^4 \left( \dfrac{1}{x} + \sqrt{x} \right) + x^5 \left( -\dfrac{1}{x^2} + \dfrac{1}{2 \sqrt{x}} \right) \\
           &= 5x^3 + 5x^{9/2} - x^3 + \dfrac{1}{2} x^{9/2} \\
           &= 4x^3 + \dfrac{11}{2} x^{9/2}

    (4).

    .. math::

        y' = \dfrac{1}{\cos^2 x} \ln x + (1 + \tan x) \cdot \dfrac{1}{x}

    (6).

    .. math::

        y' = e^x (x^3 - 3x^2 + 6x - 6) + e^x (3x^2 - 6x + 6) = e^x x^3

    (8).

    .. math::

        y' = \dfrac{-\sin x}{1 + \ln x} - \dfrac{\cos x}{(1 + \ln x)^2} \cdot \dfrac{1}{x} = - \dfrac{\cos x + x \sin x (1 + \ln x)}{x(1 + \ln x)^2}

    (10).

    .. math::

        y' = \dfrac{\dfrac{1}{x} \cdot x^2 - (1 + \ln x) \cdot 2x}{x^4} = \dfrac{1 - 2 - 2 \ln x}{x^3} = - \dfrac{2 \ln x + 1}{x^3}

    (12).

    .. math::

        y' = \dfrac{-1 \cdot (1 + x) - (1 - x) \cdot 1}{(1 + x)^2} = - \dfrac{2}{(1 + x)^2}

    (14).

    .. math::

        y' = \dfrac{2 (\sec x \tan x) \cdot (1 + x^2) - 2 \sec x \cdot 2x}{(1 + x^2)^2} = 2 \sec x \left( \dfrac{(1 + x^2) \tan x - 2x}{(1 + x^2)^2} \right)

2. 求函数在给定点的导数

(1). :math:`y = \sin x + \cos x`, 求 :math:`y'|_{x = \frac{\pi}{4}`;

(3). :math:`y = \dfrac{x + \sqrt{x}}{1 + \sqrt{x}}`,  求 :math:`y'|_{x = 1}`;

(5). 设 :math:`\varphi(x)` 是连续函数， :math:`f(x) = (1 - x^2) \varphi(x)`, 求 :math:`f'(1)`.

.. proof:solution::

    (1). :math:`y' = \cos x - \sin x`, 所以 :math:`y'|_{x = \frac{\pi}{4}} = \cos \frac{\pi}{4} - \sin \frac{\pi}{4} = \frac{\sqrt{2}}{2} - \frac{\sqrt{2}}{2} = 0`.

    (3). :math:`y' = \left( \dfrac{\sqrt{x} (1 + \sqrt{x})}{1 + \sqrt{x}} \right)' = \left( \sqrt{x} \right)' = \dfrac{1}{2 \sqrt{x}}`, 所以 :math:`y'|_{x = 1} = \dfrac{1}{2}`.

    (5). 由于 :math:`\varphi` 只是连续函数，不知道是否可导，所以需要用定义求 :math:`f(x) = (1 - x^2) \varphi(x)` 的导数

    .. math::

        f'(x) & = \lim_{\Delta x \to 0} \dfrac{f(x + \Delta x) - f(x)}{\Delta x} \\
              & = \lim_{\Delta x \to 0} \dfrac{(1 - (x + \Delta x)^2) \varphi(x + \Delta x) - (1 - x^2) \varphi(x)}{\Delta x} \\
              & = \lim_{\Delta x \to 0} \dfrac{(1 - x^2 - 2x \Delta x - \Delta x^2) \varphi(x + \Delta x) - (1 - x^2) \varphi(x)}{\Delta x} \\
              & = \lim_{\Delta x \to 0} \dfrac{(1 - x^2) \varphi(x + \Delta x) - (1 - x^2) \varphi(x) - 2x \Delta x \varphi(x + \Delta x) - \Delta x^2 \varphi(x + \Delta x)}{\Delta x} \\
              & = \lim_{\Delta x \to 0} \dfrac{(1 - x^2) (\varphi(x + \Delta x) - \varphi(x))}{\Delta x} - \lim_{\Delta x \to 0} 2x \varphi(x + \Delta x) - \lim_{\Delta x \to 0} \Delta x \varphi(x + \Delta x) \\
              & = \lim_{\Delta x \to 0} \dfrac{(1 - x^2) (\varphi(x + \Delta x) - \varphi(x))}{\Delta x} - 2x \varphi(x) - 0 \\

    上式代 :math:`x = 1` 有 :math:`f'(1) = \lim\limits_{\Delta x \to 0} 0 - 2 \cdot 1 \cdot \varphi(1) = -2 \varphi(1)`.

3. 求曲线 :math:`y = x - \dfrac{1}{x}` 在与坐标轴交点处的切线方程和法线方程.

.. proof:solution::

    先求曲线与坐标轴交点。由于曲线在 :math:`x = 0` 处无定义，即与 :math:`y` 轴无交点，所以只需求 :math:`x` 轴交点。曲线与 :math:`x` 轴交点为 :math:`x - \dfrac{1}{x} = 0`,
    解得 :math:`x = \pm 1`, 所以曲线与坐标轴交点为 :math:`(-1, 0)` 和 :math:`(1, 0)`.

    曲线 :math:`y = x - \dfrac{1}{x}` 的导函数为 :math:`y' = 1 + \dfrac{1}{x^2}`, 所以在点 :math:`(-1, 0)` 处切线斜率，即该点处的导数值为 :math:`y'|_{x=-1} = 1 + \dfrac{1}{(-1)^2} = 2`，
    所以切线方程为 :math:`y - 0 = 2 (x + 1)`, 即 :math:`y = 2x + 2`; 法线的斜率为 :math:`-\dfrac{1}{2}`, 所以法线方程为 :math:`y - 0 = -\dfrac{1}{2} (x + 1)`, 即 :math:`y = -\dfrac{1}{2} x - \dfrac{1}{2}`. 类似可求得曲线在点 :math:`(1, 0)` 处的切线方程为 :math:`y = 2x - 2`, 法线方程为 :math:`y = -\dfrac{1}{2} x + \dfrac{1}{2}`.

4. 求下列函数的导数：

(2). :math:`y = \sin x^5`; (4). :math:`y = e^{\cos 2x}`;

(6). :math:`y = \sin (nx) \sin^n x`; (8). :math:`y = \arctan \dfrac{1 + x}{1 - x}`.

.. proof:solution::

    (2). :math:`y' = \cos x^5 \cdot 5x^4`.

    (4). :math:`y' = e^{\cos 2x} \cdot (-\sin 2x) \cdot 2 = -2 e^{\cos 2x} \sin 2x`.

    (6).

    .. math::

        y' & = n \cos (nx) \sin^n x + \sin (nx) \cdot n \sin^{n-1} x \cdot \cos x \\
           & = n \sin^{n-1} x (\cos (nx) \sin x + \sin (nx) \cos x) \\
           & = n \sin^{n-1} x \sin (nx + x).

    (8). :math:`y' = \dfrac{1}{1 + \left( \dfrac{1 + x}{1 - x} \right)^2} \cdot \dfrac{(1 - x) + (1 + x)}{(1 - x)^2} = \dfrac{2}{(1 - x)^2 + (1 + x)^2} = \dfrac{1}{1 + x^2}`.

§2.3 高阶导数
--------------------------------

1. 求下列函数的二阶导数：

(2). :math:`y = \ln (x + \sqrt{x^2 + 4})`;

(4). :math:`y = \ln (x^2 + 1)`;

(6). :math:`y = \sin 2x`.

.. proof:solution::

    (2).

    .. math::

        y' & = \dfrac{1}{x + \sqrt{x^2 + 4}} \cdot (1 + \dfrac{1}{2 \sqrt{x^2 + 4}} \cdot 2x) = \dfrac{1}{x + \sqrt{x^2 + 4}} \cdot \dfrac{x + \sqrt{x^2 + 4}}{\sqrt{x^2 + 4}} = \dfrac{1}{\sqrt{x^2 + 4}} \\
        y'' & = -\dfrac{1}{2} (x^2 + 4)^{-3/2} \cdot 2x = -\dfrac{x}{(x^2 + 4)^{3/2}}

    (4).

    .. math::

        y' & = \dfrac{2x}{x^2 + 1} \\
        y'' & = \dfrac{2(x^2 + 1) - 2x \cdot 2x}{(x^2 + 1)^2} = \dfrac{2(1 - x^2)}{(x^2 + 1)^2}

    (6).

    .. math::

        y' & = 2 \cos 2x \\
        y'' & = -4 \sin 2x

2. 若 :math:`f(x)` 的二阶导数存在，求下列函数 :math:`y` 的二阶导数 :math:`\dfrac{\mathrm{d}^2 y}{\mathrm{d} x^2}`:

(2). :math:`y = \ln f(x)`.

.. proof:solution::

    .. math::

        y' & = \dfrac{1}{f(x)} \cdot f'(x) \\
        y'' & = \dfrac{1}{f(x)} \cdot f''(x) - \dfrac{1}{f^2(x)} \cdot (f'(x))^2 = \dfrac{f''(x) f(x) - (f'(x))^2}{f^2(x)}

3. 验证函数关系式：

(2). :math:`y = \dfrac{x - 3}{x - 4}` 满足关系式 :math:`2y'^2 = (y - 1) y''`.

.. proof:proof::

    .. math::

        y' & = \dfrac{(x - 4) - (x - 3)}{(x - 4)^2} = -\dfrac{1}{(x - 4)^2} \\
        y'' & = 2(x - 4)^{-3} = \dfrac{2}{(x - 4)^3}

    所以

    .. math::

        2y'^2 & = 2 \cdot \dfrac{1}{(x - 4)^4} = \dfrac{2}{(x - 4)^4} \\
        (y - 1) y'' & = \dfrac{(x - 3) - (x - 4)}{x - 4} \cdot \dfrac{2}{(x - 4)^3} = \dfrac{2}{(x - 4)^4}

    所以 :math:`2y'^2 = (y - 1) y''`.

4. 求下列函数的高阶导数：

(2). :math:`y = x (e^{x} + e^{-x})`, 求 :math:`y^{(99)}`.

.. proof:solution::

    .. math::

        y' & = e^x + e^{-x} + x (e^x - e^{-x}) \\
        y'' & = e^x - e^{-x} + e^x - e^{-x} + x (e^x + e^{-x}) = 2(e^x - e^{-x}) + x (e^x + e^{-x}) \\
        y^{(3)} & = 2(e^x + e^{-x}) + e^x + e^{-x} + x (e^x - e^{-x}) = 3(e^x + e^{-x}) + x (e^x - e^{-x})

    所以可以猜测 :math:`y^{(n)} = n(e^x + (-1)^{n - 1} e^{-x}) + x (e^x + (-1)^n e^{-x})`, 用数学归纳法证明：

    .. math::

        y^{(n + 1)} & = \dfrac{d \left( n(e^x + (-1)^{n - 1} e^{-x}) + x (e^x + (-1)^n e^{-x}) \right)}{\mathrm{d} x} \\
        & = n(e^x + (-1)^{n} e^{-x}) + (e^x + (-1)^n e^{-x}) + x (e^x + (-1)^{n + 1} e^{-x}) \\
        & = (n + 1)(e^x + (-1)^{n} e^{-x}) + x (e^x + (-1)^{n + 1} e^{-x}) \\
        & = (n + 1)(e^x + (-1)^{(n + 1) - 1} e^{-x}) + x (e^x + (-1)^{n + 1} e^{-x})

    所以 :math:`y^{(n)} = n(e^x + (-1)^{n - 1} e^{-x}) + x (e^x + (-1)^n e^{-x})`. 令 :math:`n = 99` 有

    .. math::

        y^{(99)} = 99(e^x + (-1)^{98} e^{-x}) + x (e^x + (-1)^{99} e^{-x}) = 99(e^x + e^{-x}) + x (e^x - e^{-x}).

§2.4 隐函数与参数方程所确定的函数的导数
------------------------------------------

1. 求下列隐函数所确定的函数的导数：

(1). :math:`x^3 + y^3 - 3xy = 0`;

(3). :math:`e^{x + y} - xy = 1`;

(5). :math:`y = \tan (x + y)`.

.. proof:solution::

    (1). 方程两边对 :math:`x` 求导有 :math:`3 x^2 + 3 y^2 y' - 3 (x y' + y) = 0`, 所以 :math:`y' = \dfrac{y - x^2}{y^2 - x}`.

    (3). 方程两边对 :math:`x` 求导有 :math:`e^{x + y} (1 + y') - y - xy' = 0`, 所以 :math:`y' = \dfrac{y - e^{x + y}}{e^{x + y} - x} = \dfrac{y - xy - 1}{1 + xy -x}`.

    (5). 方程两边对 :math:`x` 求导有 :math:`y' = \dfrac{1}{\cos^2 (x + y)} (1 + y')`, 所以 :math:`y' = \dfrac{1}{\cos^2 (x + y) - 1} = -\dfrac{1}{\sin^2 (x + y)}`.

3. :math:`y = 1 + x e^y`, 求 :math:`y'|_{x = 0}, y''|_{x = 0}`.

.. proof:solution::

    首先将 :math:`x = 0` 代入方程 :math:`y = 1 + x e^y` 得 :math:`y|_{x = 0} = 1`.

    方程 :math:`y = 1 + x e^y` 两边对 :math:`x` 求导有 :math:`y' = e^y + x e^y y'`, 所以 :math:`y' = \dfrac{e^y}{1 - x e^y}`. 所以 :math:`y'|_{x = 0} = e^{1} = e`.

    :math:`y' = \dfrac{e^y}{1 - x e^y} = \dfrac{e^y}{2 - y}` 两边对 :math:`x` 求二阶导有

    .. math::

        y'' & = \dfrac{e^y y' (2 - y) - e^y (-y')}{(2 - y)^2} = \dfrac{e^y y' (2 - y) + e^y y'}{(2 - y)^2} \\
            & = \dfrac{3 e^y y' - y y' e^y}{(2 - y)^2}

    将 :math:`y|_{x = 0} = 1` 和 :math:`y'|_{x = 0} = e` 代入上式得 :math:`y''|_{x = 0} = \dfrac{3 e^2 - e^2}{(1 - 0)^2} = 2 e^2`.

6. 设参数方程为 :math:`\begin{cases} x = e^t \sin t \\ y = e^t \cos t \end{cases}`,

(1). 求曲线在 :math:`t = \dfrac{\pi}{3}` 处的切线方程和法线方程;

(2). 验证函数满足关系式 :math:`\dfrac{d^2 y}{\mathrm{d} x^2} (x + y)^2 = 2 \left( x \dfrac{\mathrm{d} y}{\mathrm{d} x} - y \right)`.

.. proof:solution::

    (1). :math:`\dfrac{\mathrm{d} y}{\mathrm{d} x} = \left. \left( \dfrac{\mathrm{d} y}{\mathrm{d} t} \right) \right/ \left( \dfrac{\mathrm{d} x}{\mathrm{d} t} \right) = \dfrac{e^t \cos t - e^t \sin t}{e^t \sin t + e^t \cos t} = \dfrac{\cos t - \sin t}{\sin t + \cos t}`.
    曲线在 :math:`t = \dfrac{\pi}{3}` 处的切线斜率为 :math:`\left. \dfrac{\mathrm{d} y}{\mathrm{d} x} \right|_{t = \dfrac{\pi}{3}} = \dfrac{\dfrac{1}{2} - \dfrac{\sqrt{3}}{2}}{\dfrac{\sqrt{3}}{2} + \dfrac{1}{2}} = \sqrt{3} - 2`.
    曲线在 :math:`t = \dfrac{\pi}{3}` 处过点 :math:`(e^{\frac{\pi}{3}} \sin \frac{\pi}{3}, e^{\frac{\pi}{3}} \cos \frac{\pi}{3})`,
    所以切线方程为 :math:`y - e^{\frac{\pi}{3}} \cos \frac{\pi}{3} = (\sqrt{3} - 2) (x - e^{\frac{\pi}{3}} \sin \frac{\pi}{3})`,
    即 :math:`y = (\sqrt{3} - 2) x + e^{\frac{\pi}{3}} (\sqrt{3} - 1)`.

    法线斜率为 :math:`-\dfrac{1}{\sqrt{3} - 2}`, 所以法线方程为 :math:`y - e^{\frac{\pi}{3}} \cos \frac{\pi}{3} = -\dfrac{1}{\sqrt{3} - 2} (x - e^{\frac{\pi}{3}} \sin \frac{\pi}{3})`,
    即 :math:`y = (2 + \sqrt{3}) x - e^{\frac{\pi}{3}} (1 + \sqrt{3})`.

    (2). 由于 :math:`\dfrac{\mathrm{d} y}{\mathrm{d} x} = \dfrac{\cos t - \sin t}{\cos t + \sin t}`, 所以

    .. math::

        \dfrac{d^2 y}{\mathrm{d} x^2} & = \dfrac{\dfrac{d}{\mathrm{d} t} \left( \dfrac{\mathrm{d} y}{\mathrm{d} x} \right)}{\dfrac{\mathrm{d} x}{\mathrm{d} t}} = \dfrac{\dfrac{d}{\mathrm{d} t} \left( \dfrac{\cos t - \sin t}{\cos t + \sin t} \right)}{e^t \sin t + e^t \cos t} \\
        & = \dfrac{\left( \dfrac{-(\cos t + \sin t) \cdot (\cos t + \sin t) - (\cos t - \sin t) \cdot (\cos t - \sin t)}{(\cos t + \sin t)^2} \right)}{e^t \sin t + e^t \cos t} \\
        & = \dfrac{-2}{e^t (\sin t + \cos t)^3}.

    所以

    .. math::

        \dfrac{d^2 y}{\mathrm{d} x^2} (x + y)^2 & = \dfrac{-2}{e^t (\sin t + \cos t)^3} \cdot (e^t \sin t + e^t \cos t)^2 = - \dfrac{2 e^t}{\sin t + \cos t} \\
        2 \left( x \dfrac{\mathrm{d} y}{\mathrm{d} x} - y \right) & = 2 \left( e^t \sin t \cdot \dfrac{\cos t - \sin t}{\cos t + \sin t} - e^t \cos t \right) = - \dfrac{2 e^t}{\sin t + \cos t}

    于是有 :math:`\dfrac{d^2 y}{\mathrm{d} x^2} (x + y)^2 = 2 \left( x \dfrac{\mathrm{d} y}{\mathrm{d} x} - y \right)`.

§2.5 函数的微分
--------------------------------

1. 已知 :math:`y = x^2 + 1`, 计算在 :math:`x = 1` 点处当 :math:`\Delta x = 0.1` 和 :math:`0.01` 时的 :math:`\Delta y` 和 :math:`\mathrm{d} y`.

.. proof:solution::

    函数 :math:`y = x^2 + 1` 的微分为 :math:`\mathrm{d} y = 2x \mathrm{d} x`, 所以当 :math:`x = 1` 时 :math:`\mathrm{d} y = 2 \mathrm{d} x`.

    当 :math:`\Delta x = 0.1` 时， :math:`\Delta y = f(1 + 0.1) - f(1) = 2.21 - 2 = 0.21, \mathrm{d} y = 2 \cdot 0.1 = 0.2`.

    当 :math:`\Delta x = 0.01` 时， :math:`\Delta y = f(1 + 0.01) - f(1) = 2.0201 - 2 = 0.0201, \mathrm{d} y = 2 \cdot 0.01 = 0.02`.

2. 求下列函数的微分：

(1). :math:`y = x^2 + \sqrt{x}`;

(3). :math:`y = e^{x^2 + x}`;

(5). :math:`y = \ln (1 + x^2)`;

(7). :math:`y = \arctan \dfrac{1 - x}{1 + x}`;

(9). :math:`x^3 + y^3 -3x^2y - 3y^2x = 4a^2`.

.. proof:solution::

    (1). :math:`\mathrm{d} y = 2x \mathrm{d} x + \dfrac{1}{2 \sqrt{x}} \mathrm{d} x = (2x + \dfrac{1}{2 \sqrt{x}}) \mathrm{d} x`.

    (3). :math:`\mathrm{d} y = (2x + 1) e^{x^2 + x} \mathrm{d} x`.

    (5). :math:`\mathrm{d} y = \dfrac{2x}{1 + x^2} \mathrm{d} x`.

    (7). :math:`\left( \arctan\dfrac{1 - x}{1 + x} \right)' = \dfrac{1}{1 + \left( \dfrac{1 - x}{1 + x} \right)^2} \cdot \dfrac{-(1 + x) - (1 - x)}{(1 + x)^2} = \dfrac{-1}{1 + x^2}`,
    所以 :math:`\mathrm{d} y = \dfrac{1}{1 + x^2} \mathrm{d} x`.

    (9). 对等式两边求微分有 :math:`3x^2 \mathrm{d} x + 3y^2 \mathrm{d} y - 6xy \mathrm{d} x - 3x^2 \mathrm{d} y - 6xy \mathrm{d} y - 3y^2 \mathrm{d} x = 0`,
    所以 :math:`(y^2 - 2xy - x^2) \mathrm{d} y = (2xy - x^2 + y^2) \mathrm{d} x`, 即有 :math:`\mathrm{d} y = \dfrac{y^2 + 2xy - x^2}{y^2 - 2xy + x^2} \mathrm{d} x`.

3. 将适当的函数填入括号中，使得下列等式成立：

(2). :math:`\mathrm{d} (\quad) = \dfrac{1}{x^2} \mathrm{d} x`;

(4). :math:`\mathrm{d} (\quad) = e^{-2x} \mathrm{d} x`;

(6). :math:`\mathrm{d} (\quad) = \dfrac{\arctan x}{x^2 + 1} \mathrm{d} x`.

.. proof:solution::

    (2). 由于 :math:`\left( \dfrac{1}{x} \right)' = -\dfrac{1}{x^2}`, 所以 :math:`\mathrm{d} \left( -\dfrac{1}{x} \right) = \dfrac{1}{x^2} \mathrm{d} x`.

    (4). 由于 :math:`\left( -\dfrac{1}{2} e^{-2x} \right)' = e^{-2x}`, 所以 :math:`\mathrm{d} \left( -\dfrac{1}{2} e^{-2x} \right) = e^{-2x} \mathrm{d} x`.

    (6). 由于 :math:`\left( \arctan^2 x \right)' = \dfrac{\arctan x}{x^2 + 1}`, 所以 :math:`\mathrm{d} \left( \arctan^2 x \right) = \dfrac{\arctan x}{x^2 + 1} \mathrm{d} x`.

    .. note::

        一般地，可以把 :math:`\mathrm{d} x` 变形，将整个表示式变成基本初等函数的微分。例如第 (6) 题：

        .. math::

            \dfrac{\arctan x}{x^2 + 1} \mathrm{d} x & = \arctan x \cdot \dfrac{1}{x^2 + 1} \mathrm{d} x \\
            & = \arctan x \cdot \mathrm{d} (\arctan x) \\
            & = \mathrm{d} (\arctan^2 x)

4. 求下列近似值：

(2). :math:`e^{1.01}`.

.. proof:solution::

    由于 :math:`e^x` 在 :math:`x = 1` 处的导数为 :math:`e^x`, 在 :math:`x = 1` 附近有 :math:`e^{x + \Delta x} \approx e^x + e^x \cdot \Delta x`,
    那么 :math:`e^{1.01} \approx e^1 + e^1 \cdot 0.01 \approx 2.71828 + 2.71828 \cdot 0.01 = 2.74546`.

5. 当 :math:`x` 很小时，证明近似公式：

(2). :math:`\ln (1 + \sin x) \approx x`.

.. proof:solution::

    由于 :math:`\ln (1 + \sin x)` 在 :math:`x = 0` 处的值为 :math:`0`, 导数为 :math:`\left.\dfrac{\cos x}{1 + \sin x}\right|_{x = 0} = 1`,
    所以在 :math:`x = 0` 附近有 :math:`\ln (1 + \sin x) \approx 0 + 1 \cdot x = x`.

7. 已知单摆的运动规律为 :math:`y = 2\pi \sqrt{\dfrac{x}{g}}`, 其中 :math:`y` 是运动周期，:math:`g` 为重力加速度，:math:`x` 为摆长。如果摆长增加 :math:`1\%`, 单摆的运动周期约增加多少？

.. proof:solution::

    单摆运动周期 :math:`y = 2\pi \sqrt{\dfrac{x}{g}}` 关于摆长 :math:`x` 的导数为 :math:`\dfrac{\pi}{\sqrt{g x}}`, 那么当摆长增加 :math:`1\%` 时，单摆的运动周期增加约
    :math:`\dfrac{\pi}{\sqrt{g x}} \cdot 0.01 x = \pi \sqrt{\dfrac{x}{g}} \cdot 0.01 = \dfrac{y}{2} \cdot 0.01 = y \cdot 0.005`, 所以单摆的运动周期约 :math:`0.5\%`.

§2.6 微分中值定理
--------------------------------

1. 验证函数 :math:`f(x) = x \sqrt{1 - x^2}` 在 :math:`[-1, 1]` 满足罗尔定理。

3. 设 :math:`f(x)` 在 :math:`[a, b]` 连续可微，在 :math:`(a, b)` 二阶可微，且 :math:`f(a) = f(b) = f'(a) = 0`, 证明 :math:`f''(x) = 0` 在 :math:`(a, b)` 内至少有一个根。

4. 已知 :math:`c_0 + \dfrac{c_1}{2} + \cdots + \dfrac{c_n}{n + 1} = 0`, 证明 :math:`p(x) = c_0 + c_1 x + \cdots + c_n x^n = 0` 至少有一正实根。

6. 求证 :math:`\arcsin x + \arccos x \equiv \dfrac{\pi}{2} (\lvert x \rvert \le 1)`.

7. 证明：当 :math:`a > b > 0` 时， :math:`\dfrac{a - b}{a} < \ln \dfrac{a}{b} < \dfrac{a - b}{b}`.

9. 设函数 :math:`f(x)` 在区间 :math:`[a, b]` 上连续，在 :math:`(a, b)` 内可导，且有 :math:`f(a) = f(b) = 0`. 利用 :math:`g(x) = e^{-x} f(x)` 证明存在 :math:`\xi \in (a, b)` 使得 :math:`f(\xi) - f'(\xi) = 0`.

10. 求证：设 :math:`f(x)` 在 :math:`[a, b] (b > a > 0)` 上连续，在 :math:`(a, b)` 内可导，则存在 :math:`\xi \in (a, b)` 使得

.. math::

    f(b) - f(a) = \xi f'(\xi) \ln \dfrac{b}{a}.

§2.7 洛必达法则
--------------------------------

待写

§2.8 泰勒公式
--------------------------------

待写

§2.9 函数的单调性与曲线的凹凸性
--------------------------------

待写

§2.10 函数的极值与最大值最小值
--------------------------------

待写

§2.11 函数作图
--------------------------------

待写

补充内容
=================

§2.6 高阶导数
--------------------------------

莱布尼茨公式 :math:`(uv)^{(n)} = \sum\limits_{k=0}^n C_n^k u^{(k)} v^{(n-k)}` 的证明：

.. proof:proof::

    用数学归纳法证明。当 :math:`n = 1` 时， :math:`(uv)' = u'v + uv'`, 成立。

    假设当 :math:`n = k` 时， :math:`(uv)^{(k)} = \sum\limits_{i=0}^k C_k^i u^{(i)} v^{(k-i)}` 成立，那么 :math:`n = k + 1` 时有

    .. math::

        (uv)^{(k + 1)} & = \dfrac{\mathrm{d}}{\mathrm{d} x} \left( \sum\limits_{i=0}^k C_k^i u^{(i)} v^{(k-i)} \right) \\
                       & = \sum\limits_{i=0}^k C_k^i \dfrac{\mathrm{d}}{\mathrm{d} x} \left( u^{(i)} v^{(k-i)} \right) \\
                       & = \sum\limits_{i=0}^k C_k^i \left( u^{(i+1)} v^{(k-i)} + u^{(i)} v^{(k-i+1)} \right) \\
                       & = \sum\limits_{i=0}^k C_k^i u^{(i+1)} v^{(k-i)} + \sum\limits_{i=0}^k C_k^i u^{(i)} v^{(k-i+1)} \\
                       & = \sum\limits_{i=1}^{k+1} C_k^{i-1} u^{(i)} v^{(k-i+1)} + \sum\limits_{i=0}^k C_k^i u^{(i)} v^{(k-i+1)} \\
                       & = u^{(k+1)} v + \sum\limits_{i=1}^k \left( C_k^{i-1} + C_k^i \right) u^{(i)} v^{(k-i+1)} + u v^{(k+1)} \\
                       & = u^{(k+1)} v + \sum\limits_{i=1}^k C_{k+1}^i u^{(i)} v^{(k-i+1)} + u v^{(k+1)} \\
                       & = C_{k+1}^{k+1} u^{(k+1)} v + \sum\limits_{i=0}^k C_{k+1}^i u^{(i)} v^{(k-i+1)} + C_{k+1}^0 u v^{(k+1)} \\
                       & = \sum\limits_{i=0}^{k+1} C_{k+1}^i u^{(i)} v^{((k+1)-i)}

    于是当 :math:`n = k + 1` 时， :math:`(uv)^{(n)} = \sum\limits_{i=0}^n C_n^i u^{(i)} v^{(n-i)}` 成立。根据数学归纳法原理，
    对于任意的 :math:`n \in \mathbb{N}`, :math:`(uv)^{(n)} = \sum\limits_{i=0}^n C_n^i u^{(i)} v^{(n-i)}` 成立。
