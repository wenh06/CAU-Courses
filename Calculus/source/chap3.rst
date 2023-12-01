第三章  一元函数积分学及其应用
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  contents:: :local:


课后习题解答
=========================

§3.1 不定积分
---------------------

1. 计算下列不定积分：

(2). :math:`\displaystyle \int \left( \dfrac{1}{\sqrt{x}} - \dfrac{2}{\sqrt{1-x^2}} + 3e^x \right) \mathrm{d} x`;

(4). :math:`\displaystyle \int \dfrac{e^{2x} - 1}{e^x + 1} \mathrm{d} x`;

(6). :math:`\displaystyle \int (2^xe^x + 1) \mathrm{d} x`;

(8). :math:`\displaystyle \int \dfrac{1 - x + x^2}{x + x^3} \mathrm{d} x`;

(10). :math:`\displaystyle \int \dfrac{\cos 2x}{\cos^2 x \sin^2 x} \mathrm{d} x`.

.. proof:solution::

    (2).

    .. math::

        \int \left( \dfrac{1}{\sqrt{x}} - \dfrac{2}{\sqrt{1-x^2}} + 3e^x \right) \mathrm{d} x & = \int x^{-\frac{1}{2}} \mathrm{d} x - 2\int (1-x^2)^{-\frac{1}{2}} \mathrm{d} x + 3 \int e^x \mathrm{d} x \\
        & = 2\sqrt{x} - 2\arcsin x + 3e^x + C.

    (4).

    .. math::

        \int \dfrac{e^{2x} - 1}{e^x + 1} \mathrm{d} x & = \int \dfrac{(e^x + 1)(e^x - 1)}{e^x + 1} \mathrm{d} x \\
        & = \int (e^x - 1) \mathrm{d} x \\
        & = e^x - x + C.

    (6).

    .. math::

        \int (2^xe^x + 1) \mathrm{d} x & = \int (2e)^x \mathrm{d} x + \int \mathrm{d} x \\
        & = \dfrac{(2e)^x}{\ln (2e)} + x + C \\
        & = \dfrac{2^xe^x}{\ln 2 + 1} + x + C.

    (8).

    .. math::

        \int \dfrac{1 - x + x^2}{x + x^3} \mathrm{d} x & = \int \dfrac{1 + x^2}{x + x^3} \mathrm{d} x - \int \dfrac{x}{x + x^3} \mathrm{d} x \\
        & = \int \dfrac{1}{x} \mathrm{d} x - \int \dfrac{1}{x^2 + 1} \mathrm{d} x \\
        & = \ln |x| - \arctan x + C.

    (10).

    .. math::

        \int \dfrac{\cos 2x}{\cos^2 x \sin^2 x} \mathrm{d} x & = \int \dfrac{\cos 2x}{(\frac{1}{2} \sin 2x)^2} \mathrm{d} x \\
        & = 2 \int \dfrac{\mathrm{d} \sin 2x}{\sin^2 2x}  \\
        & = 2 \cdot \dfrac{-1}{\sin 2x} + C \\
        & = -\dfrac{2}{\sin 2x} + C.

2. 若某曲线过点 :math:`(1, 1)`, 且在任一点 :math:`x` 处的切线的斜率为 :math:`\dfrac{2}{x}`, 求此曲线方程.

.. proof:solution::

    设曲线方程为 :math:`y = f(x)`, 则 :math:`f'(x) = \dfrac{2}{x}`, 从而 :math:`\displaystyle f(x) = \int \dfrac{2}{x} \mathrm{d} x = 2\ln x + C`, 由 :math:`f(1) = 1` 知 :math:`C = 1`, 因此曲线方程为 :math:`y = 2\ln x + 1`.

3. 设 :math:`f'(e^x) = 1 + e^{3x}`, 且 :math:`f(0) = 1`, 求 :math:`f(x)`.

.. proof:solution::

    由题设知 :math:`f'(e^x) = 1 + e^{3x}`, 从而 :math:`f'(x) = 1 + x^3`, 那么

    .. math::

        f(x) = \int (1 + x^3) \mathrm{d} x = x + \dfrac{x^4}{4} + C

    由 :math:`f(0) = 1` 知 :math:`C = 1`, 因此 :math:`f(x) = x + \dfrac{x^4}{4} + 1`.

4. 计算下列不定积分：

(1). :math:`\displaystyle \int \dfrac{1}{(2x - 5)^{10}} \mathrm{d} x`;

(3). :math:`\displaystyle \int \dfrac{x}{\sqrt{1 + x^2}} \mathrm{d} x`;

(5). :math:`\displaystyle \int x^2 e^{2x^3} \mathrm{d} x`;

(7). :math:`\displaystyle \int \dfrac{\sqrt{1 + 3\ln x}}{x} \mathrm{d} x`;

(9). :math:`\displaystyle \int \dfrac{2x - 1}{\sqrt{1 - x^2}} \mathrm{d} x`;

(11). :math:`\displaystyle \int \dfrac{1}{4 + 9x^2} \mathrm{d} x`;

(13). :math:`\displaystyle \int \sin^2 x \cos^2 x \mathrm{d} x`;

(15). :math:`\displaystyle \int x (2x - 3)^{10} \mathrm{d} x`;

(17). :math:`\displaystyle \int \dfrac{1}{x^2 \sqrt{1 + x^2}} \mathrm{d} x`.

.. proof:solution::

    (1). 令 :math:`u = 2x - 5`, 则 :math:`\mathrm{d} u = 2 \mathrm{d} x`, 从而有

    .. math::

        \int \dfrac{1}{(2x - 5)^{10}} \mathrm{d} x & = \dfrac{1}{2} \int u^{-10} \mathrm{d} u = \dfrac{1}{2} \cdot \dfrac{u^{-9}}{-9} + C \\
        & = -\dfrac{1}{18(2x - 5)^9} + C.

    接下来，中间变量 :math:`u` 就不再写出了。

    (3).

    .. math::

        \int \dfrac{x}{\sqrt{1 + x^2}} \mathrm{d} x = \int \dfrac{\sqrt{1 + x^2}}{2} \mathrm{d} (1 + x^2) = \sqrt{1 + x^2} + C.

    (5).

    .. math::

        \int x^2 e^{2x^3} \mathrm{d} x = \dfrac{1}{6} \int e^{2x^3} \mathrm{d} (2x^3) = \dfrac{1}{6} e^{2x^3} + C.

    (7).

    .. math::

        \int \dfrac{\sqrt{1 + 3\ln x}}{x} \mathrm{d} x = \int \sqrt{1 + 3\ln x} \mathrm{d} (\ln x) = \dfrac{2}{9} (1 + 3\ln x)^{\frac{3}{2}} + C.

    (9).

    .. math::

        \int \dfrac{2x - 1}{\sqrt{1 - x^2}} \mathrm{d} x & = \int \dfrac{2x}{\sqrt{1 - x^2}} \mathrm{d} x - \int \dfrac{1}{\sqrt{1 - x^2}} \mathrm{d} x \\
        & = -\int \dfrac{1}{\sqrt{1 - x^2}} \mathrm{d} (1 - x^2) - \arcsin x + C \\
        & = -2 \sqrt{1 - x^2} - \arcsin x + C.

    (11).

    .. math::

        \int \dfrac{1}{4 + 9x^2} \mathrm{d} x = \dfrac{2}{3} \cdot \dfrac{1}{4} \int \dfrac{1}{1 + \left( \frac{3}{2} x \right)^2} \mathrm{d} \left( \frac{3}{2} x \right) = \dfrac{1}{6} \arctan \dfrac{3}{2} x + C.

    (13).

    .. math::

        \int \sin^2 x \cos^2 x \mathrm{d} x & = \dfrac{1}{4} \int \sin^2 2x \mathrm{d} x = \dfrac{1}{8} \int (1 - \cos 4x) \mathrm{d} x \\
        & = \dfrac{1}{32} \int (1 - \cos 4x) \mathrm{d} (4x) = \dfrac{1}{32} (4x - \sin 4x) + C.

    (15).

    .. math::

        \int x (2x - 3)^{10} \mathrm{d} x & = \int \dfrac{1}{2} (2x - 3)^{11} \mathrm{d} x + \int \dfrac{3}{2} (2x - 3)^{10} \mathrm{d} x \\
        & = \dfrac{1}{4} \int (2x - 3)^{11} \mathrm{d} (2x - 3) + \dfrac{3}{4} \int (2x - 3)^{10} \mathrm{d} (2x - 3) \\
        & = \dfrac{1}{4} \cdot \dfrac{(2x - 3)^{12}}{12} + \dfrac{3}{4} \cdot \dfrac{(2x - 3)^{11}}{11} + C \\
        & = \dfrac{1}{48} (2x - 3)^{12} + \dfrac{3}{44} (2x - 3)^{11} + C.

    (17).

    .. math::

        \int \dfrac{1}{x^2 \sqrt{1 + x^2}} \mathrm{d} x & = -\int \dfrac{1}{\sqrt{1 + x^2}} \mathrm{d} \left( \dfrac{1}{x} \right) = -\int \dfrac{1}{x} \cdot \dfrac{1}{\sqrt{1 + \left(\frac{1}{x}\right)^2}} \mathrm{d} \left( \dfrac{1}{x} \right) \\
        & = -\dfrac{1}{2} \int \dfrac{1}{\sqrt{1 + \left(\frac{1}{x}\right)^2}} \mathrm{d} \left( \frac{1}{x} \right)^2 \\
        & = -\sqrt{1 + \left(\frac{1}{x}\right)^2} + C \\
        & = -\dfrac{\sqrt{x^2 + 1}}{x} + C.

    以上假设了 :math:`x > 0`, 对于 :math:`x < 0` 的情况，从根式中提出 :math:`x` 要变（2次）号，最终结果是一样的。

5. 计算下列不定积分：

(2). :math:`\displaystyle \int x \cos (5x + 2) \mathrm{d} x`;

(4). :math:`\displaystyle \int \dfrac{\ln x}{\sqrt{x}} \mathrm{d} x`;

(6). :math:`\displaystyle \int \ln(1 + x^2) \mathrm{d} x`.

(8). 设 :math:`f(x)` 的一个原函数为 :math:`x \cos x`, 求积分 :math:`\displaystyle \int x f'(x) \mathrm{d} x`.

.. proof:solution::

    (2). 采用分部积分法：

    .. math::

        \int x \cos (5x + 2) \mathrm{d} x & = \dfrac{1}{5} \int x \mathrm{d} \left( \sin (5x + 2) \right) = \dfrac{1}{5} x \sin (5x + 2) - \dfrac{1}{5} \int \sin (5x + 2) \mathrm{d} x \\
        & = \dfrac{1}{5} x \sin (5x + 2) + \dfrac{1}{25} \cos (5x + 2) + C.

    (4). 令 :math:`x = t^2, t > 0`, 则 :math:`\mathrm{d} x = 2t \mathrm{d} t`, 从而有

    .. math::

        \int \dfrac{\ln x}{\sqrt{x}} \mathrm{d} x & = \int \dfrac{2t \ln t^2}{t} \mathrm{d} t = 4 \int \ln t \mathrm{d} t \\
        & = 4t \ln t - 4 \int t \mathrm{d} (\ln t) = 4t \ln t - 4 \int t \cdot \dfrac{1}{t} \mathrm{d} t \\
        & = 4t \ln t - 4t + C = 4 \sqrt{x} \ln \sqrt{x} - 4 \sqrt{x} + C \\
        & = 2 \sqrt{x} \ln x - 4 \sqrt{x} + C.

    也可以直接采用分部积分法：

    .. math::

        \int \dfrac{\ln x}{\sqrt{x}} \mathrm{d} x & = 2 \int \ln x \mathrm{d} \left( \sqrt{x} \right) = 2 \sqrt{x} \ln x - 2 \int \sqrt{x} \mathrm{d} (\ln x) \\
        & = 2 \sqrt{x} \ln x - 2 \int \sqrt{x} \cdot \dfrac{1}{x} \mathrm{d} x \\
        & = 2 \sqrt{x} \ln x - 2 \int \dfrac{1}{\sqrt{x}} \mathrm{d} x \\
        & = 2 \sqrt{x} \ln x - 4 \sqrt{x} + C.

    (6). 采用分部积分法：

    .. math::

        \int \ln(1 + x^2) \mathrm{d} x & = x \ln(1 + x^2) - \int x \mathrm{d} (\ln(1 + x^2)) = x \ln(1 + x^2) - \int x \cdot \dfrac{2x}{1 + x^2} \mathrm{d} x \\
        & = x \ln(1 + x^2) - 2 \int \dfrac{x^2}{1 + x^2} \mathrm{d} x = x \ln(1 + x^2) - 2 \int \left( 1 - \dfrac{1}{1 + x^2} \right) \mathrm{d} x \\
        & = x \ln(1 + x^2) - 2x + 2 \arctan x + C.

    (8). 采用分部积分法：

    .. math::

        \int x f'(x) \mathrm{d} x & = \int x \mathrm{d} f(x) = x f(x) - \int f(x) \mathrm{d} x \\
        & = x (x \cos x)' - x \cos x + C = x \cos x - x^2 \sin x - x \cos x + C \\
        &= -x^2 \sin x + C.

6. 计算下列不定积分：

(1). :math:`\displaystyle \int \dfrac{1}{3 + \sin^2 x} \mathrm{d} x`;

(3). :math:`\displaystyle \int \cos x \cos 5x \mathrm{d} x`;

(5). :math:`\displaystyle \int \dfrac{2x + 5}{x^2 + 4x + 8} \mathrm{d} x`;

(7). :math:`\displaystyle \int \dfrac{x}{\sqrt{3 + 4x}} \mathrm{d} x`.

.. proof:solution::

    (1).

    .. math::

        \int \dfrac{1}{3 + \sin^2 x} \mathrm{d} x & = \int \dfrac{1}{3\cos^2 x + 4\sin^2 x} \mathrm{d} x = \int \dfrac{\sec^2x \mathrm{d} x}{3 + 4\tan^2 x} \\
        & = \int \dfrac{\mathrm{d} \tan x}{3 + 4\tan^2 x} = \dfrac{1}{2\sqrt{3}} \int \dfrac{\mathrm{d} \left( \frac{2}{\sqrt{3}} \tan x \right)}{1 + \left( \frac{2}{\sqrt{3}} \tan x \right)^2} \\
        & = \dfrac{1}{2\sqrt{3}} \arctan \left( \dfrac{2}{\sqrt{3}} \tan x \right) + C.

    (3). 利用和差化积公式 :math:`\cos x \cos 5x = \dfrac{1}{2} (\cos 4x + \cos 6x)`, 从而有

    .. math::

        \int \cos x \cos 5x \mathrm{d} x & = \dfrac{1}{2} \int \cos 4x \mathrm{d} x + \dfrac{1}{2} \int \cos 6x \mathrm{d} x \\
        & = \dfrac{1}{8} \sin 4x + \dfrac{1}{12} \sin 6x + C.

    (5).

    .. math::

        \int \dfrac{2x + 5}{x^2 + 4x + 8} \mathrm{d} x & = \int \dfrac{2(x + 2) + 1}{(x + 2)^2 + 4} \mathrm{d} (x + 2) \\
        & = 2 \int \dfrac{x + 2}{(x + 2)^2 + 4} \mathrm{d} (x + 2) + \int \dfrac{1}{(x + 2)^2 + 4} \mathrm{d} (x + 2) \\
        & = \int \dfrac{1}{(x + 2)^2 + 4} \mathrm{d} (x + 2)^2 + \dfrac{1}{2} \int \dfrac{1}{(\frac{x + 2}{2})^2 + 1} \mathrm{d} \left(\dfrac{x + 2}{2}\right) \\
        & = \ln \left\lvert (x + 2)^2 + 4 \right\rvert + \dfrac{1}{2} \arctan \dfrac{x + 2}{2} + C \\
        & = \ln (x^2 + 4x + 8) + \dfrac{1}{2} \arctan \dfrac{x + 2}{2} + C.

    (7). 令 :math:`u = \sqrt{3 + 4x}`, 那么 :math:`\mathrm{d} x = \dfrac{u \mathrm{d} u}{2}`, 从而有

    .. math::

        \int \dfrac{x}{\sqrt{3 + 4x}} \mathrm{d} x & = \int \dfrac{u^2 - 3}{4u} \cdot \dfrac{u \mathrm{d} u}{2} = \dfrac{1}{8} \int (u^2 - 3) \mathrm{d} u \\
        & = \dfrac{1}{8} \cdot \dfrac{u^3}{3} - \dfrac{3}{8} u + C \\
        & = \dfrac{1}{24} (3 + 4x)^{\frac{3}{2}} - \dfrac{3}{8} \sqrt{3 + 4x} + C \\
        & = \sqrt{3 + 4x} \left( \dfrac{1}{24} (3 + 4x) - \dfrac{3}{8} \right) + C \\
        & = \dfrac{4x - 6}{24} \sqrt{3 + 4x} + C \\
        & = \dfrac{2x - 3}{12} \sqrt{3 + 4x} + C.

§3.2 定积分
---------------------

2. 设 :math:`x` 轴上有一根细棒，位于 :math:`x = a` 到 :math:`x = b` 的区间上，这棒在 :math:`x` 处的线密度为 :math:`\rho(x)`,
试用定积分表示这细棒的质量.

.. proof:solution::

    设细棒的质量为 :math:`m`, 则有

    .. math::

        m = \int_a^b \rho(x) \mathrm{d} x.

3. 利用定积分的几何意义，给出下列定积分的值：

(1). :math:`\displaystyle \int_a^b x \mathrm{d} x`;

(3). :math:`\displaystyle \int_{-\pi}^{\pi} \sin x \mathrm{d} x`;

(5). :math:`\displaystyle \int_0^4 (2 - x) \mathrm{d} x`.

.. proof:solution::

    (1). 假设 :math:`a < b`.

    定积分 :math:`\displaystyle \int_a^b x \mathrm{d} x` 表示 :math:`x` 从 :math:`a` 到 :math:`b` 曲线 :math:`y = x` 与 :math:`x` 轴之间（带正负号）的面积。
    当 :math:`a, b` 同号时，这是一个底边长 :math:`|a|, |b|`, 高为 :math:`|a - b|` 的梯形，面积为 :math:`\dfrac{|a| + |b|}{2} |a - b|`.
    当 :math:`a, b > 0` 时，面积为正的，当 :math:`a, b < 0` 时，面积为负的。值为 :math:`\dfrac{b^2 - a^2}{2}`.

    当 :math:`a \leqslant 0 \leqslant b`, 定积分 :math:`\displaystyle \int_a^b x \mathrm{d} x` 表示两个三角形的面积之差 (包括等于 :math:`0` 时退化的情况).
    这是两个等腰直角三角形，直角边长分别为 :math:`-a, b`, 面积之差为 :math:`\dfrac{b^2 - a^2}{2}`.

    (3). :math:`\sin x` 在 :math:`(-\pi, 0)` 取值为负， :math:`(0, \pi)` 取值为正，因此定积分 :math:`\displaystyle \int_{-\pi}^{\pi} \sin x \mathrm{d} x`
    表示 这两部分曲线与 :math:`x` 轴围成（带正负号）的面积之和。正两部分面积正好绝对值相等，符号相反，因此定积分的值为 :math:`0`.

    (5). :math:`\displaystyle \int_0^4 (2 - x) \mathrm{d} x` 表示 :math:`x` 从 :math:`0` 到 :math:`4` 曲线 :math:`y = 2 - x` 与 :math:`x` 轴之间（带正负号）的面积。
    :math:`x` 从 :math:`0` 到 :math:`2` 时， :math:`y = 2 - x` 在 :math:`x` 轴上方，面积为正， :math:`x` 从 :math:`2` 到 :math:`4` 时，
    :math:`y = 2 - x` 在 :math:`x` 轴下方，面积为负。这两部分面积绝对值相等，符号相反，因此定积分的值为 :math:`0`.

4. 利用定积分的性质，比较下列各组积分值的大小：

(2). :math:`\displaystyle \int_0^1 e^x \mathrm{d} x` 与 :math:`\displaystyle \int_0^1 (1 + x) \mathrm{d} x`.

.. proof:solution::

    由于在区间 :math:`(0, 1)` 上有不等式 :math:`e^x > 1 + x`, 因此有 :math:`\displaystyle \int_0^1 e^x \mathrm{d} x > \int_0^1 (1 + x) \mathrm{d} x`.

5. 证明下列不等式：

(2). :math:`\displaystyle 2 e^{-\frac{1}{4}} < \int_0^2 e^{x^2 - x} \mathrm{d} x < 2 e^2`.

.. proof:proof::

    由于 :math:`e^{x^2 - x} = e^{\left( x - \frac{1}{2} \right)^2 - \frac{1}{4}}` 在区间 :math:`[0, 2]` 上的最小值为 :math:`e^{-\frac{1}{4}}`,
    最大值为 :math:`e^2`, 因此有

    .. math::

        2 e^{-\frac{1}{4}} = \int_0^2 e^{-\frac{1}{4}} \mathrm{d} x < \int_0^2 e^{x^2 - x} \mathrm{d} x < \int_0^2 e^2 \mathrm{d} x = 2 e^2.

6. 设函数 :math:`f(x)` 在区间 :math:`[1, 3]` 上的平均值为 :math:`6`, 求定积分 :math:`\displaystyle \int_1^3 f(x) \mathrm{d} x`.

.. proof:solution::

    函数 :math:`f(x)` 在区间 :math:`[1, 3]` 上的平均值为 :math:`6`, 也就是说有

    .. math::

        \dfrac{\int_1^3 f(x) \mathrm{d} x}{3 - 1} = 6,

    从而有 :math:`\displaystyle \int_1^3 f(x) \mathrm{d} x = 12`.

§3.3 定积分的计算
---------------------

1. 计算下列各题：

(2). 设 :math:`\displaystyle f(x) = \int_0^x e^{-t^2} \mathrm{d} t`, 求 :math:`f''(1)`;

(4). 求 :math:`\displaystyle \dfrac{\mathrm{d}}{\mathrm{d} x} \int_{x^2}^{x^3} \dfrac{1}{\sqrt{1 + u^4}} \mathrm{d} u`;

(6). 求极限 :math:`\displaystyle \lim_{x \to 0} \dfrac{\int_0^x t(t + \sin t) \mathrm{d} t}{\int_x^0 \ln (1 + t^2) \mathrm{d} t}`.

.. proof:solution::

    (1). :math:`f'(x) = e^{-x^2}`, :math:`f''(x) = -2x e^{-x^2}`, 因此 :math:`f''(1) = -2e^{-1}`.

    (3). :math:`\displaystyle \dfrac{\mathrm{d}}{\mathrm{d} x} \int_{x^2}^{x^3} \dfrac{1}{\sqrt{1 + u^4}} \mathrm{d} u = \dfrac{1}{\sqrt{1 + x^{12}}} \cdot 3x^2 - \dfrac{1}{\sqrt{1 + x^8}} \cdot 2x = \dfrac{3x^2}{\sqrt{1 + x^{12}}} - \dfrac{2x}{\sqrt{1 + x^8}}`.

    (5).

    .. math::

        \displaystyle \lim_{x \to 0} \dfrac{\int_0^x t(t + \sin t) \mathrm{d} t}{\int_x^0 \ln (1 + t^2) \mathrm{d} t} & = \lim_{x \to 0} \dfrac{\int_0^x t(t + \sin t) \mathrm{d} t}{-\int_0^x \ln (1 + t^2) \mathrm{d} t} = -\lim_{x \to 0} \dfrac{x(x + \sin x)}{\ln (1 + x^2)} \\
        & = -\lim_{x \to 0} \dfrac{2x + x \cos x + \sin x}{\frac{2x}{1 + x^2}} \\
        & = -\lim_{x \to 0} (1 + x^2) \dfrac{2x + x \cos x + \sin x}{2x} \\
        & = -2.

    .. note::

        一般地，如果 :math:`\displaystyle f(x) = \int_{\varphi(x)}^{\psi(x)} g(t) \mathrm{d} t`, 那么

        .. math::

            f'(x) = g(\psi(x)) \psi'(x) - g(\varphi(x)) \varphi'(x).

2. 设 :math:`y = f(x)` 是由方程 :math:`\displaystyle x^2 y = \int_0^y \sqrt{1 + t^2} \mathrm{d} t` 所确定的隐函数，
试求 :math:`y = f(x)` 的微分 :math:`\mathrm{d} y`.

.. proof:solution::

    对方程两边求微分，有

    .. math::

        2x y \mathrm{d} x + x^2 \mathrm{d} y = \sqrt{1 + y^2} \mathrm{d} y,

    移项之后有

    .. math::

        \mathrm{d} y = \dfrac{2x y}{\sqrt{1 + y^2} - x^2} \mathrm{d} x.

3. 设函数 :math:`f(x)` 在区间 :math:`[a, b]` 上连续且单调增加，令

.. math::

    F(x) = \dfrac{1}{x - a} \int_a^x f(t) \mathrm{d} t \quad (a < x \leqslant b),

试证明在区间 :math:`(a, b]` 上恒有 :math:`F'(x) \geqslant 0`.

.. proof:proof::

    由于 :math:`f(x)` 在区间 :math:`[a, b]` 上连续且单调增加，所以有

    .. math::

        F'(x) = \dfrac{1}{x - a} \cdot f(x) - \dfrac{1}{(x - a)^2} \int_a^x f(t) \mathrm{d} t.

    进一步由积分中值定理，存在 :math:`\xi \in (a, x)` 使得 :math:`\displaystyle \int_a^x f(t) \mathrm{d} t = f(\xi) (x - a)`, 因此有

    .. math::

        F'(x) = \dfrac{1}{x - a} \cdot f(x) - \dfrac{f(\xi) (x - a)}{(x - a)^2} = \dfrac{1}{x - a} \cdot \left( f(x) - f(\xi) \right).

    由于 :math:`f(x)` 在区间 :math:`[a, b]` 上连续且单调增加，因此有 :math:`f(x) \geqslant f(\xi)`, 从而有 :math:`F'(x) \geqslant 0`.

4. 计算下列定积分：

(1). :math:`\displaystyle \int_0^4 (2 - \sqrt{x})^2 \mathrm{d} x`;

(3). :math:`\displaystyle \int_0^1 \dfrac{1}{\sqrt{4-u^2}} \mathrm{d} u`;

(5). 设 :math:`\displaystyle f(x) = \begin{cases} \frac{x}{2} + 1, & 0 \leqslant x \leqslant 2 \\ x, & 2 < x \leqslant 3 \end{cases}`, 求 :math:`\displaystyle \int_0^3 f(x) \mathrm{d} x`.

(7). :math:`\displaystyle \int_0^2 (2 - x)^2 (2 + x) \mathrm{d} x`;

(9). :math:`\displaystyle \int_0^{\pi} (1 - \sin^3 \varphi) \mathrm{d} \varphi`.

.. proof:solution::

    (1). 令 :math:`t = \sqrt{x}`, 那么 :math:`x = t^2, \mathrm{d} x = 2t \mathrm{d} t`, 从而有

    .. math::

        \int_0^4 (2 - \sqrt{x})^2 \mathrm{d} x & = \int_0^2 (2 - t)^2 \cdot 2t \mathrm{d} t = 2 \int_0^2 (4 - 4t + t^2) t \mathrm{d} t \\
        & = 2 \int_0^2 (4t - 4t^2 + t^3) \mathrm{d} t = 2 \left. \left[ 2t^2 - \dfrac{4}{3} t^3 + \dfrac{1}{4} t^4 \right] \right|_0^2 \\
        & = 2 \left( 8 - \dfrac{32}{3} + 4 \right) = \dfrac{8}{3}.

    (3). 令 :math:`u = 2 \sin \varphi`, 那么 :math:`\mathrm{d} u = 2 \cos \varphi \mathrm{d} \varphi`, 从而有

    .. math::

        \int_0^1 \dfrac{1}{\sqrt{4-u^2}} \mathrm{d} u & = \int_0^{\frac{\pi}{6}} \dfrac{1}{\sqrt{4 - 4 \sin^2 \varphi}} \cdot 2 \cos \varphi \mathrm{d} \varphi \\
        & = \int_0^{\frac{\pi}{6}} \dfrac{1}{\sqrt{4 \cos^2 \varphi}} \cdot 2 \cos \varphi \mathrm{d} \varphi = \int_0^{\frac{\pi}{6}} \dfrac{1}{2 \cos \varphi} \cdot 2 \cos \varphi \mathrm{d} \varphi \\
        & = \int_0^{\frac{\pi}{6}} \mathrm{d} \varphi = \dfrac{\pi}{6}.

    (5). 根据定积分对积分区间的可加性，有

    .. math::

        \int_0^3 f(x) \mathrm{d} x & = \int_0^2 f(x) \mathrm{d} x + \int_2^3 f(x) \mathrm{d} x = \int_0^2 \left( \dfrac{x}{2} + 1 \right) \mathrm{d} x + \int_2^3 x \mathrm{d} x \\
        & = \left. \left( \dfrac{x^2}{4} + x \right) \right|_0^2 + \left. \dfrac{x^2}{2} \right|_2^3 = 3 + \dfrac{9}{2} - 2 = \dfrac{11}{2}.

    (7).

    .. math::

        \int_0^2 (2 - x)^2 (2 + x) \mathrm{d} x & = \int_2^0 x^2 (4 - x) \mathrm{d} (2-x) = \int_0^2 x^2 (4 - x) \mathrm{d} x \\
        & = \int_0^2 (4x^2 - x^3) \mathrm{d} x = \left. \left( \dfrac{4}{3} x^3 - \dfrac{1}{4} x^4 \right) \right|_0^2 \\
        & = \dfrac{32}{3} - 4 = \dfrac{20}{3}.

    (9). 由于 :math:`\sin^3 \varphi = \dfrac{3}{4} \sin \varphi - \dfrac{1}{4} \sin 3\varphi`, 因此有

    .. math::

        \int_0^{\pi} (1 - \sin^3 \varphi) \mathrm{d} \varphi & = \int_0^{\pi} \left( 1 - \dfrac{3}{4} \sin \varphi + \dfrac{1}{4} \sin 3\varphi \right) \mathrm{d} \varphi \\
        & = \left. \left( \varphi + \dfrac{3}{4} \cos \varphi - \dfrac{1}{12} \cos 3\varphi \right) \right|_0^{\pi} \\
        & = \pi - \dfrac{3}{4} + \dfrac{1}{12} - (0 + \dfrac{3}{4} - \dfrac{1}{12}) \\
        & = \pi - \dfrac{4}{3}.

5. 计算下列定积分：

(2). :math:`\displaystyle \int_0^{\pi} \dfrac{\sin x}{1 + \cos^2 x} \mathrm{d} x`;

(4). :math:`\displaystyle \int_0^1 x^2 \sqrt{1 - x^2} \mathrm{d} x`;

(6). :math:`\displaystyle \int_1^2 \dfrac{\sqrt{x^2 - 1}}{x} \mathrm{d} x`;

(8). :math:`\displaystyle \int_{-1}^1 \dfrac{x}{\sqrt{5 - 4x}} \mathrm{d} x`.

.. proof:solution::

    (2).

    .. math::

        \int_0^{\pi} \dfrac{\sin x}{1 + \cos^2 x} \mathrm{d} x & = - \int_0^{\pi} \dfrac{\mathrm{d} \cos x}{1 + \cos^2 x} = - \left. \arctan \cos x \right|_0^{\pi} \\
        & = - \left( \arctan (-1) - \arctan 1 \right) = - \left( -\dfrac{\pi}{4} - \dfrac{\pi}{4} \right) = \dfrac{\pi}{2}.

    (4).

    .. math::

        \int_0^1 x^2 \sqrt{1 - x^2} \mathrm{d} x & = \dfrac{1}{2} \int_0^1 \sqrt{x^2 (1 - x^2)} \mathrm{d} x^2 = \dfrac{1}{2} \int_0^1 \sqrt{x (1 - x)} \mathrm{d} x \\
        & = \dfrac{1}{2} \int_0^1 \sqrt{\dfrac{1}{4} - \left( x - \dfrac{1}{2} \right)^2} \mathrm{d} \left( x - \dfrac{1}{2} \right) \\
        & = \dfrac{1}{8} \int_0^1 \sqrt{1 - \left( 2x - 1 \right)^2} \mathrm{d} \left( 2x - 1 \right) \\
        & = \dfrac{1}{8} \int_{-1}^1 \sqrt{1 - x^2} \mathrm{d} x \\
        & = \dfrac{1}{4} \int_{0}^1 \sqrt{1 - x^2} \mathrm{d} x \\
        & = \dfrac{1}{4} \int_{0}^{\frac{\pi}{2}} \sqrt{1 - \sin^2 \varphi} \mathrm{d} \sin \varphi \\
        & = \dfrac{1}{4} \int_{0}^{\frac{\pi}{2}} \cos^2 \varphi \mathrm{d} \varphi \\
        & = \dfrac{1}{4} \int_{0}^{\frac{\pi}{2}} \dfrac{1 + \cos 2\varphi}{2} \mathrm{d} \varphi \\
        & = \dfrac{1}{8} \left. \left( \varphi + \dfrac{1}{2} \sin 2\varphi \right) \right|_0^{\frac{\pi}{2}} \\
        & = \dfrac{\pi}{16}.

    另解：令 :math:`x = \sin t`, 积分区域变为 :math:`[0, \frac{\pi}{2}]`, 从而有

    .. math::

        \int_0^1 x^2 \sqrt{1 - x^2} \mathrm{d} x & = \int_0^{\frac{\pi}{2}} \sin^2 t \cos t \mathrm{d} \sin t = \int_0^{\frac{\pi}{2}} \sin^2 t \cos^2 t \mathrm{d} t \\
        & = \dfrac{1}{4} \int_0^{\frac{\pi}{2}} \sin^2 2t \mathrm{d} t \\
        & = \dfrac{1}{4} \int_0^{\frac{\pi}{2}} \dfrac{1 - \cos 4t}{2} \mathrm{d} t \\
        & = \dfrac{1}{8} \int_0^{\frac{\pi}{2}} \left( 1 - \cos 4t \right) \mathrm{d} t \\
        & = \dfrac{1}{8} \int_0^{\frac{\pi}{2}} \mathrm{d} t - \dfrac{1}{8} \int_0^{\frac{\pi}{2}} \cos 4t \mathrm{d} t \\
        & = \dfrac{\pi}{16}.

    (6). 令 :math:`x = \sec \varphi`, 积分区域变为 :math:`[0, \frac{\pi}{3}]`, 从而有

    .. math::

        \int_1^2 \dfrac{\sqrt{x^2 - 1}}{x} \mathrm{d} x & = \int_{0}^{\frac{\pi}{3}} \dfrac{\tan \varphi}{\sec \varphi} \cdot \sec \varphi \tan \varphi \mathrm{d} \varphi \\
        & = \int_{0}^{\frac{\pi}{3}} \tan^2 \varphi \mathrm{d} \varphi \\
        & = \int_{0}^{\frac{\pi}{3}} \sec^2 \varphi \mathrm{d} \varphi - \int_{0}^{\frac{\pi}{3}} \mathrm{d} \varphi \\
        & = \left. \tan \varphi \right|_0^{\frac{\pi}{3}} - \left. \varphi \right|_0^{\frac{\pi}{3}} \\
        & = \sqrt{3} - \dfrac{\pi}{3}.

    (8). 令 :math:`t = \sqrt{5 - 4x}`, 那么 :math:`x = \dfrac{5 - t^2}{4}`, :math:`\mathrm{d} x = -\dfrac{t}{2} \mathrm{d} t`, 从而有

    .. math::

        \int_{-1}^1 \dfrac{x}{\sqrt{5 - 4x}} \mathrm{d} x & = \int_{3}^1 \dfrac{\frac{5 - t^2}{4}}{t} \cdot \left( -\dfrac{t}{2} \right) \mathrm{d} t = \dfrac{1}{8} \int_1^{3} \left( 5 - t^2 \right) \mathrm{d} t \\
        & = \dfrac{1}{8} \left. \left( 5t - \dfrac{t^3}{3} \right) \right|_1^{3} = \dfrac{1}{8} \left( 15 - \dfrac{27}{3} - 5 + \dfrac{1}{3} \right) \\
        & = \dfrac{1}{6}.

6. 计算下列定积分：

(1). :math:`\displaystyle \int_0^1 x \ln(1 + x) \mathrm{d} x`;

(3). :math:`\displaystyle \int_0^{\sqrt{3}} \ln \left( x + \sqrt{1 + x^2} \right) \mathrm{d} x`;

(5). :math:`\displaystyle \int_0^{\frac{\sqrt{2}}{2}} \arccos x \mathrm{d} x`;

(7). :math:`\displaystyle \int_{-1}^1 \dfrac{x^2 \sin^5 x + 1}{1 + x^2} \mathrm{d} x`.

.. proof:solution::

    (1).

    .. math::

        \int_0^1 x \ln(1 + x) \mathrm{d} x & = \dfrac{1}{2} \int_0^1 \ln(1 + x) \mathrm{d} x^2 = \left. \dfrac{1}{2} \ln(1 + x) \cdot x^2 \right|_0^1 - \dfrac{1}{2} \int_0^1 \dfrac{x^2}{1 + x} \mathrm{d} x \\
        & = \dfrac{1}{2} \ln 2 - \dfrac{1}{2} \int_0^1 \left( x - 1 + \dfrac{1}{1 + x} \right) \mathrm{d} x \\
        & = \dfrac{1}{2} \ln 2 - \dfrac{1}{2} \left. \left( \dfrac{x^2}{2} - x + \ln(1 + x) \right) \right|_0^1 \\
        & = \dfrac{1}{2} \ln 2 - \dfrac{1}{2} \left( \dfrac{1}{2} - 1 + \ln 2 \right) \\
        & = \dfrac{1}{4}.

    (3).

    .. math::

        \int_0^{\sqrt{3}} \ln \left( x + \sqrt{1 + x^2} \right) \mathrm{d} x & = \left. x \ln \left( x + \sqrt{1 + x^2} \right) \right|_0^{\sqrt{3}} - \int_0^{\sqrt{3}} x \dfrac{1 + \dfrac{x}{\sqrt{1 + x^2}}}{x + \sqrt{1 + x^2}} \mathrm{d} x \\
        & = \sqrt{3} \ln \left( \sqrt{3} + 2 \right) - \int_0^{\sqrt{3}} \dfrac{x}{\sqrt{1 + x^2}} \mathrm{d} x \\
        & = \sqrt{3} \ln \left( \sqrt{3} + 2 \right) - \dfrac{1}{2} \int_0^{\sqrt{3}} \dfrac{\mathrm{d} x^2}{\sqrt{1 + x^2}} \\
        & = \sqrt{3} \ln \left( \sqrt{3} + 2 \right) - \dfrac{1}{2} \int_0^{\sqrt{3}} \dfrac{\mathrm{d} \left( 1 + x^2 \right)}{\sqrt{1 + x^2}} \\
        & = \sqrt{3} \ln \left( \sqrt{3} + 2 \right) - \left. \sqrt{1 + x^2} \right|_0^{\sqrt{3}} \\
        & = \sqrt{3} \ln \left( \sqrt{3} + 2 \right) - 1.

    (5).

    .. math::

        \int_0^{\frac{\sqrt{2}}{2}} \arccos x \mathrm{d} x & = \left. x \arccos x \right|_0^{\frac{\sqrt{2}}{2}} - \int_0^{\frac{\sqrt{2}}{2}} \dfrac{x}{-\sqrt{1 - x^2}} \mathrm{d} x \\
        & = \dfrac{\pi}{4} \cdot \dfrac{\sqrt{2}}{2} - \left. \sqrt{1 - x^2} \right|_0^{\frac{\sqrt{2}}{2}} \\
        & = \dfrac{\pi}{8} - \dfrac{\sqrt{2}}{2} + 1.

    (7). 因为 :math:`\dfrac{x^2 \sin^5 x}{1 + x^2}` 是奇函数，所以 :math:`\displaystyle \int_{-1}^1 \dfrac{x^2 \sin^5 x}{1 + x^2} \mathrm{d} x = 0`, 因此有

    .. math::

        \int_{-1}^1 \dfrac{x^2 \sin^5 x + 1}{1 + x^2} \mathrm{d} x & = \int_{-1}^1 \dfrac{1}{1 + x^2} \mathrm{d} x = \left. \arctan x \right|_{-1}^1 \\
        & = \arctan 1 - \arctan (-1) = \dfrac{\pi}{2}.

7. 设 :math:`f(x)` 在区间 :math:`[a, b]` 上连续，证明 :math:`\displaystyle \int_a^b f(x) \mathrm{d} x = \int_a^b f(a + b - x) \mathrm{d} x`.

.. proof:proof::

    令 :math:`t = a + b - x`, 那么 :math:`x = a + b - t, \mathrm{d} t = -\mathrm{d} x`, 积分区间变为 :math:`[a + b - b, a + b - a] = [a, b]`, 从而有

    .. math::

        \int_a^b f(a + b - x) \mathrm{d} x & = -\int_{a + b - a}^{a + b - b} f(t) \mathrm{d} t \\
        & = -\int_b^a f(t) \mathrm{d} t = \int_a^b f(t) \mathrm{d} t \\
        & = \int_a^b f(x) \mathrm{d} x.

8. 设 :math:`a > 0`, 试证明： :math:`\displaystyle \int_0^a x^3 f(x^2) \mathrm{d} x = \dfrac{1}{2} \int_0^{a^2} x f(x) \mathrm{d} x`.

.. proof:proof::

    :math:`\displaystyle \int_0^a x^3 f(x^2) \mathrm{d} x = \dfrac{1}{2} \int_0^a x^2 f(x^2) \mathrm{d} (x^2) = \dfrac{1}{2} \int_0^{a^2} x f(x) \mathrm{d} x`.

9. 证明： :math:`\displaystyle \int_0^{\pi} \sin^n x \mathrm{d} x = 2 \int_0^{\frac{\pi}{2}} \sin^n x \mathrm{d} x`.

.. proof:proof::

    令 :math:`t = x - \dfrac{\pi}{2}`, 那么 :math:`x = t + \dfrac{\pi}{2}`, :math:`\mathrm{d} t = \mathrm{d} x`, 积分区间变为 :math:`[-\dfrac{\pi}{2}, \dfrac{\pi}{2}]`, 从而有

    .. math::

        \int_0^{\pi} \sin^n x \mathrm{d} x = \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \sin^n \left( t + \dfrac{\pi}{2} \right) \mathrm{d} t = \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \cos^n t \mathrm{d} t.

    由于 :math:`\cos^n t` 是偶函数，因此有

    .. math::

        \int_0^{\pi} \sin^n x \mathrm{d} x = \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \cos^n t \mathrm{d} t = 2 \int_0^{\frac{\pi}{2}} \cos^n t \mathrm{d} t = 2 \int_0^{\frac{\pi}{2}} \sin^n x \mathrm{d} x.

§3.4 定积分的应用
---------------------

1. 求下列各曲线所围成的图形的面积：

(1). :math:`y = 9 - x^2, y = 0`;

(3). :math:`y = x^3, x = 0, y = 1`;

(5). :math:`y = \sin x, x = -\pi, x = \dfrac{\pi}{2}, y = 0`;

(7). :math:`r = 2a (2 + \cos \theta)`.

.. proof:solution::

    (1). :math:`y = 9 - x^2` 与 :math:`y = 0` 的交点为 :math:`x = \pm 3`, 因此所围成的图形的面积 :math:`S` 为

    .. math::

        S = \int_{-3}^3 (9 - x^2) \mathrm{d} x = \left. \left( 9x - \dfrac{x^3}{3} \right) \right|_{-3}^3 = 36.

    (3). :math:`y = x^3, x = 0, y = 1` 所围成的图形为正方形 :math:`[0, 1] \times [0, 1]` 内，位于曲线 :math:`y = x^3` 之上的部分，
    因此所围成的图形的面积 :math:`S` 为

    .. math::

        S = \int_0^1 (1 - x^3) \mathrm{d} x = \left. \left( x - \dfrac{x^4}{4} \right) \right|_0^1 = \dfrac{3}{4}.

    (5). :math:`y = \sin x, x = -\pi, x = \dfrac{\pi}{2}, y = 0` 所围成的图形分为两部分，一部分为 :math:`[-\pi, 0] \times [0, 1]` 内在曲线 :math:`y = \sin x` 之上的部分；另一部分为 :math:`[0, \frac{\pi}{2}] \times [0, 1]` 内在曲线 :math:`y = \sin x` 之下的部分，因此所围成的图形的面积 :math:`S` 为

    .. math::

        S = \int_{-\pi}^0 (0 - \sin x) \mathrm{d} x + \int_0^{\frac{\pi}{2}} (\sin x - 0) \mathrm{d} x = \left. \left( \cos x \right) \right|_{-\pi}^0 - \left. \cos x \right|_0^{\frac{\pi}{2}} = 3.

    (7). :math:`r = 2a (2 + \cos \theta)` 所围成的图形为 :math:`\theta` 从 :math:`0` 增加到 :math:`2\pi` 形成的闭合曲线所围成的图形，因此所围成的图形的面积 :math:`S` 为

    .. math::

        S & = \int_0^{2\pi} \dfrac{1}{2} r^2 \mathrm{d} \theta = \int_0^{2\pi} \dfrac{1}{2} \cdot 4a^2 (2 + \cos \theta)^2 \mathrm{d} \theta \\
        & = 2a^2 \int_0^{2\pi} \left( 4 + 4 \cos \theta + \cos^2 \theta \right) \mathrm{d} \theta \\
        & = 2a^2 \int_0^{2\pi} \left( 4 + 4 \cos \theta + \dfrac{1 + \cos 2\theta}{2} \right) \mathrm{d} \theta \\
        & = 2a^2 \left. \left( 4\theta + 4 \sin \theta + \dfrac{\theta}{2} + \dfrac{\sin 2\theta}{4} \right) \right|_0^{2\pi} \\
        & = 2a^2 \left( 8\pi + 0 + \pi + 0 \right) = 18 \pi a^2.

2. 求抛物线 :math:`y = -x^2 + 4x - 3` 与其在点 :math:`(0, -3)` 和 :math:`(3, 0)` 处的切线所围成的平面图形的面积.

.. proof:solution::

    抛物线 :math:`y = -x^2 + 4x - 3` 的导函数为 :math:`y' = -2x + 4`, 因此在点 :math:`A = (0, -3)` 处的切线方程为 :math:`y = 4x - 3`,
    在点 :math:`B = (3, 0)` 处的切线方程为 :math:`y = -2x + 6`, 两条切线的交点为 :math:`C = \left( \frac{3}{2}, 3 \right)`.
    因此所围成的图形的为三角形 :math:`\triangle ABC` 内位于抛物线 :math:`y = -x^2 + 4x - 3` 之上的部分。
    因此所围成的图形的面积 :math:`S` 为

    .. math::

        S & = \int_0^{3/2} (4x - 3 - (-x^2 + 4x - 3)) \mathrm{d} x + \int_{3/2}^3 (-2x + 6 - (-x^2 + 4x - 3)) \mathrm{d} x \\
        & = \int_0^{3/2} x^2 \mathrm{d} x + \int_{3/2}^3 (x^2 - 6x + 9) \mathrm{d} x \\
        & = \left. \left( \dfrac{x^3}{3} \right) \right|_0^{3/2} + \left. \left( \dfrac{x^3}{3} - 3x^2 + 9x \right) \right|_{3/2}^3 \\
        & = \dfrac{9}{8} - 0 + \left( 9 - 27 + 27 - \dfrac{9}{8} + \dfrac{27}{4} - \dfrac{27}{2} \right) \\
        & = \dfrac{9}{8} + \dfrac{9}{8} = \dfrac{9}{4}.

4. 求摆线 :math:`x = a(t - \sin t), y = a(1 - \cos t)` 的一拱 :math:`(0 \leqslant t \leqslant 2\pi)` 所围成的图形的面积.

.. proof:solution::

    摆线长 :math:`\displaystyle \ell = \int_0^{2\pi} \sqrt{\left( \dfrac{\mathrm{d} x}{\mathrm{d} t} \right)^2 + \left( \dfrac{\mathrm{d} y}{\mathrm{d} t} \right)^2} \mathrm{d} t`, 因此有

    .. math::

        \ell & = \int_0^{2\pi} \sqrt{a^2 \left( 1 - \cos t \right)^2 + a^2 \sin^2 t} \mathrm{d} t = \int_0^{2\pi} a \sqrt{2 - 2 \cos t} \mathrm{d} t \\
        & = \int_0^{2\pi} a \sqrt{4 \sin^2 \frac{t}{2}} \mathrm{d} t = 2a \int_0^{2\pi} \sin \frac{t}{2} \mathrm{d} t = -4a \left. \cos \frac{t}{2} \right|_0^{2\pi} \\
        & = 8a.

6. 设抛物线 :math:`y^2 = 2x` 与直线 :math:`y = x - 4` 围成的平面区域为 :math:`D`,

(1). 求 :math:`D` 的面积；

(2). 求 :math:`D` 绕 :math:`x` 轴旋转一周所生成的旋转体体积.

.. proof:solution::

    (1). 抛物线 :math:`y^2 = 2x` 与直线 :math:`y = x - 4` 的交点为 :math:`A = (8, 4)`, :math:`B = (2, -2)`,
    因此所围成的图形为三角形 :math:`\triangle OAB` 内位于抛物线 :math:`y^2 = 2x` 以及直线 :math:`y = x - 4` 之间的部分。
    以 :math:`y` 为自变量，那么所围成的图形的面积 :math:`S` 为直线 :math:`x = y + 4` 之下，抛物线 :math:`x = \dfrac{y^2}{2}` 之上的部分：

    .. math::

        S_D & = \int_{-2}^4 \left( y + 4 - \dfrac{y^2}{2} \right) \mathrm{d} y = \left. \left( \dfrac{y^2}{2} + 4y - \dfrac{y^3}{6} \right) \right|_{-2}^4 \\
        & = 8 + 16 - \dfrac{64}{6} - \left( 2 - 8 + \dfrac{8}{6} \right) = 18.

    (2). 令点 :math:`E = (4, 0), F = (8, 0)`, 那么旋转体的体积等于曲线 :math:`y = \sqrt{2x}`, 直线 :math:`x = 8` 与 :math:`x` 轴所围成的图形绕
    :math:`x` 轴旋转一周所形成的旋转体的体积，减去以 :math:`EF` 为高的圆锥的体积，即

    .. math::

        V & = \pi \int_0^8 \left( \sqrt{2x} \right)^2 \mathrm{d} x - \dfrac{1}{3} \pi \cdot 4^2 \cdot 4 \\
        & = 2 \pi \int_0^8 x \mathrm{d} x - \dfrac{64}{3} \pi = \left. \pi x^2 \right|_0^8 - \dfrac{64}{3} \pi \\
        & = 64 \pi - \dfrac{64}{3} \pi = \dfrac{128}{3} \pi.

8. 求曲线 :math:`xy = 1` 与直线 :math:`x = 1, x = 2, y = 0` 所围成的平面区域绕 :math:`y` 轴旋转一周所形成的旋转体体积.

.. proof:solution::

    曲线 :math:`xy = 1` 与直线 :math:`x = 1, x = 2, y = 0` 所围成的平面区域绕 :math:`y` 轴旋转一周所形成的旋转体可以分为两部分。
    第一部分为曲线 :math:`x = \dfrac{1}{y}`, 直线 :math:`y = 1, y = \dfrac{1}{2}` 与 :math:`y` 轴所围成的曲边梯形绕
    :math:`y` 轴旋转一周所形成的旋转体减去矩形 :math:`[0, 1] \times [\frac{1}{2}, 1]` 绕 :math:`y` 轴旋转一周所形成的旋转体，其体积为

    .. math::

        S_1 & = \pi \int_{\frac{1}{2}}^1 \left( \dfrac{1}{y} \right)^2 \mathrm{d} y - \left( 1 - \dfrac{1}{2} \right) \cdot \pi \cdot 1^2 \\
        & = \pi \int_{\frac{1}{2}}^1 \dfrac{1}{y^2} \mathrm{d} y - \dfrac{\pi}{2} = \left. -\dfrac{\pi}{y} \right|_{\frac{1}{2}}^1 - \dfrac{\pi}{2} \\
        & = -\pi + 2 \pi - \dfrac{\pi}{2} \\
        & = \dfrac{\pi}{2}.

    第二部分为矩形 :math:`[1, 2] \times [0, \frac{1}{2}]` 绕 :math:`y` 轴旋转一周所形成的旋转体，其体积为

    .. math::

        S_2 = \dfrac{1}{2} \cdot \pi \cdot 2^2 - \dfrac{1}{2} \cdot \pi \cdot 1^2 = \dfrac{3\pi}{2}.

    所以所围成的图形的面积 :math:`S = S_1 + S_2 = \dfrac{\pi}{2} + \dfrac{3\pi}{2} = 2\pi`.

10. 设某水库的闸门为一等腰梯形，下底为 2m, 上底为 6m, 高为 10m. 当水库水齐闸门顶时，求闸门所受的水压力.

.. proof:solution::

    水深 :math:`h` 处的压强为 :math:`\rho g h`, 其中 :math:`\rho` 为水的密度， :math:`g` 为重力加速度。
    水深 :math:`h` 处闸门宽 :math:`w` 为 :math:`w = 6 - \dfrac{4}{10} h`, 因此闸门所受的水压力

    .. math::

        F & = \int_0^{10} \rho g h \cdot \left( 6 - \dfrac{4}{10} h \right) \mathrm{d} h = \rho g \int_0^{10} \left( 6h - \dfrac{4}{10} h^2 \right) \mathrm{d} h \\
        & = \rho g \left. \left( 3h^2 - \dfrac{4}{30} h^3 \right) \right|_0^{10} = \rho g \left( 300 - \dfrac{400}{3} \right) \\
        & = \dfrac{500}{3} \rho g.

§3.5 广义积分
---------------------

1. 计算下列广义积分：

(2). :math:`\displaystyle \int_2^{+\infty} \dfrac{x}{\sqrt{1 + x^2}} \mathrm{d} x`;

(4). :math:`\displaystyle \int_1^{+\infty} \dfrac{1}{\sqrt{x}(1 + x)} \mathrm{d} x`;

(6). :math:`\displaystyle \int_0^2 \dfrac{1}{(1 - x)^2} \mathrm{d} x`.

.. proof:solution::

    (2).

    .. math::

        \int_2^{+\infty} \dfrac{x}{\sqrt{1 + x^2}} \mathrm{d} x & = \dfrac{1}{2} \int_2^{+\infty} \dfrac{\mathrm{d} (1 + x^2)}{\sqrt{1 + x^2}} \\
        & = \left. \sqrt{1 + x^2} \right|_2^{+\infty} = +\infty.

    该广义积分发散.

    (4).

    .. math::

        \int_1^{+\infty} \dfrac{1}{\sqrt{x}(1 + x)} \mathrm{d} x & = 2 \int_1^{+\infty} \dfrac{\mathrm{d} \sqrt{x}}{1 + \left( \sqrt{x} \right)^2} = 2 \cdot \left. \arctan \sqrt{x} \right|_1^{+\infty} \\
        & = 2 \cdot \left( \dfrac{\pi}{2} - \dfrac{\pi}{4} \right) = \dfrac{\pi}{2}.

    (6).

    .. math::

        \int_0^2 \dfrac{1}{(1 - x)^2} \mathrm{d} x & = \int_0^1 \dfrac{1}{(1 - x)^2} \mathrm{d} x + \int_1^2 \dfrac{1}{(1 - x)^2} \mathrm{d} x \\
        & = \left. \dfrac{1}{1 - x} \right|_0^1 + \left. \dfrac{1}{1 - x} \right|_1^2.

    该广义积分发散.

2. 讨论广义积分 :math:`\displaystyle \int_2^{+\infty} \dfrac{1}{x (\ln x)^k} \mathrm{d} x` 的敛散性，若收敛，求其值. 又当 :math:`k` 为何值时，该广义积分取得最小值.

.. proof:solution::

    由于

    .. math::

        \int_2^{+\infty} \dfrac{1}{x (\ln x)^k} \mathrm{d} x = \int_2^{+\infty} \dfrac{\mathrm{d} (\ln x)}{(\ln x)^k} = \begin{cases} \left. \dfrac{1}{(1 - k)(\ln x)^{k - 1}} \right|_2^{+\infty}, & k \neq 1 \\ \left. \dfrac{1}{\ln x} \right|_2^{+\infty}, & k = 1 \end{cases}

    所以当 :math:`k > 1` 时，该广义积分收敛，值为 :math:`\dfrac{1}{(k - 1)(\ln 2)^{k - 1}}`; 当 :math:`k \leqslant 1` 时，该广义积分发散.

    令 :math:`f(k) = (k - 1)(\ln 2)^{k - 1}, k > 1`, 那么

    .. math::

        f'(k) = (\ln 2)^{k - 1} + (k - 1)(\ln 2)^{k - 1} \cdot \ln \ln 2 = (\ln 2)^{k - 1} \left( 1 + (k - 1) \ln \ln 2 \right).

    由于 :math:`\ln 2 \in (0, 1)`, :math:`\ln \ln 2 < 0`, 令 :math:`f'(k) = 0` 解得 :math:`k = 1 - \dfrac{1}{\ln \ln 2}`.
    当 :math:`1 < k < 1 - \dfrac{1}{\ln \ln 2}` 时， :math:`f'(k) > 0`; 当 :math:`k > 1 - \dfrac{1}{\ln \ln 2}` 时， :math:`f'(k) < 0`,
    因此当 :math:`k = 1 - \dfrac{1}{\ln \ln 2}` 时， :math:`f(k)` 取得极大值. 它是 :math:`f(k)` 唯一的极大值点，因此是其最大值点，
    从而是该广义积分的最小值点.

3. 设 :math:`\displaystyle f(x) = \begin{cases} \lambda e^{-\lambda x}, & x \geqslant 0 \\ 0, & x < 0 \end{cases}`, 其中 :math:`\lambda > 0`, 试求 :math:`\displaystyle \int_{-\infty}^{+\infty} xf(x) \mathrm{d} x` 与 :math:`\displaystyle \int_{-\infty}^{+\infty} x^2 f(x) \mathrm{d} x`.

.. proof:solution::

    .. math::

        \int_{-\infty}^{+\infty} xf(x) \mathrm{d} x & = \int_0^{+\infty} x \cdot \lambda e^{-\lambda x} \mathrm{d} x = - \int_0^{+\infty} x \mathrm{d} e^{-\lambda x} \\
        & = - \left. x e^{-\lambda x} \right|_0^{+\infty} + \int_0^{+\infty} e^{-\lambda x} \mathrm{d} x \\
        & = \left. - \dfrac{1}{\lambda} e^{-\lambda x} \right|_0^{+\infty} = \dfrac{1}{\lambda}.

    .. math::

        \int_{-\infty}^{+\infty} x^2 f(x) \mathrm{d} x & = \int_0^{+\infty} x^2 \cdot \lambda e^{-\lambda x} \mathrm{d} x = - \int_0^{+\infty} x^2 \mathrm{d} e^{-\lambda x} \\
        & = - \left. x^2 e^{-\lambda x} \right|_0^{+\infty} + \int_0^{+\infty} 2x e^{-\lambda x} \mathrm{d} x \\
        & = \dfrac{2}{\lambda} \int_{-\infty}^{+\infty} xf(x) \mathrm{d} x \\
        & = \dfrac{2}{\lambda^2}.
