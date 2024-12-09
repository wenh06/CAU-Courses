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

   设 :math:`f_n \to g ~ (n \to \infty)` 对任意 :math:`x \in F = E \setminus e` 成立, 其中 :math:`e` 是零测集.
   那么由 Fatou 引理有

   .. math::

      \int_E |f - g|^2 ~ \mathrm{d} m
      & = \int_F |f - g|^2 ~ \mathrm{d} m = \int_F \lim_{n \to \infty} |f - f_n|^2 ~ \mathrm{d} m \\
      & \leqslant \varliminf_{n \to \infty} \int_F |f - f_n|^2 ~ \mathrm{d} m
        = \varliminf_{n \to \infty} \int_E |f - f_n|^2 ~ \mathrm{d} m \\
      & = \varliminf_{n \to \infty} \lVert f - f_n \rVert_2^2 = 0.

   由勒贝格积分的唯一性知 :math:`|f - g|^2 \sim 0`, 即 :math:`f \sim g`.

.. _ex-5-4:

4. 设 :math:`f, f_n \in L^p ~ (p \geqslant 1)`, :math:`f_n \xrightarrow{\text{a.e.}} f`, 又设

   .. math::

      \int_E |f_n|^p ~ \mathrm{d} m \to \int_E |f|^p ~ \mathrm{d} m.

   证明对任何可测子集 :math:`e \subset E`, 有

   .. math::

      \int_e |f_n|^p ~ \mathrm{d} m \to \int_e |f|^p ~ \mathrm{d} m.

.. proof:proof::

   这题是 :ref:`上一章第 4 章第 20 题 <ex-4-20>` 的平凡推广.

.. _ex-5-5:

5. 设 :math:`f, f_n \in L^p ~ (p \geqslant 1)`, :math:`f_n \xrightarrow{\text{a.e.}} f`. 证明在 :math:`L^p` 中
   :math:`f_n \xrightarrow{\text{强}} f` 的充要条件是 :math:`\lVert f_n \rVert_p \to \lVert f \rVert_p`.

.. proof:proof::

   必要性: 由 Minkowski 不等式, 对任意 :math:`n \in \mathbb{N}` 有

   .. math::
      :label: ex-5-5-eq-1

      \lVert f_n - f \rVert_p + \lVert f_n \rVert_p \geqslant \lVert f \rVert_p.

   对上式关于 :math:`n` 取下极限, 有

   .. math::
      :label: ex-5-5-eq-2

      \varliminf_{n \to \infty} \lVert f_n \rVert_p \geqslant \lVert f \rVert_p.

   类似地, 对任意 :math:`n \in \mathbb{N}` 有

   .. math::
      :label: ex-5-5-eq-3

      \lVert f - f_n \rVert_p + \lVert f \rVert_p \geqslant \lVert f_n \rVert_p.

   对上式关于 :math:`n` 取上极限, 有

   .. math::
      :label: ex-5-5-eq-4

      \varlimsup_{n \to \infty} \lVert f_n \rVert_p \leqslant \lVert f \rVert_p.

   综合 :eq:`ex-5-5-eq-2` 与 :eq:`ex-5-5-eq-4`, 得到 :math:`\lVert f_n \rVert_p \to \lVert f \rVert_p`.

   充分性: 由于零测集不影响可积性与积分值, 故不妨设 :math:`f_n \to f ~ (n \to \infty)` 对任意 :math:`x \in E` 成立.
   对于任意 :math:`1 \leqslant p < \infty`, 由于 :math:`\varphi(t) = t^p` 是凸函数, 故

   .. math::

      | f_n - f |^p = 2^p \left\lvert \dfrac{f_n - f}{2} \right\rvert^p \leqslant 2^{p - 1} \left( |f_n|^p + |f|^p \right).

   令 :math:`g_n = 2^{p - 1} \left( |f_n|^p + |f|^p \right) - | f_n - f |^p` 为非负可测函数. 由于 :math:`f_n \to f ~ (n \to \infty)`,
   故有 :math:`g_n \to 2^p |f|^p` 对任意 :math:`x \in E` 成立. 由 Fatou 引理知

   .. math::

      \int_E \lim_{n \to \infty} g_n ~ \mathrm{d} m \leqslant \varliminf_{n \to \infty} \int_E g_n ~ \mathrm{d} m,

   即有

   .. math::

      \int_E 2^p |f|^p ~ \mathrm{d} m
      & \leqslant \varliminf_{n \to \infty} \int_E 2^{p - 1} \left( |f_n|^p + |f|^p - | f_n - f |^p \right) ~ \mathrm{d} m \\
      & = \int_E 2^{p - 1} |f|^p ~ \mathrm{d} m + \lim_{n \to \infty} 2^{p - 1} \int_E |f_n|^p ~ \mathrm{d} m
          - \varlimsup_{n \to \infty} \int_E | f_n - f |^p ~ \mathrm{d} m \\
      & = \int_E 2^p |f|^p ~ \mathrm{d} m - \varlimsup_{n \to \infty} \int_E | f_n - f |^p ~ \mathrm{d} m.

   由上式可得

   .. math::

      \varlimsup_{n \to \infty} \int_E | f_n - f |^p ~ \mathrm{d} m \leqslant 0,

   这表明有 :math:`\lVert f_n - f \rVert_p \to 0`, 即 :math:`f_n \xrightarrow{\text{强}} f`.

.. _ex-5-6:

6. 试作依赖于给定函数 :math:`f` 的连续函数序列 :math:`\{ f_n \}` 使得对任何 :math:`p`, :math:`1 \leqslant p < \infty` 时,
   都有 :math:`f_n \xrightarrow{\text{强}} f ~ (n \to \infty)`. 又问此结论能否包括 :math:`p = \infty` 的情形?

.. proof:solution::

.. _ex-5-7:

7. 设 :math:`1 \leqslant p < q \leqslant \infty`, 问两关系式 :math:`L^q(\mathbb{R}) \subset L^p(\mathbb{R})` 与
   :math:`L^p(\mathbb{R}) \subset L^q(\mathbb{R})` 是否必有一成立?

.. proof:solution::

   :math:`L^q(\mathbb{R})` 与 :math:`L^p(\mathbb{R})` 之间的没有包含关系. 相关的例子见 :ref:`本章第 1 题 <ex-5-1>`,
   只要将其中的函数从 :math:`(0, +\infty)` 扩展到整个实数轴即可, 函数在扩充的区域 :math:`(-\infty, 0)` 上取零即可.

.. _ex-5-8:

8. 设 :math:`f \in L^p(0, \pi/2)`, :math:`1 \leqslant p < \infty`. 试证

   .. math::

      \left( \int_{(0, \pi/2)} |f(x)| \cos x ~ \mathrm{d} m \right)^p \leqslant \int_{(0, \pi/2)} |f(x)|^p \cos x ~ \mathrm{d} m.

.. proof:proof::

   :math:`p = 1` 时, 上式平凡成立, 为恒等式.

   对 :math:`p > 1` 的情形, 令 :math:`q > 1` 满足 :math:`1/p + 1/q = 1`.
   由于在 :math:`(0, \pi/2)` 上有 :math:`0 < \cos x < 1`, 故 :math:`\cos x` 及其任意正次幂都是可积函数. 由 Hölder 不等式知

   .. math::

      \int_{(0, \pi/2)} |f(x)| \cos x ~ \mathrm{d} m
      & = \int_{(0, \pi/2)} \left( |f(x)| (\cos x)^{1/p} \right) \cdot (\cos x)^{1/q} ~ \mathrm{d} m \\
      & \leqslant \left( \int_{(0, \pi/2)} |f(x)|^p \cos x ~ \mathrm{d} m \right)^{1/p} \left( \int_{(0, \pi/2)} \cos x ~ \mathrm{d} m \right)^{1/q} \\
      & = \left( \int_{(0, \pi/2)} |f(x)|^p \cos x ~ \mathrm{d} m \right)^{1/p} \cdot \left( (R)\int_0^{\pi/2} \cos x ~ \mathrm{d} x \right)^{1/q} \\
      & = \left( \int_{(0, \pi/2)} |f(x)|^p \cos x ~ \mathrm{d} m \right)^{1/p} \cdot \left( \sin x \big|_0^{\pi/2} \right)^{1/q} \\
      & = \left( \int_{(0, \pi/2)} |f(x)|^p \cos x ~ \mathrm{d} m \right)^{1/p}.

   上式两边取 p 次幂即得

   .. math::

      \left( \int_{(0, \pi/2)} |f(x)| \cos x ~ \mathrm{d} m \right)^p \leqslant \int_{(0, \pi/2)} |f(x)|^p \cos x ~ \mathrm{d} m.

.. _ex-5-9:

9. 设对任意 :math:`1 \leqslant p < \infty` 均有 :math:`f \in L^p(E)`, 这里 :math:`m E < \infty`, 问 :math:`f \in L^\infty(E)` 是否成立?
   又若对任意 :math:`0 < p < 1` 均有 :math:`f \in L^p(E)`, 是否有 :math:`f \in L^1(E)`?

.. proof:solution::

   若对任意 :math:`1 \leqslant p < \infty` 均有 :math:`f \in L^p(E)`, :math:`f \in L^\infty(E)` 不一定成立. 例如, 取 :math:`E = (0, 1)`, 以及函数

   .. math::

      f(x) = \ln \left( \dfrac{1}{x} \right),

   由于 :math:`\displaystyle \lim_{x \to 0^+} f(x) = +\infty`, 故 :math:`f \not\in L^\infty(E)`.
   另一方面, 对任意 :math:`1 \leqslant p < \infty`, 有

   .. math::

      \lim_{x \to 0^+} \dfrac{\left( \ln \left( \frac{1}{x} \right) \right)^p}{x^{-1/2}} = \lim_{t \to +\infty} \dfrac{t^p}{e^{t/2}} = 0,

   而 :math:`\displaystyle \int_{(0, 1)} x^{-1/2} ~ \mathrm{d} x = 2 < \infty`, 故 :math:`f \in L^p(E)`.

   若对任意 :math:`0 < p < 1` 均有 :math:`f \in L^p(E)`, :math:`f \in L^1(E)` 也不一定成立. 例如, 取 :math:`E = (0, 1)`, 以及函数

   .. math::

      f(x) = \dfrac{1}{x}.

   对任意 :math:`0 < p < 1`, 有

   .. math::

      \int_{(0, 1)} \dfrac{1}{x^p} ~ \mathrm{d} m = (R) \int_0^1 x^{-p} ~ \mathrm{d} x
      = \dfrac{1}{1 - p} x^{1 - p} \bigg|_0^1 = \dfrac{1}{1 - p} < \infty,

   故 :math:`f \in L^p(E)`. 但是 :math:`(0, 1)` 上的非负函数 :math:`f(x)` 的反常积分

   .. math::

      \int_0^1 x^{-1} ~ \mathrm{d} x = \ln x \bigg|_0^1 = +\infty,

   故 :math:`f \not\in L^1(E)`.

.. _ex-5-10:

10. 设 :math:`F(x)` 是 :math:`L^p ~ (p > 1)` 中某个元的不定积分, 证明渐近式

    .. math::

      F(x + h) - F(x) = O(h^{1 - 1/p}) \quad (h \to 0)

    成立.

.. proof:proof::

   设 :math:`f \in L^p` 为 :math:`F(x)` 的不定积分. 对任意 :math:`x, h`, 记 :math:`E_h` 为以 :math:`x, x + h` 为端点的区间.
   令 :math:`q > 1` 满足 :math:`1/p + 1/q = 1`, 由 Hölder 不等式有

   .. math::
      :label: ex-5-10-eq-1

      \lvert F(x + h) - F(x) \rvert & = \left\lvert \int_{E_h} f ~ \mathrm{d} m \right\rvert \leqslant \int_{E_h} |f| ~ \mathrm{d} m \\
      & \leqslant \left( \int_{E_h} |f|^p ~ \mathrm{d} m \right)^{1/p} \left( \int_{E_h} 1 ~ \mathrm{d} m \right)^{1/q} \\
      & = \left( \int_{E_h} |f|^p ~ \mathrm{d} m \right)^{1/p} \cdot |h|^{1/q} \\
      & = \left( \int_{E_h} |f|^p ~ \mathrm{d} m \right)^{1/p} \cdot |h|^{1 - 1/p}.

   由勒贝格积分的绝对连续性知, 对任意给定的 :math:`\varepsilon > 0`, 存在 :math:`\delta > 0`,
   使得对任意满足 :math:`m E_h < \delta` (即满足 :math:`|h| < \dleta`) 的区间 :math:`E_h` 有

   .. math::

      \left( \int_{E_h} |f|^p ~ \mathrm{d} m \right)^{1/p} < \varepsilon,

   代入 :eq:`ex-5-10-eq-1` 即得

   .. math::
      :label: ex-5-10-eq-2

      \lvert F(x + h) - F(x) \rvert < \varepsilon^{1/p} \cdot |h|^{1 - 1/p},

   即 :math:`F(x + h) - F(x) = O(h^{1 - 1/p})`. 从 :eq:`ex-5-10-eq-2` 可可以看出,
   我们实际证明了一个更强的结论, 即 :math:`F(x + h) - F(x) = o(h^{1 - 1/p})`.
