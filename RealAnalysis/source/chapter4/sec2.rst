§2 积分的性质
------------------------------------------

8. Levi 定理中去掉函数列的非负性假定，结论是否成立？

.. proof:solution::

    一般不成立。例如当 :math:`f_n` 的正部与负部积分都是 :math:`\infty` 时， :math:`f_n` 的积分不存在。
    即使当 :math:`f_n` 的积分有定义时，Levi 定理也不一定成立，例如 :math:`E = [0, \infty)`, :math:`f_n(x) = - \chi_{[n, \infty)}`,
    则 :math:`f_n` 的积分为 :math:`- \infty`, 但是 :math:`f_n` 逐点收敛于 :math:`f = 0`, :math:`f` 的积分为 :math:`0`, 此时

    .. math::

        \int_E f \mathrm{d} m = 0 \neq - \infty = \lim_{n \to \infty} \int_E f_n \mathrm{d} m.

    如果加上 :math:`f_n` 的积分都有定义，且 :math:`\displaystyle \int_E f_1 \mathrm{d} m \geqslant - \infty` 这个条件，Levi 定理就成立了。

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
