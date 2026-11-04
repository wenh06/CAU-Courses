§4 开集的构造
------------------------------

.. _ex-1-22:

22. 设 :math:`F_1, F_2` 是 :math:`\mathbb{R}^n` 中的闭集, 且 :math:`F_1 \cap F_2 = \emptyset`. 试证存在两个开集 :math:`G_1, G_2`,
    使 :math:`G_1 \cap G_2 = \emptyset`, 而 :math:`G_1 \supset F_1, G_2 \supset F_2`.

.. proof:proof::

   不妨设 :math:`F_1, F_2` 非空: 若某个 :math:`F_i = \emptyset`, 则取
   :math:`G_i = \emptyset`, :math:`G_j = \mathbb{R}^n` (:math:`j \neq i`) 即可.

   构造如下集合，下面说明即为题目所求.

   .. math::
      G_1 := \{x \in \mathbb {R}^n \mid \rho (x, F_1) < \rho (x, F_2) \},
      \quad G_2 := \{ x \in \mathbb {R}^n \mid \rho (x, F_2) < \rho (x, F_1) \}

   显然 :math:`G_1 \cap G_2 = \emptyset`.

   首先证明 :math:`F_i \subset G_i`: 设 :math:`x \in F_1`, 则 :math:`\rho(x, F_1) = 0`.
   若 :math:`\rho(x, F_2) = 0`, 利用 :math:`F_2` 为闭集，知道存在 :math:`y \in F_2`, 使得

   .. math::
      \rho (x, F_2) = \rho (x, y) = 0 \implies x = y

   这与 :math:`F_1 \cap F_2 = \emptyset` 矛盾. 故 :math:`\rho(x, F_2) > 0`, 从而 :math:`F_1 \subset G_1`.
   同理 :math:`F_2 \subset G_2`. 下只需证 :math:`G_1, G_2` 为开集.

   由 :math:`\rho(x, F_1) - \rho(x, F_2) =: f(x)` 关于 :math:`x` 一致连续, 知

   .. math::
      G_1 = f^{-1}((-\infty, 0)), \quad G_2 = f^{-1}((0, +\infty))

   为开集，因此命题得证.

   .. note::
      此题解答由数学232班闫宇涵提供.

   .. note::
      原解答必须加上 :math:`F_1, F_2` 至少有一个有界的条件，否则不成立. 下面是原解答:

         由于 :math:`F_1, F_2` 是 :math:`\mathbb{R}^n` 中的非空闭集, 且 :math:`F_1 \cap F_2 = \emptyset`,
         所以 :math:`\rho(F_1, F_2) > 0`. 取 :math:`\delta = \dfrac{\rho(F_1, F_2)}{3}`, 并令

         .. math::
            G_i = \bigcup_{x \in F_i} U(x, \delta), \quad i = 1, 2.

         那么 :math:`G_1, G_2` 都是开集, 且 :math:`G_1 \cap G_2 = \emptyset`. 又由于 :math:`\forall ~ x \in F_1`,
         有 :math:`U(x, \delta) \subset G_1`, 所以 :math:`F_1 \subset G_1`. 同理可证 :math:`F_2 \subset G_2`.

.. _ex-1-23:

23. 设 :math:`F_1, F_2` 为 :math:`\mathbb{R}^n` 中的非空闭集, 其中之一有界, 试证存在两点 :math:`a_1 \in F_1, a_2 \in F_2`
    使 :math:`\rho(a_1, a_2) = \rho(F_1, F_2)`.

.. proof:proof::

   首先证明, 对任意的非空 :math:`\mathbb{R}^n` 子集 :math:`F`, 函数 :math:`\mathbb{R}^n \to \mathbb{R}: \ x \mapsto \rho(x, F)`
   是一致连续的:

      任取 :math:`a, b \in \mathbb{R}^n`, 由于 :math:`\rho (a, F) := \inf\limits_{x \in F} \rho(a, x)`, 那么
      :math:`\forall ~ \varepsilon > 0`, 存在 :math:`x_0 \in F`, 使得 :math:`\rho(a, x_0) < \rho(a, F) + \varepsilon`, 于是有

      .. math::
         \rho(b, F) \leqslant \rho(b, x_0) \leqslant \rho(b, a) + \rho(a, x_0) < \rho(b, a) + \rho(a, F) + \varepsilon.

      由于 :math:`\varepsilon` 是任意的, 所以有 :math:`\rho(b, F) \leqslant \rho(b, a) + \rho(a, F)`. 同理可证
      :math:`\rho(a, F) \leqslant \rho(a, b) + \rho(b, F)`.
      所以有 :math:`\lvert \rho(a, F) - \rho(b, F) \rvert \leqslant \rho(a, b)`. 那么对于任意取定的 :math:`\varepsilon > 0`,
      取 :math:`\delta = \varepsilon`, 只要 :math:`\rho(a, b) < \delta`, 就有
      :math:`\lvert \rho(a, F) - \rho(b, F) \rvert < \varepsilon`.
      这就证明了函数 :math:`\mathbb{R}^n \to \mathbb{R}: \ x \mapsto \rho(x, F)` 是一致连续的.

   其次, 我们证明, 对任意点 :math:`a \in \mathbb{R}^n` 以及任意的非空闭集 :math:`F \subset \mathbb{R}^n`, 总存在
   :math:`x_0 \in F`, 使得 :math:`\rho(a, F) = \rho(a, x_0)`:

      取定 :math:`y \in F`, 令 :math:`\delta = \rho(a, y) + 1`, 考虑闭球
      :math:`\overline{B} := \overline{B}(a, \delta)`, 则 :math:`\overline{B} \cap F \neq \emptyset`,
      且 :math:`\overline{B} \cap F` 是 :math:`\mathbb{R}^n` 中非空有界闭集. 先证
      :math:`\rho(a, \overline{B} \cap F) = \rho(a, F)`: 一方面 :math:`\overline{B} \cap F \subset F`
      给出 :math:`\rho(a, \overline{B} \cap F) \geqslant \rho(a, F)`; 另一方面, 由下确界定义, 对任意
      :math:`\varepsilon \in (0, \delta - \rho(a, F)]` 存在 :math:`x_{\varepsilon} \in F` 使得
      :math:`\rho(a, x_{\varepsilon}) < \rho(a, F) + \varepsilon \leqslant \delta`, 即
      :math:`x_{\varepsilon} \in \overline{B} \cap F`, 故
      :math:`\rho(a, \overline{B} \cap F) \leqslant \rho(a, x_{\varepsilon}) < \rho(a, F) + \varepsilon`,
      由 :math:`\varepsilon` 的任意性即得等式. 由于函数 :math:`x \mapsto \rho(x, a)` 连续
      (实际上进一步是初等函数), 所以它在非空有界闭集 :math:`\overline{B} \cap F` 上取到最小值,
      即存在 :math:`x_0 \in \overline{B} \cap F`, 使得
      :math:`\rho(a, x_0) = \rho(a, \overline{B} \cap F) = \rho(a, F)`.

   有了以上两个结论, 我们就可以证明题设结论. 不妨设 :math:`F_1` 有界, 考虑函数

   .. math::
      \mathbb{R}^n \to \mathbb{R}: \ x \mapsto \rho(x, F_2).

   由之前第一点的结论, 它是一致连续的, 从而在有界闭集 :math:`F_1` 上取到最小值, 即存在 :math:`a_1 \in F_1`,
   使得 :math:`\rho(a_1, F_2) = \rho(F_1, F_2)`. 又由于 :math:`F_2` 是非空闭集, 根据第二点结论, 存在 :math:`a_2 \in F_2`,
   使得 :math:`\rho(a_1, F_2) = \rho(a_1, a_2)`. 于是有 :math:`\rho(a_1, a_2) = \rho(F_1, F_2)`.

.. _ex-1-24:

24. 设 :math:`G_1, G_2` 为 :math:`\mathbb{R}^1` 中的开集, 且 :math:`G_1 \subset G_2`. 试证 :math:`G_1`
    的每个构成区间含于 :math:`G_2` 的某个构成区间之中.

.. proof:proof::

   任取 :math:`G_1` 的一个构成区间 :math:`I_1 = (a_1, b_1)`, 那么有 :math:`I_1 \subset G_1 \subset G_2`. 任取
   :math:`x_0 \in I_1`, 令它包含于 :math:`G_2` 中的构成区间 :math:`I_2 = (a_2, b_2)`. 那么由构成区间的构造有

   .. math::
      a_2 = \inf \{ x : \ (x, x_0) \subset G_2 \}, \quad b_2 = \sup \{ x : \ (x_0, x) \subset G_2 \}.

   这里以及下文中的构成区间端点都可能取值 :math:`\pm \infty` (例如 :math:`G_2 = \mathbb{R}` 时
   :math:`a_2 = -\infty`, :math:`G_1 = (0, +\infty)` 时 :math:`b_1 = +\infty`); 此时上述推导按扩充实数系
   :math:`\overline{\mathbb{R}}` 理解 (例如 :math:`a_1 = -\infty` 时有 :math:`(-\infty, x_0) \subset G_2`
   且 :math:`a_2 = -\infty`), 结论不变. 又知道 :math:`(a_1, x_0) \subset I_1 \subset G_1 \subset G_2`,
   所以 :math:`a_1 \in \{ x : \ (x, x_0) \subset G_2 \}`, 故有 :math:`a_1 \geqslant a_2`.
   同理可证 :math:`b_1 \leqslant b_2`. 于是有 :math:`I_1 \subset I_2`.

.. _ex-1-25:

25. 试证 :math:`\mathbb{R}^n` 中每个闭集可表为可列个开集的交, 每个开集可表为可列个闭集的并.

.. proof:proof::

   由 De Morgan 法则, 我们只要证明前一个结论即可.

   任取 :math:`\mathbb{R}^n` 中的闭集 :math:`F`, 对任意的 :math:`n \in \mathbb{N}`, 令

   .. math::
      G_n = \bigcup_{x \in F} U \left( x, \dfrac{1}{n} \right),
      \quad U \left( x, \dfrac{1}{n} \right) := \left\{ y \in \mathbb{R}^n : \ \lvert x - y \rvert < \dfrac{1}{n} \right\}.

   那么 :math:`G_n` 是开集, 且 :math:`F \subset G_n`. 可以证明 :math:`F = \bigcap\limits_{n=1}^{\infty} G_n`. 证明如下:

   只要证明 :math:`F \supset \bigcap\limits_{n=1}^{\infty} G_n` 即可. 任取 :math:`x \in \bigcap\limits_{n=1}^{\infty} G_n`,
   那么 :math:`x \in G_n, \forall ~ n \in \mathbb{N}`, 从而存在 :math:`x_n \in F`, 使得
   :math:`x \in U \left( x_n, \dfrac{1}{n} \right)`, 即有 :math:`\lvert x - x_n \rvert < \dfrac{1}{n}`.
   于是 :math:`\{ x_n \}` 是 :math:`\mathbb{R}^n` 中的 Cauchy 列, 且收敛到 :math:`x`. 由于 :math:`F` 是闭集,
   所以 :math:`x \in F`. 于是有 :math:`\bigcap\limits_{n=1}^{\infty} G_n \subset F`.

.. _ex-1-26:

26. 设 :math:`E` 为康托三分集的补集中构成区间的中点所成的集, 求 :math:`E'`.

.. proof:solution::

   根据康托三分集的构造过程, 有如下的区间列:

   .. math::
      :label: cantor-set-chap1-sec4-ex26

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
      P_0 & = [0, 1] \setminus G_0 = \bigcap_{n=1}^{\infty} F_n \longleftarrow \text{(康托三分集)}.

   康托三分集即为 :math:`[0, 1] \setminus G_0`, :math:`G_0` 的构成区间为诸 :math:`I_{nk}`
   (:math:`I_n` 是它们的并), 集合 :math:`E` 即由这些构成区间的中点所成的集.

   任取康托三分集中的点 :math:`x \in P_0 = \bigcap\limits_{n=1}^{\infty} F_n`, 那么
   :math:`x \in F_n, \forall ~ n \in \mathbb{N}` 成立. 对任意 :math:`\varepsilon > 0`, 取 :math:`n \in \mathbb{N}`,
   使得 :math:`\dfrac{1}{3^{n}} < \varepsilon`, 那么 :math:`x \in F_n`, 从而存在 :math:`k \in \{ 1, 2, \dots, 2^n \}`,
   使得 :math:`x \in F_{nk}`. 闭区间 :math:`F_{nk}` 的长度为 :math:`\dfrac{1}{3^{n}}`, 所以 :math:`\forall ~ y \in F_{nk}`,
   都有 :math:`\lvert x - y \rvert \leqslant \varepsilon`. 同时, 闭区间 :math:`F_{nk}` 包含了 :math:`I_{n+1}` 中的某个开区间
   :math:`I_{n+1, k}, 1 \leqslant k \leqslant 2^{n}` (即第 :math:`n+1` 步从闭区间 :math:`F_{nk}` 中去除的中间
   :math:`\dfrac{1}{3}` 开区间), 进而包含了 :math:`I_{n+1, k}` 的中点, 记其为 :math:`y_0`, 那么有
   :math:`0 < \lvert x - y_0 \rvert < \varepsilon`, 即 :math:`y_0 \in \mathring{U}(x, \varepsilon) \cap E`.
   这就证明了 :math:`x \in P_0` 是 :math:`E` 的聚点. 所以有 :math:`E' \supset P_0`.

   反过来, 若 :math:`x \not\in [0, 1]`, 则 :math:`x` 与 :math:`E \subset [0, 1]` 有正距离, 显然不是
   :math:`E` 的聚点. 故设 :math:`x \in [0, 1] \setminus P_0`, 即
   :math:`x \in G_0 = \bigcup\limits_{n=1}^{\infty} I_n`, 那么存在 :math:`n \in \mathbb{N}`, 使得
   :math:`x \in I_n`, 从而存在 :math:`k \in \{ 1, 2, \dots, 2^{n-1} \}`,
   使得 :math:`x \in I_{nk}`. 如果 :math:`x` 是 :math:`I_{nk}` 的中点, 那么取 :math:`\varepsilon = \dfrac{1}{3^{n+1}}`,
   即有 :math:`\mathring{U}(x, \varepsilon) \subset I_{nk} \setminus \{ x \}`, 从而
   :math:`\mathring{U}(x, \varepsilon) \cap E = \emptyset`, 这说明了 :math:`x` 不是 :math:`E` 的聚点.
   如果 :math:`x` 不是 :math:`I_{nk} = (a, b)` 的中点, 令 :math:`y_0` 为 :math:`I_{nk}` 的中点,
   那么取 :math:`\varepsilon = \min \left\{ \dfrac{1}{2} \lvert x - y_0 \rvert,\ x - a,\ b - x \right\} > 0`,
   这样, 去心邻域 :math:`\mathring{U}(x, \varepsilon) \subset I_{nk}` 且不包含 :math:`y_0`.
   而由诸构成区间两两不交, :math:`E \cap I_{nk} = \{ y_0 \}` (每个构成区间的中点都在自己内部),
   这样就有 :math:`\mathring{U}(x, \varepsilon) \cap E = \emptyset`, 也说明了 :math:`x` 不是 :math:`E` 的聚点. 于是我们就证明了
   :math:`\mathscr{C} P_0 \cap E' = \emptyset`, 从而有 :math:`E' \subset P_0`.

   综上所述, 有 :math:`E' = P_0`.

.. _ex-1-27:

27. 设 :math:`P_0` 为 :math:`[0, 1]` 中的 Cantor 三分集, 试证 :math:`P_0 + P_0 = \{ x + y ~ : ~ x, y \in P_0 \} = [0, 2]`,
    :math:`P_0 - P_0 = \{ x - y ~ : ~ x, y \in P_0 \} = [-1, 1]`.
    (提示: 利用实数的三进表示并注意到 :math:`P_0 \pm P_0` 均为闭集.)

.. proof:solution::

   沿用 :ref:`第 26 题 <ex-1-26>` 的记号: :math:`P_0 = \bigcap\limits_{n=1}^{\infty} F_n`, 其中
   :math:`F_n = F_{n1} \cup F_{n2} \cup \cdots \cup F_{n2^{n}}` 由 :math:`2^{n}` 个长度为
   :math:`3^{-n}` 的闭区间构成. 由构造过程, :math:`F_n` 有如下的自相似分解:

   .. math::
      :label: ex-1-27-eq-1

      F_{n+1} = \varphi_1 ( F_n ) \cup \varphi_2 ( F_n ), \qquad
      \varphi_1 ( x ) = \frac{x}{3}, \quad \varphi_2 ( x ) = \frac{x + 2}{3},

   即 :math:`\varphi_1, \varphi_2` 分别是把每个闭区间压缩进其左、右两段的压缩映射.

   首先注意, :math:`P_0` 作为 :math:`\mathbb{R}^1` 中的有界闭集是紧集, 而加法运算连续, 所以
   :math:`P_0 + P_0` 与 :math:`P_0 - P_0` 都是紧集, 从而都是闭集.

   其次利用实数的三进表示. 对 :math:`n \in \mathbb{N}`, 令

   .. math::
      D_n = \left\{ \sum_{k=1}^{n} \frac{a_k}{3^{k}} \; : \; a_k \in \{ 0, 2 \} \right\}

   为前 :math:`n` 位三进数字只取 :math:`0` 和 :math:`2` 的有限三进小数之集. 这些点都是被挖去的开区间
   :math:`I_{nk}` 的端点 (或 :math:`0` 与 :math:`1`), 在构造的每一步都未被挖去, 故 :math:`D_n \subset P_0`.
   逐位相加可见 :math:`D_n + D_n = \left\{ \sum_{k=1}^{n} \frac{d_k}{3^{k}} \; : \; d_k \in \{ 0, 2, 4 \} \right\}`:
   记 :math:`d_k = 2 e_k`, :math:`e_k \in \{ 0, 1, 2 \}`, 则 :math:`\sum\limits_{k=1}^{n} e_k 3^{-k}` 恰为形如
   :math:`j \cdot 3^{-n}` (:math:`j = 0, 1, \dots, 3^{n} - 1`) 的数. 于是 :math:`D_n + D_n` 是
   :math:`[0, 2 - 2 \cdot 3^{-n}]` 中步长为 :math:`2 \cdot 3^{-n}` 的等距网格. 从而对任意 :math:`z \in [0, 2]`,
   存在 :math:`x_n, y_n \in D_n \subset P_0`, 使得

   .. math::
      \left| z - ( x_n + y_n ) \right| \leqslant \frac{2}{3^{n}},

   (:math:`z` 或者落在某相邻两格点之间, 此时到较近格点的距离不超过半个步长; 或落在最右格点
   :math:`2 - 2 \cdot 3^{-n}` 与 :math:`2` 之间, 此时距离不超过一个步长.) 由 Bolzano--Weierstrass 定理,
   点列 :math:`\{ ( x_n, y_n ) \}` 有收敛子列 :math:`( x_{n_j}, y_{n_j} ) \to ( x_0, y_0 )`;
   由于 :math:`P_0` 是闭集, 有 :math:`( x_0, y_0 ) \in P_0 \times P_0`, 且由上面的不等式知
   :math:`x_{n_j} + y_{n_j} \to z`, 故 :math:`x_0 + y_0 = z`. 这就证明了 :math:`[0, 2] \subset P_0 + P_0`;
   反方向的包含由 :math:`P_0 \subset [0, 1]` 是显然的. 于是 :math:`P_0 + P_0 = [0, 2]`.

   对于差集, 注意康托三分集关于点 :math:`\dfrac{1}{2}` 对称: 由
   :math:`1 - \varphi_1 ( x ) = \varphi_2 ( 1 - x )` 与式 :eq:`ex-1-27-eq-1` 用归纳法易得
   :math:`F_n = 1 - F_n` 对一切 :math:`n` 成立, 对 :math:`n` 取交即得 :math:`P_0 = 1 - P_0`
   (在三进表示下, 对称性就是各位数字 :math:`0 \leftrightarrow 2` 的互换). 于是
   :math:`- P_0 = P_0 - 1`, 从而

   .. math::
      P_0 - P_0 = P_0 + ( - P_0 ) = \left( P_0 + P_0 \right) - 1 = [0, 2] - 1 = [-1, 1],

   包含 :math:`P_0 - P_0 \subset [-1, 1]` 同样由 :math:`P_0 \subset [0, 1]` 显然. 综上所述, 有
   :math:`P_0 + P_0 = [0, 2]`, :math:`P_0 - P_0 = [-1, 1]`.

   .. note::
      另一种解法逐位拆分, 无需利用闭性. 令
      :math:`C = \dfrac{1}{2} P_0 = \left\{ \dfrac{x}{2} : x \in P_0 \right\}`, 那么 :math:`x \in C`
      当且仅当 :math:`x` 有各位数字只取 :math:`0, 1` 的三进表示 :math:`x = \sum\limits_{k=1}^{\infty} b_k 3^{-k}`
      (此时 :math:`2 x = \sum\limits_{k=1}^{\infty} 2 b_k 3^{-k}` 的各位数字只取 :math:`0, 2`, 故
      :math:`2x \in P_0`). 任取 :math:`w \in [0, 1]`, 取它的三进表示 :math:`w = \sum\limits_{k=1}^{\infty} c_k 3^{-k}`,
      :math:`c_k \in \{ 0, 1, 2 \}` (当 :math:`w = 1` 时取 :math:`c_k \equiv 2`). 逐位拆分:
      当 :math:`c_k \leqslant 1` 时取 :math:`b_k = 0, d_k = c_k`; 当 :math:`c_k = 2` 时取
      :math:`b_k = d_k = 1`. 那么 :math:`b_k, d_k \in \{ 0, 1 \}` 且 :math:`b_k + d_k = c_k`,
      于是 :math:`x = \sum b_k 3^{-k} \in C`, :math:`y = \sum d_k 3^{-k} \in C` 满足 :math:`x + y = w`
      (逐位相加, 无进位). 这就得到 :math:`[0, 1] \subset C + C`; 反向包含由 :math:`C \subset [0, \tfrac{1}{2}]`
      显然, 故 :math:`[0, 1] = C + C`. 于是

      .. math::
         P_0 + P_0 = 2 \left( C + C \right) = [0, 2],

      再结合 :math:`P_0 = 1 - P_0` 同样得到 :math:`P_0 - P_0 = [-1, 1]`.

   .. note::
      也可以不显式使用三进表示, 直接对构造作归纳. 补记 :math:`F_0 = [0, 1]`, 先证
      :math:`F_n + F_n = [0, 2]` 对一切 :math:`n \geqslant 0` 成立: :math:`n = 0` 时显然; 由
      :math:`F_{n+1} = \varphi_1 ( F_n ) \cup \varphi_2 ( F_n )` 与归纳假设,

      .. math::
         F_{n+1} + F_{n+1}
         = \bigcup_{i, j \in \{ 1, 2 \}} \left( \varphi_i ( F_n ) + \varphi_j ( F_n ) \right)
         = \left[ 0, \frac{2}{3} \right] \cup \left[ \frac{2}{3}, \frac{4}{3} \right] \cup \left[ \frac{4}{3}, 2 \right]
         = [0, 2],

      其中 :math:`\varphi_1 ( F_n ) + \varphi_1 ( F_n ) = \dfrac{ F_n + F_n }{3} = \left[ 0, \dfrac{2}{3} \right]`,
      :math:`\varphi_1 ( F_n ) + \varphi_2 ( F_n ) = \dfrac{ F_n + F_n + 2 }{3} = \left[ \dfrac{2}{3}, \dfrac{4}{3} \right]`,
      :math:`\varphi_2 ( F_n ) + \varphi_2 ( F_n ) = \dfrac{ F_n + F_n + 4 }{3} = \left[ \dfrac{4}{3}, 2 \right]`.
      于是对任意 :math:`z \in [0, 2]` 与每个 :math:`n`, 都存在 :math:`x_n, y_n \in F_n` 使得
      :math:`x_n + y_n = z` 精确成立. 由 Bolzano--Weierstrass 定理, :math:`\{ x_n \}` 有收敛子列
      :math:`x_{n_j} \to x_0 \in [0, 1]`, 相应地 :math:`y_{n_j} = z - x_{n_j} \to y_0 = z - x_0`.
      对任意固定的 :math:`m`, 当 :math:`j` 充分大时 :math:`n_j \geqslant m`, 此时
      :math:`x_{n_j}, y_{n_j} \in F_{n_j} \subset F_m`, 而 :math:`F_m` 是闭集, 取极限得
      :math:`x_0, y_0 \in F_m`. 由 :math:`m` 的任意性得 :math:`x_0, y_0 \in P_0`, 从而
      :math:`z = x_0 + y_0 \in P_0 + P_0`.
