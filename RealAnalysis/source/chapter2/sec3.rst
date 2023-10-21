§3 可测集的性质
------------------------------------------

.. _ex-2-9:

9. 设 :math:`E_1, E_2` 均为有界可测集，试证

.. math::

    m (E_1 \cup E_2) = m E_1 + m E_2 - m (E_1 \cap E_2).

.. proof:proof::

    因为 :math:`E_1, E_2` 均为有界可测集，所以 :math:`E_1 \cup E_2, E_1 \setminus E_2, E_2 \setminus E_1, E_1 \cap E_2` 均为有界可测集，且

    .. math::

        E_1 \cup E_2 = (E_1 \setminus E_2) \cup (E_2 \setminus E_1) \cup (E_1 \cap E_2)

    为可测集的不交并，所以根据测度的完全可加性有

    .. math::

        m (E_1 \cup E_2) = m (E_1 \setminus E_2) + m (E_2 \setminus E_1) + m (E_1 \cap E_2).

    另一方面，:math:`E_1` 有互斥分解 :math:`E_1 = (E_1 \setminus E_2) \cup (E_1 \cap E_2)`，所以根据测度的完全可加性有 :math:`m E_1 = m (E_1 \setminus E_2) + m (E_1 \cap E_2)`.
    同理 :math:`m E_2 = m (E_2 \setminus E_1) + m (E_1 \cap E_2)`，所以有

    .. math::

        m (E_1 \cup E_2) = m E_1 + m E_2 - m (E_1 \cap E_2).

10. 设 :math:`E` 是 :math:`\mathbb{R}` 中可测集，:math:`A` 是任意集，证明

.. math::

    m^* (E \cap A) + m^* (E \cap A) = m E + m^* A;

:math:`E` 不可测时如何？

.. proof:proof::

    由 Carathéodory 条件，对于任意集 :math:`A` 有

    .. math::

        m^* A = m^* (A \cap E) + m^* (A \cap \mathcal{C} E).

    对集 :math:`A \cup E` 再次应用 Carathéodory 条件，有

    .. math::

        m^* (A \cup E) = m^* ((A \cup E) \cap E) + m^* ((A \cup E) \cap \mathcal{C} E) = m E + m^* (A \cap \mathcal{C} E).

    两式消去共同项 :math:`m^* (A \cap \mathcal{C} E)` 即有

    .. math::

        m^* (E \cap A) + m^* (E \cap A) = m E + m^* A.

13. 设 :math:`G` 是开集， :math:`E` 是零测度集，试证 :math:`\overline{G} = \overline{G \setminus E}`.

.. proof:proof::

    由于 :math:`C \supset G \setminus E`，所以 :math:`\overline{G} \supset \overline{G \setminus E}`. 假设这是一个真包含关系，
    那么存在 :math:`x \in \mathbb{R}` 以及 :math:`x` 的去心邻域 :math:`\mathring{U} (x)`，使得

    .. math::

        \mathring{U} (x) \cap G \neq \emptyset` \\
        \mathring{U} (x) \cap (G \setminus E) = \emptyset.

    由于 :math:`G` 是开集，所以 :math:`\mathring{U} (x) \cap G` 也是开集。任取 :math:`\mathring{U} (x) \cap G` 的一个构成区间 :math:`(a, b)`,
    那么有 :math:`(a, b) \subset E`，这与 :math:`E` 是零测度集矛盾，所以 :math:`\overline{G} = \overline{G \setminus E}`.

15. 给出互不相交的集列 :math:`\{E_n\}_{n \in \mathbb{N}}`，满足

.. math::

    m^* \left( \bigcup_{n=1}^\infty E_n \right) < \sum_{n=1}^\infty m^* (E_n).

.. proof:proof::

    待写

17. 试举例说明，存在可测集列 :math:`\{E_n \subset (a, b)\}_{n \in \mathbb{N}}`，使极限 :math:`\lim\limits_{n \to \infty} m E_n` 存在，但 :math:`\lim\limits_{n \to \infty} E_n` 不存在.

.. proof:solution::

    可以借用 :ref:`第一章第6题<ex-1-6>` 中的例子，构造如下的可测集列

    .. math::

        E_n = \left\{ m / n : m \in \mathbb{Z} \right\} \cap (a, b), n \in \mathbb{N},

    那么每个 :math:`E_n` 都是有限集，从而 :math:`m E_n = 0`，于是极限 :math:`\lim_{n \to \infty} m E_n` 存在，值为 :math:`0`，但是

    .. math::

        \varliminf\limits_{n} E_n & = \bigcup\limits\limits_{k=1}^{\infty} \bigcap\limits_{n=k}^{\infty} E_n = \mathbb{Z} \cap (a, b), \\
        \varlimsup\limits_{n} E_n & = \bigcap\limits\limits_{k=1}^{\infty} \bigcup\limits_{n=k}^{\infty} E_n = \mathbb{Q} \cap (a, b),

    两者不相等，所以 :math:`\lim\limits_{n \to \infty} E_n` 不存在.

18. 设 :math:`A_1, A_2, \cdots, A_n` 是 :math:`[0, 1]` 中 :math:`n` 个可测集，且满足 :math:`\sum\limits_{k=1}^n m A_k > n - 1`，试证

.. math::

    m \left( \bigcap_{k=1}^n A_k \right) > 0.

.. proof:proof::

    待写

20. 试作一闭集 :math:`F \subset [0, 1]`，使 :math:`F` 中不含任何开区间，而 :math:`m F = 1/2`.

.. proof:solution::

    按如下方法修改 Cantor 三分集的构造：第一次去掉中间的开区间，长度为 :math:`0 < a \le 1/3`; 第二次从剩下的两个闭区间中去掉中间的开区间，
    长度为 :math:`a^2`; :math:`\dots`; 第 :math:`n` 次去掉剩下 :math:`2^{n-1}` 个闭区间中间的开区间，长度为 :math:`a^n`.
    这样，被去掉的开区间的总长度为

    .. math::

        \sum\limits_{n=1}^\infty 2^{n-1} a^n = \df{a}{1 - 2a}.

    以上就是从 :math:`[0, 1]` 中挖去的开集的测度。那么得到的闭集的测度为

    .. math::

        1 - \df{a}{1 - 2a} = \df{1 - 3a}{1 - 2a}.

    当 :math:`a = 1/4` 时，闭集的测度为 :math:`1/2`，且不含任何开区间。
