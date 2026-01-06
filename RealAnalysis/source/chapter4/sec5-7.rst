§5-7 乘积测度与 Fubini 定理、微分与积分、RS 积分
------------------------------------------------------------------------

.. _ex-4-27:

27. 设 :math:`f(x), g(x)` 分别是定义在集 :math:`X, Y` 上的 :math:`\mu, \nu` 可积函数. 证明

    .. math::
      h(x, y) = f(x) g(y)

    是乘积空间 :math:`X \times Y` 上的可积函数, 且有

    .. math::
      \int_{X \times Y} h ~ \mathrm{d} (\mu \times \nu) = \int_X f ~ \mathrm{d} \mu \int_Y g ~ \mathrm{d} \nu.

.. proof:proof::

   首先, 由于 :math:`f(x), g(x)` 分别是定义在集 :math:`X, Y` 上的 :math:`\mu, \nu` 可积函数, 从而可测,
   所以 :math:`h(x, y) = f(x) g(y)` 是乘积空间 :math:`X \times Y` 上的可测函数.

   接下来, 需要证明 :math:`\int_{X \times Y} h ~ \mathrm{d} (\mu \times \nu) < \infty`.
   这等价于 :math:`\int_{X \times Y} \lvert h \rvert ~ \mathrm{d} (\mu \times \nu) < \infty`.
   由 :ref:`Tonelli 定理 <thm-tonelli>` 知

   .. math::
      \int_{X \times Y} \lvert h \rvert ~ \mathrm{d} (\mu \times \nu)
      & = \int_X \left( \int_Y \lvert h(x, y) \rvert ~ \mathrm{d} \nu \right) ~ \mathrm{d} \mu
        = \int_X \left( \int_Y \lvert f(x) g(y) \rvert ~ \mathrm{d} \nu \right) ~ \mathrm{d} \mu \\
      & = \int_X \lvert f(x) \rvert \left( \int_Y \lvert g(y) \rvert ~ \mathrm{d} \nu \right) ~ \mathrm{d} \mu
        = \int_X \lvert f(x) \rvert ~ \mathrm{d} \mu \int_Y \lvert g(y) \rvert ~ \mathrm{d} \nu < \infty.

   于是 :math:`h(x, y) = f(x) g(y)` 是乘积空间 :math:`X \times Y` 上的可积函数.

   .. note::
      本题结论即为 Fubini-Tonelli 定理的一种特殊情形.

.. _ex-4-28:

28. 设 :math:`(X, \mathscr{R}, \mu), (Y, \mathscr{S}, \nu)` 为对应于勒贝格测度的单位区间这样的测度空间,
    :math:`E` 是 :math:`X \times Y` 中是和下述条件的集: 对每个 :math:`x` 与每个  :math:`y`, :math:`E_x`
    与 :math:`X \setminus E^y` 均为可列集. 证明 :math:`E` 是不可测的.

.. proof:proof::

   假设 :math:`E` 可测, 那么

   .. math::
      1 = m ([0, 1] \times [0, 1]) \geqslant m (E) = \int_{X \times Y} \chi_E ~ \mathrm{d} (\mu \times \nu),

   即 :math:`\chi_E` 是 :math:`E` 上的可积函数, 从而由 Fubini 定理知

   .. math::
         \int_X \nu(E_x) ~ \mathrm{d} \mu
         & = \int_X \left( \int_Y \chi_{E_x} ~ \mathrm{d} \nu \right) ~ \mathrm{d} \mu
           = \int_{X \times Y} \chi_E ~ \mathrm{d} (\mu \times \nu) \\
         & = \int_Y \left( \int_X \chi_{E^y} ~ \mathrm{d} \mu \right) ~ \mathrm{d} \nu = \int_Y \mu (E^y) ~ \mathrm{d} \nu.

   由于对每个 :math:`x` 与每个  :math:`y`, :math:`E_x` 与 :math:`X \setminus E^y` 均为可列集, 而可列集都是零测集,
   所以 :math:`\nu(E_x) = 0`, :math:`\mu(E^y) = m(X) = 1`, 从而有

   .. math::
      \int_X \nu(E_x) ~ \mathrm{d} \mu & = \int_X 0 ~ \mathrm{d} \mu = 0, \\
      \int_Y \mu(E^y) ~ \mathrm{d} \nu & = \int_Y 1 ~ \mathrm{d} \nu = 1,

   这与上式矛盾, 所以 :math:`E` 不可测.

.. _ex-4-29:

29. 设 :math:`\varphi` 为 :math:`\mathbb{R}` 上的一个复值连续映射, 满足

    .. math::
      \varphi(x + y) = \varphi(x) \varphi(y) ~ \text{且} ~ \lvert \varphi(x) \rvert = 1 \quad (x, y \in \mathbb{R}).

    试证: :math:`\varphi(x)` 取 :math:`e^{i \lambda x} ~ (x \in \mathbb{R})` 的形式, :math:`\lambda` 为实参数.

.. proof:proof::

   任意复值函数 :math:`\varphi(x)` 可以写成 :math:`\varphi(x) = \rho(x) e^{i \theta(x)}`,
   其中 :math:`\rho(x), \theta(x)` 为实值函数.
   由题设条件 :math:`\rho(x) = \lvert \varphi(x) \rvert = 1` 知 :math:`\varphi(x) = e^{i \theta(x)}`.
   又由题设条件 :math:`\varphi(x + y) = \varphi(x) \varphi(y)`, 有

   .. math::
      e^{i \theta(x + y)} = e^{i \theta(x)} e^{i \theta(y)}.

   于是有

   .. math::
      \theta(x + y) = \theta(x) + \theta(y).

   这里不写 :math:`+ 2 \pi k` 是因为 :math:`e^{2 \pi i k} = 1`. 令 :math:`\lambda = \theta(1)`.
   首先有 :math:`\theta(0) = \theta(0 + 0) = \theta(0) + \theta(0)`, 从而 :math:`\theta(0) = 0`.
   对于 :math:`n \in \mathbb{N}`, 有

   .. math::
      \theta(n) = \theta(\underbrace{1 + \cdots + 1}_{n ~ \text{个}}) = n \theta(1) = n \lambda.

   对于 :math:`-n`, 有 :math:`\theta(-n) = \theta(0) - \theta(n) = - n \lambda`. 由此可知, 对于任意整数 :math:`n \in \mathbb{Z}`,
   有 :math:`\theta(n) = n \lambda`. 对于有理数 :math:`r = \dfrac{m}{n}`, :math:`m, n \in \mathbb{Z}^*`, 有

   .. math::
      \theta(r)
      & = \theta \bigg( \underbrace{\dfrac{1}{n} + \cdots + \dfrac{1}{n}}_{m ~ \text{个}} \bigg)
        = m \theta \left( \dfrac{1}{n} \right), \\
      \lambda = \theta(1)
      & = \bigg( \underbrace{\dfrac{1}{n} + \cdots + \dfrac{1}{n}}_{n ~ \text{个}} \bigg)
        = n \theta \left( \dfrac{1}{n} \right),

   从而 :math:`\theta(r) = \dfrac{m}{n} \lambda = r \lambda`. 对于实数 :math:`x`, 由于有理数集在实数集中稠密,
   所以存在有理数列 :math:`\{ r_n \}`, 使得 :math:`r_n \to x ~ (n \to \infty)`, 从而由 :math:`\theta` 的连续性
   (可由 :math:`\varphi` 的连续性推得) 知

   .. math::
      \theta(x) = \theta \left( \lim_{n \to \infty} r_n \right)
      = \lim_{n \to \infty} \theta(r_n) = \lim_{n \to \infty} r_n \lambda = x \lambda.

   于是 :math:`\varphi(x) = e^{i \theta(x)} = e^{i \lambda x}`.

   .. note::
      由 :math:`\varphi` 的连续性推导 :math:`\theta` 的连续性:

      .. math::
         \lvert \varphi(x + h) - \varphi(x) \rvert
         & = \lvert \varphi(x) \varphi(h) - \varphi(x) \rvert = \lvert \varphi(x) \rvert \lvert \varphi(h) - 1 \rvert \\
         & = \rvert \lvert \varphi(h) - 1 \rvert = \lvert e^{i \theta(h)} - 1 \rvert
           = \lvert \cos \theta(h) + i \sin \theta(h) - 1 \rvert \\
         & = \sqrt{(\cos \theta(h) - 1)^2 + \sin^2 \theta(h)} = \sqrt{2 - 2 \cos \theta(h)} \\
         & = 2 \left\lvert \sin \dfrac{\theta(h)}{2} \right\rvert.

      于是由 :math:`\displaystyle \lim_{h \to 0} \lvert \varphi(x + h) - \varphi(x) \rvert = 0`,
      知 :math:`\displaystyle \lim_{h \to 0} \sin \dfrac{\theta(h)}{2} = 0`, 从而有

      .. math::
         \lim_{h \to 0} (\theta(x + h) - \theta(x)) = \lim_{h \to 0} \theta(h) = 0,

      即 :math:`\theta` 是连续的.

.. _ex-4-30:

30. 设 :math:`\theta(x)` 为区间 :math:`[0, 1]` 上的 Cantor 函数, 令 :math:`f(x) = \theta(x) + x`,
    :math:`0 \leqslant x \leqslant 1`; :math:`g = f^{-1}`. 试证:

    (1). 存在可测集 :math:`B` 使 :math:`g^{-1}(B)` 不可测;

    (2). :math:`g^{-1}` 映不可测集为不可测集.

.. proof:proof::

   有如下的互逆的连续一一映射

   .. math::
      [0, 1] \overset{f}{\underset{g}\rightleftarrows} [0, 2]

   (1). 任取 :math:`[0, 1]` 上 Cantor 三分集 :math:`P_0` 的补集 :math:`G_0` 的构成区间 :math:`I = (a, b)`,
   Cantor 函数 :math:`\theta` 在 :math:`I` 上为常值函数, 因此 :math:`f(I) = (a + \theta(a), b + \theta(b))`.
   于是有 :math:`m (f(I)) = b - a = m I`, 且 :math:`f(G_0)` 为构成区间为 :math:`f(I)` 的开集, 从而可测.
   依据测度的可列可加性, 有

   .. math::
      m (f(G_0)) = \sum_{n = 1}^\infty m (f(I_n)) = \sum_{n = 1}^\infty m (I_n) = m (G_0) = 1

   成立, 从而知

   .. math::
      m (f (P_0)) = m ([0, 2]) - m (f (G_0)) = 2 - 1 = 1.

   于是可以从正测度集 :math:`f (P_0)` 中取出不可测集 :math:`B_0`, 并令 :math:`B = g (B_0) = f^{-1} (B_0) \subset P_0`.
   由于 :math:`P_0` 是零测集, 所以它的子集 :math:`B` 也是零测集, 从而是可测集. 而 :math:`g^{-1} (B) = B_0` 不可测.

   (2). 任取 :math:`[0, 1]` 区间内的不可测集 :math:`E`, 假设 :math:`A := g^{-1} (E) = f (E)` 可测. 由于 Cantor 函数 :math:`\theta`
   在 :math:`[0, 1]` 上为增函数, 所以对于任意 :math:`x_1 < x_2 \in [0, 1]`, 有

   .. math::
      f(x_2) - f(x_1) = \theta(x_2) - \theta(x_1) + x_2 - x_1 \geqslant x_2 - x_1 > 0.

   令 :math:`[0, 2] \ni y_i = f(x_i), i = 1, 2`, 则 :math:`x_i = g(y_i) = f^{-1}(y_i)`, 因此上式可写为

   .. math::
      :label: ex-4-30-eq-1

      g(y_2) - g(y_1) \leqslant y_2 - y_1.

   由上式 :eq:`ex-4-30-eq-1` 我们来证明 :math:`g` 将零测集映为零测集. 任取 :math:`[0, 2]` 上的零测集 :math:`M`,
   则对任意 :math:`\varepsilon > 0`, 存在开区间列 :math:`\{ I_n \}` 覆盖 :math:`M`, 且有
   :math:`\displaystyle \sum_{n = 1}^\infty m (I_n) < \varepsilon`. 由上式 :eq:`ex-4-30-eq-1` 知,
   对任意区间 :math:`I_n`, 有 :math:`m (g(I_n)) \leqslant m (I_n)`. 于是有

   .. math::
      m (g(M)) \leqslant m \left( \bigcup_{n = 1}^\infty g(I_n) \right) \leqslant \sum_{n = 1}^\infty m (g(I_n))
      \leqslant \sum_{n = 1}^\infty m (I_n) < \varepsilon.

   由于 :math:`\varepsilon` 的任意性, 所以 :math:`m (g(M)) = 0`, 即 :math:`g` 将零测集映为零测集.

   由假设 :math:`A = g^{-1} (E) = f (E)` 可测, 取 :math:`K \subset A` 为 :math:`A` 的等测核,
   即 :math:`K` 为一个 :math:`F_{\sigma}` 集, 且满足 :math:`m A = m K`. 记

   .. math::
      A = K \cup Z, ~~ \text{其中} ~ Z = A \setminus K ~ \text{为零测集}.

   :math:`A` 在 :math:`g` 下的像满足

   .. math::
      E = g(A) = g(K \cup Z) = g(K) \cup g(Z).

   由于 :math:`f` 为连续映射, 而且 :math:`K` 为 Borel 集 (:math:`F_{\sigma}` 集), 于是 :math:`g(K) = f^{-1}(K)` 也是 Borel 集,
   从而可测. 又由于 :math:`Z` 为零测集, 所以由上面已经证明的结论知 :math:`g(Z)` 也是零测集, 因此 :math:`E` 可测,
   这与 :math:`E` 为不可测集的假设矛盾. 综上所述, :math:`g^{-1}` 映不可测集为不可测集.

   .. note::
      第 (2) 问中用到的关键结论是, 一个满足 Lipschitz 条件的连续映射会将零测集映为零测集. 这里, 一个函数 :math:`g`
      满足 Lipschitz 条件, 是指存在常数 :math:`L > 0`, 使得对任意 :math:`x_1, x_2` 都有

      .. math::
         \lvert g(x_2) - g(x_1) \rvert \leqslant L \lvert x_2 - x_1 \rvert.

      :math:`L` 称为 Lipschitz 常数. 在本题中, 由不等式 :eq:`ex-4-30-eq-1` 可知, :math:`g` 满足 Lipschitz 条件,
      且 Lipschitz 常数 :math:`L = 1`.

.. _ex-4-34:

34. 设 :math:`\{ f_n \}` 为 :math:`[a, b]` 上有界变差函数列, :math:`f_n` 收敛于一有限函数 :math:`f` (当 :math:`n \to \infty`),
    且有 :math:`\displaystyle \bigvee_a^b (f_n) \leqslant K`, :math:`K` 为常数 (:math:`n \in \mathbb{N}`). 证明 :math:`f`
    也是有界变差函数.

.. proof:proof::

   任取区间 :math:`[a, b]` 的一个划分

   .. math::
      \mathscr{P}: ~ a = x_0 < x_1 < \cdots < x_k = b,

   由于 :math:`\displaystyle \bigvee_a^b (f_n) \leqslant K`, 所以对任意 :math:`n \in \mathbb{N}`, 有

   .. math::
      \sum_{i = 1}^k \lvert f_n(x_i) - f_n(x_{i - 1}) \rvert \leqslant K.

   又由于 :math:`\forall ~ x \in [a, b]`, 实数列 :math:`\{ f_n(x) \}_{n \in \mathbb{N}}` 收敛于 :math:`f(x)`,
   所以特别地对 :math:`x_i, i = 0, 1, \cdots, k`, 有 :math:`\{ f_n(x_i) \}_{n \in \mathbb{N}}` 收敛于 :math:`f(x_i)`.
   于是 :math:`\forall ~ \varepsilon > 0`, 存在正整数 :math:`N(\varepsilon, i)`, 使得当 :math:`n > N(\varepsilon, i)` 时, 有

   .. math::
      \lvert f_n(x_i) - f(x_i) \rvert < \dfrac{\varepsilon}{2k}, \quad i = 0, 1, \cdots, k.

   取 :math:`N(\varepsilon, \mathscr{P}) = \max \{ N(\varepsilon, 0), N(\varepsilon, 1), \cdots, N(\varepsilon, k) \}`,
   那么当 :math:`n > N(\varepsilon, \mathscr{P})` 时, 有

   .. math::
      \lvert f_n(x_i) - f(x_i) \rvert < \dfrac{\varepsilon}{2k}, \quad i = 0, 1, \cdots, k.

   考察 :math:`f` 在这个划分上的变差, 有

   .. math::
      \sum_{i = 1}^k \lvert f(x_i) - f(x_{i - 1}) \rvert
      & \leqslant \sum_{i = 1}^k \left( \lvert f(x_i) - f_n(x_i) \rvert
        + \lvert f_n(x_i) - f_n(x_{i - 1}) \rvert + \lvert f_n(x_{i - 1}) - f(x_{i - 1}) \rvert \right) \\
      & \leqslant \sum_{i = 1}^k \dfrac{\varepsilon}{2k}
        + \sum_{i = 1}^k \left( \lvert f_n(x_i) - f_n(x_{i - 1}) \rvert \right) + \sum_{i = 1}^k \dfrac{\varepsilon}{2k} \\
      & \leqslant \varepsilon + K,

   其中 :math:`n` 是任意大于 :math:`N(\varepsilon, \mathscr{P})` 的正整数. 由于 :math:`\varepsilon` 的任意性, 所以有

   .. math::
      \sum_{i = 1}^k \lvert f(x_i) - f(x_{i - 1}) \rvert \leqslant K.

   由于上式对任意划分成立, 所以 :math:`f` 是有界变差函数, 且有 :math:`\displaystyle \bigvee_a^b (f) \leqslant K`.

.. _ex-4-35:

35. 若函数 :math:`f` 在 :math:`[a, b]` 上绝对连续, 且几乎处处存在非负导数, 证明 :math:`f` 为增函数.

.. proof:proof::

   由于函数 :math:`f` 在 :math:`[a, b]` 上绝对连续, 所以存在 :math:`[a, b]` 上可积函数 :math:`g` 使得

   .. math::
      f(x) = f(a) + \int_{[a, x]} g ~ \mathrm{d} m, \quad x \in [a, b],

   并且 :math:`f'(x) = g(x)` 几乎处处成立. 由于函数 :math:`f` 在 :math:`[a, b]` 上几乎处处存在非负导数, 即 :math:`g(x)`
   几乎处处非负, 所以对任意 :math:`x_1 < x_2 \in [a, b]`, 有
   :math:`\displaystyle \int_{[x_1, x_2]} g ~ \mathrm{d} m \geqslant 0`, 从而知

   .. math::
      f(x_2) - f(x_1) = \int_{[x_1, x_2]} g ~ \mathrm{d} m \geqslant 0,

   这就证明了 :math:`f` 是增函数.

.. _ex-4-38:

38. 证明 Vitali 引理对有有限测度的无界集成立.

.. proof:proof::

   设 :math:`E \subset \mathbb{R}` 为有有限测度的无界集, :math:`m (E) < \infty`,
   :math:`\mathscr{M}` 为 :math:`E` 的一个由有正测度的闭区间构成的 Vitali 覆盖.
   要证明 :math:`\forall ~ \varepsilon > 0`, 存在有限个互不相交的区间 :math:`d_1, d_2, \cdots, d_n \in \mathscr{M}`,
   使得 :math:`m (E \setminus \bigcup_{i = 1}^n d_i) < \varepsilon`.

   取开集 :math:`G` 使得 :math:`E \subset G`, 且 :math:`m G < \infty`. 可以不妨设 :math:`\mathscr{M}` 中的区间都包含于
   :math:`G` 中. 这是因为 :math:`\forall ~ x \in E \subset G`, :math:`x` 必然属于开集 :math:`G` 的某个构成区间
   :math:`(a, b)`, 而 :math:`\mathscr{M}` 为 :math:`E` 的 Vitali 覆盖, 对于所有的 :math:`x \in E`, 都存在闭区间列
   :math:`\{ d_k \} \subset \mathscr{M}`, 使得 :math:`x \in d_k`, 且 :math:`\displaystyle \lim_{k \to \infty} m (d_k) = 0`.
   于是从某一项开始, :math:`d_k \subset (a, b) \subset G`. 令 :math:`\mathscr{M}'` 为 :math:`\mathscr{M}` 中所有包含于
   :math:`G` 的闭区间构成的子族, 那么 :math:`\mathscr{M}'` 也是 :math:`E` 的 Vitali 覆盖.
   对 :math:`\mathscr{M}'` 证明题设结论, 则该结论对 :math:`\mathscr{M}` 也成立.

   从 :math:`\mathscr{M}` 中任选一个区间 :math:`d_1`, 由数学归纳法依照如下步骤选取区间 :math:`d_2, d_3, \cdots, d_n`:
   假设已经选取了 :math:`d_1, d_2, \cdots, d_k`, 若 :math:`\displaystyle E \subset \bigcup_{i = 1}^k d_i`, 则停止选取; 否则令

   .. math::
      :label: ex-4-38-eq-1

      \mathscr{S}_k = \{ d \in \mathscr{M} ~:~ d \cap \bigcup_{i = 1}^k d_i = \emptyset \},

   那么 :math:`\mathscr{S}_k` 非空, 这是由于任取 :math:`x \in E \setminus \bigcup_{i = 1}^k d_i \neq \emptyset`,
   因为 :math:`\mathscr{M}` 为 :math:`E` 的 Vitali 覆盖, 所以存在足够小的闭区间 :math:`d \in \mathscr{M}`,
   使得 :math:`x \in d`, 且 :math:`\displaystyle d \cap \bigcup_{i = 1}^k d_i = \emptyset`. 令

   .. math::
      :label: ex-4-38-eq-2

      \delta_k = \sup \{ m (d) ~:~ d \in \mathscr{S}_k \},

   那么 :math:`0 < \delta_k \leqslant m (G) < \infty`. 由上确界的定义, 可以从 :math:`\mathscr{S}_k`
   中选取一个闭区间 :math:`d_{k + 1}`, 使得

   .. math::
      :label: ex-4-38-eq-3

      m (d_{k + 1}) > \dfrac{\delta_k}{2}, \quad d_{k + 1} \cap \bigcup_{i = 1}^k d_i = \emptyset.

   由此可得到互不相交的区间序列 :math:`\{ d_k \}`. 由于每一个 :math:`d_k` 都包含于 :math:`G` 中, 由测度的可列可加性以及单调性, 有

   .. math::
      :label: ex-4-38-eq-4

      \sum_{k = 1}^\infty m (d_k) = m \left( \bigcup_{k = 1}^\infty d_k \right) \leqslant m (G) < \infty.

   于是由级数的 Cauchy 收敛准则知 :math:`\forall ~ \varepsilon > 0`, 存在正整数 :math:`n`, 使得

   .. math::
      :label: ex-4-38-eq-5

      \sum_{k = n + 1}^\infty m (d_k) < \dfrac{\varepsilon}{5}.

   令 :math:`\displaystyle B = E \setminus \bigcup_{k = 1}^n d_k`, 下证 :math:`m B < \varepsilon`. 任取 :math:`x \in B`,
   由于 :math:`\displaystyle \bigcup_{k = 1}^n d_k \not\ni x` 为闭集, 所以存在 :math:`\delta > 0`,
   使得 :math:`\displaystyle (x - \delta, x + \delta) \cap \bigcup_{k = 1}^n d_k = \emptyset`.
   又由于 :math:`\mathscr{M}` 为 :math:`E` 的 Vitali 覆盖, 所以存在闭区间 :math:`d(x) \in \mathscr{M}`,
   使得 :math:`x \in d(x) \subset (x - \delta, x + \delta)`. 那么有
   :math:`\displaystyle d(x) \cap \bigcup_{k = 1}^n d_k = \emptyset`, 即 :math:`d(x) \in \mathscr{S}_n`, 从而有

   .. math::
      :label: ex-4-38-eq-6

      m (d(x)) \leqslant \delta_n < 2 m (d_{n + 1}).

   可以断言必然存在 :math:`n_0 (x) > n`, 使得 :math:`d(x) \not \in \mathscr{S}_{n_0 (x)}`, 否则对任意 :math:`k > n`,
   都有 :math:`\mathbb{N} \ni d(x) \in \mathscr{S}_k`, 即有

   .. math::
      :label: ex-4-38-eq-7

      m (d_{k + 1}) > \dfrac{\delta_k}{2}
      = \dfrac{1}{2} \sup \{ m (d) ~:~ d \in \mathscr{S}_k \} \geqslant \dfrac{1}{2} m (d(x)),

   这与级数 :eq:`ex-4-38-eq-4` 的收敛性矛盾. 那么由于 :math:`d(x) \not \in \mathscr{S}_{n_0 (x)}`,
   所以存在 :math:`n_1(x) \in \mathbb{N}`, 使得 :math:`n < n_1(x) \leqslant n_0 (x)`, 且有
   :math:`d(x) \cap d_{n_1(x)} \neq \emptyset`, 以及

   .. math::
      :label: ex-4-38-eq-8

      d(x) \cap d_{k} = \emptyset, k = 1, 2, \cdots, n_1(x) - 1.

   由上式 :eq:`ex-4-38-eq-7`, 以及 :math:`\mathscr{S}_k` 的定义式 :eq:`ex-4-38-eq-1`, :math:`\delta_k`
   的定义式 :eq:`ex-4-38-eq-2`, :math:`d_{k + 1}` 的取法 :eq:`ex-4-38-eq-3`, 有

   .. math::
      :label: ex-4-38-eq-9

      m (d(x)) \leqslant \delta_{n_1(x) - 1} < 2 m (d_{n_1(x)}).

   由于 :math:`d(x) \cap d_{n_1(x)} \neq \emptyset`, 所以将闭区间 :math:`d_{n_1(x)}` 分别往左右两边延伸 :math:`2 m (d_{n_1(x)})`,
   便得到一个闭区间 :math:`d_{n_1(x)}'`, 使得 :math:`x \in d(x) \subset d_{n_1(x)}'`, 且有区间长度关系

   .. math::
      :label: ex-4-38-eq-10

      m (d_{n_1(x)}') = 5 m (d_{n_1(x)}).

   结合式 :eq:`ex-4-38-eq-5`, 有

   .. math::
      :label: ex-4-38-eq-11

      m B \leqslant m \left( \bigcup_{x \in B} d_{n_1(x)}' \right) \leqslant m \left( \bigcup_{k = n + 1}^\infty d_k' \right)
      \leqslant \sum_{k = n + 1}^\infty m (d_k') = 5 \sum_{k = n + 1}^\infty m (d_k) < \varepsilon.

   上式 :eq:`ex-4-38-eq-11` 中 :math:`d_k'` 指的是依照类似于 :eq:`ex-4-38-eq-10` 的方法将闭区间 :math:`d_k`
   分别往左右两边延伸 :math:`2 m (d_k)`, 得到的长度为 :math:`5 m (d_k)` 的闭区间; 第一个不等式成立是由集合的包含关系
   :math:`\displaystyle B \subset \bigcup_{x \in B} d_{n_1(x)}'`; 第二个不等式成立是因为集合 :math:`\{ n_1(x) ~:~ x \in B \}`
   显然是集合 :math:`\{ k \in \mathbb{N} ~:~ k = n + 1, n + 2, \cdots \}` 的子集.

.. _ex-4-39:

39. 试作一增函数, 使它的不连续点处处稠密.

.. proof:solution::

   记 :math:`\mathbb{Q} = \{ r_n \}` 为有理数集, 令

   .. math::
      f(x) = \sum_{r_n < x} 2^{-n}.

   由于级数 :math:`\displaystyle \sum_{n = 1}^\infty 2^{-n}` 收敛, 所以 :math:`f(x)` 是良定义的.

   对任意两个实数 :math:`x_1 < x_2`, 存在有理数 :math:`r_k` 使得 :math:`x_1 < r_k < x_2`, 从而有

   .. math::
      f(x_2) - f(x_1) = \sum_{r_n < x_2} 2^{-n} - \sum_{r_n < x_1} 2^{-n}
      = \sum_{x_1 \leqslant r_n < x_2} 2^{-n} \geqslant 2^{-k} > 0.

   于是 :math:`f(x)` 是增函数.

   任取有理数 :math:`a = r_{n(a)} \in \mathbb{Q}`, 对任意实数 :math:`x > a`, 有

   .. math::
      f(x) - f(a) = \sum_{r_n < x} 2^{-n} - \sum_{r_n < a} 2^{-n} = \sum_{a \leqslant r_n < x} 2^{-n} \geqslant 2^{-n(a)},

   于是有

   .. math::
      \lim_{x \to a^+} \left( f(x) - f(a) \right) \geqslant 2^{-n(a)} > 0.

   由此可知 :math:`f(x)` 在 :math:`a` 处不 (右) 连续. 由于有理数集是稠密的, 所以 :math:`f(x)` 的不连续点处处稠密.

   .. note::
      如果将 :math:`f(x)` 的定义稍作修改, 令

      .. math::
         f(x) = \sum_{r_n \leqslant x} 2^{-n},

      则 :math:`f(x)` 在每个有理数处都不左连续.

.. _ex-4-40:

40. 试作 :math:`[0, 1]` 上的一有界可测函数, 使序列 :math:`f_n(x) = f(x + \alpha_n)` 不几乎处处收敛于 :math:`f(x)`,
    这里 :math:`\{ \alpha_n \}` 是给定的趋于 :math:`0` 的正数列 (:math:`n \to \infty`).

.. proof:solution::

   由于 :math:`\displaystyle \lim_{n \to \infty} \alpha_n = 0`, 即 :math:`\displaystyle \lim_{n \to \infty} x - \alpha_n = x`,
   若函数 :math:`f(x)` 在点 :math:`x` 处连续, 则必有 :math:`\displaystyle \lim_{n \to \infty} f(x - \alpha_n) = f(x)`.
   于是, 需要构造一个不连续点集有正测度的有界可测函数.

   未完....

.. _ex-4-42:

42. 设 :math:`f(x) = x^{-1/2}`, 对 :math:`0 < x < 1`; :math:`f(x) = 0`, 其余情形. 令

    .. math::
      g(x) = \sum_{n = 1}^\infty 2^{-n} f(x - r_n),

    这里 :math:`\{ r_n \}` 为有理数集. 试证 :math:`g \in L(\mathbb{R})`, :math:`g` 处处不连续且在任一子区间上有无界,
    而 :math:`g^2` 在任一子区间上不可积.

.. proof:proof::

   由非负可测函数列的逐项积分定理, 有

   .. math::
      :label: ex-4-42-eq-1

      \int_{\mathbb{R}} g ~ \mathrm{d} m = \sum_{n = 1}^\infty 2^{-n} \int_{\mathbb{R}} f(x - r_n) ~ \mathrm{d} m
      = \sum_{n = 1}^\infty 2^{-n} \int_{(r_n, r_n + 1)} \dfrac{1}{\sqrt{x - r_n}} ~ \mathrm{d} m.

   对于定义在 :math:`(r_n, r_n + 1)` 上的非负可测函数 :math:`f_n(x) = \dfrac{1}{\sqrt{x - r_n}}`,
   若反常积分 :math:`\displaystyle \int_{r_n}^{r_n + 1} f_n(x) ~ \mathrm{d} x` 收敛, 则 :math:`f_n`
   在 :math:`(r_n, r_n + 1)` 上勒贝格可积, 并且积分值相等, 即

   .. math::
      :label: ex-4-42-eq-2

      \int_{(r_n, r_n + 1)} \dfrac{1}{\sqrt{x - r_n}} ~ \mathrm{d} m = \int_{r_n}^{r_n + 1} f_n(x) ~ \mathrm{d} x
      = 2 \sqrt{x - r_n} \bigg|_{r_n}^{r_n + 1} = 2.

   将式 :eq:`ex-4-42-eq-2` 代入式 :eq:`ex-4-42-eq-1`, 有

   .. math::
      \int_{\mathbb{R}} g ~ \mathrm{d} m
      = \sum_{n = 1}^\infty 2^{-n} \int_{(r_n, r_n + 1)} \dfrac{1}{\sqrt{x - r_n}} ~ \mathrm{d} m
      = \sum_{n = 1}^\infty 2^{-n} \cdot 2 = 1 < \infty,

   于是 :math:`g \in L(\mathbb{R})`. 由于勒贝格可积函数几乎处处有限, 所以 :math:`g` 几乎处处有限, 即正项级数
   :math:`\displaystyle \sum_{n = 1}^\infty 2^{-n} f(x - r_n)` 几乎处处收敛.

   对任意非平凡区间 :math:`(\alpha, \beta)`, 存在有理数 :math:`r_k \in (\alpha, \beta)`. 对于 :math:`r_k`,
   可以在区间 :math:`(\alpha, \beta)` 取到实数列 :math:`\{ x_m \}` 使得 :math:`\displaystyle \lim_{m \to \infty} x_m = r_k`.
   可以不妨设 :math:`x_m - r_k \in (0, 1)` 对所有 :math:`m \in \mathbb{N}` 成立, 从而有

   .. math::
      g(x_m) = \sum_{n = 1}^\infty 2^{-n} f(x_m - r_n) \geqslant 2^{-k} f(x_m - r_k) = 2^{-k} (x_m - r_k)^{-1/2}.

   由此可知

   .. math::
      \lim_{m \to \infty} g(x_m) = \lim_{m \to \infty} 2^{-k} (x_m - r_k)^{-1/2} = \infty,

   即 :math:`g(x)` 在区间 :math:`(\alpha, \beta)` 上无界. 由此也可见, 若 :math:`g(x) < \infty`,
   则 :math:`g` 在点 :math:`x` 处不连续.

   考虑 :math:`g^2` 在任意非平凡开区间 :math:`(\alpha, \beta)` 上的勒贝格积分, 有

   .. math::
      \int_{(\alpha, \beta)} g^2 ~ \mathrm{d} m
      & = \int_{(\alpha, \beta)} \left( \sum_{n = 1}^\infty 2^{-n} f(x - r_n) \right)^2 ~ \mathrm{d} m \\
      & \geqslant \int_{(\alpha, \beta)} \sum_{n = 1}^\infty 4^{-n} f^2(x - r_n) ~ \mathrm{d} m \\
      & \geqslant 4^{-k} \int_{(\alpha, \beta)} f^2(x - r_k) ~ \mathrm{d} m \\
      & = 4^{-k} \int_{(r_k, \beta_0)} \dfrac{1}{x - r_k} ~ \mathrm{d} m,

   其中 :math:`\beta_0 = \min\{r_k + 1, \beta\}`. 由于 :math:`(r_k, \beta_0)` 上的非负可测函数
   :math:`\displaystyle \dfrac{1}{x - r_k}` 的反常积分发散:

   .. math::
      \int_{r_k}^{\beta_0} \dfrac{1}{x - r_k} ~ \mathrm{d} x = \ln (x - r_k) \bigg|_{r_k}^{\beta_0} = \infty,

   所以 :math:`\displaystyle \int_{(\alpha, \beta)} g^2 ~ \mathrm{d} m = \infty`, 即 :math:`g^2` 在区间
   :math:`(\alpha, \beta)` 上不可积.
