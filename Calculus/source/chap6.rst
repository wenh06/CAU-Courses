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

   待写.

.. _ex-chap6-sec1-ex2:

2. 设函数 :math:`f(x)` 在区间 :math:`[0, 1]` 上连续, 则 :math:`\displaystyle \int_0^1 f(x) ~ \mathrm{d}x`
   可以表示成下面哪个极限.

   (1) :math:`\displaystyle \lim_{n \to \infty} \sum_{i=1}^{n} f \left( \dfrac{2i - 1}{2n} \right) \dfrac{1}{2n}`; \qquad
   (2) :math:`\displaystyle \lim_{n \to \infty} \sum_{i=1}^{n} f \left( \dfrac{2i - 1}{2n} \right) \dfrac{1}{n}`;

   (3) :math:`\displaystyle \lim_{n \to \infty} \sum_{i=1}^{2n} f \left( \dfrac{i - 1}{2n} \right) \dfrac{1}{n}`; \qquad
   (4) :math:`\displaystyle \lim_{n \to \infty} \sum_{i=1}^{2n} f \left( \dfrac{i}{2n} \right) \dfrac{2}{n}`.

.. proof:solution::

   待写.

.. _ex-chap6-sec1-ex3:

3. 利用定积分的几何意义, 计算下列各定积分的值.

   (1) :math:`\displaystyle \int_{-1}^{6} 2 ~ \mathrm{d}x`; \qquad
   (2) :math:`\displaystyle \int_0^3 2x ~ \mathrm{d}x`;

   (3) :math:`\displaystyle \int_{-\sqrt{3}}^{\sqrt{3}} \sqrt{3 - x^2} ~ \mathrm{d}x`; \qquad
   (4) :math:`\displaystyle \int_1^2 \left( 1 - \sqrt{2x - x^2} \right) \mathrm{d}x`.

.. proof:solution::

   待写.

.. _ex-chap6-sec1-ex4:

4. 用定积分表示下列和式极限.

   (1) :math:`\displaystyle \lim_{n \to \infty} \dfrac{1}{n^4} \left( 1 + 2^3 + \cdots + n^3 \right)`;

   (2) :math:`\displaystyle \lim_{n \to \infty} n \left[ \dfrac{1}{(n + 1)^2} + \dfrac{1}{(n + 2)^2} + \cdots + \dfrac{1}{(n + n)^2} \right]`;

   (3) :math:`\displaystyle \lim_{n \to \infty} \left( \dfrac{1}{\sqrt{n^2 - 1^2}} + \dfrac{1}{\sqrt{n^2 - 2^2}} + \cdots
       + \dfrac{1}{\sqrt{n^2 - (n - 1)^2}} \right)`.

.. proof:solution::

   待写.

.. _ex-chap6-sec2:

§6.2 定积分的性质
------------------------------------

.. _ex-chap6-sec2-ex1:

1. 不计算积分, 试比较下列定积分的大小.

   (1) :math:`\displaystyle \int_0^1 x ~ \mathrm{d}x` 与 :math:`\displaystyle \int_0^1 x^2 ~ \mathrm{d}x`; \qquad
   (2) :math:`\displaystyle \int_0^{\frac{\pi}{4}} \dfrac{\tan x}{x} ~ \mathrm{d}x` 与
       :math:`\displaystyle \int_0^{\frac{\pi}{4}} \dfrac{x}{\tan x} ~ \mathrm{d}x`.

.. proof:solution::

   待写.

.. _ex-chap6-sec2-ex2:

2. 估计下列定积分的值.

   (1) :math:`\displaystyle \int_1^2 (2x^2 - 1) ~ \mathrm{d}x`; \qquad
   (2) :math:`\displaystyle \int_2^0 e^{-x^2} ~ \mathrm{d}x`;

   (3) :math:`\displaystyle \int_{\frac{1}{\sqrt{3}}}^{\sqrt{3}} x^2 \arctan x ~ \mathrm{d}x`; \qquad
   (4) :math:`\displaystyle \int_0^2 \dfrac{5 - x}{9 - x^2} ~ \mathrm{d}x`.

.. proof:solution::

   待写.

.. _ex-chap6-sec2-ex3:

3. 证明下列不等式.

   (1) :math:`\dfrac{2}{5} \leqslant \displaystyle \int_1^2 \dfrac{x}{1 + x^2} ~ \mathrm{d}x \leqslant \dfrac{1}{2}`; \qquad
   (2) :math:`1 \leqslant \displaystyle \int_0^1 e^{x^2} ~ \mathrm{d}x \leqslant e`;

   (3) :math:`1 \leqslant \displaystyle \int_0^{\frac{\pi}{3}} \dfrac{\sin x}{x} ~ \mathrm{d}x \leqslant \dfrac{\pi}{2}`.

.. proof:solution::

   待写.

.. _ex-chap6-sec2-ex4:

4. 计算定积分 :math:`\displaystyle \int_{-1}^1 \lvert x \rvert ~ \mathrm{sgn}(x + 1) ~ \mathrm{d}x`.

.. proof:solution::

   待写.

.. _ex-chap6-sec2-ex5:

5. 已知 :math:`I_1 = \displaystyle \int_0^1 \dfrac{x}{2(1 + \cos x)} ~ \mathrm{d}x`,
   :math:`I_2 = \displaystyle \int_0^1 \dfrac{\ln(1 + x)}{1 + \cos x} ~ \mathrm{d}x`,
   :math:`I_3 = \displaystyle \int_0^1 \dfrac{2x}{1 + \sin x} ~ \mathrm{d}x`, 试比较 :math:`I_1`, :math:`I_2`,
   :math:`I_3` 的大小.

.. proof:solution::

   待写.

.. _ex-chap6-sec2-ex6:

6. 计算下列函数在指定区间上的平均值.

   (1) :math:`f(x) = \sqrt{1 - x^2}`, :math:`[0, 1]`; \qquad
   (2) :math:`f(x) = x^2`, :math:`[1, 5]`.

.. proof:solution::

   待写.

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

   待写.

.. _ex-chap6-sec3-ex2:

2. 计算下列极限.

   (1) :math:`\displaystyle \lim_{x \to 0^+} \dfrac{\int_0^{x^2} \sqrt{t} ~ e^{t^2} ~ \mathrm{d}t}{2x^3}`; \qquad
   (2) :math:`\displaystyle \lim_{x \to 0} \dfrac{\int_0^{x^2} t^{\frac{3}{2}} ~ \mathrm{d}t}
       {\int_0^x t (t - \sin t) ~ \mathrm{d}t}`.

.. proof:solution::

   待写.

.. _ex-chap6-sec3-ex3:

3. 计算下列定积分.

   (1) :math:`\displaystyle \int_0^1 e^x ~ \mathrm{d}x`; \qquad
   (2) :math:`\displaystyle \int_1^2 (2x + 3) ~ \mathrm{d}x`;

   (3) :math:`\displaystyle \int_0^1 \dfrac{3x^4 + 3x^2 + 1}{x^2 + 1} ~ \mathrm{d}x`; \qquad
   (4) :math:`\displaystyle \int_0^{\frac{\pi}{4}} \tan^2 x ~ \mathrm{d}x`;

   (5) :math:`\displaystyle \int_1^4 \left( \sqrt{x} + \dfrac{1}{\sqrt{x}} \right) \mathrm{d}x`; \qquad
   (6) :math:`\displaystyle \int_{-\frac{1}{2}}^{\frac{1}{2}} \dfrac{1}{\sqrt{1 - x^2}} ~ \mathrm{d}x`.

.. proof:solution::

   待写.

.. _ex-chap6-sec3-ex4:

4. 设 :math:`f(x)` 连续, :math:`\varphi(x) = \displaystyle \int_0^{x^2} x f(t) ~ \mathrm{d}t`, 若
   :math:`\varphi(1) = 1`, :math:`\varphi'(1) = 5`, 求 :math:`f(1)`.

.. proof:solution::

   待写.

.. _ex-chap6-sec3-ex5:

5. 已知函数 :math:`f(x)` 在 :math:`(-\infty, +\infty)` 上连续, 且
   :math:`f(x) = (x + 1)^2 + 2 \displaystyle \int_0^x f(t) ~ \mathrm{d}t`, 则当 :math:`n \geqslant 2` 时求
   :math:`f^{(n)}(0)`.

.. proof:solution::

   待写.

.. _ex-chap6-sec3-ex6:

6. 设函数

   .. math::
      f(x) = \begin{cases}
         \dfrac{1}{x^3} \displaystyle \int_0^x \sin t^2 ~ \mathrm{d}t, & x \neq 0, \\
         a, & x = 0
      \end{cases}

   在 :math:`x = 0` 处连续, 求 :math:`a`.

.. proof:solution::

   待写.

.. _ex-chap6-sec3-ex7:

7. 已知函数 :math:`f(x) = \displaystyle \int_x^1 \sqrt{1 + t^2} ~ \mathrm{d}t
   + \int_1^{x^2} \sqrt{1 + t} ~ \mathrm{d}t`, 求 :math:`f(x)` 的零点个数.

.. proof:solution::

   待写.

.. _ex-chap6-sec3-ex8:

8. 设函数 :math:`f(x) = \displaystyle \int_0^x \lvert t^2 - x^2 \rvert ~ \mathrm{d}t` (:math:`x > 0`), 求
   :math:`f'(x)` 和 :math:`f(x)` 的最小值.

.. proof:solution::

   待写.

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

   待写.

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

   待写.

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

   待写.

.. _ex-chap6-sec4-ex4:

4. 计算定积分 :math:`\displaystyle \int_{-\frac{\pi}{4}}^{\frac{\pi}{2}} \sqrt{\cos x - \cos^3 x} ~ \mathrm{d}x`.

.. proof:solution::

   待写.

.. _ex-chap6-sec4-ex5:

5. 设 :math:`f(x)` 连续, 求 :math:`\dfrac{\mathrm{d}}{\mathrm{d}x} \displaystyle \int_0^x
   t f(x^2 - t^2) ~ \mathrm{d}t`.

.. proof:solution::

   待写.

.. _ex-chap6-sec4-ex6:

6. 证明: :math:`f(x)` 在区间 :math:`[a, b]` 上连续, 则

   .. math::
      \int_a^b f(x) ~ \mathrm{d}x = \int_a^b f(a + b - x) ~ \mathrm{d}x
      = (b - a) \int_0^1 f \left[ a + (b - a)x \right] \mathrm{d}x.

.. proof:solution::

   待写.

.. _ex-chap6-sec4-ex7:

7. 设 :math:`f(x) = \begin{cases} 1 + x^2, & x < 0, \\ \cos \dfrac{\pi}{2} x, & x \geqslant 0, \end{cases}`
   求 :math:`\displaystyle \int_{-1}^2 f(x - 1) ~ \mathrm{d}x`.

.. proof:solution::

   待写.

.. _ex-chap6-sec4-ex8:

8. 证明: :math:`\displaystyle \int_0^1 x^m (1 - x)^n ~ \mathrm{d}x
   = \int_0^1 x^n (1 - x)^m ~ \mathrm{d}x`.

.. proof:solution::

   待写.

.. _ex-chap6-sec4-ex9:

9. 设 :math:`f(x)` 在 :math:`[a, b]` 上有二阶连续导数, :math:`f(2) = \dfrac{1}{2}`, :math:`f'(2) = 0`, 且
   :math:`\displaystyle \int_0^2 f(x) ~ \mathrm{d}x = 1`, 试求定积分
   :math:`I = \displaystyle \int_0^1 x^2 f''(2x) ~ \mathrm{d}x`.

.. proof:solution::

   待写.

.. _ex-chap6-sec4-ex10:

10. 已知函数 :math:`f(x) = \displaystyle \int_0^x \dfrac{\sin t}{x - t} ~ \mathrm{d}t`, 求
    :math:`\displaystyle \int_0^{\pi} f(x) ~ \mathrm{d}x`.

.. proof:solution::

   待写.

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

   待写.

.. _ex-chap6-sec5-ex2:

2. 当 :math:`k` 为何值时, 广义积分 :math:`\displaystyle \int_2^{+\infty} \dfrac{\mathrm{d}x}{x (\ln x)^k}`
   收敛?

.. proof:solution::

   待写.

.. _ex-chap6-sec5-ex3:

3. 讨论广义积分 :math:`\displaystyle \int_a^b \dfrac{\mathrm{d}x}{(b - x)^p}` 和
   :math:`\displaystyle \int_a^b \dfrac{\mathrm{d}x}{(x - a)^p}` 的敛散性.

.. proof:solution::

   待写.

.. _ex-chap6-sec5-ex4:

4. 证明: :math:`\displaystyle \int_{-\infty}^{+\infty} e^{-x^2} ~ \mathrm{d}x
   = 2 \int_0^{+\infty} e^{-x^2} ~ \mathrm{d}x
   = \int_0^{+\infty} \dfrac{e^{-x}}{\sqrt{x}} ~ \mathrm{d}x`.

.. proof:solution::

   待写.

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

   待写.

.. _ex-chap6-sec6-ex2:

2. 计算由下列各曲线所围成的图形的面积.

   (1) :math:`r = e^{\frac{\theta}{2}}` (:math:`\dfrac{\pi}{2} \leqslant \theta \leqslant \pi`); \qquad
   (2) :math:`r^2 = 9 \sin 2\theta` (:math:`0 \leqslant \theta \leqslant \dfrac{\pi}{2}`);

   (3) :math:`r = 3 + 2 \cos \theta`; \qquad
   (4) :math:`r = 3 \cos \theta`.

.. proof:solution::

   待写.

.. _ex-chap6-sec6-ex3:

3. 求星形线 :math:`x^{\frac{2}{3}} + y^{\frac{2}{3}} = a^{\frac{2}{3}}` 所围成的图形面积 :math:`S`.

.. proof:solution::

   待写.

.. _ex-chap6-sec6-ex4:

4. 求由摆线 :math:`x = a(t - \sin t)`, :math:`y = a(1 - \cos t)` 的一拱与 :math:`x` 轴所围成的图形面积
   :math:`S`.

.. proof:solution::

   待写.

.. _ex-chap6-sec6-ex5:

5. 计算下列各弧长.

   (1) 曲线 :math:`y = \dfrac{1}{2} x^2` 相应于 :math:`0 \leqslant x \leqslant 1` 的一段弧;

   (2) 曲线 :math:`y = \dfrac{x^3}{3} + \dfrac{1}{4x}` 相应于 :math:`1 \leqslant x \leqslant 2` 的一段弧;

   (3) 曲线 :math:`y = \displaystyle \int_0^x \tan t ~ \mathrm{d}t` 相应于
       :math:`0 \leqslant x \leqslant \dfrac{\pi}{4}` 的一段弧;

   (4) 曲线 :math:`y = \ln \sec x` 相应于 :math:`0 \leqslant x \leqslant \dfrac{\pi}{4}` 的一段弧.

.. proof:solution::

   待写.

.. _ex-chap6-sec6-ex6:

6. 计算摆线 :math:`x = a(t - \sin t)`, :math:`y = a(1 - \cos t)` (:math:`a > 0`) 一拱
   (:math:`0 \leqslant t \leqslant 2\pi`) 的长度.

.. proof:solution::

   待写.

.. _ex-chap6-sec6-ex7:

7. 求抛物线 :math:`r = \dfrac{3}{1 + \cos \theta}` 在 :math:`-\dfrac{\pi}{2} \leqslant \theta \leqslant
   \dfrac{\pi}{2}` 之间的一段弧长.

.. proof:solution::

   待写.

.. _ex-chap6-sec6-ex8:

8. 求下列各立体的体积.

   (1) 由曲线 :math:`y = \sqrt{x - 1}`, :math:`x = 5` 和 :math:`x` 轴围成的图形绕 :math:`x` 轴旋转所得的旋转体;

   (2) 由曲线 :math:`y = x^2` 和 :math:`y = 2 - x^2` 围成的图形绕 :math:`x` 轴旋转所得的旋转体;

   (3) 由曲线 :math:`y = \sqrt{x} \sin x` (:math:`0 \leqslant x \leqslant 1`) 和 :math:`x` 轴围成的图形绕
       :math:`x` 轴旋转所得的旋转体;

   (4) 由曲线 :math:`y = \dfrac{1}{2} x^2`, :math:`y = \dfrac{1}{1 + x^2}` 和 :math:`y` 轴围成的图形绕
       :math:`y` 轴旋转所得的旋转体.

.. proof:solution::

   待写.

.. _ex-chap6-sec6-ex9:

9. 在曲线 :math:`y = x^2` (:math:`x \geqslant 0`) 上某点 :math:`A` 处作一切线, 使之与曲线及 :math:`x` 轴所围成的
   图形面积为 :math:`\dfrac{1}{12}`, 试求:

   (1) 过切点 :math:`A` 的切线方程;

   (2) 上述所围图形绕 :math:`x` 轴旋转所得旋转体的体积.

.. proof:solution::

   待写.

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
