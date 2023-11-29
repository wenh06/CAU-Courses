§2 有界点集的外、内测度 · 可测集
------------------------------------------

1. 试证可列个零测度集的并集仍是零测度集.

.. proof:proof::

    设 :math:`E=\bigcup\limits_{n=1}^\infty E_n`，其中 :math:`E_n` 是零测度集。由于 :math:`0 \leqslant m_* E \leqslant m^* E`, 所以要证明 :math:`E` 是零测度集，
    只要证明 :math:`E` 的外测度为零即可。根据外测度的性质，有

    .. math::

        m^* E \leq \sum_{n=1}^\infty m^* E_n = 0

    所以 :math:`m^* E = 0`，即 :math:`E` 是零测度集。

3. 设 :math:`G_1, G_2` 是开集，且 :math:`G_1` 是 :math:`G_2` 的真子集，是否一定有 :math:`m G_1 < m G_2`?

.. proof:solution::

    不一定。例如 :math:`G_1 = (0, 1) \cup (1, 2), G_2 = (0, 2)`，则 :math:`G_1` 是 :math:`G_2` 的真子集，但是 :math:`m G_1 = m G_2 = 2`.

.. _ex-2-4:

4. 对任意开集 :math:`G`, 是否有 :math:`m \overline{G} = m G` 成立？

.. proof:solution::

    不一定。例如，令 :math:`0 < \varepsilon < 1`, 取 :math:`A = (0, 1) \cap \mathbb{Q} = \{ a_1, a_2, \cdots \}`, 对每个有理数 :math:`a_n \in A`,
    取开区间 :math:`G_n = (a_n - \frac{\varepsilon}{2^{n+1}}, a_n + \frac{\varepsilon}{2^{n+1}})`, 则 :math:`G = \bigcup\limits_{n=1}^\infty G_n` 是开集，且有

    .. math::

        m G \leqslant \sum_{n=1}^\infty m G_n = \sum_{n=1}^\infty \frac{\varepsilon}{2^n} = \varepsilon

    但是 :math:`\overline{G} = [0, 1]`，所以 :math:`m \overline{G} = 1`. 此时必有 :math:`m \overline{G} \neq m G`.

5. 如果把外测度的定义改为“有界集 :math:`E` 的外测度定义为包含 :math:`E` 的闭集的测度的下确界”，是否合理？

.. proof:solution::

    不合理。因为闭集的闭包仍然是闭集，以 :ref:`上题 <ex-2-4>` 中的 :math:`G` 为例，由于 :math:`m \overline{G} = 1`，所以这样定义的 :math:`G` 的外测度 :math:`m^* G \geqslant 1`.
    而对每一个开区间 :math:`G_n = (a_n - \frac{\varepsilon}{2^{n+1}}, a_n + \frac{\varepsilon}{2^{n+1}})` 来说，包含它的最小闭集为
    :math:`\overline{G_n} = [a_n - \frac{\varepsilon}{2^{n+1}}, a_n + \frac{\varepsilon}{2^{n+1}}]`, 所以这样定义的 :math:`G_n` 的外测度 :math:`m^* G_n = \dfrac{\varepsilon}{2^n}`.
    那么 :math:`\sum\limits_{n=1}^\infty m^* G_n = \varepsilon`. 这样一来，外测度的半可加性

    .. math::

        m^* G \leqslant \sum_{n=1}^\infty m^* G_n

    就不成立了。

6. 设 :math:`A_1, A_2, \cdots, A_n` 是 :math:`n` 个互不相交的可测集，且 :math:`E_k \subset A_k, k = 1, 2, \cdots, n`. 试证

.. math::

    m^* \left( \bigcup_{k=1}^n E_k \right) = \sum_{k=1}^n m^* E_k

.. proof:proof::

    记 :math:`E = \bigcup\limits_{k=1}^n E_k`. 由于 :math:`E_k \subset A_k, k = 1, 2, \cdots, n`, 且 :math:`A_k` 互不相交，所以

    .. math::

        E \cap A_k = E_k, \quad E \cap \mathscr{C} A_k = \bigcup\limits_{j \neq k} E_j, \quad k = 1, 2, \cdots, n

    由于 :math:`A_1, A_2, \cdots, A_n` 是可测集，根据可测集的 Carahtéodory 条件，有

    .. math::

        m^* E & = m^* (E \cap A_1) + m^* (E \cap \mathscr{C} A_1) \\
        & = m^* E_1 + m^* \left( \bigcup\limits_{k=2}^n E_k \right) \\
        & = m^* E_1 + m^* E_2 + m^* \left( \bigcup\limits_{k=3}^n E_k \right) \\
        & \quad \vdots \\
        & = \sum_{k=1}^n m^* E_k
