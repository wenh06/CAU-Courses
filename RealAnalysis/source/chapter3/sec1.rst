§1 可测函数的基本性质
------------------------------------------

.. _ex-3-1:

1. 设 :math:`f(x), g(x)` 为可测集 :math:`E` 上的可测函数, 试证 :math:`E(f > g)` 是可测集.

.. proof:proof::

   由于 :math:`f(x), g(x)` 都是可测函数, 那么 :math:`f - g` 也是可测函数, 于是由可测函数定义知 :math:`E(f > g) = E(f - g > 0)` 是可测集.

   .. note::

      也可以像证明 :math:`f - g` 是可测函数那样, 将 :math:`E(f > g)` 具体写出来:

      .. math::

         E(f > g) = \bigcup_{r \in \mathbb{Q}} \left( E(f > r) \cap E(g < r) \right).

      以上集合的可测性需要用到 :ref:`下一题 <ex-3-2>` 的结论.

.. _ex-3-2:

2. 证明 :math:`f(x)` 为 :math:`E` 上可测函数的充分必要条件是: 对于任一有理数 :math:`r`, 集 :math:`E(f > r)` 恒可测.
   如果假设对任一有理数 :math:`r`, 集 :math:`E(f = r)` 恒可测, 问 :math:`f(x)` 是否可测?

.. proof:proof::

   由 :ref:`本章补充材料 <measurable-function-supp>` 知, 若存在 :math:`D` 为 :math:`\mathbb{R}` 中稠密集,
   使得 :math:`\forall ~ \alpha \in D`, :math:`E(f > \alpha)` 都是可测集, 则 :math:`f` 是可测函数.
   特别地, 本题中取 :math:`D` 为有理数集 :math:`\mathbb{Q}`, 则 :math:`\forall ~ r \in \mathbb{Q}`,
   :math:`E(f > r)` 都是可测集, 于是 :math:`f` 是可测函数. 反过来显然.

   集 :math:`E(f = r)` 恒可测, 不能推出 :math:`f` 是可测函数. 反例如下: 设 :math:`E = [0, 1]`,
   集合 :math:`A \subset E` 是不可测集, 函数 :math:`f(x) = \chi_A(x) + \alpha`, 其中 :math:`\alpha` 为某个无理数,
   那么任取 :math:`r \in \mathbb{Q}`, 有 :math:`E(f = r) = \emptyset`, 是可测集, 但 :math:`f` 不是可测函数.

.. _ex-3-4:

4. 设 :math:`f(x)` 是 :math:`E` 上的可测函数, :math:`G, F` 分别为 :math:`\mathbb{R}` 中开集与闭集.
   试问 :math:`E(f \in G)` 与 :math:`E(f \in F)` 是否可测, 这里记号 :math:`E(f \in A) = E(x: f(x) \in A)`.

.. proof:proof::

   设开集 :math:`G \subset \mathbb{R}` 有结构表示 :math:`\displaystyle G = \bigcup_{n=1}^{\infty} (a_n, b_n)`, 则

   .. math::

      E(f \in G) = f^{-1}(G) = f^{-1} \left(\bigcup_{n=1}^{\infty} (a_n, b_n)\right) = \bigcup_{n=1}^{\infty} f^{-1}((a_n, b_n))
      = \bigcup_{n=1}^{\infty} E(f > a_n) \cap E(f < b_n)

   因此 :math:`E(f \in G)` 是可测集.

   对于闭集 :math:`F \subset \mathbb{R}`, 有 :math:`\mathbb{R} \setminus F` 是开集, 于是

   .. math::

      E(f \in F) = E(f \in \mathbb{R} \setminus (\mathbb{R} \setminus F)) = E \setminus E(f \in \mathbb{R} \setminus F)

   是可测集.

.. _ex-3-7:

7. 设 :math:`f(x)` 是 :math:`(-\infty, \infty)` 上的连续函数, :math:`g(x)` 是 :math:`[a, b]` 上的有限可测函数,
   证明 :math:`f(g(x))` 是可测函数.

.. proof:proof::

   由于 :math:`\mathbb{R}` 中开集有由互不相交的开区间构成的结构表示, 而有限函数 :math:`h(x)` 可测当且仅当
   :math:`E(a < h < b)` 对所有的开区间 :math:`(a, b)` 都可测, 因此 :math:`h(x)` 可测当且仅当
   :math:`E(f \in G)` 对所有的开集 :math:`G \subset \mathbb{R}` 都可测. 由于 :math:`f(x)` 是连续函数,
   因此 :math:`f^{-1}(G)` 是开集, 那么

   .. math::

      E(f \circ g \in G) = E(g \in f^{-1}(G)) = E(g \in f^{-1}(G))

   是可测集, 即 :math:`f \circ g` 是可测函数.

.. _ex-3-8:

8. 设 :math:`f(x)` 是可测集 :math:`E` 上的可测函数, :math:`B` 是 :math:`\mathbb{R}` 中的 Borel 集. 试证 :math:`f^{-1}(B)` 是可测集.
   又当 :math:`B` 是任意可测集时, :math:`f^{-1}(B)` 是否可测?

.. proof:proof::

   记 :math:`\mathscr{B}` 为 :math:`\mathbb{R}` 中的 Borel 集族, 那么它是由半开闭区间组成的集族生成的 :math:`\sigma`-代数:

   .. math::

      \mathscr{B} = \mathscr{R}_{\sigma} (\mathscr{S}), \quad \mathscr{S} \left\{ [a, b) : a < b \in \mathbb{R} \right\}.

   由 :ref:`上一章第 37 题 <ex-2-37>` 知

   .. math::

      f^{-1}(\mathscr{B}) = f^{-1}(\mathscr{R}_{\sigma} (\mathscr{S})) = \mathscr{R}_{\sigma} (f^{-1}(\mathscr{S})).

   对任意半开闭区间 :math:`[a, b)`, 有 :math:`f^{-1}([a, b)) = E(a \leqslant f < b)`, 是可测集.
   由于 :math:`\mathbb{R}` 中的可测集族 :math:`\mathscr{M}` 是 :math:`\sigma`-代数, 因此有

   .. math::

      \mathscr{M} \supset \mathscr{R}_{\sigma} (f^{-1}(\mathscr{S})) = f^{-1}(\mathscr{B}).

   因此对于 :math:`B \in \mathscr{B}`, 有 :math:`f^{-1}(B) \in \mathscr{M}`, 是可测集.

   当 :math:`B` 是任意可测集时, :math:`f^{-1}(B)` 不一定是可测集. 反例如下: 设 :math:`E = [0, 1]`,
   令 :math:`\Phi` 为 Cantor 函数 (见 :ref:`第一章补充材料 <cantor-function>`), 并令 :math:`\displaystyle \Psi(x) = \dfrac{1}{2} (\Phi(x) + x)`,
   那么 :math:`\Psi(x)` 是 :math:`E \to E` 的连续, 严格递增的双射, 从而有逆映射 :math:`f = \Psi^{-1}`.
   :math:`f` 也是 是 :math:`E \to E` 的连续, 严格递增的函数, 从而是可测的.

   记 Cantor 三分集为 :math:`P_0`, 它的补集为 :math:`G_0`, 那么 Cantor 函数 :math:`\Phi` 在 :math:`G_0` 的每个构成区间上是常值函数,
   于是 :math:`\Psi` 在 :math:`G_0` 的每个构成区间上是线性函数, 每个构成区间在 :math:`\Psi` 下的像是一个开区间, 长度为原区间的一半,
   因此 :math:`\Psi(G_0)` 是测度为 :math:`1/2` 的开集, :math:`\Psi(G_0)` 的补集 :math:`\Psi(P_0)` 是测度为 :math:`1/2` 的闭集.
   令 :math:`W \subset \Psi(P_0)` 为不可测集, 并取 :math:`B = \Psi^{-1}(W) \subset P_0` 为零测集, 那么 :math:`B` 是可测集.
   但 :math:`f^{-1}(B) = \Psi(B) = W` 是不可测集.

.. _ex-3-9:

9. 试在 :math:`\mathbb{R}` 上定义一个实函数, 使它在每个区间上的限制均不可测.

.. proof:solution::

   令 :math:`E = \mathbb{R} / \mathbb{Q}` 为 :math:`\mathbb{R}` 中等价关系

   .. math::

      x \sim y \Longleftrightarrow x - y \in \mathbb{Q}, \quad x, y \in \mathbb{R},

   的每个等价类中代表元素的集合. 之前已经证明过, :math:`E` 是不可测集, 且在 :math:`\mathbb{R}` 中稠密,
   并且 :math:`E` 与每个区间的交集都是不可测集. 令 :math:`f = \chi_E` 为 :math:`\mathbb{R}` 上的特征函数,
   那么 :math:`f` 在每个区间上的限制都是不可测函数.

.. _ex-3-10:

10. 设 :math:`x \in [0, 1)` 的三进表示为 :math:`x = 0.x_1 x_2 \cdots x_n \cdots`, :math:`x_n \in \{0, 1, 2\}`,
    并约定全用无限表示. 用 :math:`P_i` 表示 :math:`x` 的三进表示中不出现数字 :math:`i` 的点集, :math:`i = 0, 1, 2`. 令

    .. math::

      f(x) = \begin{cases}
         x + i, & x \in P_i, i = 0, 1, 2, \\
         x + 3, & x \in [0, 1) \setminus \cup_{i=0}^2 P_i,
      \end{cases}

    并规定 :math:`f(0) = 3, f(1/2) = 7/2`. 问 :math:`f(x)` 是否可测, 是否连续?

.. proof:solution::

   对每一个自然数 :math:`n`, 将 :math:`(0, 1)` 开区间分成 :math:`3^n` 个等长的开区间, 依顺序记为 :math:`I_{n, k} = \left(\dfrac{k}{3^n}, \dfrac{k+1}{3^n}\right)`,
   :math:`k = 0, 1, \cdots, 3^n - 1`. 那么

   .. math::

      x \in I_{n, k} \Longrightarrow x \text{ 的三进表示中第 } n \text{ 位数字为 } k \mod{3}.

   同时, 除 :math:`0, 1` 以外, 这些区间的端点为 :math:`1/3^n, 2/3^n, \cdots, (3^n - 1)/3^n`, 相应的无限三进表示分别为

   .. math::

      0.\cdots 0 2 2 \cdots, 0.\cdots 1 2 2 \cdots, 0.\cdots 2 2 2 \cdots, \cdots

   因此有 (不交并表示）

   .. math::

      P_i = P_i^{(0)} \cup Z_i,

   其中

   .. math::

      P_i^{(0)} = \bigcap_{n=1}^{\infty} \left( \bigcup_{k \not\equiv i \mod{3}} I_{n, k} \right),

   :math:`Z_i \subset C` 是 Cantor 三分集 :math:`C` 的子集, 为零测集. 因此 :math:`P_i` 都是可测集. 我们还可以将 :math:`P_i` 表示为

   .. math::

      P_i = \left( \bigcap_{n=1}^{\infty} \left( \bigcup_{k \not\equiv i \mod{3}} I_{n, k}^{(i)} \right) \right) \setminus E_i,

   其中

   .. math::

      & I_{n, k}^{(2)} = I_{n, k}, \quad E_i = \emptyset, \\
      & I_{n, k}^{(1)} = I_{n, k} \cup \left\{ \dfrac{k+1}{3^n} \right\} = \left( \dfrac{k}{3^n}, \dfrac{k+1}{3^n} \right], \quad E_1 = \left\{ 1 \right\}, \\
      & I_{n, k}^{(0)} = I_{n, k} \cup \left\{ \dfrac{k}{3^n} \right\} = \left[ \dfrac{k}{3^n}, \dfrac{k+1}{3^n} \right), \quad E_0 = \left\{ 0 \right\}.

   注意到 :math:`P_i` 的交可能非空, 事实上有

   .. math::

      P_0 \cap P_1 & = Z_0 \cap Z_1 = \{0.222\cdots\} = \{1\} \not\subset [0, 1), \text{因此 } P_0 \cap P_1 = \emptyset, \\
      P_1 \cap P_2 & = Z_1 \cap Z_2 =\{0.000\cdots\} = \{0\}, \\
      P_2 \cap P_0 & = Z_2 \cap Z_0 = \{0.111\cdots\} = \{1/2\}.

   因此需要如题干中所述对 :math:`f(x)` 进行特殊定义. 同时, 易知

   .. math::

      f(P_0) \subset [0, 1], f(P_1) \subset [1, 2], f(P_2) \subset [2, 3], f \left( [0, 1) \setminus \bigcup_{i=0}^2 P_i \right) \subset [3, 4].

   于是有

   .. math::

      E(f > \alpha) = \begin{cases}
         \emptyset, & \alpha > 4, \\
         (\alpha - 3, +\infty) \cap ([0, 1) \setminus \cup_{i=0}^2 P_i), & 3 < \alpha \leqslant 4, \\
         (\alpha - 2, +\infty) \cap P_2, & 2 < \alpha \leqslant 3, \\
         P_2 \cup ((\alpha - 1, +\infty) \cap P_1), & 1 < \alpha \leqslant 2, \\
         P_2 \cup P_1 \cup ((\alpha, +\infty) \cap P_0), & 0 < \alpha \leqslant 1, \\
         [0, 1), & \alpha \leqslant 0.
      \end{cases}

   以上集合都是可测集, 因此 :math:`f(x)` 是可测函数.

   函数 :math:`f(x)` 在 :math:`[0, 1)` 上不连续. 事实上, 任取 :math:`\displaystyle x \in \left( \bigcup_{i=0}^2 P_i \right) \setminus \left\{ 0, \dfrac{1}{2} \right\}`.
   对任意 :math:`0 < \varepsilon < \dfrac{1}{2}`, 取 :math:`n \in \mathbb{N}` 使得 :math:`3^{-n} < \varepsilon`,
   将 :math:`x` 的三进表示中第 :math:`n + 1` 至 :math:`n + 3` 位数字改为 :math:`012`, 记得到的数为 :math:`x'`, 则 :math:`x' \not \in \bigcup_{i=0}^2 P_i`,
   且 :math:`\lvert x - x' \rvert < 3^{-n} < \varepsilon`, 但同时有

   .. math::

      \lvert f(x') - f(x) \rvert = \lvert x' + 3 - x - i \rvert \geqslant 3 - i - \lvert x' - x \rvert \geqslant \dfrac{5}{2} - i > \dfrac{1}{2} > \varepsilon.

   上式中 :math:`i \in \{0, 1, 2\}` 为 :math:`x` 所属集合 :math:`P_i` 的下标. 因此 :math:`f(x)` 在 :math:`[0, 1)` 上不连续.

.. _ex-3-11:

11. 设 :math:`f(x, y)` 为定义在 :math:`\mathbb{R}^2` 上的几乎处处有限的函数, 它对每个固定的 :math:`x` 关于 :math:`y` 连续,
    且对每个固定的 :math:`y` 关于 :math:`x` 也连续. 试证 :math:`f(x, y)` 是 :math:`\mathbb{R}^2` 上的可测函数.

.. proof:proof::

   对每个自然数 :math:`n \in \mathbb{N}`, 令

   .. math::

      f_n(x, y) = f \left( \dfrac{[nx]}{n}, y \right),

   其中 :math:`[nx]` 表示 :math:`nx` 的整数部分.

   首先, 证明每个 :math:`f_n(x, y)` 都是可测函数: :math:`\forall ~ \alpha \in \mathbb{R}`, 有

   .. math::

      E(f_n > \alpha) & = \left\{ (x, y) \in \mathbb{R}^2 : f_n(x, y) > \alpha \right\} = \left\{ (x, y) \in \mathbb{R}^2: f \left( \dfrac{[nx]}{n}, y \right) > \alpha \right\} \\
      & = \bigcup_{k \in \mathbb{Z}} \left[ \dfrac{k}{n}, \dfrac{k+1}{n} \right) \times \left\{ y \in \mathbb{R}: f \left( \dfrac{k}{n}, y \right) > \alpha \right\},

   由于 :math:`f(x, y)` 对每个固定的 :math:`x` 关于 :math:`y` 连续, 那么集合
   :math:`\left\{ y \in \mathbb{R}: f \left( \dfrac{k}{n}, y \right) > \alpha \right\}` 是开集, 因此 :math:`E(f_n > \alpha)` 是可测集,
   于是 :math:`f_n(x, y)` 是可测函数.

   其次, 证明 :math:`\displaystyle \lim_{n \to \infty} f_n(x, y) = f(x, y)`. 事实上, 由于 :math:`f(x, y)` 对每个固定的 :math:`y` 关于 :math:`x` 连续,
   因此 :math:`\forall ~ \varepsilon > 0`, 存在 :math:`\delta > 0`, 使得 :math:`\forall ~ x' \in \mathbb{R}`, 当 :math:`\lvert x' - x \rvert < \delta` 时,
   有 :math:`\lvert f(x', y) - f(x, y) \rvert < \varepsilon`. 又由于

   .. math::

      \lim_n \dfrac{[nx]}{n} = x

   对任意 :math:`x \in \mathbb{R}` 成立, 那么对取好的 :math:`\delta > 0`, 存在 :math:`N \in \mathbb{N}`, 使得
   :math:`\forall ~ n > N`, 有 :math:`\left\lvert \dfrac{[nx]}{n} - x \right\rvert < \delta`. 于是有

   .. math::

      \lvert f_n(x, y) - f(x, y) \rvert = \left\lvert f \left( \dfrac{[nx]}{n}, y \right) - f(x, y) \right\rvert < \varepsilon, \forall ~ n > N.

   这就证明了 :math:`\displaystyle \lim_{n \to \infty} f_n(x, y) = f(x, y)` 对所有的 :math:`(x, y) \in \mathbb{R}^2` 成立.
   根据可测函数列的性质, :math:`\displaystyle f = \lim_n f_n` 也是可测函数.
