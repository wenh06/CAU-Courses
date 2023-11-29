§1 勒贝格积分的引入
------------------------------------------

2. 设 :math:`f` 于 :math:`E` 上可积，令 :math:`E_n = E( \lvert f \rvert \ge n)`, 证明 :math:`\displaystyle \lim_n m E_n = 0`.

.. proof:proof::

    :math:`f` 于 :math:`E` 上可积，那么 :math:`\lvert f \rvert` 于 :math:`E` 上可积，即 :math:`\displaystyle \int_E \lvert f \rvert \mathrm{d} m < \infty`.
    由于 :math:`\{ m E_n \}_{n \in \mathbb{N}}` 是单调不增的，且 :math:`m E_n \ge 0`, 所以 :math:`\displaystyle \lim_n m E_n` 极限存在，设为 :math:`\alpha`.
    假设 :math:`\alpha > 0`, 那么存在 :math:`N \in \mathbb{N}`, 使得当 :math:`n \ge N` 时，有 :math:`m E_n \ge \dfrac{\alpha}{2}`, 于是

    .. math::

        \int_E \lvert f \rvert \mathrm{d} m \ge \int_{E_n} \lvert f \rvert \mathrm{d} m \ge n \cdot m E_n \ge \frac{n \alpha}{2}

    对任意 :math:`n \ge N` 成立，这与 :math:`\displaystyle \int_E \lvert f \rvert \mathrm{d} m < \infty` 矛盾，所以 :math:`\alpha = 0`.

3. 设函数 :math:`f` 在 Cantor 三分集 :math:`P_0` 上定义为零，而在 :math:`P_0` 的补集中长为 :math:`\dfrac{1}{3^n}` 的构成区间上定义为 :math:`n`, :math:`n \in \mathbb{N}`
试证 :math:`f \in L`, 并求积分值。

.. proof:proof::

    :math:`P_0` 在 :math:`E = [0, 1]` 中的补集 :math:`G_0` 的长为 :math:`\dfrac{1}{3^n}` 的构成区间共有 :math:`2^{n - 1}` 个，
    记为 :math:`I_{n, k}, k = 1, 2, \dots, 2^{n - 1}`. 于是

    .. math::

        f = \sum_{n = 1}^\infty \sum_{k = 1}^{2^{n - 1}} n \cdot \chi_{I_{n, k}}.

    :math:`f` 以及 :math:`\chi_{I_{n, k}}` 都是非负可测函数，所以由逐项积分定理可得

    .. math::

        \int_E f \mathrm{d} m = \sum_{n = 1}^\infty \sum_{k = 1}^{2^{n - 1}} n \cdot m I_{n, k} = \sum_{n = 1}^\infty \dfrac{n \cdot 2^{n - 1}}{3^n} = \dfrac{1}{2} \sum_{n = 1}^\infty n \cdot \left( \dfrac{2}{3} \right)^n.

    以上级数是收敛的，所以 :math:`f \in L_E`. 记 :math:`I = \displaystyle \int_E f \mathrm{d} m, a = \dfrac{2}{3}`, 那么

    .. math::

        I - a I = \dfrac{1}{2} \sum_{n = 1}^\infty a^n = \dfrac{a}{2(1 - a)},

    因此 :math:`I = \dfrac{a}{2(1 - a)^2} = 3`.

5. 设由 :math:`[0, 1]` 中取 :math:`n` 个可测子集 :math:`E_1, E_2, \dots, E_n`. 假定 :math:`[0, 1]` 中任一点至少属于这 :math:`n` 个集合中的 :math:`p` 个，
试证这 :math:`n` 个自己中必有一集，它的测度不小于 :math:`\dfrac{p}{n}`.

.. proof:proof::

    由于 :math:`[0, 1]` 中任一点至少属于 :math:`E_1, E_2, \dots, E_n` 的 :math:`p` 个，所以

    .. math::

        \sum_{k = 1}^n \chi_{E_k} (x) \ge p, \quad \forall x \in [0, 1],

    于是有

    .. math::

        \sum_{k = 1}^n m E_k = \sum_{k = 1}^n \int_{[0, 1]} \chi_{E_k} (x) \mathrm{d} m = \int_{[0, 1]} \sum_{k = 1}^n \chi_{E_k} (x) \mathrm{d} m \ge \int_{[0, 1]} p \mathrm{d} m = p.

    所以上式左端的和至少有一项不小于 :math:`\dfrac{p}{n}`, 也即对应的集合的测度不小于 :math:`\dfrac{p}{n}`.

6. 设 :math:`m E > 0`, 又设 :math:`E` 上可积函数 :math:`f, g` 满足 :math:`f < g`, 试证

.. math::

    \int_E f \mathrm{d} m < \int_E g \mathrm{d} m.

.. proof:proof::

    由于可积函数 :math:`f, g` 满足 :math:`f < g`, 所以 :math:`\lvert g - f \rvert = g - f`. 假设 :math:`\displaystyle \int_E f \mathrm{d} m = \int_E g \mathrm{d} m`,
    那么 :math:`\displaystyle \int_E \lvert g - f \rvert \mathrm{d} m = 0`, 由唯一性定理可知 :math:`g - f \sim 0`, 也即 :math:`g(x) = f(x)` a.e. :math:`x \in E`. 这意味着

    .. math::

        0 = m E (g \neq f) = m E,

    这与 :math:`m E > 0` 矛盾，所以 :math:`\displaystyle \int_E f \mathrm{d} m < \int_E g \mathrm{d} m`.

7. 设 :math:`f` 为 :math:`E` 上可积函数，如果对任何有界可测函数 :math:`\varphi`, 都有

.. math::

    \int_E f \varphi \mathrm{d} m = 0,

证明 :math:`f \sim 0`.

.. proof:proof::

    :math:`\forall n \in \mathbb{N}`, 令 :math:`E_n = E( \lvert f \rvert \ge n)`, 那么 :math:`\displaystyle \lim_{n \to \infty} m E_n = 0`. 令

    .. math::

        \varphi_n (x) = \begin{cases}
            f(x), & x \in E \setminus E_n, \\
            0, & x \in E_n,
        \end{cases}

    那么 :math:`\varphi_n` 是 :math:`E` 上有界可测函数 (:math:`\lvert \varphi_n \rvert \le n`), 且依题意有

    .. math::

        0 = \int_E f \varphi_n \mathrm{d} m = \int_{E \setminus E_n} f^2 \mathrm{d} m.

    那么有 :math:`f(x) = 0` a.e. :math:`x \in E \setminus E_n`, 进而有

    .. math::

        f(x) = 0, \quad a.e. ~ x \in \bigcup_{n = 1}^\infty (E \setminus E_n) = E \setminus \bigcap_{n = 1}^\infty E_n.

    由于 :math:`\displaystyle \lim_{n \to \infty} m E_n = 0`, 所以 :math:`\displaystyle m \left( \bigcap_{n = 1}^\infty E_n \right) = 0`,
    那么 :math:`f(x) = 0` a.e. :math:`x \in E`.
