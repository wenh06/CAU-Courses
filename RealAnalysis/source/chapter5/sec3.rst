§3 傅里叶变换概要
------------------------------------------

.. _ex-5-39:

39. 设 :math:`f, f_n \in L^1(\mathbb{R}), n \in \mathbb{N},` 且 :math:`f_n \xrightarrow{\text{强}} f` (在 :math:`L^1(\mathbb{R})` 中),
    证明在 :math:`\mathbb{R}` 上一致地有 :math:`\displaystyle \lim_{n \to \infty} \hat{f}_n(t) = \hat{f}(t).`
    问在 :math:`L^2(\mathbb{R})` 中相应的命题是否成立?

.. proof:proof::

   对任意 :math:`t \in \mathbb{R}`, 有

   .. math::

      \left\lvert \hat{f}_n(t) - \hat{f}(t) \right\rvert
      & = \dfrac{1}{2\pi} \left\lvert \int_{\mathbb{R}} f_n(x) e^{-itx} ~ \mathrm{d} x - \int_{\mathbb{R}} f(x) e^{-itx} ~ \mathrm{d} x \right\rvert \\
      & \leqslant \dfrac{1}{2\pi} \int_{\mathbb{R}} \left\lvert f_n(x) - f(x) \right\rvert ~ \mathrm{d} x \\
      & = \dfrac{1}{2\pi} \lVert f_n - f \rVert_1 \xrightarrow{n \to \infty} 0.

   这表明了 :math:`\displaystyle \lim_{n \to \infty} \hat{f}_n(t) = \hat{f}(t)` 在 :math:`\mathbb{R}` 上一致成立.

   在 :math:`L^2(\mathbb{R})` 中, 相应的命题不成立. 反例如下:

   取 :math:`\displaystyle \varphi(x) = \dfrac{1}{2}\chi_{[-1, 1]}(x) \in L^1(\mathbb{R}) \cap L^2(\mathbb{R})`,
   并令 :math:`f_n(x) = \varphi^{*n}(x)`, 其中 :math:`\varphi^{*n}` 表示 :math:`\varphi` 自身的卷积 :math:`n` 次.
   容易验证 :math:`f_n` 是具有紧支集的非负函数, 且 :math:`\lVert f_n \rVert_1 = 1`. 故对所有 :math:`n \in \mathbb{N}`,
   有 :math:`f_n \in L^1(\mathbb{R}) \cap L^2(\mathbb{R})`. 那么有

   .. math::

      \begin{gathered}
      \hat{f}(t) = \hat{\varphi}(t) = \dfrac{\sin t}{2\pi t}, \\
      \hat{f}_n(t) = (2\pi)^{n-1} \hat{\varphi}^n(t) = \dfrac{\sin^n t}{2\pi t^n}.
      \end{gathered}

   那么由帕塞瓦尔 (Parseval) 公式知

   .. math::

      \lim_{n \to \infty} \lVert f_n \rVert_2^2
      & = \lim_{n \to \infty} 2 \pi \int_{\mathbb{R}} \lvert \hat{f}_n(t) \rvert^2 ~ \mathrm{d} t
      = \lim_{n \to \infty} \dfrac{1}{2\pi} \int_{\mathbb{R}} \dfrac{\sin^{2n} t}{t^{2n}} ~ \mathrm{d} t \\
      & = \dfrac{1}{2\pi} \int_{\mathbb{R}} \lim_{n \to \infty} \dfrac{\sin^{2n} t}{t^{2n}} ~ \mathrm{d} t \\
      & = 0,

   即在 :math:`L^2(\mathbb{R})` 中 :math:`f_n \xrightarrow{\text{强}} 0`, 但是 :math:`t = 0` 处, :math:`\hat{f}_n(t)` 不收敛到 :math:`0`.

.. _ex-5-40:

40. 设 :math:`C_0` 表示 :math:`\mathbb{R}` 上有界连续函数 :math:`g` 且满足 :math:`\displaystyle \lim_{t \to \pm\infty} g(t) = 0` 的函数类.
    问每个 :math:`g \in C_0` 是否均为某一可积函数的傅里叶变换的像?

.. proof:proof::

   不是每个 :math:`g \in C_0` 都是某一可积函数的傅里叶变换的像.

   反例: 考虑如下定义的奇函数 :math:`g`:

   .. math::

      g(t) = \begin{cases}
      1 / \ln t, & t > e, \\
      t / e, & 0 \leqslant t \leqslant e, \\
      -g(-t), & t < 0.
      \end{cases}

   容易验证函数 :math:`g` 连续, :math:`\lvert g \rvert \leqslant 1`, 且 :math:`\displaystyle \lim_{t \to \pm\infty} g(t) = 0`.
   但是对于函数 :math:`g` 有

   .. math::
      :label: ex-5-40-eq-1

      \int_e^c \dfrac{g(t)}{t} ~ \mathrm{d} t = \int_e^c \dfrac{1}{t \ln t} ~ \mathrm{d} t = \ln \ln c - \ln \ln e \xrightarrow{c \to \infty} \infty.

   下面证明, 对于任意实值可积函数 :math:`f`, 若

   .. math::
      :label: ex-5-40-eq-2

      \hat{f}(t) = \dfrac{1}{2\pi} \int_{\mathbb{R}} f(x) e^{-itx} ~ \mathrm{d} x
      = \dfrac{1}{2\pi} \int_{\mathbb{R}} f(x) \cos tx ~ \mathrm{d} x + i \dfrac{1}{2\pi} \int_{\mathbb{R}} f(x) \sin tx ~ \mathrm{d} x

   为奇函数, 则必存在常数 :math:`M`, 使得

   .. math::
      :label: ex-5-40-eq-3

      \left\lvert \int_a^c \dfrac{\hat{f}(t)}{t} ~ \mathrm{d} t \right\rvert \leqslant M

   对任意 :math:`0 < a < c \in \mathbb{R}` 成立. 这样 :eq:`ex-5-40-eq-1`, :eq:`ex-5-40-eq-2` 两式矛盾, 从而得证.

   事实上, 由 :eq:`ex-5-40-eq-2` 式已看出, 若 :math:`\hat{f}(t)` 为奇函数, 则有

   .. math::

      \hat{f}(t) = i \dfrac{1}{2\pi} \int_{\mathbb{R}} f(x) \sin tx ~ \mathrm{d} x.

   于是

   .. math::

      \left\lvert \int_a^c \dfrac{\hat{f}(t)}{t} ~ \mathrm{d} t \right\rvert
      = \dfrac{1}{2\pi} \left\lvert \int_a^c \int_{\mathbb{R}} f(x) \dfrac{\sin tx}{t} ~ \mathrm{d} x ~ \mathrm{d} t \right\rvert.

   由于 :math:`\displaystyle \left\lvert f(x) \dfrac{\sin tx}{t} \right\rvert \leqslant \dfrac{\lvert f(x) \rvert}{t}`,
   在 :math:`\mathbb{R} \times (a, c)` 上可积, 由 Fubini 定理, 有

   .. math::
      :label: ex-5-40-eq-4

      \left\lvert \int_a^c \dfrac{\hat{f}(t)}{t} ~ \mathrm{d} t \right\rvert
      & = \dfrac{1}{2\pi} \left\lvert \int_a^c \int_{\mathbb{R}} f(x) \dfrac{\sin tx}{t} ~ \mathrm{d} x ~ \mathrm{d} t \right\rvert \\
      & = \dfrac{1}{2\pi} \left\lvert \int_{\mathbb{R}} f(x) \int_a^c \dfrac{\sin tx}{t} ~ \mathrm{d} t ~ \mathrm{d} x \right\rvert.

   由于 :math:`\displaystyle \varphi(s) = \int_0^s \dfrac{\sin t}{t} ~ \mathrm{d} t` 为有界函数, 设它的一个上界为 :math:`M_0`. 又有

   .. math::

      \begin{gathered}
      \int_a^c \dfrac{\sin tx}{t} ~ \mathrm{d} t = \int_{ax}^{cx} \dfrac{\sin t}{t} ~ \mathrm{d} t = \varphi(cx) - \varphi(ax), \quad x > 0, \\
      \int_a^c \dfrac{\sin tx}{t} ~ \mathrm{d} t = -\int_{-ax}^{-cx} \dfrac{\sin t}{t} ~ \mathrm{d} t = \varphi(-ax) - \varphi(-cx), \quad x < 0,
      \end{gathered}

   故 :math:`\displaystyle \left\lvert \int_a^c \dfrac{\sin tx}{t} ~ \mathrm{d} t \right\rvert \leqslant 2M_0`. 代入 :eq:`ex-5-40-eq-4` 式有

   .. math::

      \left\lvert \int_a^c \dfrac{\hat{f}(t)}{t} ~ \mathrm{d} t \right\rvert \leqslant \dfrac{1}{2\pi} \int_{\mathbb{R}} \lvert f(x) \rvert 2M_0 ~ \mathrm{d} x = \dfrac{M_0}{\pi} \lVert f \rVert_1.

   于是取 :math:`\displaystyle M = \dfrac{M_0}{\pi} \lVert f \rVert_1` 即可.

.. _ex-5-41:

41. 设 :math:`f \in L^1(\mathbb{R})` 或 :math:`L^2(\mathbb{R})` 且 :math:`\hat{f} = 0`. 证明 :math:`f \sim 0`.

.. proof:proof::

   由于 :math:`\hat{f} = 0 \in L^1(\mathbb{R})`, 故当 :math:`f \in L^1(\mathbb{R})` 时, 由反演公式

   .. math::

      f(x) = \int_{\mathbb{R}} \hat{f}(t) e^{itx} ~ \mathrm{d} t = 0, \quad \text{a.e.} ~ x \in \mathbb{R},

   即有 :math:`f \sim 0`.

   当 :math:`f \in L^2(\mathbb{R})` 时, 由普朗席奈定理 (Plancherel 定理), 相应的反演公式为

   .. math::

      f(x) = \dfrac{\mathrm{d}}{\mathrm{d} x} \left( \int_{\mathbb{R}} \hat{f}(t) \dfrac{e^{itx} - 1}{it} ~ \mathrm{d} t \right) = 0,
      \quad \text{a.e.} ~ x \in \mathbb{R},

   也有 :math:`f \sim 0`.
