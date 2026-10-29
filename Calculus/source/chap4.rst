第四章  微分中值定理与导数的应用
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. contents:: :local:


.. _ex-chap4:

课后习题解答
====================================

.. _ex-chap4_sec1:

§4.1 微分中值定理
------------------------------------

.. _ex-chap4_sec1-ex1:

1. 验证函数 :math:`f(x) = x \sqrt{3 - x}` 在区间 :math:`[0, 3]` 上是否满足罗尔中值定理, 若满足, 求出定理中的
   :math:`\xi`.

.. proof:solution::

   待写.

.. _ex-chap4_sec1-ex2:

2. 不用求出函数 :math:`f(x) = (x - 2)(x - 3)(x - 4)(x - 5)` 的导数, 说明方程 :math:`f'(x) = 0` 有几个实根,
   并指出它们所在的区间.

.. proof:solution::

   待写.

.. _ex-chap4_sec1-ex3:

3. 设 :math:`f(x)` 在 :math:`[0, 1]` 上连续, 在 :math:`(0, 1)` 内可导, 且 :math:`f(1) = 0`, 试证明: 至少存在一点
   :math:`\xi \in (0, 1)` 使得 :math:`\displaystyle f'(\xi) = -\dfrac{2 f(\xi)}{\xi}`.

.. proof:proof::

   构造辅助函数 :math:`g(x) = x^2 f(x)`. 那么 :math:`g(x)` 在 :math:`[0, 1]` 上连续, 在 :math:`(0, 1)` 内可导,
   且 :math:`g(0) = g(1) = 0`.

   .. math::
      g'(x) = 2x f(x) + x^2 f'(x).

   由罗尔定理知, 存在 :math:`\xi \in (0, 1)` 使得

   .. math::
      g'(\xi) = 0 \implies f'(\xi) = -\dfrac{2f(\xi)}{\xi}.

.. _ex-chap4_sec1-ex4:

4. 设 :math:`0 < a < b`, 证明不等式 :math:`\displaystyle \dfrac{b-a}{b} < \ln \dfrac{b}{a} < \dfrac{b-a}{a}`.

.. proof:proof::

   设 :math:`f(x) = \ln x`, 则 :math:`f'(x) = \dfrac{1}{x}`. 由拉格朗日中值定理知, 存在 :math:`\xi \in (a, b)` 使得

   .. math::
      \ln \dfrac{b}{a} = f(b) - f(a) = f'(\xi) \cdot \left( b - a \right) = \dfrac{1}{\xi} \cdot \left( b - a \right).

   由于 :math:`\displaystyle \dfrac{1}{b} < \dfrac{1}{\xi} < \dfrac{1}{a}`, 所以

   .. math::
      \dfrac{b-a}{b} < \ln \dfrac{b}{a} < \dfrac{b-a}{a}.

.. note::

   这些不等式的证明, 都是通过构造某个 (辅助) 函数, 再利用微分中值定理来完成的.
   关键在于, 通过要证明的不等式, 找到 (反推) 合适的辅助函数.

.. _ex-chap4_sec2:

§4.2 洛必达法则
------------------------------------

.. _ex-chap4_sec2-ex1:

1. 用洛必达法则求下列极限.

   (1) :math:`\lim\limits_{x \to 0} \dfrac{\ln(1 + x)}{x}`; \qquad
   (2) :math:`\lim\limits_{x \to 0} \dfrac{e^x - e^{-x}}{\sin x}`;

   (3) :math:`\lim\limits_{x \to 0} \dfrac{\tan x - x}{x - \sin x}`; \qquad
   (4) :math:`\lim\limits_{x \to 0} \dfrac{\sin 3x}{\tan 5x}`;

   (5) :math:`\lim\limits_{x \to a} \dfrac{x^m - a^m}{x^n - a^n}`; \qquad
   (6) :math:`\lim\limits_{x \to 1} \left( \dfrac{2}{x^2 - 1} - \dfrac{1}{x - 1} \right)`;

   (7) :math:`\lim\limits_{x \to \infty} \left( 1 + \dfrac{a}{x} \right)^x`; \qquad
   (8) :math:`\lim\limits_{x \to 0} x^{\sin x}`.

.. proof:solution::

   待写.

.. _ex-chap4_sec2-ex2:

2. 验证极限 :math:`\lim\limits_{x \to \infty} \dfrac{x + \sin x}{x}` 存在, 但不能用洛必达法则得出.

.. proof:solution::

   待写.

.. _ex-chap4_sec2-ex3:

3. 验证极限 :math:`\lim\limits_{x \to 0} \dfrac{x^2 \sin \dfrac{1}{x}}{\sin x}` 存在, 但不能用洛必达法则得出.

.. proof:solution::

   待写.

.. _ex-chap4_sec3:

§4.3 泰勒公式
------------------------------------

.. _ex-chap4_sec3-ex1:

1. 证明函数 :math:`f(x)` 和它的泰勒多项式 :math:`P_n(x)` 在 :math:`x_0` 处的 :math:`0` 阶, :math:`1` 阶,
   :math:`\cdots`, :math:`n` 阶导数值完全相同.

.. proof:solution::

   待写.

.. _ex-chap4_sec3-ex2:

2. 计算函数 :math:`f(x) = \sin x + x^2` 在 :math:`x_0 = \pi` 处的 :math:`0` 阶, :math:`1` 阶, :math:`2` 阶,
   :math:`3` 阶泰勒多项式.

.. proof:solution::

   待写.

.. _ex-chap4_sec3-ex3:

3. 计算第 2 题中 :math:`3` 阶泰勒多项式在 :math:`x_0 = \pi` 处的 :math:`0` 阶, :math:`1` 阶, :math:`2` 阶,
   :math:`3` 阶导数, 并将它们与 :math:`f(x)` 在 :math:`x_0 = \pi` 处的 :math:`0` 阶, :math:`1` 阶, :math:`2` 阶,
   :math:`3` 阶导数进行对比.

.. proof:solution::

   待写.

.. _ex-chap4_sec3-ex4:

4. 分别计算函数 :math:`f(x) = \sin x` 在 :math:`x_0 = 0` 和 :math:`x_0 = \dfrac{\pi}{2}` 处带有皮亚诺余项的
   泰勒公式, 其中 :math:`n` 是一个自然数.

.. proof:solution::

   待写.

.. _ex-chap4_sec3-ex5:

5. 计算函数 :math:`f(x) = x^3 + 6x - 1` 在 :math:`x_0 = 2` 处的带有拉格朗日余项的 :math:`n` 阶泰勒公式, 其中
   :math:`n \geqslant 3`.

.. proof:solution::

   待写.

.. _ex-chap4_sec3-ex6:

6. 考虑 :math:`a` 为实数和 :math:`n` 为自然数, 计算函数 :math:`f(x) = (1 + x)^a` 带有皮亚诺余项的
   :math:`n` 阶麦克劳林公式.

.. proof:solution::

   待写.

.. _ex-chap4_sec3-ex7:

7. 利用 :math:`e^x` 带有拉格朗日余项的麦克劳林公式计算 :math:`e` 的近似值, 要求误差不超过 :math:`10^{-3}`.

.. proof:solution::

   待写.

.. _ex-chap4_sec3-ex8:

8. 证明当 :math:`x \to 0` 时, 有:

   .. math::
      \ln(\cos x) = -\frac{1}{2}x^2 - \frac{1}{12}x^4 - \frac{1}{45}x^6 + o(x^6).

.. proof:proof::

   由泰勒公式知, 当 :math:`x \to 0` 时, 有

   .. math::
      & \cos x = 1 - \frac{1}{2}x^2 + \frac{1}{24}x^4 - \frac{1}{720}x^6 + o(x^6), \\
      & \ln (1 + u) = {\color{red}u} - {\color{cyan}\frac{1}{2}u^2} + {\color{green}\frac{1}{3}u^3} + o(u^3).

   .. note::
      注意思考为什么 :math:`\ln (1 + u)` 展开到 3 次项就够了.

   将 :math:`u = -\frac{1}{2}x^2 + \frac{1}{24}x^4 - \frac{1}{720}x^6 + o(x^6)` 代入第二式, 得

   .. math::
      \ln(\cos x) = \ln(1 + u) = & {\color{red} -\frac{1}{2}x^2 + \frac{1}{24}x^4 - \frac{1}{720}x^6 + o(x^6)} \\
      & - {\color{cyan} \frac{1}{2}\left(-\frac{1}{2}x^2 + \frac{1}{24}x^4 - \frac{1}{720}x^6 + o(x^6)\right)^2} \\
      & + {\color{green} \frac{1}{3}\left(-\frac{1}{2}x^2 + \frac{1}{24}x^4 - \frac{1}{720}x^6 + o(x^6)\right)^3} + o(u^3) \\
      = & {\color{red} - \frac{1}{2}x^2 + \frac{1}{24}x^4 - \frac{1}{720}x^6 + o(x^6)} \\
      & -{\color{cyan} \frac{1}{2}\left( \frac{1}{4}x^4 - \frac{1}{24}x^6 + o(x^6)\right)} \\
      & +{\color{green} \frac{1}{3}\left( -\frac{1}{8}x^6 + o(x^6)\right)} + o(x^6) \\
      = & {\color{red} -\frac{1}{2}x^2} - \left({\color{cyan}\frac{1}{8}} - {\color{red}\frac{1}{24}}\right) x^4
        - \left({\color{red}\frac{1}{720}} - {\color{cyan}\frac{1}{48}} + {\color{green}\frac{1}{24}}\right) x^6 + o(x^6) \\
      = & -\frac{1}{2}x^2 - \frac{1}{12}x^4 - \frac{1}{45}x^6 + o(x^6).

.. _ex-chap4_sec3-ex9:

9. 用泰勒公式计算极限:

   .. math::
      \lim_{x \to 0} \dfrac{\ln(\cos x)}{x \sin x - \frac{1}{2}(e^x - 1)^2}.

.. proof:solution::

   可以利用 :ref:`上一题 <ex-chap4_sec3-ex8>` 的结果, 先对分子进行等价无穷小替换

   .. math::
      \ln(\cos x) \sim -\frac{1}{2}x^2.

   .. note::
      假设我们不知道 :ref:`上一题 <ex-chap4_sec3-ex8>` 的结果, 我们同样可以做等价无穷小替换

      .. math::
         \ln(\cos x) = \ln(1 + (\cos x - 1)) \sim \cos x - 1 \sim -\frac{1}{2}x^2.

   对于分母中涉及的函数, 有

   .. math::
      & \sin x = x - \frac{1}{6}x^3 + o(x^3), \\
      & e^x = 1 + x + \frac{1}{2}x^2 + o(x^2),

   代入极限式中, 有

   .. math::
      \lim_{x \to 0} \dfrac{\ln(\cos x)}{x \sin x - \frac{1}{2}(e^x - 1)^2}
      = & \lim_{x \to 0} \dfrac{-\frac{1}{2}x^2}{(x^2 - \frac{1}{6}x^4 + o(x^4)) - \frac{1}{2}(x + \frac{1}{2}x^2 + o(x^2))^2} \\
      = & \lim_{x \to 0} \dfrac{-\frac{1}{2}x^2}{(x^2 + o(x^2)) - \frac{1}{2}(x^2 + o(x^2))} \\
      = & \lim_{x \to 0} \dfrac{-\frac{1}{2}x^2}{\frac{1}{2}x^2 + o(x^2)} \\
      = & -1.

.. _ex-chap4_sec4:

§4.4 函数的单调性
------------------------------------

.. _ex-chap4_sec4-ex1:

1. 证明: 开区间上的可微函数是常数当且仅当它的导数在这个区间上恒为 :math:`0`.

.. proof:solution::

   待写.

.. _ex-chap4_sec4-ex2:

2. 确定函数 :math:`f(x) = 2x^3 - 9x^2 + 12x - 3` 的单调区间.

.. proof:solution::

   待写.

.. _ex-chap4_sec4-ex3:

3. 确定函数 :math:`f(x) = \left( x^2 \right)^{\frac{1}{3}}` 的单调区间.

.. proof:solution::

   待写.

.. _ex-chap4_sec5:

§4.5 函数的极值与最值
------------------------------------

.. _ex-chap4_sec5-ex1:

1. 求下列函数的极值.

   (1) :math:`y = x^3 - 3x^2 - 9x + 5`; \qquad
   (2) :math:`y = (x - 1) \sqrt[3]{x^2}`;

   (3) :math:`y = x - 2 \sin x` (:math:`0 \leqslant x \leqslant 2\pi`); \qquad
   (4) :math:`y = x + \sqrt{1 - x}`;

   (5) :math:`y = x^2 \ln x`; \qquad
   (6) :math:`y = \dfrac{\ln^2 x}{x}`.

.. proof:solution::

   待写.

.. _ex-chap4_sec5-ex2:

2. 求下列函数在指定区间上的最大值和最小值.

   (1) :math:`y = x^4 - 8x^2 + 6`, :math:`x \in [-1, 3]`; \qquad
   (2) :math:`y = x + \sqrt{1 - x}`, :math:`x \in [-5, 1]`;

   (3) :math:`y = 2 \tan x - \tan^2 x`, :math:`x \in \left[ 0, \dfrac{\pi}{3} \right]`; \qquad
   (4) :math:`y = \lvert x^2 + 3x + 2 \rvert`, :math:`x \in [-3, 3]`;

   (5) :math:`y = \sqrt{x} \ln x`, :math:`x \in (0, +\infty)`; \qquad
   (6) :math:`y = \sin^3 x + \cos^3 x`, :math:`x \in \left[ -\dfrac{\pi}{4}, \dfrac{3\pi}{4} \right]`.

.. proof:solution::

   待写.

.. _ex-chap4_sec5-ex3:

3. 设 :math:`y = 2x^3 + ax + 3` 在 :math:`x = 1` 处取得极小值, 求 :math:`a` 的值.

.. proof:solution::

   待写.

.. _ex-chap4_sec5-ex4:

4. 问函数 :math:`f(x) = x^2 - \dfrac{54}{x}` (:math:`x < 0`) 在何处取得最小值?

.. proof:solution::

   待写.

.. _ex-chap4_sec5-ex5:

5. 问函数 :math:`f(x) = \dfrac{x}{1 + x^2}` (:math:`x \geqslant 0`) 在何处取得最大值?

.. proof:solution::

   待写.

.. _ex-chap4_sec5-ex6:

6. 讨论二次函数 :math:`f(x) = ax^2 + bx + c` 的最大值与最小值.

.. proof:solution::

   待写.

.. _ex-chap4_sec5-ex7:

7. 欲做一个底面为长方形的带盖的箱子, 其体积为 :math:`72 \text{ cm}^3`, 其底边宽与长的比为
   :math:`1 : 2`, 问各边的长为多少时, 才能使表面积最小?

.. proof:solution::

   待写.

.. _ex-chap4_sec5-ex8:

8. 设有一块边长为 :math:`a` 的正方形铁皮, 从四个角截去相同的小方块, 成为一个无盖的方盒子, 问小方块的边长为多少时
   才能使盒子容积最大?

.. proof:solution::

   待写.

.. _ex-chap4_sec5-ex9:

9. 制作一个上、下均有底的圆柱形容器, 要求容积为定值 :math:`V`. 问底半径 :math:`r` 为多大时, 容器的表面积最小?
   并求此最小面积.

.. proof:solution::

   待写.

.. _ex-chap4_sec5-ex10:

10. 某仓储设备的库存费与生产准备费之和 :math:`P(x)` 是每批产量 :math:`x` 的函数, 即

    .. math::
       P(x) = \dfrac{ab}{x} + \dfrac{c}{2} x \quad \left[ x \in (0, a) \right],

    其中 :math:`a` 为年产量, :math:`b` 为每批批次的生产准备费, :math:`c` 为每件产品的库存费. 问在生产能力足够大的
    条件下, 每批生产多少件产品时, :math:`P(x)` 最小?

.. proof:solution::

   待写.

.. _ex-chap4_sec6:

§4.6 函数的凹凸性
------------------------------------

.. _ex-chap4_sec6-ex1:

1. 证明函数 :math:`f(x) = ax^2 + bx + c` 是凸函数, 其中 :math:`a, b, c` 是实数, 且 :math:`a > 0`.

.. proof:solution::

   待写.

.. _ex-chap4_sec6-ex2:

2. 已知函数 :math:`g(x) = 4x^4 - 3x^3 + 2x^2`, 计算其二阶导数, 并证明 :math:`g(x)` 是凸函数.

.. proof:solution::

   待写.

.. _ex-chap4_sec6-ex3:

3. 如果 :math:`f(x)` 和 :math:`g(x)` 是两个凸函数, 证明对于任意的 :math:`\alpha, \beta \geqslant 0`, 函数
   :math:`h(x) = \alpha f(x) + \beta g(x)` 也是凸函数.

.. proof:solution::

   待写.

.. _ex-chap4_sec6-ex4:

4. 如果 :math:`f(x)` 和 :math:`g(x)` 是两个凸函数, 请问 :math:`f[g(x)]` 是否也是凸函数?

.. proof:solution::

   待写.

.. _ex-chap4_sec6-ex5:

5. 利用 :math:`\ln(x)` 的凹凸性证明下面的不等式.

   (1) 算术平均-几何平均不等式: :math:`x_1, x_2, \cdots, x_n > 0`, 有

       .. math::
          \dfrac{x_1 + x_2 + \cdots + x_n}{n} \geqslant \sqrt[n]{x_1 \cdot x_2 \cdots x_n},

       当且仅当所有 :math:`x_i` 相等时等号成立.

   (2) 对数函数的上界: 当 :math:`x > 0` 时有 :math:`\ln(x) \leqslant x - 1`.

.. proof:solution::

   待写.

.. _ex-chap4_sec6-ex6:

6. 求出下列函数的渐近线.

   (1) :math:`y = \dfrac{x + 1}{x}`; \qquad
   (2) :math:`y = \dfrac{x^3}{x^2 + 2x - 3}`; \qquad
   (3) :math:`y = \dfrac{1}{1 + e^x}`.

.. proof:solution::

   待写.

.. _ex-chap4_sec7:

§4.7 函数作图
------------------------------------

.. _ex-chap4_sec7-ex1:

1. 绘制函数 :math:`f(x) = x^3 - x^2 - x + 1` 的图像.

.. proof:solution::

   待写.

.. _ex-chap4_sec7-ex2:

2. 绘制函数 :math:`f(x) = \dfrac{\cos x}{\cos 2x}` 的图像.

.. proof:solution::

   待写.

.. _ex-chap4_sec7-ex3:

3. 绘制椭圆 :math:`x^2 - xy + y^2 = 3` 的图像.

.. proof:solution::

   待写.

.. _ex-chap4_sec7-ex4:

4. (探究光合作用与光照强度) 植物的光合作用速率 :math:`R(I)` (单位: 摩尔葡萄糖/:math:`\text{m}^2 \cdot \text{s}`)
   与光照强度 :math:`I` (单位: 摩尔光子/:math:`\text{m}^2 \cdot \text{s}`) 的关系可以用函数
   :math:`R(I) = \dfrac{aI}{b + I}` 来描述, 其中 :math:`a` 和 :math:`b` 是正常数. 绘制 :math:`R(I)` 的函数图像,
   并选择合适的 :math:`a` 值和 :math:`b` 值来模拟实际的光合作用情况. 解释图像的饱和点代表什么, 并计算光照强度达到
   饱和点一半时光合作用速率. 讨论如何通过图像来估计植物在不同光照强度下的光合作用效率.

.. proof:solution::

   待写.

.. _ex-chap4_sec7-ex5:

5. 绘制函数 :math:`g(x) = \dfrac{x^2 + 1}{x - 1}` 的图像, 并讨论其渐近行为. 如果存在的话, 找出函数的垂直渐近线,
   水平渐近线和斜渐近线.

.. note::
   本题原来误录在 :ref:`§4.5 <ex-chap4_sec5>` 之下, 现按教材归位到本节.

.. proof:solution::

   :math:`x = 1` 为奇点, 由于

   .. math::
      \lim_{x \to 1^-} f(x) = -\infty, \quad \lim_{x \to 1^+} f(x) = +\infty,

   故 :math:`x = 1` 为垂直渐近线.

   计算水平渐近线、斜渐近线 :math:`y = kx + b`:

   .. math::
      k & = \lim_{x \to \infty} \dfrac{f(x)}{x} = \lim_{x \to \infty} \dfrac{x^2+1}{x(x-1)} = 1, \\
      b & = \lim_{x \to \infty} \left( f(x) - kx \right) = \lim_{x \to \infty} \left( \dfrac{x^2+1}{x-1} - x \right) = \lim_{x \to \infty} \dfrac{x+1}{x-1} = 1,

   故有斜渐近线 :math:`y = x + 1`.

   .. tikz:: 函数 :math:`\displaystyle f(x) = \dfrac{x^2+1}{x-1}` 的图像
      :align: center
      :xscale: 70

      \begin{axis}[
         width=8cm, height=10cm, axis lines=middle,
         xlabel=$x$, ylabel=$y$,
         smooth, samples=200, minor tick num=4,
         xmin=-5, xmax=7, ymin=-30, ymax=30,
      ]
      \addplot[thick, cyan, domain=-5:0.99] {(\x^2+1)/(\x-1)};
      \addplot[thick, cyan, domain=1.01:7] {(\x^2+1)/(\x-1)};
      \addplot[dashed, red, domain=-5:7] {\x + 1};
      \addplot[dashed, red, domain=-30:30, variable=\y] ({1}, {\y});
      \end{axis}

.. _ex-chap4-zong:

总习题 4
------------------------------------

.. _ex-chap4-zong-ex1:

1. 用洛必达法则求极限.

   (1) :math:`\lim\limits_{x \to 0} \dfrac{e^x - e^{-x}}{\sin x}`; \qquad
   (2) :math:`\lim\limits_{x \to 0} \dfrac{\tan x - x}{x^3}`; \qquad
   (3) :math:`\lim\limits_{x \to 0} \dfrac{\ln \cos x}{x^2}`;

   (4) :math:`\lim\limits_{x \to 0} \dfrac{a^x - 1}{3x}` (:math:`a > 0` 且 :math:`a \neq 1`); \qquad
   (5) :math:`\lim\limits_{x \to \infty} \left[ x^2 \ln \left( 1 + \dfrac{1}{x} \right) - x \right]`.

.. proof:solution::

   待写.

.. _ex-chap4-zong-ex2:

2. 计算函数 :math:`y = e^x` 在 :math:`x = 0` 点的泰勒公式.

.. proof:solution::

   待写.

.. _ex-chap4-zong-ex3:

3. 证明当 :math:`x > 0` 时, :math:`\dfrac{x}{1 + x^2} < \arctan x < x`.

.. proof:solution::

   待写.

.. _ex-chap4-zong-ex4:

4. 设奇函数 :math:`f(x)` 在 :math:`[0, 1]` 上连续, 在 :math:`(0, 1)` 内可导, 且 :math:`f(1) = 1`, 证明: 存在
   :math:`\xi \in (0, 1)`, 使得 :math:`f'(\xi) = 1`.

.. proof:solution::

   待写.

.. _ex-chap4-zong-ex5:

5. 证明: 当 :math:`x > 0` 时, :math:`\ln(1 + x) > \dfrac{\arctan x}{1 + x}`.

.. proof:solution::

   待写.

.. _ex-chap4-zong-ex6:

6. 求函数 :math:`f(x) = 4x^2 (1 - x)^2` 在 :math:`[0, 1]` 上的最大值与最小值.

.. proof:solution::

   待写.

.. _ex-chap4-zong-ex7:

7. 求函数 :math:`y = \dfrac{(\ln x)^2}{x}` 的极值.

.. proof:solution::

   待写.

.. _ex-chap4-zong-ex8:

8. 设 :math:`a > 0` 为常数, :math:`f(x) = \ln x - \dfrac{x}{e} + a`, 问方程 :math:`f(x) = 0` 有几个实数根?

.. proof:solution::

   待写.

.. _ex-chap4-zong-ex9:

9. 讨论 :math:`y = x^3 - 3x^2 - 1` 的单调性、凸凹性、极值及拐点.

.. proof:solution::

   待写.

.. _ex-chap4-zong-ex10:

10. 求函数 :math:`y = \ln(1 + x^2)` 的图形的凹凸区间及拐点.

.. proof:solution::

   待写.

.. _ex-chap4-zong-ex11:

11. 确定函数 :math:`y = \dfrac{(x - 2)(3 - x)}{x^2}` 的单调区间, 并求其在区间 :math:`[1, 3]` 上的最值.

.. proof:solution::

   待写.

.. _ex-chap4-zong-ex12:

12. 设函数 :math:`f(x)` 和 :math:`g(x)` 在 :math:`[a, b]` 上可导, 且 :math:`f(a) = g(b)`, :math:`f(b) = g(a)`,
    :math:`g(x) g'(x) \neq 0`, 试证: 在开区间 :math:`(a, b)` 内至少存在一点 :math:`\xi`, 使
    :math:`\dfrac{f(\xi)}{g(\xi)} = -\dfrac{f'(\xi)}{g'(\xi)}`.

.. proof:solution::

   待写.

.. _extra-chap4:

补充内容
====================================

.. _extra-chap4-sec1:

§4.1 微分中值定理
--------------------------------

.. _extra-chap4-sec1-topic1:

1. 设函数 :math:`f(x)` 在区间 :math:`[a, b]` 上二阶可导, 且 :math:`f(0) = f(1)`, 证明存在 :math:`\xi \in (0, 1)`
   使得 :math:`f''(\xi) = \dfrac{2f'(\xi)}{1-\xi}`.

.. proof:proof::

   令

   .. math::
      F(x) = (x - 1)^2 f'(x),

   那么 :math:`F(1) = 0`. 由于 :math:`f(0) = f(1)`, 由罗尔定理知存在 :math:`c \in (0, 1)` 使得 :math:`f'(c) = 0`,
   从而有 :math:`F(c) = (c - 1)^2 f'(c) = 0`. 那么函数 :math:`F(x)` 就是 :math:`[c, 1]` 上连续, :math:`(c, 1)` 上可导的函数,
   并且满足 :math:`F(c) = F(1) = 0`. 再一次利用罗尔定理知, 存在 :math:`\xi \in (c, 1) \subset (0, 1)`, 使得

   .. math::
      0 = F'(\xi) = 2(\xi - 1) f'(\xi) + (\xi - 1)^2 f''(\xi),

   移项得 :math:`f''(\xi) = \dfrac{2f'(\xi)}{1-\xi}`.

.. _extra-chap4-sec2:

§4.2 洛必达法则
--------------------------------

.. _extra-chap4-sec2-topic1:

1. :math:`\dfrac{\infty}{\infty}` 型未定式的洛必达法则证明:

.. proof:proof::

   由于有 :math:`\lim\limits_{x \to x_0} = f(x) = \lim\limits_{x \to x_0} = g(x) = \infty`, 所以可以假定在 :math:`x_0` 的某个小的去心邻域
   :math:`\mathring{U}(x_0, \delta)` 内有 :math:`f(x) \neq 0, g(x) \neq 0`. 对于包含于 :math:`\mathring{U}(x_0, \delta)`
   且在 :math:`x_0` 某一边 (不妨设为右边) 的区间 :math:`[x, y]`, 在其上用柯西中值定理有

   .. math::
      & \dfrac{f(x) - f(y)}{g(x) - g(y)} = \dfrac{f'(\xi)}{g'(\xi)}, \quad \xi \in (x, y) \\
      \implies & f(x) g'(\xi) = f(y)g'(\xi) + (g(x) - g(y)) f'(\xi) \\
      \implies & \dfrac{f(x)}{g(x)} = \dfrac{f(y)}{g(x)} + \left( 1 - \dfrac{g(y)}{g(x)} \right) \dfrac{f'(\xi)}{g'(\xi)}.

   那么由于 :math:`\lim\limits_{x \to x_0} = f(x) = \lim\limits_{x \to x_0} = g(x) = \infty`,
   对任意的 :math:`K = \dfrac{1}{\varepsilon} \in \mathbb{R}^+`,
   以及对任意取定的 :math:`y`, 存在相应的 :math:`x \in (x_0, y) \cap \mathring{U}(x_0, \delta)` 使得

   .. math::
      \lvert g(x) \rvert > K \cdot f(y), \quad \lvert g(x) \rvert > K \cdot g(y),

   即有

   .. math::
      \left\lvert \dfrac{f(y)}{g(x)} \right\rvert < \varepsilon, \quad \left\lvert \dfrac{g(y)}{g(x)} \right\rvert < \varepsilon.

   记以上的极限过程为 :math:`\tau` (即让 :math:`y, x` 都趋于 :math:`x_0`, 但先选好 :math:`y`, 再选 :math:`x`, 使得以上关系成立), 那么有

   .. math::
      \lim_{\tau} \dfrac{f(x)}{g(x)}
      & = \lim_{\tau} \left( \dfrac{f(y)}{g(x)} + \left( 1 - \dfrac{g(y)}{g(x)} \right) \dfrac{f'(\xi)}{g'(\xi)} \right) \\
      & = 0 + (1 - 0) \lim_{\tau} \dfrac{f'(\xi)}{g'(\xi)} = \lim_{\tau} \dfrac{f'(\xi)}{g'(\xi)}.

   在极限过程 :math:`\tau` 中, 同样有 :math:`\xi \to x_0`, 所以

   .. math::
      \lim_{\tau} \dfrac{f'(\xi)}{g'(\xi)} & = \lim_{\xi \to x_0} \dfrac{f'(\xi)}{g'(\xi)} \\
      \lim_{\tau} \dfrac{f(x)}{g(x)} & = \lim_{\xi \to x_0} \dfrac{f'(\xi)}{g'(\xi)}.

   因此 :math:`\lim\limits_{x \to x_0} \dfrac{f(x)}{g(x)} = \lim\limits_{x \to x_0} \dfrac{f'(x)}{g'(x)}` 成立.

.. _extra-chap4-sec3:

§4.3 泰勒公式
--------------------------------

.. _extra-chap4-sec3-topic1:

1. 泰勒公式拉格朗日型余项 :math:`R_n(x) = \dfrac{f^{(n+1)}(\xi)}{(n+1)!} (x - x_0)^{n+1}` 的证明:

.. proof:proof::

   由 :math:`R_n(x) = f(x) - P_n(x) = f(x) - \left( f(x_0) + f'(x_0)(x - x_0) + \cdots + \dfrac{f^{(n)}(x_0)}{n!} (x - x_0)^n \right)`
   容易算得

   .. math::
      & R_n'(x_0) = R_n''(x_0) = \cdots = R_n^{(n)}(x_0) = 0, \\
      & R_n^{(n+1)}(x) = f^{(n+1)}(x).

   对函数 :math:`R_n(x)` 和 :math:`g(x) = (x - x_0)^{n + 1}` 应用 Cauchy 中值定理知, 存在 :math:`x_0` 与 :math:`x`
   之间的某个数 :math:`\xi_1` 使得

   .. math::
      \dfrac{R_n(x)}{(x - x_0)^{n + 1}} = \dfrac{R_n(x) - R_n(x_0)}{(x - x_0)^{n + 1} - (x_0 - x_0)^{n + 1}}
      = \dfrac{R_n'(\xi_1)}{(n + 1)(\xi_1 - x_0)^n}
      = \dfrac{1}{n + 1} \cdot \dfrac{R_n'(\xi_1)}{(\xi_1 - x_0)^n}

   再依次利用 Cauchy 中值定理, 有

   .. math::
      \dfrac{R_n(x)}{(x - x_0)^{n + 1}}
      & = \dfrac{1}{n + 1} \cdot \dfrac{R_n'(\xi_1)}{(\xi_1 - x_0)^n}
        = \dfrac{1}{n + 1} \cdot \dfrac{R_n'(\xi_1) - R_n'(x_0)}{(\xi_1 - x_0)^n - (x_0 - x_0)^n} \\
      & = \dfrac{1}{n + 1} \cdot \dfrac{1}{n} \cdot \dfrac{R_n''(\xi_2)}{(\xi_2 - x_0)^{n-1}}
        = \dfrac{1}{n + 1} \cdot \dfrac{1}{n} \cdot \dfrac{R_n''(\xi_2) - R_n''(x_0)}{(\xi_2 - x_0)^{n-1} - (x_0 - x_0)^{n-1}} \\
      & \vdots \\
      & = \dfrac{1}{n + 1} \cdot \dfrac{1}{n} \cdots \cdot \dfrac{1}{2} \cdot \dfrac{R_n^{(n)}(\xi_n)}{(\xi_n - x_0)}
        = \dfrac{1}{n + 1} \cdot \dfrac{1}{n} \cdots \cdot \dfrac{1}{2} \cdot \dfrac{R_n^{(n)}(\xi_n) - R_n^{(n)}(x_0)}{(\xi_n - x_0) - (x_0 - x_0)} \\
      & = \dfrac{1}{(n + 1)!} R_n^{(n+1)}(\xi_{n+1}),

   其中 :math:`\xi_{k+1}` 在 :math:`\xi_k` 与 :math:`x_0` 之间. 由于 :math:`R_n^{(n+1)}(\xi_{n+1}) = f^{(n+1)}(\xi_{n+1})`,
   所以令 :math:`\xi = \xi_{n+1}` 即有

   .. math::
      R_n(x) = \dfrac{f^{(n+1)}(\xi)}{(n+1)!} (x - x_0)^{n+1}.
