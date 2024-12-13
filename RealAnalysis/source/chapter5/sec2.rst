§2 :math:`L^p` 空间的可分性
------------------------------------------

.. _ex-5-22:

22. 设 :math:`\{ f_n \}` 是 :math:`L^2` 中的序列, :math:`\{ f_n \}` 依测度收敛于 :math:`f` 且 :math:`\lVert f_n \rVert_2 \leqslant K`,
    :math:`K` 为常数, 证明 :math:`f_n \xrightarrow{\text{弱}} f` (:math:`n \to \infty`).

.. proof:proof::

   由可积函数空间关于依测度收敛的完备性, 可知 :math:`f \in L^2`. 又由 Minkowski 不等式

   .. math::

      \lVert f_n - f \rVert_2 \leqslant \lVert f_n \rVert_2 + \lVert f \rVert_2,

   可以用函数列 :math:`f_n - f` 代替 :math:`f_n` 证明相关结论. 以下假设 :math:`f = 0`.

   由 Hölder 不等式, 对任意 :math:`g \in L^2` 有

   .. math::
      :label: ex-5-22-eq-1

      \int_E | f_n g | ~ \mathrm{d} m & = \int_{E_n} | f_n g | ~ \mathrm{d} m + \int_{E \setminus E_n} | f_n g | ~ \mathrm{d} m \\
      & \leqslant \left( \int_{E_n} |f_n|^2 ~ \mathrm{d} m \right)^{1/2} \left( \int_{E_n} |g|^2 ~ \mathrm{d} m \right)^{1/2}
                  + \varepsilon \int_{E \setminus E_n} | g | ~ \mathrm{d} m \\
      & \leqslant K \left( \int_{E_n} |g|^2 ~ \mathrm{d} m \right)^{1/2} + \varepsilon \lVert g \rVert_1.

   由勒贝格积分的绝对连续性, 对任意的 :math:`\varepsilon`, 存在 :math:`\delta > 0`,
   使得对任意满足 :math:`m A < \delta` 的 :math:`A \subset E` 有

   .. math::
      :label: ex-5-22-eq-2

      \int_A |g|^2 ~ \mathrm{d} m \leqslant \varepsilon^2.

   由 :math:`\{ f_n \}` 依测度收敛于 :math:`f = 0` 知, 对取好的 :math:`\varepsilon > 0` 有

   .. math::

      \lim_{n \to \infty} m E_n := \lim_{n \to \infty} m E(|f_n| > \varepsilon) = 0,

   也就是说, 对已经取好的 :math:`\delta > 0`, 可以选取 :math:`N > 0`, 使得对任意 :math:`n > N` 有

   .. math::

      m E_n < \delta.

   于是由 :eq:`ex-5-22-eq-2` 知

   .. math::

      \int_{E_n} |g|^2 ~ \mathrm{d} m \leqslant \varepsilon^2,

   代入 :eq:`ex-5-22-eq-1` 中有

   .. math::

      \int_E | f_n g | ~ \mathrm{d} m \leqslant (K + \lVert g \rVert_1) \cdot \varepsilon.

   以上表明了 :math:`\displaystyle \lim_{n \to \infty} \int_E | f_n g | ~ \mathrm{d} m = 0`,
   从而有 :math:`f_n \xrightarrow{\text{弱}} f` (:math:`n \to \infty`).

.. _ex-5-23:

23. 问在 :math:`L^2` 中弱收敛于 :math:`f` 的序列 :math:`\{ f_n \}` 是否依测度收敛?

.. proof:solution::

   不一定.

   反例: 取 :math:`E = (0, \pi)`, :math:`f_n(x) = \sin(nx)`, :math:`n \in \mathbb{N}`. 容易验证 :math:`f_n(x) \in L^2(E)`.
   由 :ref:`Riemann-Lebesgue 引理 <ex-4-24>`, 对任意可积函数 (特别地, :math:`L^2(E)` 中的函数) :math:`g(x)`, 都有

   .. math::

      \lim_{n \to \infty} \int_{(0, \pi)} f_n g ~ \mathrm{d} m = 0.

   因此 :math:`f_n(x)` 弱收敛到 :math:`0`. 但是对足够小的 :math:`\varepsilon > 0`, 有

   .. math::

      E(|f_n| > \varepsilon) = \bigcup_{k = 0}^{n - 1}
      \left( \dfrac{k\pi + \arcsin \varepsilon}{n}, \dfrac{k\pi + \pi - \arcsin \varepsilon}{n} \right),

   于是

   .. math::

      E(|f_n| > \varepsilon) = \sum_{k = 0}^{n - 1} \dfrac{\pi - 2 \arcsin \varepsilon}{n} = \pi - 2 \arcsin \varepsilon,

   由此可知 :math:`f_n` 不依测度收敛到 :math:`0`.

.. _ex-5-27:

27. 设 :math:`E` 为可测集, :math:`m E < \infty`, :math:`f \in L^{\infty}(E)` 且 :math:`\lVert f \rVert_{\infty} > 0`.
    令 :math:`\displaystyle C_n = \int_E |f|^n ~ \mathrm{d} m`,
    证明 :math:`\displaystyle \lVert f \rVert_{\infty} = \lim_{n \to \infty} C_{n + 1} / C_n`.

.. proof:proof::

   由于 :math:`m E < \infty`, :math:`f \in L^{\infty}(E)`, 且 :math:`\lVert f \rVert_{\infty} > 0`,
   可以考虑 :math:`g = f / \lVert f \rVert_{\infty}`,
   则有 :math:`\displaystyle C_n = \lVert f \rVert_{\infty}^n \int_E |g|^n ~ \mathrm{d} m`.
   故可以不妨设 :math:`\lVert f \rVert_{\infty} = 1`, 并证明 :math:`\displaystyle 1 = \lim_{n \to \infty} C_{n + 1} / C_n`.

   首先, 由 Hölder 不等式, 对任意 :math:`n \in \mathbb{N}`, 有

   .. math::

      C_{n + 1} & = \int_E |f|^{n + 1} ~ \mathrm{d} m = \int_E |f|^n |f| ~ \mathrm{d} m \\
      & \leqslant \lVert |f|^n \rVert_1 \lVert f \rVert_{\infty} = \int_E |f|^n ~ \mathrm{d} m = C_n,

   于是

   .. math::
      :label: ex-5-27-eq-1

      \varlimsup_{n \to \infty} \dfrac{C_{n + 1}}{C_n} \leqslant 1.

   另一方面, 由于 :math:`1` 为 :math:`f` 的本性上确界, 故对任意 :math:`0 < r < 1`, 集合

   .. math::

      A_r = E(|f| > r)

   有正测度, 即 :math:`m A_r > 0`. 那么

   .. math::

      C_{n + 1} = \int_E |f|^{n+1} ~ \mathrm{d} m
      & \geqslant \int_{A_r} |f|^{n+1} ~ \mathrm{d} m \geqslant r \int_{A_r} |f|^n ~ \mathrm{d} m \\
      & = r C_n - r \int_{E \setminus A_r} |f|^n ~ \mathrm{d} m \\
      & \geqslant r C_n - r \cdot r^n m (E \setminus A_r) \\
      & = r C_n - r^{n + 1} m (E \setminus A_r),

   即有不等式

   .. math::
      :label: ex-5-27-eq-2

      \dfrac{C_{n + 1}}{C_n} \geqslant r - r^{n + 1} \dfrac{m (E \setminus A_r)}{C_n}.

   取实数 :math:`s` 满足 :math:`r < s < 1`, 那么集合

   .. math::

      A_s = E(|f| > s)

   也有正测度, 即 :math:`m A_s > 0,` 并且有

   .. math::

      C_n = \int_E |f|^n ~ \mathrm{d} m \geqslant \int_{A_s} |f|^n ~ \mathrm{d} m \geqslant s^n \cdot m A_s.

   将上式代入 :eq:`ex-5-27-eq-2` 即有

   .. math::

      \dfrac{C_{n + 1}}{C_n} \geqslant r - r \dfrac{m (E \setminus A_r)}{m A_s} \left(\dfrac{r}{s}\right)^n

   对上式关于 :math:`n \to \infty` 取下极限, 即有

   .. math::

      \varliminf_{n \to \infty} \dfrac{C_{n + 1}}{C_n} \geqslant r.

   由于上式对任意的 :math:`0 < r < 1` 都成立 (或者说对上式取极限 :math:`r \to 1-`), 所以有

   .. math::
      :label: ex-5-27-eq-3

      \varliminf_{n \to \infty} \dfrac{C_{n + 1}}{C_n} \geqslant 1.

   :eq:`ex-5-27-eq-1`, :eq:`ex-5-27-eq-3` 两式相结合即有 :math:`\displaystyle \lim_{n \to \infty} C_{n + 1} / C_n = 1`.

   .. note::

      当 :math:`m E < \infty` 且 :math:`f \in L^{\infty}(E)` 时, 成立

      .. math::

         \lim_{p \to \infty} \lVert f \rVert_p = \lVert f \rVert_{\infty},

      特别地对 :math:`n \in \mathbb{N}` 有

      .. math::
         :label: ex-5-27-eq-4

         \lim_{n \to \infty} \lVert f \rVert_n = \lVert f \rVert_{\infty}.

      本题添加了条件 :math:`\lVert f \rVert_{\infty} > 0`, 进而得到的结论

      .. math::
         :label: ex-5-27-eq-5

         \lVert f \rVert_{\infty} = \lim_{n \to \infty} \dfrac{C_{n + 1}}{C_n}
         = \lim_{n \to \infty} \dfrac{\lVert f \rVert_{n+1}^{n+1}}{\lVert f \rVert_n}

      是要强于 :eq:`ex-5-27-eq-4` 的. 实际上, 令 :math:`a_n = \ln C_{n + 1} - \ln C_n`, 并约定 :math:`a_n = \ln C_1`.
      那么 :eq:`ex-5-27-eq-4` 实际上说的是

      .. math::
         :label: ex-5-27-eq-6

         \dfrac{1}{n} \sum_{k = 1}^n a_k \to \ln \lVert f \rVert_{\infty}, \quad n \to \infty.

      而 :eq:`ex-5-27-eq-5` 实际上说的是

      .. math::
         :label: ex-5-27-eq-7

         a_n \to \ln \lVert f \rVert_{\infty}, \quad n \to \infty.

      对一般的数列 :math:`\{ a_n \}` 来说, :eq:`ex-5-27-eq-7` 是要严格强于 :eq:`ex-5-27-eq-6` 的.
      相关知识可查阅级数的 Cesàro 求和法.

.. _ex-5-31:

31. 设 :math:`I` 为实轴上的一区间, :math:`\varphi` 为 :math:`I` 上的实函数. 称 :math:`\varphi` 为 :math:`I` 上凸函数,
    如果对任何 :math:`x, y \in I` 和任意 :math:`t \in (0, 1)` 有

    .. math::

      \varphi(tx + (1 - t)y) \leqslant t\varphi(x) + (1 - t)\varphi(y).

    试证:

    (1) :math:`\varphi` 在 :math:`I` 的每个内点处连续;

    (2) 设 :math:`(X, \mathscr{R}, \mu)` 为有限测度空间, 若 :math:`f` 为 :math:`X` 上实可积函数且 :math:`f` 的值域含于 :math:`I`,
        则有延森 (B. Jensen) 不等式

        .. math::

            \varphi \left( \dfrac{1}{\mu X} \int_X f ~ \mathrm{d} \mu \right)
            \leqslant \dfrac{1}{\mu X} \int_X \varphi(f) ~ \mathrm{d} \mu.

.. proof:proof::

   (1) 任取 :math:`x \in I` 为 :math:`I` 的内点, 于是存在区间 :math:`[a, b] \subset I` 使得 :math:`x \in (a, b)`.
   任取点列 :math:`\{ x_n \} \subset (x, b)` 使得 :math:`x_n \to x +`, 并记 :math:`t_n = (x_n - x) / (b - x)`, 则有

   .. math::

      x_n = t_n b + (1 - t_n) x,

   并且

   .. math::

      t_n \to 0 (n \to \infty).

   由于 :math:`\varphi` 为凸函数, 有

   .. math::

      \varphi(x_n) \leqslant t_n \varphi(b) + (1 - t_n) \varphi(x) = \varphi(x) + t_n (\varphi(b) - \varphi(x)).

   对上式两边关于 :math:`n \to \infty` 取上极限, 有

   .. math::
      :label: ex-5-31-eq-1

      \varlimsup_{n \to \infty} \varphi(x_n) \leqslant \varphi(x).

   另一方面, 记 :math:`s_n = (x_n - x) / (x_n - a)`, 则有

   .. math::

      x = s_n a + (1 - s_n) x_n,

   并且

   .. math::

      s_n \to 0 (n \to \infty).

   由于 :math:`\varphi` 为凸函数, 有

   .. math::

      \varphi(x) \leqslant s_n \varphi(x_n) + (1 - s_n) \varphi(a) = \varphi(a) + s_n (\varphi(x_n) - \varphi(a)).

   对上式两边关于 :math:`n \to \infty` 取下极限, 有

   .. math::
      :label: ex-5-31-eq-2

      \varphi(x) \leqslant \varliminf_{n \to \infty} \varphi(x_n).

   由 :eq:`ex-5-31-eq-1`, :eq:`ex-5-31-eq-2` 两式相结合即有

   .. math::

      \varphi(x) = \lim_{n \to \infty} \varphi(x_n).

   由于点列 :math:`\{ x_n \}` 的任意性, 知 :math:`\varphi` 在 :math:`x` 右连续. 同理可证 :math:`\varphi` 在 :math:`x` 左连续.

   (2) 由于 :math:`f` 为 :math:`X` 上实可积函数, 取简单函数列 :math:`\{ g_n \}` 使得

   .. math::

      \lim_{n \to \infty} \int_X g_n ~ \mathrm{d} \mu = \int_X f ~ \mathrm{d} \mu.

   对于 :math:`\displaystyle g_n = \sum_{k = 1}^{N_n} a_{nk} \chi_{E_{nk}}`, :math:`\displaystyle X = \bigcup_{k = 1}^{N_n} E_{nk}`,
   且 :math:`E_{nk}` 两两不交, 有

   .. math::

      \varphi \left( \dfrac{1}{\mu X} \int_X g_n ~ \mathrm{d} \mu \right)
      & = \varphi \left( \sum_{k = 1}^{N_n} \dfrac{\mu E_{nk}}{\mu X} a_{nk} \right) \\
      & \leqslant \sum_{k = 1}^{N_n} \dfrac{\mu E_{nk}}{\mu X} \varphi \left( a_{nk} \right)
        = \dfrac{1}{\mu X} \int_X \varphi(g_n) ~ \mathrm{d} \mu.

   由 :math:`\varphi` 的连续性, 两边取极限即有

   .. math::

      \varphi \left( \dfrac{1}{\mu X} \int_X f ~ \mathrm{d} \mu \right)
      \leqslant \dfrac{1}{\mu X} \int_X \varphi(f) ~ \mathrm{d} \mu.
