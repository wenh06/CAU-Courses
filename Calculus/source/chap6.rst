第六章  定积分及其应用
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. contents:: :local:


.. _ex-chap6:

课后习题解答
====================================

.. _ex-chap6-sec1:

§6.1 定积分的概念
------------------------------------

.. _ex-chap6-sec1-ex1:

1. 利用定积分的定义计算定积分 :math:`\displaystyle \int_0^1 (x^2 + 1) ~ \mathrm{d}x`.

.. proof:solution::

   将 :math:`[0, 1]` 分成 :math:`n` 等份, 取第 :math:`i` 个小区间的右端点 :math:`\xi_i = \dfrac{i}{n}`, 则
   :math:`\Delta x_i = \dfrac{1}{n}`, 由定积分的定义,

   .. math::
      \int_0^1 (x^2 + 1) ~ \mathrm{d}x
      = \lim_{n \to \infty} \sum_{i=1}^{n} \left[ \left( \dfrac{i}{n} \right)^2 + 1 \right] \dfrac{1}{n}
      = \lim_{n \to \infty} \left[ \dfrac{1}{n^3} \sum_{i=1}^{n} i^2 + \dfrac{1}{n} \sum_{i=1}^{n} 1 \right].

   利用 :math:`\displaystyle \sum_{i=1}^{n} i^2 = \dfrac{n(n+1)(2n+1)}{6}`, 得

   .. math::
      \int_0^1 (x^2 + 1) ~ \mathrm{d}x
      = \lim_{n \to \infty} \left[ \dfrac{(n+1)(2n+1)}{6n^2} + 1 \right]
      = \dfrac{1}{3} + 1 = \dfrac{4}{3}.

.. _ex-chap6-sec1-ex2:

2. 设函数 :math:`f(x)` 在区间 :math:`[0, 1]` 上连续, 则 :math:`\displaystyle \int_0^1 f(x) ~ \mathrm{d}x`
   可以表示成下面哪个极限.

   (1) :math:`\displaystyle \lim_{n \to \infty} \sum_{i=1}^{n} f \left( \dfrac{2i - 1}{2n} \right) \dfrac{1}{2n}`; \qquad
   (2) :math:`\displaystyle \lim_{n \to \infty} \sum_{i=1}^{n} f \left( \dfrac{2i - 1}{2n} \right) \dfrac{1}{n}`;

   (3) :math:`\displaystyle \lim_{n \to \infty} \sum_{i=1}^{2n} f \left( \dfrac{i - 1}{2n} \right) \dfrac{1}{n}`; \qquad
   (4) :math:`\displaystyle \lim_{n \to \infty} \sum_{i=1}^{2n} f \left( \dfrac{i}{2n} \right) \dfrac{2}{n}`.

.. proof:solution::

   答案: (2).

   (2) 中取 :math:`\xi_i = \dfrac{2i-1}{2n}`, 它恰是小区间 :math:`\left[ \dfrac{i-1}{n}, \dfrac{i}{n} \right]` 的中点,
   :math:`\Delta x_i = \dfrac{1}{n}`, 因此该和式是 :math:`f(x)` 在 :math:`[0, 1]` 上的一个黎曼和
   (中点矩形和), 其极限为 :math:`\displaystyle \int_0^1 f(x) ~ \mathrm{d}x`.

   其余三项都不是 :math:`\displaystyle \int_0^1 f(x) ~ \mathrm{d}x`: (1) 中小区间宽度为 :math:`\dfrac{1}{2n}` 而
   取点范围为 :math:`\left[ 0, \dfrac{1}{2} \right]`, 极限是 :math:`\displaystyle \int_0^{\frac{1}{2}} f(x) ~ \mathrm{d}x`;
   (3) 与 (4) 中, 和式可分别写成

   .. math::
      \sum_{i=1}^{2n} f \left( \dfrac{i - 1}{2n} \right) \dfrac{1}{n} = 2 \sum_{i=1}^{2n} f \left( \dfrac{i-1}{2n} \right) \dfrac{1}{2n}, \qquad
      \sum_{i=1}^{2n} f \left( \dfrac{i}{2n} \right) \dfrac{2}{n} = 2 \sum_{i=1}^{2n} f \left( \dfrac{i}{2n} \right) \dfrac{1}{2n},

   方括号内分别是 :math:`\displaystyle \int_0^1 f(x) ~ \mathrm{d}x` 的左端点与右端点黎曼和, 故两者的极限都是
   :math:`2 \displaystyle \int_0^1 f(x) ~ \mathrm{d}x`, 而非所求.

.. _ex-chap6-sec1-ex3:

3. 利用定积分的几何意义, 计算下列各定积分的值.

   (1) :math:`\displaystyle \int_{-1}^{6} 2 ~ \mathrm{d}x`; \qquad
   (2) :math:`\displaystyle \int_0^3 2x ~ \mathrm{d}x`;

   (3) :math:`\displaystyle \int_{-\sqrt{3}}^{\sqrt{3}} \sqrt{3 - x^2} ~ \mathrm{d}x`; \qquad
   (4) :math:`\displaystyle \int_1^2 \left( 1 - \sqrt{2x - x^2} \right) \mathrm{d}x`.

.. proof:solution::

   (1). 被积函数恒为 :math:`2`, 积分是以 :math:`7` 为底、高为 :math:`2` 的矩形面积:

   .. math::
      \int_{-1}^{6} 2 ~ \mathrm{d}x = 2 \times 7 = 14.

   (2). :math:`y = 2x` 与 :math:`x` 轴在 :math:`[0, 3]` 上围成底为 :math:`3`、高为 :math:`6` 的三角形:

   .. math::
      \int_0^3 2x ~ \mathrm{d}x = \dfrac{1}{2} \times 3 \times 6 = 9.

   (3). :math:`y = \sqrt{3 - x^2}` 是上半圆 :math:`x^2 + y^2 = 3 ~ (y \geqslant 0)`, 半径 :math:`\sqrt{3}`,
   积分为该半圆的面积:

   .. math::
      \int_{-\sqrt{3}}^{\sqrt{3}} \sqrt{3 - x^2} ~ \mathrm{d}x = \dfrac{1}{2} \pi \left( \sqrt{3} \right)^2 = \dfrac{3\pi}{2}.

   (4). :math:`\sqrt{2x - x^2} = \sqrt{1 - (x-1)^2}` 是以 :math:`(1, 0)` 为圆心、半径为 :math:`1` 的上半圆;
   它在 :math:`[1, 2]` 上对应的图形是四分之一圆, 面积 :math:`\dfrac{\pi}{4}`, 而矩形 :math:`[1, 2] \times [0, 1]`
   面积为 :math:`1`, 故所求为两者之差:

   .. math::
      \int_1^2 \left( 1 - \sqrt{2x - x^2} \right) \mathrm{d}x = 1 - \dfrac{\pi}{4}.

.. _ex-chap6-sec1-ex4:

4. 用定积分表示下列和式极限.

   (1) :math:`\displaystyle \lim_{n \to \infty} \dfrac{1}{n^4} \left( 1 + 2^3 + \cdots + n^3 \right)`;

   (2) :math:`\displaystyle \lim_{n \to \infty} n \left[ \dfrac{1}{(n + 1)^2} + \dfrac{1}{(n + 2)^2} + \cdots + \dfrac{1}{(n + n)^2} \right]`;

   (3) :math:`\displaystyle \lim_{n \to \infty} \left( \dfrac{1}{\sqrt{n^2 - 1^2}} + \dfrac{1}{\sqrt{n^2 - 2^2}} + \cdots
       + \dfrac{1}{\sqrt{n^2 - (n - 1)^2}} \right)`.

.. proof:solution::

   把每个和式都凑成黎曼和 :math:`\displaystyle \sum \frac{1}{n} f\left( \frac{i}{n} \right)` 的形状:

   (1). :math:`\displaystyle \sum_{i=1}^{n} \dfrac{i^3}{n^4} = \sum_{i=1}^{n} \left( \dfrac{i}{n} \right)^3 \cdot \dfrac{1}{n}`, 故

   .. math::
      \lim_{n \to \infty} \dfrac{1}{n^4} \left( 1 + 2^3 + \cdots + n^3 \right)
      = \int_0^1 x^3 ~ \mathrm{d}x = \dfrac{1}{4}.

   (2). :math:`\displaystyle \sum_{i=1}^{n} \dfrac{n}{(n+i)^2} = \sum_{i=1}^{n} \dfrac{1}{\left( 1 + \frac{i}{n} \right)^2} \cdot \dfrac{1}{n}`, 故

   .. math::
      \lim_{n \to \infty} n \left[ \dfrac{1}{(n+1)^2} + \cdots + \dfrac{1}{(n+n)^2} \right]
      = \int_0^1 \dfrac{\mathrm{d}x}{(1 + x)^2}
      = \left[ -\dfrac{1}{1+x} \right]_0^1 = \dfrac{1}{2}.

   (3). :math:`\displaystyle \sum_{k=1}^{n-1} \dfrac{1}{\sqrt{n^2 - k^2}} = \sum_{k=1}^{n-1} \dfrac{1}{\sqrt{1 - \left( \frac{k}{n} \right)^2}} \cdot \dfrac{1}{n}`, 故

   .. math::
      \lim_{n \to \infty} \left( \dfrac{1}{\sqrt{n^2 - 1^2}} + \cdots + \dfrac{1}{\sqrt{n^2 - (n-1)^2}} \right)
      = \int_0^1 \dfrac{\mathrm{d}x}{\sqrt{1 - x^2}}
      = \left[ \arcsin x \right]_0^1 = \dfrac{\pi}{2}.

.. _ex-chap6-sec2:

§6.2 定积分的性质
------------------------------------

.. _ex-chap6-sec2-ex1:

1. 不计算积分, 试比较下列定积分的大小.

   (1) :math:`\displaystyle \int_0^1 x ~ \mathrm{d}x` 与 :math:`\displaystyle \int_0^1 x^2 ~ \mathrm{d}x`; \qquad
   (2) :math:`\displaystyle \int_0^{\frac{\pi}{4}} \dfrac{\tan x}{x} ~ \mathrm{d}x` 与
       :math:`\displaystyle \int_0^{\frac{\pi}{4}} \dfrac{x}{\tan x} ~ \mathrm{d}x`.

.. proof:solution::

   (1). 当 :math:`0 \leqslant x \leqslant 1` 时, :math:`x \geqslant x^2`, 且除端点 :math:`x = 0, 1` 外严格成立.
   由定积分的保序性, :math:`\displaystyle \int_0^1 x ~ \mathrm{d}x > \int_0^1 x^2 ~ \mathrm{d}x`.

   (2). 当 :math:`0 < x \leqslant \dfrac{\pi}{4}` 时, :math:`\tan x > x` (由 :math:`(\tan x - x)' = \tan^2 x > 0` 且
   :math:`\tan 0 - 0 = 0`), 于是 :math:`\dfrac{\tan x}{x} > 1 > \dfrac{x}{\tan x}`. 由保序性,

   .. math::
      \int_0^{\frac{\pi}{4}} \dfrac{\tan x}{x} ~ \mathrm{d}x > \int_0^{\frac{\pi}{4}} \dfrac{x}{\tan x} ~ \mathrm{d}x.

.. _ex-chap6-sec2-ex2:

2. 估计下列定积分的值.

   (1) :math:`\displaystyle \int_1^2 (2x^2 - 1) ~ \mathrm{d}x`; \qquad
   (2) :math:`\displaystyle \int_2^0 e^{-x^2} ~ \mathrm{d}x`;

   (3) :math:`\displaystyle \int_{\frac{1}{\sqrt{3}}}^{\sqrt{3}} x^2 \arctan x ~ \mathrm{d}x`; \qquad
   (4) :math:`\displaystyle \int_0^2 \dfrac{5 - x}{9 - x^2} ~ \mathrm{d}x`.

.. proof:solution::

   利用估值定理 :math:`m(b-a) \leqslant \displaystyle \int_a^b f(x) ~ \mathrm{d}x \leqslant M(b-a)`:

   (1). :math:`2x^2 - 1` 在 :math:`[1, 2]` 上单调增加, 最小值 :math:`1`, 最大值 :math:`7`, 区间长度为 :math:`1`, 故

   .. math::
      1 \leqslant \int_1^2 (2x^2 - 1) ~ \mathrm{d}x \leqslant 7.

   (2). :math:`\displaystyle \int_2^0 e^{-x^2} ~ \mathrm{d}x = - \int_0^2 e^{-x^2} ~ \mathrm{d}x`. 而
   :math:`e^{-x^2}` 在 :math:`[0, 2]` 上单调减少, 最大值 :math:`1`, 最小值 :math:`e^{-4}`, 故

   .. math::
      -2 \leqslant \int_2^0 e^{-x^2} ~ \mathrm{d}x \leqslant -2e^{-4}.

   (3). :math:`x^2 \arctan x` 在 :math:`\left[ \frac{1}{\sqrt{3}}, \sqrt{3} \right]` 上单调增加
   (两个因子都正且单调增加), 最小值 :math:`\dfrac{1}{3} \cdot \dfrac{\pi}{6} = \dfrac{\pi}{18}`, 最大值
   :math:`3 \cdot \dfrac{\pi}{3} = \pi`, 区间长度 :math:`\sqrt{3} - \dfrac{1}{\sqrt{3}} = \dfrac{2}{\sqrt{3}}`, 故

   .. math::
      \dfrac{\pi}{18} \cdot \dfrac{2}{\sqrt{3}} \leqslant \int_{\frac{1}{\sqrt{3}}}^{\sqrt{3}} x^2 \arctan x ~ \mathrm{d}x
      \leqslant \pi \cdot \dfrac{2}{\sqrt{3}},
      \qquad \text{即} ~ \dfrac{\sqrt{3}\pi}{27} \leqslant \int \leqslant \dfrac{2\sqrt{3}\pi}{3}.

   (4). :math:`f(x) = \dfrac{5 - x}{9 - x^2}` 的导数 :math:`f'(x) = \dfrac{-x^2 + 10x - 9}{(9 - x^2)^2}`:
   在 :math:`[0, 1]` 上 :math:`f' < 0` (减少), 在 :math:`[1, 2]` 上 :math:`f' > 0` (增加), 故最小值
   :math:`f(1) = \dfrac{1}{2}`; 比较两端点 :math:`f(0) = \dfrac{5}{9}` 与 :math:`f(2) = \dfrac{3}{5}`,
   最大值为 :math:`\dfrac{3}{5}`. 区间长度 :math:`2`, 故

   .. math::
      1 \leqslant \int_0^2 \dfrac{5 - x}{9 - x^2} ~ \mathrm{d}x \leqslant \dfrac{6}{5}.

.. _ex-chap6-sec2-ex3:

3. 证明下列不等式.

   (1) :math:`\dfrac{2}{5} \leqslant \displaystyle \int_1^2 \dfrac{x}{1 + x^2} ~ \mathrm{d}x \leqslant \dfrac{1}{2}`; \qquad
   (2) :math:`1 \leqslant \displaystyle \int_0^1 e^{x^2} ~ \mathrm{d}x \leqslant e`;

   (3) :math:`1 \leqslant \displaystyle \int_0^{\frac{\pi}{3}} \dfrac{\sin x}{x} ~ \mathrm{d}x \leqslant \dfrac{\pi}{2}`.

.. proof:solution::

   .. note::
      题面按印刷原文给出, 但按 :math:`\dfrac{\pi}{3}` 计算时下界不成立:
      :math:`\displaystyle \int_0^{\frac{\pi}{3}} \dfrac{\sin x}{x} ~ \mathrm{d}x \approx 0.985 < 1`.
      正确的上限应为 :math:`\dfrac{\pi}{2}` (此时上下界 :math:`1` 与 :math:`\dfrac{\pi}{2}` 恰由下面两个
      经典不等式给出). 下面按修正后的题目证明
      :math:`1 \leqslant \displaystyle \int_0^{\frac{\pi}{2}} \dfrac{\sin x}{x} ~ \mathrm{d}x \leqslant \dfrac{\pi}{2}`.

   下界: 由若尔当 (Jordan) 不等式, 当 :math:`0 \leqslant x \leqslant \dfrac{\pi}{2}` 时 :math:`\sin x \geqslant \dfrac{2}{\pi} x`
   (:math:`\sin x` 在 :math:`\left[ 0, \frac{\pi}{2} \right]` 上向下凸, 图像位于连接 :math:`(0,0)` 与
   :math:`\left( \frac{\pi}{2}, 1 \right)` 的弦之上), 于是

   .. math::
      \int_0^{\frac{\pi}{2}} \dfrac{\sin x}{x} ~ \mathrm{d}x \geqslant \int_0^{\frac{\pi}{2}} \dfrac{2}{\pi} ~ \mathrm{d}x = 1.

   上界: 当 :math:`x > 0` 时 :math:`\sin x < x`, 故 :math:`\dfrac{\sin x}{x} < 1`, 从而

   .. math::
      \int_0^{\frac{\pi}{2}} \dfrac{\sin x}{x} ~ \mathrm{d}x < \int_0^{\frac{\pi}{2}} ~ \mathrm{d}x = \dfrac{\pi}{2}.

.. _ex-chap6-sec2-ex4:

4. 计算定积分 :math:`\displaystyle \int_{-1}^1 \lvert x \rvert ~ \mathrm{sgn}(x + 1) ~ \mathrm{d}x`.

.. proof:solution::

   当 :math:`x \in (-1, 1]` 时, :math:`x + 1 > 0`, 故 :math:`\operatorname{sgn}(x+1) = 1`
   (仅在 :math:`x = -1` 一点处取值 :math:`0`, 不影响积分值). 于是

   .. math::
      \int_{-1}^1 \lvert x \rvert ~ \operatorname{sgn}(x + 1) ~ \mathrm{d}x
      = \int_{-1}^1 \lvert x \rvert ~ \mathrm{d}x
      = 2 \int_0^1 x ~ \mathrm{d}x = 1.

.. _ex-chap6-sec2-ex5:

5. 已知 :math:`I_1 = \displaystyle \int_0^1 \dfrac{x}{2(1 + \cos x)} ~ \mathrm{d}x`,
   :math:`I_2 = \displaystyle \int_0^1 \dfrac{\ln(1 + x)}{1 + \cos x} ~ \mathrm{d}x`,
   :math:`I_3 = \displaystyle \int_0^1 \dfrac{2x}{1 + \sin x} ~ \mathrm{d}x`, 试比较 :math:`I_1`, :math:`I_2`,
   :math:`I_3` 的大小.

.. proof:solution::

   比较 :math:`I_1` 与 :math:`I_2`: 当 :math:`0 < x < 1` 时 :math:`\ln(1 + x) > \dfrac{x}{2}`
   (令 :math:`g(x) = \ln(1+x) - \frac{x}{2}`, :math:`g'(x) = \dfrac{2}{1+x} \cdot \dfrac{1}{2} - \dfrac{1}{2} = \dfrac{1-x}{2(1+x)} > 0`,
   :math:`g(0) = 0`), 且两积分的分母相同, 故被积函数 :math:`\dfrac{\ln(1+x)}{1+\cos x} > \dfrac{x}{2(1+\cos x)}`,
   从而 :math:`I_2 > I_1`.

   比较 :math:`I_2` 与 :math:`I_3`: 由 :math:`\ln(1+x) \leqslant x` (:math:`x > 0`, 见 :ref:`§4.6 题5(2) <ex-chap4_sec6-ex5>`),

   .. math::
      \dfrac{\ln(1+x)}{1 + \cos x} \leqslant \dfrac{x}{1 + \cos x}.

   又当 :math:`x > 0` 时 :math:`\sin x < 1 < 1 + 2 \cos x`, 即 :math:`1 + \sin x < 2(1 + \cos x)`, 于是

   .. math::
      \dfrac{x}{1 + \cos x} < \dfrac{2x}{1 + \sin x}.

   因此 :math:`I_3` 的被积函数恒大于 :math:`I_2` 的被积函数, 即 :math:`I_3 > I_2`.

   综上 :math:`I_1 < I_2 < I_3`. (数值印证: :math:`I_1 \approx 0.143`, :math:`I_2 \approx 0.219`, :math:`I_3 \approx 0.632`.)

.. _ex-chap6-sec2-ex6:

6. 计算下列函数在指定区间上的平均值.

   (1) :math:`f(x) = \sqrt{1 - x^2}`, :math:`[0, 1]`; \qquad
   (2) :math:`f(x) = x^2`, :math:`[1, 5]`.

.. proof:solution::

   平均值公式 :math:`\bar{f} = \dfrac{1}{b - a} \displaystyle \int_a^b f(x) ~ \mathrm{d}x`:

   (1). :math:`\displaystyle \int_0^1 \sqrt{1 - x^2} ~ \mathrm{d}x` 是半径为 :math:`1` 的四分之一圆的面积
   :math:`\dfrac{\pi}{4}`, 故

   .. math::
      \bar{f} = \dfrac{1}{1 - 0} \cdot \dfrac{\pi}{4} = \dfrac{\pi}{4}.

   (2). :math:`\displaystyle \int_1^5 x^2 ~ \mathrm{d}x = \left[ \dfrac{x^3}{3} \right]_1^5 = \dfrac{125 - 1}{3} = \dfrac{124}{3}`, 故

   .. math::
      \bar{f} = \dfrac{1}{5 - 1} \cdot \dfrac{124}{3} = \dfrac{31}{3}.

.. _ex-chap6-sec2-ex7:

7. 已知函数 :math:`f(x)` 在区间 :math:`[0,1]` 上具有 2 阶导数, 且 :math:`f(0) = 0`, :math:`f(1) = 1`,
   :math:`\displaystyle \int_0^1 f(x) ~ \mathrm{d}x = 1`, 试证明:
   (1) 存在 :math:`\xi \in (0, 1)`, 使得 :math:`f'(\xi) = 0`;
   (2) 存在 :math:`\eta \in (0, 1)`, 使得 :math:`f''(\eta) < -2`.

.. proof:solution::

   (1) 由积分中值定理, 存在 :math:`x_0 \in (0, 1)`, 使得

   .. math::
      1 = \int_0^1 f(x) ~ \mathrm{d}x = f(x_0) (1 - 0) = f(x_0).

   又由于 :math:`f(1) = 1`, 由罗尔定理, 存在 :math:`\xi \in (x_0, 1) \subset (0, 1)`, 使得 :math:`f'(\xi) = 0`.

   (2) 令 :math:`g(x) = f(x) + x^2`, 希望证明 :math:`g''(x) = f''(x) + 2 < 0` 在某点成立.

   若能证明存在 :math:`x_1 < x_2 \in (0, 1)`, 使得 :math:`g'(x_1) > g'(x_2)`, 则由拉格朗日中值定理,
   存在 :math:`\eta \in (x_1, x_2) \subset (0, 1)`, 使得 :math:`g''(\eta) < 0`, 即 :math:`f''(\eta) < -2`.

   下证存在这样的 :math:`x_1, x_2`. 对 (1) 中的 :math:`x_0`, 在区间 :math:`[0, x_0]` 以及 :math:`[x_0, 1]` 上分别应用拉格朗日中值定理,
   则存在 :math:`x_1 \in (0, x_0)`, :math:`x_2 \in (x_0, 1)`, 使得

   .. math::
      g'(x_1) & = \frac{g(x_0) - g(0)}{x_0 - 0} = \frac{f(x_0) + x_0^2}{x_0} = \frac{1}{x_0} + x_0, \\
      g'(x_2) & = \frac{g(1) - g(x_0)}{1 - x_0} = \frac{2 - (f(x_0) + x_0^2)}{1 - x_0} = \frac{1 - x_0^2}{1 - x_0} = 1 + x_0.

   因为 :math:`0 < x_0 < 1`, 所以 :math:`\dfrac{1}{x_0} + x_0 > 1 + x_0`, 即 :math:`g'(x_1) > g'(x_2)`, 证毕.

.. _ex-chap6-sec3:

§6.3 微积分基本定理
------------------------------------

.. _ex-chap6-sec3-ex1:

1. 计算下列函数 :math:`y` 的导数 :math:`\dfrac{\mathrm{d}y}{\mathrm{d}x}`.

   (1) :math:`\displaystyle y = \int_x^{\pi} \sin(1 + t^2) ~ \mathrm{d}t`; \qquad
   (2) :math:`\displaystyle y = \int_0^{\sqrt{x}} \cos t^2 ~ \mathrm{d}t`;

   (3) :math:`\displaystyle y = \int_{\sin x}^{\cos x} e^{t^2} ~ \mathrm{d}t`; \qquad
   (4) :math:`\displaystyle y = \int_0^x x \tan t ~ \mathrm{d}t`;

   (5) :math:`\begin{cases} \displaystyle x = \int_0^t \sin u ~ \mathrm{d}u, \\[1ex]
       \displaystyle y = \int_0^t \cos u ~ \mathrm{d}u; \end{cases}` \qquad
   (6) :math:`\displaystyle \int_0^y e^{-t^2} ~ \mathrm{d}t + \int_0^x \cos t^2 ~ \mathrm{d}t = 0`.

.. proof:solution::

   变限积分求导公式: :math:`\dfrac{\mathrm{d}}{\mathrm{d}x} \displaystyle \int_a^{\varphi(x)} f(t) ~ \mathrm{d}t = f\left( \varphi(x) \right) \varphi'(x)`.

   (1). :math:`y = \displaystyle \int_x^{\pi} \sin(1+t^2) ~ \mathrm{d}t = -\int_{\pi}^{x} \sin(1+t^2) ~ \mathrm{d}t`, 故

   .. math::
      \dfrac{\mathrm{d}y}{\mathrm{d}x} = -\sin(1 + x^2).

   (2). 上限为 :math:`\varphi(x) = \sqrt{x}`, :math:`\varphi'(x) = \dfrac{1}{2\sqrt{x}}`:

   .. math::
      \dfrac{\mathrm{d}y}{\mathrm{d}x} = \cos\left( \sqrt{x} \right)^2 \cdot \dfrac{1}{2\sqrt{x}} = \dfrac{\cos x}{2 \sqrt{x}}.

   (3). 上下限都含 :math:`x`, 拆成两项相减:

   .. math::
      \dfrac{\mathrm{d}y}{\mathrm{d}x} = e^{\cos^2 x} \cdot (-\sin x) - e^{\sin^2 x} \cdot \cos x.

   (4). 被积函数中的 :math:`x` 与积分变量 :math:`t` 无关, 可先提出:

   .. math::
      y = x \int_0^x \tan t ~ \mathrm{d}t, \qquad
      \dfrac{\mathrm{d}y}{\mathrm{d}x} = \int_0^x \tan t ~ \mathrm{d}t + x \tan x = -\ln \left\lvert \cos x \right\rvert + x \tan x.

   (5). :math:`\dfrac{\mathrm{d}x}{\mathrm{d}t} = \sin t`, :math:`\dfrac{\mathrm{d}y}{\mathrm{d}t} = \cos t`, 故

   .. math::
      \dfrac{\mathrm{d}y}{\mathrm{d}x} = \dfrac{\cos t}{\sin t} = \cot t.

   (6). 方程两边对 :math:`x` 求导 (:math:`y` 是 :math:`x` 的函数), 得

   .. math::
      e^{-y^2} \cdot y' + \cos(x^2) = 0, \qquad \text{解得} ~ y' = -e^{y^2} \cos(x^2).

.. _ex-chap6-sec3-ex2:

2. 计算下列极限.

   (1) :math:`\displaystyle \lim_{x \to 0^+} \dfrac{\int_0^{x^2} \sqrt{t} ~ e^{t^2} ~ \mathrm{d}t}{2x^3}`; \qquad
   (2) :math:`\displaystyle \lim_{x \to 0} \dfrac{\int_0^{x^2} t^{\frac{3}{2}} ~ \mathrm{d}t}
       {\int_0^x t (t - \sin t) ~ \mathrm{d}t}`.

.. proof:solution::

   两者都是 :math:`\dfrac{0}{0}` 型, 用洛必达法则 (结合变限积分求导).

   (1). 分子求导: :math:`\sqrt{x^2}\, e^{x^4} \cdot 2x = 2x^2 e^{x^4}` (:math:`x \to 0^+` 时 :math:`\sqrt{x^2} = x`), 于是

   .. math::
      \lim_{x \to 0^+} \dfrac{\int_0^{x^2} \sqrt{t}\, e^{t^2} ~ \mathrm{d}t}{2x^3}
      = \lim_{x \to 0^+} \dfrac{2x^2 e^{x^4}}{6x^2}
      = \lim_{x \to 0^+} \dfrac{e^{x^4}}{3} = \dfrac{1}{3}.

   (2). 分子 :math:`\displaystyle \int_0^{x^2} t^{\frac{3}{2}} ~ \mathrm{d}t = \dfrac{2}{5} x^5` 可先算出;
   分母求导得 :math:`x(x - \sin x)`, 用等价无穷小 :math:`x - \sin x \sim \dfrac{x^3}{6}`. 用洛必达法则:

   .. math::
      \lim_{x \to 0} \dfrac{\frac{2}{5}x^5}{\int_0^x t(t - \sin t) ~ \mathrm{d}t}
      = \lim_{x \to 0} \dfrac{2x^4}{x(x - \sin x)}
      = \lim_{x \to 0} \dfrac{2x^3}{x - \sin x}
      = \lim_{x \to 0} \dfrac{2x^3}{\frac{x^3}{6}} = 12.

.. _ex-chap6-sec3-ex3:

3. 计算下列定积分.

   (1) :math:`\displaystyle \int_0^1 e^x ~ \mathrm{d}x`; \qquad
   (2) :math:`\displaystyle \int_1^2 (2x + 3) ~ \mathrm{d}x`;

   (3) :math:`\displaystyle \int_0^1 \dfrac{3x^4 + 3x^2 + 1}{x^2 + 1} ~ \mathrm{d}x`; \qquad
   (4) :math:`\displaystyle \int_0^{\frac{\pi}{4}} \tan^2 x ~ \mathrm{d}x`;

   (5) :math:`\displaystyle \int_1^4 \left( \sqrt{x} + \dfrac{1}{\sqrt{x}} \right) \mathrm{d}x`; \qquad
   (6) :math:`\displaystyle \int_{-\frac{1}{2}}^{\frac{1}{2}} \dfrac{1}{\sqrt{1 - x^2}} ~ \mathrm{d}x`.

.. proof:solution::

   (1). :math:`\displaystyle \int_0^1 e^x ~ \mathrm{d}x = \left[ e^x \right]_0^1 = e - 1`.

   (2). :math:`\displaystyle \int_1^2 (2x + 3) ~ \mathrm{d}x = \left[ x^2 + 3x \right]_1^2 = 10 - 4 = 6`.

   (3). 先做除法 :math:`\dfrac{3x^4 + 3x^2 + 1}{x^2 + 1} = 3x^2 + \dfrac{1}{x^2 + 1}`:

   .. math::
      \int_0^1 \dfrac{3x^4 + 3x^2 + 1}{x^2 + 1} ~ \mathrm{d}x
      = \int_0^1 3x^2 ~ \mathrm{d}x + \int_0^1 \dfrac{\mathrm{d}x}{1 + x^2}
      = 1 + \dfrac{\pi}{4}.

   (4). 利用 :math:`\tan^2 x = \sec^2 x - 1`:

   .. math::
      \int_0^{\frac{\pi}{4}} \tan^2 x ~ \mathrm{d}x
      = \left[ \tan x - x \right]_0^{\frac{\pi}{4}} = 1 - \dfrac{\pi}{4}.

   (5).

   .. math::
      \int_1^4 \left( x^{\frac{1}{2}} + x^{-\frac{1}{2}} \right) \mathrm{d}x
      = \left[ \dfrac{2}{3} x^{\frac{3}{2}} + 2 x^{\frac{1}{2}} \right]_1^4
      = \left( \dfrac{16}{3} + 4 \right) - \left( \dfrac{2}{3} + 2 \right) = \dfrac{20}{3}.

   (6). :math:`\displaystyle \int_{-\frac{1}{2}}^{\frac{1}{2}} \dfrac{\mathrm{d}x}{\sqrt{1 - x^2}} = \left[ \arcsin x \right]_{-\frac{1}{2}}^{\frac{1}{2}} = \dfrac{\pi}{6} - \left( -\dfrac{\pi}{6} \right) = \dfrac{\pi}{3}`.

.. _ex-chap6-sec3-ex4:

4. 设 :math:`f(x)` 连续, :math:`\varphi(x) = \displaystyle \int_0^{x^2} x f(t) ~ \mathrm{d}t`, 若
   :math:`\varphi(1) = 1`, :math:`\varphi'(1) = 5`, 求 :math:`f(1)`.

.. proof:solution::

   先把与积分变量无关的 :math:`x` 提出积分号: :math:`\varphi(x) = x \displaystyle \int_0^{x^2} f(t) ~ \mathrm{d}t`. 求导

   .. math::
      \varphi'(x) = \int_0^{x^2} f(t) ~ \mathrm{d}t + x \cdot f(x^2) \cdot 2x
      = \int_0^{x^2} f(t) ~ \mathrm{d}t + 2x^2 f(x^2).

   代入 :math:`x = 1`: :math:`\varphi'(1) = \displaystyle \int_0^1 f(t) ~ \mathrm{d}t + 2 f(1)`. 由
   :math:`\varphi(1) = \displaystyle \int_0^1 f(t) ~ \mathrm{d}t = 1`, 得 :math:`1 + 2f(1) = 5`, 故

   .. math::
      f(1) = 2.

.. _ex-chap6-sec3-ex5:

5. 已知函数 :math:`f(x)` 在 :math:`(-\infty, +\infty)` 上连续, 且
   :math:`f(x) = (x + 1)^2 + 2 \displaystyle \int_0^x f(t) ~ \mathrm{d}t`, 则当 :math:`n \geqslant 2` 时求
   :math:`f^{(n)}(0)`.

.. proof:solution::

   方程两边对 :math:`x` 求导: :math:`f'(x) = 2(x+1) + 2f(x)`, 且由原式得初值
   :math:`f(0) = 1`. 这是一个一阶线性微分方程 :math:`f' - 2f = 2x + 2`. 设
   :math:`f = C e^{2x} + ax + b`, 代入方程: :math:`2Ce^{2x} + a = 2Ce^{2x} + 2ax + 2b + 2x + 2`,
   比较系数得 :math:`0 = 2a + 2 \Rightarrow a = -1`, :math:`a = 2b + 2 \Rightarrow b = -\dfrac{3}{2}`.
   再由 :math:`f(0) = C - \dfrac{3}{2} = 1` 得 :math:`C = \dfrac{5}{2}`. 于是

   .. math::
      f(x) = \dfrac{5}{2} e^{2x} - x - \dfrac{3}{2}.

   对 :math:`n \geqslant 2`, 二次及以下各项求导后消失, 只剩指数项, 故

   .. math::
      f^{(n)}(x) = \dfrac{5}{2} \cdot 2^n e^{2x}, \qquad f^{(n)}(0) = 5 \cdot 2^{n-1}.

.. _ex-chap6-sec3-ex6:

6. 设函数

   .. math::
      f(x) = \begin{cases}
         \dfrac{1}{x^3} \displaystyle \int_0^x \sin t^2 ~ \mathrm{d}t, & x \neq 0, \\
         a, & x = 0
      \end{cases}

   在 :math:`x = 0` 处连续, 求 :math:`a`.

.. proof:solution::

   连续性要求 :math:`a = \displaystyle \lim_{x \to 0} \dfrac{1}{x^3} \int_0^x \sin t^2 ~ \mathrm{d}t`. 这是
   :math:`\dfrac{0}{0}` 型极限, 由洛必达法则 (被积函数 :math:`\sin t^2 \sim t^2`):

   .. math::
      \lim_{x \to 0} \dfrac{\int_0^x \sin t^2 ~ \mathrm{d}t}{x^3}
      = \lim_{x \to 0} \dfrac{\sin x^2}{3x^2}
      = \lim_{x \to 0} \dfrac{x^2}{3x^2} = \dfrac{1}{3}.

   故 :math:`a = \dfrac{1}{3}`.

.. _ex-chap6-sec3-ex7:

7. 已知函数 :math:`f(x) = \displaystyle \int_x^1 \sqrt{1 + t^2} ~ \mathrm{d}t
   + \int_1^{x^2} \sqrt{1 + t} ~ \mathrm{d}t`, 求 :math:`f(x)` 的零点个数.

.. proof:solution::

   首先注意到 :math:`f(1) = 0`, 即 :math:`x = 1` 是一个零点. 求导

   .. math::
      f'(x) = -\sqrt{1 + x^2} + 2x \sqrt{1 + x^2} = (2x - 1) \sqrt{1 + x^2}.

   由于 :math:`\sqrt{1+x^2} > 0`, :math:`f'` 的符号由 :math:`2x - 1` 决定: :math:`f` 在
   :math:`\left( -\infty, \dfrac{1}{2} \right]` 上单调减少, 在 :math:`\left[ \dfrac{1}{2}, +\infty \right)` 上单调增加,
   :math:`x = \dfrac{1}{2}` 是最小值点.

   再看两端与最小值的符号. 由积分意义直接计算:

   .. math::
      f(1) = 0, \qquad f(0) = \int_0^1 \sqrt{1+t^2} ~ \mathrm{d}t - \int_0^1 \sqrt{1+t} ~ \mathrm{d}t
      = \dfrac{\sqrt{2} + \ln(1 + \sqrt{2})}{2} - \dfrac{2}{3}\left( 2\sqrt{2} - 1 \right) < 0,

   (数值约为 :math:`1.148 - 1.219 < 0`); 而

   .. math::
      f(-1) = \int_{-1}^{1} \sqrt{1 + t^2} ~ \mathrm{d}t = \sqrt{2} + \ln \left( 1 + \sqrt{2} \right) > 0.

   且当 :math:`x \to -\infty` 时 :math:`\displaystyle \int_1^{x^2} \sqrt{1+t} ~ \mathrm{d}t \sim \dfrac{2}{3} |x|^3 \to +\infty`
   (增长快于 :math:`\displaystyle \int_x^1 \sqrt{1+t^2} ~ \mathrm{d}t \sim -\dfrac{x^2}{2}`), 故 :math:`x \to -\infty` 时
   :math:`f \to +\infty`.

   于是: 在 :math:`\left( -\infty, \dfrac{1}{2} \right)` 上 :math:`f` 严格减少, 从 :math:`+\infty` 降到
   :math:`f\left( \dfrac{1}{2} \right) < f(0) < 0`, 恰有一个零点; 在 :math:`\left[ \dfrac{1}{2}, +\infty \right)` 上
   :math:`f` 严格增加, 从负值经 :math:`f(1) = 0` 增向 :math:`+\infty`, 恰有一个零点 :math:`x = 1`.

   综上, :math:`f(x)` 共有 :math:`2` 个零点 (一个在 :math:`(-1, 0)` 内, 一个为 :math:`x = 1`).

.. _ex-chap6-sec3-ex8:

8. 设函数 :math:`f(x) = \displaystyle \int_0^x \lvert t^2 - x^2 \rvert ~ \mathrm{d}t` (:math:`x > 0`), 求
   :math:`f'(x)` 和 :math:`f(x)` 的最小值.

.. proof:solution::

   对固定的 :math:`x > 0`, 积分变量 :math:`t \in [0, x]` 满足 :math:`t^2 \leqslant x^2`, 故
   :math:`\lvert t^2 - x^2 \rvert = x^2 - t^2`, 于是

   .. math::
      f(x) = \int_0^x (x^2 - t^2) ~ \mathrm{d}t = x^3 - \dfrac{x^3}{3} = \dfrac{2}{3} x^3,

   从而

   .. math::
      f'(x) = 2x^2.

   :math:`f(x)` 在 :math:`(0, +\infty)` 上严格单调增加, 因此没有最小值; 其下确界为
   :math:`\displaystyle \lim_{x \to 0^+} \dfrac{2}{3}x^3 = 0`, 即 :math:`f(x)` 可任意接近 :math:`0` 但取不到.
   (若把定义域放宽为 :math:`x \geqslant 0`, 则最小值 :math:`f(0) = 0`.)

.. _ex-chap6-sec4:

§6.4 定积分的换元法和分部积分法
------------------------------------

.. _ex-chap6-sec4-ex1:

1. 计算下列定积分.

   (1) :math:`\displaystyle \int_0^{\frac{\pi}{2}} \sin^3 x \cos x ~ \mathrm{d}x`; \qquad
   (2) :math:`\displaystyle \int_0^3 \dfrac{1}{(3 + 2x)^2} ~ \mathrm{d}x`;

   (3) :math:`\displaystyle \int_0^3 \dfrac{x}{\sqrt{36 - x^2}} ~ \mathrm{d}x`; \qquad
   (4) :math:`\displaystyle \int_1^2 \dfrac{1}{x \sqrt{1 + \ln x}} ~ \mathrm{d}x`;

   (5) :math:`\displaystyle \int_0^1 \dfrac{\sqrt{x}}{1 + \sqrt{x}} ~ \mathrm{d}x`; \qquad
   (6) :math:`\displaystyle \int_0^1 (x^3 - x) \sqrt{1 - x^2} ~ \mathrm{d}x`;

   (7) :math:`\displaystyle \int_0^{\ln 5} \sqrt{e^x - 1} ~ \mathrm{d}x`; \qquad
   (8) :math:`\displaystyle \int_{\frac{1}{\pi}}^{\frac{\pi}{2}} \dfrac{1}{x^2} \sin \dfrac{1}{x} ~ \mathrm{d}x`;

   (9) :math:`\displaystyle \int_0^{\pi} \dfrac{x^2}{(4 - x^2) \sqrt{4 - x^2}} ~ \mathrm{d}x`; \qquad
   (10) :math:`\displaystyle \int_0^8 \dfrac{1}{1 + \sqrt[3]{x}} ~ \mathrm{d}x`;

   (11) :math:`\displaystyle \int_0^2 \dfrac{2x - 4}{x^2 + 2x + 4} ~ \mathrm{d}x`; \qquad
   (12) :math:`\displaystyle \int_0^1 \dfrac{1}{(2x^2 + 1) \sqrt{x^2 + 1}} ~ \mathrm{d}x`.

.. proof:solution::

   (1). :math:`\displaystyle \int_0^{\frac{\pi}{2}} \sin^3 x \cos x ~ \mathrm{d}x = \left[ \dfrac{\sin^4 x}{4} \right]_0^{\frac{\pi}{2}} = \dfrac{1}{4}`.

   (2). :math:`\displaystyle \int_0^3 \dfrac{\mathrm{d}x}{(3 + 2x)^2} = \left[ -\dfrac{1}{2(3+2x)} \right]_0^3 = \dfrac{1}{6} - \dfrac{1}{18} = \dfrac{1}{9}`.

   (3). :math:`\displaystyle \int_0^3 \dfrac{x ~ \mathrm{d}x}{\sqrt{36 - x^2}} = \left[ -\sqrt{36 - x^2} \right]_0^3 = 6 - \sqrt{27} = 6 - 3\sqrt{3}`.

   (4). 令 :math:`u = 1 + \ln x`, :math:`\mathrm{d}u = \dfrac{\mathrm{d}x}{x}`, :math:`x: 1 \to 2` 对应 :math:`u: 1 \to 1 + \ln 2`:

   .. math::
      \int_1^2 \dfrac{\mathrm{d}x}{x \sqrt{1 + \ln x}} = \int_1^{1+\ln 2} \dfrac{\mathrm{d}u}{\sqrt{u}}
      = \left[ 2\sqrt{u} \right]_1^{1+\ln 2} = 2 \left( \sqrt{1 + \ln 2} - 1 \right).

   (5). 令 :math:`t = \sqrt{x}`, :math:`\mathrm{d}x = 2t ~ \mathrm{d}t`:

   .. math::
      \int_0^1 \dfrac{\sqrt{x}}{1 + \sqrt{x}} ~ \mathrm{d}x
      = \int_0^1 \dfrac{2t^2}{1 + t} ~ \mathrm{d}t
      = 2 \int_0^1 \left( t - 1 + \dfrac{1}{1+t} \right) \mathrm{d}t
      = 2 \left[ \dfrac{t^2}{2} - t + \ln(1 + t) \right]_0^1 = 2 \ln 2 - 1.

   (6). :math:`x^3 - x = -x(1 - x^2)`, 令 :math:`u = 1 - x^2`, :math:`x ~ \mathrm{d}x = -\dfrac{\mathrm{d}u}{2}`;
   :math:`x: 0 \to 1` 对应 :math:`u: 1 \to 0`:

   .. math::
      \int_0^1 (x^3 - x)\sqrt{1 - x^2} ~ \mathrm{d}x
      = -\int_0^1 x (1 - x^2)^{\frac{3}{2}} ~ \mathrm{d}x
      = \dfrac{1}{2} \int_1^0 u^{\frac{3}{2}} ~ \mathrm{d}u
      = -\dfrac{1}{2} \int_0^1 u^{\frac{3}{2}} ~ \mathrm{d}u
      = -\dfrac{1}{5}.

   (7). 令 :math:`t = \sqrt{e^x - 1}`, 则 :math:`x = \ln(1 + t^2)`, :math:`\mathrm{d}x = \dfrac{2t}{1 + t^2} ~ \mathrm{d}t`;
   :math:`x: 0 \to \ln 5` 对应 :math:`t: 0 \to 2`:

   .. math::
      \int_0^{\ln 5} \sqrt{e^x - 1} ~ \mathrm{d}x
      = \int_0^2 \dfrac{2t^2}{1 + t^2} ~ \mathrm{d}t
      = 2 \int_0^2 \left( 1 - \dfrac{1}{1 + t^2} \right) \mathrm{d}t
      = 4 - 2 \arctan 2.

   (8). 令 :math:`u = \dfrac{1}{x}`, :math:`\mathrm{d}u = -\dfrac{\mathrm{d}x}{x^2}`; :math:`x: \dfrac{1}{\pi} \to \dfrac{\pi}{2}`
   对应 :math:`u: \pi \to \dfrac{2}{\pi}`:

   .. math::
      \int_{\frac{1}{\pi}}^{\frac{\pi}{2}} \dfrac{1}{x^2} \sin \dfrac{1}{x} ~ \mathrm{d}x
      = \int_{\frac{2}{\pi}}^{\pi} \sin u ~ \mathrm{d}u
      = \left[ -\cos u \right]_{\frac{2}{\pi}}^{\pi} = 1 + \cos \dfrac{2}{\pi}.

   (9). 按印刷原文, 被积函数 :math:`\dfrac{x^2}{(4 - x^2)\sqrt{4 - x^2}}` 在 :math:`x > 2` 处无定义 (根号内为负),
     积分在 :math:`[0, \pi]` 上没有意义, 疑为分母印误.

   .. note::
      修正为 :math:`\displaystyle \int_0^{\pi} \dfrac{x^2}{(4 + x^2)\sqrt{4 + x^2}} ~ \mathrm{d}x` 后可解
      (积分区间与原题一致): 令 :math:`x = 2 \tan t`, 则 :math:`\sqrt{4 + x^2} = 2 \sec t`,
      :math:`\mathrm{d}x = 2 \sec^2 t ~ \mathrm{d}t`,

      .. math::
         \int_0^{\pi} \dfrac{x^2}{(4 + x^2)\sqrt{4 + x^2}} ~ \mathrm{d}x
         = \int_0^{\arctan \frac{\pi}{2}} \dfrac{4 \tan^2 t \cdot 2 \sec^2 t}{4 \sec^2 t \cdot 2 \sec t} ~ \mathrm{d}t
         = \int_0^{\arctan \frac{\pi}{2}} \left( \sec t - \cos t \right) \mathrm{d}t.

      由 :math:`\displaystyle \int (\sec t - \cos t) ~ \mathrm{d}t = \ln \lvert \sec t + \tan t \rvert - \sin t + C`,
      记 :math:`\alpha = \arctan \dfrac{\pi}{2}`, 则 :math:`\sec \alpha = \dfrac{\sqrt{4 + \pi^2}}{2}`,
      :math:`\tan \alpha = \dfrac{\pi}{2}`, :math:`\sin \alpha = \dfrac{\pi}{\sqrt{4 + \pi^2}}`, 故

      .. math::
         \int_0^{\pi} \dfrac{x^2}{(4 + x^2)\sqrt{4 + x^2}} ~ \mathrm{d}x
         = \ln \dfrac{\sqrt{4 + \pi^2} + \pi}{2} - \dfrac{\pi}{\sqrt{4 + \pi^2}}.

   (10). 令 :math:`t = \sqrt[3]{x}`, :math:`x = t^3`, :math:`\mathrm{d}x = 3t^2 ~ \mathrm{d}t`;
   :math:`x: 0 \to 8` 对应 :math:`t: 0 \to 2`:

   .. math::
      \int_0^8 \dfrac{\mathrm{d}x}{1 + \sqrt[3]{x}} = \int_0^2 \dfrac{3t^2}{1 + t} ~ \mathrm{d}t
      = 3 \left[ \dfrac{t^2}{2} - t + \ln(1 + t) \right]_0^2 = 3 \ln 3.

   (11). 分子写成 :math:`2x - 4 = (2x + 2) - 6`:

   .. math::
      \int_0^2 \dfrac{2x - 4}{x^2 + 2x + 4} ~ \mathrm{d}x
      = \left[ \ln \left( x^2 + 2x + 4 \right) \right]_0^2 - 6 \int_0^2 \dfrac{\mathrm{d}(x+1)}{(x+1)^2 + 3}
      = \ln 3 - \dfrac{6}{\sqrt{3}} \left[ \arctan \dfrac{x+1}{\sqrt{3}} \right]_0^2.

   由 :math:`\arctan \sqrt{3} = \dfrac{\pi}{3}`, :math:`\arctan \dfrac{1}{\sqrt{3}} = \dfrac{\pi}{6}`, 得

   .. math::
      \int_0^2 \dfrac{2x - 4}{x^2 + 2x + 4} ~ \mathrm{d}x = \ln 3 - \dfrac{6}{\sqrt{3}} \cdot \dfrac{\pi}{6}
      = \ln 3 - \dfrac{\sqrt{3}\,\pi}{3}.

   (12). 令 :math:`x = \tan t`, 则 :math:`\sqrt{x^2 + 1} = \sec t`, :math:`\mathrm{d}x = \sec^2 t ~ \mathrm{d}t`:

   .. math::
      \int_0^1 \dfrac{\mathrm{d}x}{(2x^2 + 1)\sqrt{x^2 + 1}}
      = \int_0^{\frac{\pi}{4}} \dfrac{\cos t}{2 \sin^2 t + \cos^2 t} ~ \mathrm{d}t
      = \int_0^{\frac{\pi}{4}} \dfrac{\mathrm{d}(\sin t)}{1 + \sin^2 t}
      = \left[ \arctan(\sin t) \right]_0^{\frac{\pi}{4}}
      = \arctan \dfrac{\sqrt{2}}{2}.

.. _ex-chap6-sec4-ex2:

2. 计算下列定积分.

   (1) :math:`\displaystyle \int_0^{\frac{\pi}{2}} x \sec^2 x ~ \mathrm{d}x`; \qquad
   (2) :math:`\displaystyle \int_0^{e - 1} \ln(x + 1) ~ \mathrm{d}x`;

   (3) :math:`\displaystyle \int_0^{\frac{\pi}{2}} x \cos 2x ~ \mathrm{d}x`; \qquad
   (4) :math:`\displaystyle \int_0^1 x e^{-x} ~ \mathrm{d}x`;

   (5) :math:`\displaystyle \int_0^{\frac{\sqrt{3}}{2}} \arccos x ~ \mathrm{d}x`; \qquad
   (6) :math:`\displaystyle \int_0^1 x 2^x ~ \mathrm{d}x`;

   (7) :math:`\displaystyle \int_1^e \dfrac{\ln x}{x^2} ~ \mathrm{d}x`; \qquad
   (8) :math:`\displaystyle \int_1^e \sin(\ln x) ~ \mathrm{d}x`.

.. proof:solution::

   (1). 按印刷原文, :math:`x \sec^2 x` 在 :math:`x \to \dfrac{\pi}{2}^-` 时无界 (:math:`\sec^2 x \sim \dfrac{1}{(\frac{\pi}{2} - x)^2}`),
     积分发散, 疑上限印误.

   .. note::
      修正为上限 :math:`\dfrac{\pi}{4}` 后可解: 由分部积分,

      .. math::
         \int_0^{\frac{\pi}{4}} x \sec^2 x ~ \mathrm{d}x
         = \left[ x \tan x \right]_0^{\frac{\pi}{4}} - \int_0^{\frac{\pi}{4}} \tan x ~ \mathrm{d}x
         = \dfrac{\pi}{4} + \left[ \ln \left\lvert \cos x \right\rvert \right]_0^{\frac{\pi}{4}}
         = \dfrac{\pi}{4} - \dfrac{1}{2} \ln 2.

   (2). 分部积分 (:math:`u = \ln(x+1)`, :math:`\mathrm{d}v = \mathrm{d}x`):

   .. math::
      \int_0^{e-1} \ln(x + 1) ~ \mathrm{d}x
      = \left[ (x+1) \ln(x+1) - (x+1) \right]_0^{e-1} = (e - e) - (0 - 1) = 1.

   (3). 分部积分 (:math:`u = x`, :math:`\mathrm{d}v = \cos 2x ~ \mathrm{d}x`, :math:`v = \dfrac{\sin 2x}{2}`):

   .. math::
      \int_0^{\frac{\pi}{2}} x \cos 2x ~ \mathrm{d}x
      = \left[ \dfrac{x \sin 2x}{2} \right]_0^{\frac{\pi}{2}} - \dfrac{1}{2} \int_0^{\frac{\pi}{2}} \sin 2x ~ \mathrm{d}x
      = 0 + \dfrac{1}{4} \left[ \cos 2x \right]_0^{\frac{\pi}{2}} = \dfrac{\cos \pi - \cos 0}{4} = -\dfrac{1}{2}.

   (4). 分部积分:

   .. math::
      \int_0^1 x e^{-x} ~ \mathrm{d}x = \left[ -x e^{-x} \right]_0^1 + \int_0^1 e^{-x} ~ \mathrm{d}x
      = -e^{-1} + \left( 1 - e^{-1} \right) = 1 - \dfrac{2}{e}.

   (5). 分部积分 (:math:`u = \arccos x`, :math:`v = x`), 注意 :math:`\mathrm{d}(\arccos x) = -\dfrac{\mathrm{d}x}{\sqrt{1-x^2}}`:

   .. math::
      \int_0^{\frac{\sqrt{3}}{2}} \arccos x ~ \mathrm{d}x
      = \left[ x \arccos x - \sqrt{1 - x^2} \right]_0^{\frac{\sqrt{3}}{2}}
      = \left( \dfrac{\sqrt{3}}{2} \cdot \dfrac{\pi}{6} - \dfrac{1}{2} \right) - (-1)
      = \dfrac{\sqrt{3}\,\pi}{12} + \dfrac{1}{2}.

   (6). 分部积分 (:math:`u = x`, :math:`\mathrm{d}v = 2^x ~ \mathrm{d}x`, :math:`v = \dfrac{2^x}{\ln 2}`):

   .. math::
      \int_0^1 x 2^x ~ \mathrm{d}x = \left[ \dfrac{x \cdot 2^x}{\ln 2} \right]_0^1 - \dfrac{1}{\ln 2} \int_0^1 2^x ~ \mathrm{d}x
      = \dfrac{2}{\ln 2} - \dfrac{1}{\ln^2 2} = \dfrac{2 \ln 2 - 1}{\ln^2 2}.

   (7). 分部积分 (:math:`u = \ln x`, :math:`\mathrm{d}v = \dfrac{\mathrm{d}x}{x^2}`, :math:`v = -\dfrac{1}{x}`):

   .. math::
      \int_1^e \dfrac{\ln x}{x^2} ~ \mathrm{d}x = \left[ -\dfrac{\ln x}{x} \right]_1^e + \int_1^e \dfrac{\mathrm{d}x}{x^2}
      = -\dfrac{1}{e} + \left( 1 - \dfrac{1}{e} \right) = 1 - \dfrac{2}{e}.

   (8). 记 :math:`I = \displaystyle \int_1^e \sin(\ln x) ~ \mathrm{d}x`. 分部积分 (:math:`u = \sin(\ln x)`, :math:`v = x`):

   .. math::
      I = \left[ x \sin(\ln x) \right]_1^e - \int_1^e \cos(\ln x) ~ \mathrm{d}x = e \sin 1 - J,

   再对 :math:`J = \displaystyle \int_1^e \cos(\ln x) ~ \mathrm{d}x` 分部积分:

   .. math::
      J = \left[ x \cos(\ln x) \right]_1^e + \int_1^e \sin(\ln x) ~ \mathrm{d}x = e \cos 1 - 1 + I.

   于是 :math:`I = e \sin 1 - e \cos 1 + 1 - I`, 解得

   .. math::
      I = \dfrac{e}{2} \left( \sin 1 - \cos 1 \right) + \dfrac{1}{2}.

.. _ex-chap6-sec4-ex3:

3. 利用奇偶性计算下列定积分.

   (1) :math:`\displaystyle \int_{-\pi}^{\pi} (x^3 + 2) \cos x ~ \mathrm{d}x`; \qquad
   (2) :math:`\displaystyle \int_{-2}^{2} \dfrac{7x^{2025} + 9x^3}{1 + x^2} ~ \mathrm{d}x`;

   (3) :math:`\displaystyle \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \left[ \ln \left( x + \sqrt{1 + x^2} \right)
       + \sin^2 x \right] \cos^2 x ~ \mathrm{d}x`; \qquad
   (4) :math:`\displaystyle \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} (x + \cos x)^2 ~ \mathrm{d}x`;

   (5) :math:`\displaystyle \int_{-1}^{1} \left( x^2 \tan x + \dfrac{1}{2} \right) \sqrt{1 - x^2} ~ \mathrm{d}x`; \qquad
   (6) :math:`\displaystyle \int_{-2}^{2} \dfrac{x + \lvert x \rvert}{2 + x^2} ~ \mathrm{d}x`.

.. proof:solution::

   (1). :math:`x^3 \cos x` 是奇函数, 积分为零; :math:`2\cos x` 是偶函数, 故

   .. math::
      \int_{-\pi}^{\pi} (x^3 + 2) \cos x ~ \mathrm{d}x = 2 \int_0^{\pi} 2 \cos x ~ \mathrm{d}x = 4 \left[ \sin x \right]_0^{\pi} = 0.

   (2). :math:`\dfrac{7x^{2025} + 9x^3}{1 + x^2}` 的分子是奇函数, 分母是偶函数, 故被积函数是奇函数, 积分为 :math:`0`.

   (3). :math:`\ln\left( x + \sqrt{1 + x^2} \right)` 是奇函数 (反双曲正弦), 乘以偶函数 :math:`\cos^2 x` 后仍为奇函数,
   其积分为零. 于是

   .. math::
      \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \left[ \ln \left( x + \sqrt{1 + x^2} \right) + \sin^2 x \right] \cos^2 x ~ \mathrm{d}x
      = 2 \int_0^{\frac{\pi}{2}} \sin^2 x \cos^2 x ~ \mathrm{d}x
      = \dfrac{1}{2} \int_0^{\frac{\pi}{2}} \sin^2 2x ~ \mathrm{d}x
      = \dfrac{1}{4} \int_0^{\frac{\pi}{2}} (1 - \cos 4x) ~ \mathrm{d}x = \dfrac{\pi}{8}.

   (4). 展开 :math:`(x + \cos x)^2 = x^2 + 2x\cos x + \cos^2 x`: :math:`2x \cos x` 是奇函数, 积分为零, 故

   .. math::
      \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} (x + \cos x)^2 ~ \mathrm{d}x
      = 2 \int_0^{\frac{\pi}{2}} x^2 ~ \mathrm{d}x + \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \cos^2 x ~ \mathrm{d}x
      = \dfrac{\pi^3}{12} + \dfrac{\pi}{2}.

   (5). :math:`x^2 \tan x \sqrt{1 - x^2}` 是奇函数 (奇 × 奇... 确切地: :math:`x^2\sqrt{1-x^2}` 偶, :math:`\tan x` 奇, 乘积奇),
   积分为零, 故

   .. math::
      \int_{-1}^{1} \left( x^2 \tan x + \dfrac{1}{2} \right) \sqrt{1 - x^2} ~ \mathrm{d}x
      = \dfrac{1}{2} \int_{-1}^{1} \sqrt{1 - x^2} ~ \mathrm{d}x = \dfrac{1}{2} \cdot \dfrac{\pi}{2} = \dfrac{\pi}{4}.

   (6). 当 :math:`x < 0` 时 :math:`x + \lvert x \rvert = 0`; 当 :math:`x \geqslant 0` 时 :math:`x + \lvert x \rvert = 2x`. 故

   .. math::
      \int_{-2}^{2} \dfrac{x + \lvert x \rvert}{2 + x^2} ~ \mathrm{d}x
      = \int_0^2 \dfrac{2x}{2 + x^2} ~ \mathrm{d}x
      = \left[ \ln \left( 2 + x^2 \right) \right]_0^2 = \ln 6 - \ln 2 = \ln 3.

.. _ex-chap6-sec4-ex4:

4. 计算定积分 :math:`\displaystyle \int_{-\frac{\pi}{4}}^{\frac{\pi}{2}} \sqrt{\cos x - \cos^3 x} ~ \mathrm{d}x`.

.. proof:solution::

   在 :math:`\left[ -\dfrac{\pi}{4}, \dfrac{\pi}{2} \right]` 上 :math:`\cos x \geqslant 0`, 于是

   .. math::
      \sqrt{\cos x - \cos^3 x} = \sqrt{\cos x \left( 1 - \cos^2 x \right)} = \sqrt{\cos x}\, \lvert \sin x \rvert.

   按 :math:`\sin x` 的符号分两段去掉绝对值:

   .. math::
      \int_{-\frac{\pi}{4}}^{\frac{\pi}{2}} \sqrt{\cos x - \cos^3 x} ~ \mathrm{d}x
      = -\int_{-\frac{\pi}{4}}^{0} \sqrt{\cos x}\, \sin x ~ \mathrm{d}x + \int_0^{\frac{\pi}{2}} \sqrt{\cos x}\, \sin x ~ \mathrm{d}x.

   利用 :math:`\mathrm{d}(\cos x) = -\sin x ~ \mathrm{d}x`:

   .. math::
      -\int_{-\frac{\pi}{4}}^{0} \sqrt{\cos x}\, \sin x ~ \mathrm{d}x = \int_0^{-\frac{\pi}{4}} \sqrt{\cos x} ~ \mathrm{d}(\cos x) = \left[ \dfrac{2}{3} \cos^{\frac{3}{2}} x \right]_0^{-\frac{\pi}{4}} = \dfrac{2}{3} \left( \left( \dfrac{\sqrt{2}}{2} \right)^{\frac{3}{2}} - 1 \right),

   .. math::
      \int_0^{\frac{\pi}{2}} \sqrt{\cos x}\, \sin x ~ \mathrm{d}x = -\int_0^{\frac{\pi}{2}} \sqrt{\cos x} ~ \mathrm{d}(\cos x) = \dfrac{2}{3}.

   其中 :math:`\left( \dfrac{\sqrt{2}}{2} \right)^{\frac{3}{2}} = 2^{-\frac{3}{4}}`. 故

   .. math::
      \int_{-\frac{\pi}{4}}^{\frac{\pi}{2}} \sqrt{\cos x - \cos^3 x} ~ \mathrm{d}x
      = \dfrac{2}{3} \left( 2^{-\frac{3}{4}} - 1 \right) + \dfrac{2}{3} = \dfrac{2}{3} \left( 1 - 2^{-\frac{3}{4}} \right) + \dfrac{2}{3}
      = \dfrac{4}{3} - \dfrac{2}{3} \cdot 2^{-\frac{3}{4}}.

   等价地写作 :math:`\dfrac{2}{3}\left( 2 - 2^{-\frac{3}{4}} \right)`.

.. _ex-chap6-sec4-ex5:

5. 设 :math:`f(x)` 连续, 求 :math:`\dfrac{\mathrm{d}}{\mathrm{d}x} \displaystyle \int_0^x
   t f(x^2 - t^2) ~ \mathrm{d}t`.

.. proof:solution::

   被积函数中含上限变量 :math:`x`, 先换元把它移出积分号. 令 :math:`u = x^2 - t^2`, 则
   :math:`\mathrm{d}u = -2t ~ \mathrm{d}t`; :math:`t: 0 \to x` 对应 :math:`u: x^2 \to 0`. 于是

   .. math::
      \int_0^x t f(x^2 - t^2) ~ \mathrm{d}t = -\dfrac{1}{2} \int_{x^2}^{0} f(u) ~ \mathrm{d}u
      = \dfrac{1}{2} \int_0^{x^2} f(u) ~ \mathrm{d}u.

   再对 :math:`x` 求导:

   .. math::
      \dfrac{\mathrm{d}}{\mathrm{d}x} \int_0^x t f(x^2 - t^2) ~ \mathrm{d}t
      = \dfrac{1}{2} \cdot f(x^2) \cdot 2x = x f(x^2).

.. _ex-chap6-sec4-ex6:

6. 证明: :math:`f(x)` 在区间 :math:`[a, b]` 上连续, 则

   .. math::
      \int_a^b f(x) ~ \mathrm{d}x = \int_a^b f(a + b - x) ~ \mathrm{d}x
      = (b - a) \int_0^1 f \left[ a + (b - a)x \right] \mathrm{d}x.

.. proof:solution::

   第一部分: 令 :math:`u = a + b - x`, 则 :math:`\mathrm{d}u = -\mathrm{d}x`; :math:`x: a \to b` 对应
   :math:`u: b \to a`, 于是

   .. math::
      \int_a^b f(a + b - x) ~ \mathrm{d}x = \int_b^a f(u) \cdot (-\mathrm{d}u) = \int_a^b f(u) ~ \mathrm{d}u.

   第二部分: 令 :math:`u = a + (b - a)x`, 则 :math:`\mathrm{d}u = (b - a) ~ \mathrm{d}x`;
   :math:`x: 0 \to 1` 对应 :math:`u: a \to b`, 于是

   .. math::
      (b - a) \int_0^1 f \left[ a + (b - a)x \right] \mathrm{d}x = \int_a^b f(u) ~ \mathrm{d}u.

   综上三者相等. 这两个等式表明: 定积分与积分变量的记号无关, 且区间上的积分可以标准化到 :math:`[0, 1]` 上.

.. _ex-chap6-sec4-ex7:

7. 设 :math:`f(x) = \begin{cases} 1 + x^2, & x < 0, \\ \cos \dfrac{\pi}{2} x, & x \geqslant 0, \end{cases}`
   求 :math:`\displaystyle \int_{-1}^2 f(x - 1) ~ \mathrm{d}x`.

.. proof:solution::

   令 :math:`t = x - 1`, 则 :math:`\mathrm{d}x = \mathrm{d}t`, :math:`x: -1 \to 2` 对应 :math:`t: -2 \to 1`:

   .. math::
      \int_{-1}^2 f(x - 1) ~ \mathrm{d}x = \int_{-2}^1 f(t) ~ \mathrm{d}t
      = \int_{-2}^0 (1 + t^2) ~ \mathrm{d}t + \int_0^1 \cos \dfrac{\pi t}{2} ~ \mathrm{d}t.

   分别计算:

   .. math::
      \int_{-2}^0 (1 + t^2) ~ \mathrm{d}t = \left[ t + \dfrac{t^3}{3} \right]_{-2}^0
      = 0 - \left( -2 - \dfrac{8}{3} \right) = \dfrac{14}{3}, \qquad
      \int_0^1 \cos \dfrac{\pi t}{2} ~ \mathrm{d}t = \dfrac{2}{\pi} \left[ \sin \dfrac{\pi t}{2} \right]_0^1 = \dfrac{2}{\pi}.

   故

   .. math::
      \int_{-1}^2 f(x - 1) ~ \mathrm{d}x = \dfrac{14}{3} + \dfrac{2}{\pi}.

.. _ex-chap6-sec4-ex8:

8. 证明: :math:`\displaystyle \int_0^1 x^m (1 - x)^n ~ \mathrm{d}x
   = \int_0^1 x^n (1 - x)^m ~ \mathrm{d}x`.

.. proof:solution::

   在左端积分中作换元 :math:`x = 1 - u`, 则 :math:`\mathrm{d}x = -\mathrm{d}u`, :math:`x: 0 \to 1` 对应
   :math:`u: 1 \to 0`:

   .. math::
      \int_0^1 x^m (1 - x)^n ~ \mathrm{d}x
      = \int_1^0 (1 - u)^m u^n \cdot (-\mathrm{d}u)
      = \int_0^1 u^n (1 - u)^m ~ \mathrm{d}u
      = \int_0^1 x^n (1 - x)^m ~ \mathrm{d}x,

   最后一步利用了定积分与积分变量记号无关. 证毕.

.. _ex-chap6-sec4-ex9:

9. 设 :math:`f(x)` 在 :math:`[a, b]` 上有二阶连续导数, :math:`f(2) = \dfrac{1}{2}`, :math:`f'(2) = 0`, 且
   :math:`\displaystyle \int_0^2 f(x) ~ \mathrm{d}x = 1`, 试求定积分
   :math:`I = \displaystyle \int_0^1 x^2 f''(2x) ~ \mathrm{d}x`.

.. proof:solution::

   先换元 :math:`t = 2x`, 则 :math:`\mathrm{d}x = \dfrac{\mathrm{d}t}{2}`, :math:`x: 0 \to 1` 对应 :math:`t: 0 \to 2`,
   :math:`x^2 = \dfrac{t^2}{4}`:

   .. math::
      I = \int_0^2 \dfrac{t^2}{4} f''(t) \cdot \dfrac{\mathrm{d}t}{2} = \dfrac{1}{8} \int_0^2 t^2 f''(t) ~ \mathrm{d}t.

   分部积分 (:math:`u = t^2`, :math:`\mathrm{d}v = f''(t) ~ \mathrm{d}t`):

   .. math::
      \int_0^2 t^2 f''(t) ~ \mathrm{d}t = \left[ t^2 f'(t) \right]_0^2 - \int_0^2 2t f'(t) ~ \mathrm{d}t
      = 4 f'(2) - 2 \left( \left[ t f(t) \right]_0^2 - \int_0^2 f(t) ~ \mathrm{d}t \right).

   代入已知条件 :math:`f(2) = \dfrac{1}{2}`, :math:`f'(2) = 0`, :math:`\displaystyle \int_0^2 f(t) ~ \mathrm{d}t = 1`:

   .. math::
      \int_0^2 t^2 f''(t) ~ \mathrm{d}t = 0 - 2 \left( 2 \cdot \dfrac{1}{2} - 0 - 1 \right) = 0.

   故

   .. math::
      I = \dfrac{1}{8} \times 0 = 0.

.. _ex-chap6-sec4-ex10:

10. 已知函数 :math:`f(x) = \displaystyle \int_0^x \dfrac{\sin t}{x - t} ~ \mathrm{d}t`, 求
    :math:`\displaystyle \int_0^{\pi} f(x) ~ \mathrm{d}x`.

.. proof:solution::

   .. note::
      按印刷原文 :math:`f(x) = \displaystyle \int_0^x \dfrac{\sin t}{x - t} ~ \mathrm{d}t`, 当 :math:`t \to x^-` 时
      被积函数 :math:`\sim \dfrac{\sin x}{x - t}` 无界, 对一般 :math:`x` 积分发散, 题面疑为印刷错误.
      按同类题的通行版本, 应为乘积形式 :math:`f(x) = \displaystyle \int_0^x (x - t) \sin t ~ \mathrm{d}t`,
      下面按此求解.

   先算出 :math:`f(x)`: 分部积分两次 (或直接按 :math:`\int_0^x (x-t) g(t) ~ \mathrm{d}t = x \int_0^x g - \int_0^x t g ~ \mathrm{d}t` 展开):

   .. math::
      f(x) = x \int_0^x \sin t ~ \mathrm{d}t - \int_0^x t \sin t ~ \mathrm{d}t
      = x (1 - \cos x) - \left( \sin x - x \cos x \right)
      = x - \sin x.

   于是

   .. math::
      \int_0^{\pi} f(x) ~ \mathrm{d}x = \int_0^{\pi} (x - \sin x) ~ \mathrm{d}x
      = \dfrac{\pi^2}{2} - \left[ -\cos x \right]_0^{\pi} = \dfrac{\pi^2}{2} - 2.

.. _ex-chap6-sec5:

§6.5 广义积分
------------------------------------

.. _ex-chap6-sec5-ex1:

1. 下列广义积分是否收敛? 如果收敛求出它的值.

   (1) :math:`\displaystyle \int_0^{+\infty} x^3 e^{-x^2} ~ \mathrm{d}x`; \qquad
   (2) :math:`\displaystyle \int_1^{+\infty} \dfrac{1}{e^x + e^{2 - x}} ~ \mathrm{d}x`;

   (3) :math:`\displaystyle \int_0^{+\infty} \dfrac{x}{(1 + x^2)^3} ~ \mathrm{d}x`; \qquad
   (4) :math:`\displaystyle \int_e^{+\infty} \dfrac{1}{x \ln x^2} ~ \mathrm{d}x`;

   (5) :math:`\displaystyle \int_0^{+\infty} \dfrac{1}{x^2 + 4x + 8} ~ \mathrm{d}x`; \qquad
   (6) :math:`\displaystyle \int_0^{+\infty} \dfrac{\ln(1 + x)}{(1 + x)^2} ~ \mathrm{d}x`;

   (7) :math:`\displaystyle \int_0^1 \ln^2 x ~ \mathrm{d}x`; \qquad
   (8) :math:`\displaystyle \int_0^1 \dfrac{x}{(2 - x^2) \sqrt{1 - x^2}} ~ \mathrm{d}x`;

   (9) :math:`\displaystyle \int_0^1 \sqrt{\dfrac{x}{1 - x}} ~ \mathrm{d}x`; \qquad
   (10) :math:`\displaystyle \int_1^{+\infty} \dfrac{1}{x \sqrt{x^2 - 1}} ~ \mathrm{d}x`.

.. proof:solution::

   (1). 令 :math:`u = x^2`, :math:`\mathrm{d}u = 2x ~ \mathrm{d}x`: :math:`x^3 ~ \mathrm{d}x = \dfrac{u}{2} ~ \mathrm{d}u`,

   .. math::
      \int_0^{+\infty} x^3 e^{-x^2} ~ \mathrm{d}x = \dfrac{1}{2} \int_0^{+\infty} u e^{-u} ~ \mathrm{d}u
      = \dfrac{1}{2} \left[ -u e^{-u} - e^{-u} \right]_0^{+\infty} = \dfrac{1}{2}.

   (2). 分子分母同乘 :math:`e^x`, 令 :math:`u = e^x` (:math:`x: 1 \to +\infty` 对应 :math:`u: e \to +\infty`):

   .. math::
      \int_1^{+\infty} \dfrac{\mathrm{d}x}{e^x + e^{2 - x}}
      = \int_1^{+\infty} \dfrac{e^x ~ \mathrm{d}x}{e^{2x} + e^2}
      = \int_e^{+\infty} \dfrac{\mathrm{d}u}{u^2 + e^2}
      = \dfrac{1}{e} \left[ \arctan \dfrac{u}{e} \right]_e^{+\infty}
      = \dfrac{1}{e} \left( \dfrac{\pi}{2} - \dfrac{\pi}{4} \right) = \dfrac{\pi}{4e}.

   (3). 令 :math:`u = 1 + x^2`:

   .. math::
      \int_0^{+\infty} \dfrac{x ~ \mathrm{d}x}{(1 + x^2)^3} = \dfrac{1}{2} \int_1^{+\infty} \dfrac{\mathrm{d}u}{u^3}
      = \dfrac{1}{2} \left[ -\dfrac{1}{2u^2} \right]_1^{+\infty} = \dfrac{1}{4}.

   (4). :math:`\ln x^2 = 2 \ln x` (:math:`x > 0`), 令 :math:`u = \ln x`:

   .. math::
      \int_e^{+\infty} \dfrac{\mathrm{d}x}{x \ln x^2} = \dfrac{1}{2} \int_e^{+\infty} \dfrac{\mathrm{d}x}{x \ln x}
      = \dfrac{1}{2} \int_1^{+\infty} \dfrac{\mathrm{d}u}{u} = \dfrac{1}{2} \left[ \ln u \right]_1^{+\infty} = +\infty,

   积分发散.

   (5). 配方 :math:`x^2 + 4x + 8 = (x + 2)^2 + 4`:

   .. math::
      \int_0^{+\infty} \dfrac{\mathrm{d}x}{x^2 + 4x + 8}
      = \left[ \dfrac{1}{2} \arctan \dfrac{x + 2}{2} \right]_0^{+\infty}
      = \dfrac{1}{2} \left( \dfrac{\pi}{2} - \dfrac{\pi}{4} \right) = \dfrac{\pi}{8}.

   (6). 分部积分 (:math:`u = \ln(1+x)`, :math:`\mathrm{d}v = \dfrac{\mathrm{d}x}{(1+x)^2}`, :math:`v = -\dfrac{1}{1+x}`):

   .. math::
      \int_0^{+\infty} \dfrac{\ln(1 + x)}{(1 + x)^2} ~ \mathrm{d}x
      = \left[ -\dfrac{\ln(1+x)}{1 + x} \right]_0^{+\infty} + \int_0^{+\infty} \dfrac{\mathrm{d}x}{(1 + x)^2}
      = 0 + 1 = 1.

   (7). 这是瑕积分 (在 :math:`x = 0` 处). 分部积分 (:math:`u = \ln^2 x`, :math:`v = x`):

   .. math::
      \int_0^1 \ln^2 x ~ \mathrm{d}x = \left[ x \ln^2 x \right]_0^1 - 2 \int_0^1 \ln x ~ \mathrm{d}x = 0 - 2 \left( \left[ x \ln x \right]_0^1 - \int_0^1 \mathrm{d}x \right) = 2,

   其中用到 :math:`\lim\limits_{x \to 0^+} x \ln x = 0` 与 :math:`\lim\limits_{x \to 0^+} x \ln^2 x = 0`, 故收敛, 值为 :math:`2`.

   (8). 令 :math:`x = \sin t` (:math:`t: 0 \to \dfrac{\pi}{2}`), :math:`\sqrt{1 - x^2} = \cos t`, :math:`\mathrm{d}x = \cos t ~ \mathrm{d}t`:

   .. math::
      \int_0^1 \dfrac{x ~ \mathrm{d}x}{(2 - x^2)\sqrt{1 - x^2}}
      = \int_0^{\frac{\pi}{2}} \dfrac{\sin t ~ \mathrm{d}t}{2 - \sin^2 t}
      = \int_0^{\frac{\pi}{2}} \dfrac{\sin t ~ \mathrm{d}t}{1 + \cos^2 t}
      = \left[ -\arctan \left( \cos t \right) \right]_0^{\frac{\pi}{2}} = \dfrac{\pi}{4}.

   (9). 令 :math:`x = \sin^2 t` (:math:`t: 0 \to \dfrac{\pi}{2}`), :math:`\mathrm{d}x = 2 \sin t \cos t ~ \mathrm{d}t`:

   .. math::
      \int_0^1 \sqrt{\dfrac{x}{1 - x}} ~ \mathrm{d}x
      = \int_0^{\frac{\pi}{2}} \dfrac{\sin t}{\cos t} \cdot 2 \sin t \cos t ~ \mathrm{d}t
      = 2 \int_0^{\frac{\pi}{2}} \sin^2 t ~ \mathrm{d}t
      = 2 \cdot \dfrac{\pi}{4} = \dfrac{\pi}{2}.

   (10). 令 :math:`x = \sec t` (:math:`t: 0 \to \dfrac{\pi}{2}`), :math:`\sqrt{x^2 - 1} = \tan t`, :math:`\mathrm{d}x = \sec t \tan t ~ \mathrm{d}t`:

   .. math::
      \int_1^{+\infty} \dfrac{\mathrm{d}x}{x \sqrt{x^2 - 1}} = \int_0^{\frac{\pi}{2}} \mathrm{d}t = \dfrac{\pi}{2}.

.. _ex-chap6-sec5-ex2:

2. 当 :math:`k` 为何值时, 广义积分 :math:`\displaystyle \int_2^{+\infty} \dfrac{\mathrm{d}x}{x (\ln x)^k}`
   收敛?

.. proof:solution::

   令 :math:`u = \ln x`, :math:`\mathrm{d}u = \dfrac{\mathrm{d}x}{x}`; :math:`x: 2 \to +\infty` 对应 :math:`u: \ln 2 \to +\infty`:

   .. math::
      \int_2^{+\infty} \dfrac{\mathrm{d}x}{x (\ln x)^k} = \int_{\ln 2}^{+\infty} \dfrac{\mathrm{d}u}{u^k}.

   由幂函数广义积分的结论: 当 :math:`k > 1` 时收敛, 值为 :math:`\dfrac{(\ln 2)^{1 - k}}{k - 1}`;
   当 :math:`k \leqslant 1` 时发散 (:math:`k = 1` 时为对数积分 :math:`[\ln \ln x]_2^{+\infty}`, :math:`k < 1` 时为
   :math:`\dfrac{u^{1-k}}{1-k} \to +\infty`).

   故仅当 :math:`k > 1` 时积分收敛.

.. _ex-chap6-sec5-ex3:

3. 讨论广义积分 :math:`\displaystyle \int_a^b \dfrac{\mathrm{d}x}{(b - x)^p}` 和
   :math:`\displaystyle \int_a^b \dfrac{\mathrm{d}x}{(x - a)^p}` 的敛散性.

.. proof:solution::

   两积分分别以 :math:`x = b` 和 :math:`x = a` 为瑕点, 只需讨论其一, 另一个由对称性 (:math:`x \to a + b - x`) 同理.

   对 :math:`\displaystyle \int_a^b \dfrac{\mathrm{d}x}{(b - x)^p}`, 任取 :math:`\varepsilon \in (0, b - a)`, 计算

   .. math::
      \int_a^{b - \varepsilon} \dfrac{\mathrm{d}x}{(b - x)^p} = \begin{cases}
         \left[ \dfrac{(b - x)^{1 - p}}{p - 1} \right]_a^{b - \varepsilon}
         = \dfrac{\varepsilon^{1 - p} - (b - a)^{1 - p}}{p - 1}, & p > 1, \\[3mm]
         \left[ \dfrac{(b - x)^{1 - p}}{1 - p} \right]_a^{b - \varepsilon}
         = \dfrac{(b - a)^{1 - p} - \varepsilon^{1 - p}}{1 - p}, & 0 < p < 1.
      \end{cases}

   当 :math:`p > 1` 时 :math:`1 - p < 0`, :math:`\varepsilon^{1-p} \to +\infty` (:math:`\varepsilon \to 0^+`), 积分发散;

   当 :math:`0 < p < 1` 时 :math:`\varepsilon^{1 - p} \to 0`, 积分收敛, 值为 :math:`\dfrac{(b - a)^{1 - p}}{1 - p}`;

   当 :math:`p = 1` 时 :math:`\displaystyle \int_a^{b-\varepsilon} \dfrac{\mathrm{d}x}{b - x} = \ln(b - a) - \ln \varepsilon \to +\infty`, 发散.

   综上: 两积分都在 :math:`p < 1` 时收敛, 在 :math:`p \geqslant 1` 时发散 (其中约定 :math:`p > 0`;
   :math:`p \leqslant 0` 时被积函数在 :math:`[a, b]` 上连续, 是通常的定积分).

.. _ex-chap6-sec5-ex4:

4. 证明: :math:`\displaystyle \int_{-\infty}^{+\infty} e^{-x^2} ~ \mathrm{d}x
   = 2 \int_0^{+\infty} e^{-x^2} ~ \mathrm{d}x
   = \int_0^{+\infty} \dfrac{e^{-x}}{\sqrt{x}} ~ \mathrm{d}x`.

.. proof:solution::

   第一个等号: :math:`e^{-x^2}` 是偶函数, 且 :math:`\displaystyle \int_0^{+\infty} e^{-x^2} ~ \mathrm{d}x` 收敛
   (因 :math:`e^{-x^2} \leqslant e^{-x}` 而 :math:`\displaystyle \int_0^{+\infty} e^{-x} ~ \mathrm{d}x = 1`),
   由奇偶对称性,

   .. math::
      \int_{-\infty}^{+\infty} e^{-x^2} ~ \mathrm{d}x = \int_{-\infty}^{0} e^{-x^2} ~ \mathrm{d}x + \int_0^{+\infty} e^{-x^2} ~ \mathrm{d}x
      = 2 \int_0^{+\infty} e^{-x^2} ~ \mathrm{d}x.

   第二个等号: 对右边积分作换元 :math:`x^2 = t`, 即 :math:`x = \sqrt{t}`, :math:`\mathrm{d}x = \dfrac{\mathrm{d}t}{2\sqrt{t}}`;
   :math:`x: 0 \to +\infty` 对应 :math:`t: 0 \to +\infty`, 于是

   .. math::
      2 \int_0^{+\infty} e^{-x^2} ~ \mathrm{d}x
      = 2 \int_0^{+\infty} e^{-t} \cdot \dfrac{\mathrm{d}t}{2 \sqrt{t}}
      = \int_0^{+\infty} \dfrac{e^{-t}}{\sqrt{t}} ~ \mathrm{d}t
      = \int_0^{+\infty} \dfrac{e^{-x}}{\sqrt{x}} ~ \mathrm{d}x.

   (其中后一步把积分变量记号 :math:`t` 改写为 :math:`x`.) 综上三式相等, 证毕.

.. _ex-chap6-sec6:

§6.6 定积分的几何应用
------------------------------------

.. _ex-chap6-sec6-ex1:

1. 计算由下列各曲线所围成的图形的面积.

   (1) :math:`y = x^2` 和 :math:`y = 2x - x^2`; \qquad
   (2) :math:`y = x - 1` 和 :math:`y^2 = 2x + 6`;

   (3) :math:`y = \ln x`, :math:`x = ey` 和 :math:`y = 0`; \qquad
   (4) :math:`y = \dfrac{1}{x}`, :math:`y = \dfrac{1}{x^2}` 和 :math:`x = 2`;

   (5) :math:`x = 5y^2` 和 :math:`x = 1 + y^2`; \qquad
   (6) 曲线 :math:`y = \sin x`, :math:`y = \cos x` 和直线 :math:`x = 0`, :math:`x = \pi`.

.. proof:solution::

   (1). 交点: :math:`x^2 = 2x - x^2 \Rightarrow x = 0, 1`. 在 :math:`[0, 1]` 上 :math:`2x - x^2 \geqslant x^2`,

   .. math::
      S = \int_0^1 \left[ (2x - x^2) - x^2 \right] \mathrm{d}x = \int_0^1 (2x - 2x^2) ~ \mathrm{d}x = 1 - \dfrac{2}{3} = \dfrac{1}{3}.

   (2). 以 :math:`y` 为积分变量较方便: :math:`y = x - 1 \Rightarrow x = y + 1`; :math:`y^2 = 2x + 6 \Rightarrow x = \dfrac{y^2 - 6}{2}`.
   交点: :math:`y + 1 = \dfrac{y^2 - 6}{2} \Rightarrow y^2 - 2y - 8 = 0 \Rightarrow y = 4, -2`. 在
   :math:`[-2, 4]` 上 :math:`y + 1 \geqslant \dfrac{y^2 - 6}{2}`,

   .. math::
      S = \int_{-2}^4 \left[ (y + 1) - \dfrac{y^2 - 6}{2} \right] \mathrm{d}y
      = \int_{-2}^4 \left( y + 4 - \dfrac{y^2}{2} \right) \mathrm{d}y
      = \left[ \dfrac{y^2}{2} + 4y - \dfrac{y^3}{6} \right]_{-2}^4 = 18.

   (3). 三条边界: :math:`y = \ln x` (即 :math:`x = e^y`)、直线 :math:`x = ey` (过原点) 与 :math:`y = 0`. 曲线与直线的交点:
   :math:`e^y = ey \Leftrightarrow e^{y-1} = y`, 唯一解 :math:`y = 1` (令 :math:`g(y) = e^{y-1} - y`, 则
   :math:`g'(y) = e^{y-1} - 1 \leqslant 0` 于 :math:`[0,1]`, :math:`g(1) = 0`, :math:`g(0) = e^{-1} > 0`). 于是区域以
   :math:`y` 为积分变量: :math:`y \in [0, 1]`, 右边界 :math:`x = e^y`, 左边界 :math:`x = ey`, 且当
   :math:`0 \leqslant y \leqslant 1` 时 :math:`e^y \geqslant ey`,

   .. math::
      S = \int_0^1 \left( e^y - ey \right) \mathrm{d}y
      = \left[ e^y - \dfrac{e y^2}{2} \right]_0^1
      = \left( e - \dfrac{e}{2} \right) - 1 = \dfrac{e}{2} - 1.

   (4). 两曲线交于 :math:`x = 1` (:math:`\dfrac{1}{x} = \dfrac{1}{x^2} \Rightarrow x = 1`); 直线 :math:`x = 2`.
   在 :math:`[1, 2]` 上 :math:`\dfrac{1}{x} \geqslant \dfrac{1}{x^2}`,

   .. math::
      S = \int_1^2 \left( \dfrac{1}{x} - \dfrac{1}{x^2} \right) \mathrm{d}x
      = \left[ \ln x + \dfrac{1}{x} \right]_1^2 = \ln 2 + \dfrac{1}{2} - 1 = \ln 2 - \dfrac{1}{2}.

   (5). 交点: :math:`5y^2 = 1 + y^2 \Rightarrow y = \pm \dfrac{1}{2}`. 以 :math:`y` 为积分变量, 在
   :math:`\left[ -\dfrac{1}{2}, \dfrac{1}{2} \right]` 上 :math:`1 + y^2 \geqslant 5y^2`,

   .. math::
      S = \int_{-\frac{1}{2}}^{\frac{1}{2}} \left[ (1 + y^2) - 5y^2 \right] \mathrm{d}y
      = \int_{-\frac{1}{2}}^{\frac{1}{2}} (1 - 4y^2) ~ \mathrm{d}y
      = 2 \left[ y - \dfrac{4y^3}{3} \right]_0^{\frac{1}{2}} = 2 \left( \dfrac{1}{2} - \dfrac{1}{6} \right) = \dfrac{2}{3}.

   (6). 在 :math:`\left[ 0, \dfrac{\pi}{4} \right]` 上 :math:`\cos x \geqslant \sin x`; 在
   :math:`\left[ \dfrac{\pi}{4}, \pi \right]` 上 :math:`\sin x \geqslant \cos x`,

   .. math::
      S & = \int_0^{\frac{\pi}{4}} (\cos x - \sin x) ~ \mathrm{d}x + \int_{\frac{\pi}{4}}^{\pi} (\sin x - \cos x) ~ \mathrm{d}x \\
        & = \left[ \sin x + \cos x \right]_0^{\frac{\pi}{4}} + \left[ -\cos x - \sin x \right]_{\frac{\pi}{4}}^{\pi} \\
        & = (\sqrt{2} - 1) + (1 + \sqrt{2}) = 2\sqrt{2}.

.. _ex-chap6-sec6-ex2:

2. 计算由下列各曲线所围成的图形的面积.

   (1) :math:`r = e^{\frac{\theta}{2}}` (:math:`\dfrac{\pi}{2} \leqslant \theta \leqslant \pi`); \qquad
   (2) :math:`r^2 = 9 \sin 2\theta` (:math:`0 \leqslant \theta \leqslant \dfrac{\pi}{2}`);

   (3) :math:`r = 3 + 2 \cos \theta`; \qquad
   (4) :math:`r = 3 \cos \theta`.

.. proof:solution::

   极坐标面积公式 :math:`S = \dfrac{1}{2} \displaystyle \int_\alpha^\beta r^2(\theta) ~ \mathrm{d}\theta`:

   (1). :math:`S = \dfrac{1}{2} \displaystyle \int_{\frac{\pi}{2}}^{\pi} e^{\theta} ~ \mathrm{d}\theta
   = \dfrac{1}{2} \left[ e^{\theta} \right]_{\frac{\pi}{2}}^{\pi} = \dfrac{e^{\pi} - e^{\frac{\pi}{2}}}{2}`.

   (2). :math:`S = \dfrac{1}{2} \displaystyle \int_0^{\frac{\pi}{2}} 9 \sin 2\theta ~ \mathrm{d}\theta
   = \dfrac{9}{4} \left[ -\cos 2\theta \right]_0^{\frac{\pi}{2}} = \dfrac{9}{4} (1 + 1) = \dfrac{9}{2}`.

   (3). 对称于极轴, 取 :math:`\theta \in [0, \pi]` 加倍:

   .. math::
      S = \int_0^{\pi} (3 + 2 \cos \theta)^2 ~ \mathrm{d}\theta
      = \int_0^{\pi} \left( 9 + 12 \cos \theta + 4 \cos^2 \theta \right) \mathrm{d}\theta
      = 9\pi + 0 + 4 \cdot \dfrac{\pi}{2} = 11\pi.

   (4). :math:`r = 3\cos\theta` 是过极点、直径为 :math:`3` 的圆 (:math:`x^2 + y^2 = 3x`), 面积
   :math:`\pi \left( \dfrac{3}{2} \right)^2 = \dfrac{9\pi}{4}`; 或按公式:

   .. math::
      S = \dfrac{1}{2} \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} 9 \cos^2 \theta ~ \mathrm{d}\theta
      = \dfrac{9}{2} \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \dfrac{1 + \cos 2\theta}{2} ~ \mathrm{d}\theta
      = \dfrac{9\pi}{4}.

.. _ex-chap6-sec6-ex3:

3. 求星形线 :math:`x^{\frac{2}{3}} + y^{\frac{2}{3}} = a^{\frac{2}{3}}` 所围成的图形面积 :math:`S`.

.. proof:solution::

   星形线关于两坐标轴对称, 用参数方程 :math:`x = a \cos^3 t`, :math:`y = a \sin^3 t` (:math:`a > 0`),
   取第一象限部分 (:math:`t: \dfrac{\pi}{2} \to 0` 对应 :math:`x: 0 \to a`) 面积的四倍:

   .. math::
      S = 4 \int_0^a y ~ \mathrm{d}x = 4 \int_{\frac{\pi}{2}}^{0} a \sin^3 t \cdot 3a \cos^2 t \cdot (-\sin t) ~ \mathrm{d}t
      = 12 a^2 \int_0^{\frac{\pi}{2}} \sin^4 t \cos^2 t ~ \mathrm{d}t.

   计算 :math:`\displaystyle \int_0^{\frac{\pi}{2}} \sin^4 t \cos^2 t ~ \mathrm{d}t`: 由华里士 (Wallis) 公式,

   .. math::
      \int_0^{\frac{\pi}{2}} \sin^4 t \cos^2 t ~ \mathrm{d}t
      = \dfrac{3 \cdot 1 \cdot 1}{6 \cdot 4 \cdot 2} \cdot \dfrac{\pi}{2} = \dfrac{\pi}{32}.

   故

   .. math::
      S = 12 a^2 \cdot \dfrac{\pi}{32} = \dfrac{3\pi a^2}{8}.

.. _ex-chap6-sec6-ex4:

4. 求由摆线 :math:`x = a(t - \sin t)`, :math:`y = a(1 - \cos t)` 的一拱与 :math:`x` 轴所围成的图形面积
   :math:`S`.

.. proof:solution::

   一拱对应 :math:`t: 0 \to 2\pi` (:math:`x: 0 \to 2\pi a`, :math:`y \geqslant 0`). 由参数方程求面积公式:

   .. math::
      S = \int_0^{2\pi a} y ~ \mathrm{d}x = \int_0^{2\pi} a(1 - \cos t) \cdot a(1 - \cos t) ~ \mathrm{d}t
      = a^2 \int_0^{2\pi} (1 - \cos t)^2 ~ \mathrm{d}t.

   展开: :math:`(1 - \cos t)^2 = 1 - 2\cos t + \cos^2 t`, 积分值 :math:`2\pi - 0 + \pi = 3\pi`, 故

   .. math::
      S = 3\pi a^2.

.. _ex-chap6-sec6-ex5:

5. 计算下列各弧长.

   (1) 曲线 :math:`y = \dfrac{1}{2} x^2` 相应于 :math:`0 \leqslant x \leqslant 1` 的一段弧;

   (2) 曲线 :math:`y = \dfrac{x^3}{3} + \dfrac{1}{4x}` 相应于 :math:`1 \leqslant x \leqslant 2` 的一段弧;

   (3) 曲线 :math:`y = \displaystyle \int_0^x \tan t ~ \mathrm{d}t` 相应于
       :math:`0 \leqslant x \leqslant \dfrac{\pi}{4}` 的一段弧;

   (4) 曲线 :math:`y = \ln \sec x` 相应于 :math:`0 \leqslant x \leqslant \dfrac{\pi}{4}` 的一段弧.

.. proof:solution::

   弧长公式 :math:`s = \displaystyle \int_a^b \sqrt{1 + y'^2} ~ \mathrm{d}x`:

   (1). :math:`y' = x`, :math:`s = \displaystyle \int_0^1 \sqrt{1 + x^2} ~ \mathrm{d}x
   = \dfrac{1}{2} \left[ x \sqrt{1 + x^2} + \ln \left( x + \sqrt{1 + x^2} \right) \right]_0^1
   = \dfrac{1}{2} \left[ \sqrt{2} + \ln \left( 1 + \sqrt{2} \right) \right]`.

   (2). :math:`y' = x^2 - \dfrac{1}{4x^2}`, 于是

   .. math::
      1 + y'^2 = 1 + x^4 - \dfrac{1}{2} + \dfrac{1}{16x^4} = x^4 + \dfrac{1}{2} + \dfrac{1}{16x^4}
      = \left( x^2 + \dfrac{1}{4x^2} \right)^2,

   故

   .. math::
      s = \int_1^2 \left( x^2 + \dfrac{1}{4x^2} \right) \mathrm{d}x
      = \left[ \dfrac{x^3}{3} - \dfrac{1}{4x} \right]_1^2
      = \left( \dfrac{8}{3} - \dfrac{1}{8} \right) - \left( \dfrac{1}{3} - \dfrac{1}{4} \right) = \dfrac{59}{24}.

   (3). :math:`y' = \tan x` (:math:`y = -\ln \cos x`), 故

   .. math::
      s = \int_0^{\frac{\pi}{4}} \sqrt{1 + \tan^2 x} ~ \mathrm{d}x
      = \int_0^{\frac{\pi}{4}} \sec x ~ \mathrm{d}x
      = \left[ \ln \left\lvert \sec x + \tan x \right\rvert \right]_0^{\frac{\pi}{4}}
      = \ln \left( \sqrt{2} + 1 \right).

   (4). :math:`y = \ln \sec x`, 由复合函数求导法则 :math:`y' = \dfrac{(\sec x)'}{\sec x} = \dfrac{\sec x \tan x}{\sec x} = \tan x`
   (事实上 :math:`y = \ln \sec x = -\ln \cos x`, 与 (3) 的曲线完全相同), 于是同 (3):

   .. math::
      s = \int_0^{\frac{\pi}{4}} \sec x ~ \mathrm{d}x = \ln \left( \sqrt{2} + 1 \right).

.. _ex-chap6-sec6-ex6:

6. 计算摆线 :math:`x = a(t - \sin t)`, :math:`y = a(1 - \cos t)` (:math:`a > 0`) 一拱
   (:math:`0 \leqslant t \leqslant 2\pi`) 的长度.

.. proof:solution::

   :math:`\dfrac{\mathrm{d}x}{\mathrm{d}t} = a(1 - \cos t)`, :math:`\dfrac{\mathrm{d}y}{\mathrm{d}t} = a \sin t`, 于是

   .. math::
      \sqrt{\left( \dfrac{\mathrm{d}x}{\mathrm{d}t} \right)^2 + \left( \dfrac{\mathrm{d}y}{\mathrm{d}t} \right)^2}
      = a \sqrt{(1 - \cos t)^2 + \sin^2 t}
      = a \sqrt{2 - 2 \cos t}
      = 2a \left\lvert \sin \dfrac{t}{2} \right\rvert.

   当 :math:`t \in [0, 2\pi]` 时 :math:`\sin \dfrac{t}{2} \geqslant 0`, 故

   .. math::
      s = \int_0^{2\pi} 2a \sin \dfrac{t}{2} ~ \mathrm{d}t
      = 2a \left[ -2 \cos \dfrac{t}{2} \right]_0^{2\pi} = 2a (2 + 2) = 8a.

.. _ex-chap6-sec6-ex7:

7. 求抛物线 :math:`r = \dfrac{3}{1 + \cos \theta}` 在 :math:`-\dfrac{\pi}{2} \leqslant \theta \leqslant
   \dfrac{\pi}{2}` 之间的一段弧长.

.. proof:solution::

   :math:`r'(\theta) = \dfrac{3 \sin \theta}{(1 + \cos \theta)^2}`, 于是

   .. math::
      r^2 + r'^2 = \dfrac{9}{(1 + \cos \theta)^2} + \dfrac{9 \sin^2 \theta}{(1 + \cos \theta)^4}
      = \dfrac{9 \left[ (1 + \cos \theta)^2 + \sin^2 \theta \right]}{(1 + \cos \theta)^4}
      = \dfrac{9 \left( 2 + 2 \cos \theta \right)}{(1 + \cos \theta)^4}
      = \dfrac{18}{(1 + \cos \theta)^3}.

   利用半角公式 :math:`1 + \cos \theta = 2 \cos^2 \dfrac{\theta}{2}` (在 :math:`\left[ -\frac{\pi}{2}, \frac{\pi}{2} \right]` 上非负),

   .. math::
      \sqrt{r^2 + r'^2} = \dfrac{3\sqrt{2}}{\left( 2 \cos^2 \frac{\theta}{2} \right)^{\frac{3}{2}}}
      = \dfrac{3}{2} \sec^3 \dfrac{\theta}{2}.

   由极坐标弧长公式 (:math:`s = \displaystyle \int \sqrt{r^2 + r'^2} ~ \mathrm{d}\theta`, 见 :ref:`补充内容 <extra-chap6-topic3>`),
   令 :math:`u = \dfrac{\theta}{2}` (:math:`\mathrm{d}\theta = 2 ~ \mathrm{d}u`), 并利用被积函数的偶性:

   .. math::
      s = \dfrac{3}{2} \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \sec^3 \dfrac{\theta}{2} ~ \mathrm{d}\theta
      = 3 \int_{-\frac{\pi}{4}}^{\frac{\pi}{4}} \sec^3 u ~ \mathrm{d}u
      = 6 \int_0^{\frac{\pi}{4}} \sec^3 u ~ \mathrm{d}u.

   由 :math:`\displaystyle \int \sec^3 u ~ \mathrm{d}u = \dfrac{1}{2} \left[ \sec u \tan u + \ln \left\lvert \sec u + \tan u \right\rvert \right] + C`,

   .. math::
      s = 3 \left[ \sec u \tan u + \ln \left\lvert \sec u + \tan u \right\rvert \right]_0^{\frac{\pi}{4}}
      = 3 \left[ \sqrt{2} + \ln \left( \sqrt{2} + 1 \right) \right].

.. _ex-chap6-sec6-ex8:

8. 求下列各立体的体积.

   (1) 由曲线 :math:`y = \sqrt{x - 1}`, :math:`x = 5` 和 :math:`x` 轴围成的图形绕 :math:`x` 轴旋转所得的旋转体;

   (2) 由曲线 :math:`y = x^2` 和 :math:`y = 2 - x^2` 围成的图形绕 :math:`x` 轴旋转所得的旋转体;

   (3) 由曲线 :math:`y = \sqrt{x} \sin x` (:math:`0 \leqslant x \leqslant 1`) 和 :math:`x` 轴围成的图形绕
       :math:`x` 轴旋转所得的旋转体;

   (4) 由曲线 :math:`y = \dfrac{1}{2} x^2`, :math:`y = \dfrac{1}{1 + x^2}` 和 :math:`y` 轴围成的图形绕
       :math:`y` 轴旋转所得的旋转体.

.. proof:solution::

   (1). 旋转体半径 :math:`R(x) = \sqrt{x - 1}`, :math:`x \in [1, 5]`:

   .. math::
      V = \pi \int_1^5 (x - 1) ~ \mathrm{d}x = \pi \left[ \dfrac{(x-1)^2}{2} \right]_1^5 = 8\pi.

   (2). 两曲线交于 :math:`x = \pm 1`; 对 :math:`x \in [-1, 1]`, 外半径 :math:`R = 2 - x^2`, 内半径 :math:`r = x^2`:

   .. math::
      V = \pi \int_{-1}^1 \left[ (2 - x^2)^2 - x^4 \right] \mathrm{d}x
      = \pi \int_{-1}^1 (4 - 4x^2) ~ \mathrm{d}x
      = \pi \left( 8 - \dfrac{8}{3} \right) = \dfrac{16\pi}{3}.

   (3). :math:`V = \pi \displaystyle \int_0^1 y^2 ~ \mathrm{d}x = \pi \int_0^1 x \sin^2 x ~ \mathrm{d}x`.
   由 :math:`\sin^2 x = \dfrac{1 - \cos 2x}{2}` 及分部积分:

   .. math::
      \int_0^1 x \sin^2 x ~ \mathrm{d}x
      = \dfrac{1}{2} \int_0^1 x ~ \mathrm{d}x - \dfrac{1}{2} \int_0^1 x \cos 2x ~ \mathrm{d}x
      = \dfrac{1}{4} - \dfrac{1}{2} \left( \left[ \dfrac{x \sin 2x}{2} \right]_0^1 - \dfrac{1}{2} \int_0^1 \sin 2x ~ \mathrm{d}x \right)
      = \dfrac{1}{4} - \dfrac{\sin 2}{4} - \dfrac{\cos 2}{8} + \dfrac{1}{8}
      = \dfrac{3}{8} - \dfrac{\sin 2}{4} - \dfrac{\cos 2}{8},

   故

   .. math::
      V = \pi \left( \dfrac{3}{8} - \dfrac{\sin 2}{4} - \dfrac{\cos 2}{8} \right)
      = \dfrac{\pi}{8} \left( 3 - 2 \sin 2 - \cos 2 \right).

   (4). 两曲线交点: :math:`\dfrac{x^2}{2} = \dfrac{1}{1 + x^2} \Rightarrow x^4 + x^2 - 2 = 0 \Rightarrow x = 1`
   (交于 :math:`(1, \dfrac{1}{2})`); 抛物线过原点, 双曲线在 :math:`x = 0` 处 :math:`y = 1`. 围成的区域:
   :math:`0 \leqslant x \leqslant 1`, :math:`\dfrac{x^2}{2} \leqslant y \leqslant \dfrac{1}{1 + x^2}`.

   绕 :math:`y` 轴旋转, 按水平切片 (垫圈法): 对 :math:`0 \leqslant y \leqslant \dfrac{1}{2}`, 右边界是抛物线
   :math:`x = \sqrt{2y}` (此时 :math:`\sqrt{2y} \leqslant \sqrt{\frac{1}{y} - 1}`, 因为该式等价于 :math:`y \leqslant \dfrac{1}{2}`);
   对 :math:`\dfrac{1}{2} \leqslant y \leqslant 1`, 右边界是 :math:`x = \sqrt{\dfrac{1}{y} - 1}`. 于是

   .. math::
      V = \pi \int_0^{\frac{1}{2}} 2y ~ \mathrm{d}y + \pi \int_{\frac{1}{2}}^1 \left( \dfrac{1}{y} - 1 \right) \mathrm{d}y
      = \dfrac{\pi}{4} + \pi \left[ \ln y - y \right]_{\frac{1}{2}}^1
      = \dfrac{\pi}{4} + \pi \left( -1 + \ln 2 + \dfrac{1}{2} \right)
      = \pi \left( \ln 2 - \dfrac{1}{4} \right).

.. _ex-chap6-sec6-ex9:

9. 在曲线 :math:`y = x^2` (:math:`x \geqslant 0`) 上某点 :math:`A` 处作一切线, 使之与曲线及 :math:`x` 轴所围成的
   图形面积为 :math:`\dfrac{1}{12}`, 试求:

   (1) 过切点 :math:`A` 的切线方程;

   (2) 上述所围图形绕 :math:`x` 轴旋转所得旋转体的体积.

.. proof:solution::

   设切点 :math:`A = (a, a^2)` (:math:`a > 0`). :math:`y' = 2x`, 切线: :math:`y = 2a(x - a) + a^2 = 2ax - a^2`.
   切线与 :math:`x` 轴交于 :math:`x = \dfrac{a}{2}`; 曲线过原点.

   (1). 所围图形由 :math:`x` 轴 (从原点到 :math:`(\frac{a}{2}, 0)`)、切线 (从 :math:`(\frac{a}{2},0)` 到 :math:`A`) 与曲线
   (从 :math:`A` 回到原点) 围成. 面积

   .. math::
      S = \int_0^{\frac{a}{2}} x^2 ~ \mathrm{d}x + \int_{\frac{a}{2}}^a \left[ x^2 - (2ax - a^2) \right] \mathrm{d}x.

   第一段: :math:`\dfrac{1}{3} \cdot \dfrac{a^3}{8} = \dfrac{a^3}{24}`. 第二段: :math:`x^2 - 2ax + a^2 = (x-a)^2`,

   .. math::
      \int_{\frac{a}{2}}^a (x - a)^2 ~ \mathrm{d}x = \left[ \dfrac{(x - a)^3}{3} \right]_{\frac{a}{2}}^a = \dfrac{1}{3} \cdot \dfrac{a^3}{8} = \dfrac{a^3}{24}.

   故 :math:`S = \dfrac{a^3}{12} = \dfrac{1}{12}`, 解得 :math:`a = 1`. 切点 :math:`A = (1, 1)`, 切线方程为

   .. math::
      y = 2x - 1.

   (2). 绕 :math:`x` 轴旋转: 对 :math:`0 \leqslant x \leqslant \dfrac{1}{2}`, 区域由曲线 :math:`y = x^2` 与 :math:`x` 轴围出,
   旋转半径为 :math:`x^2`; 对 :math:`\dfrac{1}{2} \leqslant x \leqslant 1`, 用垫圈法, 外半径 :math:`x^2` (曲线)、内半径
   :math:`2x - 1` (切线, 非负). 于是

   .. math::
      V = \pi \int_0^{\frac{1}{2}} x^4 ~ \mathrm{d}x + \pi \int_{\frac{1}{2}}^1 \left[ x^4 - (2x - 1)^2 \right] \mathrm{d}x.

   第一项: :math:`\pi \cdot \dfrac{1}{5} \cdot \dfrac{1}{32} = \dfrac{\pi}{160}`. 第二项展开计算:

   .. math::
      \int_{\frac{1}{2}}^1 \left[ x^4 - 4x^2 + 4x - 1 \right] \mathrm{d}x
      = \left[ \dfrac{x^5}{5} - \dfrac{4x^3}{3} + 2x^2 - x \right]_{\frac{1}{2}}^1
      = -\dfrac{2}{15} - \left( \dfrac{1}{160} - \dfrac{1}{6} \right)
      = -\dfrac{2}{15} + \dfrac{77}{480} = \dfrac{13}{480}.

   故

   .. math::
      V = \dfrac{\pi}{160} + \dfrac{13\pi}{480} = \dfrac{3\pi + 13\pi}{480} = \dfrac{\pi}{30}.

.. _extra-chap6:

补充内容
====================================

.. _extra-chap6-topic1:

1. 求定积分 :math:`\displaystyle \int_{-1}^1 \dfrac{e^x + e^{-x}}{1 + 3^x} \mathrm{d}x`.

.. proof:solution::

   .. math::
      \int_{-1}^1 \dfrac{e^x + e^{-x}}{1 + 3^x} \mathrm{d}x & = \left(\int_{-1}^0 + \int_0^1 \right) \dfrac{e^x + e^{-x}}{1 + 3^x} \mathrm{d}x \\
      & = \int_{1}^0 \dfrac{e^{-x} + e^{x}}{1 + 3^{-x}} \mathrm{d}(-x) + \int_0^1 \dfrac{e^x + e^{-x}}{1 + 3^x} \mathrm{d}x \\
      & = \int_0^1 3^x \cdot \dfrac{e^{-x} + e^{x}}{1 + 3^x} \mathrm{d}x + \int_0^1 \dfrac{e^x + e^{-x}}{1 + 3^x} \mathrm{d}x \\
      & = \int_0^1 \left( 3^x + 1 \right) \cdot \dfrac{e^{-x} + e^{x}}{1 + 3^x} \mathrm{d}x \\
      & = \int_0^1 e^{-x} + e^{x} \mathrm{d}x \\
      & = \left. \left( -e^{-x} + e^{x} \right) \right|_0^1 \\
      & = e - \dfrac{1}{e}.

   .. note::
      被积函数 :math:`\dfrac{e^x + e^{-x}}{1 + 3^x}` 分母里的 :math:`3` 替换为任何正实数, 定积分的值都是 :math:`e - \dfrac{1}{e}`.

.. _extra-chap6-topic2:

2. 计算定积分 :math:`\displaystyle I = \int_0^2 \dfrac{(x-1)^2 + 1}{(x-1)^2 + x^2(x-2)^2} \mathrm{d}x`.

.. proof:solution::

   做变量替换 :math:`t = x - 1`, 则原积分变为

   .. math::
      :label: eq-extra-chap6-topic2-1

      I & = \int_{-1}^1 \dfrac{t^2 + 1}{t^2 + (t+1)^2 (t-1)^2} \mathrm{d}t
          = \int_{-1}^1 \dfrac{t^2 + 1}{t^2 + (t^2-1)^2} \mathrm{d}t \\
        & = \int_{-1}^1 \dfrac{1 + 1/t^2}{1 + (t - 1/t)^2} \mathrm{d}t
          = \int_{-1}^1 \dfrac{\mathrm{d} \left( t - 1/t \right)}{1 + (t - 1/t)^2}.

   令 :math:`u = t - 1/t`. 注意, 此时区间 :math:`t \in [-1, 1]` 应分为 :math:`[-1, 0)` 和 :math:`(0, 1]` 两部分,
   这样才是光滑 (处处可导) 的变换. 这两个区间分别对应 :math:`u \in [0, +\infty)` 和 :math:`u \in (-\infty, 0]`.
   因此, 原积分可写为

   .. math::
      I & = \int_{0}^{+\infty} \dfrac{\mathrm{d}u}{1 + u^2} + \int_{-\infty}^{0} \dfrac{\mathrm{d}u}{1 + u^2} \\
        & = \int_{0}^{+\infty} \dfrac{\mathrm{d}u}{1 + u^2} + \int_{0}^{+\infty} \dfrac{\mathrm{d}v}{1 + v^2} \\
        & = 2 \int_{0}^{+\infty} \dfrac{\mathrm{d}u}{1 + u^2} = 2 \left. \arctan u \right|_0^{+\infty} \\
        & = 2 \cdot \dfrac{\pi}{2} = \pi.

   .. note::
      注意在变换过程中, 由于 :math:`t = 0` 时, 被积函数无定义, 因此需要分开积分, 也就是说,
      这题 **不能** 直接从 :eq:`eq-extra-chap6-topic2-1` 得

      .. math::
         I = \left. \arctan \left( t - \dfrac{1}{t} \right) \right|_{-1}^1 = \arctan 0 - \arctan 0 = 0.

.. _extra-chap6-topic3:

3. 极坐标下曲线 :math:`r = r(\theta)` 求曲线长公式推导.

.. proof:solution::

   由定义, 弧长为折线段长度和的极限, 记 :math:`\mathrm{d} \ell` 为弧长元素 (折线长), 那么 :math:`r(\theta)`, :math:`r(\theta + \mathrm{d} \theta)`,
   :math:`\mathrm{d} \ell` 三者构成一个三角形, 由余弦定理有

   .. math::
      (\mathrm{d} \ell)^2 = r^2(\theta) + r^2(\theta + \mathrm{d} \theta) - 2 r(\theta) r(\theta + \mathrm{d} \theta) \cos \mathrm{d} \theta.

   假设 :math:`r(\theta)` 在 :math:`[\alpha, \beta]` 上足够光滑 (连续可导), 那么

   .. math::
      r(\theta + \mathrm{d} \theta) = r(\theta) + r'(\theta) \mathrm{d} \theta + o(\mathrm{d} \theta),

   于是有

   .. math::
      (\mathrm{d} \ell)^2
      & = r^2(\theta) + r^2(\theta + \mathrm{d} \theta) - 2 r(\theta) r(\theta + \mathrm{d} \theta) \cos \mathrm{d} \theta \\
      & = (r(\theta) - r(\theta + \mathrm{d} \theta))^2 + 2 r(\theta) r(\theta + \mathrm{d} \theta) (1 - \cos \mathrm{d} \theta) \\
      & = (r'(\theta) \mathrm{d} \theta + o(\mathrm{d} \theta))^2
          + r(\theta) (r(\theta) + r'(\theta) \mathrm{d} \theta + o(\mathrm{d} \theta)) ((\mathrm{d} \theta)^2 + o((\mathrm{d} \theta)^2)) \\
      & = (r'(\theta))^2 (\mathrm{d} \theta)^2 + {\color{red} 2 r'(\theta) \mathrm{d} \theta o(\mathrm{d} \theta)} + o((\mathrm{d} \theta)^2) \\
      &   \phantom{===} + r^2(\theta) (\mathrm{d} \theta)^2 + {\color{red} r^2(\theta) o((\mathrm{d} \theta)^2)}
          + {\color{red} r(\theta) r'(\theta) (\mathrm{d} \theta)^3} \\
      &   \phantom{===} + {\color{red} r(\theta) r'(\theta) \mathrm{d} \theta o((\mathrm{d} \theta)^2)}
          + {\color{red} r(\theta) (\mathrm{d} \theta)^2 o(\mathrm{d} \theta)} + {\color{red} r(\theta) o((\mathrm{d} \theta)^3)} \\
      & = (r'(\theta))^2 (\mathrm{d} \theta)^2 + r^2(\theta) (\mathrm{d} \theta)^2 + o((\mathrm{d} \theta)^2) \\
      & = (r'(\theta)^2 + r^2(\theta) + o(1)) (\mathrm{d} \theta)^2.

   以上倒数第二个等式成立是因为红色的项都是 :math:`(\mathrm{d} \theta)^2` 的高阶无穷小,
   第三个等式用到了 :math:`\cos \mathrm{d} \theta` 的麦克劳林展开式 (的变形)

   .. math::
      2(1 - \cos \mathrm{d} \theta) = (\mathrm{d} \theta)^2 + o((\mathrm{d} \theta)^2),

   所以有

   .. math::
      \mathrm{d} \ell = \sqrt{r'(\theta)^2 + r^2(\theta)} \mathrm{d} \theta.

   我们也可以发现, 对于以 :math:`r(\theta)` 为半径, :math:`\mathrm{d} \theta` 为角度的圆弧, 其弧长平方 :math:`r^2(\theta) (\mathrm{d} \theta)^2` 与折线平方的误差为

   .. math::
      r'(\theta)^2) (\mathrm{d} \theta)^2.

   究其原因, 就是因为圆弧, 折线, 以及 :math:`r(\theta + \mathrm{d} \theta)` 相对于 :math:`r(\theta)` 的增量 (或减量) :math:`r'(\theta) \mathrm{d} \theta`
   几乎构成了一个以折线为斜边的直角三角形, 从而导致了这个误差.
