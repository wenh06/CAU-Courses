第一章  函数与极限
^^^^^^^^^^^^^^^^^^^^^^^^^

..  contents:: :local:

§1.2 函数的极限补充问题
--------------------------------

1. 设 :math:`a_n > 0 (n = 1, 2, \ldots)` 且存在常数 :math:`c > 0` 使得 :math:`\forall n > m > 1` 有 :math:`a_n \le c \cdot a_m`.
已知 :math:`\{a_n\}` 存在子列 :math:`\{a_{n_k}\}` 极限等于0，求证 :math:`\lim\limits_{n \to \infty} a_n = 0`。

.. proof:proof::

    由于 :math:`\lim_{k \to \infty} a_{n_k} = 0`, 那么 :math:`\forall \varepsilon > 0, \exists K(\varepsilon) \in \mathbb{N}^+`,
    使得 :math:`\forall k > K(\varepsilon)` 有 :math:`|a_{n_k} - 0| < \varepsilon / c`, 由于 :math:`a_n > 0` 对所有 :math:`n` 成立, 我们可以得到

    .. math::

        0 < a_{n_k} < \varepsilon / c

    由于 :math:`\forall n > m > 1` 有 :math:`a_n \le c \cdot a_m`, 那么 :math:`\forall n > n_{K(\varepsilon)+1}` 有

    .. math::

        0 < a_n < c \cdot a_{n_{K(\varepsilon)+1}} < c \cdot \varepsilon / c = \varepsilon

    由于 :math:`\varepsilon` 是任意的，所以 :math:`\lim\limits_{n \to \infty} a_n = 0`.

§1.4 极限存在准则与两个重要极限补充问题
--------------------------------------------

求 :math:`\lim\limits_{x \to 0} x \left[ \dfrac{1}{x} \right]`

.. proof:solution::

    取整函数的定义为

    .. math::

        [x] = \max \{ n \in \mathbb{Z} | n \le x \} = n \text{ 若 } n \le x < n + 1, n \in \mathbb{Z}

    那么对于 :math:`\left[ \dfrac{1}{x} \right]` 来说，有 :math:`\left[ \dfrac{1}{x} \right] \le \dfrac{1}{x} < \left[ \dfrac{1}{x} \right] + 1`
    (将上式的 :math:`x, n` 分别替换为 :math:`\dfrac{1}{x}, \left[ \dfrac{1}{x} \right]` 即可)，那么

    .. math::

        \dfrac{1}{x} - 1 < \left[ \dfrac{1}{x} \right] \le \dfrac{1}{x}

    那么可以利用夹逼准则得到

    .. math::

        1 = \lim\limits_{x \to 0} x \left( \dfrac{1}{x} - 1 \right) \le \lim\limits_{x \to 0} x \left[ \dfrac{1}{x} \right] \le \lim\limits_{x \to 0} x \cdot \dfrac{1}{x} = 1

§1.6 函数的连续型与连续函数的运算补充问题
--------------------------------------------

Riemann 函数定义为

.. math::

    f(x) = \begin{cases}
        0, & x \text{ 为无理数} \\
        \dfrac{1}{q}, & x = \dfrac{p}{q} \text{ 为有理数, 且 } p, q \text{ 互素, } q > 0
    \end{cases}

求证 Riemann 函数在所有无理数点处连续，且在所有有理数点处间断。

.. proof:proof::

    待写
