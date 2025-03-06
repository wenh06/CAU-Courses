§4 关于测度的几点评注
------------------------------------------

.. _ex-2-24:

24. 设 :math:`E` 是一维有界集, :math:`I_1, I_2, \dots` 是任意区间集列 (可以相交), 其并覆盖 :math:`E`, 试证

    .. math::

      m^*(E) = \inf\limits_{\cup I_k \supset E} \sum\limits_{k=1}^\infty l(I_n).

    对于二维情形如何?

.. proof:proof::

   在一维有界集的情况, :math:`E` 的外测度定义为

   .. math::

      m^* E = \inf_{G \supset E} m G = \inf_{\cup J_k = G \supset E} \sum_k m I_k \geqslant \inf_{\cup I_k \supset E} \sum_k m I_k,

   其中 :math:`G` 为包含 :math:`E` 的开集, :math:`m G = \sum\limits_{k} m J_k` 为 :math:`G` 的测度,
   :math:`G = \bigcup\limits_k J_k` 为 :math:`G` 的结构表示.
   最后的不等式成立是因为结构表示 :math:`\{J_k\}` 是任意区间集列 :math:`\{I_k\}` 的特例.

   另一方面, 由于外测度的次可加性, 对所有覆盖 :math:`E` 的区间集列 :math:`\{I_k\}` 有

   .. math::

      m^* E \leqslant \sum\limits_{k=1}^\infty m^* I_k = \sum\limits_{k=1}^\infty m I_k,

   从而有

   .. math::

      m^* E \leqslant \inf_{\cup I_k \supset E} \sum\limits_{k=1}^\infty m I_k.

   综上, 有

   .. math::

      m^* E = \inf_{\cup I_k \supset E} \sum\limits_{k=1}^\infty l(I_n).

   对于二维 (或更高维) 情形, 需要将区间集列改为矩体集列.

.. _ex-2-25:

25. 设 :math:`Q` 是 :math:`\mathbb{R}^2` 中的单位正方形 :math:`[0,1;0,1]`, :math:`\{E_n\}_{n \in \mathbb{N}}` 是 :math:`Q` 中的可测集列,
    且数列 :math:`\{m E_n \}_{n \in \mathbb{N}}` 有聚点 :math:`1`, 证明存在子列 :math:`\{E_{n_k}\}_{k \in \mathbb{N}}` 使
    :math:`m \left( \bigcap\limits_{k=1}^\infty E_{n_k} \right) > 0`.

.. proof:proof::

   由于数列 :math:`\{m E_n \}_{n \in \mathbb{N}}` 有聚点 :math:`1`, 那么存在子列 :math:`\{E_{n_k}\}_{k \in \mathbb{N}}`
   使得 :math:`\lim\limits_{k \to \infty} m E_{n_k} = 1`. 令基本集为单位正方形 :math:`[0,1;0,1]`,
   那么有 :math:`\lim\limits_{k \to \infty} m \mathscr{C} E_{n_k} = 0`. 那么对任意的 :math:`\varepsilon > 0`,
   可以选出 :math:`\{E_{n_k}\}_{k \in \mathbb{N}}` 的子列 :math:`\{E_{n_{k_i}}\}_{i \in \mathbb{N}}` 使得

   .. math::

      m \mathscr{C} E_{n_{k_i}} < \frac{\varepsilon}{2^i}, \quad i \in \mathbb{N}.

   那么有

   .. math::

      m \left( \bigcap_{i = 1}^{\infty} E_{n_{k_i}} \right) = 1 - m \left( \bigcup_{i = 1}^{\infty} \mathscr{C} E_{n_{k_i}} \right)
      \geqslant 1 - \sum_{i = 1}^{\infty} m \mathscr{C} E_{n_{k_i}} \geqslant 1 - \varepsilon.

   :math:`\varepsilon` 足够小的时候 (比如 :math:`\varepsilon < 1`), 有 :math:`m \left( \bigcap\limits_{i=1}^\infty E_{n_{k_i}} \right) > 0`.
   所以, 子列 :math:`\{E_{n_{k_i}}\}_{i \in \mathbb{N}}` 即是题目所求.

.. _ex-2-27:

27. 设 :math:`E` 是 :math:`\mathbb{R}` 中的可测集, 证明 :math:`D(E) = \left\{ (x,y) \in \mathbb{R}^2 : x-y \in E \right\}` 是 :math:`\mathbb{R}^2` 中的可测集.

.. proof:proof::

   由于 :math:`E` 是 :math:`\mathbb{R}` 中的可测集, 那么存在一个 :math:`F_{\sigma}` 集 :math:`F`, 即 :math:`E` 的等测核,
   使得 :math:`F \subset E` 且 :math:`m F = m E`. 记 :math:`Z = E \setminus F`, 那么 :math:`Z` 是零测集, 且

   .. math::

      E = F \cup Z

   为一个 Borel 集与零测集的不交并. 令

   .. math::

      f: \mathbb{R}^2 \to \mathbb{R}, \quad f(x, y) = x - y,

   那么 :math:`f` 是一个线性映射, 从而是连续的. 令 :math:`\mathscr{B}` 为 :math:`\mathbb{R}` 中的 Borel 集构成的 :math:`\sigma` 代数,
   那么由 :ref:`本节第 35 题 <ex-2-35>` 知 :math:`\{ f^{-1} (B) : B \in \mathscr{B} \}` 为 :math:`\mathbb{R}^2` 中的 :math:`\sigma` 代数.
   由于开集在连续映射下的原像为开集, 所以这个 :math:`\sigma` 代数是 :math:`\mathbb{R}^2` 中的 Borel :math:`\sigma` 代数.
   由于 :math:`D(E) = f^{-1} (E) = f^{-1} (F) \cup f^{-1} (Z)`, 其中 :math:`f^{-1} (F)` 为 :math:`\mathbb{R}^2` 中的 Borel 集,
   只要证明 :math:`f^{-1} (Z)` 为 :math:`\mathbb{R}^2` 中的零测集, 即有 :math:`D(E)` 为 :math:`\mathbb{R}^2` 中的可测集.

   下证 :math:`f^{-1} (Z)` 为 :math:`\mathbb{R}^2` 中的零测集. 事实上, :math:`f` 可以视为如下两个映射的复合:

   .. math::

      & T: \mathbb{R}^2 \to \mathbb{R}^2, \quad T(x, y) = (x - y, y), \\
      & \operatorname{pr}_1: \mathbb{R}^2 \to \mathbb{R}, \quad \operatorname{pr}_1 (x, y) = x,

   即 :math:`f = \operatorname{pr}_1 \circ T`. 由于 :math:`T` 是一个非奇异线性变换, 对任意 :math:`A \subset \mathbb{R}^2` 有
   (这个结论参见 :ref:`本节第 32 题 <ex-2-32>`)

   .. math::

      m^* (T^{-1}(A)) = \lvert \det T^{-1} \rvert m^* A,

   所以只要证明 :math:`\operatorname{pr}_1^{-1} (Z)` 为 :math:`\mathbb{R}^2` 中的零测集即可. 事实上任取 :math:`\varepsilon > 0`, 有

   .. math::

      \operatorname{pr}_1^{-1} (Z) = \{ (x, y) \in \mathbb{R}^2 : x \in Z \} = Z \times \mathbb{R} \subset \bigcup_{k = 1}^{\infty} G_k \times (-k, k),

   其中 :math:`Z \subset G_k \subset \mathbb{R}` 是开集, 且 :math:`m G_k < \dfrac{\varepsilon}{k \cdot 2^{k+1}}`.
   这样的 :math:`G_k` 总可以取到, 因为 :math:`Z` 是零测集. 那么有

   .. math::

      m^* \left( \operatorname{pr}_1^{-1} (Z) \right) \leqslant \sum_{k = 1}^{\infty} m^* \left( G_k \times (-k, k) \right)
      = \sum_{k = 1}^{\infty} m G_k \cdot 2k < \sum_{k = 1}^{\infty} \frac{\varepsilon}{k \cdot 2^{k+1}} \cdot 2k = \varepsilon.

   由于 :math:`\varepsilon` 是任意的正数, 所以 :math:`\operatorname{pr}_1^{-1} (Z)` 为 :math:`\mathbb{R}^2` 中的零测集.
   于是我们证明了 :math:`\operatorname{pr}_1^{-1} (Z)` 为 :math:`\mathbb{R}^2` 中的零测集.

   综上所述,

   .. math::

      D(E) = f^{-1} (F) \cup f^{-1} (Z) = f^{-1} (F) \cup T^{-1} (\operatorname{pr}_1^{-1} (Z))

   为 :math:`\mathbb{R}^2` 中的可测集.

   .. note::

      可以利用一般性的结论: 设 :math:`f: \mathbb{R}^n \to \mathbb{R}` 可测, :math:`T: \mathbb{R}^n \to \mathbb{R}^n` 为非奇异线性变换,
      那么 :math:`f \circ T` 为可测函数. 那么这题就归结为证明 :math:`\operatorname{pr}_1: \mathbb{R}^2 \to \mathbb{R}` 为可测函数,
      以及在映射 :math:`\operatorname{pr}_1` 下, 零测集的原像仍为零测集.

.. _ex-2-28:

28. 设 :math:`A` 为一维可测集且 :math:`m A > 0`, 证明 :math:`A` 存在不可测子集.

.. proof:proof::

   令 :math:`E_n` 为 :ref:`本章第 15 题 <ex-2-15>` 中的集列, 每个 :math:`E_n \subset [0, 1)` 都不可测, 两两互不相交,
   并且 :math:`\displaystyle \bigcup_{n=1}^{\infty} E_n = [0, 1)`. 对 :math:`n, k \in \mathbb{N}`, 令

   .. math::

      E_{n, k} = E_n + k = \{ x + k ~ : ~ x \in E_n \},

   那么 :math:`E_{n, k}` 也是不可测集, 两两互不相交, 且 :math:`\displaystyle \bigcup_{n, k \in \mathbb{N}} E_{n, k} = \mathbb{R}`.
   令 :math:`A_{n, k} = A \cap E_{n, k}`, 那么 :math:`A_{n, k}` 两两互不相交, 且 :math:`\displaystyle \bigcup_{n, k \in \mathbb{N}} A_{n, k} = A`.

   若对所有 :math:`n, k \in \mathbb{N}`, 集 :math:`A_{n, k}` 都是可测的, 那么由测度的 :math:`\sigma`-可加性知

   .. math::

      m A = \sum\limits_{n, k \in \mathbb{N}} m A_{n, k}.

   由于 :math:`m A > 0`, 那么至少存在一个 :math:`n_0, k_0 \in \mathbb{N}`, 使得 :math:`m A_{n_0, k_0} > 0`. 那么对每个 :math:`n \in \mathbb{N}`,
   可以找到 :math:`E_{n, k_0}` 中的正测度的可测子集

   .. math::

      (A_{n_0, k_0} - k_0 + r_n \mod 1) + k_0 = \{ x + k_0 ~ : ~ x \in A_{n_0, k_0} - k_0 + r_n \mod 1 \},

   其中 :math:`\mathbb{Q} = \{ r_n \}_{n \in \mathbb{N}}` 是有理数集. 这些集合两两互不相交, 那么由测度的 :math:`\sigma`-可加性知

   .. math::

      1 = m [k, k + 1) \geqslant \sum_{n \in \mathbb{N}} m \left( (A_{n_0, k_0} - k_0 + r_n \mod 1) + k_0 \right)
      = \sum_{n \in \mathbb{N}} m A_{n_0, k_0} = \infty,

   矛盾. 所以至少存在一个 :math:`n_0, k_0 \in \mathbb{N}`, 使得 :math:`A_{n_0, k_0}` 不可测.

.. _ex-2-29:

29. 设 :math:`E` 为 :math:`(0, 1)` 中正测度子集且存在常数 :math:`c > 0` 使对 :math:`(0, 1)` 中的变动区间 :math:`I` 有
    :math:`\lim\limits_{m I \to 0} m(E \cap I) / m I = c`, 证明 :math:`m E = 1`.

.. proof:proof::

   首先, 由于 :math:`E \cap I \subset I`, 所以有 :math:`m(E \cap I) \leqslant m I`, 从而有 :math:`m(E \cap I) / m I \leqslant 1`.
   由此可知必须有 :math:`c \leqslant 1`.

   由于 :math:`\lim\limits_{m I \to 0} m(E \cap I) / m I = c`, 那么任取 :math:`0 < c' < c`, 存在 :math:`\delta > 0`,
   使得当 :math:`m I < \delta` 时有 :math:`m(E \cap I) / m I > c'`, 即

   .. math::
      :label: ex-2-29-eq-1

      m(E \cap I) > c' m I.

   假设 :math:`m E < 1`, 那么 :math:`m \mathscr{C} E > 0`,
   即 :math:`\mathscr{C} E` 是具有正测度的可测集, 那么根据引理 4.1, 对于数 :math:`\alpha = 1 - \dfrac{c'}{2} \in (0, 1)`,
   存在开区间 :math:`J \subset (0, 1)`, 使得

   .. math::
      :label: ex-2-29-eq-2

      m \left( \mathscr{C} E \cap J \right) > \alpha m J = \left( 1 - \frac{c'}{2} \right) m J.

   可以假设 :math:`m J < \delta`, 否则可以将 :math:`J` 平均分割成若干个长度小于 :math:`\delta` 的开区间 (有限个区间端点对测度不影响),
   那么其中至少有一个开区间 :math:`J'` 满足 :math:`m \left( \mathscr{C} E \cap J' \right) > \alpha m J'`,
   否则上述不等式不成立. 那么由式 :eq:`ex-2-29-eq-1` 知

   .. math::
      :label: ex-2-29-eq-3

      m \left( E \cap J \right) > c' m J.

   式 :eq:`ex-2-29-eq-3` 与式 :eq:`ex-2-29-eq-2` 相加, 有

   .. math::

      m J = m \left( \mathscr{C} E \cap J \right) + m \left( E \cap J \right)
      > \left( 1 - \frac{c'}{2} \right) m J + c' m J = \left( 1 + \frac{c'}{2} \right) m J,

   从而有 :math:`c' m J < 0`, 矛盾. 所以必须有 :math:`m E = 1`.

.. _ex-2-30:

30. 设 :math:`\{E_n\}_{n \in \mathbb{N}}` 为 :math:`\mathbb{R}` 中互不相交的集列, 满足条件
    :math:`m^* \left( \bigcup\limits_{n=1}^\infty E_n \right) < \sum\limits_{n=1}^\infty m^* (E_n)`,
    证明存在最小的自然数 :math:`N` 使得 :math:`m^* \left( \bigcup\limits_{n=1}^N E_n \right) < \sum\limits_{n=1}^N m^* (E_n)`,
    并且此时 :math:`E_N` 是不可测的.

.. proof:proof::

   对所有 :math:`n \in \mathbb{N}`, 令 :math:`\displaystyle A_n = \bigcup_{k=1}^{n} E_k`, 那么 :math:`\{A_n\}_{n \in \mathbb{N}}`
   形成了一个渐张集列, 且有 :math:`\displaystyle \bigcup_{n=1}^{\infty} A_n = \bigcup_{n=1}^{\infty} E_n`.
   由 :ref:`本章第 3 节第 14 题 <ex-2-14>` 有

   .. math::
      :label: ex-2-30-eq-1

      m^* \left( \bigcup_{n=1}^{\infty} E_n \right) = m^* \left( \bigcup_{n=1}^{\infty} A_n \right)
      = \lim_{n \to \infty} m^* A_n = \lim_{n \to \infty} m^* \left( \bigcup_{k=1}^{n} E_k \right).

   假设对所有自然数 :math:`n`, 有 :math:`m^* \left( \bigcup\limits_{k=1}^n E_k \right) = \sum\limits_{k=1}^n m^* E_k`,
   对此式两边同时取极限 :math:`n \to \infty`, 有

   .. math::
      :label: ex-2-30-eq-2

      \lim_{n \to \infty} m^* \left( \bigcup_{k=1}^{n} E_k \right) = \lim_{n \to \infty} \sum_{k=1}^{n} m^* E_k = \sum_{n=1}^{\infty} m^* E_n.

   式 :eq:`ex-2-30-eq-1` 与式 :eq:`ex-2-30-eq-2` 结合即得

   .. math::

      m^* \left( \bigcup_{n=1}^{\infty} E_n \right) = \sum_{n=1}^{\infty} m^* E_n,

   这与题设已知的 :math:`m^* \left( \bigcup\limits_{n=1}^\infty E_n \right) < \sum\limits_{n=1}^\infty m^* E_n` 矛盾.
   所以存在 (最小的) 自然数 :math:`N \geqslant 2` 使得

   .. math::

      m^* \left( \bigcup\limits_{n=1}^N E_n \right) < \sum\limits_{n=1}^N m^* E_n.

   假设 :math:`E_N` 是可测的, 那么由 Carathéodory 定理, 取 :math:`\displaystyle A_N = \bigcup_{k=1}^{N} E_k` 为测试集,
   再注意到 :math:`E_1, \dots, E_N` 互不相交, 有

   .. math::

      \sum_{n=1}^{N} m^* E_n > m^* A_N & = m^* \left( A_N \cap E_N \right) + m^* \left( A_N \cap \mathscr{C} E_N \right) \\
      & = m^* E_N + m^* A_{N-1}.

   上式两边同时消去 :math:`m^* E_{N}`, 有

   .. math::

      m^* \left( \bigcup\limits_{n=1}^{N-1} E_n \right) = m^* A_{N-1} < \sum\limits_{n=1}^{N-1} m^* E_n,

   这与 :math:`N` 的最小性矛盾. 所以 :math:`E_N` 是不可测的.

.. _ex-2-32:

32. 设 :math:`T` 是 :math:`\mathbb{R}^n` 上的非奇异线性变换, 证明对任一 :math:`E \subset \mathbb{R}^n` 有

    .. math::

      m^* (T(E)) = \lvert \det T \rvert m^* E.

.. proof:proof::

   由于非奇异线性变换都可以表示为以下三类变换的复合:

   1. 某两个分量的交换: :math:`T(x_1, \dots, x_i, \dots, x_j, \dots, x_n) = (x_1, \dots, x_j, \dots, x_i, \dots, x_n)`;

   2. 某个分量的伸缩: :math:`T(x_1, \dots, x_i, \dots, x_n) = (x_1, \dots, c x_i, \dots, x_n)`, 其中 :math:`c \ne 0`;

   3. 某个分量乘以常数加到另一个分量上: :math:`T(x_1, \dots, x_i, \dots, x_j, \dots, x_n) = (x_1, \dots, x_i + c x_j, \dots, x_j, \dots, x_n)`.

   而又有 :math:`\det T_k \circ \cdots \circ T_1 = \det T_k \cdots \det T_1`, 所以只要证明对于上述三种变换, 结论成立即可.

   :math:`\mathbb{R}^n` 中点集外测度的定义为该点集的 :math:`L`-覆盖的体积和的下确界, :math:`L`-覆盖由可数多个半开闭矩体构成,
   因此只要对半开闭矩体的变换证明结论成立即可. 任取一个半开闭矩体 :math:`I = [a_1, b_1) \times \cdots \times [a_n, b_n)`,
   :math:`m I = (b_1 - a_1) \cdots (b_n - a_n)`.

   对于第一类变换, :math:`T(I) = [a_1, b_1) \times \cdots \times [a_j, b_j) \times \cdots \times [a_i, b_i) \times \cdots \times [a_n, b_n)`,
   :math:`\det T = -1`, 有

   .. math::

      m T(I) = (b_1 - a_1) \cdots (b_j - a_j) \cdots (b_i - a_i) \cdots (b_n - a_n) = m I = \lvert \det T \rvert m I.

   对于第二类变换, 若 :math:`c > 0`, 则 :math:`T(I) = [a_1, b_1) \times \cdots \times [c a_i, c b_i) \times \cdots \times [a_n, b_n)`,
   :math:`\det T = c`, 若 :math:`c < 0`, 则 :math:`T(I) = [c b_1, c a_1) \times \cdots \times (c b_i, c a_i] \times \cdots \times [c b_n, c a_n)`,
   :math:`\det T = c`. 那么有

   .. math::

      m T(I) & = (b_1 - a_1) \cdots \lvert c b_i - c a_i \rvert \cdots (b_n - a_n) = c (b_1 - a_1) \cdots (b_i - a_i) \cdots (b_n - a_n) \\
      & = \lvert c \rvert m I = \lvert \det T \rvert m I.

   对于第三类变换,
   :math:`T(I) = [a_1, b_1) \times \cdots \times [a_i + c (b_j - a_j), b_i + c (b_j - a_j)) \times \cdots \times [a_j, b_j) \times \cdots \times [a_n, b_n)`,
   :math:`\det T = 1`,

   .. math::

      m T(I) & = (b_1 - a_1) \cdots (b_i + c (b_j - a_j) - a_i - c (b_j - a_j)) \cdots (b_j - a_j) \cdots (b_n - a_n) \\
      & = (b_1 - a_1) \cdots (b_i - a_i) \cdots (b_j - a_j) \cdots (b_n - a_n) \\
      & = m I = \lvert \det T \rvert m I.

   综上所述, 对于任意的半开闭矩体 :math:`I`, 有 :math:`m T(I) = \lvert \det T \rvert m I`, 从而有 :math:`m^* (T(E)) = \lvert \det T \rvert m^* E`.

.. _ex-2-33:

33. 设 :math:`E` 为 :math:`\mathbb{R}^n` 中任一子集, :math:`\alpha` 为给定正数. 对任意的 :math:`\varepsilon > 0`, 令

    .. math::

      H_{\alpha, \varepsilon} (E) = \inf \sum_k d (E_k)^{\alpha},

    其中 :math:`d (E_k)` 表示 :math:`E_k` 的直径, 下确界对一切满足 :math:`E \subset \bigcup\limits_{k} E_k`
    而 :math:`d (E_k) < \varepsilon, k \in \mathbb{N}` 的集列 :math:`\{E_k\}` 而取. 再令

    .. math::

      H_{\alpha} (E) = \lim\limits_{\varepsilon \to 0} H_{\alpha, \varepsilon} (E) = \sup\limits_{\varepsilon > 0} H_{\alpha, \varepsilon} (E).

    试证 :math:`H_{\alpha}` 为基本集 :math:`\mathbb{R}^n` 上的外测度并满足条件: 若 :math:`H_{\alpha} (E) < \infty`,
    则当 :math:`\beta > \alpha` 时, :math:`H_{\beta} (E) = 0`.

    :math:`H_{\alpha}` 称为 :math:`E` 的带指标 :math:`\alpha` 的豪斯多夫 (Hausdorff) 测度.

.. proof:proof::

   :math:`1^{\circ}`. :math:`H_{\alpha}` 的非负性: 由于集合的直径是非负的, 而 :math:`\lim, \sup, \inf` 都具有保号性,
   所以 :math:`H_{\alpha} (E) \geqslant 0` 对于任意的 :math:`E \subset \mathbb{R}^n` 成立. 对于 :math:`E = \emptyset`,
   以及任意给定的 :math:`\varepsilon > 0`, 对任意 :math:`n \in \mathbb{N}`, 可以取到 :math:`E_n \in \mathbb{R}^n`,
   使得其直径 :math:`d (E_n) < \varepsilon / n`, 例如直径为 :math:`\varepsilon / 2n` 的闭球. 那么有 :math:`E \subset E_n`, 以及

   .. math::

      H_{\alpha, \varepsilon} (E) \leqslant \inf_{n \in \mathbb{N}} d (E_n)^{\alpha} \leqslant \inf_{n \in \mathbb{N}} \left( \frac{\varepsilon}{n} \right)^{\alpha} = 0,

   从而有 :math:`H_{\alpha} (\emptyset) = 0`.

   :math:`2^{\circ}`. :math:`H_{\alpha}` 的次可加性: 设 :math:`\{A_n\}_{n \in \mathbb{N}}` 为 :math:`\mathbb{R}^n` 中的集列,
   记 :math:`\displaystyle A = \bigcup_{n=1}^{\infty} A_n`, 那么依定义

   .. math::

      H_{\alpha}\left( A \right) = \sup_{\varepsilon > 0} \inf \sum_{k = 1}^{\infty} d (E_{k})^{\alpha},

   其中下确界对一切满足 :math:`A \subset \bigcup\limits_{k = 1}^{\infty} E_{k}` 且 :math:`d (E_{k}) < \varepsilon, k \in \mathbb{N}`
   的集列 :math:`\{E_{k}\}_{k \in \mathbb{N}}` 而取. 对于每一个 :math:`A_n`, 以及给定的 :math:`\varepsilon > 0`,
   假设 :math:`\{E^{(n)}_k\}_{k \in \mathbb{N}}` 为满足 :math:`A_n \subset \bigcup\limits_{k = 1}^{\infty} E^{(n)}_k`
   且 :math:`d (E^{(n)}_k) < \varepsilon, k \in \mathbb{N}` 的集列, 那么集列 :math:`\{E^{(n)}_k\}_{n, k \in \mathbb{N}}` 覆盖 :math:`A`,
   且每一个 :math:`E^{(n)}_k` 的直径都小于 :math:`\varepsilon`. 但是覆盖集合 :math:`A` 的满足其中每个元素的直径都小于 :math:`\varepsilon` 的集列
   并不一定具有以上的 :math:`\{E^{(n)}_k\}_{n, k \in \mathbb{N}}` 的形式, 即集合

   .. math::

      \left\{ \{E^{(n)}_k\}_{n, k \in \mathbb{N}} \ :\ A \subset
      \bigcup_{n=1}^{\infty} \bigcup_{k=1}^{\infty} E^{(n)}_k, d (E^{(n)}_k) < \varepsilon, n, k \in \mathbb{N} \right\}

   是集合

   .. math::

      \left\{ \{E_k\}_{k \in \mathbb{N}} \ :\ A \subset \bigcup_{k=1}^{\infty} E_k, d (E_k) < \varepsilon, k \in \mathbb{N} \right\}

   的子集. 所以有

   .. math::

      H_{\alpha, \varepsilon} (A) \leqslant \inf \sum_{n = 1}^{\infty} \sum_{k = 1}^{\infty} d (E^{(n)}_k)^{\alpha}.

   对于不同的 :math:`n`, 即不同的 :math:`A_n`, 覆盖的选取是独立无关的, 所以实际上有

   .. math::

      \inf \sum_{n = 1}^{\infty} \sum_{k = 1}^{\infty} d (E^{(n)}_k)^{\alpha}
      = \sum_{n = 1}^{\infty} \inf \sum_{k = 1}^{\infty} d (E^{(n)}_k)^{\alpha} = \sum_{n = 1}^{\infty} H_{\alpha, \varepsilon} (A_n),

   即有 :math:`H_{\alpha, \varepsilon} (A) \leqslant \sum\limits_{n = 1}^{\infty} H_{\alpha, \varepsilon} (A_n)`, 进而有

   .. math::

      H_{\alpha} (A) = \sup_{\varepsilon > 0} H_{\alpha, \varepsilon} (A)
      \leqslant \sup_{\varepsilon > 0} \sum_{n = 1}^{\infty} H_{\alpha, \varepsilon} (A_n)
      \leqslant \sum_{n = 1}^{\infty} \sup_{\varepsilon > 0} H_{\alpha, \varepsilon} (A_n)
      = \sum_{n = 1}^{\infty} H_{\alpha} (A_n).

   :math:`3^{\circ}`. :math:`H_{\alpha}` 的单调性: 设 :math:`A \subset B`, 那么任何一个由直径不超过 :math:`\varepsilon` 的集合构成的覆盖 :math:`B` 的集列
   同时也是覆盖 :math:`A` 的集列, 但反过来不一定成立. 所以有

   .. math::

      H_{\alpha, \varepsilon} (A) \leqslant H_{\alpha, \varepsilon} (B).

   对 :math:`\varepsilon > 0` 取上确界, 有

   .. math::

      H_{\alpha} (A) = \sup_{\varepsilon > 0} H_{\alpha, \varepsilon} (A) \leqslant \sup_{\varepsilon > 0} H_{\alpha, \varepsilon} (B) = H_{\alpha} (B).

   设集列 :math:`\{E_k\}_{k \in \mathbb{N}}` 满足 :math:`d (E_k) < \varepsilon, \forall ~ k \in \mathbb{N}`. 对于 :math:`\beta > \alpha`, 有

   .. math::

      \sum_{k} d (E_k)^{\beta} = \sum_{k} d (E_k)^{\alpha} \cdot d (E_k)^{\beta - \alpha} \leqslant \varepsilon^{\beta - \alpha} \sum_{k} d (E_k)^{\alpha}.

   于是有

   .. math::

      H_{\beta, \varepsilon} (E) = \inf \sum_{k} d (E_k)^{\beta}
      \leqslant \varepsilon^{\beta - \alpha} \inf \sum_{k} d (E_k)^{\alpha}
      = \varepsilon^{\beta - \alpha} H_{\alpha, \varepsilon} (E).

   由于 :math:`\lim\limits_{\varepsilon \to 0} \varepsilon^{\beta - \alpha} = 0`,
   :math:`\lim\limits_{\varepsilon \to 0} H_{\alpha, \varepsilon} (E) = H_{\alpha} (E)` 为有限值,
   所以上式右边的极限为 :math:`0`. 对上式两边同时令 :math:`\varepsilon \to 0`, 有

   .. math::

      H_{\beta} (E) = \lim_{\varepsilon \to 0} H_{\beta, \varepsilon} (E)
      \leqslant \lim_{\varepsilon \to 0} \varepsilon^{\beta - \alpha} H_{\alpha, \varepsilon} (E) = 0.

.. _ex-2-34:

34. 设 :math:`r` 为给定的正数, :math:`a, b` 为正的常数. :math:`\mathbb{R}^n` 中子集列 :math:`V_1, V_2, \dots` 满足条件:
    每个 :math:`V_k` 中含有半径 :math:`ar` 的一个球且其直径 :math:`d(V_k) \leqslant br`.
    试证任一球 :math:`B(z, r)` 与 :math:`\{\overline{V}_k\}` 中元素相交的个数小于或等于 :math:`(1+b)^n a^{-n}`.

.. proof:proof::

   这题假设这些 :math:`V_k` 是互不相交的.

   由于每个 :math:`V_k` 中直径 :math:`d(V_k) \leqslant br`, 所以若 :math:`B(z, r)` 与 :math:`\overline{V}_k` 相交,
   那么 :math:`B(z, r) \cup \overline{V}_k \subset B(z, (1+b)r)`. 设球 :math:`B(z, (1+b)r)` 中能容纳半径为 :math:`ar` 的球的个数为 :math:`N`,
   令 :math:`c = \dfrac{\pi^{n/2}}{\Gamma (n/2 + 1)}`, 那么有

   .. math::

      N \cdot c (ar)^n \leqslant c ((1+b)r)^n,

   从而有 :math:`N \leqslant (1+b)^n a^{-n}`.

.. _ex-2-35:

35. 设 :math:`f` 为集 :math:`X \to Y` 的任一映射, :math:`\mathscr{A}, \mathscr{B}` 分别为 :math:`X, Y` 中的 :math:`\sigma` 代数, 证明

    .. math::

      \{ f^{-1} (B) : B \in \mathscr{B} \}, \quad \{B : f^{-1} (B) \in \mathscr{A} \}

    分别为 :math:`X, Y` 中的 :math:`\sigma` 代数.

.. proof:proof::

   (1). 首先证明 :math:`\{ f^{-1} (B) : B \in \mathscr{B} \}` 为 :math:`X` 中的 :math:`\sigma` 代数:

   :math:`1^{\circ}`. 由于 :math:`\mathscr{B}` 为 :math:`Y` 中的 :math:`\sigma` 代数, 那么 :math:`Y \in \mathscr{B}`.
   由于 :math:`f^{-1} (Y) = X`, 那么 :math:`X \in \{ f^{-1} (B) : B \in \mathscr{B} \}`.

   :math:`2^{\circ}`. 任取 :math:`A_1, A_2 \in \{ f^{-1} (B) : B \in \mathscr{B} \}`, 那么存在 :math:`B_1, B_2 \in \mathscr{B}`,
   使得 :math:`A_1 = f^{-1} (B_1), A_2 = f^{-1} (B_2)`. 那么有

   .. math::

      A_1 \setminus A_2 & = f^{-1} (B_1) \setminus f^{-1} (B_2) = f^{-1} (B_1) \cap \mathscr{C}_X f^{-1} (B_2) \\
      & = f^{-1} (B_1 \cap \mathscr{C}_Y B_2) = f^{-1} (B_1 \setminus B_2).

   由于 :math:`\mathscr{B}` 为 :math:`Y` 中的 :math:`\sigma` 代数, 那么 :math:`B_1 \setminus B_2 \in \mathscr{B}`,
   从而 :math:`A_1 \setminus A_2 \in \{ f^{-1} (B) : B \in \mathscr{B} \}`.

   :math:`3^{\circ}`. 任取 :math:`\{A_n\}_{n \in \mathbb{N}} \subset \{ f^{-1} (B) : B \in \mathscr{B} \}`,
   那么存在 :math:`\{B_n\}_{n \in \mathbb{N}} \subset \mathscr{B}`, 使得 :math:`A_n = f^{-1} (B_n), n \in \mathbb{N}`. 那么有

   .. math::

      \bigcup_{n=1}^{\infty} A_n = \bigcup_{n=1}^{\infty} f^{-1} (B_n) = f^{-1} \left( \bigcup_{n=1}^{\infty} B_n \right).

   由于 :math:`\mathscr{B}` 为 :math:`Y` 中的 :math:`\sigma` 代数, 那么 :math:`\bigcup\limits_{n=1}^{\infty} B_n \in \mathscr{B}`,
   从而 :math:`\bigcup\limits_{n=1}^{\infty} A_n \in \{ f^{-1} (B) : B \in \mathscr{B} \}`.

   综合 :math:`1^{\circ}, 2^{\circ}, 3^{\circ}`, 有 :math:`\{ f^{-1} (B) : B \in \mathscr{B} \}` 为 :math:`X` 中的 :math:`\sigma` 代数.

   (2). 再证明 :math:`\{B : f^{-1} (B) \in \mathscr{A} \}` 为 :math:`Y` 中的 :math:`\sigma` 代数:

   :math:`1^{\circ}`. 由于 :math:`\mathscr{A}` 为 :math:`X` 中的 :math:`\sigma` 代数, 那么 :math:`f^{-1} (Y) = X \in \mathscr{A}`,
   从而有 :math:`Y \in \{B : f^{-1} (B) \in \mathscr{A} \}`.

   :math:`2^{\circ}`. 任取 :math:`B_1, B_2 \in \{B : f^{-1} (B) \in \mathscr{A} \}`, 那么有 :math:`f^{-1} (B_1), f^{-1} (B_2) \in \mathscr{A}`.
   由于 :math:`\mathscr{A}` 为 :math:`X` 中的 :math:`\sigma` 代数, 那么

   .. math::

      \mathscr{A} \ni f^{-1} (B_1) \setminus f^{-1} (B_2) = f^{-1} (B_1 \setminus B_2).

   从而 :math:`B_1 \setminus B_2 \in \{B : f^{-1} (B) \in \mathscr{A} \}`.

   :math:`3^{\circ}`. 任取 :math:`\{B_n\}_{n \in \mathbb{N}} \subset \{B : f^{-1} (B) \in \mathscr{A} \}`,
   那么有 :math:`\{f^{-1} (B_n)\}_{n \in \mathbb{N}} \subset \mathscr{A}`. 由于 :math:`\mathscr{A}` 为 :math:`X` 中的 :math:`\sigma` 代数,
   那么有

   .. math::

      \mathscr{A} \ni \bigcup_{n=1}^{\infty} f^{-1} (B_n) = f^{-1} \left( \bigcup_{n=1}^{\infty} B_n \right).

   从而 :math:`\bigcup\limits_{n=1}^{\infty} B_n \in \{B : f^{-1} (B) \in \mathscr{A} \}`.

   综合 :math:`1^{\circ}, 2^{\circ}, 3^{\circ}`, 有 :math:`\{B : f^{-1} (B) \in \mathscr{A} \}` 为 :math:`Y` 中的 :math:`\sigma` 代数.

.. _ex-2-36:

36. 设 :math:`\mathscr{A}` 为由 :math:`\mathbb{R}` 中的一切这样的可测集 :math:`E` 构成:
    或者 :math:`m E = 0` 或者 :math:`m \mathscr{C} E = 0`. 试证 :math:`\mathscr{A}` 为 :math:`\mathbb{R}` 中的 :math:`\sigma` 代数.

.. proof:proof::

   :math:`1^{\circ}`. 由于 :math:`\emptyset = \mathscr{C} \mathbb{R}` 且 :math:`m \emptyset = 0`, 那么 :math:`\mathbb{R} \in \mathscr{A}`.

   :math:`2^{\circ}`. 任取 :math:`A_1, A_2 \in \mathscr{A}`, 那么有 :math:`m A_1 = 0` 或者 :math:`m \mathscr{C} A_1 = 0`;
   :math:`m A_2 = 0` 或者 :math:`m \mathscr{C} A_2 = 0`. 若 :math:`m A_1 = 0`, 那么

   .. math::

      m (A_1 \setminus A_2) \leqslant m A_1 = 0;

   若 :math:`m \mathscr{C} A_1 = 0`, 那么考虑到 :math:`\mathscr{C}(A_1 \setminus A_2) = \mathscr{C} A_1 \cup A_2`, 当 :math:`m A_2 = 0` 时有

   .. math::

      m (\mathscr{C}(A_1 \setminus A_2)) = m (\mathscr{C} A_1 \cup A_2) \leqslant m \mathscr{C} A_1 + m A_2 = 0;

   当 :math:`m \mathscr{C} A_2 = 0` 时有

   .. math::

      m (A_1 \setminus A_2) = m (A_1 \cap \mathscr{C} A_2) \leqslant m \mathscr{C} A_2 = 0.

   从而知 :math:`A_1 \setminus A_2 \in \mathscr{A}`.

   :math:`3^{\circ}`. 任取 :math:`\{A_n\}_{n \in \mathbb{N}} \subset \mathscr{A}`. 假设 :math:`m A_n = 0` 对所有 :math:`n \in \mathbb{N}` 成立,
   那么有

   .. math::

      m \left( \bigcup_{n=1}^{\infty} A_n \right) \leqslant \sum_{n=1}^{\infty} m A_n = 0.

   若存在 :math:`A_{n_0} \in \{A_n\}_{n \in \mathbb{N}}`, 使得 :math:`m \mathscr{C} A_{n_0} = 0`, 那么有

   .. math::

      m \left( \mathscr{C} \left( \bigcup_{n=1}^{\infty} A_n \right) \right)
      = m \left( \bigcap_{n=1}^{\infty} \mathscr{C} A_n \right) \leqslant m \mathscr{C} A_{n_0} = 0.

   即知 :math:`\bigcup\limits_{n=1}^{\infty} A_n \in \mathscr{A}`.

   综合 :math:`1^{\circ}, 2^{\circ}, 3^{\circ}`, 有 :math:`\mathscr{A}` 为 :math:`\mathbb{R}` 中的 :math:`\sigma` 代数.

.. _ex-2-37:

37. 设 :math:`\mathscr{S}` 为 :math:`X` 中任一非空子集族. 试证

    .. math::

      \sigma (f^{-1} (\mathscr{S})) = f^{-1} (\sigma (\mathscr{S})),

    其中 :math:`f` 为 :math:`Y \to X` 的映射, :math:`\sigma (\mathscr{S})` 为 :math:`\mathscr{S}` 生成的 :math:`\sigma` 代数.

.. proof:proof::

   由于 :math:`\mathscr{S} \subset \sigma (\mathscr{S})`, 那么有 :math:`f^{-1} (\mathscr{S}) \subset f^{-1} (\sigma (\mathscr{S}))`.
   由于 :math:`\sigma (f^{-1} (\mathscr{S}))` 为包含 :math:`f^{-1} (\mathscr{S})` 的最小的 :math:`\sigma` 代数,
   并且由 :ref:`本章第 35 题 <ex-2-35>` 知 :math:`f^{-1} (\sigma (\mathscr{S}))` 为 :math:`Y` 中的 :math:`\sigma` 代数,
   故 :math:`\sigma (f^{-1} (\mathscr{S})) \subset f^{-1} (\sigma (\mathscr{S}))`.

   另一方面, 我们需要注意到这样一个事实:

      对于任意一个 :math:`A \in f^{-1} (\sigma (\mathscr{S}))`, 有 :math:`f^{-1}(f(A)) = A`.

   对于 :math:`A \in f^{-1} (\sigma (\mathscr{S}))`, 有 :math:`f(A) \in \sigma (\mathscr{S})`, 从而存在 :math:`E_1, E_2, \dots \in \mathscr{S}`,
   使得

   .. math::

      f(A) \subset \bigcup\limits_{n=1}^{\infty} E_n \subset \bigcup\limits_{n=1}^{\infty} f(f^{-1} (E_n)).

   记 :math:`\widetilde{E}_n = f(f^{-1} (E_n)), E = \left( \bigcup\limits_{n=1}^{\infty} \widetilde{E}_n \right) \setminus f(A)`, 有

   .. math::

      f^{-1} (E) = f^{-1} \left( \left( \bigcup\limits_{n=1}^{\infty} \widetilde{E}_n \right) \setminus f(A) \right)
      = \left( \bigcup\limits_{n=1}^{\infty} f^{-1} (\widetilde{E}_n) \right) \setminus A
      = \left( \bigcup\limits_{n=1}^{\infty} f^{-1} (E_n) \right) \setminus A.

   由于 :math:`\bigcup\limits_{n=1}^{\infty} f^{-1} (E_n) \in \sigma (f^{-1} (\mathscr{S})) \subset f^{-1} (\sigma (\mathscr{S}))`,
   并且 :math:`A \in f^{-1} (\sigma (\mathscr{S}))`, 那么有 :math:`f^{-1} (E) \in f^{-1} (\sigma (\mathscr{S}))`,
   即 :math:`E \in \sigma (\mathscr{S})`.

   未完。。。。
