§4 关于测度的几点评注
------------------------------------------

24. 设 :math:`E` 是一维有界集， :math:`I_1, I_2, \dots` 是任意区间集列（可以相交），其并覆盖 :math:`E`, 试证

.. math::

    m^*(E) = \inf\limits_{\cup I_k \supset E} \sum\limits_{k=1}^\infty l(I_n).

对于二维情形如何？

.. proof:proof::

    待写

25. 设 :math:`Q` 是 :math:`\mathbb{R}^2` 中的单位正方形 :math:`[0,1;0,1]`, :math:`\{E_n\}_{n \in \mathbb{N}}` 是 :math:`Q` 中的可测集列，
且数列 :math:`\{m E_n \}_{n \in \mathbb{N}}` 有聚点 :math:`1`, 证明存在子列 :math:`\{E_{n_k}\}_{k \in \mathbb{N}}` 使
:math:`m \left( \bigcap\limits_{k=1}^\infty E_{n_k} \right) > 0`.

.. proof:proof::

    待写

27. 设 :math:`E` 是 :math:`\mathbb{R}` 中的可测集，证明 :math:`D(E) = \left\{ (x,y) \in \mathbb{R}^2 : x-y \in E \right\}` 是 :math:`\mathbb{R}^2` 中的可测集。

.. proof:proof::

    待写

29. 设 :math:`E` 为 :math:`(0, 1)` 中正测度子集且存在常数 :math:`c > 0` 使对 :math:`(0, 1)` 中的变动区间 :math:`I` 有
:math:`\lim\limits_{m I \to 0} m(E \cap I) / m I = c`, 证明 :math:`m E = c`.

.. proof:proof::

    待写

30. 设 :math:`\{E_n\}_{n \in \mathbb{N}}` 为 :math:`\mathbb{R}` 中互不相交的集列，满足条件
:math:`m^* \left( \bigcup\limits_{n=1}^\infty E_n \right) < \sum\limits_{n=1}^\infty m^* (E_n)`,
证明存在最小的自然数 :math:`N` 使得 :math:`m^* \left( \bigcup\limits_{n=1}^N E_n \right) < \sum\limits_{n=1}^N m^* (E_n)`,
并且此时 :math:`E_N` 是不可测的。

.. proof:proof::

    待写

33. 设 :math:`E` 为 :math:`\mathbb{R}^n` 中任一子集， :math:`\alpha` 为给定正数。对任意的 :math:`\varepsilon > 0`, 令

.. math::

    H_{\alpha, \varepsilon} (E) = \inf \sum_k d (E_k)^{\alpha},

其中 :math:`d (E_k)` 表示 :math:`E_k` 的直径，下确界对一切满足 :math:`E \subset \bigcup\limits_{k} E_k`
而 :math:`d (E_k) < \varepsilon, k \in \mathbb{N}` 的集列 :math:`\{E_k\}` 而取。再令

.. math::

    H_{\alpha} (E) = \lim\limits_{\varepsilon \to 0} H_{\alpha, \varepsilon} (E) = \sup\limits_{\varepsilon > 0} H_{\alpha, \varepsilon} (E).

试证 :math:`H_{\alpha}` 为基本集 :math:`\mathbb{R}^n` 上的外测度并满足条件： 若 :math:`H_{\alpha} (E) < \infty`,
则当 :math:`\beta > \alpha` 时， :math:`H_{\beta} (E) = 0`.

:math:`H_{\alpha}` 称为 :math:`E` 的带指标 :math:`\alpha` 的豪斯多夫 (Hausdorff) 测度。

.. proof:proof::

    待写

34. 设 :math:`r` 为给定的正数， :math:`a, b` 为正的常数. :math:`\mathbb{R}^n` 中子集列 :math:`V_1, V_2, \dots` 满足条件：
每个 :math:`V_k` 中含有半径 :math:`ar` 的一个球且其直径 :math:`d(V_k) \le br`.
试证任一球 :math:`B(z, r)` 与 :math:`\{\overline{V}_k\}` 中元素相交的个数小于或等于 :math:`(1+b)^n a^{-n}`.

.. proof:proof::

    待写

35. 设 :math:`f` 为集 :math:`X \to Y` 的任一映射， :math:`\mathcal{A}, \mathcal{B}` 分别为 :math:`X, Y` 中的 :math:`\sigma` 代数，证明

.. math::

    \{ f^{-1} (B) : B \in \mathcal{B} \}, \quad \{B : f^{-1} (B) \in \mathcal{A} \}

分别为 :math:`X, Y` 中的 :math:`\sigma` 代数。

36. 设 :math:`\mathcal{A}` 为由 :math:`\mathbb{R}` 中的一切这样的可测集 :math:`E` 构成：
或者 :math:`m E = 0` 或者 :math:`m \mathcal{C} E = 0`. 试证 :math:`\mathcal{A}` 为 :math:`\mathbb{R}` 中的 :math:`\sigma` 代数。

.. proof:proof::

    待写
