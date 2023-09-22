第一章  集与点集
^^^^^^^^^^^^^^^^^^^^^^^^^

..  contents:: :local:

§1.2 函数的极限补充问题：

设 :math:`a_n > 0 (n = 1, 2, \ldots)` 且存在常数 :math:`c > 0` 使得 :math:`\forall n > m > 1` 有 :math:`a_n \le c \cdot a_m`.
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
