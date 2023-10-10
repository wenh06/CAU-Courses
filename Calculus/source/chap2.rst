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

        y^{(n + 1)} & = \dfrac{d \left( n(e^x + (-1)^{n - 1} e^{-x}) + x (e^x + (-1)^n e^{-x}) \right)}{dx} \\
        & = n(e^x + (-1)^{n} e^{-x}) + (e^x + (-1)^n e^{-x}) + x (e^x + (-1)^{n + 1} e^{-x}) \\
        & = (n + 1)(e^x + (-1)^{n} e^{-x}) + x (e^x + (-1)^{n + 1} e^{-x}) \\
        & = (n + 1)(e^x + (-1)^{(n + 1) - 1} e^{-x}) + x (e^x + (-1)^{n + 1} e^{-x})

    所以 :math:`y^{(n)} = n(e^x + (-1)^{n - 1} e^{-x}) + x (e^x + (-1)^n e^{-x})`. 令 :math:`n = 99` 有

    .. math::

        y^{(99)} = 99(e^x + (-1)^{98} e^{-x}) + x (e^x + (-1)^{99} e^{-x}) = 99(e^x + e^{-x}) + x (e^x - e^{-x}).

§2.4 隐函数与参数方程所确定的函数的导数
------------------------------------------

待写

§2.5 函数的微分
--------------------------------

待写

§2.6 微分中值定理
--------------------------------

待写

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
