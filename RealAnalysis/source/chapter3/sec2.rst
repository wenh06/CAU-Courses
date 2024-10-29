§2 可测函数列的收敛性
------------------------------------------

.. _ex-3-13:

13. 试给出关于可测函数列当极限函数为无穷大情形的相应 Egorov 定理的陈述并加以证明.

.. proof:solution::

   可测函数列当极限函数为无穷大情形的相应 Egorov 定理:

      设 :math:`E` 是可测集, :math:`m E < \infty`, :math:`\{f_n\}` 是 :math:`E` 上几乎处处有限的可测函数列,
      且 :math:`\displaystyle \lim_{n \to \infty} f_n(x) = \infty` 几乎处处成立, 那么对于任意给定的 :math:`\delta > 0`,
      存在可测集 :math:`E_\delta \subset E` 使得 :math:`m (E \setminus E_\delta) < \delta`, 且 :math:`\{f_n\}` 在 :math:`E_\delta` 上一致收敛于 :math:`\infty`.

   相应的证明:

      考虑可测函数列 :math:`g_n = \dfrac{f_n}{1 + \lvert f_n \rvert}`, 那么 :math:`\{g_n\}` 是 :math:`E` 上处处有限的可测函数列,
      而且 :math:`\displaystyle \lim_{n \to \infty} g_n(x) = 1` 几乎处处成立. 由 Egorov 定理, 对于任意给定的 :math:`\delta > 0`,
      存在可测集 :math:`E_\delta \subset E` 使得 :math:`m (E \setminus E_\delta) < \delta`, 且 :math:`\{g_n\}` 在 :math:`E_\delta` 上一致收敛于 :math:`1`.
      也就是说, 对任意 :math:`\varepsilon > 0`, 存在自然数 :math:`N (\varepsilon) \in \mathbb{N}`, 使得当 :math:`n > N (\varepsilon)` 时,
      有 :math:`0 < 1 - g_n(x) < \varepsilon, \forall x \in E_\delta`. 由于 :math:`g_n(x) = \dfrac{f_n(x)}{1 + \lvert f_n(x) \rvert}`,
      所以对任意 :math:`n > N (\varepsilon)` 以及任意的 :math:`x \in E_\delta`, 有

      .. math::

         \dfrac{1}{1 + \lvert f_n(x) \rvert} \leqslant \dfrac{1 + \lvert f_n(x) \rvert - f_n(x)}{1 + \lvert f_n(x) \rvert} = 1 - g_n(x) < \varepsilon.

      这等价于

      .. math::

         \lvert f_n(x) \rvert > \dfrac{1}{\varepsilon} - 1,

      这意味着 :math:`\{f_n\}` 在 :math:`E_\delta` 上一致收敛于 :math:`\infty`.

.. _ex-3-14:

14. 设 :math:`x \in [0, 1)`, 其二进表示为 :math:`\displaystyle x = \sum_{i=1}^\infty \frac{x_i}{2^i}`,
    :math:`x_i \in \{0, 1\}`, 并约定用有尽表示. 定义函数 :math:`\displaystyle \varphi (x) = \sum_{i=1}^\infty \frac{2x_i}{3^i}`,
    再取 :math:`[0, 1)` 的一不可测子集 :math:`E`, 并在 :math:`\mathbb{R}` 上定义函数

    .. math::

      \psi (x) = \begin{cases}
         1, & x \in \varphi (E), \\
         0, & \text{其余情形}.
      \end{cases}

    试证 :math:`\varphi, \psi` 均可测, 但 :math:`\psi \circ \varphi` 不可测.

.. proof:proof::

   设 :math:`\displaystyle x = \sum_{i=1}^\infty \frac{x_i}{2^i}, y = \sum_{i=1}^\infty \frac{y_i}{2^i} \in [0, 1)`,
   其中 :math:`x_i, y_i \in \{0, 1\}`, 且都是有尽表示. 假设 :math:`x < y`, 那么存在 :math:`k_0 \in \mathbb{N}`,
   使得 :math:`x_{k_0} = 0, y_{k_0} = 1`, 并且要么 :math:`k_0 = 1`, 要么 :math:`k_0 > 1` 且 :math:`x_k = y_k, \forall 1 \leqslant k < k_0`.
   于是有

   .. math::

      \varphi (x) = \sum_{i=1}^\infty \frac{2x_i}{3^i} < \sum_{i=1}^\infty \frac{2y_i}{3^i} = \varphi (y).

   所以 :math:`\varphi` 是严格单调递增的, 为单射, 并且其值域为 Cantor 三分集 :math:`P_0`. 记 :math:`I = [0, 1)`,
   那么对于 :math:`\alpha \in \mathbb{R}` 有

   .. math::

      I (\varphi > \alpha) = \begin{cases}
         \emptyset, & \alpha \geqslant 1, \\
         (\varphi^{-1} (\alpha), 1), & \alpha \in P_0, \\
         [\varphi^{-1} (\beta), 1), & \alpha \in I \setminus P_0, \beta = \inf \{ x \in P_0 : x > \alpha \}, \\
         I, & \alpha < 0.
      \end{cases}

   以上都是可测集, 因此 :math:`\varphi` 是可测函数. 事实上, 若 :math:`\alpha \in I \setminus P_0 = G_0`,
   那么 :math:`\alpha` 落入开集 :math:`G_0` 的某个构成区间 :math:`I_{n, k} = (a, b)`, 上式中的 :math:`\beta` 即为
   :math:`I_{n, k}` 的右端点 :math:`b`.

   :math:`\forall \alpha \in \mathbb{R}`, 对于函数 :math:`\psi` 有

   .. math::

      I (\psi > \alpha) = \begin{cases}
         \emptyset, & \alpha \geqslant 1, \\
         \varphi (E), & \alpha \in [0, 1), \\
         \mathbb{R}, & \alpha < 0.
      \end{cases}

   由于 :math:`P_0` 是零测集, 而 :math:`\varphi (E) \subset P_0`, 所以 :math:`\varphi (E)` 也是零测集, 从而可测.
   于是 :math:`\psi` 是可测函数.

   对于 :math:`\psi \circ \varphi` 来说, 取 :math:`\alpha \in [0, 1)` 有

   .. math::

      I (\psi \circ \varphi > \alpha) = \left\{ x \in [0, 1) : \psi (\varphi (x)) > \alpha \right\}
      = \left\{ x \in [0, 1) : \varphi (x) \in \varphi (E) \right\} = E,

   为不可测集, 因此 :math:`\psi \circ \varphi` 不可测.

.. _ex-3-15:

15. 设 :math:`\{E_n\}` 为可测集列, :math:`\displaystyle E = \bigcup_{n=1}^\infty E_n`, 试证 :math:`f` 在 :math:`E` 上可测的充分必要条件是
    :math:`f` 限制在每个 :math:`E_n` 上均可测, :math:`n \in \mathbb{N}`.

.. proof:proof::

   由于有

   .. math::

      E(f > \alpha) = E \cap f^{-1} (\alpha, \infty) = \bigcup_{n=1}^\infty E_n \cap f^{-1} (\alpha, \infty) = \bigcup_{n=1}^\infty E_n (f > \alpha),

   所以若每个 :math:`E_n` 上 :math:`f` 可测, 即 :math:`E_n (f > \alpha)` 可测, 那么 :math:`E(f > \alpha)` 可测.

   另一方面, 若 :math:`E(f > \alpha)` 可测, 那么对于任意的 :math:`n \in \mathbb{N}`, 由于 :math:`E_n \subset E`, 有

   .. math::

      E_n (f > \alpha) = E_n \cap f^{-1} (\alpha, \infty) = E_n \cap f^{-1} (\alpha, \infty) \cap E = E_n \cap E (f > \alpha),

   从而可知 :math:`f` 限制在每个 :math:`E_n` 上均可测.

.. _ex-3-16:

16. 设函数列 :math:`\{f_n\}_{n \in \mathbb{N}}` 在有界集 :math:`E` 上近一致收敛于 :math:`f`, 试证 :math:`\{f_n\}_{n \in \mathbb{N}}` 几乎处处收敛于 :math:`f`.

.. proof:proof::

   由于 :math:`\{f_n\}_{n \in \mathbb{N}}` 在有界集 :math:`E` 上近一致收敛于 :math:`f`, 那么对于任意给定的 :math:`k \in \mathbb{N}`,
   存在有界集 :math:`E_k \subset E` 使得 :math:`m (E \setminus E_k) < \dfrac{1}{k}`, 且 :math:`\{f_n\}_{n \in \mathbb{N}}` 在 :math:`E_k` 上一致收敛于 :math:`f`.
   取 :math:`\displaystyle E^* = \bigcup_{k=1}^\infty E_k`, 那么 :math:`\{f_n\}_{n \in \mathbb{N}}` 在 :math:`E^*` 上处处收敛于 :math:`f`, 且有

   .. math::

      m (E \setminus E^*) = m \left( \bigcap_{k=1}^\infty (E \setminus E_k) \right) \leqslant m (E \setminus E_k) < \dfrac{1}{k},

   对所有的 :math:`k \in \mathbb{N}` 都成立, 从而必有 :math:`m (E \setminus E^*) = 0`, 即 :math:`\{f_n\}_{n \in \mathbb{N}}` 几乎处处收敛于 :math:`f`.

.. _ex-3-17:

17. 设函数列 :math:`\{f_n\}_{n \in \mathbb{N}}` 在 :math:`E` 上依测度收敛于 :math:`f`, 且在 :math:`E` 上几乎处处有 :math:`f_n \leqslant g`,
    :math:`n \in \mathbb{N}`. 试证在 :math:`E` 上几乎处处有 :math:`f \leqslant g`.

.. proof:proof::

   令 :math:`E_n = E (f_n > g), n \in \mathbb{N},` 由于在 :math:`E` 上几乎处处有 :math:`f_n \leqslant g`, 所以 :math:`m E_n = 0`.
   令 :math:`\displaystyle E_0 = \bigcup_{n=1}^\infty E_n`, 那么 :math:`m E_0 = 0`. 于是, 在 :math:`\widetilde{E} = E \setminus E_0` 上,
   对于任意的 :math:`x \in \widetilde{E}`, 有 :math:`f_n(x) \leqslant g(x), \forall n \in \mathbb{N}`,
   且函数列 :math:`\{f_n\}_{n \in \mathbb{N}}` 在 :math:`\widetilde{E}` 上也依测度收敛于 :math:`f`. 我们有

   .. math::

      \widetilde{E} (f > g) = \bigcup_{k=1}^\infty \widetilde{E} \left( f - g \geqslant \dfrac{1}{k} \right).

   由于 :math:`\left\{ \widetilde{E} \left( f - g > \dfrac{1}{k} \right) \right\}_{k \in \mathbb{N}}` 构成了渐张可测集列,
   因此

   .. math::

      m \widetilde{E} (f > g) = m \left( \bigcup_{k=1}^\infty \widetilde{E} \left( f - g \geqslant \dfrac{1}{k} \right) \right)
      = \lim_{k \to \infty} m \widetilde{E} \left( f - g \geqslant \dfrac{1}{k} \right).

   由于 :math:`f - g = (f - f_n) + (f_n - g)`, 所以 :math:`\forall n \in \mathbb{N}` 有

   .. math::

      \widetilde{E} \left( f \geqslant g + \dfrac{1}{k} \right) \subset \widetilde{E} \left( f - f_n \geqslant \dfrac{1}{k} \right)
      \subset \widetilde{E} \left( \lvert f - f_n \rvert > \dfrac{1}{k} \right),

   从而有

   .. math::

      m \widetilde{E} \left( f \geqslant g + \dfrac{1}{k} \right)
      \leqslant \inf_{n \in \mathbb{N}} m \widetilde{E} \left( \lvert f - f_n \rvert > \dfrac{1}{k} \right).

   另一方面, 由于函数列 :math:`\{f_n\}_{n \in \mathbb{N}}` 在 :math:`\widetilde{E}` 上依测度收敛于 :math:`f`,
   那么对于任意给定的 :math:`k \in \mathbb{N}` 有

   .. math::

      \lim_{n \to \infty} m \widetilde{E} \left( \lvert f_n - f \rvert > \dfrac{1}{k} \right) = 0,

   因此, :math:`m \widetilde{E} \left( f \geqslant g + \dfrac{1}{k} \right) = 0, \forall k \in \mathbb{N}`, 从而有

   .. math::

      m \widetilde{E} (f > g) = \lim_{k \to \infty} m \widetilde{E} \left( f - g \geqslant \dfrac{1}{k} \right) = 0,

   以及

   .. math::

      0 \leqslant m E (f > g) \leqslant m (E_0 \cup \widetilde{E} (f > g)) = m E_0 + m \widetilde{E} (f > g) = 0.

   最终我们有 :math:`m E (f > g) = 0`, 即 :math:`f \leqslant g` 几乎处处成立.

.. _ex-3-18:

18. 设函数列 :math:`\{f_n\}_{n \in \mathbb{N}}` 在 :math:`E` 上依测度收敛于 :math:`f`, 且几乎处处有 :math:`f_n \leqslant f_{n+1}`, :math:`n \in \mathbb{N}`,
    证明 :math:`\{f_n\}_{n \in \mathbb{N}}` 几乎处处收敛于 :math:`f`.

.. proof:proof::

   由 Riesz 定理, 存在 :math:`\{f_n\}_{n \in \mathbb{N}}` 的子列 :math:`\{f_{n_k}\}_{k \in \mathbb{N}}` 几乎处处收敛于 :math:`f`,
   记此集合为 :math:`E_1`, 有 :math:`m (E \setminus E_1) = 0`. 又由于几乎处处有 :math:`f_n \leqslant f_{n+1}`, :math:`n \in \mathbb{N}`,
   记此集合为 :math:`E_2`, 有 :math:`m (E \setminus E_2) = 0`. 于是, 取 :math:`E^* = E_1 \cap E_2`, 有 :math:`m (E \setminus E^*) = 0`.
   那么在任意 :math:`x \in E^*` 处, 有 :math:`f_{n_k} (x) \to f(x)`. 由于 :math:`\{f_n(x)\}_{n \in \mathbb{N}}` 是单调递增的,
   其子列 :math:`\{f_{n_k}(x)\}_{k \in \mathbb{N}}` 也是单调递增的. 若 :math:`f(x) = \infty`, 那么对于任意的 :math:`M > 0`,
   存在 :math:`K \in \mathbb{N}`, 使得 :math:`f_{n_k}(x) > M, \forall k \geqslant K`, 从而对任意的 :math:`n \geqslant n_K`,
   有 :math:`f_n(x) \geqslant f_{n_K}(x) > M`, 这表明 :math:`f_n(x) \to \infty = f(x)`. 若 :math:`f(x) \in \mathbb{R}`,
   那么 :math:`f(x)` 是数列 :math:`\{f_n(x)\}_{n \in \mathbb{N}}` 的一个上界, 从而由单调有界定理, 有 :math:`f_n(x) \to f(x)`.
   综上所述, :math:`\{f_n\}_{n \in \mathbb{N}}` 几乎处处 (在集合 :math:`E^*` 上) 收敛于 :math:`f`.

.. _ex-3-19:

19. 设函数列 :math:`\{f_n\}_{n \in \mathbb{N}}` 在 :math:`E` 上依测度收敛于 :math:`f`, 而 :math:`f_n \sim g_n`, :math:`n \in \mathbb{N}`,
    证明 :math:`\{g_n\}_{n \in \mathbb{N}}` 也在 :math:`E` 上依测度收敛于 :math:`f`.

.. proof:proof::

   由 Riesz 定理, 对 :math:`\{f_n\}_{n \in \mathbb{N}}` 的任意子列 :math:`\{f_{n_k}\}_{k \in \mathbb{N}}`,
   存在其子列 :math:`\{f_{n_{k_i}}\}_{i \in \mathbb{N}}`, 使得 :math:`f_{n_{k_i}} \to f` 几乎处处成立, 记此集合为 :math:`E_1`,
   有 :math:`m (E \setminus E_1) = 0`. 又由于 :math:`f_n \sim g_n`, :math:`n \in \mathbb{N}`, 记此集合为 :math:`E_2`,
   有 :math:`m (E \setminus E_2) = 0`. 于是, 取 :math:`E^* = E_1 \cap E_2`, 有 :math:`m (E \setminus E^*) = 0`.
   那么在任意 :math:`x \in E^*` 处, 有 :math:`f_{n_{k_i}}(x) \to f(x)`, 且 :math:`f_{n_{k_i}}(x) = g_{n_{k_i}}(x)`,
   从而 :math:`g_{n_{k_i}}(x) \to f(x)`. 所以, 对 :math:`\{g_n\}_{n \in \mathbb{N}}` 的任意子列 :math:`\{g_{n_k}\}_{k \in \mathbb{N}}`,
   我们找到了它的子列 :math:`\{g_{n_{k_i}}\}_{i \in \mathbb{N}}`, 使得 :math:`g_{n_{k_i}} \to f` 几乎处处成立.
   由 Riesz 定理, :math:`\{g_n\}_{n \in \mathbb{N}}` 在 :math:`E` 上依测度收敛于 :math:`f`.

.. _ex-3-20:

20. 设 :math:`m E < \infty`, 在 :math:`E` 上几乎处处有限的可测函数列 :math:`\{f_n\}_{n \in \mathbb{N}}` 与 :math:`\{g_n\}_{n \in \mathbb{N}}`
    分别依测度收敛于 :math:`f` 与 :math:`g`. 试证 :math:`\{f_n \cdot g_n\}_{n \in \mathbb{N}}` 依测度收敛于 :math:`f \cdot g`.

.. proof:proof::

   采用 Riesz 定理, 很容易验证 :math:`\{f_n^2\}_{n \in \mathbb{N}}`, :math:`\{g_n^2\}_{n \in \mathbb{N}}` 分别依测度收敛于 :math:`f^2`, :math:`g^2`.
   (证明方法与 :ref:`本章第 18 题 <ex-3-18>` 以及 :ref:`本章第 19 题 <ex-3-19>` 类似)

   由依测度收敛的定义, 对任意 :math:`\varepsilon > 0` 有

   .. math::

      & \lim_{n \to \infty} m (E (\lvert f_n - f \rvert > \varepsilon)) = 0, \\
      & \lim_{n \to \infty} m (E (\lvert g_n - g \rvert > \varepsilon)) = 0.

   由三角不等式

   .. math::

      \lvert f_n + g_n - f - g \rvert \leqslant \lvert f_n - f \rvert + \lvert g_n - g \rvert

   可知 :math:`\displaystyle \lim_{n \to \infty} m (E (\lvert f_n + g_n - f - g \rvert > 2 \varepsilon)) = 0`,
   即有 :math:`\{f_n + g_n\}_{n \in \mathbb{N}}` 依测度收敛于 :math:`f + g`. 进一步由 Riesz 定理有
   :math:`\{(f_n + g_n)^2\}_{n \in \mathbb{N}}` 依测度收敛于 :math:`(f + g)^2`.

   由于有恒等式

   .. math::

      f_n \cdot g_n = \dfrac{1}{4} \left( (f_n + g_n)^2 - f_n^2 - g_n^2 \right),

   以及已证明的 :math:`\{f_n^2\}_{n \in \mathbb{N}}`, :math:`\{g_n^2\}_{n \in \mathbb{N}}`, :math:`\{(f_n + g_n)^2\}_{n \in \mathbb{N}}`
   分别依测度收敛于 :math:`f^2`, :math:`g^2`, :math:`(f + g)^2`, 从而有 :math:`\{f_n \cdot g_n\}_{n \in \mathbb{N}}` 依测度收敛于 :math:`f \cdot g`.

.. _ex-3-21:

21. 试构造 :math:`[0, 1]` 上的连续函数列 :math:`\{f_n\}_{n \in \mathbb{N}}`, 使满足
    (i) :math:`\{f_n\}_{n \in \mathbb{N}}` 在 :math:`[0, 1]` 上几乎处处收敛于 :math:`0`,
    但 (ii) :math:`\{f_n\}_{n \in \mathbb{N}}` 在任何子区间上不一致收敛于 :math:`0`.

.. proof:solution::

   令 :math:`A = \{ r_1, r_2, \cdots \} = \mathbb{Q} \cap [0, 1]` 是 :math:`[0, 1]` 区间内的有理数之集.
   取 :math:`\delta = \dfrac{1}{2}`, 对于每个 :math:`r_k \in A`, 取

   .. math::

      I_k & = (a_k, b_k) = \left( r_k - \dfrac{\delta}{2^{k+1}}, r_k + \dfrac{\delta}{2^{k+1}} \right), \\
      d_k & = \dfrac{\lvert I_k \rvert}{2} = \dfrac{\delta}{2^{k+1}}.

   对 :math:`r \in A`, 约定 :math:`q(r)` 表示 :math:`r` 的既约分数表示的分母. 对每个 :math:`t \in \mathbb{N}`, 令

   .. math::

      \varphi_{k, t} (x) = \begin{cases}
         \dfrac{1}{q(r_k)} \cdot \left( 1 - \dfrac{2^{t+1}}{d_k} \lvert x - r_k \rvert \right), & x \in \left[ r_k - \dfrac{d_k}{2^{t+1}}, r_k + \dfrac{d_k}{2^{t+1}} \right], \\
         0, & \text{其余情形}.
      \end{cases}

   通过如下的一一对应 :math:`\mathbb{N} \times \mathbb{N} \to \mathbb{N}`:

   .. math::

      s: \mathbb{N} \times \mathbb{N} \to \mathbb{N}, \quad (k, t) \mapsto \dfrac{(k + t - 2)(k + t - 1)}{2} + k,

   令 :math:`n = s(k, t)`, 以及 :math:`f_n = \varphi_{k, t}`, 那么 :math:`\{f_n\}_{n \in \mathbb{N}}` 是 :math:`[0, 1]` 上的连续函数列.

   首先, :math:`\{f_n\}_{n \in \mathbb{N}}` 在 :math:`[0, 1]` 上几乎处处收敛于 :math:`0`. 事实上,
   对于任意给定的 :math:`x \in [0, 1] \setminus A`, 任取 :math:`\varepsilon > 0`, 取 :math:`q_0 \in \mathbb{N}`,
   使得 :math:`\dfrac{1}{q_0} < \varepsilon`, 令

   .. math::

      k_0 = \min \left\{ k \in \mathbb{N} : q(r_k) \geqslant q_0 \right\},

   那么对任意 :math:`k > k_0, t \in \mathbb{N}`, 有 :math:`q(r_k) \geqslant q_0`, 从而 :math:`\varphi_{k, t} (x) < \varepsilon`.
   对于 :math:`k \leqslant k_0`, 令

   .. math::

      d & = \min \left\{ \lvert x - r_k \rvert : k \leqslant k_0 \right\} > 0, \\
      t_0 & = \min \left\{ t \in \mathbb{N} : \dfrac{d_k}{2^{t+1}} < \dfrac{d}{2}, ~ \forall k \leqslant k_0 \right\},

   那么对任意 :math:`t > t_0, k \leqslant k_0`, 有 :math:`\varphi_{k, t} (x) = 0 < \varepsilon`. 因此取

   .. math::

      N_0 = s(k_0 + 1, t_0 + 1) = \dfrac{(k_0 + t_0 + 1)(k_0 + t_0 + 2)}{2} + k_0 + 1,

   必有 :math:`f_n (x) < \varepsilon, \forall n > N_0`. 这就证明了在 :math:`[0, 1]` 区间的所有无理点上,
   有 :math:`\displaystyle \lim_{n \to \infty} f_n (x) = 0`, 即 :math:`\{f_n\}_{n \in \mathbb{N}}`
   在 :math:`[0, 1]` 上几乎处处收敛于 :math:`0`.

   其次, :math:`\{f_n\}_{n \in \mathbb{N}}` 在任何子区间上不一致收敛于 :math:`0`. 事实上,
   :math:`[0, 1]` 区间的任何子区间都包含有理数, 设其中一个为 :math:`r_{k_0}`, 那么对于任意的 :math:`t \in \mathbb{N}`,
   有 :math:`f_{s(k_0, t)} (r_{k_0}) = \dfrac{1}{q(r_{k_0})}`,
   从而 :math:`\{f_n\}_{n \in \mathbb{N}}` 在 :math:`[0, 1]` 区间的任何子区间上都不一致收敛于 :math:`0`.

.. _ex-3-22:

22. 设 :math:`f, f_n (n \in \mathbb{N})` 是定义在区间 :math:`E = [a, b]` 上的实函数, :math:`r` 为自然数,
    用记号 :math:`E(\lvert f_n - f \rvert \leqslant 1 / r)` 表示 :math:`E` 中满足 :math:`\lvert f_n (x) - f (x) \rvert \leqslant 1 / r` 的点所成的集.
    试证集 :math:`\displaystyle \bigcap_{r=1}^\infty \varliminf\limits_{n} E(\lvert f_n - f \rvert \leqslant 1 / r)` 是 :math:`E` 中使
    :math:`\{f_n\}_{n \in \mathbb{N}}` 收敛于 :math:`f` （当 :math:`n \to \infty` ）的点集.

.. proof:proof::

   :math:`E` 中使 :math:`\{f_n\}_{n \in \mathbb{N}}` 收敛于 :math:`f` （当 :math:`n \to \infty` ）的点集为

   .. math::

      A = \{ x \in E : \forall \varepsilon > 0, \exists N (x, \varepsilon) \in \mathbb{N}, \forall n > N (x, \varepsilon), \lvert f_n (x) - f(x) \rvert < \varepsilon \}.

   任取 :math:`x \in A`, 那么 :math:`\forall \varepsilon > 0`, 存在 :math:`N (x, \varepsilon) \in \mathbb{N}`,
   使得 :math:`\forall n > N (x, \varepsilon)` 有 :math:`\lvert f_n (x) - f(x) \rvert < \varepsilon`. 特别地,
   对每个自然数 :math:`r \in \mathbb{N}`, 取 :math:`\varepsilon = \dfrac{1}{2r}`,
   那么 :math:`x \in E (\lvert f_n - f \rvert \leqslant 1 / r), \forall n > N (x, \varepsilon)`,
   从而知 :math:`\displaystyle x \in \bigcap_{n=N (x, \varepsilon)+1}^\infty E(\lvert f_n - f \rvert \leqslant 1 / r)`, 因此

   .. math::

      x \in \varliminf\limits_{n} E(\lvert f_n - f \rvert \leqslant 1 / r) = \bigcup_{k=1}^\infty \bigcap_{n=k}^\infty E(\lvert f_n - f \rvert \leqslant 1 / r).

   由于上式对任意的 :math:`r \in \mathbb{N}` 都成立, 因此

   .. math::

      x \in \bigcap_{r=1}^\infty \varliminf\limits_{n} E(\lvert f_n - f \rvert \leqslant 1 / r).

   因此 :math:`\displaystyle A \subset \bigcap_{r=1}^\infty \varliminf\limits_{n} E(\lvert f_n - f \rvert \leqslant 1 / r)`.

   反过来, 任取 :math:`\displaystyle x \in \bigcap_{r=1}^\infty \varliminf\limits_{n} E(\lvert f_n - f \rvert \leqslant 1 / r)`,
   那么 :math:`\forall r \in \mathbb{N}`, 有 :math:`x \in \varliminf\limits_{n} E(\lvert f_n - f \rvert \leqslant 1 / r)`.
   这表明, 对每个自然数 :math:`r \in \mathbb{N}`, 存在自然数 :math:`N (x, r) \in \mathbb{N}`, 使得 :math:`\forall n > N (x, r)`,
   有 :math:`x \in E(\lvert f_n - f \rvert \leqslant 1 / r)`. 对任取的 :math:`\varepsilon > 0`,
   取 :math:`r = \left\lceil \dfrac{1}{\varepsilon} \right\rceil`, 那么 :math:`\dfrac{1}{r} < \varepsilon`,
   于是 :math:`x \in E(\lvert f_n - f \rvert \leqslant 1 / r) \subset E(\lvert f_n - f \rvert < \varepsilon)`
   对所有的 :math:`n > N (x, r)` 都成立. 这表明了 :math:`x \in A`, 因此
   :math:`\displaystyle \bigcap_{r=1}^\infty \varliminf\limits_{n} E(\lvert f_n - f \rvert \leqslant 1 / r) \subset A`.

   综上所述, :math:`\displaystyle \bigcap_{r=1}^\infty \varliminf\limits_{n} E(\lvert f_n - f \rvert \leqslant 1 / r) = A`,

.. _ex-3-25:

25. 设 :math:`m E > 0`, :math:`\{f_n\}` 是 :math:`E` 上几乎处处有限的可测函数列, 且当 :math:`n \to \infty` 时,
    :math:`\{f_n\}` 在 :math:`E` 上几乎处处收敛. 证明存在常数 :math:`c` 与正测度集 :math:`E_0 \subset E`,
    使在 :math:`E_0` 上对一切 :math:`n \in \mathbb{N}` 有 :math:`\lvert f_n \rvert \leqslant c`.

.. proof:proof::

   由于 :math:`\{f_n\}` 是 :math:`E` 上几乎处处有限的可测函数列, 那么 :math:`\displaystyle Z_0 = \bigcup_{n=1}^\infty E (\lvert f_n \rvert = \infty)`
   是零测集. 又由于 :math:`\{f_n\}` 在 :math:`E` 上几乎处处收敛（ 注意: 收敛指的是收敛到一个有限的值, 不包括 :math:`\pm\infty` ）,
   那么存在零测集 :math:`Z_1 \subset E` 使得 :math:`\{f_n\}` 在 :math:`E \setminus Z_1` 上处处收敛. 令 :math:`E_1 = E \setminus (Z_0 \cup Z_1)`,
   那么 :math:`\displaystyle f(x) := \lim_{n \to \infty} f_n(x)` 是 :math:`E_1` 上处处有限的可测函数, 且 :math:`m E_1 > 0`. 由于

   .. math::

      E_1 = E_1 (\lvert f \rvert < \infty) = \bigcup_{k=1}^\infty \left( E_1 (\lvert f \rvert < k) \cap \{ x \in E_1 : \lvert x \rvert < k \} \right),

   那么存在 :math:`k_0 \in \mathbb{N}`, 使得 :math:`m \left( E_1 (\lvert f \rvert < k_0) \cap \{ x \in E_1 : \lvert x \rvert < k_0 \} \right) > 0`. 令

   .. math::

      E_2 = E_1 (\lvert f \rvert < k_0) \cap \{ x \in E_1 : \lvert x \rvert < k_0 \},

   那么 :math:`0 < m E_2 < \infty` 且 :math:`\lvert f \rvert < k_0` 在 :math:`E_2` 上处处成立. 由 Egorov 定理, 对于 :math:`\delta = \dfrac{m E_2}{2} > 0`,
   存在集合 :math:`E_3 \subset E_2` 使得 :math:`m E_3 > m E_2 - \delta = \dfrac{m E_2}{2} > 0`, 且 :math:`\{f_n\}` 在 :math:`E_3` 上一致收敛于 :math:`f`.
   因此, 对于 :math:`\varepsilon = 1`, 存在 :math:`N \in \mathbb{N}`, 使得当 :math:`n > N` 时, 有 :math:`\lvert f_n(x) - f(x) \rvert < \varepsilon = 1, \forall x \in E_3`.
   那么对于所有的 :math:`n > N`, 有

   .. math::

      E_3(\lvert f_n \rvert \leqslant k_0 + 1) = E_3.

   另一方面, 令 :math:`E_{30} = E_3`, 有 :math:`m E_{30} > 0`, 且

   .. math::

      E_{30} = E_{30} (\lvert f_1 \rvert < \infty) = \bigcup_{k=1}^\infty E_{30} (\lvert f_1 \rvert < k),

   于是可以选取 :math:`k_1 \in \mathbb{N}`, 使得

   .. math::

      m E_{31} = m E_{30} (\lvert f_1 \rvert < k_1) > 0.

   于是对于 :math:`1 \leqslant n \leqslant N`, 可以归纳地选取 :math:`k_n \in \mathbb{N}` 以及集合 :math:`E_{3n} \subset E_{3(n-1)}` 使得 :math:`m E_{3n} > 0`,
   且 :math:`f_n(x) < k_n` 在 :math:`E_{3n}` 上处处成立. 那么令

   .. math::

      & c = \max \{ k_1, \cdots, k_N, k_0 + 1 \}, \\
      & E_0 = E_{3N},

   即有 :math:`\lvert f_n \rvert \leqslant c` 在正测度集 :math:`E_0` 上对一切 :math:`n \in \mathbb{N}` 成立.

.. _ex-3-26:

26. 设函数列 :math:`\{f_n\}` 在 :math:`\mathbb{R}` 上几乎处处收敛于有限函数 :math:`f`. 试证存在可测集列 :math:`\{E_k\}_{k \in \mathbb{N}}`,
    使在每个 :math:`E_k` 上 :math:`\{f_n\}` 一致收敛于 :math:`f, (n \to \infty)` 而 :math:`\displaystyle \mathscr{C} \left(\bigcup_{k=1}^\infty E_k \right)` 为零测集.

.. proof:proof::

   由于函数列 :math:`\{f_n\}` 在 :math:`\mathbb{R}` 上几乎处处收敛于有限函数 :math:`f`, 那么对于每个自然数 :math:`k \in \mathbb{N}`,
   函数列 :math:`\{f_n\}` 在区间 :math:`[-k, k]` 上几乎处处收敛于 :math:`f`. 由 Egorov 定理, 对于任意给定的 :math:`\varepsilon > 0`,
   存在可测集 :math:`F_k \subset [-k, k]` 使得 :math:`m([-k, k] \setminus F_k) < \varepsilon / 2^k`, 且 :math:`\{f_n\}` 在 :math:`F_k` 上一致收敛于 :math:`f`.
   令 :math:`\displaystyle E_k = \bigcup_{i=1}^k F_i \subset [-k, k]`, 那么 :math:`\{E_k\}_{k \in \mathbb{N}}` 是渐张可测集列,
   且 :math:`f_n` 在 :math:`E_k` 上一致收敛于 :math:`f`, 且有

   .. math::

      m \left( [-k, k] \setminus E_k \right) \leqslant m \left( [-k, k] \setminus F_k \right) < \varepsilon / 2^k.

   进一步考虑可测集列

   .. math::

      G_d := [-d, d] \cap \mathscr{C} \left(\bigcup_{k=1}^\infty E_k \right), \quad d \in \mathbb{N},

   那么 :math:`\{ G_d \}_{d \in \mathbb{N}}` 是渐张可测集列, 且对任意 :math:`d \in \mathbb{N}`, 有

   .. math::

      G_d & = [-d, d] \cap \mathscr{C} \left(\bigcup_{k=1}^\infty E_k \right) = [-d, d] \cap \left( \bigcap_{k=1}^\infty \mathscr{C} (E_k) \right) \\
      & = \left( \bigcap_{k=1}^\infty \left( [-d, d] \cap \mathscr{C} (E_k) \right) \right) \\
      & \subset [-k, k] \setminus E_k, \quad \forall k \geqslant d,

   于是 :math:`m G_d \leqslant m \left( [-k, k] \setminus E_k \right) < \varepsilon / 2^k, \forall k \geqslant d`, 从而必有 :math:`m G_d = 0`.
   另一方面, 由于

   .. math::

      \bigcup_{d=1}^\infty G_d = \bigcup_{d=1}^\infty \left( [-d, d] \cap \mathscr{C} \left(\bigcup_{k=1}^\infty E_k \right) \right)
      = \left( \bigcup_{d=1}^\infty [-d, d] \right) \cap \mathscr{C} \left( \bigcup_{k=1}^\infty E_k \right)
      = \mathscr{C} \left(\bigcup_{k=1}^\infty E_k \right),

   因此有

   .. math::

      m \left( \mathscr{C} \left(\bigcup_{k=1}^\infty E_k \right) \right) = m \left( \bigcup_{d=1}^\infty G_d \right) \leqslant \sum_{d=1}^\infty m G_d = 0.

   .. note::

      这里要注意的是, 尽管 :math:`\mathscr{C} E_k, k \in \mathbb{N}` 构成了一个渐缩可测集列, 但其中每一个集合的测度都是无穷大的, 因此关于渐缩可测集列的性质

      .. math::

         m \left( \mathscr{C} \left(\bigcup_{k=1}^\infty E_k \right) \right) = m \left( \bigcap_{k=1}^\infty \mathscr{C} E_k \right)
         = \lim_{k \to \infty} m \left( \mathscr{C} E_k \right)

      在这里不能使用.

.. _ex-3-29:

29. 对 :math:`n \in \mathbb{N}`, 令

    .. math::

      \alpha_n = 1 + \dfrac{1}{2} + \cdots + \dfrac{1}{n} - \left[ 1 + \dfrac{1}{2} + \cdots + \dfrac{1}{n} \right],

    其中 :math:`[\alpha]` 表示数 :math:`\alpha` 的整部. 定义区间列

    .. math::

      I_n = \begin{cases}
         \left[ \alpha_n, \alpha_{n+1} \right), & \text{ 若 } \alpha_n \leqslant \alpha_{n+1}, \\
         \\ % add some vertical space
         \left[ \alpha_{n}, 1 \right) \cup \left[ 0, \alpha_{n+1} \right), & \text{ 若 } \alpha_n > \alpha_{n+1}.
      \end{cases}

    再定义 :math:`[0, 1)` 上的函数列 :math:`\{f_n = \chi_{I_n}\}_{n \in \mathbb{N}}`. 试证 :math:`\{f_n\}` 依测度收敛于 :math:`0`
    而不几乎处处收敛于 :math:`0`. 试选出子序列 :math:`\{f_{n_k}\}` 使它处处收敛于 :math:`0`.

.. proof:proof::

   令 :math:`r_n = 1 + \dfrac{1}{2} + \cdots + \dfrac{1}{n}`, 那么 :math:`\alpha_n = \{ r_n \}`, 其中 :math:`\{ \cdot \}` 表示取小数部分.
   我们有

   .. math::

      \alpha_{n+1} = \begin{cases}
         \alpha_n + \dfrac{1}{n + 1}, & \text{ 若 } \alpha_n < 1 - \dfrac{1}{n+1}, \\
         \alpha_n + \dfrac{1}{n + 1} - 1 = \alpha_n - \dfrac{n}{n + 1}, & \text{ 若 } \alpha_n \geqslant 1 - \dfrac{1}{n+1}.
      \end{cases}

   在这两种情况下, 总有 :math:`m I_n = \dfrac{1}{n + 1} \to 0 (n \to \infty)`. 因此 :math:`\{f_n = \chi_{I_n}\}` 依测度收敛于 :math:`0`.

   由于 :math:`r_n \to + \infty (n \to \infty)`, 那么 :math:`\forall n \in \mathbb{N}`, 总存在 :math:`k \in \mathbb{N}`,
   使得 :math:`\dfrac{1}{n+1} + \cdots + \dfrac{1}{n+k} > 1`. 这种情况下, :math:`I_n, \cdots, I_{n+k}` 构成了 :math:`[0, 1)` 的一个覆盖,
   那么对于所有的 :math:`x \in [0, 1)`, :math:`\{f_n(x), \cdots, f_{n+k}(x)\}` 至少有一个为 1, 因此数列 :math:`\{f_n(x)\}_{n \in \mathbb{N}}`
   不收敛于 :math:`0`. 因此 :math:`\{f_n\}` 不几乎处处收敛于 :math:`0`.

   我们将所有满足 :math:`a_n \geqslant 1 - \dfrac{1}{n+1}` 的 :math:`n` 挑出来, 按从小到大的顺序排列, 得到下标的序列记为 :math:`\{n_k\}`.
   由于 :math:`r_n \to + \infty (n \to \infty)`, 得到的序列也是一个无穷序列 :math:`\{n_k\}_{k \in \mathbb{N}}`. 在这种情况下, 有

   .. math::

      I_{n_k} = [\alpha_{n_k}, 1) \cup [0, \alpha_{n_k + 1}).

   由于 :math:`1 > a_{n_k} \geqslant 1 - \dfrac{1}{n_k+1}, 0 < \alpha_{n_k + 1} < \dfrac{1}{n_k + 1}`, 因此 :math:`\forall x \in (0, 1)`,
   存在 :math:`K \in \mathbb{N}`, 使得当 :math:`k > K` 时, 有 :math:`x < 1 - \dfrac{1}{n_k+1} < a_{n_k}` 且 :math:`x > \dfrac{1}{n_k + 1} > \alpha_{n_k + 1}`,
   即 :math:`x \not \in I_{n_k}`. 因此 :math:`\{f_{n_k}\}` 在 :math:`(0, 1)` 上处处收敛于 :math:`0`. 由于 :math:`0 \in I_{n_k}, \forall k \in \mathbb{N}`,
   所以 :math:`\displaystyle \lim_{k \to \infty} f_{n_k}(0) = 1`, 总之, :math:`\{f_{n_k}\}` 在 :math:`[0, 1)` 上几乎处处（除了 :math:`x = 0` 这一点）收敛于 :math:`0`,
   离想要的结果还差一点.

   更进一步: 将所有满足 :math:`a_n \geqslant 1 - \dfrac{1}{n+1}` 的 :math:`n` 挑出来, 按从小到大的顺序排列, 得到下标的序列记为 :math:`\{m_k\}_{k \in \mathbb{N}}`.
   令 :math:`n_k = m_k - 1, k \in \mathbb{N}`, 即上一种取法的每一项在原序列中的前一项, 那么有

   .. math::

      1 - \dfrac{1}{n_k + 1 + 1} \leqslant a_{n_k + 1} = a_{n_k} + \dfrac{1}{n_k + 1},

   即

   .. math::

      1 - \dfrac{1}{n_k + 2} - \dfrac{1}{n_k + 1} \leqslant a_{n_k}, \quad 1 - \dfrac{1}{n_k + 2} \leqslant a_{n_k + 1} < 1,

   而且 :math:`I_{n_k} = [\alpha_{n_k}, \alpha_{n_k + 1})`. 可以看到, 当 :math:`k \to \infty` 时, :math:`a_{n_k} \to 1, a_{n_k + 1} \to 1`,
   因此 :math:`\forall x \in [0, 1)`, 存在 :math:`K \in \mathbb{N}`, 使得当 :math:`k > K` 时, 有 :math:`x < 1 - \dfrac{1}{n_k + 2} - \dfrac{1}{n_k + 1} < a_{n_k}`,
   即 :math:`x \not \in I_{n_k}`. 因此 :math:`\{f_{n_k}\}` 在 :math:`[0, 1)` 上处处收敛于 :math:`0`.

   .. note::

      我们这里取的区间 :math:`I_{n_k}` 是随着 :math:`k` 的增大, 逐渐向 :math:`1` 靠近, 而且区间长度逐渐趋于 :math:`0`.

.. _ex-3-30:

30. 试作 :math:`E = [0, 1]` 上的可测函数 :math:`f`, 使对 :math:`E` 上任何连续函数 :math:`g` 有 :math:`m E( f \neq g ) \neq 0`.
    此结果与 Luzin 定理有无矛盾?

.. proof:solution::

   取

   .. math::

      f(x) = \begin{cases} -1, & 0 \leqslant x < 1/2, \\ 1, & 1/2 \leqslant x \leqslant 1. \end{cases}.

   假设存在连续函数 :math:`g` 使得 :math:`m E( f \neq g ) = 0`, 则 :math:`m E(g = -1) = m E(f = -1) = 1/2`,
   :math:`m E(g = 1) = m E(f = 1) = 1/2`, 即存在 :math:`x_1, x_2 \in E` 使得 :math:`g(x_1) = -1`, :math:`g(x_2) = 1`.
   由于 :math:`g` 是连续函数, 那么 :math:`\forall y \in (-1, 1)`, 存在 :math:`x_3 \in E` 使得 :math:`g(x_3) = y`,
   即 :math:`g(E) \subset [-1, 1]`. 由于开集在连续函数下的原像是非空开集, 那么 :math:`g^{-1}((-1, 1))` 是开集, 从而有正测度,
   即 :math:`m E (-1 < g < 1) > 0`. 这会导致

   .. math::

      1 = m E \geqslant m E(g = -1) + m E(g = 1) + m E (-1 < g < 1) > 1,

   矛盾. 因此不存在这样的连续函数 :math:`g`, 也就是说 :math:`m E( f \neq g ) \neq 0` 对任何连续函数 :math:`g` 都成立.

   这与 Luzin 定理不矛盾, 因为 Luzin 定理的结论是 :math:`\forall \varepsilon > 0`, 存在连续函数 :math:`g` 使得 :math:`m E( f \neq g ) < \varepsilon`.
   在我们的例子中, :math:`\forall \varepsilon > 0`, 可以取区间 :math:`(1/2 - \varepsilon/2, 1/2 + \varepsilon/2)`, 并令

   .. math::

      g(x) = \begin{cases}
         -1, & 0 \leqslant x < 1/2 - \varepsilon/2, \\
         1, & 1/2 + \varepsilon/2 < x \leqslant 1, \\
         1 + \dfrac{2}{\varepsilon} \left( x - \dfrac{1 + \varepsilon}{2} \right), & 1/2 - \varepsilon/2 \leqslant x < 1/2 + \varepsilon/2.
      \end{cases}

.. _ex-3-32:

32. 试证对 :math:`[0, 1]` 上带连续参数的可测函数族 :math:`\{f_t\}_{t \in [0, 1]}`, Egorov 定理不成立.
    即存在 :math:`I = [0, 1]` 上的可测函数族 :math:`\{f_t\}_{t \in [0, 1]}`, 当 :math:`t \to 0` 时有 :math:`f_t \to 0` a.e.,
    但对某个 :math:`\varepsilon > 0`, :math:`m^* I(f_t > \varepsilon) \nrightarrow 0 (t \to 0)`.

.. proof:proof::

   待写
