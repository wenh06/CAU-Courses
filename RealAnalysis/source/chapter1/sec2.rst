§2 映射·集的对等·可列集
------------------------------

.. _ex-1-7:

7. 试作下列各题中集之间的一一对应：

(1). :math:`[0, 1)` 与 :math:`(0, 1)`;

(2). :math:`[a, b]` 与 :math:`(-\infty, +\infty)`;

(3). 开区间 :math:`(0, 1)` 与 无理数集;

(4). 开上半平面与开单位圆;

(5). :math:`\mathbb{N}^2` 与 :math:`\mathbb{N}`.

.. proof:solution::

    (1). 由于 :math:`(0, 1)` 中有理数是可列的，记为 :math:`\{ r_1, r_2, \dots, r_n, \dots \}`, 记 :math:`r_0 = 0`, 那么可以通过如下的映射给出一一对应：

    .. math::

        f: [0, 1) \to (0, 1), \quad x \mapsto \begin{cases}
        r_{n}, & x = r_{n-1}, n \in \mathbb{N}, \\
        x, & x \in (0, 1) \setminus \mathbb{Q}.
        \end{cases}

    (2). 闭区间 :math:`[a, b]` 与 :math:`[0, 1]` 可以通过映射 :math:`f: x \mapsto \dfrac{x - a}{b - a}` 得到一一对应。
    另一方面，:math:`(-\infty, +\infty)` 与 :math:`(0, 1)` 可以通过映射 :math:`g: x \mapsto \dfrac{1 + \tanh x}{2}` 得到一一对应。
    再利用类似 (1) 中的方法，可以构造 :math:`[0, 1]` 与 :math:`(0, 1)` 的一一对应 :math:`\varphi`,
    那么复合映射 :math:`g^{-1} \circ \varphi \circ f` 就给出了 :math:`[a, b]` 与 :math:`(-\infty, +\infty)` 的一一对应。

    (3). 由于 :math:`g(x) = \dfrac{1 + \tanh x}{2}` 给出了 :math:`\mathbb{R}` 到 :math:`(0, 1)` 的一一对应，
    所以我们只要给出 :math:`\mathbb{R}` 与无理数集 :math:`\mathbb{R} \setminus \mathbb{Q}` 的一一对应即可。
    记集 :math:`A = \mathbb{Q} + \sqrt{2} = \{ r + \sqrt{2} : \ r \in \mathbb{Q} \} = \{ a_1, a_2, \dots, a_n, \dots \}`,
    那么集 :math:`A` 是可列集且 :math:`A \cap \mathbb{Q} = \emptyset`. 记 :math:`\mathbb{Q} = \{ r_1, r_2, \dots, r_n, \dots \}`,
    那么可以通过如下的映射给出一一对应：

    .. math::

        f: \mathbb{R} \rightarrow \mathbb{R} \setminus \mathbb{Q}, \quad x \mapsto \begin{cases}
        x, & x \in \mathbb{R} \setminus (\mathbb{Q} \cup A), \\
        a_{2n-1}, & x = r_n, n \in \mathbb{N}, \\
        a_{2n}, & x = a_n, n \in \mathbb{N}.
        \end{cases}

    (4). 记 :math:`\mathbb{H} = \{ (x, y) \in \mathbb{R}^2 : \ y > 0 \}` 为开上半平面，
    :math:`\mathbb{D} = \{ (x, y) \in \mathbb{R}^2 : \ x^2 + y^2 < 1 \}` 为开单位圆。
    我们将 :math:`\mathbb{D}` 分为三个部分

        :math:`\mathbb{D}_1 = \{ (x, y) \in \mathbb{D} : \ y < 0 \}`,

        :math:`\mathbb{D}_2 = \{ (x, y) \in \mathbb{D} : \ y > 0 \}`,

        :math:`\mathbb{D}_3 = \{ (x, y) \in \mathbb{D} : \ y = 0 \}`.

    类似地，我们将 :math:`\mathbb{H}` 分为三个部分

        :math:`\mathbb{H}_1 = \mathbb{D}_2 = \{ (x, y) \in \mathbb{H} : \ x^2 + y^2 < 1 \}`,

        :math:`\mathbb{H}_2 = \{ (x, y) \in \mathbb{H} : \ x^2 + y^2 > 1 \}`,

        :math:`\mathbb{H}_3 = \{ (x, y) \in \mathbb{H} : \ x^2 + y^2 = 1 \}`.

    我们给出对应部分之间的一一映射：

        :math:`\mathbb{D}_1 \to \mathbb{H}_1: \quad (x, y) \mapsto (x, -y)`,

        :math:`\mathbb{D}_2 \to \mathbb{H}_2: \quad (r, \theta) \mapsto (1/r, \theta)` (注意，这里是极坐标),

        :math:`\mathbb{D}_3 \to \mathbb{H}_3: \quad (x, 0) \mapsto (x, \sqrt{1 - x^2})`.

    另解：将 :math:`\mathbb{R}^2` 与 :math:`\mathbb{C}` 对等，那么 :math:`\mathbb{D} = \{ z \in \mathbb{C} : \ \lvert z \rvert < 1 \}` 到
    :math:`\mathbb{H} = \{ z \in \mathbb{C} : \ \mathfrak{Im} (z) > 0 \}` 的一一对应可以通过 Möbius 变换给出：

    .. math::

        f: \mathbb{D} \rightarrow \mathbb{H}, ~ z \mapsto i \dfrac{1 + z}{1 - z}.

    (5). :math:`f: \mathbb{N}^2 \rightarrow \mathbb{N}: \quad (m, n) \mapsto 2^{m-1} (2n - 1)`, 或者

        .. math::

            f: \mathbb{N}^2 \rightarrow \mathbb{N}: \quad (m, n) \mapsto \dfrac{(m + n - 2)(m + n - 1)}{2} + m.

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

    以上映射给出了集合 :math:`B \setminus B_0` 与区间 :math:`[0, 1]` 之间的一一对应，而 :math:`B_0` 是可列集，
    所以集合 :math:`B = (B \setminus B_0) \cup B_0` 也与区间 :math:`[0, 1]` 对等 [1]_ ，从而它的势为 :math:`\aleph`.

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

        见 :ref:`习题1.7 <ex-1-7>`.

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

.. _ex-1-11:

11. 设用 :math:`C[0, 1]` 表示 :math:`[0, 1]` 上的一切连续函数所成的集，试证它的势为 :math:`\aleph`.

.. proof:proof::

    :math:`[0, 1]` 上常值函数全体与 :math:`\mathbb{R}` 对等，而且是 :math:`C[0, 1]` 的真子集。
    另一方面，:math:`[0, 1]` 上的任一连续函数 :math:`f` 完全由它在所有有理点上的取值决定，于是 :math:`C[0, 1]` 与 :math:`\mathbb{R}^{\mathbb{N}}` 的真子集对等。
    这里是真子集是因为需要排除不能对应于连续函数的实数列，例如设 :math:`a_1, a_2, \dots` 是 :math:`[0, 1]` 上的一个收敛到 :math:`\frac{\sqrt{2}}{2}` 的有理数数序列，
    相应的值 :math:`f(a_n) = (-1)^n` 不能对应于任何连续函数。于是 :math:`C[0, 1]` 与 :math:`\mathbb{R}^{\mathbb{N}}` 的真子集对等。
    由 Cantor-Bernstein 定理，有 :math:`C[0, 1]` 与 :math:`\mathbb{R}` 对等，从而它的势为 :math:`\aleph`.

    这里，我们还需要说明 :math:`\mathbb{R}^{\mathbb{N}}` 与 :math:`\mathbb{R}` 对等，或者等价地， :math:`(0, 1)^{\mathbb{N}}` 与 :math:`(0, 1)` 对等：

    .. math::

        (0.a_{11}a_{12}a_{13} \cdots, 0.a_{21}a_{22}a_{23} \cdots, \dots) \mapsto 0.a_{11}a_{12}a_{21}a_{13}a_{22}a_{31} \cdots.

.. _ex-1-12:

12. 设用 :math:`M` 表示 :math:`(-\infty, +\infty)` 上一切单调函数所成的集，试讨论它的势。

.. proof:solution::

    任一单调函数 :math:`f` 至多有可数个间断点，而且每个间断点都是第一类间断点，所以单调函数 :math:`f` 可以表示为 :math:`f = f_1 + f_2`, 其中 :math:`f_1` 是连续函数，
    :math:`f_2` 是有至多可数个第一类间断点的阶跃函数。:math:`f_2` 完全由间断点的值以及相应的阶跃的量决定，所以可视为
    :math:`\mathbb{R}^{\mathbb{N}} \times \mathbb{R}^{\mathbb{N}}` 的一个元素，故其全体具有势 :math:`\aleph`.
    再结合 :ref:`上题 <ex-1-11>` 的结论，有 :math:`M` 的势为 :math:`\aleph`.

.. _ex-1-13:

13. 设 :math:`A` 是势大于 :math:`1` 的集，:math:`A` 上的一一映射称为 :math:`A` 的置换. 试证存在 :math:`A` 的一个置换 :math:`f` 使对一切 :math:`x \in A`, :math:`f(x) \neq x`.

..
    https://math.stackexchange.com/a/1383804/692822
    https://math.stackexchange.com/q/56466/692822
    https://math.stackexchange.com/q/134152/692822

.. proof:solution::

    若 :math:`A` 是有限集, 记为 :math:`A = \{ a_0, a_2, \dots, a_{n-1} \}`, :math:`n > 1`,
    那么 :math:`a_{k} \mapsto a_{k + 1} \mod n` 就是一个满足条件的置换。以下我们考虑 :math:`A` 是无限集的情况。

    由于 :math:`A` 为无限集，那么 :math`A` 与 :math:`A \times \mathbb{F}_2` 对等，其中 :math:`\mathbb{F}_2 = \{ \bar{0}, \bar{1} \}`
    (此结论非平凡), 即有双射 :math:`\varphi: A \to A \times \mathbb{F}_2`. 容易看出

    .. math::

        g: A \times \mathbb{F}_2 \rightarrow A \times \mathbb{F}_2, \quad (x, y) \mapsto (x, y + 1 \mod 2)

    是一个没有不动点的置换，从而复合映射 :math:`f = \varphi^{-1} \circ g \circ \varphi` 就是集 :math:`A` 的一个没有不动点的置换。

    .. note::

        利用选择公理 (或者 Zorn 引理) 的证明方法：考虑集 :math:`A` 的所有满足如下条件的子集族

        .. math::

            \{ S_i \}_{i \in I}: \quad S_i \subset A, \quad \lvert S_i \rvert = 2, \quad \forall i \in I; \quad S_i \cap S_j = \emptyset, \quad i \neq j.

        由包含关系定义偏序关系，那么任一全序子集都是上界，从而根据 Zorn 引理，存在极大元素 :math:`\mathcal{S} = \{ S_i \}_{i \in I}`.
        那么 :math:`\bigcup_{i \in I} S_i` 要么等于 :math:`A`，要么等于 :math:`A \setminus \{ x \}`，其中 :math:`x` 是 :math:`A` 中的一个元素。
        由于 :math:`A` 与 :math:`A \setminus \{ x \}` 对等，所以只要对 :math:`\bigcup_{i \in I} S_i = A` 的情况证明即可。
        记 :math:`S_i = \{ a_{i0}, a_{i1} \}`, 那么可以通过如下的映射给出一个没有不动点的置换：

        .. math::

            f: A \to A, \quad a_{ij} \mapsto a_{i (j+1 \mod 2)}.

        其实，以上我们 (利用选择公理) 也证明了 :math:`A` 与 :math:`A \times \mathbb{F}_2` 对等。
        但是要注意的是，

            每一个无限集 :math:`A` 都与 :math:`A \times \mathbb{F}_2` 对等

        要严格弱于选择公理，即不能从这个结论推出选择公理。

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

.. rubric:: 注

.. [1] 这是根据本节例1的结论得到的：“设集 :math:`A` 与 :math:`[0, 1]` 对等， :math:`B` 是可列集，则 :math:`A \cup B` 与 :math:`A \setminus B` 均与 :math:`[0, 1]` 对等。”
