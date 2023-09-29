第一章  集与点集
^^^^^^^^^^^^^^^^^^^^^^^^^

..  contents:: :local:

§1 集及其运算
----------------

1. 证明关系式

(1). :math:`(A \setminus B) \cap (C \setminus D) = (A \cap C) \setminus (B \cup D).`

(2). :math:`(A \cap B) \cup C = (A \cup C) \cap (B \cup C).`

(3). :math:`A \setminus (B \setminus C) \subset (A \setminus B) \cup C.`

(4). :math:`(A \setminus B) \setminus (C \setminus D) \subset (A \setminus C) \cup (D \setminus B).`

(5). :math:`(A \setminus B) \cup C = A \setminus (B \setminus C)` 成立的充要条件是什么？

(6). :math:`A \cup (B \setminus C) = (A \cup B) \setminus C` 是否成立？

.. proof:proof::

    总可以假设上述集合都包含在某个基本集 :math:`X` 中，于是可以将差集写成与相应补集的交集。

    (1). 有

    .. math::

        \begin{align*}
        & (A \setminus B) \cap (C \setminus D) \\
        = & (A \cap \mathcal{C} B) \cap (C \cap \mathcal{C} D) = (A \cap C) \cap (\mathcal{C} B \cap \mathcal{C} D) \\
        = & (A \cap C) \cap \mathcal{C} ( B \cup D) = (A \cap C) \setminus (B \cup D)
        \end{align*}

    (2). 这是集合交、并运算的分配律。

    (3). 有

    .. math::

        \begin{align*}
        & A \setminus (B \setminus C) \\
        = & A \cap \mathcal{C} (B \cap \mathcal{C} C) = A \cap (\mathcal{C} B \cup C) \\
        = & (A \cap \mathcal{C} B) \cup (A \cap C) \subset (A \setminus B) \cup C
        \end{align*}

    (4). 有

    .. math::

        \begin{align*}
        & (A \setminus B) \setminus (C \setminus D) \\
        = & (A \cap \mathcal{C} B) \cap \mathcal{C}(C \cap \mathcal{C} D) = (A \cap \mathcal{C} B) \cap (\mathcal{C} C \cup D) \\
        = & (A \cap \mathcal{C} B \cap \mathcal{C} C) \cup (A \cap \mathcal{C} B \cap D) = ((A \cap \mathcal{C} B) \setminus C) \cup ((D \cap A) \setminus B) \\
        \subset & (A \setminus C) \cup (D \setminus B)
        \end{align*}

    (5). 等式的左边化为集合交、并的形式为

    .. math::
        :label: 1-5-left

        \begin{align*}
        & (A \setminus B) \cup C \\
        = & (A \cap \mathcal{C} B) \cup C = (A \cup C) \cap (\mathcal{C} B \cup C) \\
        = & (A \cap (\mathcal{C} B \cup C)) \cup (C \cap (\mathcal{C} B \cup C)) \\
        = & (A \cap (\mathcal{C} B \cup C)) \cup C
        \end{align*}

    等式的右边化为集合交、并的形式为

    .. math::
        :label: 1-5-right

        A \cap \mathcal{C} (B \cap \mathcal{C} C) = A \cap (\mathcal{C} B \cup C)

    比较式 :eq:`1-5-left` 与式 :eq:`1-5-right`, 若要使等式成立，必须有 :math:`(A \cap (\mathcal{C} B \cup C)) \cup C = A \cap (\mathcal{C} B \cup C)`,
    这要求 :math:`C \subset A \cap (\mathcal{C} B \cup C)`. 因为 :math:`C \subset \mathcal{C} B \cup C` 是显然的，故上式等价于 :math:`C \subset A`.

    (6). 不成立。因为集合 :math:`A` 是左边 :math:`A \cup (B \setminus C)` 的一个子集，但如果 :math:`A \cap C \neq \emptyset` 的话，
    集合 :math:`A` 不是右边 :math:`(A \cup B) \setminus C` 的子集。

3. 设给出集 :math:`E` 与任一集族 :math:`A_{\alpha}, \alpha \in I`, 问关系式

.. math::

    E \cup \bigcap_{\alpha \in I} A_{\alpha} = \bigcap_{\alpha \in I} (E \cup A_{\alpha})

是否恒成立？

.. proof:proof::

    首先证明左边包含于右边。任取 :math:`x \in E \cup \bigcap\limits_{\alpha \in I} A_{\alpha}`, 若 :math:`x \in E`,
    那么由于 :math:`E \subset E \cup A_{\alpha}, \forall \alpha \in I`, 从而有 :math:`x \in E \cup A_{\alpha}, \forall \alpha \in I`,
    那么有 :math:`x \in \bigcap\limits_{\alpha \in I} (E \cup A_{\alpha})`. 若 :math:`x \not\in E`, 那么 :math:`x \in \bigcap\limits_{\alpha \in I} A_{\alpha}`,
    从而 :math:`x \in E \cup A_{\alpha}, \forall \alpha \in I`, 所以 :math:`x \in \bigcap\limits_{\alpha \in I} (E \cup A_{\alpha})`.

    再证明右边包含于左边。任取 :math:`x \in \bigcap\limits_{\alpha \in I} (E \cup A_{\alpha})`, 那么 :math:`x \in E \cup A_{\alpha}, \forall \alpha \in I`.
    即对任意 :math:`\alpha \in I`, 或有 :math:`x \in E`, 或有 :math:`x \in A_{\alpha}`. 若 :math:`x \in E`, 那么 :math:`x \in E \cup \bigcap\limits_{\alpha \in I} A_{\alpha}`.
    若 :math:`x \not\in E`, 那么就必须有 :math:`x \in A_{\alpha}, \forall \alpha \in I`, 从而 :math:`x \in \bigcap\limits_{\alpha \in I} A_{\alpha}`, 这种情况下同样有
    :math:`x \in E \cup \bigcap\limits_{\alpha \in I} A_{\alpha}`.

5. 定义集 :math:`A, B` 的 **对称差** 为 :math:`A \triangle B = (A \setminus B) \cup (B \setminus A)`. 试证对任意集 :math:`A, B, C` 有

(1). :math:`A = B` 的充分必要条件为 :math:`A \triangle B = \emptyset`.

(2). :math:`A \cup B = (A \cap B) \cup (A \triangle B)`.

(3). :math:`A \triangle B \subset (A \triangle C) \cup (C \triangle B)`.

.. proof:proof::

    (1). :math:`A = B \Longleftrightarrow A \setminus B = \emptyset \land B \setminus A = \emptyset \Longleftrightarrow A \triangle B = (A \setminus B) \cup (B \setminus A) = \emptyset`.

    (2). 容易知道，对任意两个集合 :math:`A, B`, 总有 :math:`A \cup (B \setminus A) = A \cup B`, 于是有

    .. math::

        \begin{align*}
        & (A \cap B) \cup (A \triangle B) \\
        = & (A \cap B) \cup \Bigl((A \setminus B) \cup (B \setminus A)\Bigr) \\
        = & \Bigl(\bigl(A \cup (B \setminus A)\bigr) \cup (A \setminus B)\Bigr) \cap \Bigl(\bigl(B \cup (A \setminus B)\bigr) \cup (B \setminus A)\Bigr) \\
        = & \Bigl((A \cup B) \cup (A \setminus B)\Bigr) \cap \Bigl((B \cup A) \cup (B \setminus A)\Bigr) \\
        = & (A \cup B) \cap (B \cup A) \\
        = & A \cup B
        \end{align*}

    (3). 任取 :math:`x \in A \triangle B`, 要么有 :math:`x \in A \setminus (A \cap B)`, 要么有 :math:`x \in B \setminus (A \cap B)`,
    这两种情况有且只有一种成立。以下对 :math:`x` 是否属于集合 :math:`C` 分两种情况讨论。

    情况1. 若 :math:`x \not\in C`, 那么

        情况1.1. 若 :math:`x \in A \setminus (A \cap B)`, 那么此时有 :math:`(x \in A) \land (x \not\in C)`,
        即有 :math:`x \in A \setminus C \subset A \triangle C \subset (A \triangle C) \cup (C \triangle B)`.

        情况1.2. 若 :math:`x \in B \setminus (A \cap B)`, 那么此时有 :math:`(x \in B) \land (x \not\in C)`,
        即有 :math:`x \in B \setminus C \subset B \triangle C \subset (A \triangle C) \cup (C \triangle B)`.

    情况2. 若 :math:`x \in C`, 那么

        情况2.1. 若 :math:`x \in A \setminus (A \cap B)`, 那么此时有 :math:`(x \not \in B) \land (x \in C)`,
        即有 :math:`x \in C \setminus B \subset C \triangle B \subset (A \triangle C) \cup (C \triangle B)`.

        情况2.2. 若 :math:`x \in B \setminus (A \cap B)`, 那么此时有 :math:`(x \not \in A) \land (x \in C)`,
        即有 :math:`x \in C \setminus A \subset C \triangle A \subset (A \triangle C) \cup (C \triangle B)`.

    综上所述，对任意 :math:`x \in A \triangle B`, 总有 :math:`x \in (A \triangle C) \cup (C \triangle B)`,
    从而有 :math:`A \triangle B \subset (A \triangle C) \cup (C \triangle B)`.

6. 设 :math:`E_n = \left\{ m / n : m \in \mathbb{Z} \right\}, n \in \mathbb{N}`, 证明 :math:`\varliminf\limits_{n} E_n = \mathbb{Z}`,
:math:`\varlimsup\limits_{n} E_n = \mathbb{Q}`. 这里的 **上限集、下限集** 分别定义为
:math:`\varliminf\limits_{n} E_n = \bigcup\limits\limits_{k=1}^{\infty} \bigcap\limits_{n=k}^{\infty} E_n`, 以及
:math:`\varlimsup\limits_{n} E_n = \bigcap\limits\limits_{k=1}^{\infty} \bigcup\limits_{n=k}^{\infty} E_n`.

.. proof:proof::

    对任意 :math:`n \in \mathbb{N}`, 考虑 :math:`m \in n \mathbb{Z}`, 那么总有 :math:`\mathbb{Z} = \left\{ m / n : m \in n\mathbb{Z} \right\} \subset E_n`,
    从而有 :math:`\mathbb{Z} \subset \bigcap\limits_{n=1}^{\infty} E_n`,
    于是有 :math:`\mathbb{Z} \subset \bigcup\limits\limits_{k=1}^{\infty} \bigcap\limits_{n=k}^{\infty} E_n = \varliminf\limits_{n} E_n`.
    另一方面，任取 :math:`x \in \varliminf\limits_{n} E_n = \bigcup\limits\limits_{k=1}^{\infty} \bigcap\limits_{n=k}^{\infty} E_n`,
    那么存在 :math:`k \in \mathbb{N}`, 使得 :math:`x \in \bigcap\limits_{n=k}^{\infty} E_n`. 将 :math:`x = \dfrac{p}{q}, q > 0` 写为既约分数的形式,
    那么 :math:`\forall n \ge k, n \in \mathbb{N}`, 都有 :math:`x = \dfrac{p}{q} \in E_n = \left\{ m / n : m \in \mathbb{Z} \right\}`. 假设 :math:`q \neq 1`,
    那么取 :math:`n \in \mathbb{N}`, 使得 :math:`n > k` 且不被 :math:`q` 的某个素因子 :math:`p_0 > 1` 整除。那么由 :math:`\dfrac{p}{q} = \dfrac{m}{n}`,
    即 :math:`p n = q m`, 两边不可能有相同的素因子组 (例如 :math:`p_0` 不是左边的素因子，但是是右边的素因子)。所以 :math:`q \neq 1` 的假设不成立，也就是说
    :math:`\varliminf\limits_{n} E_n` 中任何元素写成既约分数的形式时，分母都是1，也就是说 :math:`\varliminf\limits_{n} E_n \subset \mathbb{Z}`.
    综上所述，有 :math:`\varliminf\limits_{n} E_n = \mathbb{Z}`.

    由于对任意 :math:`n \in \mathbb{N}`, 都有 :math:`E_n \subset \mathbb{Q}`, 于是 :math:`\bigcup\limits_{k=n}^{\infty} E_n \subset \mathbb{Q}`
    对任意 :math:`k \in \mathbb{N}` 成立，进而有
    :math:`\varlimsup\limits_{n} E_n = \bigcap\limits_{k=1}^{\infty} \bigcup\limits_{n=k}^{\infty} E_n \subset \mathbb{Q}`. 反过来，
    任取 :math:`x = \dfrac{p}{q} \in \mathbb{Q}, q > 0`, 并设其为既约分数。令 :math:`n = k \cdot q`, 那么有
    :math:`x = \dfrac{p}{q} = \dfrac{kp}{kq} = \dfrac{kp}{n} \in E_n = \left\{ m / n : m \in \mathbb{Z} \right\}`,
    这就证明了 :math:`x \in \bigcup\limits_{k=n}^{\infty} E_n` 对任意 :math:`k \in \mathbb{N}` 成立。那么有 :math:`\mathbb{Q} \subset \varlimsup\limits_{n} E_n`.
    综上所述，有 :math:`\varlimsup\limits_{n} E_n = \mathbb{Q}`.

    .. note::

        我们通常可将 :math:`E_n` 简写为 :math:`\dfrac{1}{n} \mathbb{Z}`, 那么这题的结论可以用数学符号更简洁地表达为

        .. math::

            \varliminf\limits_{n} \dfrac{1}{n} \mathbb{Z} = \mathbb{Z}, \quad \varlimsup\limits_{n} \dfrac{1}{n} \mathbb{Z} = \mathbb{Q}.


§2 映射·集的对等·可列集
------------------------------

8. 设 :math:`A = \{0, 1\}`, 试证一切排列

.. math::

    (a_1, a_2, \cdots, a_n, \cdots): \quad a_n \in A, n \in \mathbb{N}

所成之集的势为 :math:`\aleph`.

.. proof:proof::

    令集合 :math:`B = \{ (a_1, a_2, \cdots, a_n, \cdots): \ a_n \in A, n \in \mathbb{N} \}`, 以及集合
    :math:`B_0 = \{ (a_1, a_2, \cdots, a_n, \cdots) \in B: \ \exists n \in \mathbb{N}, s.t. \forall k \ge n, a_k = 1 \}`,
    并考虑映射

    .. math::

        f: B \setminus B_0 \to \mathbb{N}, \quad (a_1, a_2, \cdots, a_n, \cdots) \mapsto \sum_{n=1}^{\infty} a_n 2^n.

    以上映射给出了集合 :math:`B \setminus B_0` 与区间 :math:`[0, 1]` 之间的一一对应，而 :math:`B_0` 是可列集，所以集合 :math:`B = (B \setminus B_0) \cup B_0`
    也与区间 :math:`[0, 1]` 对等，从而它的势为 :math:`\aleph`.

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

        H(\dfrac{p}{q}) = \max \{ \lVert p \rVert, \lVert q \rVert \}, \quad
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

        可以通过显式表达式给出一一对应 :math:`\mathbb{N} \times \mathbb{N} \to \mathbb{N}`：

        .. math::

            s: \mathbb{N} \times \mathbb{N} \to \mathbb{N}, \quad (n_1, n_2) \mapsto \dfrac{(n_1 + n_2 - 2)(n_1 + n_2 - 1)}{2} + n_1.

    (2). 这题是课本 §2 的例1，做法如下：

    将 :math:`[0, 1]` 中的数写成二进制小数的形式 :math:`x = 0.x_1x_2 \cdots`, 相应的一一对应关系为

    .. math::

        [0, 1] \times [0, 1] \to [0, 1] : \quad (x, y) \mapsto z = 0.x_1y_1x_2y_2 \cdots

    由于约定了二进制小数不用 :math:`0.\cdots 0111\cdots` 的形式表示，需要检查的就只有通过上述映射得到的 :math:`z` 不具有这种形式，用反证法很容易证明这种情况不会发生。

10. 证明整系数多项式全体是可列的。

.. proof:proof::

    对于整系数多项式全体 :math:`\mathbb{Z}[X]` 有分解

    .. math::

        \mathbb{Z}[X] = \bigcup_{n=0}^{\infty} \mathbb{Z}_n[X], \quad \mathbb{Z}_n[X] = \{ f \in \mathbb{Z}[X]: \ \deg f = n \} \cong \mathbb{Z}^{n} \times \mathbb{Z}^{\ast},

    其中 :math:`\mathbb{Z}^{\ast} = \mathbb{Z} \setminus \{ 0 \}` (最高次项系数不为 :math:`0`). 由于 :math:`\mathbb{Z}^{n} \times \mathbb{Z}^{\ast}` 是可列集，
    所以 :math:`\mathbb{Z}_n[X]` 是可列集，从而 :math:`\mathbb{Z}[X]` 是可列集。

15. 设给定映射 :math:`f: X \to Y`. 试证对 :math:`Y` 中的任意集族 :math:`\{ B_{\alpha} \}_{\alpha \in I}` 有

.. math::

    \begin{gather*}
    f^{-1} \left( \bigcup_{\alpha \in I} B_{\alpha} \right) = \bigcup_{\alpha \in I} f^{-1} (B_{\alpha}), \quad
    f^{-1} \left( \bigcap_{\alpha \in I} B_{\alpha} \right) \subset \bigcap_{\alpha \in I} f^{-1} (B_{\alpha}), \\
    f^{-1} (\mathcal{C} B) = \mathcal{C} f^{-1} (B).
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

    若 :math:`f^{-1} (\mathcal{C} B) = \emptyset`, 即 :math:`\forall x \in X, f(x) \not\in \mathcal{C} B`, 那么有 :math:`\forall x \in X, f(x) \in B`,
    这意味着 :math:`f^{-1} (B) = X`, 于是有 :math:`\mathcal{C} f^{-1} (B) = \emptyset`. 若 :math:`f^{-1} (\mathcal{C} B) \neq \emptyset`,
    任取 :math:`x \in f^{-1} (\mathcal{C} B)`, 那么有 :math:`f(x) \in \mathcal{C} B`, 于是有 :math:`f(x) \not\in B`, 从而有
    :math:`x \not\in f^{-1} (B)`, 于是有 :math:`x \in \mathcal{C} f^{-1} (B)`. 反过来，任取 :math:`x \in \mathcal{C} f^{-1} (B)`,
    那么有 :math:`x \not\in f^{-1} (B)`, 于是有 :math:`f(x) \not\in B`, 从而有 :math:`f(x) \in \mathcal{C} B`, 于是有
    :math:`x \in f^{-1} (\mathcal{C} B)`. 综上所述，有 :math:`f^{-1} (\mathcal{C} B) = \mathcal{C} f^{-1} (B)`.

§3 一维开集、闭集及其性质
------------------------------

16. 证明任何点集的内点全体是开集。

.. proof:proof::

    令 :math:`\mathring{E} = \{ x \in E : \ x \text{ 为 } E \text{ 的内点} \}` 表示点集 :math:`E` 的内点全体。任取 :math:`x \in \mathring{E}`,
    由于 :math:`x` 为 :math:`E` 的内点，所以存在 :math:`x` 的邻域 :math:`U \subset E`. 任取 :math:`y \in U`, 那么 :math:`U` 也是 :math:`y` 的邻域，
    故 :math:`y` 也是 :math:`E` 的内点，从而有 :math:`y \in \mathring{E}`, 于是有 :math:`U \subset \mathring{E}`, 这就证明了 :math:`x` 是 :math:`\mathring{E}` 的内点。
    由于 :math:`x` 是任意取自 :math:`\mathring{E}` 的，所以 :math:`\mathring{E}` 是开集。

17. 设 :math:`f(x)` 是定义在 :math:`\mathbb{R}^1` 上只取整数值的函数，试证它的连续点集为开集，不连续点集为闭集。

.. proof:proof::

    任取 :math:`f` 的连续点 :math:`x_0`, 那么对 :math:`\varepsilon = \dfrac{1}{3}`, 存在 :math:`\delta > 0`, 使得 :math:`\forall x \in U(x_0, \delta)`,
    都有 :math:`\lvert f(x) - f(x_0) \rvert < \dfrac{1}{3}`. 由于 :math:`f` 只取整数值，此时必须有 :math:`f(x) = f(x_0)`. 考察集合 :math:`U(x_0, \delta / 3)`,
    任取 :math:`\tilde{x} \in U(x_0, \delta / 3)`, 有 :math:`U(\tilde{x}, \delta / 3) \subset \subset U(x_0, \delta)`, 从而有 :math:`f(\tilde{x}) = f(x_0)`,
    故 :math:`\tilde{x}` 也是 :math:`f` 的连续点。这就证明了集合 :math:`U(x_0, \delta / 3)` 包含于 :math:`f` 的连续点集中，从而 :math:`x_0` 是其内点。
    由于 :math:`x_0` 是任意取自 :math:`f` 的连续点集的，所以 :math:`f` 的连续点集是开集。

    :math:`f` 的连续点集的补集为 :math:`f` 的不连续点集，我们已经证明了前者是开集，所以后者是闭集。

.. _ex-1-18:

18. 设点集列 :math:`\{ E_k \}` 是有限区间 :math:`[a, b]` 中的渐缩列： :math:`E_1 \supset E_2 \supset \cdots \supset E_k \supset \cdots`,
且每个 :math:`E_k` 均为非空闭集，试证交集 :math:`\bigcap\limits_{k=1}^{\infty} E_k` 非空。

.. proof:proof::

    用反证法证明。取基本集为 :math:`\mathbb{R}`. 假设交集 :math:`\bigcap\limits_{k=1}^{\infty} E_k = \emptyset`, 那么考虑集族
    :math:`\{ \mathcal{C} E_k \}`, 这是闭区间 :math:`[a, b]` 的开覆盖，由于 :math:`[a, b]` 是紧集，所以存在有限子覆盖
    :math:`\{ \mathcal{C} E_{k_i} \}_{i=1}^{N}`, 即
    :math:`[a, b] \subset \bigcup\limits_{i=1}^{N} (\mathcal{C} E_{k_i}) = \mathcal{C} \left( \bigcap\limits_{i=1}^{N} E_{k_i} \right)`,
    此时必须有 :math:`\bigcap\limits_{i=1}^{N} E_{k_i} = \emptyset`, 否则其作为 :math:`[a, b]` 的子集非空，就不可能有
    :math:`[a, b] \subset \mathcal{C} \left( \bigcap\limits_{i=1}^{N} E_{k_i} \right)` 成立。于是有

    .. math::

        E_{k_N} = \bigcap_{i=1}^{N} E_{k_i} = \emptyset,

    这与题设矛盾。所以交集 :math:`\bigcap\limits_{k=1}^{\infty} E_k` 非空。

19. 设点集列 :math:`\{ E_k \}` 如 :ref:`上题<ex-1-18>`, :math:`f` 为 :math:`[a, b]` 上连续函数，
证明 :math:`f \left( \bigcap\limits_{k=1}^{\infty} E_k \right) = \bigcap\limits_{k=1}^{\infty} f(E_k)`.

.. proof:proof::

    任取 :math:`y \in f \left( \bigcap\limits_{k=1}^{\infty} E_k \right)`, 那么存在 :math:`x \in \bigcap\limits_{k=1}^{\infty} E_k`,
    使得 :math:`y = f(x)`. 由于 :math:`x \in \bigcap\limits_{k=1}^{\infty} E_k`, 所以 :math:`x \in E_k, \forall k \in \mathbb{N}`,
    这说明了 :math:`y = f(x) \in f(E_k), \forall k \in \mathbb{N}`, 从而有 :math:`y \in \bigcap\limits_{k=1}^{\infty} f(E_k)`.
    这样，我们就证明了 :math:`f \left( \bigcap\limits_{k=1}^{\infty} E_k \right) \subset \bigcap\limits_{k=1}^{\infty} f(E_k)`.

    反过来，任取 :math:`y \in \bigcap\limits_{k=1}^{\infty} f(E_k)`, 那么 :math:`y \in f(E_k), \forall k \in \mathbb{N}`, 于是存在
    :math:`x_k \in E_k`, 使得 :math:`y = f(x_k)`. 由于 :math:`\{ E_k \}` 是区间 :math:`[a, b]` 中的渐缩列，所以 :math:`\{ x_k \}` 是有界数列，
    从而存在收敛子列 :math:`\{ x_{k_i} \}`, 令 :math:`\lim\limits_{i \to \infty} x_{k_i} = x_0 \in [a, b]`. 由于 :math:`f` 在 :math:`[a, b]` 上连续，
    所以有 :math:`\lim\limits_{i \to \infty} f(x_{k_i}) = f(x_0)`, 于是有 :math:`y = f(x_0)`. 可以断言 :math:`x_0 \in \bigcap\limits_{k=1}^{\infty} E_k`,
    如若不然，那么存在 :math:`k_0 \in \mathbb{N}`, 使得 :math:`x_0 \not\in E_{k_0}`, 那么 :math:`x_0 \in \mathcal{C} E_{k_0}`.
    而 :math:`\mathcal{C} E_{k_0}` 是一个开集，所以存在 :math:`\varepsilon > 0`, 使得 :math:`U(x_0, \varepsilon) \subset \mathcal{C} E_{k_0}`,
    那么对任意 :math:`k \ge k_0`, 都有 :math:`U(x_0, \varepsilon) \subset \mathcal{C} E_{k_0} \subset \mathcal{C} E_k`, 于是有
    :math:`\lvert x_k - x_0 \rvert >= \varepsilon`, 这与 :math:`\{ x_k \}` 收敛到 :math:`x_0` 矛盾。所以有 :math:`x_0 \in \bigcap\limits_{k=1}^{\infty} E_k`.
    于是 :math:`y = f(x_0) \in f \left( \bigcap\limits_{k=1}^{\infty} E_k \right)`.
    这样，我们就证明了 :math:`\bigcap\limits_{k=1}^{\infty} f(E_k) \subset f \left( \bigcap\limits_{k=1}^{\infty} E_k \right)`.

    综上所述，有 :math:`f \left( \bigcap\limits_{k=1}^{\infty} E_k \right) = \bigcap\limits_{k=1}^{\infty} f(E_k)`.

21. 设 :math:`f(x)` 是 :math:`\mathbb{R}` 上实函数，映任一开集为开集，问它是否连续？又连续映射是否映开集为开集？

.. proof:solution::

    :math:`\mathbb{R} \to \mathbb{R}` 的开映射（将任一开集映为开集）不一定连续。反例如下：定义 :math:`\mathbb{R}` 上的一个等价关系为

    .. math::

        x \sim y \Leftrightarrow x - y \in \mathbb{Q}, \quad x, y \in \mathbb{R},

    并令 :math:`\mathcal{C} = \mathbb{R} / \sim` 表示商集，其中的元素记为

    .. math::
        :label: ex-1-21-eq-1

        [x] = \{ y \in \mathbb{R} : \ y \sim x \} = x + \mathbb{Q}

    :math:`x` 为代表元。可以验证，集合 :math:`\mathcal{C}` 与 :math:`\mathbb{R}` 对等， 那么可以做双射 :math:`f: \mathcal{C} \to \mathbb{R}`. 定义

    .. math::

        g: \mathbb{R} \to \mathbb{R}, \quad x \mapsto f([x]).

    任取 :math:`\mathbb{R}` 中开集 :math:`U`. 对值域 :math:`\mathbb{R}` 中的任意元素 :math:`y`, 令它在商集 :math:`\mathcal{C}` 中的双射 :math:`f` 下的原像为
    :math:`C \in \mathcal{C}`, 即 :math:`y = f(C)`. 由于每一个 :math:`C` 的形式都如 :eq:`ex-1-21-eq-1` 所示，所以满足 :math:`g(x) = y` 的 :math:`x`
    在 :math:`\mathbb{R}` 中稠密（包含 :math:`C` 作为陪集的每一个元素），故与开集 :math:`U` 相交非空，从而有 :math:`y \in g(U)`.
    由于 :math:`y` 是任意取自 :math:`\mathbb{R}` 的元素，所以 :math:`g(U) = \mathbb{R}`, 这就证明了 :math:`g` 将任一开集映为开集 :math:`\mathbb{R}`,
    同时这也说明了 :math:`g` 在任何一点都不连续。

    连续映射不一定将开集映为开集。反例为 :math:`f(x) = x^2`，它将开区间 :math:`(-1, 1)` 映左闭右开区间 :math:`[0, 1)`.

§4 开集的构造
------------------------------

23. 设 :math:`F_1, F_2` 为 :math:`\mathbb{R}^n` 中的闭集，其中之一有界，试证存在两点 :math:`a_1 \in F_1, a_2 \in F_2` 使 :math:`\rho(a_1, a_2) = \rho(F_1, F_2)`.

.. proof:proof::

    首先证明，对任意的 :math:`\mathbb{R}^n` 的子集 :math:`F`, 函数 :math:`\mathbb{R}^n \to \mathbb{R}: \ x \mapsto \rho(x, F)`
    是一致连续的：

        任取 :math:`a, b \in \mathbb{R}^n`, 由于 :math:`\rho (a, F) := \inf\limits_{x \in F} \rho(a, x)`, 那么 :math:`\forall \varepsilon > 0`,
        存在 :math:`x_0 \in F`, 使得 :math:`\rho(a, x_0) < \rho(a, F) + \varepsilon`, 于是有

        .. math::

            \rho(b, F) \le \rho(b, x_0) \le \rho(b, a) + \rho(a, x_0) < \rho(b, a) + \rho(a, F) + \varepsilon.

        由于 :math:`\varepsilon` 是任意的，所以有 :math:`\rho(b, F) \le \rho(b, a) + \rho(a, F)`. 同理可证 :math:`\rho(a, F) \le \rho(a, b) + \rho(b, F)`.
        所以有 :math:`\lvert \rho(a, F) - \rho(b, F) \rvert \le \rho(a, b)`. 那么对于任意取定的 :math:`\varepsilon > 0`, 取 :math:`\delta = \varepsilon`,
        只要 :math:`\rho(a, b) < \delta`, 就有 :math:`\lvert \rho(a, F) - \rho(b, F) \rvert < \varepsilon`.
        这就证明了函数 :math:`\mathbb{R}^n \to \mathbb{R}: \ x \mapsto \rho(x, F)` 是一致连续的。

    其次，我们证明，对任意点 :math:`a \in \mathbb{R}^n` 以及任意的非空闭集 :math:`F \subset \mathbb{R}^n`, 总存在 :math:`x_0 \in F`, 使得
    :math:`\rho(a, F) = \rho(a, x_0)`:

        考虑闭球 :math:`\overline{B} := \overline{B}(a, \delta)` 使得 :math:`\overline{B} \cap F \neq \emptyset`,
        那么 :math:`\overline{B} \cap F` 是 :math:`\mathbb{R}^n` 中有界闭集，且有 :math:`\rho(a, \overline{B} \cap F) = \rho(a, F)`.
        由于函数 :math:`\mathbb{R}^n \to \mathbb{R}: \ x \mapsto \rho(x, a)` 连续函数 (实际上进一步是初等函数)，所以它在有界闭集 :math:`\overline{B} \cap F` 上
        取到最小值，即存在 :math:`x_0 \in \overline{B} \cap F`, 使得 :math:`\rho(a, x_0) = \rho(a, \overline{B} \cap F) = \rho(a, F)`.

    有了以上两个结论，我们就可以证明题设结论。不妨设 :math:`F_1` 有界，考虑函数 :math:`\mathbb{R}^n \to \mathbb{R}: \ x \mapsto \rho(x, F_2)`.
    由之前第一点的结论，它是一致连续的，从而在有界闭集 :math:`F_1` 上取到最小值，即存在 :math:`a_1 \in F_1`, 使得 :math:`\rho(a_1, F_2) = \rho(F_1, F_2)`.
    又由于 :math:`F_2` 是非空闭集，根据第二点结论，存在 :math:`a_2 \in F_2`, 使得 :math:`\rho(a_1, F_2) = \rho(a_1, a_2)`. 于是有 :math:`\rho(a_1, a_2) = \rho(F_1, F_2)`.

24. 设 :math:`G_1, G_2` 为 :math:`\mathbb{R}^1` 中的开集，且 :math:`G_1 \subset G_2`. 试证 :math:`G_1` 的每个构成区间含于 :math:`G_2` 的某个构成区间之中。

.. proof:proof::

    任取 :math:`G_1` 的一个构成区间 :math:`I_1 = (a_1, b_1)`, 那么有 :math:`I_1 \subset G_1 \subset G_2`. 任取 :math:`x_0 \in I_1`,
    令它在 :math:`G_2` 中的构成区间为 :math:`I_2 = (a_2, b_2)`. 那么由构成区间的构造

    .. math::

        a_2 = \inf \{ x : \ (x, x_0) \subset G_2 \}, \quad b_2 = \sup \{ x : \ (x_0, x) \subset G_2 \}.

    又知道 :math:`(a_1, x_0) \subset I_1 \subset G_1 \subset G_2`, 所以 :math:`a_1 \in \{ x : \ (x, x_0) \subset G_2 \}`, 故有 :math:`a_1 \le a_2`.
    同理可证 :math:`b_1 \ge b_2`. 于是有 :math:`I_1 \subset I_2`.

26. 设 :math:`E` 为康托三分集的补集中构成区间的中点所成的集，求 :math:`E'`.

.. proof:solution::

    根据康托三分集的构造过程，有如下的区间列：

    .. math::

        \begin{align*}
        F_1 & = F_{11} \cup F_{12} = \left[ 0, \dfrac{1}{3} \right] \cup \left[ \dfrac{2}{3}, 1 \right], \\
        I_1 & = I_{11} = \left( \dfrac{1}{3}, \dfrac{2}{3} \right), \\
        F_2 & = F_{21} \cup F_{22} \cup F_{23} \cup F_{24} = \left[ 0, \dfrac{1}{9} \right] \cup
                \left[ \dfrac{2}{9}, \dfrac{1}{3} \right] \cup \left[ \dfrac{2}{3}, \dfrac{7}{9} \right]
                \cup \left[ \dfrac{8}{9}, 1 \right], \\
        I_2 & = I_{21} \cup I_{22} = \left( \dfrac{1}{9}, \dfrac{2}{9} \right) \cup \left( \dfrac{7}{9}, \dfrac{8}{9} \right), \\
        & \vdots \\
        F_n & = F_{n1} \cup F_{n2} \cup \cdots \cup F_{n2^{n}}, \\
        I_n & = I_{n1} \cup I_{n2} \cup \cdots \cup I_{n2^{n-1}}, \\
        & \vdots \\
        G_0 & = \bigcup_{n=1}^{\infty} I_n, \\
        P_0 & = \mathcal{C} G_0 = \bigcap_{n=1}^{\infty} F_n \longleftarrow \text{(康托三分集)}. \\
        \end{align*}

    康托三分集的补集即为 :math:`G_0`, 其构成区间为 :math:`I_n`, 集合 :math:`E` 即由这些构成区间的中点所成的集。

    任取康托三分集中的点 :math:`x \in P_0 = \bigcap\limits_{n=1}^{\infty} F_n`, 那么 :math:`x \in F_n, \forall n \in \mathbb{N}` 成立。
    对任意 :math:`\varepsilon > 0`, 取 :math:`n \in \mathbb{N}`, 使得 :math:`\dfrac{1}{3^{n}} < \varepsilon`,
    那么 :math:`x \in F_n`, 从而存在 :math:`k \in \{ 1, 2, \dots, 2^n \}`, 使得 :math:`x \in F_{nk}`. 闭区间 :math:`F_{nk}` 的长度为
    :math:`\dfrac{1}{3^{n}}`, 所以 :math:`\forall y \in F_{nk}`, 都有 :math:`\lvert x - y \rvert \le \varepsilon`. 同时，
    闭区间 :math:`F_{nk}` 包含了 :math:`I_{n+1}` 中的某个开区间 :math:`I_{n+1, k}, 1 \le k \le 2^{n}`
    (即第 :math:`n+1` 步从闭区间 :math:`F_{nk}` 中去除的中间 :math:`\dfrac{1}{3}` 开区间)，进而包含了 :math:`I_{n+1, k}` 的中点，
    记其为 :math:`y_0`, 那么有 :math:`0 < \lvert x - y_0 \rvert < \varepsilon`, 即 :math:`y_0 \in \mathring{U}(x, \varepsilon) \cap E`.
    这就证明了 :math:`x \in P_0` 是 :math:`E` 的聚点。所以有 :math:`E' \supset P_0`.

    反过来，任取 :math:`x \not\in P_0`, 即有 :math:`x \in G_0 = \bigcup\limits_{n=1}^{\infty} I_n`,
    那么存在 :math:`n \in \mathbb{N}`, 使得 :math:`x \in I_n`, 从而存在 :math:`k \in \{ 1, 2, \dots, 2^{n-1} \}`,
    使得 :math:`x \in I_{nk}`. 如果 :math:`x` 是 :math:`I_{nk}` 的中点，那么取 :math:`\varepsilon = \dfrac{1}{3^{n+1}}`,
    即有 :math:`\mathring{U}(x, \varepsilon) \subset I_{nk} \setminus \{ x \}`, 从而 :math:`\mathring{U}(x, \varepsilon) \cap E = \emptyset`,
    这说明了 :math:`x` 不是 :math:`E` 的聚点。如果 :math:`x` 不是 :math:`I_{nk}` 的中点，令 :math:`y_0` 为 :math:`I_{nk}` 的中点，
    那么取 :math:`\varepsilon = \min \left\{ \dfrac{1}{3^{n+1}}, \dfrac{1}{2} \lvert x - y_0 \rvert \right\}`, 这样，去心邻域 :math:`\mathring{U}(x, \varepsilon)`
    既不包含 :math:`y_0`, 也不会与 :math:`F_n` 中含有的与 :math:`I_{nk}` 相邻的任何一个闭区间的中间 :math:`\dfrac{1}{3}` 开区间相交，
    这样就有 :math:`\mathring{U}(x, \varepsilon) \cap E = \emptyset`, 也说明了 :math:`x` 不是 :math:`E` 的聚点。于是我们就证明了
    :math:`\mathcal{C} P_0 \cap E' = \emptyset`, 从而有 :math:`E' \subset P_0`.

    综上所述，有 :math:`E' = P_0`.

\*§5 集的势·序集
------------------------------

无。
