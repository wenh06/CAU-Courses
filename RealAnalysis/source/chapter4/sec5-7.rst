§5-7 乘积测度与 Fubini 定理、微分与积分、RS 积分
------------------------------------------------------------------------

.. _ex-4-27:

27. 设 :math:`f(x), g(x)` 分别是定义在集 :math:`X, Y` 上的 :math:`\mu, \nu` 可积函数。证明

.. math::

    h(x, y) = f(x) g(y)

是乘积空间 :math:`X \times Y` 上的可积函数，且有

.. math::

    \int_{X \times Y} h \mathrm{d} (\mu \times \nu) = \int_X f \mathrm{d} \mu \int_Y g \mathrm{d} \nu.

.. proof:proof::

    首先，由于 :math:`f(x), g(x)` 分别是定义在集 :math:`X, Y` 上的 :math:`\mu, \nu` 可积函数，从而可测，
    所以 :math:`h(x, y) = f(x) g(y)` 是乘积空间 :math:`X \times Y` 上的可测函数。

    接下来，需要证明 :math:`\int_{X \times Y} h \mathrm{d} (\mu \times \nu) < \infty`.
    这等价于 :math:`\int_{X \times Y} \lvert h \rvert \mathrm{d} (\mu \times \nu) < \infty`.
    由 :ref:`Tonelli 定理 <thm-tonelli>` 知

    .. math::

        \int_{X \times Y} \lvert h \rvert \mathrm{d} (\mu \times \nu) & = \int_X \left( \int_Y \lvert h(x, y) \rvert \mathrm{d} \nu \right) \mathrm{d} \mu = \int_X \left( \int_Y \lvert f(x) g(y) \rvert \mathrm{d} \nu \right) \mathrm{d} \mu \\
        & = \int_X \lvert f(x) \rvert \left( \int_Y \lvert g(y) \rvert \mathrm{d} \nu \right) \mathrm{d} \mu = \int_X \lvert f(x) \rvert \mathrm{d} \mu \int_Y \lvert g(y) \rvert \mathrm{d} \nu < \infty.

    于是 :math:`h(x, y) = f(x) g(y)` 是乘积空间 :math:`X \times Y` 上的可积函数。

    .. note::

        本题结论即为所谓的 Fubini-Tonelli 定理。

.. _ex-4-28:

28. 设 :math:`(X, \mathscr{R}, \mu), (Y, \mathscr{S}, \nu)` 为对应于勒贝格测度的单位区间这样的测度空间， :math:`E` 是 :math:`X \times Y` 中是和下述条件的集：
对每个 :math:`x` 与每个  :math:`y`, :math:`E_x` 与 :math:`X \setminus E^y` 均为可列集。证明 :math:`E` 是不可测的。

.. proof:proof::

    假设 :math:`E` 可测，那么

    .. math::

        1 = m ([0, 1] \times [0, 1]) \geqslant m (E) = \int_{X \times Y} \chi_E \mathrm{d} (\mu \times \nu),

    即 :math:`\chi_E` 是 :math:`E` 上的可积函数，从而由 Fubini 定理知

    .. math::

            \int_X \nu(E_x) \mathrm{d} \mu = \int_X \left( \int_Y \chi_{E_x} \mathrm{d} \nu \right) \mathrm{d} \mu = \int_{X \times Y} \chi_E \mathrm{d} (\mu \times \nu) = int_Y \left( \int_X \chi_{E^y} \mathrm{d} \mu \right) \mathrm{d} \nu = \int_Y \mu (E^y) \mathrm{d} \nu.

    由于对每个 :math:`x` 与每个  :math:`y`, :math:`E_x` 与 :math:`X \setminus E^y` 均为可列集，而可列集都是零测集，
    所以 :math:`\nu(E_x) = 0`, :math:`\mu(E^y) = m(X) = 1`, 从而有

    .. math::

        \int_X \nu(E_x) \mathrm{d} \mu & = \int_X 0 \mathrm{d} \mu = 0, \\
        \int_Y \mu(E^y) \mathrm{d} \nu & = \int_Y 1 \mathrm{d} \nu = 1,

    这与上式矛盾，所以 :math:`E` 不可测。

.. _ex-4-30:

30. 设 :math:`\theta(x)` 为区间 :math:`[0, 1]` 上的 Cantor 函数，令 :math:`f(x) = \theta(x) + x`, :math:`0 \leqslant x \leqslant 1`;
:math:`g = f^{-1}`. 试证：

(1). 存在可测集 :math:`B` 使 :math:`g^{-1}(B)` 不可测；

(2). :math:`g^{-1}` 映不可测集为不可测集。

.. proof:proof::

    有如下的互逆的连续一一映射

    .. math::

        [0, 1] \overset{f}{\underset{g}\rightleftarrows} [0, 2]

    (1). 任取 :math:`[0, 1]` 上 Cantor 三分集 :math:`P_0` 的补集 :math:`G_0` 的构成区间 :math:`I = (a, b)`,
    Cantor 函数 :math:`\theta` 在 :math:`I` 上为常值函数，因此 :math:`f(I) = (a + \theta(a), b + \theta(b))`.
    于是有 :math:`m (f(I)) = b - a = m I`, 且 :math:`f(G_0)` 为构成区间为 :math:`f(I)` 的开集，从而可测。
    依据测度的可列可加性，有

    .. math::

        m (f(G_0)) = \sum_{n = 1}^\infty m (f(I_n)) = \sum_{n = 1}^\infty m (I_n) = m (G_0) = 1

    成立，从而知

    .. math::

        m (f (P_0)) = m ([0, 2]) - m (f (G_0)) = 2 - 1 = 1.

    于是可以从正测度集 :math:`f (P_0)` 中取出不可测集 :math:`B_0`, 并令 :math:`B = g (B_0) = f^{-1} (B_0) \subset P_0`.
    由于 :math:`P_0` 是零测集，所以它的子集 :math:`B` 也是零测集，从而是可测集。而 :math:`g^{-1} (B) = B_0` 不可测。

    (2). 任取 :math:`[0, 1]` 区间内的不可测集 :math:`E`, 假设 :math:`g^{-1} (E) = f (E)` 可测。未写完。。。。

.. _ex-4-34:

34. 设 :math:`\{ f_n \}` 为 :math:`[a, b]` 上有界变差函数列， :math:`f_n` 收敛于一有限函数 :math:`f` (当 :math:`n \to \infty`),
且有 :math:`\displaystyle \bigvee_a^b (f_n) \leqslant K`, :math:`K` 为常数 (:math:`n \in \mathbb{N}`)。证明 :math:`f` 也是有界变差函数。

.. proof:proof::

    待写。

.. _ex-4-35:

35. 若函数 :math:`f` 在 :math:`[a, b]` 上绝对连续，且几乎处处存在非负导数，证明 :math:`f` 为增函数。

.. proof:proof::

    由于函数 :math:`f` 在 :math:`[a, b]` 上绝对连续，所以存在 :math:`[a, b]` 上可积函数 :math:`g` 使得

    .. math::

        f(x) = f(a) + \int_{[a, x]} g \mathrm{d} m, \quad x \in [a, b],

    并且 :math:`f'(x) = g(x)` 几乎处处成立。由于函数 :math:`f` 在 :math:`[a, b]` 上几乎处处存在非负导数，即 :math:`f'(x) = g(x)` 几乎处处非负，
    所以对任意 :math:`x_1 < x_2 \in [a, b]`, 有 :math:`\displaystyle \int_{[x_1, x_2]} g \mathrm{d} m \geqslant 0`, 从而知

    .. math::

        f(x_2) - f(x_1) = \int_{[x_1, x_2]} g \mathrm{d} m \geqslant 0,

    这就证明了 :math:`f` 是增函数。

.. _ex-4-38:

38. 证明 Vitali 引理对有有限测度的无界集成立。

.. proof:proof::

    待写。
