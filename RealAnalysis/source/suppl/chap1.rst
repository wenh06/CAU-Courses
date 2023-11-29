第一章补充材料
^^^^^^^^^^^^^^^^^^^^^^^^^

1. Cantor 函数的连续性以及非绝对连续性。Cantor 函数定义如下：记 Cantor 三分集为 :math:`P_0`, 定义其上的函数

.. math::

    \varphi: P_0 \to [0, 1], \quad x = 2 \sum\limits_{i=1}^{\infty} \dfrac{a_i}{3^i} \mapsto \sum\limits_{i=1}^{\infty} \dfrac{a_i}{2^i}.

其中 :math:`a_i \in \{0, 1\}`。基于这个函数，我们可以定义 Cantor 函数 :math:`\Phi` 为

.. math::

    \Phi: [0, 1] \to [0, 1], \quad x \mapsto \sup \{ \varphi(y) \mid y \in P_0, y \leq x \}.

.. proof:proof::

    (1). 首先来证明 :math:`\varphi` 是连续的（甚至是一致连续的）：
    不妨设 :math:`x < y, x = \sum\limits_{i=1}^{\infty} \dfrac{a_i}{3^i}, y = \sum\limits_{i=1}^{\infty} \dfrac{b_i}{3^i}`,
    其中 :math:`a_i, b_i \in \{0, 1, 2\}`. 令 :math:`k(x) = \min \{ i \mid a_i = 1 \}`, :math:`k(y) = \min \{ i \mid b_i =1 \}`,
    并约定 :math:`k(x) = +\infty` 当 :math:`x \in P_0`; :math:`k(y) = +\infty` 当 :math:`y \in P_0`。那么

    .. math::

        \Phi(x) & = \sum\limits_{i=1}^{k(x)-1} \dfrac{a_i}{2^{i+1}} + \sum\limits_{i=k(x)+1}^{\infty} \dfrac{1}{2^i} = \sum\limits_{i=1}^{k(x)-1} \dfrac{a_i}{2^{i+1}} + \dfrac{1}{2^{k(x)}} = \varphi(0.a_1 a_2 \cdots a_{k(x)-1} 2) = \varphi(\tilde{x}), \\
        \Phi(y) & = \sum\limits_{i=1}^{k(y)-1} \dfrac{b_i}{2^{i+1}} + \sum\limits_{i=k(y)+1}^{\infty} \dfrac{1}{2^i} = \sum\limits_{i=1}^{k(y)-1} \dfrac{b_i}{2^{i+1}} + \dfrac{1}{2^{k(y)}} = \varphi(0.b_1 b_2 \cdots b_{k(y)-1} 2) = \varphi(\tilde{y}),

    其中 :math:`0.a_1 a_2 \cdots a_{k(x)-1} 2` 和 :math:`0.b_1 b_2 \cdots b_{k(y)-1} 2` 是三进制小数，
    并约定 :math:`\sum\limits_{\infty}^{\infty} \cdot = 0, \sum\limits_{i = 1}^{0} \cdot = 0`. 这是因为对于 :math:`x \not \in P_0`,
    我们如下的 :math:`P_0` 的子列

    .. math::

        c_m = 0.a_1 a_2 \cdots a_{k(x)-1} 0 \underbrace{2 2 \cdots 2}_{m\text{个}} 0 0 \cdots \in P_0, \quad m = 1, 2, \cdots

    满足 :math:`c_m < x`, 且 :math:`0.a_1 a_2 \cdots a_{k(x)-1} 2 > x`. 对于 :math:`y \not \in P_0`, 我们有类似的 :math:`P_0` 的子列 :math:`d_m` 满足 :math:`d_m < y`, 且 :math:`0.b_1 b_2 \cdots b_{k(y)-1} 2 > y`. 记 :math:`\tilde{x}` 的三进制小数表示为 :math:`0.\tilde{a}_1 \tilde{a}_2 \cdots`, :math:`\tilde{y}` 的三进制小数表示为 :math:`0.\tilde{b}_1 \tilde{b}_2 \cdots`, 其中

    .. math::

        \tilde{a}_i = \begin{cases}
            a_i, & 1 \leq i \leq k(x) - 1, \\
            2, & i = k(x), \\
            0, & i > k(x),
        \end{cases} \quad
        \tilde{b}_i = \begin{cases}
            b_i, & 1 \leq i \leq k(y) - 1, \\
            2, & i = k(y), \\
            0, & i > k(y),
        \end{cases}

    任取 :math:`1 > \varepsilon > 0`, 记其二进制小数表示为 :math:`0.\varepsilon_1 \varepsilon_2 \cdots, \varepsilon_i \in \{0, 1\}`.
    令 :math:`N = \min \{ i \mid \varepsilon_i = 1 \}`. 取 :math:`1 > \delta > 0`, 使得其三进制小数表示为 :math:`0.\delta_1 \delta_2 \cdots`,
    满足 :math:`\delta_i = 2 \varepsilon_i`. 任取 :math:`x, y \in [0, 1]`, 且 :math:`\lvert x - y \rvert < \delta`, 那么

    .. math::

        \min \{ i \mid \tilde{a}_i \neq \tilde{b}_i \} \geqslant \min \{ i \mid a_i \neq b_i \} \geqslant N.

    因此有

    .. math::

        \lvert \Phi(x) - \Phi(y) \rvert = \lvert \varphi(\tilde{x}) - \varphi(\tilde{y}) \rvert \leqslant \left\lvert \sum\limits_{i=N}^{\infty} \dfrac{2}{2^{i+1}} \right\rvert = \dfrac{1}{2^{N-1}} < 2\varepsilon.

    由 :math:`\varepsilon` 的任意性，可知 :math:`\Phi` 是连续的。

    (2). 接下来证明 :math:`\Phi` 不是绝对连续的。这需要用到第二章测度论的知识。假设 :math:`\Phi` 是绝对连续的，
    那么对于任意的 :math:`\varepsilon > 0`, 存在 :math:`\delta > 0`, 使得对于任意有限多个互不相交的开区间 :math:`(a_i, b_i), i = 1, \dots, n`, 只要

    .. math::

        \sum\limits_{i=1}^{n} (b_i - a_i) < \delta,

    就有

    .. math::

        \sum\limits_{i=1}^{n} (\Phi(b_i) - \Phi(a_i)) = \sum\limits_{i=1}^{n} \lvert \Phi(b_i) - \Phi(a_i) \rvert < \varepsilon.

    不妨把 :math:`\Phi` 延拓到 :math:`\mathbb{R}` 上，其中 :math:`\Phi(x) = 0` 当 :math:`x < 0`, :math:`\Phi(x) = 1` 当 :math:`x > 1`.
    在第二章中，我们已经证明了 Cantor 三分集 :math:`P_0` 是一个零测集，也就是说对于 :math:`\delta`, 总存在开集 :math:`G`, 使得 :math:`m(G) < \delta`,
    且 :math:`P_0 \subset G`. 令 :math:`G` 的结构表示为 :math:`G = \bigcup\limits_{i} I_i`, 其中 :math:`I_i = (a_i, b_i)` 是互不相交的开区间。
    又由于 :math:`P_0` 是有界闭集，那么可以从它的开覆盖 :math:`G` 中选出有限个开区间
    :math:`I_1, \dots, I_n`, 使得 :math:`P_0 \subset \bigcup\limits_{i=1}^{n} I_i`. 那么有

    .. math::

        \sum\limits_{i=1}^{n} (b_i - a_i) \leqslant m(G) < \delta,

    从而有

    .. math::
        :label: abs-cont-cond

        \sum\limits_{i=1}^{n} (\Phi(b_i) - \Phi(a_i)) < \varepsilon.

    另一方面， Cantor 函数 :math:`\Phi` 在 :math:`\mathbb{R} \setminus P_0 \supset \mathbb{R} \setminus G` 上是常值函数，
    特别地，:math:`\Phi` 在所有的闭区间 :math:`[b_i, a_{i+1}], i = 1, \dots, n-1` 上都是常值函数，因此

    .. math::

        \sum\limits_{i=1}^{n} (\Phi(b_i) - \Phi(a_i)) & = -\Phi(a_1) + (\Phi(b_1) - \Phi(a_2)) + \cdots + (\Phi(b_{n-1}) - \Phi(a_n)) + \Phi(b_n) \\
        & = \Phi(b_n) - \Phi(a_0)

    由于 :math:`\{I_i = (a_i, b_i)\}_{i = 1, \dots, n}` 覆盖了 :math:`P_0`, 不妨设 :math:`a_1 < b_1 < a_2 < b_2 < \cdots < a_n < b_n`,
    因此 :math:`a_0 < 0, b_n > 1`, 从而有 :math:`\Phi(a_0) = 0, \Phi(b_n) = 1`. 于是有

    .. math::

        \sum\limits_{i=1}^{n} (\Phi(b_i) - \Phi(a_i)) = \Phi(b_n) - \Phi(a_0) = 1.

    这与式 :eq:`abs-cont-cond` 矛盾，因此 :math:`\Phi` 不是绝对连续的。
