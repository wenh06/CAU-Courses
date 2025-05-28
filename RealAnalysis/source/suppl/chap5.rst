第五章补充材料
^^^^^^^^^^^^^^^^^^^^^^^^^

.. _modes-of-convergence:

1. 截止到第五章, 我们已经学习了一些收敛的概念, 它们之间的关系可以用下图总结:

   .. tikz::
      :align: center
      :xscale: 100
      :libs: arrows.meta, positioning, calc, cd
      :packages: amsfonts, [slantfont,boldfont]xeCJK, pifont, relsize

      \node (uniform) at (-12, -4) {$\text{({\color{cyan}近})一致收敛}$};
      \node (ae) at (-7,0) {$\text{({\color{magenta}子列})几乎处处收敛}$};
      \node (measure) at (5, 0) {$\text{依测度收敛}$};
      \node (norm) at (-3, -4) {$\text{强收敛 (依范数收敛)}$};
      \node (weak) at (-3, -8) {$\text{弱收敛}$};

      \draw[arrows={-{Stealth[length=3mm, width=2mm]}}, transform canvas={xshift=0.5em}] (uniform) -- (ae) node[sloped, anchor=center, midway, below] {$\checkmark$};
      \draw[arrows={-{Stealth[length=3mm, width=2mm]}}, transform canvas={xshift=-0.5em}] (ae) -- (uniform) node[sloped, anchor=center, midway, above] {{\color{red}$\boldsymbol{\times}$}, ~~ {\color{cyan} Egorov ($m E < \infty$)}};

      \draw[arrows={-{Stealth[length=3mm, width=2mm]}}, transform canvas={yshift=0.3em}] (ae) -- (measure) node[sloped, anchor=center, midway, above] {{\color{red}$\boldsymbol{\times}$}, ~~ $m E < \infty$};
      \draw[arrows={-{Stealth[length=3mm, width=2mm]}}, transform canvas={yshift=-0.3em}] (measure) -- (ae) node[sloped, anchor=center, midway, below] {{\color{red}$\boldsymbol{\times}$}, ~~ {\color{magenta} Riesz ($m E < \infty$)}};

      \draw[arrows={-{Stealth[length=3mm, width=2mm]}}, transform canvas={xshift=0.5em}] (norm) -- (ae) node[sloped, anchor=center, midway, above] {\color{red}$\boldsymbol{\times}$};
      \draw[arrows={-{Stealth[length=3mm, width=2mm]}}, transform canvas={xshift=-0.5em}] (ae) -- (norm) node[sloped, anchor=center, midway, below] {{\color{red}$\boldsymbol{\times}$}, ~ $\lVert f_n \rVert_p \to \lVert f \rVert_p$};

      \draw[arrows={-{Stealth[length=3mm, width=2mm]}}, transform canvas={xshift=-0.8em}] (norm) -- (measure) node[sloped, anchor=center, midway, above] {$\checkmark$};
      \draw[arrows={-{Stealth[length=3mm, width=2mm]}}, transform canvas={xshift=0.8em}] (measure) -- (norm) node[sloped, anchor=center, midway, below] {{\color{red}$\boldsymbol{\times}$}, ~~ $\text{\smaller 等度绝对连续积分}$ ($m E < \infty$)};

      \draw[arrows={-{Stealth[length=3mm, width=2mm]}}, transform canvas={xshift=-0.3em}] (norm) -- (weak) node[midway, left] {$\checkmark$};
      \draw[arrows={-{Stealth[length=3mm, width=2mm]}}, transform canvas={xshift=0.3em}] (weak) -- (norm) node[midway, right] {\color{red}$\boldsymbol{\times}$};

      \draw[arrows={-{Stealth[length=3mm, width=2mm]}}, transform canvas={yshift=-0.3em}] (uniform) -- (weak) node[sloped, anchor=center, midway, below] {{\color{red}$\boldsymbol{\times}$}, ~~ $m E < \infty$};
      \draw[arrows={-{Stealth[length=3mm, width=2mm]}}, transform canvas={yshift=0.3em}] (weak) -- (uniform) node[sloped, anchor=center, midway, above] {\color{red}$\boldsymbol{\times}$};

      \draw[arrows={-{Stealth[length=3mm, width=2mm]}}, transform canvas={yshift=0.3em}] (uniform) -- (norm) node[sloped, anchor=center, midway, above] {{\color{red}$\boldsymbol{\times}$}, ~~ $m E < \infty$};
      \draw[arrows={-{Stealth[length=3mm, width=2mm]}}, transform canvas={yshift=-0.3em}] (norm) -- (uniform) node[sloped, anchor=center, midway, below] {{\color{red}$\boldsymbol{\times}$}};

      \draw[arrows={-{Stealth[length=3mm, width=2mm]}}, transform canvas={xshift=0.7em}] (measure) -- (weak) node[sloped, anchor=center, midway, above] {{\color{red}$\boldsymbol{\times}$}};
      \draw[arrows={-{Stealth[length=3mm, width=2mm]}}, transform canvas={xshift=1.6em}] (weak) -- (measure) node[sloped, anchor=center, midway, below] {{\color{red}$\boldsymbol{\times}$}};

   上图中, :math:`A \xrightarrow{\color{red} \boldsymbol{\times}} B` 表示 :math:`A` 不蕴含 (不能推出) :math:`B`,
   如果 :math:`\color{red} \times` 之后有注释, 则表示在某些条件下成立, 相应的结论也可能会弱一些 (对应括号中同颜色的文字).
   :math:`A \xrightarrow{\checkmark} B` 表示 :math:`A` 蕴含 :math:`B`. 还有要注意的是,
   讨论蕴含关系时, 都是在某个空间中进行讨论的, 例如, :math:`L^p` 空间等.

   - 几乎处处收敛但不依测度收敛的例子 (注意, 这里必须有 :math:`m E = \infty`):

     .. math::

         f_n(x) = \chi_{[n, n + 1]}(x), \quad n \in \mathbb{N}.

     可以验证 :math:`f_n(x)` 处处收敛到 :math:`0` 但不依测度收敛到 :math:`0`.

   - 依测度收敛但不几乎处处收敛的例子: :math:`E = [0, 1]`,

     .. math::
      :label: modes-of-convergence-eg-1

         f_n(x) = \chi_{\left[ \frac{i}{2^k}, \frac{i + 1}{2^k} \right]}(x), \quad n = 2^k + i, \quad 0 \leqslant i < 2^k.

     可以验证 :math:`f_n(x)` 依测度收敛到 :math:`0` 但不几乎处处 (实际上是, 处处都不) 收敛到 :math:`0`.

   - 强收敛但不几乎处处收敛的例子: :eq:`modes-of-convergence-eg-1` 中的函数序列也在 :math:`L^p(E)` 中的强收敛到 :math:`0`.

   - 依测度收敛但不强收敛的例子: 只要对 :eq:`modes-of-convergence-eg-1` 中的函数序列稍作修改即可:

     .. math::
         :label: modes-of-convergence-eg-2

         f_n(x) = 2^k \chi_{\left[ \frac{i}{2^k}, \frac{i + 1}{2^k} \right]}(x), \quad n = 2^k + i, \quad 0 \leqslant i < 2^k.

     可以验证 :math:`f_n(x)` 依测度收敛到 :math:`0` 但不强收敛到 :math:`0`.

   - 依测度收敛但不弱收敛的例子: :eq:`modes-of-convergence-eg-2` 中的函数序列也在 :math:`L^p(E)` 中的依测度收敛到 :math:`0`,
     但不弱收敛到 :math:`0`, 只要取 :math:`g(x) = 1 \in L^q(E)` 即可.

   - 一致收敛但不弱收敛 (也不强收敛) 的例子 (注意, 这里必须有 :math:`m E = \infty`):

     .. math::
         :label: modes-of-convergence-eg-3

         f_n(x) = \dfrac{1}{n} \chi_{[1, e^n]}(x),

     容易验证 :math:`f_n(x)` 一致收敛到 :math:`0`. 设 :math:`p, q > 1` 满足 :math:`\displaystyle \dfrac{1}{p} + \dfrac{1}{q} = 1`,
     则 :math:`f_n \in L^p(\mathbb{R})`. 取 :math:`\displaystyle g(x) = \dfrac{\chi_{[1, +\infty)}(x)}{x}`, 则 :math:`g \in L^q(\mathbb{R})`,
     但是

     .. math::

         \int_{\mathbb{R}} f_n(x) g(x) ~ \mathrm{d} x = \dfrac{1}{n} \int_{1}^{e^n} \dfrac{1}{x} ~ \mathrm{d} x = 1.

     因此, :math:`f_n` 不弱收敛到 :math:`0`, 因此也不强收敛到 :math:`0`.

   - 弱收敛但不一致收敛的例子: :math:`E = [0, 1)`,

     .. math::

         f_n(x) = x^n, \quad n \in \mathbb{N}.

     容易验证 :math:`f_n(x) \in L^p(E)` 且由控制收敛定理知, 对任意 :math:`g \in L^q(E) \subset L^1(E)`, 都有

     .. math::

         \lim_{n \to \infty} \int_{E} f_n(x) g(x) ~ \mathrm{d} m = \int_{E} \lim_{n \to \infty} f_n(x) g(x) ~ \mathrm{d} m = 0.

     故 :math:`f_n(x)` 弱收敛到 :math:`0`, 但不一致收敛到 :math:`0`.

   - 弱收敛但不强收敛的例子: :math:`E = (0, \pi)`,

     .. math::

         f_n(x) = \sin(nx), \quad n \in \mathbb{N}.

     容易验证 :math:`f_n(x) \in L^2(E)`. 由 :ref:`Riemann-Lebesgue 引理 <ex-4-24>`, 对任意可积函数 (特别地, :math:`L^2(E)` 中的函数) :math:`g(x)`,
     都有 :math:`\displaystyle \int_{0}^{\pi} f_n(x) g(x) ~ \mathrm{d} x \to 0`, 因此 :math:`f_n(x)` 弱收敛到 :math:`0`. 但是

     .. math::

         \lVert f_n \rVert_2^2 = \int_{0}^{\pi} \sin^2(nx) ~ \mathrm{d} x = \dfrac{\pi}{2},

     因此 :math:`f_n(x)` 不强收敛到 :math:`0`. 此外, :math:`f_n(x)` 也不几乎处处收敛到 :math:`0`.
