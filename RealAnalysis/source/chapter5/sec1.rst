§1 :math:`L^p` 空间 · 完备性
------------------------------------------

.. _ex-5-1:

1. 试证: 当 :math:`m E < \infty` 时, 对 :math:`1 \leqslant r < p` 有 :math:`L^p \subset L^r`. 当 :math:`m E = \infty` 时, 结论如何?

.. proof:proof::

   :math:`1^{\circ}` 当 :math:`p = \infty` 时, 存在非负实数 :math:`M`, 以及零测集 :math:`e \subset E`,
   使得对任意 :math:`x \in E \setminus e` 有 :math:`|f(x)| \leqslant M`. 于是

   .. math::

      \int_E |f|^r ~ \mathrm{d} m = \int_{E \setminus e} |f|^r ~ \mathrm{d} m \leqslant M^r m E < \infty,

   即 :math:`f \in L^r`. 因此 :math:`L^\infty \subset L^r`.

   :math:`2^{\circ}` 当 :math:`p < \infty` 时, 由于 :math:`f \in L^p`, 故 :math:`\displaystyle \int_E |f|^p ~ \mathrm{d} m < \infty`.
   令 :math:`A = E(|f| \geqslant 1)`, 由于 :math:`1 \leqslant r < p`, 故对任意 :math:`x \in A` 有 :math:`|f(x)|^r \leqslant |f(x)|^p`. 于是

   .. math::

      \int_E |f|^r ~ \mathrm{d} m & = \int_A |f|^r ~ \mathrm{d} m + \int_{E \setminus A} |f|^r ~ \mathrm{d} m \\
      & \leqslant \int_A |f|^p ~ \mathrm{d} m + m E \leqslant \int_E |f|^p ~ \mathrm{d} m + m E < \infty,

   即 :math:`f \in L^r`. 因此 :math:`L^p \subset L^r`.

   :math:`3^{\circ}` 当 :math:`m E = \infty` 时, :math:`L^p` 与 :math:`L^r` 没有包含关系. 例如, 取 :math:`E = (0, +\infty)`.
   当 :math:`p = \infty` 时,

   - 取 :math:`f(x) = 1`, 则 :math:`f \in L^\infty`, 但 :math:`f \not\in L^r`;
   - 取 :math:`f(x) = \begin{cases} x^{-1/2r}, & x \leqslant 1, \\ 0, & x > 1, \end{cases}` 则 :math:`f \in L^r`, 但 :math:`f \not\in L^\infty`.

   当 :math:`p < \infty` 时,

   - 取 :math:`f(x) = \begin{cases} x^{-1/p}, & x \leqslant 1, \\ 0, & x > 1, \end{cases}` 则 :math:`f \in L^r`, 但 :math:`f \not\in L^p`;
   - 取 :math:`f(x) = \begin{cases} x^{-1/r}, & x \geqslant 1, \\ 0, & x < 1, \end{cases}` 则 :math:`f \in L^p`, 但 :math:`f \not\in L^r`.

.. _ex-5-2:

2. 设 :math:`p > 1`, 序列 :math:`\{ f_n \} \subset L^p` 并设基本集 :math:`E` 的测度为有限.
   若在 :math:`L^p` 中 :math:`f_n \xrightarrow{\text{强}} f`, :math:`f \in L^p`,
   证明当 :math:`1 \leqslant r < p` 时在 :math:`L^r` 中 :math:`f_n \xrightarrow{\text{强}} f`.

.. proof:proof::

   由 :ref:`本章第 1 题 <ex-5-1>` 知 :math:`L^p \subset L^r`, 故 :math:`f_n \in L^r`.
   由 :math:`L^p` 以及 :math:`L^r` 的完备性知 :math:`f \in L^p \subset L^r`. 先对 :math:`p < \infty` 的情形证明.
   由于在 :math:`L^p` 中 :math:`f_n \xrightarrow{\text{强}} f`, 即有

   .. math::

      \lim_{n \to \infty} \lVert f_n - f \rVert_p = 0.

   取实数 :math:`q > 1`, 使得 :math:`1/p + 1/q = 1/r`, 对一般的 :math:`E` 上可测函数 :math:`g_1, g_2`,
   考虑函数 :math:`|g_1|^r` 与 :math:`|g_2|^r`, 以及 :math:`1/(\frac{p}{r}) + 1/(\frac{q}{r}) = 1`, 由 Hölder 不等式知

   .. math::

      \int_E |g_1 g_2|^r ~ \mathrm{d} m
      \leqslant \left( \int_E (|g_1|^r)^{p/r} ~ \mathrm{d} m \right)^{r/p} \left( \int_E (|g_2|^r)^{q/r} ~ \mathrm{d} m \right)^{r/q}
      = \lVert g_1 \rVert_p^r \lVert g_2 \rVert_q^r.

   对上式两边开 r 次方, 有

   .. math::

      \lVert g_1 g_2 \rVert_r \leqslant \lVert g_1 \rVert_p \lVert g_2 \rVert_q.

   由于 :math:`E` 的测度有限, 取 :math:`g_1 = f_n - f`, :math:`g_2 = 1`, 有

   .. math::

      \lVert f_n - f \rVert_r \leqslant \lVert f_n - f \rVert_p \cdot \lVert 1 \rVert_q
      = \lVert f_n - f \rVert_p \cdot m E^{1/q} \to 0 \quad (n \to \infty).

   即 :math:`f_n \xrightarrow{\text{强}} f` 在 :math:`L^r` 中成立.

   当 :math:`p = \infty` 时, 由条件知 :math:`\displaystyle \lim_{n \to \infty} \lVert f_n - f \rVert_\infty = 0`,
   那么对任意给定的 :math:`\varepsilon > 0`, 存在 :math:`N`, 使得对任意 :math:`n > N` 有 :math:`\lVert f_n - f \rVert_\infty < \varepsilon`.
   也就是说存在零测集 :math:`e_n \subset E`, 使得对任意 :math:`x \in E \setminus e_n` 有 :math:`|f_n(x) - f(x)| < 2\varepsilon`. 于是

   .. math::

      \int_E |f_n - f|^r ~ \mathrm{d} m = \int_{E \setminus e_n} |f_n - f|^r ~ \mathrm{d} m  \leqslant 2^r \varepsilon^r m E.

   对上式两边开 r 次方, 可得对任意 :math:`n > N` 有

   .. math::

      \lVert f_n - f \rVert_r \leqslant 2 \varepsilon (m E)^{1/r}.

   这就表明了 :math:`\displaystyle \lim_{n \to \infty} \lVert f_n - f \rVert_r = 0`, 即 :math:`f_n \xrightarrow{\text{强}} f` 在 :math:`L^r` 中成立.

.. _ex-5-3:

3. 设在 :math:`L^2` 中 :math:`f_n \xrightarrow{\text{强}} f`, 又 :math:`f_n \xrightarrow{\text{a.e.}} g`, 证明 :math:`f \sim g`.

.. proof:proof::
