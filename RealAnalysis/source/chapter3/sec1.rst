§1 可测函数的基本性质
------------------------------------------

2. 证明 :math:`f(x)` 为 :math:`E` 上可测函数的充分必要条件是：对于任一有理数 :math:`r`，集 :math:`E(f > r)` 恒可测。
如果假设对任一有理数 :math:`r`，集 :math:`E(f = r)` 恒可测，问 :math:`f(x)` 是否可测？

.. proof:proof::

    由 :ref:`本章补充材料 <measurable_function_supp>` 知，若存在 :math:`D` 为 :math:`\mathbb{R}` 中稠密集，
    使得 :math:`\forall \alpha \in D`, :math:`E(f > \alpha)` 都是可测集，则 :math:`f` 是可测函数。
    特别地，本题中取 :math:`D` 为有理数集 :math:`\mathbb{Q}`，则 :math:`\forall r \in \mathbb{Q}`,
    :math:`E(f > r)` 都是可测集，于是 :math:`f` 是可测函数。反过来显然。

    集 :math:`E(f = r)` 恒可测，不能推出 :math:`f` 是可测函数。反例如下：设 :math:`E = [0, 1]`,
    集合 :math:`A \subset E` 是不可测集，函数 :math:`f(x) = \chi_A(x) + \alpha`, 其中 :math:`\alpha` 任一无理数，
    那么任取 :math:`r \in \mathbb{Q}`，有 :math:`E(f = r) = \emptyset`，是可测集，但 :math:`f` 不是可测函数。

4. 设 :math:`f(x)` 是 :math:`E` 上的可测函数， :math:`G, F` 分别为 :math:`\mathbb{R}` 中开集与闭集。
试问 :math:`E(f \in G)` 与 :math:`E(f \in F)` 是否可测，这里记号 :math:`E(f \in A) = E(x: f(x) \in A)`.

.. proof:proof::

    设开集 :math:`G \subset \mathbb{R}` 有结构表示 :math:`\displaystyle G = \bigcup_{n=1}^{\infty} (a_n, b_n)`，则

    .. math::

        E(f \in G) = f^{-1}(G) = f^{-1} \left(\bigcup_{n=1}^{\infty} (a_n, b_n)\right) = \bigcup_{n=1}^{\infty} f^{-1}((a_n, b_n)) = \bigcup_{n=1}^{\infty} E(f > a_n) \cap E(f < b_n)

    因此 :math:`E(f \in G)` 是可测集。

    对于闭集 :math:`F \subset \mathbb{R}`，有 :math:`\mathbb{R} \setminus F` 是开集，于是

    .. math::

        E(f \in F) = E(f \in \mathbb{R} \setminus (\mathbb{R} \setminus F)) = E \setminus E(f \in \mathbb{R} \setminus F)

    是可测集。

6. 设 :math:`f(x)` 是 :math:`(-\infty, \infty)` 上的连续函数， :math:`g(x)` 是 :math:`[a, b]` 上的有限可测函数，
证明 :math:`f(g(x))` 是可测函数。

.. proof:proof::

    由于 :math:`\mathbb{R}` 中开集有由互不相交的开区间构成的结构表示，而有限函数 :math:`h(x)` 可测当且仅当
    :math:`E(a < h < b)` 对所有的开区间 :math:`(a, b)` 都可测，因此 :math:`h(x)` 可测当且仅当
    :math:`E(f \in G)` 对所有的开集 :math:`G \subset \mathbb{R}` 都可测。由于 :math:`f(x)` 是连续函数，
    因此 :math:`f^{-1}(G)` 是开集，那么

    .. math::

        E(f \circ g \in G) = E(g \in f^{-1}(G)) = E(g \in f^{-1}(G))

    是可测集，即 :math:`f \circ g` 是可测函数。

10. 设 :math:`x \in [0, 1)` 的三进表示为 :math:`x = 0.x_1 x_2 \cdots x_n \cdots`, :math:`x_n \in \{0, 1, 2\}`,
并约定全用无限表示。用 :math:`P_i` 表示 :math:`x` 的三进表示中不出现数字 :math:`i` 的点集， :math:`i = 0, 1, 2`. 令

.. math::

    f(x) = \begin{cases}
        x + i, & x \in P_i, i = 0, 1, 2, \\
        x + 3, & x \in [0, 1) \setminus \cup_{i=0}^2 P_i,
    \end{cases}

并规定 :math:`f(0) = 3, f(1/2) = 7/2`. 问 :math:`f(x)` 是否可测，是否连续？

.. proof:solution::

    待写

11. 设 :math:`f(x, y)` 为定义在 :math:`\mathbb{R}^2` 上的几乎处处有限的函数，它对每个固定的 :math:`x` 关于 :math:`y` 连续，
且对每个固定的 :math:`y` 关于 :math:`x` 也连续。试证 :math:`f(x, y)` 是 :math:`\mathbb{R}^2` 上的可测函数。

.. proof:proof::

    待写
