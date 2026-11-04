第二章  极限与连续
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. contents:: :local:


.. _ex-chap2:

课后习题解答
================================

.. _ex-chap2-sec1:

§2.1 数列的极限
--------------------------------

.. _ex-chap2-sec1-ex1:

1. 依据 :math:`\varepsilon - N` 定义证明:

   (1). :math:`\lim\limits_{n \to \infty} \dfrac{n}{2n+3} = \dfrac{1}{2}`;

   (2). :math:`\lim\limits_{n \to \infty} \dfrac{2n^2-1}{n^2+3} = 2`;

   (3). :math:`\lim\limits_{n \to \infty} \dfrac{\sqrt[3]{n^2} \sin n}{n+1} = 0`;

   (4). :math:`\lim\limits_{n \to \infty} (\ln(n+1) - \ln n) = 0`;

   (5). :math:`\lim\limits_{n \to \infty} \left[ \dfrac{1}{1 \times 2} + \dfrac{1}{2 \times 3} + \cdots + \dfrac{1}{(n-1) \times n} \right] = 1`;

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

2. 用数学语言给出 :math:`\lim\limits_{n \to \infty} x_n \neq l` 的定义, 并证明数列 :math:`\left\{ \dfrac{1}{n} \right\}` 不以 1 为极限.

.. proof:proof::

   :math:`\lim\limits_{n \to \infty} x_n \neq l` 的定义为: 存在正数 :math:`\varepsilon_0`, 使得对任意正整数 :math:`N`,
   总存在 :math:`n > N`, 满足 :math:`|x_n - l| \geqslant \varepsilon_0`.

   下面证明数列 :math:`\left\{ \dfrac{1}{n} \right\}` 不以 1 为极限. 取 :math:`\varepsilon_0 = \dfrac{1}{2}`, 对任意正整数 :math:`N`,
   取 :math:`n > N`, 则 :math:`n \geqslant 2`, 于是

   .. math::
      \left| \dfrac{1}{n} - 1 \right| = 1 - \dfrac{1}{n} \geqslant \dfrac{1}{2} = \varepsilon_0.

   这就证明了数列 :math:`\left\{ \dfrac{1}{n} \right\}` 不以 1 为极限.

3. 设数列 :math:`\{ x_n \}` 满足 :math:`\lim\limits_{n \to \infty} x_{2n} = \lim\limits_{n \to \infty} x_{2n+1} = l`, 证明 :math:`\lim\limits_{n \to \infty} x_n = l`.

.. proof:proof::

   任给 :math:`\varepsilon > 0`. 由 :math:`\lim\limits_{n \to \infty} x_{2n} = l`, 存在正整数 :math:`N_1`, 使得当 :math:`n > N_1` 时,
   有 :math:`|x_{2n} - l| < \varepsilon`; 由 :math:`\lim\limits_{n \to \infty} x_{2n+1} = l`, 存在正整数 :math:`N_2`, 使得当 :math:`n > N_2` 时,
   有 :math:`|x_{2n+1} - l| < \varepsilon`. 取 :math:`N = \max \{ 2N_1, 2N_2 + 1 \}`, 则当 :math:`n > N` 时:

   若 :math:`n` 为偶数, 记 :math:`n = 2k`, 则 :math:`k > N_1`, 有 :math:`|x_n - l| = |x_{2k} - l| < \varepsilon`;

   若 :math:`n` 为奇数, 记 :math:`n = 2k+1`, 则 :math:`k > N_2`, 有 :math:`|x_n - l| = |x_{2k+1} - l| < \varepsilon`.

   综上, 对任意 :math:`n > N` 都有 :math:`|x_n - l| < \varepsilon`, 即 :math:`\lim\limits_{n \to \infty} x_n = l`.

.. _ex-chap2-sec1-ex4:

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

5. 证明: 若 :math:`\lim\limits_{n \to \infty} x_n = l`, 则 :math:`\lim\limits_{n \to \infty} |x_n| = |l|`. 其逆命题是否成立?

.. proof:proof::

   由不等式 :math:`\bigl| |x_n| - |l| \bigr| \leqslant |x_n - l|` 可知, 任给 :math:`\varepsilon > 0`, 由 :math:`\lim\limits_{n \to \infty} x_n = l`,
   存在正整数 :math:`N`, 使得当 :math:`n > N` 时, 有 :math:`|x_n - l| < \varepsilon`, 从而

   .. math::
      \bigl| |x_n| - |l| \bigr| \leqslant |x_n - l| < \varepsilon,

   即 :math:`\lim\limits_{n \to \infty} |x_n| = |l|`.

   逆命题不成立. 例如数列 :math:`x_n = (-1)^n` 发散, 但 :math:`|x_n| = 1`, 显然 :math:`\lim\limits_{n \to \infty} |x_n| = 1`.

6. 设 :math:`x_n \geqslant 0 ~ (n = 1, 2, \cdots)`, 且 :math:`\lim\limits_{n \to \infty} x_n = l \geqslant 0`, 证明: :math:`\lim\limits_{n \to \infty} \sqrt{x_n} = \sqrt{l}`.

.. proof:proof::

   先设 :math:`l > 0`. 任给 :math:`\varepsilon > 0`, 由 :math:`\lim\limits_{n \to \infty} x_n = l`, 存在正整数 :math:`N`,
   使得当 :math:`n > N` 时, 有 :math:`|x_n - l| < \sqrt{l}\, \varepsilon`. 于是当 :math:`n > N` 时,

   .. math::
      \left| \sqrt{x_n} - \sqrt{l} \right|
      = \dfrac{|x_n - l|}{\sqrt{x_n} + \sqrt{l}} \leqslant \dfrac{|x_n - l|}{\sqrt{l}} < \varepsilon,

   即 :math:`\lim\limits_{n \to \infty} \sqrt{x_n} = \sqrt{l}`.

   再设 :math:`l = 0`. 任给 :math:`\varepsilon > 0`, 存在正整数 :math:`N`, 使得当 :math:`n > N` 时, 有
   :math:`x_n < \varepsilon^2`, 从而 :math:`\sqrt{x_n} < \varepsilon`, 即 :math:`\lim\limits_{n \to \infty} \sqrt{x_n} = 0 = \sqrt{l}`.

.. _ex-chap2-sec1-ex7:

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

.. _ex-chap2-sec2:

§2.2 函数的极限
--------------------------------

1. 用定义证明下列极限.

   (1). :math:`\lim\limits_{x \to x_0} x^2 = x_0^2`;

   (2). :math:`\lim\limits_{x \to x_0} \sin x = \sin x_0`;

   (3). :math:`\lim\limits_{x \to \infty} \dfrac{x^2-1}{2x^2+3} = \dfrac{1}{2}`;

   (4). :math:`\lim\limits_{x \to 1} \dfrac{x^4-1}{x-1} = 4`;

   (5). :math:`\lim\limits_{x \to \infty} \dfrac{1}{x+2} = 0`;

   (6). :math:`\lim\limits_{x \to -\infty} e^x = 0`.

.. proof:proof::

   (1). 任给 :math:`\varepsilon > 0`. 当 :math:`|x - x_0| < 1` 时, :math:`|x + x_0| \leqslant |x - x_0| + 2|x_0| < 1 + 2|x_0|`,
   于是

   .. math::
      |x^2 - x_0^2| = |x - x_0| \cdot |x + x_0| < (1 + 2|x_0|) |x - x_0|.

   故取 :math:`\delta = \min \left\{ 1, \dfrac{\varepsilon}{1 + 2|x_0|} \right\}`, 则当 :math:`0 < |x - x_0| < \delta` 时,
   有 :math:`|x^2 - x_0^2| < \varepsilon`, 即 :math:`\lim\limits_{x \to x_0} x^2 = x_0^2`.

   (2). 利用和差化积公式,

   .. math::
      |\sin x - \sin x_0| = \left| 2 \cos \dfrac{x + x_0}{2} \sin \dfrac{x - x_0}{2} \right|
      \leqslant 2 \left| \sin \dfrac{x - x_0}{2} \right| \leqslant |x - x_0|,

   故取 :math:`\delta = \varepsilon`, 则当 :math:`0 < |x - x_0| < \delta` 时, 有 :math:`|\sin x - \sin x_0| < \varepsilon`.

   (3). 当 :math:`x \neq 0` 时,

   .. math::
      \left| \dfrac{x^2-1}{2x^2+3} - \dfrac{1}{2} \right|
      = \dfrac{5}{2(2x^2+3)} < \dfrac{5}{4x^2}.

   故对任给 :math:`\varepsilon > 0`, 取 :math:`X = \sqrt{\dfrac{5}{4\varepsilon}}`, 则当 :math:`|x| > X` 时,
   有 :math:`\left| \dfrac{x^2-1}{2x^2+3} - \dfrac{1}{2} \right| < \varepsilon`.

   (4). :math:`\dfrac{x^4-1}{x-1} = (x+1)(x^2+1)`. 当 :math:`|x - 1| < 1` 即 :math:`0 < x < 2` 时,
   :math:`|(x+1)(x^2+1)| \leqslant 3 \cdot 5 = 15`. 故对任给 :math:`\varepsilon > 0`,
   取 :math:`\delta = \min \left\{ 1, \dfrac{\varepsilon}{15} \right\}`, 则当 :math:`0 < |x-1| < \delta` 时,

   .. math::
      \left| \dfrac{x^4-1}{x-1} - 4 \right| = |(x+1)(x^2+1) - 4| \leqslant |x+1| \cdot |x^2+1| < 15\delta \leqslant \varepsilon.

   (5). 对任给 :math:`\varepsilon > 0`, 由 :math:`\left| \dfrac{1}{x+2} - 0 \right| = \dfrac{1}{|x+2|} < \varepsilon`
   解得 :math:`|x + 2| > \dfrac{1}{\varepsilon}`. 取 :math:`X = \dfrac{1}{\varepsilon} + 2`, 则当 :math:`|x| > X` 时,
   有 :math:`|x+2| \geqslant |x| - 2 > X - 2 = \dfrac{1}{\varepsilon}`, 从而 :math:`\left| \dfrac{1}{x+2} \right| < \varepsilon`.

   (6). 对任给 :math:`0 < \varepsilon < 1`, 由 :math:`|e^x - 0| = e^x < \varepsilon` 解得 :math:`x < \ln \varepsilon`.
   取 :math:`X = -\ln \varepsilon > 0`, 则当 :math:`x < -X` 时, 有 :math:`e^x < e^{-X} = \varepsilon`, 即
   :math:`\lim\limits_{x \to -\infty} e^x = 0`.

2. 用数学语言给出 :math:`\lim\limits_{x \to x_0} f(x) \neq A` 的定义, 并证明 :math:`\lim\limits_{x \to 1} x^3 \neq 8`.

.. proof:proof::

   :math:`\lim\limits_{x \to x_0} f(x) \neq A` 的定义为: 存在正数 :math:`\varepsilon_0`, 使得对任意 :math:`\delta > 0`,
   总存在 :math:`x` 满足 :math:`0 < |x - x_0| < \delta`, 但 :math:`|f(x) - A| \geqslant \varepsilon_0`.

   下面证明 :math:`\lim\limits_{x \to 1} x^3 \neq 8`. 取 :math:`\varepsilon_0 = 3`, 对任意 :math:`\delta > 0`,
   取 :math:`x = 1 + \dfrac{1}{2}\min \{ \delta, 1 \}`, 则 :math:`0 < x - 1 < \delta` 且 :math:`1 < x \leqslant \dfrac{3}{2}`,
   于是 :math:`x^3 \leqslant \dfrac{27}{8}`, 从而

   .. math::
      |x^3 - 8| = 8 - x^3 \geqslant 8 - \dfrac{27}{8} = \dfrac{37}{8} > 3 = \varepsilon_0.

   这就证明了 :math:`\lim\limits_{x \to 1} x^3 \neq 8`.

3. 证明函数极限的局部有界性, 即若 :math:`\lim\limits_{x \to x_0} f(x)` 存在, 则存在 :math:`x_0` 的某个去心邻域 :math:`(x_0 - \delta, x_0 + \delta) \setminus \{ x_0 \}` 和常数 :math:`M`, 使得当 :math:`0 < |x - x_0| < \delta` 时, 总有

   .. math::
      |f(x)| \leqslant M.

.. proof:proof::

   设 :math:`\lim\limits_{x \to x_0} f(x) = A`. 在极限定义中取 :math:`\varepsilon = 1`, 则存在 :math:`\delta > 0`,
   使得当 :math:`0 < |x - x_0| < \delta` 时, 有 :math:`|f(x) - A| < 1`, 从而

   .. math::
      |f(x)| = |f(x) - A + A| \leqslant |f(x) - A| + |A| < |A| + 1.

   取 :math:`M = |A| + 1`, 即证得 :math:`f(x)` 在 :math:`x_0` 的去心邻域 :math:`(x_0 - \delta, x_0 + \delta) \setminus \{ x_0 \}` 内有界.

4. 证明: 若 :math:`\lim\limits_{x \to x_0} f(x) = A`, 则 :math:`\lim\limits_{x \to x_0} |f(x)| = |A|`, 并考虑其逆命题是否成立.

.. proof:proof::

   由不等式 :math:`\bigl| |f(x)| - |A| \bigr| \leqslant |f(x) - A|` 可知, 任给 :math:`\varepsilon > 0`,
   存在 :math:`\delta > 0`, 使得当 :math:`0 < |x - x_0| < \delta` 时, 有 :math:`|f(x) - A| < \varepsilon`, 从而

   .. math::
      \bigl| |f(x)| - |A| \bigr| \leqslant |f(x) - A| < \varepsilon,

   即 :math:`\lim\limits_{x \to x_0} |f(x)| = |A|`.

   逆命题不成立. 例如 :math:`f(x) = \dfrac{|x|}{x}` (:math:`x \neq 0`), 则 :math:`|f(x)| = 1` (:math:`x \neq 0`),
   故 :math:`\lim\limits_{x \to 0} |f(x)| = 1`; 但 :math:`f(x)` 在 :math:`x = 0` 处左极限为 :math:`-1`, 右极限为 :math:`1`,
   极限不存在.

5. 讨论下列函数在 :math:`x = 0` 处的左极限、右极限和极限的存在性.

   (1). :math:`f(x) = \dfrac{x}{|x|}`;

   (2). :math:`f(x) = \begin{cases} 3^x, & x > 0, \\ 1, & x = 0, \\ 1 + x^3, & x < 0. \end{cases}`

.. proof:solution::

   (1). :math:`f(x) = \dfrac{x}{|x|}` 在 :math:`x \neq 0` 时等于 :math:`1` 或 :math:`-1`, 于是左极限
   :math:`\lim\limits_{x \to 0^-} f(x) = -1`, 右极限 :math:`\lim\limits_{x \to 0^+} f(x) = 1`, 两者都存在但不相等,
   因此 :math:`\lim\limits_{x \to 0} f(x)` 不存在.

   (2). 左极限 :math:`\lim\limits_{x \to 0^-} f(x) = \lim\limits_{x \to 0^-} (1 + x^3) = 1`,
   右极限 :math:`\lim\limits_{x \to 0^+} f(x) = \lim\limits_{x \to 0^+} 3^x = 1`, 两者都存在且相等,
   因此 :math:`\lim\limits_{x \to 0} f(x) = 1` 存在.

.. _ex-chap2-sec2-ex6:

6. 证明: 若 :math:`\lim\limits_{x\to\infty} f(x) = a > 0`, 则存在 :math:`X > 0`,
   使得当 :math:`|x| > X` 时, :math:`f(x) > 0`.

.. proof:proof::

   由于 :math:`\lim\limits_{x \to \infty} f(x) = a > 0`, 那么对于 :math:`\varepsilon = \dfrac{a}{2} > 0`,
   存在 :math:`X > 0`, 使得当 :math:`|x| > X` 时, :math:`|f(x) - a| < \varepsilon = \dfrac{a}{2}`.
   也就是说有

   .. math::
      0 < \dfrac{a}{2} < f(x) < \dfrac{3a}{2}.

.. _ex-chap2-sec3:

§2.3 极限运算法则
--------------------------------

1. 计算下列数列极限.

   (1). :math:`\lim\limits_{n \to \infty} \dfrac{2n^2+n-2}{n^2+6}`;

   (2). :math:`\lim\limits_{n \to \infty} \dfrac{2^n+3^n}{3^n+4^n}`;

   (3). :math:`\lim\limits_{n \to \infty} (\sqrt{n+\sqrt{n}} - \sqrt{n})`;

   (4). :math:`\lim\limits_{n \to \infty} (\sqrt[n]{1} + \sqrt[n]{2} + \cdots + \sqrt[n]{100})`;

   (5). :math:`\lim\limits_{n \to \infty} (\sqrt{2}\sqrt[4]{2}\cdots\sqrt[2^n]{2})`;

   (6). :math:`\lim\limits_{n \to \infty} \left( \dfrac{1}{n^2} + \dfrac{2}{n^2} + \cdots + \dfrac{n}{n^2} \right)`;

   (7). :math:`\lim\limits_{n \to \infty} \left( 1 - \dfrac{1}{2^2} \right) \left( 1 - \dfrac{1}{3^2} \right) \cdots \left( 1 - \dfrac{1}{n^2} \right)`.

.. proof:solution::

   (1). 分子分母同除以 :math:`n^2`, 得

   .. math::
      \lim_{n \to \infty} \dfrac{2n^2+n-2}{n^2+6}
      = \lim_{n \to \infty} \dfrac{2 + \frac{1}{n} - \frac{2}{n^2}}{1 + \frac{6}{n^2}} = 2.

   (2). 分子分母同除以 :math:`4^n`, 得

   .. math::
      \lim_{n \to \infty} \dfrac{2^n+3^n}{3^n+4^n}
      = \lim_{n \to \infty} \dfrac{\left(\frac{1}{2}\right)^n + \left(\frac{3}{4}\right)^n}{\left(\frac{3}{4}\right)^n + 1} = \dfrac{0}{1} = 0.

   (3). 分子有理化,

   .. math::
      \lim_{n \to \infty} \left( \sqrt{n+\sqrt{n}} - \sqrt{n} \right)
      = \lim_{n \to \infty} \dfrac{\sqrt{n}}{\sqrt{n+\sqrt{n}} + \sqrt{n}}
      = \lim_{n \to \infty} \dfrac{1}{\sqrt{1 + \frac{1}{\sqrt{n}}} + 1} = \dfrac{1}{2}.

   (4). 由 :math:`\lim\limits_{n \to \infty} \sqrt[n]{k} = 1` (:math:`k` 为固定正整数) 及极限的四则运算法则,

   .. math::
      \lim_{n \to \infty} \left( \sqrt[n]{1} + \sqrt[n]{2} + \cdots + \sqrt[n]{100} \right) = \underbrace{1 + 1 + \cdots + 1}_{100 \text{ 项}} = 100.

   (5). 化为 2 的幂,

   .. math::
      \sqrt{2}\sqrt[4]{2}\cdots\sqrt[2^n]{2}
      = 2^{\frac{1}{2} + \frac{1}{4} + \cdots + \frac{1}{2^n}}
      = 2^{1 - \frac{1}{2^n}}
      \longrightarrow 2.

   (6). 通分求和,

   .. math::
      \lim_{n \to \infty} \left( \dfrac{1}{n^2} + \dfrac{2}{n^2} + \cdots + \dfrac{n}{n^2} \right)
      = \lim_{n \to \infty} \dfrac{n(n+1)}{2n^2} = \dfrac{1}{2}.

   (7). 因式分解后裂项相消,

   .. math::
      \left( 1 - \dfrac{1}{2^2} \right) \left( 1 - \dfrac{1}{3^2} \right) \cdots \left( 1 - \dfrac{1}{n^2} \right)
      = \prod_{k=2}^{n} \dfrac{(k-1)(k+1)}{k^2}
      = \dfrac{1}{n} \cdot \dfrac{n+1}{2}
      = \dfrac{n+1}{2n}
      \longrightarrow \dfrac{1}{2}.

2. 计算下列函数极限.

   (1). :math:`\lim\limits_{x \to 0} \dfrac{x+1}{x^2-x-2}`;

   (2). :math:`\lim\limits_{x \to 2} \dfrac{x^2-4}{x+1}`;

   (3). :math:`\lim\limits_{x \to 1} \dfrac{x^4-1}{x^3-1}`;

   (4). :math:`\lim\limits_{x \to 1} \dfrac{x^2+x-2}{x^2-4x+3}`;

   (5). :math:`\lim\limits_{h \to 0} \dfrac{(x+h)^3-x^3}{h}`;

   (6). :math:`\lim\limits_{x \to 1} \left( \dfrac{1}{x-1} + \dfrac{3}{1-x^3} \right)`;

   (7). :math:`\lim\limits_{x \to 1} \dfrac{x+x^2+\cdots+x^n-n}{x-1}`;

   (8). :math:`\lim\limits_{x \to x_0} a^x`.

.. proof:solution::

   (1). 直接代入 (分母极限不为零),

   .. math::
      \lim_{x \to 0} \dfrac{x+1}{x^2-x-2} = \dfrac{1}{-2} = -\dfrac{1}{2}.

   (2). 直接代入,

   .. math::
      \lim_{x \to 2} \dfrac{x^2-4}{x+1} = \dfrac{0}{3} = 0.

   (3). 约去零因子 :math:`x - 1`,

   .. math::
      \lim_{x \to 1} \dfrac{x^4-1}{x^3-1}
      = \lim_{x \to 1} \dfrac{(x-1)(x+1)(x^2+1)}{(x-1)(x^2+x+1)}
      = \lim_{x \to 1} \dfrac{(x+1)(x^2+1)}{x^2+x+1}
      = \dfrac{2 \times 2}{3} = \dfrac{4}{3}.

   (4). 约去零因子 :math:`x - 1`,

   .. math::
      \lim_{x \to 1} \dfrac{x^2+x-2}{x^2-4x+3}
      = \lim_{x \to 1} \dfrac{(x+2)(x-1)}{(x-3)(x-1)}
      = \lim_{x \to 1} \dfrac{x+2}{x-3}
      = -\dfrac{3}{2}.

   (5). 展开后约去 :math:`h`,

   .. math::
      \lim_{h \to 0} \dfrac{(x+h)^3-x^3}{h}
      = \lim_{h \to 0} \dfrac{3x^2 h + 3xh^2 + h^3}{h}
      = \lim_{h \to 0} \left( 3x^2 + 3xh + h^2 \right) = 3x^2.

   (6). 通分化简, 注意 :math:`\dfrac{1}{1-x^3} = -\dfrac{1}{(x-1)(x^2+x+1)}`,

   .. math::
      \lim_{x \to 1} \left( \dfrac{1}{x-1} + \dfrac{3}{1-x^3} \right)
      = \lim_{x \to 1} \dfrac{x^2 + x + 1 - 3}{(x-1)(x^2+x+1)}
      = \lim_{x \to 1} \dfrac{(x+2)(x-1)}{(x-1)(x^2+x+1)}
      = \lim_{x \to 1} \dfrac{x+2}{x^2+x+1} = 1.

   (7). 将分子拆成 :math:`(x^k - 1)` 之和,

   .. math::
      \lim_{x \to 1} \dfrac{x+x^2+\cdots+x^n-n}{x-1}
      = \sum_{k=1}^{n} \lim_{x \to 1} \dfrac{x^k - 1}{x-1}
      = \sum_{k=1}^{n} k = \dfrac{n(n+1)}{2},

   其中用到 :math:`\lim\limits_{x \to 1} \dfrac{x^k-1}{x-1} = \lim\limits_{x \to 1} (x^{k-1} + x^{k-2} + \cdots + 1) = k`.

   (8). 由指数函数 :math:`a^x` 在定义域内连续 (或按 :math:`a^x` 极限的定义), 直接代入得

   .. math::
      \lim_{x \to x_0} a^x = a^{x_0}.

3. 设
   :math:`f(x) = \dfrac{a_0 x^m + a_1 x^{m-1} + \cdots + a_{m-1} x + a_m}{b_0 x^n + b_1 x^{n-1} + \cdots + b_{n-1} x + b_n}`
   (:math:`a_0 b_0 \neq 0, m \leqslant n`), 求 :math:`\lim\limits_{x \to +\infty} f(x)`.

.. proof:solution::

   分子分母同除以最高次幂 :math:`x^n`, 得

   .. math::
      f(x) = \dfrac{a_0 x^{m-n} + a_1 x^{m-n-1} + \cdots + a_{m-1} x^{1-n} + a_m x^{-n}}
      {b_0 + b_1 x^{-1} + \cdots + b_{n-1} x^{1-n} + b_n x^{-n}},

   当 :math:`x \to +\infty` 时, 分子中各项 :math:`a_i x^{m-n-i} \, (i = 0, 1, \dots, m)` 的次数都不超过零次幂,
   且分母 :math:`\to b_0 \neq 0`. 于是:

   若 :math:`m < n`, 则 :math:`m - n - i < 0`, 分子各项都趋于 :math:`0`, 故 :math:`\lim\limits_{x \to +\infty} f(x) = 0`;

   若 :math:`m = n`, 则分子除首项外各项都趋于 :math:`0`, 故 :math:`\lim\limits_{x \to +\infty} f(x) = \dfrac{a_0}{b_0}`.

4. 判断下列命题是否正确? 正确的请给予证明, 不正确的请举例说明.

   (1). 若 :math:`\{ x_n \}` 收敛, :math:`\{ y_n \}` 发散, 则 :math:`\{ x_n + y_n \}` 和 :math:`\{ x_n y_n \}` 均发散;

   (2). 若 :math:`\{ x_n \}` 和 :math:`\{ y_n \}` 均发散, 则 :math:`\{ x_n + y_n \}` 和 :math:`\{ x_n y_n \}` 均发散.

.. proof:proof::

   (1). 命题不正确, 其中"和必发散"是对的, 但"积必发散"不对.

   先证 :math:`\{ x_n + y_n \}` 必发散: 若不然, 设 :math:`\{ x_n + y_n \}` 收敛, 则由极限的四则运算法则,
   :math:`y_n = (x_n + y_n) - x_n` 是两个收敛数列之差, 应当收敛, 与 :math:`\{ y_n \}` 发散矛盾.

   再举反例说明 :math:`\{ x_n y_n \}` 可以收敛: 取 :math:`x_n \equiv 0` (收敛), :math:`y_n = (-1)^n` (发散),
   则 :math:`x_n y_n \equiv 0` 收敛.

   (2). 命题不正确, "和"与"积"都可以收敛.

   例如 :math:`x_n = (-1)^n`, :math:`y_n = -(-1)^n`, 两者都发散, 但 :math:`x_n + y_n \equiv 0` 收敛.

   又如 :math:`x_n = y_n = (-1)^n`, 两者都发散, 但 :math:`x_n y_n \equiv 1` 收敛.

.. _ex-chap2-sec3-ex5:

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

.. _ex-chap2-sec4:

§2.4 极限存在准则与重要极限
--------------------------------

1. 求下列极限.

   (1). :math:`\lim\limits_{x \to 0} \dfrac{\sin mx}{\sin nx}`;

   (2). :math:`\lim\limits_{x \to 0} \dfrac{1-\cos 3x}{\sin x \tan 2x}`;

   (3). :math:`\lim\limits_{h \to 0} \dfrac{\sin(x+h)-\sin x}{h}`;

   (4). :math:`\lim\limits_{h \to 0} \dfrac{\cos(x+h)-\cos x}{h}`;

   (5). :math:`\lim\limits_{x \to 0} \dfrac{\cos nx-\cos mx}{x^2}`;

   (6). :math:`\lim\limits_{n \to \infty} 3^n \sin \dfrac{x}{3^n}`;

   (7). :math:`\lim\limits_{n \to \infty} \left( 1+\dfrac{4}{n} \right)^{2n}`;

   (8). :math:`\lim\limits_{n \to \infty} \left( 1-\dfrac{1}{n^2} \right)^n`;

   (9). :math:`\lim\limits_{x \to \infty} \left( 1-\dfrac{2}{x} \right)^{5x}`;

   (10). :math:`\lim\limits_{x \to \infty} \left( \dfrac{3-2x}{2-2x} \right)^x`.

.. proof:solution::

   (1). 利用重要极限 :math:`\lim\limits_{u \to 0} \dfrac{\sin u}{u} = 1`,

   .. math::
      \lim_{x \to 0} \dfrac{\sin mx}{\sin nx}
      = \lim_{x \to 0} \dfrac{\sin mx}{mx} \cdot \dfrac{nx}{\sin nx} \cdot \dfrac{m}{n} = \dfrac{m}{n}.

   (2). 利用等价无穷小 :math:`1 - \cos 3x \sim \dfrac{(3x)^2}{2}`, :math:`\sin x \sim x`, :math:`\tan 2x \sim 2x`,

   .. math::
      \lim_{x \to 0} \dfrac{1-\cos 3x}{\sin x \tan 2x}
      = \lim_{x \to 0} \dfrac{\frac{9}{2}x^2}{x \cdot 2x} = \dfrac{9}{4}.

   (3). 和差化积后用重要极限,

   .. math::
      \lim_{h \to 0} \dfrac{\sin(x+h)-\sin x}{h}
      = \lim_{h \to 0} \dfrac{2 \cos \left( x + \dfrac{h}{2} \right) \sin \dfrac{h}{2}}{h}
      = \lim_{h \to 0} \cos \left( x + \dfrac{h}{2} \right) \cdot \dfrac{\sin \frac{h}{2}}{\frac{h}{2}}
      = \cos x.

   (4). 同理,

   .. math::
      \lim_{h \to 0} \dfrac{\cos(x+h)-\cos x}{h}
      = \lim_{h \to 0} \dfrac{-2 \sin \left( x + \dfrac{h}{2} \right) \sin \dfrac{h}{2}}{h}
      = -\sin x.

   (5). 和差化积,

   .. math::
      \cos nx - \cos mx = -2 \sin \dfrac{(n+m)x}{2} \sin \dfrac{(n-m)x}{2}
      \sim -2 \cdot \dfrac{(n+m)x}{2} \cdot \dfrac{(n-m)x}{2}
      = \dfrac{m^2 - n^2}{2} x^2,

   因此

   .. math::
      \lim_{x \to 0} \dfrac{\cos nx-\cos mx}{x^2} = \dfrac{m^2 - n^2}{2}.

   (6). 当 :math:`x \neq 0` 时, 由 :math:`\dfrac{x}{3^n} \to 0` 及 :math:`\sin u \sim u`,

   .. math::
      \lim_{n \to \infty} 3^n \sin \dfrac{x}{3^n}
      = \lim_{n \to \infty} 3^n \cdot \dfrac{x}{3^n} \cdot \dfrac{\sin \frac{x}{3^n}}{\frac{x}{3^n}} = x;

   当 :math:`x = 0` 时极限显然为 :math:`0`, 上式也成立.

   (7). 利用第二重要极限,

   .. math::
      \lim_{n \to \infty} \left( 1+\dfrac{4}{n} \right)^{2n}
      = \lim_{n \to \infty} \left[ \left( 1+\dfrac{4}{n} \right)^{\frac{n}{4}} \right]^{8} = e^8.

   (8). 因式分解 :math:`1 - \dfrac{1}{n^2} = \left( 1 - \dfrac{1}{n} \right) \left( 1 + \dfrac{1}{n} \right)`, 则

   .. math::
      \lim_{n \to \infty} \left( 1-\dfrac{1}{n^2} \right)^n
      = \lim_{n \to \infty} \left( 1-\dfrac{1}{n} \right)^n \cdot \left( 1+\dfrac{1}{n} \right)^n
      = e^{-1} \cdot e = 1.

   (9). 利用第二重要极限,

   .. math::
      \lim_{x \to \infty} \left( 1-\dfrac{2}{x} \right)^{5x}
      = \lim_{x \to \infty} \left[ \left( 1-\dfrac{2}{x} \right)^{-\frac{x}{2}} \right]^{-10} = e^{-10}.

   (10). 将底数变形 :math:`\dfrac{3-2x}{2-2x} = \dfrac{2x-3}{2x-2} = 1 - \dfrac{1}{2x-2}`, 于是

   .. math::
      \lim_{x \to \infty} \left( \dfrac{3-2x}{2-2x} \right)^x
      = \lim_{x \to \infty} \left( 1 - \dfrac{1}{2x-2} \right)^{x}
      = \lim_{x \to \infty} \left[ \left( 1 - \dfrac{1}{2x-2} \right)^{-(2x-2)} \right]^{-\frac{x}{2x-2}}
      = e^{-\frac{1}{2}}.

2. 设 :math:`x_n = \dfrac{1}{2} \cdot \dfrac{3}{4} \cdots \dfrac{2n-1}{2n}`, 证明
   :math:`x_n < \dfrac{1}{\sqrt{2n+1}}`, 并求 :math:`\lim\limits_{n \to \infty} x_n`.

.. proof:proof::

   对每个 :math:`k = 1, 2, \dots, n`, 有 :math:`(2k-1)(2k+1) = 4k^2 - 1 < 4k^2`, 即

   .. math::
      \dfrac{2k-1}{2k} < \dfrac{2k}{2k+1}.

   将 :math:`k = 1, 2, \dots, n` 各式连乘, 得

   .. math::
      x_n = \dfrac{1}{2} \cdot \dfrac{3}{4} \cdots \dfrac{2n-1}{2n}
      < \dfrac{2}{3} \cdot \dfrac{4}{5} \cdots \dfrac{2n}{2n+1}
      = \dfrac{1}{x_n} \cdot \dfrac{1}{2n+1},

   其中最后一步用到了 :math:`x_n \cdot \dfrac{2}{3} \cdot \dfrac{4}{5} \cdots \dfrac{2n}{2n+1} = \dfrac{1 \cdot 2 \cdots 2n}{2 \cdot 3 \cdots (2n+1)} = \dfrac{1}{2n+1}`.
   两边同乘 :math:`x_n > 0`, 即得 :math:`x_n^2 < \dfrac{1}{2n+1}`, 亦即 :math:`x_n < \dfrac{1}{\sqrt{2n+1}}`.

   又 :math:`x_n > 0`, 且 :math:`\dfrac{1}{\sqrt{2n+1}} \to 0`, 由夹逼准则得

   .. math::
      \lim_{n \to \infty} x_n = 0.

3. 利用单调有界准则证明下列数列极限存在.

   (1). :math:`x_n = \dfrac{1}{n+1} + \dfrac{1}{n+2} + \cdots + \dfrac{1}{n+n}`;

   (2). :math:`x_n = \dfrac{1}{1^2} + \dfrac{1}{2^2} + \cdots + \dfrac{1}{n^2}`.

.. proof:proof::

   (1). 数列 :math:`\{ x_n \}` 满足 :math:`x_n = \dfrac{1}{n+1} + \cdots + \dfrac{1}{2n}`, 且

   .. math::
      x_{n+1} - x_n = \dfrac{1}{2n+1} + \dfrac{1}{2n+2} - \dfrac{1}{n+1} = \dfrac{1}{2n+1} - \dfrac{1}{2n+2} > 0,

   故 :math:`\{ x_n \}` 单调递增. 又每一项都小于 :math:`\dfrac{1}{n}`, 所以

   .. math::
      x_n < n \cdot \dfrac{1}{n} = 1,

   即 :math:`\{ x_n \}` 有上界. 由单调有界准则, 数列 :math:`\{ x_n \}` 的极限存在.

   (2). 数列 :math:`\{ x_n \}` 显然单调递增. 对 :math:`k \geqslant 2`, 有 :math:`\dfrac{1}{k^2} < \dfrac{1}{k(k-1)} = \dfrac{1}{k-1} - \dfrac{1}{k}`,
   于是

   .. math::
      x_n = 1 + \sum_{k=2}^{n} \dfrac{1}{k^2} < 1 + \sum_{k=2}^{n} \left( \dfrac{1}{k-1} - \dfrac{1}{k} \right)
      = 1 + 1 - \dfrac{1}{n} < 2,

   即 :math:`\{ x_n \}` 有上界. 由单调有界准则, 数列 :math:`\{ x_n \}` 的极限存在.

.. _ex-chap2-sec4-ex4:

4. 设 :math:`a > 0`, 数列 :math:`\{ x_n \}` 满足 :math:`x_1 = \sqrt{a}`, :math:`x_2 = \sqrt{a + x_1}`,
   ..., :math:`x_n = \sqrt{a + x_{n-1}}`, ..., 证明数列 :math:`\{ x_n \}` 收敛, 并求其极限.

.. proof:proof::

   首先, 很容易观察到 :math:`x_n = \sqrt{a + x_{n-1}} \geqslant \sqrt{a}`. 接下来, 检查数列的单调性.
   由于 :math:`x_1 = \sqrt{a}`, :math:`x_2 = \sqrt{a + \sqrt{a}} > \sqrt{a} = x_1`.
   假设 :math:`x_n > x_{n-1}` 成立, 那么

   .. math::
      x_{n+1} = \sqrt{a + x_n} > \sqrt{a + x_{n-1}} = x_n.

   由数学归纳法可知数列 :math:`\{ x_n \}` 是单调递增的.

   .. note::
      到这里, 还不能用单调有界准则来说明数列收敛, 因为只证明了单调递增数列 :math:`\{ x_n \}` 有下界 :math:`\sqrt{a}`,
      还需要证明的是 :math:`\{ x_n \}` 有上界.

   下面来证明数列 :math:`\{ x_n \}` 有上界. 由于 :math:`x_n = \sqrt{a + x_{n-1}} < \sqrt{a + x_n}`,
   那么 :math:`x_n^2 - x_n - a < 0`, 即

   .. math::
      \left( x_n - \dfrac{1 + \sqrt{1 + 4a}}{2} \right) \left( x_n - \dfrac{1 - \sqrt{1 + 4a}}{2} \right) < 0.

   由于 :math:`x_n > 0`, 那么 :math:`x_n < \dfrac{1 + \sqrt{1 + 4a}}{2}`. 这样就证明了数列 :math:`\{ x_n \}` 有上界.
   由单调有界准则可知数列 :math:`\{ x_n \}` 收敛.

   设 :math:`\lim\limits_{n \to \infty} x_n = A`, 那么对数列的递推关系式取极限, 有

   .. math::
      A = \sqrt{a + A},

   解得 :math:`A = \dfrac{1 + \sqrt{1 + 4a}}{2}` (舍去负根).

.. _ex-chap2-sec4-ex5:

5. 设 :math:`a_1, a_2, \dots, a_k` 是 :math:`k` 个正数, 求极限
   :math:`\lim\limits_{n \to \infty} \sqrt[n]{a_1^n + a_2^n + \cdots + a_k^n}`.

.. proof:solution::

   记 :math:`M = \max \{ a_1, a_2, \dots, a_k \}`. 那么有

   .. math::
      M = \sqrt[n]{M^n} \leqslant \sqrt[n]{a_1^n + a_2^n + \cdots + a_k^n}
      \leqslant \sqrt[n]{k M^n} = \sqrt[n]{k} \cdot M.

   由于 :math:`\lim\limits_{n \to \infty} \sqrt[n]{k} = 1`, 由夹逼准则可知

   .. math::
      \lim_{n \to \infty} \sqrt[n]{a_1^n + a_2^n + \cdots + a_k^n} = M = \max \{ a_1, a_2, \dots, a_k \}.

6. 设数列 :math:`\{ x_n \}` 满足下列条件 :math:`|x_{n+1}| \leqslant q|x_n|`, 其中 :math:`q`
   是一个小于 1 的正数, 证明 :math:`\lim\limits_{n \to \infty} x_n = 0`.

.. proof:proof::

   由条件递推可得

   .. math::
      |x_n| \leqslant q |x_{n-1}| \leqslant q^2 |x_{n-2}| \leqslant \cdots \leqslant q^{n-1} |x_1|.

   由于 :math:`0 < q < 1`, 有 :math:`\lim\limits_{n \to \infty} q^{n-1} |x_1| = 0`, 又 :math:`|x_n| \geqslant 0`,
   由夹逼准则得 :math:`\lim\limits_{n \to \infty} |x_n| = 0`, 即 :math:`\lim\limits_{n \to \infty} x_n = 0`.

.. _ex-chap2-sec4-ex7:

7. 斐波那契数列 :math:`\{ x_n \}` 如下定义:

   .. math::
      x_1 = 1, x_2 = 1, \dots, x_{n+1} = x_n + x_{n-1},

   记 :math:`y_n = \dfrac{x_{n+1}}{x_n}`.

   (1). 证明 :math:`\{ y_n \}` 收敛;

   (2). 求 :math:`\lim\limits_{n\to\infty} y_n`.

.. proof:proof::

   从斐波那契数列 :math:`\{ x_n \}` 的定义式出发, 有

   .. math::
      y_1 = 1, \dots, y_{n} = 1 + \dfrac{1}{y_{n-1}}.

   由此可见 :math:`y_n \geqslant 1`, 即 1 是它的一个下界. 另一方面, 由 :math:`y_n \geqslant 1` 可推出

   .. math::
      y_{n} = 1 + \dfrac{1}{y_{n-1}} \leqslant 1 + \dfrac{1}{1} = 2,

   即数列 :math:`\{ y_n \}` 满足 :math:`1 \leqslant y_n \leqslant 2`.

   接下来, 检查数列 :math:`\{ y_n \}` 的单调性. 但是经过检查发现, 数列 :math:`\{ y_n \}` 没有单调性:

   .. math::
      \text{假设} ~ y_n > y_{n-1} ~ \implies ~ y_{n+1} = 1 + \dfrac{1}{y_n} < 1 + \dfrac{1}{y_{n-1}} = y_n; \\
      \text{假设} ~ y_n < y_{n-1} ~ \implies ~ y_{n+1} = 1 + \dfrac{1}{y_n} > 1 + \dfrac{1}{y_{n-1}} = y_n.

   但是可以考察 :math:`y_n` 的偶数项与奇数项, 可以发现它们分别是单调的:

   .. math::
      y_{n} = 1 + \dfrac{1}{y_{n-1}} = 1 + \dfrac{1}{1 + \dfrac{1}{y_{n-2}}} = \dfrac{2 y_{n-2} + 1}{y_{n-2} + 1},

   那么有

   .. math::
      y_{n} - y_{n-2} & = \dfrac{2 y_{n-2} + 1}{y_{n-2} + 1} - y_{n-2} = \dfrac{1 + y_{n-2} - y_{n-2}^2}{y_{n-2} + 1} \\
      & = - \dfrac{(y_{n-2} - \frac{1 + \sqrt{5}}{2})(y_{n-2} - \frac{1 - \sqrt{5}}{2})}{y_{n-2} + 1}.

   记 :math:`L = \frac{1 + \sqrt{5}}{2}`, 从上式可以看出

   .. math::
      \text{若} ~ y_n \geqslant L ~ \implies~ y_n - y_{n-2} \leqslant 0; \\
      \text{若} ~ y_n \leqslant L ~ \implies~ y_n - y_{n-2} \geqslant 0.

   接下来, 可以用数学归纳法证明 :math:`y_{2n} \geqslant L` 且 :math:`y_{2n-1} \leqslant L`:

   .. math::
      y_1 = 1 \leqslant L, \dots, y_{2n+1} = 1 + \dfrac{1}{y_{2n}} \leqslant 1 + \dfrac{1}{L} = L; \\
      y_2 = 2 \geqslant L, \dots, y_{2n+2} = 1 + \dfrac{1}{y_{2n+1}} \geqslant 1 + \dfrac{1}{L} = L.

   由此可知数列 :math:`\{ y_{2n} \}` 是单调递减且有下界的, 因此它收敛; 数列 :math:`\{ y_{2n-1} \}` 是单调递增且有上界的, 因此它也收敛.
   设 :math:`\lim\limits_{n \to \infty} y_{2n} = A`, :math:`\lim\limits_{n \to \infty} y_{2n-1} = B`, 那么由递推关系式有

   .. math::
      A = 1 + \dfrac{1}{B}, \quad B = 1 + \dfrac{1}{A}.

   解得 :math:`A = B = L`. 由于数列 :math:`\{ y_n \}` 的偶数项与奇数项的极限相等, 因此数列 :math:`\{ y_n \}` 收敛, 且

   .. math::
      \lim_{n \to \infty} y_n = L = \dfrac{1 + \sqrt{5}}{2}.

.. _ex-chap2-sec5:

§2.5 无穷大量与无穷小量
--------------------------------

1. 证明: 当 :math:`x \to 0` 时, 有

   (1). :math:`\sec x - 1 \sim \dfrac{x^2}{2}`;

   (2). :math:`\sqrt{\tan x + 1} - \sqrt{\sin x + 1} \sim \dfrac{x^3}{4}`.

.. proof:proof::

   (1). 分子有理化并利用 :math:`1 - \cos x \sim \dfrac{x^2}{2}`,

   .. math::
      \sec x - 1 = \dfrac{1-\cos x}{\cos x} \sim \dfrac{\frac{x^2}{2}}{1} = \dfrac{x^2}{2},

   其中 :math:`x \to 0` 时 :math:`\cos x \to 1`.

   (2). 分子有理化,

   .. math::
      \sqrt{\tan x + 1} - \sqrt{\sin x + 1}
      = \dfrac{\tan x - \sin x}{\sqrt{\tan x + 1} + \sqrt{\sin x + 1}}
      \sim \dfrac{\tan x - \sin x}{2},

   其中 :math:`x \to 0` 时分母 :math:`\to 2`. 又

   .. math::
      \tan x - \sin x = \tan x (1 - \cos x) \sim x \cdot \dfrac{x^2}{2} = \dfrac{x^3}{2},

   因此 :math:`\sqrt{\tan x + 1} - \sqrt{\sin x + 1} \sim \dfrac{1}{2} \cdot \dfrac{x^3}{2} = \dfrac{x^3}{4}`.

.. _ex-chap2-sec5-ex2:

2. 计算下列极限.

   (1). :math:`\lim\limits_{x \to 0} \dfrac{\sin^2 x}{\sin x}`;

   (2). :math:`\lim\limits_{x \to 0} \dfrac{1-\cos 3x}{x \sin 2x}`;

   (3). :math:`\lim\limits_{x \to 0} \dfrac{e^x - e^{\cos x}}{x \tan x}`;

   (4). :math:`\lim\limits_{x \to 0} \dfrac{\ln(1+x^3)}{\tan x - \sin x}`;

   (5). :math:`\lim\limits_{x \to +\infty} x \left[ \ln(1+x) - x \right]`;

   (6). :math:`\lim\limits_{x \to +\infty} \dfrac{\ln(2+e^{3x})}{\ln(3+e^{2x})}`.

.. proof:solution::

   (1). 约分后用重要极限,

   .. math::
      \lim_{x \to 0} \dfrac{\sin^2 x}{\sin x} = \lim_{x \to 0} \sin x = 0.

   (2). 利用等价无穷小 :math:`1 - \cos 3x \sim \dfrac{(3x)^2}{2}`, :math:`\sin 2x \sim 2x`,

   .. math::
      \lim_{x \to 0} \dfrac{1-\cos 3x}{x \sin 2x} = \lim_{x \to 0} \dfrac{\frac{9}{2}x^2}{x \cdot 2x} = \dfrac{9}{4}.

   (3). 这不是未定式. 分子极限

   .. math::
      \lim_{x \to 0} \left( e^x - e^{\cos x} \right) = 1 - e \neq 0,

   而分母 :math:`x \tan x > 0` (:math:`x \neq 0` 附近) 且 :math:`x \tan x \to 0^+`, 故

   .. math::
      \lim_{x \to 0} \dfrac{e^x - e^{\cos x}}{x \tan x} = -\infty.

   (4). 利用等价无穷小 :math:`\ln(1+x^3) \sim x^3`, :math:`\tan x - \sin x = \tan x(1-\cos x) \sim x \cdot \dfrac{x^2}{2} = \dfrac{x^3}{2}`,

   .. math::
      \lim_{x \to 0} \dfrac{\ln(1+x^3)}{\tan x - \sin x} = \lim_{x \to 0} \dfrac{x^3}{\frac{x^3}{2}} = 2.

   (5). 由于

   .. math::
      \lim\limits_{x \to +\infty} [\ln(x + 1) - x] = \lim\limits_{x \to +\infty} \ln \dfrac{x + 1}{e^x} = -\infty,

   因此 :math:`\lim\limits_{x \to +\infty} x[\ln(x + 1) - x] = -\infty`.

   .. note::
      这题应该又是一个印刷错误, 正确的题目应该是计算 :math:`\lim\limits_{x \to +\infty} x[\ln(x + 1) - \ln x]`,
      那么计算过程如下:

      .. math::
         \lim_{x \to +\infty} x[\ln(x + 1) - \ln x] = \lim_{x \to +\infty} x \ln \left( 1 + \dfrac{1}{x} \right)
         \xlongequal{t = \frac{1}{x}} \lim_{t \to 0^+} \dfrac{\ln(1 + t)}{t} = 1.

   (6). 分子分母各提出主部: 当 :math:`x \to +\infty` 时,

   .. math::
      \ln(2 + e^{3x}) = 3x + \ln \left( 1 + 2e^{-3x} \right), \quad
      \ln(3 + e^{2x}) = 2x + \ln \left( 1 + 3e^{-2x} \right),

   其中 :math:`\ln \left( 1 + 2e^{-3x} \right) \to 0`, :math:`\ln \left( 1 + 3e^{-2x} \right) \to 0`. 于是

   .. math::
      \lim_{x \to +\infty} \dfrac{\ln(2+e^{3x})}{\ln(3+e^{2x})}
      = \lim_{x \to +\infty} \dfrac{3x + \ln(1 + 2e^{-3x})}{2x + \ln(1 + 3e^{-2x})}
      = \lim_{x \to +\infty} \dfrac{3 + \frac{1}{x}\ln(1 + 2e^{-3x})}{2 + \frac{1}{x}\ln(1 + 3e^{-2x})}
      = \dfrac{3}{2}.

3. 设 :math:`x \to x_0` 时, :math:`g(x)` 是有界量, :math:`f(x)` 是无穷大, 证明
   :math:`g(x) \pm f(x)` 是无穷大.

.. proof:proof::

   设 :math:`x \to x_0` 时 :math:`|g(x)| \leqslant M` (在 :math:`x_0` 的某去心邻域内). 任给 :math:`G > 0`,
   由 :math:`f(x)` 是无穷大, 存在 :math:`\delta > 0`, 使得当 :math:`0 < |x - x_0| < \delta` 时,
   有 :math:`|f(x)| > G + M`. 于是当 :math:`0 < |x - x_0| < \delta` 时,

   .. math::
      |g(x) \pm f(x)| \geqslant |f(x)| - |g(x)| > (G + M) - M = G,

   即 :math:`g(x) \pm f(x)` 是当 :math:`x \to x_0` 时的无穷大.

4. 设 :math:`x \to x_0` 时, :math:`g(x)` 是有界量, :math:`f(x)` 是无穷大, 请问
   :math:`g(x) \cdot f(x)` 是否为无穷大?

.. proof:solution::

   不一定是无穷大, 乘积的类型取决于 :math:`g(x)` 趋于零 (或保持有界) 的快慢. 例如取 :math:`x_0 = 0`,
   :math:`f(x) = \dfrac{1}{x}` 是当 :math:`x \to 0` 时的无穷大:

   取 :math:`g(x) = x^2`, 它是有界量, 但 :math:`g(x) f(x) = x \to 0`, 乘积是无穷小;

   取 :math:`g(x) = x`, 它是有界量, 但 :math:`g(x) f(x) \equiv 1`, 乘积既非无穷大也非无穷小;

   取 :math:`g(x) = \sqrt{|x|}`, 它是有界量, 此时 :math:`g(x) f(x) = \dfrac{\sqrt{|x|}}{x} \to \infty`, 乘积是无穷大.

5. 设当 :math:`x \to x_0` 时, :math:`f(x) \sim g(x)`, 证明:
   :math:`f(x) - g(x) = o[g(x)]` 或者 :math:`f(x) - g(x) = o[f(x)]`.

.. proof:proof::

   由 :math:`f(x) \sim g(x)` 知 :math:`\lim\limits_{x \to x_0} \dfrac{f(x)}{g(x)} = 1`, 于是

   .. math::
      \lim_{x \to x_0} \dfrac{f(x) - g(x)}{g(x)} = \lim_{x \to x_0} \dfrac{f(x)}{g(x)} - 1 = 0,

   即 :math:`f(x) - g(x) = o[g(x)]`.

   又 :math:`g(x) \sim f(x)` (等价是相互的), 故 :math:`\lim\limits_{x \to x_0} \dfrac{g(x)}{f(x)} = 1`, 同理

   .. math::
      \lim_{x \to x_0} \dfrac{f(x) - g(x)}{f(x)} = 1 - \lim_{x \to x_0} \dfrac{g(x)}{f(x)} = 0,

   即 :math:`f(x) - g(x) = o[f(x)]`.

.. _ex-chap2-sec6:

§2.6 函数的连续性和间断点
--------------------------------

1. 下列函数在 :math:`x = 0` 处是否连续? 为什么?

   (1). :math:`f(x) = \begin{cases} x\sin\dfrac{1}{x}, & x \neq 0, \\ 0, & x = 0; \end{cases}`

   (2). :math:`f(x) = \begin{cases} e^{2x}, & x \leqslant 0, \\ \dfrac{\sin x}{x}, & x > 0. \end{cases}`

.. proof:solution::

   (1). 由 :math:`\left| x\sin\dfrac{1}{x} \right| \leqslant |x| \to 0` 得 :math:`\lim\limits_{x \to 0} f(x) = 0 = f(0)`,
   故 :math:`f(x)` 在 :math:`x = 0` 处连续.

   (2). 左极限 :math:`\lim\limits_{x \to 0^-} e^{2x} = 1`, 右极限 :math:`\lim\limits_{x \to 0^+} \dfrac{\sin x}{x} = 1`,
   两者相等且等于函数值 :math:`f(0) = e^0 = 1`, 故 :math:`f(x)` 在 :math:`x = 0` 处连续.

2. 研究下列函数的连续性.

   (1). :math:`f(x) = \dfrac{1}{e^x - 1}`;

   (2). :math:`f(x) = \dfrac{\ln(1-2x)}{x}`;

   (3). :math:`f(x) = \dfrac{x^2 - 2x - 3}{x^2 - 3x - 4}`;

   (4). :math:`f(x) = \sin^2 \dfrac{1}{x}`.

.. proof:solution::

   (1). :math:`f(x) = \dfrac{1}{e^x - 1}` 是初等函数, 在定义区间 :math:`(-\infty, 0)` 与 :math:`(0, +\infty)` 内连续.
   在 :math:`x = 0` 处无定义, 且 :math:`\lim\limits_{x \to 0^+} \dfrac{1}{e^x - 1} = +\infty`,
   :math:`\lim\limits_{x \to 0^-} \dfrac{1}{e^x - 1} = -\infty`, 故 :math:`x = 0` 是第二类 (无穷) 间断点.

   (2). 定义域为 :math:`x < \dfrac{1}{2}` 且 :math:`x \neq 0`, :math:`f(x)` 在 :math:`(-\infty, 0)` 与 :math:`(0, \tfrac{1}{2})` 内连续.
   在 :math:`x = 0` 处, :math:`\lim\limits_{x \to 0} \dfrac{\ln(1-2x)}{x} = \lim\limits_{x \to 0} \dfrac{-2x}{x} = -2`,
   极限存在但函数在 :math:`x=0` 无定义, 故 :math:`x = 0` 是第一类 (可去) 间断点.

   (3). 因式分解 :math:`f(x) = \dfrac{(x-3)(x+1)}{(x-4)(x+1)}`, 定义域为 :math:`x \neq -1, 4`,
   :math:`f(x)` 在 :math:`(-\infty, -1)`, :math:`(-1, 4)`, :math:`(4, +\infty)` 内连续.
   在 :math:`x = -1` 处, :math:`\lim\limits_{x \to -1} \dfrac{x-3}{x-4} = \dfrac{4}{5}`, 为第一类 (可去) 间断点;
   在 :math:`x = 4` 处, :math:`\lim\limits_{x \to 4} \dfrac{x-3}{x-4} = \infty`, 为第二类 (无穷) 间断点.

   (4). :math:`f(x)` 在 :math:`x \neq 0` 处连续. 在 :math:`x = 0` 处无定义, 且 :math:`x \to 0` 时 :math:`\dfrac{1}{x} \to \infty`,
   :math:`\sin^2 \dfrac{1}{x}` 在 :math:`0` 与 :math:`1` 之间无限振荡, 极限不存在, 故 :math:`x = 0` 是第二类 (振荡) 间断点.

3. 求下列极限.

   (1). :math:`\lim\limits_{x \to 0} \dfrac{\ln(1+x^2)}{\sin(1+x^2)}`;

   (2). :math:`\lim\limits_{x \to \frac{\pi}{6}} \ln(2\cos 2x)`;

   (3). :math:`\lim\limits_{x \to 0} \sqrt{x^2 - 2x + 5}`;

   (4). :math:`\lim\limits_{x \to 1} \dfrac{\sqrt{1+x} - 1}{x}`.

.. proof:solution::

   这些极限都由连续函数直接代入 (或作简单变形) 求得:

   (1). :math:`x \to 0` 时分子 :math:`\ln(1+x^2) \to \ln 1 = 0`, 分母 :math:`\sin(1+x^2) \to \sin 1 \neq 0`, 故极限为 :math:`0`.

   (2). :math:`\ln(2\cos 2x)` 在 :math:`x = \dfrac{\pi}{6}` 处连续, 直接代入得
   :math:`\ln\left( 2\cos\dfrac{\pi}{3} \right) = \ln 1 = 0`.

   (3). :math:`\sqrt{x^2 - 2x + 5}` 在 :math:`x = 0` 处连续, 直接代入得 :math:`\sqrt{5}`.

   (4). 分子有理化,

   .. math::
      \lim_{x \to 1} \dfrac{\sqrt{1+x} - 1}{x}
      = \lim_{x \to 1} \dfrac{x}{x\left(\sqrt{1+x} + 1\right)}
      = \lim_{x \to 1} \dfrac{1}{\sqrt{1+x} + 1} = \dfrac{1}{\sqrt{2}+1} = \sqrt{2}-1.

4. 设 :math:`f(x) = \begin{cases} a+x, & x < 0, \\ 1, & x = 0, \\ \ln(b+x+x^2), & x > 0, \end{cases}`
   已知 :math:`f(x)` 在 :math:`x = 0` 处连续, 试确定 :math:`a` 和 :math:`b` 的值.

.. proof:solution::

   :math:`f(x)` 在 :math:`x = 0` 处连续等价于左、右极限都存在且等于 :math:`f(0) = 1`. 计算

   .. math::
      \lim_{x \to 0^-} f(x) = \lim_{x \to 0^-} (a + x) = a, \qquad
      \lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} \ln(b + x + x^2) = \ln b,

   故需 :math:`a = \ln b = 1`, 解得

   .. math::
      a = 1, \qquad b = e.

   此时 :math:`b + x + x^2 = e + x + x^2 > 0` 在 :math:`x = 0` 附近成立, 符合题意.

5. 求函数 :math:`f(x) = \dfrac{x^3 + 3x^2 - x - 3}{x^2 + x - 6}` 的连续区间, 并求极限
   :math:`\lim\limits_{x \to 0} f(x)`, :math:`\lim\limits_{x \to 2} f(x)` 和 :math:`\lim\limits_{x \to -3} f(x)`.

.. proof:solution::

   因式分解:

   .. math::
      f(x) = \dfrac{x^3 + 3x^2 - x - 3}{x^2 + x - 6}
      = \dfrac{(x+3)(x-1)(x+1)}{(x+3)(x-2)}
      = \dfrac{(x-1)(x+1)}{x-2} \quad (x \neq -3).

   定义域为 :math:`x \neq -3, 2`, 故连续区间为 :math:`(-\infty, -3)`, :math:`(-3, 2)`, :math:`(2, +\infty)`;
   其中 :math:`x = -3` 是第一类 (可去) 间断点, :math:`x = 2` 是第二类 (无穷) 间断点.

   由连续性 (或约分后的表达式) 计算各极限:

   .. math::
      \lim_{x \to 0} f(x) = \dfrac{(0-1)(0+1)}{0-2} = \dfrac{1}{2}; \qquad
      \lim_{x \to 2} f(x) = \lim_{x \to 2} \dfrac{(x-1)(x+1)}{x-2} = \infty;

   .. math::
      \lim_{x \to -3} f(x) = \lim_{x \to -3} \dfrac{(x-1)(x+1)}{x-2} = \dfrac{(-4) \times (-2)}{-5} = -\dfrac{8}{5}.

6. 设函数 :math:`g(x)` 在 :math:`x_0` 处连续, 且 :math:`\lim\limits_{x \to x_0} g(x) = 0`,
   已知 :math:`|f(x)| \leqslant |g(x)|`, 证明 :math:`f(x)` 在 :math:`x_0` 处也连续.

.. proof:proof::

   在 :math:`x = x_0` 处, 由条件 :math:`|f(x_0)| \leqslant |g(x_0)| = 0`, 得 :math:`f(x_0) = 0`.

   任给 :math:`\varepsilon > 0`. 由 :math:`g(x)` 在 :math:`x_0` 处连续且 :math:`g(x_0) = 0`, 即
   :math:`\lim\limits_{x \to x_0} g(x) = 0`, 存在 :math:`\delta > 0`, 使得当 :math:`0 < |x - x_0| < \delta` 时,
   有 :math:`|g(x)| < \varepsilon`. 于是当 :math:`0 < |x - x_0| < \delta` 时,

   .. math::
      |f(x) - f(x_0)| = |f(x)| \leqslant |g(x)| < \varepsilon.

   这就证明了 :math:`\lim\limits_{x \to x_0} f(x) = 0 = f(x_0)`, 即 :math:`f(x)` 在 :math:`x_0` 处连续.

.. _ex-chap2-sec7:

§2.7 闭区间上连续函数的性质
--------------------------------

1. 证明方程 :math:`2^x = x^2` 在 :math:`(-1,1)` 内必有实根. (提示: 对 :math:`f(x) = 2^x - x^2`
   在 :math:`[-1,1]` 上应用零点存在定理进行证明.)

.. proof:proof::

   按提示, 令 :math:`f(x) = 2^x - x^2`, 它是初等函数, 在闭区间 :math:`[-1, 1]` 上连续. 计算

   .. math::
      f(-1) = 2^{-1} - (-1)^2 = \dfrac{1}{2} - 1 = -\dfrac{1}{2} < 0, \qquad
      f(1) = 2 - 1 = 1 > 0.

   由零点存在定理, 存在 :math:`x_0 \in (-1, 1)`, 使得 :math:`f(x_0) = 0`, 即 :math:`2^{x_0} = x_0^2`.
   故方程 :math:`2^x = x^2` 在 :math:`(-1, 1)` 内必有实根.

2. 用零点定理证明介值定理.

.. proof:proof::

   设 :math:`f(x)` 在 :math:`[a, b]` 上连续, :math:`c` 介于 :math:`f(a)` 与 :math:`f(b)` 之间, 不妨设
   :math:`f(a) < c < f(b)` (若 :math:`c = f(a)` 或 :math:`c = f(b)`, 取 :math:`x = a` 或 :math:`x = b` 即可;
   若 :math:`f(a) > f(b)`, 对 :math:`-f(x)` 用同样的论证).

   作辅助函数 :math:`F(x) = f(x) - c`, 则 :math:`F(x)` 在 :math:`[a, b]` 上连续, 且

   .. math::
      F(a) = f(a) - c < 0, \qquad F(b) = f(b) - c > 0.

   由零点存在定理, 存在 :math:`x_0 \in (a, b)`, 使得 :math:`F(x_0) = 0`, 即 :math:`f(x_0) = c`. 介值定理得证.

3. 设 :math:`f(x)` 在 :math:`[0,1]` 上连续, 并且当 :math:`x \in [0,1]` 时, :math:`0 < f(x) < 1`.
   证明存在 :math:`x_0 \in (0,1)`, 使得 :math:`f(x_0) = x_0` 成立.

.. proof:proof::

   作辅助函数 :math:`F(x) = f(x) - x`, 则 :math:`F(x)` 在 :math:`[0, 1]` 上连续, 且

   .. math::
      F(0) = f(0) - 0 = f(0) > 0, \qquad F(1) = f(1) - 1 < 0.

   由零点存在定理, 存在 :math:`x_0 \in (0, 1)`, 使得 :math:`F(x_0) = 0`, 即 :math:`f(x_0) = x_0`.

4. 设 :math:`f(x)` 在 :math:`(a,b)` 上连续, :math:`x_1, x_2 \in (a,b)`, :math:`x_1 < x_2` 且
   :math:`f(x_1) < f(x_2)`. 求证: 对任何 :math:`c \in [f(x_1), f(x_2)]`, 存在
   :math:`x \in (a,b)`, 使得 :math:`f(x) = c` 成立.

.. proof:proof::

   由于 :math:`[x_1, x_2] \subset (a, b)`, :math:`f(x)` 在闭区间 :math:`[x_1, x_2]` 上连续.

   若 :math:`c = f(x_1)`, 取 :math:`x = x_1`; 若 :math:`c = f(x_2)`, 取 :math:`x = x_2`, 结论成立.

   若 :math:`f(x_1) < c < f(x_2)`, 由介值定理 (在 :math:`[x_1, x_2]` 上应用), 存在
   :math:`x \in (x_1, x_2) \subset (a, b)`, 使得 :math:`f(x) = c`. 综上, 结论成立.

.. _extra-chap2:

补充内容
================================

.. _extra-chap2-sec2:

§2.2 函数的极限
--------------------------------

.. _extra-chap2-sec2-topic1:

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

.. _extra-chap2-sec4:

§2.4 极限存在准则与重要极限
--------------------------------------------

.. _extra-chap2-sec4-topic1:

1. 求 :math:`\lim\limits_{x \to 0} x \left[ \dfrac{1}{x} \right]`

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

.. _extra-chap2-sec6:

§2.6 函数的连续性和间断点
--------------------------------------------

.. _extra-chap2-sec6-topic1:

1. Riemann 函数定义为

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
