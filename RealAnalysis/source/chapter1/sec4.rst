§4 开集的构造
------------------------------

.. _ex-1-22:

22. 设 :math:`F_1, F_2` 是 :math:`\mathbb{R}^n` 中的非空闭集，且 :math:`F_1 \cap F_2 = \emptyset`. 试证存在两个开集 :math:`G_1, G_2`,
    使 :math:`G_1 \cap G_2 = \emptyset`, 而 :math:`G_1 \supset F_1, G_2 \supset F_2`.

.. proof:proof::

   由于 :math:`F_1, F_2` 是 :math:`\mathbb{R}^n` 中的非空闭集，且 :math:`F_1 \cap F_2 = \emptyset`, 所以 :math:`\rho(F_1, F_2) > 0`.
   取 :math:`\delta = \dfrac{\rho(F_1, F_2)}{3}`, 并令

   .. math::

      G_i = \bigcup_{x \in F_i} U(x, \delta), \quad i = 1, 2.

   那么 :math:`G_1, G_2` 都是开集，且 :math:`G_1 \cap G_2 = \emptyset`. 又由于 :math:`\forall x \in F_1`, 有 :math:`U(x, \delta) \subset G_1`,
   所以 :math:`F_1 \subset G_1`. 同理可证 :math:`F_2 \subset G_2`.

.. _ex-1-23:

23. 设 :math:`F_1, F_2` 为 :math:`\mathbb{R}^n` 中的闭集，其中之一有界，试证存在两点 :math:`a_1 \in F_1, a_2 \in F_2` 使 :math:`\rho(a_1, a_2) = \rho(F_1, F_2)`.

.. proof:proof::

   首先证明，对任意的 :math:`\mathbb{R}^n` 的子集 :math:`F`, 函数 :math:`\mathbb{R}^n \to \mathbb{R}: \ x \mapsto \rho(x, F)`
   是一致连续的：

      任取 :math:`a, b \in \mathbb{R}^n`, 由于 :math:`\rho (a, F) := \inf\limits_{x \in F} \rho(a, x)`, 那么 :math:`\forall \varepsilon > 0`,
      存在 :math:`x_0 \in F`, 使得 :math:`\rho(a, x_0) < \rho(a, F) + \varepsilon`, 于是有

      .. math::

         \rho(b, F) \leqslant \rho(b, x_0) \leqslant \rho(b, a) + \rho(a, x_0) < \rho(b, a) + \rho(a, F) + \varepsilon.

      由于 :math:`\varepsilon` 是任意的，所以有 :math:`\rho(b, F) \leqslant \rho(b, a) + \rho(a, F)`. 同理可证 :math:`\rho(a, F) \leqslant \rho(a, b) + \rho(b, F)`.
      所以有 :math:`\lvert \rho(a, F) - \rho(b, F) \rvert \leqslant \rho(a, b)`. 那么对于任意取定的 :math:`\varepsilon > 0`, 取 :math:`\delta = \varepsilon`,
      只要 :math:`\rho(a, b) < \delta`, 就有 :math:`\lvert \rho(a, F) - \rho(b, F) \rvert < \varepsilon`.
      这就证明了函数 :math:`\mathbb{R}^n \to \mathbb{R}: \ x \mapsto \rho(x, F)` 是一致连续的。

   其次，我们证明，对任意点 :math:`a \in \mathbb{R}^n` 以及任意的非空闭集 :math:`F \subset \mathbb{R}^n`, 总存在 :math:`x_0 \in F`, 使得
   :math:`\rho(a, F) = \rho(a, x_0)`:

      考虑闭球 :math:`\overline{B} := \overline{B}(a, \delta)` 使得 :math:`\overline{B} \cap F \neq \emptyset`,
      那么 :math:`\overline{B} \cap F` 是 :math:`\mathbb{R}^n` 中有界闭集，且有 :math:`\rho(a, \overline{B} \cap F) = \rho(a, F)`.
      由于函数 :math:`\mathbb{R}^n \to \mathbb{R}: \ x \mapsto \rho(x, a)` 连续函数 (实际上进一步是初等函数)，所以它在有界闭集 :math:`\overline{B} \cap F` 上
      取到最小值，即存在 :math:`x_0 \in \overline{B} \cap F`, 使得 :math:`\rho(a, x_0) = \rho(a, \overline{B} \cap F) = \rho(a, F)`.

   有了以上两个结论，我们就可以证明题设结论。不妨设 :math:`F_1` 有界，考虑函数 :math:`\mathbb{R}^n \to \mathbb{R}: \ x \mapsto \rho(x, F_2)`.
   由之前第一点的结论，它是一致连续的，从而在有界闭集 :math:`F_1` 上取到最小值，即存在 :math:`a_1 \in F_1`, 使得 :math:`\rho(a_1, F_2) = \rho(F_1, F_2)`.
   又由于 :math:`F_2` 是非空闭集，根据第二点结论，存在 :math:`a_2 \in F_2`, 使得 :math:`\rho(a_1, F_2) = \rho(a_1, a_2)`. 于是有 :math:`\rho(a_1, a_2) = \rho(F_1, F_2)`.

.. _ex-1-24:

24. 设 :math:`G_1, G_2` 为 :math:`\mathbb{R}^1` 中的开集，且 :math:`G_1 \subset G_2`. 试证 :math:`G_1` 的每个构成区间含于 :math:`G_2` 的某个构成区间之中。

.. proof:proof::

   任取 :math:`G_1` 的一个构成区间 :math:`I_1 = (a_1, b_1)`, 那么有 :math:`I_1 \subset G_1 \subset G_2`. 任取 :math:`x_0 \in I_1`,
   令它包含于 :math:`G_2` 中的构成区间 :math:`I_2 = (a_2, b_2)`. 那么由构成区间的构造有

   .. math::

      a_2 = \inf \{ x : \ (x, x_0) \subset G_2 \}, \quad b_2 = \sup \{ x : \ (x_0, x) \subset G_2 \}.

   又知道 :math:`(a_1, x_0) \subset I_1 \subset G_1 \subset G_2`, 所以 :math:`a_1 \in \{ x : \ (x, x_0) \subset G_2 \}`, 故有 :math:`a_1 \geqslant a_2`.
   同理可证 :math:`b_1 \leqslant b_2`. 于是有 :math:`I_1 \subset I_2`.

.. _ex-1-25:

25. 试证 :math:`\mathbb{R}^n` 中每个闭集可表为可列个开集的交，每个开集可表为可列个闭集的并。

.. proof:proof::

   由 De Morgan 法则，我们只要证明前一个结论即可。

   任取 :math:`\mathbb{R}^n` 中的闭集 :math:`F`, 对任意的 :math:`n \in \mathbb{N}`, 令

   .. math::

      G_n = \bigcup_{x \in F} U \left( x, \dfrac{1}{n} \right),
      \quad U \left( x, \dfrac{1}{n} \right) := \left\{ y \in \mathbb{R}^n : \ \lvert x - y \rvert < \dfrac{1}{n} \right\}.

   那么 :math:`G_n` 是开集，且 :math:`F \subset G_n`. 可以证明 :math:`F = \bigcap\limits_{n=1}^{\infty} G_n`. 证明如下：

   只要证明 :math:`F \supset \bigcap\limits_{n=1}^{\infty} G_n` 即可。任取 :math:`x \in \bigcap\limits_{n=1}^{\infty} G_n`,
   那么 :math:`x \in G_n, \forall n \in \mathbb{N}`, 从而存在 :math:`x_n \in F`, 使得 :math:`x \in U \left( x_n, \dfrac{1}{n} \right)`,
   即有 :math:`\lvert x - x_n \rvert < \dfrac{1}{n}`. 于是 :math:`\{ x_n \}` 是 :math:`\mathbb{R}^n` 中的 Cauchy 列，且收敛到 :math:`x`.
   由于 :math:`F` 是闭集，所以 :math:`x \in F`. 于是有 :math:`\bigcap\limits_{n=1}^{\infty} G_n \subset F`.

.. _ex-1-26:

26. 设 :math:`E` 为康托三分集的补集中构成区间的中点所成的集，求 :math:`E'`.

.. proof:solution::

   根据康托三分集的构造过程，有如下的区间列：

   .. math::
      :label: cantor-set-chap1-sec4-ex26

      \begin{align*}
      F_1 & = F_{11} \cup F_{12} = \left[ 0, \dfrac{1}{3} \right] \cup \left[ \dfrac{2}{3}, 1 \right], \\
      I_1 & = I_{11} = \left( \dfrac{1}{3}, \dfrac{2}{3} \right), \\
      F_2 & = F_{21} \cup F_{22} \cup F_{23} \cup F_{24} = \left[ 0, \dfrac{1}{9} \right] \cup
               \left[ \dfrac{2}{9}, \dfrac{1}{3} \right] \cup \left[ \dfrac{2}{3}, \dfrac{7}{9} \right]
               \cup \left[ \dfrac{8}{9}, 1 \right], \\
      I_2 & = I_{21} \cup I_{22} = \left( \dfrac{1}{9}, \dfrac{2}{9} \right) \cup \left( \dfrac{7}{9}, \dfrac{8}{9} \right), \\
      & \vdots \\
      F_n & = F_{n1} \cup F_{n2} \cup \cdots \cup F_{n2^{n}}, \\
      I_n & = I_{n1} \cup I_{n2} \cup \cdots \cup I_{n2^{n-1}}, \\
      & \vdots \\
      G_0 & = \bigcup_{n=1}^{\infty} I_n, \\
      P_0 & = \mathscr{C} G_0 = \bigcap_{n=1}^{\infty} F_n \longleftarrow \text{(康托三分集)}. \\
      \end{align*}

   康托三分集的补集即为 :math:`G_0`, 其构成区间为 :math:`I_n`, 集合 :math:`E` 即由这些构成区间的中点所成的集。

   任取康托三分集中的点 :math:`x \in P_0 = \bigcap\limits_{n=1}^{\infty} F_n`, 那么 :math:`x \in F_n, \forall n \in \mathbb{N}` 成立。
   对任意 :math:`\varepsilon > 0`, 取 :math:`n \in \mathbb{N}`, 使得 :math:`\dfrac{1}{3^{n}} < \varepsilon`,
   那么 :math:`x \in F_n`, 从而存在 :math:`k \in \{ 1, 2, \dots, 2^n \}`, 使得 :math:`x \in F_{nk}`. 闭区间 :math:`F_{nk}` 的长度为
   :math:`\dfrac{1}{3^{n}}`, 所以 :math:`\forall y \in F_{nk}`, 都有 :math:`\lvert x - y \rvert \leqslant \varepsilon`. 同时，
   闭区间 :math:`F_{nk}` 包含了 :math:`I_{n+1}` 中的某个开区间 :math:`I_{n+1, k}, 1 \leqslant k \leqslant 2^{n}`
   (即第 :math:`n+1` 步从闭区间 :math:`F_{nk}` 中去除的中间 :math:`\dfrac{1}{3}` 开区间)，进而包含了 :math:`I_{n+1, k}` 的中点，
   记其为 :math:`y_0`, 那么有 :math:`0 < \lvert x - y_0 \rvert < \varepsilon`, 即 :math:`y_0 \in \mathring{U}(x, \varepsilon) \cap E`.
   这就证明了 :math:`x \in P_0` 是 :math:`E` 的聚点。所以有 :math:`E' \supset P_0`.

   反过来，任取 :math:`x \not\in P_0`, 即有 :math:`x \in G_0 = \bigcup\limits_{n=1}^{\infty} I_n`,
   那么存在 :math:`n \in \mathbb{N}`, 使得 :math:`x \in I_n`, 从而存在 :math:`k \in \{ 1, 2, \dots, 2^{n-1} \}`,
   使得 :math:`x \in I_{nk}`. 如果 :math:`x` 是 :math:`I_{nk}` 的中点，那么取 :math:`\varepsilon = \dfrac{1}{3^{n+1}}`,
   即有 :math:`\mathring{U}(x, \varepsilon) \subset I_{nk} \setminus \{ x \}`, 从而 :math:`\mathring{U}(x, \varepsilon) \cap E = \emptyset`,
   这说明了 :math:`x` 不是 :math:`E` 的聚点。如果 :math:`x` 不是 :math:`I_{nk}` 的中点，令 :math:`y_0` 为 :math:`I_{nk}` 的中点，
   那么取 :math:`\varepsilon = \min \left\{ \dfrac{1}{3^{n+1}}, \dfrac{1}{2} \lvert x - y_0 \rvert \right\}`, 这样，去心邻域 :math:`\mathring{U}(x, \varepsilon)`
   既不包含 :math:`y_0`, 也不会与 :math:`F_n` 中含有的与 :math:`I_{nk}` 相邻的任何一个闭区间的中间 :math:`\dfrac{1}{3}` 开区间相交，
   这样就有 :math:`\mathring{U}(x, \varepsilon) \cap E = \emptyset`, 也说明了 :math:`x` 不是 :math:`E` 的聚点。于是我们就证明了
   :math:`\mathscr{C} P_0 \cap E' = \emptyset`, 从而有 :math:`E' \subset P_0`.

   综上所述，有 :math:`E' = P_0`.
