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

(15). :math:`\displaystyle \int x (2x - 3)^10 \mathrm{d} x`;

(17). :math:`\displaystyle \int \dfrac{1}{x^2 \sqrt{1 + x^2}} \mathrm{d} x`.

.. proof:solution::

    (1). 令 :math:`u = 2x - 5`, 则 :math:`\mathrm{d} u = 2 \mathrm{d} x`, 从而有

    .. math::

        \int \dfrac{1}{(2x - 5)^{10}} \mathrm{d} x & = \dfrac{1}{2} \int u^{-10} \mathrm{d} u = \dfrac{1}{2} \cdot \dfrac{u^{-9}}{-9} + C \\
        & = -\dfrac{1}{18(2x - 5)^9} + C.

    接下来，中间变量 :math:`u` 就不再写出了。

    (3).

    .. math::

        \int \dfrac{x}{\sqrt{1 + x^2}} \mathrm{d} x = \int \dfrac{\sqrt{1 + x^2}}{2} \mathrm{d} (1 + x^2) = \dfrac{\sqrt{1 + x^2}}{2} + C.

    (5).

    .. math::

        \int x^2 e^{2x^3} \mathrm{d} x = \dfrac{1}{6} \int e^{2x^3} \mathrm{d} (2x^3) = \dfrac{1}{6} e^{2x^3} + C.

    (7).

    .. math::

        \int \dfrac{\sqrt{1 + 3\ln x}}{x} \mathrm{d} x = \int \sqrt{1 + 3\ln x} \mathrm{d} (\ln x) = \dfrac{2}{3} (1 + 3\ln x)^{\frac{3}{2}} + C.

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

        \int x (2x - 3)^10 \mathrm{d} x & = \int \dfrac{1}{2} (2x - 3)^11 \mathrm{d} x + \int \dfrac{3}{2} (2x - 3)^10 \mathrm{d} x \\
        & = \dfrac{1}{4} \int (2x - 3)^11 \mathrm{d} (2x - 3) + \dfrac{3}{4} \int (2x - 3)^10 \mathrm{d} (2x - 3) \\
        & = \dfrac{1}{4} \cdot \dfrac{(2x - 3)^12}{12} + \dfrac{3}{4} \cdot \dfrac{(2x - 3)^11}{11} + C \\
        & = \dfrac{1}{48} (2x - 3)^12 + \dfrac{3}{44} (2x - 3)^11 + C.

    (17).

    .. math::

        \int \dfrac{1}{x^2 \sqrt{1 + x^2}} \mathrm{d} x & = -\int \dfrac{1}{\sqrt{1 + x^2}} \mathrm{d} \left( \dfrac{1}{x} \right) = -\int \dfrac{1}{x} \cdot \dfrac{1}{\sqrt{1 + \left(\frac{1}{x}\right)^2}} \mathrm{d} \left( \dfrac{1}{x} \right) \\
        & = -\dfrac{1}{2} \int \dfrac{1}{\sqrt{1 + \left(\frac{1}{x}\right)^2}} \mathrm{d} \left( \frac{1}{x} \right)^2 \\
        & = -\sqrt{1 + \left(\frac{1}{x}\right)^2} + C.

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

    (6).

    .. math::

        \int \ln(1 + x^2) \mathrm{d} x & = x \ln(1 + x^2) - \int x \mathrm{d} (\ln(1 + x^2)) = x \ln(1 + x^2) - \int x \cdot \dfrac{2x}{1 + x^2} \mathrm{d} x \\
        & = x \ln(1 + x^2) - 2 \int \dfrac{x^2}{1 + x^2} \mathrm{d} x = x \ln(1 + x^2) - 2 \int \left( 1 - \dfrac{1}{1 + x^2} \right) \mathrm{d} x \\
        & = x \ln(1 + x^2) - 2x + 2 \arctan x + C.

    (8).

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
        & = \int \dfrac{\mathrm{d} \tan x}{3 + 4\tan^2 x} = \dfrac{\sqrt{3}}{2} \int \dfrac{\mathrm{d} \left( \frac{2}{\sqrt{3}} \tan x \right)}{1 + \left( \frac{2}{\sqrt{3}} \tan x \right)^2} \\
        & = \dfrac{\sqrt{3}}{2} \arctan \left( \dfrac{2}{\sqrt{3}} \tan x \right) + C.

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

§3.3 定积分的计算
---------------------

§3.4 定积分的应用
---------------------

§3.5 广义积分
---------------------
