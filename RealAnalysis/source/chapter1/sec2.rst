§2 映射·集的对等·可列集
------------------------------

.. _ex-1-8:

8. 设 :math:`A = \{0, 1\}`, 试证一切排列

.. math::

    (a_1, a_2, \cdots, a_n, \cdots): \quad a_n \in A, n \in \mathbb{N}

所成之集的势为 :math:`\aleph`.

.. proof:proof::

    令集合 :math:`B = \{ (a_1, a_2, \cdots, a_n, \cdots): \ a_n \in A, n \in \mathbb{N} \}`, 以及集合
    :math:`B_0 = \{ (a_1, a_2, \cdots, a_n, \cdots) \in B: \ \exists n \in \mathbb{N}, s.t. \forall k \geqslant n, a_k = 1 \}`,
    并考虑映射

    .. math::

        f: B \setminus B_0 \to [0, 1], \quad (a_1, a_2, \cdots, a_n, \cdots) \mapsto \sum_{n=1}^{\infty} a_n 2^n.

    以上映射给出了集合 :math:`B \setminus B_0` 与区间 :math:`[0, 1]` 之间的一一对应，而 :math:`B_0` 是可列集，所以集合 :math:`B = (B \setminus B_0) \cup B_0`
    也与区间 :math:`[0, 1]` 对等，从而它的势为 :math:`\aleph`.

.. _ex-1-9:

9. 问下列各集能否与自然数集或区间 :math:`[0, 1]` 构成一一对应：

(1). 以有理数为端点的区间集；

(2). 闭正方形 :math:`[0, 1; 0, 1]`.

如果可能，试作出对应方法。

.. proof:solution::

    (1). 以有理数为端点的（开）区间集为 :math:`A = \left\{ (a, b) : \ a < b, a, b \in \mathbb{Q} \right\}`. 首先，:math:`A` 是 :math:`\mathbb{Q}^2` 的子集；
    另一方面，可以通过单射 :math:`\mathbb{Q} \to A: \ a \mapsto (a, a + 1)` 将 :math:`\mathbb{Q}` 视为 :math:`A` 的子集，从而集合 :math:`A` 是可列的。
    令 :math:`\mathbb{Q} = \{ r_1, r_2, \dots, r_n, \dots \}`, 那么 :math:`A` 到自然数集 :math:`\mathbb{N}` 的一一对应可以通过如下方式构造：

    首先，将集合 :math:`A` 改写为 :math:`A = \left\{ (a, d) : \ a \in \mathbb{Q}, d \in \mathbb{Q}^+ \right\}`, 其中 :math:`d` 为区间长度。
    那么 :math:`A \cong \mathbb{Q} \times \mathbb{Q}^+`. 我们可以定义 :math:`\mathbb{Q}^* = \mathbb{Q} \setminus \{ 0 \}` 上的高度函数
    :math:`H: \mathbb{Q}^* \to \mathbb{N}` 如下：

    .. math::

        H(\dfrac{p}{q}) = \max \{ \lvert p \rvert, \lvert q \rvert \}, \quad
        \text{其中} \dfrac{p}{q} \text{ 是既约分数}, q > 0.

    那么 :math:`\mathbb{Q}` 以及 :math:`\mathbb{Q}^+` 中高度等于定值 :math:`h` 的元素全体是有限集，于是可以通过如下的排序方式分别给出 :math:`\mathbb{Q}`
    以及 :math:`\mathbb{Q}^+` 到 :math:`\mathbb{N}` 的一一对应：

    .. math::

        \begin{align*}
        r_1 & \quad \{ 0 \}, \mathcal{H}_{11}, \mathcal{H}_{12}, \dots, \mathcal{H}_{1k}, \dots \\
        r_2 & \quad \{ 0 \}, \mathcal{H}_{21}, \mathcal{H}_{22}, \dots, \mathcal{H}_{2k}, \dots
        \end{align*}

    对于 :math:`k \in \mathbb{N}`, :math:`\mathcal{H}_{1k}` 表示 :math:`\mathbb{Q}` 中高度为 :math:`k` 的元素全体；:math:`\mathcal{H}_{2k}`
    表示 :math:`\mathbb{Q}^+` 中高度为 :math:`k` 的元素全体。在每一个 :math:`\mathcal{H}_{1k}` 以及 :math:`\mathcal{H}_{2k}` 中，将元素按其作为有理数的大小排序。
    这样，我们就给出了 :math:`\mathbb{Q} \times \mathbb{Q}^+` 到 :math:`\mathbb{N} \times \mathbb{N}` 的一一对应
    :math:`(r_1, r_2): \mathbb{Q} \times \mathbb{Q}^+ \to \mathbb{N} \times \mathbb{N}`.

    类似地，可以通过如下的排序方式给出一一对应 :math:`\mathbb{N} \times \mathbb{N} \to \mathbb{N}`:

    .. math::

        s: \mathcal{G}_1, \mathcal{G}_2, \dots, \mathcal{G}_k, \dots

    其中， :math:`\mathcal{G}_k = \{ (n_1, n_2) \in \mathbb{N} \times \mathbb{N} : \ n_1 + n_2 = k \}`, 其内部按 :math:`n_1` 的大小进行排序。于是，我们就给出了一一对应

    .. math::

        A \cong \mathbb{Q} \times \mathbb{Q}^+ \xrightarrow{(r_1, r_2)} \mathbb{N} \times \mathbb{N} \xrightarrow{s} \mathbb{N}.

    .. note::

        可以通过显式表达式给出一一对应 :math:`\mathbb{N} \times \mathbb{N} \to \mathbb{N}`:

        .. math::

            s: \mathbb{N} \times \mathbb{N} \to \mathbb{N}, \quad (n_1, n_2) \mapsto \dfrac{(n_1 + n_2 - 2)(n_1 + n_2 - 1)}{2} + n_1.

    (2). 这题是课本 §2 的例1，做法如下：

    将 :math:`[0, 1]` 中的数写成二进制小数的形式 :math:`x = 0.x_1x_2 \cdots`, 相应的一一对应关系为

    .. math::

        [0, 1] \times [0, 1] \to [0, 1] : \quad (x, y) \mapsto z = 0.x_1y_1x_2y_2 \cdots

    由于约定了二进制小数不用 :math:`0.\cdots 0111\cdots` 的形式表示，需要检查的就只有通过上述映射得到的 :math:`z` 不具有这种形式，用反证法很容易证明这种情况不会发生。

.. _ex-1-10:

10. 证明整系数多项式全体是可列的。

.. proof:proof::

    对于整系数多项式全体 :math:`\mathbb{Z}[X]` 有分解

    .. math::

        \mathbb{Z}[X] = \bigcup_{n=0}^{\infty} \mathbb{Z}_n[X], \quad \mathbb{Z}_n[X] = \{ f \in \mathbb{Z}[X]: \ \deg f = n \} \cong \mathbb{Z}^{n} \times \mathbb{Z}^{\ast},

    其中 :math:`\mathbb{Z}^{\ast} = \mathbb{Z} \setminus \{ 0 \}` (最高次项系数不为 :math:`0`). 由于 :math:`\mathbb{Z}^{n} \times \mathbb{Z}^{\ast}` 是可列集，
    所以 :math:`\mathbb{Z}_n[X]` 是可列集，从而 :math:`\mathbb{Z}[X]` 是可列集。

.. _ex-1-15:

15. 设给定映射 :math:`f: X \to Y`. 试证对 :math:`Y` 中的任意集族 :math:`\{ B_{\alpha} \}_{\alpha \in I}` 有

.. math::

    \begin{gather*}
    f^{-1} \left( \bigcup_{\alpha \in I} B_{\alpha} \right) = \bigcup_{\alpha \in I} f^{-1} (B_{\alpha}), \quad
    f^{-1} \left( \bigcap_{\alpha \in I} B_{\alpha} \right) \subset \bigcap_{\alpha \in I} f^{-1} (B_{\alpha}), \\
    f^{-1} (\mathscr{C} B) = \mathscr{C} f^{-1} (B).
    \end{gather*}

.. proof:proof::

    任取 :math:`x \in f^{-1} \left( \bigcup\limits_{\alpha \in I} B_{\alpha} \right)`, 那么有 :math:`f(x) \in \bigcup\limits_{\alpha \in I} B_{\alpha}`,
    这意味着存在 :math:`\alpha \in I`, 使得 :math:`f(x) \in B_{\alpha}`, 从而有 :math:`x \in f^{-1} (B_{\alpha})`, 于是有
    :math:`x \in \bigcup\limits_{\alpha \in I} f^{-1} (B_{\alpha})`. 反过来，任取 :math:`x \in \bigcup\limits_{\alpha \in I} f^{-1} (B_{\alpha})`,
    那么存在 :math:`\alpha \in I`, 使得 :math:`x \in f^{-1} (B_{\alpha})`, 于是有 :math:`f(x) \in B_{\alpha}`, 从而有
    :math:`f(x) \in \bigcup\limits_{\alpha \in I} B_{\alpha}`, 于是有 :math:`x \in f^{-1} \left( \bigcup\limits_{\alpha \in I} B_{\alpha} \right)`.
    综上所述，有 :math:`f^{-1} \left( \bigcup\limits_{\alpha \in I} B_{\alpha} \right) = \bigcup\limits_{\alpha \in I} f^{-1} (B_{\alpha})`.

    任取 :math:`x \in f^{-1} \left( \bigcap\limits_{\alpha \in I} B_{\alpha} \right)`, 那么有 :math:`f(x) \in \bigcap\limits_{\alpha \in I} B_{\alpha}`,
    这意味着对任意 :math:`\alpha \in I`, 都有 :math:`f(x) \in B_{\alpha}`, 从而有 :math:`x \in f^{-1} (B_{\alpha})`, 于是有
    :math:`x \in \bigcap\limits_{\alpha \in I} f^{-1} (B_{\alpha})`. 反过来，任取 :math:`x \in \bigcap\limits_{\alpha \in I} f^{-1} (B_{\alpha})`,
    那么对任意 :math:`\alpha \in I`, 都有 :math:`x \in f^{-1} (B_{\alpha})`, 于是有 :math:`f(x) \in B_{\alpha}`, 从而有
    :math:`f(x) \in \bigcap\limits_{\alpha \in I} B_{\alpha}`, 于是有 :math:`x \in f^{-1} \left( \bigcap\limits_{\alpha \in I} B_{\alpha} \right)`.

    若 :math:`f^{-1} (\mathscr{C} B) = \emptyset`, 即 :math:`\forall x \in X, f(x) \not\in \mathscr{C} B`, 那么有 :math:`\forall x \in X, f(x) \in B`,
    这意味着 :math:`f^{-1} (B) = X`, 于是有 :math:`\mathscr{C} f^{-1} (B) = \emptyset`. 若 :math:`f^{-1} (\mathscr{C} B) \neq \emptyset`,
    任取 :math:`x \in f^{-1} (\mathscr{C} B)`, 那么有 :math:`f(x) \in \mathscr{C} B`, 于是有 :math:`f(x) \not\in B`, 从而有
    :math:`x \not\in f^{-1} (B)`, 于是有 :math:`x \in \mathscr{C} f^{-1} (B)`. 反过来，任取 :math:`x \in \mathscr{C} f^{-1} (B)`,
    那么有 :math:`x \not\in f^{-1} (B)`, 于是有 :math:`f(x) \not\in B`, 从而有 :math:`f(x) \in \mathscr{C} B`, 于是有
    :math:`x \in f^{-1} (\mathscr{C} B)`. 综上所述，有 :math:`f^{-1} (\mathscr{C} B) = \mathscr{C} f^{-1} (B)`.
