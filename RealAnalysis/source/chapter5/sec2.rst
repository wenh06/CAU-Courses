§2 :math:`L^p` 空间的可分性
------------------------------------------

.. _ex-5-22:

22. 设 :math:`\{ f_n \}` 是 :math:`L^2` 中的序列, :math:`\{ f_n \}` 依测度收敛于 :math:`f` 且
    :math:`\lVert f_n \rVert_2 \leqslant K`, :math:`K` 为常数, 证明
    :math:`f_n \xrightarrow{\text{弱}} f` (:math:`n \to \infty`).

.. proof:proof::

   由可积函数空间关于依测度收敛的完备性, 可知 :math:`f \in L^2`，所以可以用函数列 :math:`f_n - f` 代替 :math:`f_n` 证明相关结论.
   以下假设 :math:`f = 0`.

   任取 :math:`g \in L^2`, 需要证明 :math:`\displaystyle \lim_{n \to \infty} \int_E | f_n g | ~ \mathrm{d} m = 0`.
   由于 :math:`g \in L^2`, 考虑集合 :math:`E_t = E \cap [-t, t]`, :math:`t \in \mathbb{N}`, 则由 Levi 定理知

   .. math::
      \lim_{t \to \infty} \int_{E_t} |g|^2 ~ \mathrm{d} m
      = \lim_{t \to \infty} \int_{E} |g|^2 \chi_{E_t} ~ \mathrm{d} m
      = \int_{E} \lim_{t \to \infty} |g|^2 \chi_{E_t} ~ \mathrm{d} m
      = \int_{E} |g|^2 ~ \mathrm{d} m
      = \lVert g \rVert_2^2 < \infty,

   因此存在 :math:`N > 0`, 使得对任意 :math:`t > N` 有

   .. math::
      \int_{E \setminus E_t} |g|^2 ~ \mathrm{d} m < \varepsilon^2.

   记 :math:`A = E_N`. 注意, 集合 :math:`A` 的测度是有限的, 从而有 :math:`L^2(A) \subset L^1(A)`.
   由 Hölder 不等式, 对于任意的 :math:`n \in \mathbb{N}`, 有

   .. math::
      :label: ex-5-22-eq-1

      \int_A | f_n g | ~ \mathrm{d} m
      & = \int_{A_n} | f_n g | ~ \mathrm{d} m + \int_{A \setminus A_n} | f_n g | ~ \mathrm{d} m \\
      & \leqslant \left( \int_{A_n} |f_n|^2 ~ \mathrm{d} m \right)^{1/2}
                  \left( \int_{A_n} |g|^2 ~ \mathrm{d} m \right)^{1/2}
                  + \varepsilon \int_{A \setminus A_n} | g | ~ \mathrm{d} m \\
      & \leqslant K \left( \int_{A_n} |g|^2 ~ \mathrm{d} m \right)^{1/2}
                  + \varepsilon \lVert g \rVert_{1,A},

   其中 :math:`A_n = A \cap E \left( |f_n| \geqslant \varepsilon \right)`,
   :math:`\lVert g \rVert_{1,A} = \int_A |g| ~ \mathrm{d} m` 表示 :math:`g` 在集合 :math:`A` 上的 :math:`L^1` 范数.
   由勒贝格积分的绝对连续性, 对任意的 :math:`\varepsilon > 0`, 存在 :math:`\delta > 0`,
   使得对任意满足 :math:`m B < \delta` 的 :math:`B \subset A` 有

   .. math::
      :label: ex-5-22-eq-2

      \int_B |g|^2 ~ \mathrm{d} m \leqslant \varepsilon^2.

   由 :math:`\{ f_n \}` 依测度收敛于 :math:`f = 0` 知, 对取好的 :math:`\varepsilon > 0` 有

   .. math::
      \lim_{n \to \infty} m A_n = \lim_{n \to \infty} m (A \cap E(|f_n| \geqslant \varepsilon)) = 0.

   也就是说, 对已经取好的 :math:`\delta > 0`, 可以选取 :math:`M > 0`, 使得对任意 :math:`n > M` 有

   .. math::
      m A_n < \delta.

   于是由 :eq:`ex-5-22-eq-2` 知

   .. math::
      \int_{A_n} |g|^2 ~ \mathrm{d} m \leqslant \varepsilon^2.

   代入 :eq:`ex-5-22-eq-1` 中有

   .. math::
      :label: ex-5-22-eq-3

      \int_A | f_n g | ~ \mathrm{d} m \leqslant (K + \lVert g \rVert_{1,A}) \varepsilon.

   另一方面, 对于 :math:`E \setminus A`, 由 Hölder 不等式有

   .. math::
      :label: ex-5-22-eq-4

      \int_{E \setminus A} | f_n g | ~ \mathrm{d} m
      & \leqslant \left( \int_{E \setminus A} |f_n|^2 ~ \mathrm{d} m \right)^{1/2}
        \left( \int_{E \setminus A} |g|^2 ~ \mathrm{d} m \right)^{1/2} \\
      & \leqslant K \left( \int_{E \setminus A} |g|^2 ~ \mathrm{d} m \right)^{1/2}
      < K \varepsilon.

   综合 :eq:`ex-5-22-eq-3`, :eq:`ex-5-22-eq-4` 两式, 可知对任意 :math:`n > M` 有

   .. math::
      \int_E | f_n g | ~ \mathrm{d} m
      = \int_A | f_n g | ~ \mathrm{d} m + \int_{E \setminus A} | f_n g | ~ \mathrm{d} m
      < (2K + \lVert g \rVert_{1,A}) \varepsilon.

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

.. _ex-5-24:

24. 试证 :math:`L^2(0, 1)` 中规范正交系的势不超过 :math:`\aleph_0`.

    提示: 设 :math:`\{ \omega_{\alpha} \}` 为 :math:`L^2(0, 1)` 中任一规范正交系, 则对
    :math:`\alpha \neq \alpha'` 有 :math:`\lVert \omega_{\alpha} - \omega_{\alpha'} \rVert_2 = \sqrt{2}`.
    取 :math:`L^2(0, 1)` 的一可数稠密子集 :math:`A = \{ \varphi_n \}` 并作球族
    :math:`\mathscr{B} = \{ \mathscr{B}(\varphi_n, 1/2) : n \in \mathbb{N} \}`, 则每个
    :math:`\omega_{\alpha}` 必含于某个球 :math:`\mathscr{B}(\varphi_n, 1/2)` 中且不同的
    :math:`\omega_{\alpha}, \omega_{\alpha'}` 不可能含于同一个球 :math:`\mathscr{B}(\varphi_n, 1/2)` 中,
    否则将有 :math:`\sqrt{2} = \lVert \omega_{\alpha} - \omega_{\alpha'} \rVert_2
    \leqslant \lVert \omega_{\alpha} - \varphi_n \rVert + \lVert \varphi_n - \omega_{\alpha'} \rVert
    \leqslant 1` (矛盾!). 于是 :math:`\{ \omega_{\alpha} \}` 与 :math:`\mathscr{B}` 的一子集成一一对应,
    因而至多可数.

.. proof:solution::

   待写.

.. _ex-5-25:

25. 试证: 若一可积函数的傅里叶级数在一正测度集 :math:`E` 上处处收敛, 则它的傅里叶系数趋于零.

.. proof:solution::

   待写.

.. _ex-5-26:

26. 设 :math:`f \in L(0, 2\pi)` 而 :math:`g` 有界且有周期 :math:`2\pi`, 证明

    .. math::
       \lim_{n \to \infty} \int_{-\pi}^{\pi} f(x) g(nx) ~ \mathrm{d} m
       = \dfrac{1}{2\pi} \int_{-\pi}^{\pi} f(x) ~ \mathrm{d} m \int_{-\pi}^{\pi} g(x) ~ \mathrm{d} m.

.. proof:solution::

   待写.

.. _ex-5-27:

27. 设 :math:`E` 为可测集, :math:`m E < \infty`, :math:`f \in L^{\infty}(E)` 且 :math:`\lVert f \rVert_{\infty} > 0`.
    令 :math:`\displaystyle C_n = \int_E |f|^n ~ \mathrm{d} m`,
    证明 :math:`\displaystyle \lVert f \rVert_{\infty} = \lim_{n \to \infty} C_{n + 1} / C_n`.

.. proof:proof::

   .. note::
      首先要注意的是, 我们事先是不知道数列 :math:`\{ C_{n + 1} / C_n \}` 是否收敛的 (或者说是否有极限的).
      如果事先知道了这个数列是收敛的, 那么这个题目的结论就是平凡的, 直接能从

      .. math::
         \lim_{n \to \infty} C_n^{1/n} = \lVert f \rVert_{\infty}

      得到.

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

.. _ex-5-28:

28. 试将 :math:`\S 3` 例 2 的结果推广到 :math:`\mathbb{R}^n` 情形.

    提示: 此时 :math:`f(x) = e^{-|x|^2/2}`, :math:`|x|^2 = x_1^2 + x_2^2 + \cdots + x_n^2`, 而
    :math:`\mathrm{d} x = \mathrm{d} x_1 \mathrm{d} x_2 \cdots \mathrm{d} x_n`,
    :math:`e^{-i t \cdot x} = e^{-i t_1 x_1} e^{-i t_2 x_2} \cdots e^{-i t_n x_n}`,
    :math:`x = (x_1, x_2, \cdots, x_n)`, :math:`t = (t_1, t_2, \cdots, t_n)`. 可求出
    :math:`\hat{f}(t) = (2\pi)^{-n/2} e^{-|t|^2/2}`.

.. proof:solution::

   待写.

.. _ex-5-29:

29. 设 :math:`1 < p < \infty`, :math:`f \in L^p(0, \infty)`, 并令
    :math:`\displaystyle F(x) = x^{-1} \int_0^x f(t) ~ \mathrm{d} m`, :math:`0 < x < \infty`. 试证,
    映射 :math:`f \to F` 是 :math:`L^p(0, \infty)` 到 :math:`L^p(0, \infty)` 的有界映射, 且满足
    :math:`\lVert F \rVert_p \leqslant p (p - 1)^{-1} \lVert f \rVert_p`. 又等式成立的充分必要条件是什么?

    提示: 先对连续并具紧支集的函数 :math:`f` 考虑并且限定 :math:`f \geqslant 0`, 然后对 :math:`F(x)`
    的 :math:`p` 次幂用分部积分公式, 再应用 Hölder 不等式.

.. proof:solution::

   待写.

.. _ex-5-30:

30. 设 :math:`m E = 1`, 试证

    .. math::
       \lim_{p \to 0} \lVert f \rVert_p = \exp \left\{ \int_E \ln |f(x)| ~ \mathrm{d} m \right\}.

    提示: 可对 :math:`f \geqslant 0` 考察, 注意 :math:`p^{-1} (f^p - 1)` 单调递减趋于
    :math:`\ln f` (当 :math:`p \to 0`), 再设法应用控制收敛定理.

.. proof:solution::

   待写.

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

   对于 :math:`\displaystyle g_n = \sum_{k = 1}^{N_n} a_{nk} \chi_{E_{nk}}`,
   :math:`\displaystyle X = \bigcup_{k = 1}^{N_n} E_{nk}`, 且 :math:`E_{nk}` 两两不交, 有

   .. math::
      \varphi \left( \dfrac{1}{\mu X} \int_X g_n ~ \mathrm{d} \mu \right)
      & = \varphi \left( \sum_{k = 1}^{N_n} \dfrac{\mu E_{nk}}{\mu X} a_{nk} \right) \\
      & \leqslant \sum_{k = 1}^{N_n} \dfrac{\mu E_{nk}}{\mu X} \varphi \left( a_{nk} \right)
        = \dfrac{1}{\mu X} \int_X \varphi(g_n) ~ \mathrm{d} \mu.

   由 :math:`\varphi` 的连续性, 两边取极限即有

   .. math::
      \varphi \left( \dfrac{1}{\mu X} \int_X f ~ \mathrm{d} \mu \right)
      \leqslant \dfrac{1}{\mu X} \int_X \varphi(f) ~ \mathrm{d} \mu.

.. _ex-5-32:

32. 设 :math:`E` 是一维勒贝格可测集, 对于任意的 :math:`x \in \mathbb{R}`, 令

    .. math::
       \Delta_h (x) = (2h)^{-1} m \left( E \cap (x - h, x + h) \right), \quad h > 0.

    试证: 几乎对一切 :math:`x \in E` 有 :math:`\displaystyle \lim_{h \to 0} \Delta_h (x) = 1`,
    而几乎对一切 :math:`x \not\in E` 有 :math:`\displaystyle \lim_{h \to 0} \Delta_h (x) = 0`;
    试作一集 :math:`E` 使极限 :math:`\displaystyle \lim_{h \to 0} \Delta_h (0)` 不存在.
    又问当 :math:`E` 是不可测集时结论如何?

.. proof:solution::

   待写.

.. _ex-5-33:

33. 设 :math:`f` 是 :math:`\mathbb{R}` 上可测函数, 令 :math:`\mu (\alpha) = m \mathbb{R} (|f| > \alpha)`.
    试证:

    .. math::
       \int_{\mathbb{R}} |f(x)|^p ~ \mathrm{d} x = - \int_0^{\infty} \alpha^p ~ \mathrm{d} \mu (\alpha),
       \quad p \geqslant 1;

    .. math::
       \lVert f \rVert_{\infty} = \inf \{ \alpha : \mu (\alpha) = 0 \}.

    提示: 对 :math:`f \in L^p` 情形, 先对简单函数证明结果, 然后应用极限过程.

.. proof:solution::

   待写.

.. _ex-5-34:

34. 令 :math:`\displaystyle M f(x) = \sup_{r > 0} \dfrac{1}{2r} \int_{x - r}^{x + r} |f(t)| ~ \mathrm{d} t`.
    试证存在常数 :math:`C`, 使 :math:`m (M f > \alpha) \leqslant C \alpha^{-1} \lVert f \rVert_1`,
    对任一 :math:`\alpha > 0` 成立.

    提示: 利用习题 33.

.. proof:solution::

   待写.

.. _ex-5-35:

35. 设 :math:`f \in L(0, 1)`, :math:`\alpha \in (0, 1)`. 试证对每个 :math:`e`, :math:`m e = \alpha`,
    :math:`\int_e f ~ \mathrm{d} m = 0` 蕴含 :math:`f \sim 0`.

.. proof:solution::

   待写.

.. _ex-5-36:

36. 设 :math:`f \in L(0, 1)` 满足 :math:`\displaystyle \int_{(0, 1)} t^k f(t) ~ \mathrm{d} t = 0`
    对每个 :math:`k \in \mathbb{N} \cup \{ 0 \}`, 证明 :math:`f \sim 0`.

    提示: 取 :math:`[0, 1]` 上一致有界的多项式列 :math:`p_n`, 使 :math:`p_n(t) \to \mathrm{sign} f(t)`,
    a.e. (:math:`n \to \infty`).

.. proof:solution::

   待写.

.. _ex-5-37:

37. 设 :math:`\alpha \in (0, 1)`. 试作一集 :math:`E \subset [0, 1]`, :math:`m E = \alpha` 使对每个
    :math:`c \in [0, 1] \setminus E` 有

    .. math::
       \int_E |x - c|^{-1} ~ \mathrm{d} x = \infty.

.. proof:solution::

   待写.

.. _ex-5-38:

38. 设 :math:`E \subset \mathbb{R}` 且 :math:`m E < \infty`. 试求极限
    :math:`\displaystyle \lim_{k \to \infty} \int_E (2 - \sin kx)^{-1} ~ \mathrm{d} x` 的值.

.. proof:solution::

   首先来求被积函数 :math:`f_k(x) = (2 - \sin kx)^{-1}` 的不定积分. 令 :math:`t = \tan \dfrac{kx}{2}`, 则有

   .. math::
      \sin kx = \dfrac{2t}{1 + t^2}, \quad \mathrm{d} x = \dfrac{2}{k} \dfrac{\mathrm{d} t}{1 + t^2},

   从而有

   .. math::
      \int \dfrac{1}{2 - \sin kx} ~ \mathrm{d} x
      & = \int \dfrac{1}{2 - \dfrac{2t}{1 + t^2}} \dfrac{2}{k} \dfrac{\mathrm{d} t}{1 + t^2} \\
      & = \dfrac{1}{k} \int \dfrac{1}{(1 + t^2) - t} ~ \mathrm{d} t \\
      & = \dfrac{1}{k} \int \dfrac{1}{(t - 1/2)^2 + 3/4} ~ \mathrm{d} (t - 1/2) \\
      & = \dfrac{2}{\sqrt{3} k} \arctan \dfrac{2t - 1}{\sqrt{3}} + C \\
      & = \dfrac{2}{\sqrt{3} k} \arctan \dfrac{2 \tan \dfrac{kx}{2} - 1}{\sqrt{3}} + C.

   注意, 由于 :math:`\tan \dfrac{kx}{2}` 的周期性, 实际上在不同的周期内, 常数 :math:`C` 的值是不同的. 在 :math:`f_k(x)`
   的每个最小正周期 :math:`T_k = \dfrac{2\pi}{k}` 内,
   其积分值 :math:`I_{k, 0} = \displaystyle \int_{-\pi/k}^{\pi/k} f_k(x) ~ \mathrm{d} x = \dfrac{2\pi}{\sqrt{3} k}`.

   由于 :math:`1/3 \leqslant |f_k| \leqslant 1`, 且 :math:`m E < \infty`, 那么对任意 :math:`\varepsilon > 0`,
   可选取开集 :math:`G \supset E` 使得 :math:`m G < m E + \varepsilon/4`, 从而有

   .. math::
      :label: ex-5-38-eq-1

      \left\lvert \int_G f_k(x) ~ \mathrm{d} x - \int_E f_k(x) ~ \mathrm{d} x \right\rvert
      \leqslant \int_{G \setminus E} |f_k(x)| ~ \mathrm{d} x
      \leqslant m (G \setminus E) \leqslant \varepsilon/4.

   设开集 :math:`G` 的结构表示为 :math:`\displaystyle G = \bigcup_{s = 1}^{\infty} (a_s, b_s)`.

   对于一个一般的固定的区间 :math:`(a, b)`, 记 :math:`N_{a, b} = \left[\dfrac{(b-a)k}{2\pi} \right]`, 其中 :math:`[ x ]`
   表示 :math:`x` 的整数部分. 注意到 :math:`|f_k| \leqslant 1`, 有

   .. math::
      \int_{(a, b)} f_k(x) ~ \mathrm{d} x
      & = \int_{(a, a + N_{a, b}T_k)} f_k(x) ~ \mathrm{d} x + \int_{(a + N_{a, b}T_k, b)} f_k(x) ~ \mathrm{d} x \\
      & = N_{a, b} \cdot I_{k, 0} + \int_{(a + N_{a, b}T_k, b)} f_k(x) ~ \mathrm{d} x,

   从而有

   .. math::
      & \left\lvert \int_{(a, b)} f_k(x) ~ \mathrm{d} x
        - \left[\dfrac{(b-a)k}{2\pi} \right] \cdot \dfrac{2\pi}{\sqrt{3} k} \right\rvert \\
      \leqslant & \int_{(a + N_{a, b}T_k, b)} 1 ~ \mathrm{d} x = b - a - N_{a, b}T_k
      = \left\{ \dfrac{(b-a)k}{2\pi} \right\} \cdot \dfrac{2\pi}{k},

   其中 :math:`\{ x \}` 表示 :math:`x` 的小数部分. 于是进一步有

   .. math::
      :label: ex-5-38-eq-2

      & \left\lvert \int_{(a, b)} f_k(x) ~ \mathrm{d} x - \dfrac{(b-a)}{\sqrt{3}} \right\rvert \\
      \leqslant & \left\lvert \int_{(a, b)} f_k(x) ~ \mathrm{d} x - \left[\dfrac{(b-a)k}{2\pi} \right]
        \cdot \dfrac{2\pi}{\sqrt{3} k} \right\rvert
        + \left\lvert \left[\dfrac{(b-a)k}{2\pi} \right] \cdot \dfrac{2\pi}{\sqrt{3} k}
        - \dfrac{(b-a)}{\sqrt{3}} \right\rvert \\
      \leqslant & \left\{ \dfrac{(b-a)k}{2\pi} \right\} \cdot \dfrac{2\pi}{k}
        + \left\{ \dfrac{(b-a)k}{2\pi} \right\} \cdot \dfrac{2\pi}{\sqrt{3} k} \\
      \leqslant & \dfrac{4\pi}{k}.

   对于取好的 :math:`\varepsilon`, 可取足够大的 :math:`N` 使得
   :math:`\displaystyle \sum_{s = N + 1}^{\infty} (b_s - a_s) < \varepsilon/4`.
   记 :math:`\displaystyle G_{\varepsilon} = \bigcup_{s = 1}^{N} (a_s, b_s)`, 则有

   .. math::
      :label: ex-5-38-eq-3

      \left\lvert \int_G f_k(x) ~ \mathrm{d} x - \int_{G_{\varepsilon}} f_k(x) ~ \mathrm{d} x \right\rvert
      \leqslant \varepsilon/4.

   另一方面, 取足够大的 :math:`k` 使得 :math:`4N\pi/k < \varepsilon/4`, 由 :eq:`ex-5-38-eq-2` 知

   .. math::
      :label: ex-5-38-eq-4

      \left\lvert \int_{G_{\varepsilon}} f_k(x) ~ \mathrm{d} x - \dfrac{1}{\sqrt{3}} \sum_{s = 1}^{N} (b_s-a_s) \right\rvert
      & \leqslant \sum_{s = 1}^{N} \left\lvert \int_{(a_s, b_s)} f_k(x) ~ \mathrm{d} x
        - \dfrac{(b_s-a_s)}{\sqrt{3}} \right\rvert \\
      & \leqslant \sum_{s = 1}^{N} \dfrac{4\pi}{k} < \varepsilon/4.

   综合 :eq:`ex-5-38-eq-1`, :eq:`ex-5-38-eq-3`, :eq:`ex-5-38-eq-4` 三式, 可知对充分大的 :math:`k` 有

   .. math::
      & \left\lvert \int_E f_k(x) ~ \mathrm{d} x - m E / \sqrt{3} \right\rvert \\
      \leqslant & \left\lvert \int_E f_k(x) ~ \mathrm{d} x - \int_{G} f_k(x) ~ \mathrm{d} x \right\rvert
        + \left\lvert \int_G f_k(x) ~ \mathrm{d} x - \int_{G_{\varepsilon}} f_k(x) ~ \mathrm{d} x \right\rvert \\
      & + \left\lvert \int_{G_{\varepsilon}} f_k(x) ~ \mathrm{d} x
        - \dfrac{1}{\sqrt{3}} \sum_{s = 1}^{N} (b_s-a_s) \right\rvert
        + \left\lvert \dfrac{1}{\sqrt{3}} \sum_{s = 1}^{N} (b_s-a_s) - m E / \sqrt{3} \right\rvert \\
      < & \dfrac{\varepsilon}{4} + \dfrac{\varepsilon}{4} + \dfrac{\varepsilon}{4} + \dfrac{\varepsilon}{4\sqrt{3}} \\
      < & \varepsilon,

   于是有

   .. math::
      \lim_{k \to \infty} \int_E (2 - \sin kx)^{-1} ~ \mathrm{d} x
      = \lim_{k \to \infty} \int_E f_k(x) ~ \mathrm{d} x = m E / \sqrt{3}.
