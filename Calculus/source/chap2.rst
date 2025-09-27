第二章  极限与连续
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. contents:: :local:


课后习题解答
================================

§2.1 数列的极限
--------------------------------

1. 依据 :math:`\varepsilon - N` 定义证明:

   (6). :math:`\lim\limits_{n \to \infty} \sqrt[n]{n} = 1`.

.. proof:proof::

   需要证明对任意 :math:`\varepsilon > 0`, 存在正整数 :math:`N`, 使得当 :math:`n > N` 时,
   有 :math:`\lvert \sqrt[n]{n} - 1 \rvert < \varepsilon`, 即 :math:`n < (1 + \varepsilon)^n`.
   利用二项式展开右端, 有

   .. math::
      :label: binomial-expansion

      (1 + \varepsilon)^n =
      1 + n \varepsilon + \dfrac{n(n-1)}{2} \varepsilon^2 + \cdots + \varepsilon^n
      > \dfrac{n(n-1)}{2} \varepsilon^2.

   因此只需找到 :math:`N` 使得 :math:`n < \dfrac{n(n-1)}{2} \varepsilon^2` 对所有 :math:`n > N` 都成立.
   于是, 只需要取 :math:`N = \max \left\{ 2, \left[ \dfrac{2}{\varepsilon^2} + 1 \right] \right\}` 即可.
   这里 :math:`[ x ]` 表示 :math:`x` 的整数部分. 这里让 :math:`N` 至少为 2,
   是为了保证二项式展开式 :eq:`binomial-expansion` 中的 :math:`\dfrac{n(n-1)}{2} \varepsilon^2` 项存在.

4. 设 :math:`x_n = \begin{cases} \dfrac{n-1}{n}, & n ~ \text{为偶数}, \\ \dfrac{\sqrt{n^2+1}}{n}, & n ~ \text{为奇数}, \end{cases}`
   证明 :math:`\lim\limits_{n \to \infty} x_n = 1`.

.. proof:proof::

   需要证明对任意 :math:`\varepsilon > 0`, 存在正整数 :math:`N`, 使得当 :math:`n > N` 时,
   有 :math:`|x_n - 1| < \varepsilon`. 可以算得

   .. math::

      |x_n - 1| = \begin{cases}
         \dfrac{1}{n}, & n ~ \text{为偶数}, \\
         \dfrac{\sqrt{n^2 + 1} - n}{n} = \dfrac{1}{n(\sqrt{n^2 + 1} + n)} < \dfrac{1}{n}, & n ~ \text{为奇数}.
      \end{cases}

   因此只需取 :math:`N = \left[ \dfrac{1}{\varepsilon} \right] + 1` 即可.

7. 设 :math:`\lim\limits_{n \to \infty} x_n = 0`, :math:`y_n` 是一个有界数列, 即存在常数 :math:`M > 0`,
   使得 :math:`|y_n| < M (n = 1, 2, \dots)`. 证明 :math:`\lim\limits_{n \to \infty} x_n y_n = 0`.

.. proof:proof::

   由于 :math:`\lim\limits_{n \to \infty} x_n = 0`, 那么对任意 :math:`\varepsilon > 0`, 存在正整数 :math:`N`,
   使得当 :math:`n > N` 时, 有 :math:`|x_n - 0| < \dfrac{\varepsilon}{M}`, 即 :math:`|x_n| < \dfrac{\varepsilon}{M}`.
   又因为数列 :math:`y_n` 有界, 存在常数 :math:`M > 0`, 使得对所有 :math:`n` 都有 :math:`|y_n| < M`.
   因此当 :math:`n > N` 时, 有

   .. math::

      |x_n y_n - 0| = |x_n y_n| = |x_n| |y_n| < \dfrac{\varepsilon}{M} \cdot M = \varepsilon.

   这就证明了 :math:`\lim\limits_{n \to \infty} x_n y_n = 0`.

§2.2 函数的极限
--------------------------------

6. 证明: 若 :math:`\lim\limits_{x\to\infty} f(x) = a > 0`, 则存在 :math:`X > 0`,
   使得当 :math:`|x| > X` 时, :math:`f(x) > 0`.

.. proof:proof::

   由于 :math:`\lim\limits_{x \to \infty} f(x) = a > 0`, 那么对于 :math:`\varepsilon = \dfrac{a}{2} > 0`,
   存在 :math:`X > 0`, 使得当 :math:`|x| > X` 时, :math:`|f(x) - a| < \varepsilon = \dfrac{a}{2}`.
   也就是说有

   .. math::

      0 < \dfrac{a}{2} < f(x) < \dfrac{3a}{2}.

§2.3 极限运算法则
--------------------------------

5. 设 :math:`f(x)` 是一个函数, 若直线 :math:`y = kx + b` 满足

   .. math::

      \lim_{x \to +\infty} \left [ f (x) - kx - b \right] = 0 \quad
      (\text {或者} ~ \lim_{x \to -\infty} \left [ f (x) - kx - b \right] = 0),

   则称直线 :math:`y = kx + b` 是函数 :math:`f(x)` 在正无穷 (或者负无穷) 处的渐近线,
   当 :math:`k = 0` 时, 称为水平渐近线; 当 :math:`k \neq 0` 时, 称为斜渐近线. 若

   .. math::

      \lim_{x \to x_0^+} f (x) = \infty \quad \text {或者} \quad \lim_{x \to x_0^-} f (x) = \infty,

   记函数 :math:`f(x)` 在 :math:`x_0` 某一侧趋于无穷, 则称直线 :math:`x = x_0` 是函数 :math:`f(x)` 的垂直渐近线.

   (1). 证明：若直线 :math:`y = kx + b` 是 :math:`f(x)` 在正无穷处的渐近线, 则

   .. math::

      k = \lim_{x \to +\infty} \dfrac{f(x)}{x}, \quad b = \lim_{x \to +\infty} \left[ f(x) - kx \right];

   (2). 求函数 :math:`f(x) = \dfrac{x^3}{(x - 1)^2}` 的所有渐近线.

.. proof:solution::

   (1). 由题意, 有

   .. math::

      \lim_{x \to +\infty} \left [ f (x) - kx - b \right] = 0,

   利用极限四则运算 (这里是加法) 法则有

   .. math::

      b = \lim_{x \to +\infty} \left[ (f(x) - kx - b) + b \right] = 0 + b = b.

   利用上式, 也可以知道 :math:`\lim\limits_{x \to +\infty} \left[ f(x) - kx \right] = b`, 于是

   .. math::

      0 = \lim_{x \to +\infty} \dfrac{b}{x} = \lim_{x \to +\infty} \dfrac{f(x) - kx}{x}
        = \lim_{x \to +\infty} \dfrac{f(x)}{x} - k,

   从而有 :math:`k = \lim\limits_{x \to +\infty} \dfrac{f(x)}{x}`.

   (2). 首先, 函数 :math:`f(x) = \dfrac{x^3}{(x - 1)^2}` 在 :math:`x = 1` 无定义, 且

   .. math::

      \lim_{x \to 1} f(x) = \lim_{x \to 1} \dfrac{x^3}{(x - 1)^2} = \infty,

   因此 :math:`x = 1` 是 :math:`f(x)` 的垂直渐近线.

   接下来计算斜渐近线以及水平渐近线: 有

   .. math::

      \dfrac{f(x)}{x} = \dfrac{x^3}{x(x - 1)^2} \to 1 \quad ( x \to \infty ),

   于是, 斜率 :math:`k = 1`. 又有

   .. math::

      f(x) - x = \dfrac{x^3}{(x - 1)^2} - x = \dfrac{x^3 - x(x - 1)^2}{(x - 1)^2}
      = \dfrac{2x^2 - x}{(x - 1)^2} \to 2 \quad ( x \to \infty ).

   于是, 截距 :math:`b = 2`. 这样就算得 :math:`f(x)` 还有斜渐近线 :math:`y = x + 2`.

§2.4 极限存在准则与重要极限
--------------------------------

§2.5 无穷大量与无穷小量
--------------------------------

§2.6 函数的连续性和间断点
--------------------------------

§2.7 闭区间上连续函数的性质
--------------------------------

补充内容
================================

§2.2 函数的极限
--------------------------------

1. 设 :math:`a_n > 0 (n = 1, 2, \ldots)` 且存在常数 :math:`c > 0` 使得 :math:`\forall n > m > 1` 有 :math:`a_n \leqslant c \cdot a_m`.
   已知 :math:`\{a_n\}` 存在子列 :math:`\{a_{n_k}\}` 极限等于0, 求证 :math:`\lim\limits_{n \to \infty} a_n = 0`.

.. proof:proof::

   由于 :math:`\lim_{k \to \infty} a_{n_k} = 0`, 那么 :math:`\forall \varepsilon > 0, \exists K(\varepsilon) \in \mathbb{N}^+`,
   使得 :math:`\forall k > K(\varepsilon)` 有 :math:`|a_{n_k} - 0| < \varepsilon / c`, 由于 :math:`a_n > 0` 对所有 :math:`n` 成立, 我们可以得到

   .. math::

      0 < a_{n_k} < \varepsilon / c

   由于 :math:`\forall n > m > 1` 有 :math:`a_n \leqslant c \cdot a_m`, 那么 :math:`\forall n > n_{K(\varepsilon)+1}` 有

   .. math::

      0 < a_n < c \cdot a_{n_{K(\varepsilon)+1}} < c \cdot \varepsilon / c = \varepsilon

   由于 :math:`\varepsilon` 是任意的, 所以 :math:`\lim\limits_{n \to \infty} a_n = 0`.

§2.4 极限存在准则与重要极限
--------------------------------------------

求 :math:`\lim\limits_{x \to 0} x \left[ \dfrac{1}{x} \right]`

.. proof:solution::

   取整函数的定义为

   .. math::

      [x] = \max \{ n \in \mathbb{Z} | n \leqslant x \} = n \text{ 若 } n \leqslant x < n + 1, n \in \mathbb{Z}

   那么对于 :math:`\left[ \dfrac{1}{x} \right]` 来说, 有 :math:`\left[ \dfrac{1}{x} \right] \leqslant \dfrac{1}{x} < \left[ \dfrac{1}{x} \right] + 1`
   (将上式的 :math:`x, n` 分别替换为 :math:`\dfrac{1}{x}, \left[ \dfrac{1}{x} \right]` 即可), 那么

   .. math::

      \dfrac{1}{x} - 1 < \left[ \dfrac{1}{x} \right] \leqslant \dfrac{1}{x},

   从而有

   .. math::

      \begin{cases}
         1 - x < x \left[ \dfrac{1}{x} \right] \leqslant 1, & \text{若} x > 0, \\
         1 \leqslant x \left[ \dfrac{1}{x} \right] < 1 - x, & \text{若} x < 0.
      \end{cases}

   总之, 有 :math:`1 - \lvert x \rvert < x \left[ \dfrac{1}{x} \right] < 1 + \lvert x \rvert`,
   从而由夹逼准则知 :math:`\lim\limits_{x \to 0} x \left[ \dfrac{1}{x} \right] = 1`.

§2.6 函数的连续性和间断点
--------------------------------------------

Riemann 函数定义为

.. math::

   R(x) = \begin{cases}
      0, & x \text{ 为无理数} \\
      \dfrac{1}{q}, & x = \dfrac{p}{q} \text{ 为有理数, 且 } p, q \text{ 互素, } q > 0
   \end{cases}

求证 Riemann 函数在所有无理数点处连续, 且在所有有理数点处间断.

.. proof:proof::

   首先来证明 Riemann 函数在所有无理数点处连续. 任取无理数 :math:`x_0 \in \mathbb{R} \setminus \mathbb{Q}`, 同时任取 :math:`1 > \varepsilon > 0`.
   对于 :math:`\varepsilon`, 取正整数 :math:`0 < q_0 \in \mathbb{N}^+`, 使得 :math:`\dfrac{1}{q_0} < \varepsilon`. 我们知道以下集合

   .. math::
      :label: riemann-nbhd

      \begin{aligned}
      A(x_0, q_0) & := \left\{ a \in \mathbb{Q} \ :\ a = \dfrac{p}{q}, p, q \text{ 互素, } 0 < q \leqslant q_0, ([x_0] - 1) q \leqslant p \leqslant ([x_0] + 2) q \right\} \\
      & \subset [[x_0] - 1, [x_0] + 2]
      \end{aligned}

   是有限集, 元素个数至多为 :math:`3 + \cdots + 3q_0 = 2 q_0 (q_0 + 1) / 3`, 其中 :math:`[ \cdot ]` 表示取整. 那么我们可以找到一个 :math:`\delta > 0`,
   使得存在无理数 :math:`x_0` 的邻域 :math:`U(x_0, \delta)` (可以不妨设这个邻域包含于区间 :math:`[[x_0] - 1, [x_0] + 2]`),
   使得 :math:`U(x_0, \delta) \cap A(x_0, q_0) = \emptyset`. 那么对于 :math:`\forall x \in U(x_0, \delta)`,有

   .. math::
      :label: riemann-neq

      \lvert R(x) - 0 \rvert = R(x) < \dfrac{1}{q_0} < \varepsilon,

   这是因为在这个领域内使得 :math:`R(x) \geqslant \dfrac{1}{q_0}` 的(有理)数 :math:`x` 都必须属于集合 :math:`A`. 那么 :math:`\lim\limits_{x \to x_0} R(x) = 0 = R(x_0)`.
   由于 :math:`x_0` 是任意的, 所以 Riemann 函数 :math:`R(x)` 在所有无理数点处连续.

   然后来证明 Riemann 函数在所有有理数点处间断. 任取有理数 :math:`x_0 = \dfrac{p_0}{q_0} \in \mathbb{Q}`, 取 :math:`\varepsilon = \dfrac{1}{2 q_0}`, 那么
   对于任意的 :math:`\delta > 0`, 总存在无理数 :math:`x_1 \in U(x_0, \delta)`, 这时有 :math:`R(x_1) = 0`, 从而有

   .. math::

      \lvert R(x_1) - R(x_0) \rvert = \dfrac{1}{q_0} > \varepsilon

   这说明了 Riemann 函数 :math:`R(x)` 当自变量 :math:`x` 趋于有理点 :math:`x_0` 时, 函数值 :math:`R(x)` 不可能以这点的函数值 :math:`R(x_0)` 为极限,
   从而知 Riemann 函数在所有有理数点处间断. 进一步考察去心邻域 :math:`\mathring{U}(x_0, \delta) = U(x_0, \delta) \setminus \{ x_0 \}`,
   他与集合 :math:`A(x_0, q_0)` (对有理数也可以依 :eq:`riemann-nbhd` 类似定义) 的交集也是空集, 不等式 :eq:`riemann-neq` 仍然成立, 因此 Riemann 函数在所有有理数点的极限仍然是0,
   由此可知 Riemann 函数在所有有理数点处的间断点类型都是第一类的可去间断点.

   需要进一步注意的是, Riemann 函数在任何一个无理数的任何一个开邻域, 也就是包含这个无理数的开区间都不连续, 因为这个开区间里面一定有有理数, 黎曼函数在这些点处是不连续的.
   因此 Riemann 函数是满足如下性质的特殊函数

      函数在一点连续, 但在这点任何一个开邻域内都不连续.
