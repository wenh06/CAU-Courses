第四章补充材料
^^^^^^^^^^^^^^^^^^^^^^^^^

.. _dirichlet-kernel-uniformly-bounded:

1. 令 :math:`\varphi = \chi_{(\alpha, \beta)}`, 其中 :math:`(\alpha, \beta) \subset E = [-\pi, \pi]`, 那么

   .. math::

      \varphi_n (x) = \dfrac{1}{\pi} \int_{-\pi}^{\pi} \varphi(x + u) \dfrac{\sin(n + \frac{1}{2})u}{2 \sin \frac{1}{2}u} ~ \mathrm{d}u
      = \dfrac{1}{\pi} \int_{(\alpha-x))/2}^{(\beta-x)/2} \dfrac{\sin(2n+1)v}{\sin v} ~ \mathrm{d}v

   一致有界, 即存在常数 :math:`C` 使得 :math:`\|\varphi_n\|_{\infty} \leq C` 对所有 :math:`n` 成立.

.. proof:proof::

   由对称性, 只需要考虑 :math:`0 \leqslant \alpha - x \leqslant \beta - x \leqslant \pi` 的情况. 此时,
   被积函数 :math:`\dfrac{\sin(2n+1)v}{\sin v}` 的分母在被积区间 :math:`\left(\dfrac{\alpha-x}{2}, \dfrac{\beta-x}{2}\right)` 上非负,
   且单调递增. 有一个重要的观察是, 令区间 :math:`I_k = \left[ \dfrac{k-1}{2n+1}\pi, \dfrac{k}{2n+1}\pi \right]`,
   那么在相邻的区间 :math:`I_k` 和 :math:`I_{k+1}` 上有

   .. math::

      \left\lvert \int_{I_k} \dfrac{\sin(2n+1)v}{\sin v} ~ \mathrm{d}v \right\rvert
      > \left\lvert \int_{I_{k+1}} \dfrac{\sin(2n+1)v}{\sin v} ~ \mathrm{d}v \right\rvert,

   但积分值的符号相反, :math:`k` 为奇数时为正, :math:`k` 为偶数时为负. 那么令

   .. math::

      k_{\alpha} & = \min \{ k \ :\ \dfrac{k}{2n+1} \geqslant \dfrac{\alpha-x}{2} \}, \\
      k_{\alpha, 0} & = \min \{ k \ :\ k \geqslant k_{\alpha}, \text{ 且 } k \text{为偶数} \}, \\
      k_{\alpha, 1} & = \min \{ k \ :\ k \geqslant k_{\alpha}, \text{ 且 } k \text{为奇数} \}, \\
      k_{\beta} & = \max \{ k \ :\ \dfrac{k}{2n+1} \leqslant \dfrac{\beta-x}{2} \}, \\
      k_{\beta, 0} & = \max \{ k \ :\ k \leqslant k_{\beta}, \text{ 且 } k \text{为偶数} \}, \\
      k_{\beta, 1} & = \max \{ k \ :\ k \leqslant k_{\beta}, \text{ 且 } k \text{为奇数} \}

   有

   .. math::

      \varphi_n(x)
      & = \dfrac{1}{\pi} \left( \int_{(\alpha-x)/2}^{\pi k_{\alpha, 1}/(2n+1)} + \left( \int_{I_{k_{\alpha, 1}}} + \int_{I_{k_{\alpha, 1} + 1}} \right)
         + \cdots + \int_{\pi k_{\beta, 1}/(2n+1)}^{(\beta-x)/2} \right) \dfrac{\sin(2n+1)v}{\sin v} ~ \mathrm{d}v \\
      & \geqslant \dfrac{1}{\pi} \left( \int_{(\alpha-x)/2}^{\pi k_{\alpha, 1}/(2n+1)} + \int_{\pi k_{\beta, 1}/(2n+1)}^{(\beta-x)/2} \right)
         \dfrac{\sin(2n+1)v}{\sin v} ~ \mathrm{d}v,

   同时

   .. math::

      \varphi_n(x)
      & = \dfrac{1}{\pi} \left( \int_{(\alpha-x)/2}^{\pi k_{\alpha, 0}/(2n+1)} + \left( \int_{I_{k_{\alpha, 0}}} + \int_{I_{k_{\alpha, 0} + 1}} \right)
         + \cdots + \int_{\pi k_{\beta, 0}/(2n+1)}^{(\beta-x)/2} \right) \dfrac{\sin(2n+1)v}{\sin v} ~ \mathrm{d}v \\
      & \leqslant \dfrac{1}{\pi} \left( \int_{(\alpha-x)/2}^{\pi k_{\alpha, 0}/(2n+1)} + \int_{\pi k_{\beta, 0}/(2n+1)}^{(\beta-x)/2} \right)
         \dfrac{\sin(2n+1)v}{\sin v} ~ \mathrm{d}v.

   总之, 有

   .. math::

      \lvert \varphi_n (x) \rvert
      & \leqslant 2 \cdot \dfrac{1}{\pi} \cdot \max\limits_k \int_{I_k} \left\lvert \dfrac{\sin(2n+1)v}{\sin v} \right\rvert ~ \mathrm{d}v \\
      & = \dfrac{2}{\pi} \cdot \int_{I_1} \dfrac{\sin(2n+1)v}{\sin v} ~ \mathrm{d}v \\
      & = \dfrac{2}{\pi} \cdot \int_0^{\frac{\pi}{2n+1}} \dfrac{\sin(2n+1)v}{\sin v} ~ \mathrm{d}v.

   我们知道 :math:`\dfrac{\sin(2n+1)v}{\sin v} = 1 + 2 \sum\limits_{k=1}^n \cos(2kv)`, 其导数为 :math:`-2 \sum\limits_{k=1}^n 2k \sin(2kv)`,
   在 :math:`[0, \pi/(2n+1)]` 恒负, 因此 :math:`\dfrac{\sin(2n+1)v}{\sin v}` 在 :math:`[0, \pi/(2n+1)]` 上单调递减, 于是有

   .. math::

      \lvert \varphi_n (x) \rvert
      & \leqslant \dfrac{2}{\pi} \cdot \int_0^{\frac{\pi}{2n+1}} \dfrac{\sin(2n+1)v}{\sin v} ~ \mathrm{d}v \\
      & \leqslant \dfrac{2}{\pi} \cdot \int_0^{\frac{\pi}{2n+1}} (2n+1) ~ \mathrm{d}v \\
      & = \dfrac{2}{\pi} \cdot \dfrac{\pi}{2n+1} \cdot (2n+1) = 2.

   这样就证明了 :math:`\varphi_n` 一致有界.

   .. note::

      Dirichlet 核 :math:`\dfrac{\sin\frac{2n+1}{2}v}{\sin\frac{1}{2}v}` 的图像如下所示:

      .. image:: ../_static/images/Dirichlet_kernels.svg
         :align: center
         :width: 80%

      以上图片来自 `Wikipedia <https://en.wikipedia.org/wiki/Dirichlet_kernel>`_.

.. _thm-differentiation-under-integral-sign:

2. 积分号下求导定理: 设 :math:`f(x, t)` 定义在 :math:`E \times (\alpha, \beta)` 上,
   且对任意 :math:`t \in (\alpha, \beta)` 有 :math:`f(x, t) \in L_E`; 对任意 :math:`x \in E` 有 :math:`f(x, t)` 关于 :math:`t` 处处可微.
   若存在 :math:`F(x) \in L_E` 使得

   .. math::

      \left\lvert \dfrac{\partial f(x, t)}{\partial t} \right\rvert \leqslant F(x), \quad \forall ~ (x, t) \in E \times (\alpha, \beta),

   那么

   .. math::

      \dfrac{~ \mathrm{d}}{~ \mathrm{d}t} \int_E f(x, t) ~ \mathrm{d}x = \int_E \dfrac{\partial f(x, t)}{\partial t} ~ \mathrm{d}x.

.. proof:proof::

   由微分中值定理, 有

   .. math::

      \dfrac{~ \mathrm{d}}{~ \mathrm{d}t} \int_E f(x, t) ~ \mathrm{d}x & = \lim\limits_{h \to 0} \dfrac{1}{h} \int_E \left( f(x, t+h) - f(x, t) \right) ~ \mathrm{d}x \\
      & = \lim\limits_{h \to 0} \dfrac{1}{h} \int_E \left( \dfrac{\partial}{\partial t} f(x, t + \theta(h) h) \right) \cdot h ~ \mathrm{d}x \\
      & = \lim\limits_{h \to 0} \int_E \dfrac{\partial}{\partial t} f(x, t + \theta(h) h) ~ \mathrm{d}x, \quad \theta(h) \in (0, 1).

   那么 :math:`\left\{ g_h(x) := \dfrac{\partial}{\partial t} f(x, t + \theta(h) h) \right\}_{h \in (0, 1)}` 构成一个可测函数族,
   且满足 :math:`g_h(x) \leqslant F(x) \in L_E`, :math:`0` 为 指标集 :math:`(0, 1)` 的聚点, 由 Lebesgue 控制收敛定理, 有

   .. math::

      \dfrac{~ \mathrm{d}}{~ \mathrm{d}t} \int_E f(x, t) ~ \mathrm{d}x & = \lim\limits_{h \to 0} \int_E \dfrac{\partial}{\partial t} f(x, t + \theta(h) h) ~ \mathrm{d}x \\
      & = \int_E \lim\limits_{h \to 0} \dfrac{\partial}{\partial t} f(x, t + \theta(h) h) ~ \mathrm{d}x \\
      & = \int_E \dfrac{\partial}{\partial t} f(x, t) ~ \mathrm{d}x.

.. _diagram-of-lebesgue-integral-and-differential:

3. 关于勒贝格积分与微分关系的图表

   约定一些集合（空间）的记号

   .. math::

      L_{[a, b]} & = [a, b] \text{ 区间上的 Lebesgue 可积函数}, \\
      L_0 & = \{ f \in L_{[a, b]} ~:~ f \sim 0\}, \\
      C([a, b]) & = [a, b] \text{ 区间上的连续函数}, \\
      AB([a, b]) & = [a, b] \text{ 区间上几乎处处有限的函数}, \\
      BV([a, b]) & = [a, b] \text{ 区间上有界变差函数}, \\
      AC([a, b]) & = [a, b] \text{ 区间上绝对连续函数}.

   以上都是线性空间. 勒贝格积分与微分的结论主要是围绕上述空间的关系以及它们之间的（线性）映射展开的, 可以用下面的图表来表示:

   .. tikz::
      :align: center
      :xscale: 100
      :libs: arrows.meta,positioning,calc,cd

      \node (L0) at (0, 0) {$L_0$};
      \node (L) at (2, 0) {$L_{[a, b]}$};
      \draw[arrows={- Classical TikZ Rightarrow[]}] ([xshift=0.5ex,yshift=1ex] L0.east) arc (90:270:0.5ex) -- (L);

      \node (B) at (7, 0) {$C([a, b])$};
      \draw[arrows={- Classical TikZ Rightarrow[]}] (L) -- (B) node[midway,above] {$\int_{[a, x]}$};

      \node (BV) at (7, -2) {$BV([a, b]) \cap C([a, b])$};
      \draw[arrows={- Classical TikZ Rightarrow[]}] ([xshift=-1ex,yshift=0.5ex] BV.north) arc (180:360:0.5ex) -- (B);
      \draw[arrows={- Classical TikZ Rightarrow[]}, dashed] (L) -- (BV) node[midway,above] {$\int_{[a, x]}$};

      \node (BV2) at (11, -2) {$BV([a, b])$};
      \draw[arrows={- Classical TikZ Rightarrow[]}] ([xshift=0.5ex,yshift=1ex] BV.east) arc (90:270:0.5ex) -- (BV2);

      \node (AC) at (7, -4) {$AC([a, b])$};
      \draw[arrows={- Classical TikZ Rightarrow[]}, dashed] ([xshift=-1ex,yshift=0.5ex] AC.north) arc (180:360:0.5ex) -- (BV);
      \draw[arrows={- Classical TikZ Rightarrow[]}, dashed] (L) -- ([xshift=-4ex] AC.north) node[midway,left] {$\int_{[a, x]}$};

      \node (p1) at (2, -4) {$L_{[a, b]} / L_0$};
      \draw[arrows={- Classical TikZ Rightarrow[sep] Classical TikZ Rightarrow[]}] (L) -- (p1) node[midway,left] {$\operatorname{pr}$};
      \draw[arrows={- Classical TikZ Rightarrow[]}, dashed] (p1) -- (AC) node[midway,above] {$\int_{[a, x]}$};

      \node (AB) at (14, -2) {$AB([a, b])$};
      \draw[arrows={- Classical TikZ Rightarrow[]}, dashed] (BV2) -- (AB) node[midway,above] {$\widetilde{~ \mathrm{d}}$};

      \node (L_again) at (14, -4) {$L_{[a, b]}$};
      \draw[arrows={- Classical TikZ Rightarrow[]}] ([xshift=-1ex,yshift=0.5ex] L_again.north) arc (180:360:0.5ex) -- (AB);
      \draw[arrows={- Classical TikZ Rightarrow[]}, dashed] (AC) -- (L_again) node[midway,above] {$\widetilde{~ \mathrm{d}}$};

      \node (p2) at (17, -4) {$L_{[a, b]} / L_0$};
      \draw[arrows={- Classical TikZ Rightarrow[sep] Classical TikZ Rightarrow[]}] (L_again) -- (p2) node[midway,above] {$\operatorname{pr}$};
      \draw[arrows={- Classical TikZ Rightarrow[]}, dashed, bend right = 15] (p1) to node[midway,below] {$\operatorname{pr}~\circ~\widetilde{~ \mathrm{d}}~\circ~\int_{[a, x]} = \operatorname{id}$} (p2);

   以上的 :math:`\int_{[a, x]}` 表示变上限勒贝格积分, :math:`\widetilde{~ \mathrm{d}}` 表示微分 (几乎处处有定义, 没有定义的集合是零测集,
   约定微分取值为 :math:`0`), :math:`\hookrightarrow` 表示自然的嵌入 (包含) 映射, :math:`\operatorname{pr}` 表示商映射.
   虚线的箭头就是相关的定理.

.. _thm-tonelli:

4. Tonelli 定理: 设 :math:`f(x, y)` 是定义在 :math:`E \times F` 上的非负可测函数,
   其中 :math:`E \subset \mathbb{R}^m`, :math:`F \subset \mathbb{R}^n` 都是可测集, 那么有

   - 截口 :math:`f_x(y)` 关于 :math:`y` 在 :math:`F` 上非负可测, :math:`a.e. x \in E`;
   - 截口 :math:`f^y(x)` 关于 :math:`x` 在 :math:`E` 上非负可测, :math:`a.e. y \in F`;
   - 记 :math:`\displaystyle g(x) = \int_F f(x, y) ~ \mathrm{d}y`, 那么 :math:`g(x)` 在 :math:`E` 上非负可测;
   - 记 :math:`\displaystyle h(y) = \int_E f(x, y) ~ \mathrm{d}x`, 那么 :math:`h(y)` 在 :math:`F` 上非负可测;
   - 有如下的等式成立

   .. math::

      \int_{E \times F} f(x, y) ~ \mathrm{d}(x, y) = \int_E \left( \int_F f(x, y) ~ \mathrm{d}y \right) ~ \mathrm{d}x
      = \int_F \left( \int_E f(x, y) ~ \mathrm{d}x \right) ~ \mathrm{d}y.

   .. note::

      与 Fubini 定理结合起来, 可以得到 Fubini-Tonelli 定理: 设 :math:`f(x, y)` 是定义在 :math:`E \times F` 上的可测函数, 那么

      .. math::

         \int_{E \times F} \lvert f(x, y) \rvert ~ \mathrm{d} x \times ~ \mathrm{d} y
         = \int_E \left( \int_F \lvert f(x, y) \rvert ~ \mathrm{d}y \right) ~ \mathrm{d}x
         = \int_F \left( \int_E \lvert f(x, y) \rvert ~ \mathrm{d}x \right) ~ \mathrm{d}y.

      若上式三项中的任意一项有限（即可积）, 那么进一步会有

      .. math::

         \int_{E \times F} f(x, y) ~ \mathrm{d} x \times ~ \mathrm{d} y
         = \int_E \left( \int_F f(x, y) ~ \mathrm{d}y \right) ~ \mathrm{d}x = \int_F \left( \int_E f(x, y) ~ \mathrm{d}x \right) ~ \mathrm{d}y.
