第四章  微分中值定理与导数的应用
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. contents:: :local:


课后习题解答
====================================

§4.1 微分中值定理
------------------------------------

§4.2 洛必达法则
------------------------------------

§4.3 泰勒公式
------------------------------------

§4.4 函数的单调性
------------------------------------

§4.5 函数的极值与最值
------------------------------------

补充内容
====================================

§4.1 微分中值定理
--------------------------------

设函数 :math:`f(x)` 在区间 :math:`[a, b]` 上二阶可导, 且 :math:`f(0) = f(1)`, 证明存在 :math:`\xi \in (0, 1)` 使得 :math:`f''(\xi) = \dfrac{2f'(\xi)}{1-\xi}`.

.. proof:proof::

   令

   .. math::

      F(x) = (x - 1)^2 f'(x),

   那么 :math:`F(1) = 0`. 由于 :math:`f(0) = f(1)`, 由罗尔定理知存在 :math:`c \in (0, 1)` 使得 :math:`f'(c) = 0`,
   从而有 :math:`F(c) = (c - 1)^2 f'(c) = 0`. 那么函数 :math:`F(x)` 就是 :math:`[c, 1]` 上连续, :math:`(c, 1)` 上可导的函数, 并且满足 :math:`F(c) = F(1) = 0`.
   再一次利用罗尔定理知, 存在 :math:`\xi \in (c, 1) \subset (0, 1)`, 使得

   .. math::

      0 = F'(\xi) = 2(\xi - 1) f'(\xi) + (\xi - 1)^2 f''(\xi),

   移项得 :math:`f''(\xi) = \dfrac{2f'(\xi)}{1-\xi}`.

§4.2 洛必达法则
--------------------------------

:math:`\dfrac{\infty}{\infty}` 型未定式的洛必达法则证明:

由于有 :math:`\lim\limits_{x \to x_0} = f(x) = \lim\limits_{x \to x_0} = g(x) = \infty`, 所以可以假定在 :math:`x_0` 的某个小的去心邻域
:math:`\mathring{U}(x_0, \delta)` 内有 :math:`f(x) \neq 0, g(x) \neq 0`. 对于包含于 :math:`\mathring{U}(x_0, \delta)`
且在 :math:`x_0` 某一边 (不妨设为右边) 的区间 :math:`[x, y]`, 在其上用柯西中值定理有

.. math::

   & \dfrac{f(x) - f(y)}{g(x) - g(y)} = \dfrac{f'(\xi)}{g'(\xi)}, \quad \xi \in (x, y) \\
   \Longrightarrow & f(x) g'(\xi) = f(y)g'(\xi) + (g(x) - g(y)) f'(\xi) \\
   \Longrightarrow & \dfrac{f(x)}{g(x)} = \dfrac{f(y)}{g(x)} + \left( 1 - \dfrac{g(y)}{g(x)} \right) \dfrac{f'(\xi)}{g'(\xi)}.

那么由于 :math:`\lim\limits_{x \to x_0} = f(x) = \lim\limits_{x \to x_0} = g(x) = \infty`, 对任意的 :math:`K = \dfrac{1}{\varepsilon} \in \mathbb{R}^+`,
以及对任意取定的 :math:`y`, 存在相应的 :math:`x \in (x_0, y) \cap \mathring{U}(x_0, \delta)` 使得

.. math::

   \lvert g(x) \rvert > K \cdot f(y), \quad \lvert g(x) \rvert > K \cdot g(y),

即有

.. math::

   \left\lvert \dfrac{f(y)}{g(x)} \right\rvert < \varepsilon, \quad \left\lvert \dfrac{g(y)}{g(x)} \right\rvert < \varepsilon.

记以上的极限过程为 :math:`\tau` (即让 :math:`y, x` 都趋于 :math:`x_0`, 但先选好 :math:`y`, 再选 :math:`x`, 使得以上关系成立), 那么有

.. math::

   \lim_{\tau} \dfrac{f(x)}{g(x)} & = \lim_{\tau} \left( \dfrac{f(y)}{g(x)} + \left( 1 - \dfrac{g(y)}{g(x)} \right) \dfrac{f'(\xi)}{g'(\xi)} \right) \\
   & = 0 + (1 - 0) \lim_{\tau} \dfrac{f'(\xi)}{g'(\xi)} = \lim_{\tau} \dfrac{f'(\xi)}{g'(\xi)}.

在极限过程 :math:`\tau` 中, 同样有 :math:`\xi \to x_0`, 所以

.. math::

   \lim_{\tau} \dfrac{f'(\xi)}{g'(\xi)} & = \lim_{\xi \to x_0} \dfrac{f'(\xi)}{g'(\xi)} \\
   \lim_{\tau} \dfrac{f(x)}{g(x)} & = \lim_{\xi \to x_0} \dfrac{f'(\xi)}{g'(\xi)}.

因此 :math:`\lim\limits_{x \to x_0} \dfrac{f(x)}{g(x)} = \lim\limits_{x \to x_0} \dfrac{f'(x)}{g'(x)}` 成立.

§4.3 泰勒公式
--------------------------------

泰勒公式拉格朗日型余项 :math:`R_n(x) = \dfrac{f^{(n+1)}(\xi)}{(n+1)!} (x - x_0)^{n+1}` 的证明:

.. proof:proof::

   由 :math:`R_n(x) = f(x) - P_n(x) = f(x) - \left( f(x_0) + f'(x_0)(x - x_0) + \cdots + \dfrac{f^{(n)}(x_0)}{n!} (x - x_0)^n \right)` 容易算得

   .. math::

      & R_n'(x_0) = R_n''(x_0) = \cdots = R_n^{(n)}(x_0) = 0, \\
      & R_n^{(n+1)}(x) = f^{(n+1)}(x).

   由 Cauchy 中值定理知, 存在 :math:`x_0` 与 :math:`x` 之间的某个数 :math:`\xi_1` 使得

   .. math::

      \dfrac{R_n(x)}{(x - x_0)^{n + 1}} = \dfrac{R_n(x) - R_n(x_0)}{(x - x_0)^{n + 1} - (x_0 - x_0)^{n + 1}} = \dfrac{R_n'(\xi_1)}{(n + 1)(\xi_1 - x_0)^n}
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
