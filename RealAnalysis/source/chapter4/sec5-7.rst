§5-7 乘积测度与 Fubini 定理、微分与积分、RS 积分
------------------------------------------------------------------------

.. _ex-4-27:

27. 设 :math:`f(x), g(x)` 分别是定义在集 :math:`X, Y` 上的 :math:`\mu, \nu` 可积函数。证明

.. math::

    h(x, y) = f(x) g(y)

是乘积空间 :math:`X \times Y` 上的可积函数，且有

.. math::

    \int_{X \times Y} h \mathrm{d} (\mu \times \nu) = \int_X f \mathrm{d} \mu \int_Y g \mathrm{d} \nu.

.. proof:proof::

    首先，由于 :math:`f(x), g(x)` 分别是定义在集 :math:`X, Y` 上的 :math:`\mu, \nu` 可积函数，从而可测，
    所以 :math:`h(x, y) = f(x) g(y)` 是乘积空间 :math:`X \times Y` 上的可测函数。

    接下来，需要证明 :math:`\int_{X \times Y} h \mathrm{d} (\mu \times \nu) < \infty`.
    这等价于 :math:`\int_{X \times Y} \lvert h \rvert \mathrm{d} (\mu \times \nu) < \infty`.
    由 :ref:`Tonelli 定理 <thm-tonelli>` 知

    .. math::

        \int_{X \times Y} \lvert h \rvert \mathrm{d} (\mu \times \nu) & = \int_X \left( \int_Y \lvert h(x, y) \rvert \mathrm{d} \nu \right) \mathrm{d} \mu = \int_X \left( \int_Y \lvert f(x) g(y) \rvert \mathrm{d} \nu \right) \mathrm{d} \mu \\
        & = \int_X \lvert f(x) \rvert \left( \int_Y \lvert g(y) \rvert \mathrm{d} \nu \right) \mathrm{d} \mu = \int_X \lvert f(x) \rvert \mathrm{d} \mu \int_Y \lvert g(y) \rvert \mathrm{d} \nu < \infty.

    于是 :math:`h(x, y) = f(x) g(y)` 是乘积空间 :math:`X \times Y` 上的可积函数。

    .. note::

        本题结论即为 Fubini-Tonelli 定理的一种特殊情形。

.. _ex-4-28:

28. 设 :math:`(X, \mathscr{R}, \mu), (Y, \mathscr{S}, \nu)` 为对应于勒贝格测度的单位区间这样的测度空间， :math:`E` 是 :math:`X \times Y` 中是和下述条件的集：
对每个 :math:`x` 与每个  :math:`y`, :math:`E_x` 与 :math:`X \setminus E^y` 均为可列集。证明 :math:`E` 是不可测的。

.. proof:proof::

    假设 :math:`E` 可测，那么

    .. math::

        1 = m ([0, 1] \times [0, 1]) \geqslant m (E) = \int_{X \times Y} \chi_E \mathrm{d} (\mu \times \nu),

    即 :math:`\chi_E` 是 :math:`E` 上的可积函数，从而由 Fubini 定理知

    .. math::

            \int_X \nu(E_x) \mathrm{d} \mu = \int_X \left( \int_Y \chi_{E_x} \mathrm{d} \nu \right) \mathrm{d} \mu = \int_{X \times Y} \chi_E \mathrm{d} (\mu \times \nu) = int_Y \left( \int_X \chi_{E^y} \mathrm{d} \mu \right) \mathrm{d} \nu = \int_Y \mu (E^y) \mathrm{d} \nu.

    由于对每个 :math:`x` 与每个  :math:`y`, :math:`E_x` 与 :math:`X \setminus E^y` 均为可列集，而可列集都是零测集，
    所以 :math:`\nu(E_x) = 0`, :math:`\mu(E^y) = m(X) = 1`, 从而有

    .. math::

        \int_X \nu(E_x) \mathrm{d} \mu & = \int_X 0 \mathrm{d} \mu = 0, \\
        \int_Y \mu(E^y) \mathrm{d} \nu & = \int_Y 1 \mathrm{d} \nu = 1,

    这与上式矛盾，所以 :math:`E` 不可测。

.. _ex-4-30:

30. 设 :math:`\theta(x)` 为区间 :math:`[0, 1]` 上的 Cantor 函数，令 :math:`f(x) = \theta(x) + x`, :math:`0 \leqslant x \leqslant 1`;
:math:`g = f^{-1}`. 试证：

(1). 存在可测集 :math:`B` 使 :math:`g^{-1}(B)` 不可测；

(2). :math:`g^{-1}` 映不可测集为不可测集。

.. proof:proof::

    有如下的互逆的连续一一映射

    .. math::

        [0, 1] \overset{f}{\underset{g}\rightleftarrows} [0, 2]

    (1). 任取 :math:`[0, 1]` 上 Cantor 三分集 :math:`P_0` 的补集 :math:`G_0` 的构成区间 :math:`I = (a, b)`,
    Cantor 函数 :math:`\theta` 在 :math:`I` 上为常值函数，因此 :math:`f(I) = (a + \theta(a), b + \theta(b))`.
    于是有 :math:`m (f(I)) = b - a = m I`, 且 :math:`f(G_0)` 为构成区间为 :math:`f(I)` 的开集，从而可测。
    依据测度的可列可加性，有

    .. math::

        m (f(G_0)) = \sum_{n = 1}^\infty m (f(I_n)) = \sum_{n = 1}^\infty m (I_n) = m (G_0) = 1

    成立，从而知

    .. math::

        m (f (P_0)) = m ([0, 2]) - m (f (G_0)) = 2 - 1 = 1.

    于是可以从正测度集 :math:`f (P_0)` 中取出不可测集 :math:`B_0`, 并令 :math:`B = g (B_0) = f^{-1} (B_0) \subset P_0`.
    由于 :math:`P_0` 是零测集，所以它的子集 :math:`B` 也是零测集，从而是可测集。而 :math:`g^{-1} (B) = B_0` 不可测。

    (2). 任取 :math:`[0, 1]` 区间内的不可测集 :math:`E`, 假设 :math:`g^{-1} (E) = f (E)` 可测。未写完。。。。

.. _ex-4-34:

34. 设 :math:`\{ f_n \}` 为 :math:`[a, b]` 上有界变差函数列， :math:`f_n` 收敛于一有限函数 :math:`f` (当 :math:`n \to \infty`),
且有 :math:`\displaystyle \bigvee_a^b (f_n) \leqslant K`, :math:`K` 为常数 (:math:`n \in \mathbb{N}`)。证明 :math:`f` 也是有界变差函数。

.. proof:proof::

    待写。

.. _ex-4-35:

35. 若函数 :math:`f` 在 :math:`[a, b]` 上绝对连续，且几乎处处存在非负导数，证明 :math:`f` 为增函数。

.. proof:proof::

    由于函数 :math:`f` 在 :math:`[a, b]` 上绝对连续，所以存在 :math:`[a, b]` 上可积函数 :math:`g` 使得

    .. math::

        f(x) = f(a) + \int_{[a, x]} g \mathrm{d} m, \quad x \in [a, b],

    并且 :math:`f'(x) = g(x)` 几乎处处成立。由于函数 :math:`f` 在 :math:`[a, b]` 上几乎处处存在非负导数，即 :math:`g(x)` 几乎处处非负，
    所以对任意 :math:`x_1 < x_2 \in [a, b]`, 有 :math:`\displaystyle \int_{[x_1, x_2]} g \mathrm{d} m \geqslant 0`, 从而知

    .. math::

        f(x_2) - f(x_1) = \int_{[x_1, x_2]} g \mathrm{d} m \geqslant 0,

    这就证明了 :math:`f` 是增函数。

.. _ex-4-38:

38. 证明 Vitali 引理对有有限测度的无界集成立。

.. proof:proof::

    设 :math:`E \subset \mathbb{R}` 为有有限测度的无界集， :math:`m (E) < \infty`,
    :math:`\mathscr{M}` 为 :math:`E` 的一个由有正测度的闭区间构成的 Vitali 覆盖。
    要证明 :math:`\forall \varepsilon > 0`, 存在有限个互不相交的区间 :math:`d_1, d_2, \cdots, d_n \in \mathscr{M}`,
    使得 :math:`m (E \setminus \bigcup_{i = 1}^n d_i) < \varepsilon`.

    取开集 :math:`G` 使得 :math:`E \subset G`, 且 :math:`m G < \infty`. 可以不妨设 :math:`\mathscr{M}` 中的区间都包含于 :math:`G` 中。
    这是因为 :math:`\forall x \in E \subset G`, :math:`x` 必然属于开集 :math:`G` 的某个构成区间 :math:`(a, b)`,
    而 :math:`\mathscr{M}` 为 :math:`E` 的 Vitali 覆盖，对于所有的 :math:`x \in E`, 都存在闭区间列 :math:`\{ d_k \} \subset \mathscr{M}`,
    使得 :math:`x \in d_k`, 且 :math:`\displaystyle \lim_{k \to \infty} m (d_k) = 0`. 于是从某一项开始， :math:`d_k \subset (a, b) \subset G`.
    令 :math:`\mathscr{M}'` 为 :math:`\mathscr{M}` 中所有包含于 :math:`G` 的闭区间构成的子族，那么 :math:`\mathscr{M}'` 也是 :math:`E` 的 Vitali 覆盖。
    对 :math:`\mathscr{M}'` 证明题设结论，则该结论对 :math:`\mathscr{M}` 也成立。

    从 :math:`\mathscr{M}` 中任选一个区间 :math:`d_1`, 由数学归纳法依照如下步骤选取区间 :math:`d_2, d_3, \cdots, d_n`:
    假设已经选取了 :math:`d_1, d_2, \cdots, d_k`, 若 :math:`\displaystyle E \subset \bigcup_{i = 1}^k d_i`, 则停止选取; 否则令

    .. math::
        :label: ex-4-38-1

        \mathscr{S}_k = \{ d \in \mathscr{M} ~:~ d \cap \bigcup_{i = 1}^k d_i = \emptyset \},

    那么 :math:`\mathscr{S}_k` 非空，这是由于任取 :math:`x \in E \setminus \bigcup_{i = 1}^k d_i \neq \emptyset`,
    因为 :math:`\mathscr{M}` 为 :math:`E` 的 Vitali 覆盖，所以存在足够小的闭区间 :math:`d \in \mathscr{M}`,
    使得 :math:`x \in d`, 且 :math:`\displaystyle d \cap \bigcup_{i = 1}^k d_i = \emptyset`. 令

    .. math::
        :label: ex-4-38-2

        \delta_k = \sup \{ m (d) ~:~ d \in \mathscr{S}_k \},

    那么 :math:`0 < \delta_k \leqslant m (G) < \infty`. 由上确界的定义，可以从 :math:`\mathscr{S}_k` 中选取一个闭区间 :math:`d_{k + 1}`, 使得

    .. math::
        :label: ex-4-38-3

        m (d_{k + 1}) > \dfrac{\delta_k}{2}, \quad d_{k + 1} \cap \bigcup_{i = 1}^k d_i = \emptyset.

    由此可得到互不相交的区间序列 :math:`\{ d_k \}`. 由于每一个 :math:`d_k` 都包含于 :math:`G` 中，由测度的可列可加性以及单调性，有

    .. math::
        :label: ex-4-38-4

        \sum_{k = 1}^\infty m (d_k) = m \left( \bigcup_{k = 1}^\infty d_k \right) \leqslant m (G) < \infty.

    于是由级数的 Cauchy 收敛准则知 :math:`\forall \varepsilon > 0`, 存在正整数 :math:`n`, 使得

    .. math::
        :label: ex-4-38-5

        \sum_{k = n + 1}^\infty m (d_k) < \dfrac{\varepsilon}{5}.

    令 :math:`\displaystyle B = E \setminus \bigcup_{k = 1}^n d_k`, 下证 :math:`m B < \varepsilon`. 任取 :math:`x \in B`,
    由于 :math:`\displaystyle \bigcup_{k = 1}^n d_k \not\ni x` 为闭集，所以存在 :math:`\delta > 0`,
    使得 :math:`\displaystyle (x - \delta, x + \delta) \cap \bigcup_{k = 1}^n d_k = \emptyset`.
    又由于 :math:`\mathscr{M}` 为 :math:`E` 的 Vitali 覆盖，所以存在闭区间 :math:`d(x) \in \mathscr{M}`,
    使得 :math:`x \in d(x) \subset (x - \delta, x + \delta)`. 那么有 :math:`\displaystyle d(x) \cap \bigcup_{k = 1}^n d_k = \emptyset`,
    即 :math:`d(x) \in \mathscr{S}_n`, 从而有

    .. math::
        :label: ex-4-38-6

        m (d(x)) \leqslant \delta_n < 2 m (d_{n + 1}).

    可以断言必然存在 :math:`n_0 (x) > n`, 使得 :math:`d(x) \not \in \mathscr{S}_{n_0 (x)}`, 否则对任意 :math:`k > n`,
    都有 :math:`\mathbb{N} \ni d(x) \in \mathscr{S}_k`, 即有

    .. math::
        :label: ex-4-38-7

        m (d_{k + 1}) > \dfrac{\delta_k}{2} = \dfrac{1}{2} \sup \{ m (d) ~:~ d \in \mathscr{S}_k \} \geqslant \dfrac{1}{2} m (d(x)),

    这与级数 :eq:`ex-4-38-4` 的收敛性矛盾。那么由于 :math:`d(x) \not \in \mathscr{S}_{n_0 (x)}`, 所以存在 :math:`n_1(x) \in \mathbb{N}`,
    使得 :math:`n < n_1(x) \leqslant n_0 (x)`, 且有 :math:`d(x) \cap d_{n_1(x)} \neq \emptyset`, 以及

    .. math::
        :label: ex-4-38-8

        d(x) \cap d_{k} = \emptyset, k = 1, 2, \cdots, n_1(x) - 1.

    由上式 :eq:`ex-4-38-7`, 以及 :math:`\mathscr{S}_k` 的定义式 :eq:`ex-4-38-1`, :math:`\delta_k` 的定义式 :eq:`ex-4-38-2`,
    :math:`d_{k + 1}` 的取法 :eq:`ex-4-38-3`, 有

    .. math::
        :label: ex-4-38-9

        m (d(x)) \leqslant \delta_{n_1(x) - 1} < 2 m (d_{n_1(x)}).

    由于 :math:`d(x) \cap d_{n_1(x)} \neq \emptyset`, 所以将闭区间 :math:`d_{n_1(x)}` 分别往左右两边延伸 :math:`2 m (d_{n_1(x)})`,
    便得到一个闭区间 :math:`d_{n_1(x)}'`, 使得 :math:`x \in d(x) \subset d_{n_1(x)}'`, 且有区间长度关系

    .. math::
        :label: ex-4-38-10

        m (d_{n_1(x)}') = 5 m (d_{n_1(x)}).

    结合式 :eq:`ex-4-38-5`, 有

    .. math::
        :label: ex-4-38-11

        m B \leqslant m \left( \bigcup_{x \in B} d_{n_1(x)}' \right) \leqslant m \left( \bigcup_{k = n + 1}^\infty d_k' \right) \leqslant \sum_{k = n + 1}^\infty m (d_k') = 5 \sum_{k = n + 1}^\infty m (d_k) < \varepsilon.

    上式 :eq:`ex-4-38-11` 中 :math:`d_k'` 指的是依照类似于 :eq:`ex-4-38-10` 的方法将闭区间 :math:`d_k` 分别往左右两边延伸 :math:`2 m (d_k)`,
    得到的长度为 :math:`5 m (d_k)` 的闭区间；第一个不等式成立是由集合的包含关系 :math:`\displaystyle B \subset \bigcup_{x \in B} d_{n_1(x)}'`;
    第二个不等式成立是因为集合 :math:`\{ n_1(x) ~:~ x \in B \}` 显然是集合 :math:`\{ k \in \mathbb{N} ~:~ k = n + 1, n + 2, \cdots \}` 的子集。
