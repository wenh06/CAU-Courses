第四章  微分中值定理与导数的应用
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. contents:: :local:


.. _exercises-chap4:

课后习题解答
====================================

.. _exercises-chap4_sec1:

§4.1 微分中值定理
------------------------------------

.. _exercises-chap4_sec1-ex3:

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

.. _exercises-chap4_sec1-ex4:

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

.. _exercises-chap4_sec2:

§4.2 洛必达法则
------------------------------------

.. _exercises-chap4_sec3:

§4.3 泰勒公式
------------------------------------

.. _exercises-chap4_sec3-ex8:

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

.. _exercises-chap4_sec3-ex9:

9. 用泰勒公式计算极限:

   .. math::
      \lim_{x \to 0} \dfrac{\ln(\cos x)}{x \sin x - \frac{1}{2}(e^x - 1)^2}.

.. proof:solution::

   可以利用 :ref:`上一题 <exercises-chap4_sec3-ex8>` 的结果, 先对分子进行等价无穷小替换

   .. math::
      \ln(\cos x) \sim -\frac{1}{2}x^2.

   .. note::
      假设我们不知道 :ref:`上一题 <exercises-chap4_sec3-ex8>` 的结果, 我们同样可以做等价无穷小替换

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

.. _exercises-chap4_sec4:

§4.4 函数的单调性
------------------------------------

.. _exercises-chap4_sec5:

§4.5 函数的极值与最值
------------------------------------

.. _exercises-chap4_sec5-ex5:

5. 绘制函数 :math:`\displaystyle f(x) = \dfrac{x^2+1}{x-1}` 的图像, 并讨论其渐近行为. 如果存在的话, 找出函数的垂直渐近线,
   水平渐近线和斜渐近线.

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
