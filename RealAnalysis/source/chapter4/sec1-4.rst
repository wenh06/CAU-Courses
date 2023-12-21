§1-4 勒贝格积分的引入、性质、积分序列的极限、与黎曼积分的关系
-------------------------------------------------------------------------------------

.. _ex-4-2:

2. 设 :math:`f` 于 :math:`E` 上可积，令 :math:`E_n = E( \lvert f \rvert \geqslant n)`, 证明 :math:`\displaystyle \lim_n m E_n = 0`.

.. proof:proof::

    :math:`f` 于 :math:`E` 上可积，那么 :math:`\lvert f \rvert` 于 :math:`E` 上可积，即 :math:`\displaystyle \int_E \lvert f \rvert \mathrm{d} m < \infty`.
    由于 :math:`\{E_n\}_{n \in \mathbb{N}}` 是渐缩列，故数列 :math:`\{ m E_n \}_{n \in \mathbb{N}}` 是非负单调不增数列，
    所以 :math:`\displaystyle \lim_{n \to \infty} m E_n` 极限存在，设为 :math:`\alpha`. 假设 :math:`\alpha > 0`, 那么存在 :math:`N \in \mathbb{N}`,
    使得当 :math:`n \geqslant N` 时，有 :math:`m E_n \geqslant \dfrac{\alpha}{2}`, 于是

    .. math::

        \int_E \lvert f \rvert \mathrm{d} m \geqslant \int_{E_n} \lvert f \rvert \mathrm{d} m \geqslant n \cdot m E_n \geqslant \frac{n \alpha}{2}

    对任意 :math:`n \geqslant N` 成立，这与 :math:`\displaystyle \int_E \lvert f \rvert \mathrm{d} m < \infty` 矛盾，所以 :math:`\alpha = 0`.

.. _ex-4-3:

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

.. _ex-4-5:

5. 设由 :math:`[0, 1]` 中取 :math:`n` 个可测子集 :math:`E_1, E_2, \dots, E_n`. 假定 :math:`[0, 1]` 中任一点至少属于这 :math:`n` 个集合中的 :math:`p` 个，
试证这 :math:`n` 个自己中必有一集，它的测度不小于 :math:`\dfrac{p}{n}`.

.. proof:proof::

    由于 :math:`[0, 1]` 中任一点至少属于 :math:`E_1, E_2, \dots, E_n` 的 :math:`p` 个，所以

    .. math::

        \sum_{k = 1}^n \chi_{E_k} (x) \geqslant p, \quad \forall x \in [0, 1],

    于是有

    .. math::

        \sum_{k = 1}^n m E_k = \sum_{k = 1}^n \int_{[0, 1]} \chi_{E_k} (x) \mathrm{d} m = \int_{[0, 1]} \sum_{k = 1}^n \chi_{E_k} (x) \mathrm{d} m \geqslant \int_{[0, 1]} p \mathrm{d} m = p.

    所以上式左端的和至少有一项不小于 :math:`\dfrac{p}{n}`, 也即对应的集合的测度不小于 :math:`\dfrac{p}{n}`.

.. _ex-4-6:

6. 设 :math:`m E > 0`, 又设 :math:`E` 上可积函数 :math:`f, g` 满足 :math:`f < g`, 试证

.. math::

    \int_E f \mathrm{d} m < \int_E g \mathrm{d} m.

.. proof:proof::

    由于可积函数 :math:`f, g` 满足 :math:`f < g`, 所以 :math:`\lvert g - f \rvert = g - f`. 假设 :math:`\displaystyle \int_E f \mathrm{d} m = \int_E g \mathrm{d} m`, 那么

    .. math::

        \int_E \lvert g - f \rvert \mathrm{d} m = \int_E (g - f) \mathrm{d} m = \int_E g \mathrm{d} m - \int_E f \mathrm{d} m = 0.

    由唯一性定理可知 :math:`g - f \sim 0`, 也即 :math:`g(x) = f(x)` a.e. :math:`x \in E`. 这意味着

    .. math::

        0 = m E (g \neq f) = m E,

    这与 :math:`m E > 0` 矛盾，所以必有 :math:`\displaystyle \int_E f \mathrm{d} m < \int_E g \mathrm{d} m`.

.. _ex-4-7:

7. 设 :math:`f` 为 :math:`E` 上可积函数，如果对任何有界可测函数 :math:`\varphi`, 都有

.. math::

    \int_E f \varphi \mathrm{d} m = 0,

证明 :math:`f \sim 0`.

.. proof:proof::

    :math:`\forall n \in \mathbb{N}`, 令 :math:`E_n = E( \lvert f \rvert \geqslant n)`, 那么 :math:`\displaystyle \lim_{n \to \infty} m E_n = 0`. 令

    .. math::

        \varphi_n (x) = f(x) \cdot \chi_{E \setminus E_n} = \begin{cases}
            f(x), & x \in E \setminus E_n, \\
            0, & x \in E_n,
        \end{cases}

    那么 :math:`\varphi_n` 是 :math:`E` 上有界可测函数 (:math:`\lvert \varphi_n \rvert \leqslant n`), 且依题意有

    .. math::

        0 = \int_E f \varphi_n \mathrm{d} m = \int_{E \setminus E_n} f^2 \mathrm{d} m.

    那么有 :math:`f(x) = 0` a.e. :math:`x \in E \setminus E_n`, 进而有

    .. math::

        f(x) = 0, \quad a.e. ~ x \in \bigcup_{n = 1}^\infty (E \setminus E_n) = E \setminus \bigcap_{n = 1}^\infty E_n.

    由于 :math:`\displaystyle \lim_{n \to \infty} m E_n = 0`, 所以 :math:`\displaystyle m \left( \bigcap_{n = 1}^\infty E_n \right) = 0`,
    那么 :math:`f(x) = 0` a.e. :math:`x \in E`.

.. _ex-4-8:

8. Levi 定理中去掉函数列的非负性假定，结论是否成立？

.. proof:solution::

    一般不成立。例如当 :math:`f_n` 的正部与负部积分都是 :math:`\infty` 时， :math:`f_n` 的积分不存在。
    即使当 :math:`f_n` 的积分有定义时，Levi 定理也不一定成立，例如 :math:`E = [0, \infty)`, :math:`f_n(x) = - \chi_{[n, \infty)}`,
    则 :math:`f_n` 的积分为 :math:`- \infty`, 但是 :math:`f_n` 逐点收敛于 :math:`f = 0`, :math:`f` 的积分为 :math:`0`, 此时

    .. math::

        \int_E f \mathrm{d} m = 0 \neq - \infty = \lim_{n \to \infty} \int_E f_n \mathrm{d} m.

    如果加上 :math:`f_n` 的积分都有定义，且 :math:`\displaystyle \int_E f_1 \mathrm{d} m \geqslant - \infty` 这个条件，Levi 定理就成立了。

.. _ex-4-14:

14. 设 :math:`f` 是区间 :math:`[0, 1]` 上的可积函数，若对任何 :math:`c \in (0, 1)` 恒有

    .. math::

        \int_0^c f(x) \mathrm{d} m = 0,

证明 :math:`f \sim 0`.

.. proof:proof::

    对每个 :math:`n \in \mathbb{N}`, 取

    .. math::

        c_n & = 1 - \dfrac{1}{2n}, \\
        I_n & = (0, c_n) = \left(0, 1 - \dfrac{1}{2n}\right), \\
        E_n & = I_n(f \neq 0) = \{x \in I_n \ :\ f(x) \neq 0\},

    那么 :math:`E_1 \subset E_2 \subset \cdots \subset E_n \subset \cdots` 构成了一个渐张可测集列。另一方面，
    由 :math:`\displaystyle \int_0^{c_n} f(x) \mathrm{d} m = 0` 知 :math:`m E_n = 0`, 那么对于渐张可测集列 :math:`\{E_n\}_{n \in \mathbb{N}}` 有

    .. math::

        m \left(\bigcup_{n=1}^\infty E_n\right) = \lim_{n \to \infty} m E_n = 0.

    由于 :math:`\displaystyle \bigcup_{n=1}^\infty I_n = \bigcup_{n=1}^\infty \left(0, 1 - \dfrac{1}{2n}\right) = (0, 1)`, 所以

    .. math::

        \bigcup_{n=1}^\infty E_n = \{ x \in (0, 1) \ :\ f(x) \neq 0 \},

    它与 :math:`\{ x \in [0, 1] \ :\ f(x) \neq 0 \}` 至多只差一个有限集。记 :math:`I = [0, 1]`,
    那么有 :math:`m I(f \neq 0) = 0`, 即 :math:`f \sim 0`.

.. _ex-4-19:

19. 设对每个 :math:`n \in \mathbb{N}`, :math:`f_n` 在 :math:`E` 上可积，序列 :math:`\{f_n\}` 几乎处处收敛于 :math:`f, n \to \infty`,
且一致地有

.. math::

    \int_E \lvert f_n \rvert \mathrm{d} m \leqslant K, \quad K \text{ 为常数},

证明 :math:`f` 可积。

.. proof:proof::

    由于 :math:`f_n` 在 :math:`E` 上可积，序列 :math:`\{f_n\}` 几乎处处收敛于 :math:`f, n \to \infty`,
    所以 :math:`\lvert f_n \rvert` 在 :math:`E` 上可积，序列 :math:`\{ \lvert f_n \rvert \}` 几乎处处收敛于 :math:`\lvert f \rvert, n \to \infty`.
    令 :math:`\displaystyle E_0 = E \left( \lim_{n \to \infty} \lvert f_n \rvert \neq \lvert f \rvert \right)`, 那么 :math:`m E_0 = 0`.
    对 :math:`E` 上的非负可测函数列 :math:`\{ f_n \}` 应用 Fatou 引理，有

    .. math::

        K \geqslant \varliminf_{n \to \infty} \int_E \lvert f_n \rvert \mathrm{d} m \geqslant \int_E \varliminf_{n \to \infty} \lvert f_n \rvert \mathrm{d} m & = \int_{E_0} \varliminf_{n \to \infty} \lvert f_n \rvert \mathrm{d} m + \int_{E \setminus E_0} \varliminf_{n \to \infty} \lvert f_n \rvert \mathrm{d} m \\
        & = \int_{E_0} \lvert f \rvert \mathrm{d} m + 0 \\
        & = \int_{E_0} \lvert f \rvert \mathrm{d} m + \int_{E \setminus E_0} \lvert f \rvert \mathrm{d} m \\
        & = \int_E \lvert f \rvert \mathrm{d} m.

    所以 :math:`\lvert f \rvert` 在 :math:`E` 上可积，从而知 :math:`f` 可积。

.. _ex-4-21:

21. 设 :math:`f` 在 :math:`(-\infty, \infty)` 上可积，证明

.. math::

    \lim_{h \to 0} \int_{-\infty}^\infty \lvert f(x + h) - f(x) \rvert \mathrm{d} m = 0.

.. proof:proof::

    对每个自然数 :math:`k \in \mathbb{N}`, 令 :math:`E_k = [-k, k]`, 那么 :math:`\forall x \in \mathbb{R}`,
    有 :math:`\displaystyle \lim_{k \to \infty} f \cdot \chi_{E_k} (x) = f (x)`. 由于 :math:`f \in L_{\mathbb{R}}`,
    所以 :math:`\lvert f \rvert \in L_{\mathbb{R}}`, 并且 :math:`\lvert f \cdot \chi_{E_k} (x) \rvert \leqslant \lvert f (x) \rvert`
    对所有 :math:`x \in \mathbb{R}` 以及 :math:`k \in \mathbb{N}` 成立。于是，由 Lebesgue 控制收敛定理可得

    .. math::

        \lim_{k \to \infty} \int_{E_k} f \mathrm{d} m = \lim_{k \to \infty} \int_{\mathbb{R}} f \cdot \chi_{E_k} \mathrm{d} m = \int_{\mathbb{R}} \lim_{k \to \infty} f \cdot \chi_{E_k} \mathrm{d} m = \int_{\mathbb{R}} f \mathrm{d} m.

    那么 :math:`\forall \varepsilon > 0`, 存在 :math:`K \in \mathbb{N}`, 使得当 :math:`k > K` 时， 有

    .. math::

        0 \leqslant \int_{\mathbb{R} \setminus E_{k-1}} \lvert f \rvert \mathrm{d} m = \int_{\mathbb{R}} \lvert f \rvert \mathrm{d} m - \int_{E_{k-1}} \lvert f \rvert \mathrm{d} m < \dfrac{\varepsilon}{3}.

    同时，对于任一取定的 :math:`k > K`, 可以选取定义在 :math:`E_k` 上的简单函数 :math:`\displaystyle \varphi = \sum_{i=1}^n c_i \chi_{e_i}` 使得

    .. math::
        :label: ex-4-21-eq-1

        \int_{E_k} \lvert f - \varphi \rvert \mathrm{d} m \leqslant \int_{E_{k+1}} \lvert f - \varphi \rvert \mathrm{d} m < \dfrac{\varepsilon}{9}.

    这里，:math:`\varphi` 也被视作是 :math:`E_{k+1}` 上的简单函数。对于 :math:`0 < \lvert h \rvert < 1`, 在 :math:`E_{k+1}` 上有

    .. math::

        \lvert f(x + h) - f(x) \rvert \leqslant \lvert f(x + h) - \varphi(x + h) \rvert + \lvert \varphi(x + h) - \varphi(x) \rvert + \lvert \varphi(x) - f(x) \rvert.

    对于简单函数 :math:`\varphi`, 令 :math:`M = \displaystyle \sup_{x \in E_{k+1}} \lvert \varphi(x) \rvert = \max_{1 \leqslant i \leqslant n} \lvert c_i \rvert`.
    对所有 :math:`1 \leqslant i \leqslant n`, 可以选取开集 :math:`G_i \supset e_i` 使得 :math:`m G_i < m e_i + \dfrac{\varepsilon}{72nM}`.
    那么所有开集 :math:`G_i` 的构成区间形成了紧集 :math:`E_{k+1}` 的一个开覆盖，从而可以选出有限个开区间 :math:`I_1, I_2, \dots, I_t`,
    使得 :math:`\displaystyle E_{k+1} \subset \bigcup_{j=1}^t I_j`. 令 :math:`\displaystyle \widetilde{\varphi} = \sum_{j=1}^t \widetilde{c}_j \chi_{I_j}`,
    其中 :math:`\widetilde{c}_j = c_i` 若 :math:`I_j \subset G_i`; 对于可能重叠的部分，任意取定其中某一个值即可。
    那么当 :math:`\displaystyle 0 < h < \min_{1 \leqslant j \leqslant t} m I_j`, 总有

    .. math::

        \int_{E_{k+1}} \lvert \widetilde{\varphi} (x + h) - \widetilde{\varphi} (x) \rvert \mathrm{d} m \leqslant 2 M t \lvert h \rvert.

    进一步缩小 :math:`\lvert h \rvert`, 使其满足 :math:`0 < \lvert h \rvert < \dfrac{\varepsilon}{36 M t}`, 那么有

    .. math::

        \int_{E_{k+1}} \lvert \widetilde{\varphi} (x + h) - \widetilde{\varphi} (x) \rvert \mathrm{d} m < \dfrac{\varepsilon}{18}.

    另一方面有

    .. math::

        \lvert \varphi(x + h) - \varphi(x) \rvert \leqslant \lvert \varphi(x + h) - \widetilde{\varphi}(x + h) \rvert + \lvert \widetilde{\varphi} (x + h) - \widetilde{\varphi} (x) \rvert + \lvert \widetilde{\varphi}(x) - \varphi(x) \rvert,

    从而有

    .. math::
        :label: ex-4-21-eq-2

        & \int_{E_k} \lvert \varphi(x + h) - \varphi(x) \rvert \mathrm{d} m \\
        & \leqslant \int_{E_k} \lvert \varphi(x + h) - \widetilde{\varphi}(x + h) \rvert \mathrm{d} m + \int_{E_k} \lvert \widetilde{\varphi} (x + h) - \widetilde{\varphi} (x) \rvert \mathrm{d} m + \int_{E_k} \lvert \widetilde{\varphi}(x) - \varphi(x) \rvert \mathrm{d} m \\
        & \leqslant \int_{E_{k+1}} \lvert \varphi(x) - \widetilde{\varphi}(x) \rvert \mathrm{d} m + \int_{E_k} \lvert \widetilde{\varphi} (x + h) - \widetilde{\varphi} (x) \rvert \mathrm{d} m + \int_{E_{k+1}} \lvert \widetilde{\varphi}(x) - \varphi(x) \rvert \mathrm{d} m \\
        & \leqslant 2 \cdot 2M \cdot \dfrac{\varepsilon}{72nM} \cdot n + \dfrac{\varepsilon}{18} \\
        & \leqslant \dfrac{\varepsilon}{9}.

    综合式 :eq:`ex-4-21-eq-1` 和 :eq:`ex-4-21-eq-2`, 有

    .. math::

        & \int_{E_k} \lvert f(x + h) - f(x) \rvert \mathrm{d} m \\
        & \leqslant \int_{E_k} \leqslant \lvert f(x + h) - \varphi(x + h) \rvert  \mathrm{d} m + \int_{E_k} \lvert \varphi(x + h) - \varphi(x) \rvert  \mathrm{d} m + \int_{E_k} \lvert \varphi(x) - f(x) \rvert  \mathrm{d} m \\
        & \leqslant \int_{E_{k+1}} \leqslant \lvert f(x) - \varphi(x) \rvert  \mathrm{d} m + \int_{E_k} \lvert \varphi(x + h) - \varphi(x) \rvert  \mathrm{d} m + \int_{E_{k+1}} \lvert \varphi(x) - f(x) \rvert  \mathrm{d} m \\
        & \leqslant \dfrac{\varepsilon}{9} + \dfrac{\varepsilon}{9} + \dfrac{\varepsilon}{9} = \dfrac{\varepsilon}{3}.

    于是有

    .. math::

        \int_{\mathbb{R}} \lvert f(x + h) - f(x) \rvert \mathrm{d} m & = \left( \int_{E_k} + \int_{\mathbb{R} \setminus E_k} \right) \lvert f(x + h) - f(x) \rvert \mathrm{d} m \\
        & \leqslant \int_{E_k} \lvert f(x + h) - f(x) \rvert \mathrm{d} m + \int_{\mathbb{R} \setminus E_k} \lvert f(x + h) \rvert + \lvert f(x) \rvert \mathrm{d} m \\
        & \leqslant \dfrac{\varepsilon}{3} + \int_{\mathbb{R} \setminus E_{k-1}} 2 \lvert f(x) \rvert \mathrm{d} m \\
        & \leqslant \dfrac{\varepsilon}{3} + 2 \cdot \dfrac{\varepsilon}{3} = \varepsilon.

    这便证明了 :math:`\displaystyle \lim_{h \to 0} \int_{-\infty}^\infty \lvert f(x + h) - f(x) \rvert \mathrm{d} m = 0.`

    .. note::

        以上性质称作是 Lebesgue 积分的平均连续性。

.. _ex-4-23:

23. 设 :math:`f` 是 :math:`\mathbb{R}` 上的可积函数，试证

.. math::

    \widehat{f} (t) = \int_{\mathbb{R}} f(x) e^{-itx} \mathrm{d} x.

是 :math:`\mathbb{R}` 上的连续函数，且

.. math::

    \widehat{f} (t) = \dfrac{\mathrm{d}}{\mathrm{d} t} \int_{\mathbb{R}} \dfrac{e^{-itx} - 1}{-ix} f(x) \mathrm{d} x.

.. proof:proof::

    待写。

.. _ex-4-25:

25. 设 :math:`f` 是 :math:`\mathbb{R}` 上的可测函数，令 :math:`\mu (\alpha) = m \mathbb{R}(\lvert f \rvert > \alpha)`, 试证

.. math::

    \int_{\mathbb{R}} \lvert f \rvert^p \mathrm{d} m = \int_0^\infty \alpha^{p-1} \mu (\alpha) \mathrm{d} \alpha, \quad 1 \leqslant p < \infty.

.. proof:proof::

    待写。

.. _ex-4-26:

26. 设 :math:`m E < \infty`, 证明函数 :math:`f` 在 :math:`E` 上可积的充分必要条件是级数 :math:`\displaystyle \sum_{n=1}^\infty m E ( \lvert f \rvert \geqslant n)` 收敛。
当 :math:`m E = \infty` 时，结论是否成立？

.. proof:proof::

    待写。
