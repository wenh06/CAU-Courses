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
    任取 :math:`\tilde{x} \in U(x_0, \delta / 3)`, 有 :math:`U(\tilde{x}, \delta / 3) \subset U(x_0, \delta)`, 从而有 :math:`f(\tilde{x}) = f(x_0)`,
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
