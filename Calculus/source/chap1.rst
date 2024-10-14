第一章  函数与极限
^^^^^^^^^^^^^^^^^^^^^^^^^

.. contents:: :local:


课后习题解答
=================

§1.1 函数
--------------------------------

1. 确定函数在指定区间内的单调性

(1). :math:`y = \dfrac{x}{1-x}, \quad (-\infty, 1)`

.. proof:solution::

    由于 :math:`y = -1 + \dfrac{1}{1-x}`, 而 :math:`1 - x` 在区间 :math:`(-\infty, 1)` 上是单调递减的, 从而知 :math:`\dfrac{1}{1-x}` 单调递增,
    进而知 :math:`y = -1 + \dfrac{1}{1-x}` 单调递增.

    .. note::

        也可以直接求导数 :math:`y' = \dfrac{1}{(1-x)^2}`, 由于 :math:`(1-x)^2 > 0`, 所以 :math:`y' > 0`, 从而知 :math:`y` 单调递增.

(2). :math:`y = e^{\frac{1}{x}}, \quad (0, +\infty)`

.. proof:solution::

    由于 :math:`y = e^u` 单调递增, 而 :math:`u = \dfrac{1}{x}` 在 :math:`x \in (0, +\infty)` 上单调递减, 所以 :math:`y = e^{\frac{1}{x}}` 单调递减.

    .. note::

        也可以直接求导数 :math:`y' = -\dfrac{1}{x^2} e^{\frac{1}{x}}`, 由于 :math:`x > 0`, 所以 :math:`y' < 0`, 从而知 :math:`y` 单调递减.

2. 确定函数奇偶性

(1). :math:`f(x) = \ln (x + \sqrt{1 + x^2})`

.. proof:solution::

    :math:`f(x)` 的定义域为 :math:`(-\infty, +\infty)`, 关于原点对称. 由于

    .. math::

        \begin{align*}
        f(-x) & = \ln (-x + \sqrt{1 + (-x)^2}) = \ln (-x + \sqrt{1 + x^2}) = \ln \dfrac{1}{x + \sqrt{1 + x^2}} \\
        & = - \ln (x + \sqrt{1 + x^2}) = - f(x),
        \end{align*}

    所以 :math:`f(x)` 是奇函数.

(2). :math:`f(x) = \dfrac{a^x + a^{-x}}{2}, \quad a > 0`

.. proof:solution::

    :math:`f(x)` 的定义域为 :math:`(-\infty, +\infty)`, 关于原点对称. 由于

    .. math::

        f(-x) = \dfrac{a^{-x} + a^x}{2} = \dfrac{a^x + a^{-x}}{2} = f(x),

    所以 :math:`f(x)` 是偶函数.

3. 下列哪些函数是周期函数, 周期是多少?

(1). :math:`f(x) = x \sin x`; (2). :math:`f(x) = \cos^2 x`

.. proof:solution::

    (1). :math:`f(x)` 不是周期函数. 假设 :math:`f(x)` 是周期函数, 以 :math:`T > 0` 为周期, 那么 :math:`\forall x \in \mathbb{R}`, 有 :math:`f(x + T) = f(x)`,
    特别地取 :math:`x = 0`, 那么 :math:`T \sin T = f(T) = f(0) = 0`, 由于 :math:`T > 0`, 所以 :math:`\sin T = 0`, 即 :math:`T = k \pi`, 其中 :math:`k \in \mathbb{N}^+`.
    将其代入 :math:`f(x + T) = f(x)` 有

    .. math::

        (x + k \pi) \sin (x + k \pi) = (x + k \pi) (\pm \sin x) = f(x + T) = f(x) = x \sin x

    在 :math:`x \neq k \pi` 处, 能从上式得到 :math:`x = \pm (x + k \pi)`, 进而有 :math:`k \pi = 0` 或者 :math:`x = -\dfrac{k \pi}{2}`, 这都是当 :math:`x \neq k \pi` 时不可能成立,
    或者不恒成立的, 所以 :math:`f(x)` 不是周期函数.

    (2). :math:`f(x)` 是周期函数, 因为 :math:`f(x) = \cos^2 x = \dfrac{1 + \cos 2x}{2}`, 由于 :math:`\cos 2x` 的周期是 :math:`k\pi`,
    所以 :math:`f(x)` 的周期是 :math:`k\pi`, 其中 :math:`k \in \mathbb{N}^+`.

4. 设 :math:`f(x)` 为定义在 :math:`(-\ell, \ell)` 内的奇函数, 若 :math:`f(x)` 在 :math:`(0, \ell)` 内单调增加, 且 :math:`f(0) = 0`,
证明 :math:`f(x)` 在 :math:`(-\ell, 0)` 内也单调增加.

.. proof:proof::

    由于 :math:`f(x)` 在 :math:`(0, \ell)` 内单调增加, 所以 :math:`f(x_1) \leqslant f(x_2)` 对于 :math:`0 < x_1 < x_2 < \ell` 成立.
    现任取 :math:`-\ell < x_1 < x_2 < 0`, 那么有 :math:`0 < -x_2 < -x_1 < \ell`, 由于 :math:`f(x)` 是奇函数, 所以有

    .. math::

        f(x_2) = -f(-x_2) \leqslant -f(-x_1) = f(x_1),

    由于 :math:`x_1, x_2` 的任意性, 所以 :math:`f(x)` 在 :math:`(-\ell, 0)` 内单调增加.

5. 设下面所考虑的函数都是定义在区间 :math:`(-\ell, \ell)` 上的, 证明:

(1). 两个偶函数的和是偶函数, 两个奇函数的和是奇函数；

(2). 两个偶函数的乘积是偶函数, 两个奇函数的乘积是偶函数, 偶函数与奇函数的乘积是奇函数.

.. proof:proof::

    (1). 设 :math:`f(x), g(x)` 是偶函数, 那么 :math:`f(-x) = f(x), g(-x) = g(x)`, 记 :math:`h(x) = f(x) + g(x)`, 那么

    .. math::

        h(-x) = f(-x) + g(-x) = f(x) + g(x) = h(x),

    所以 :math:`h(x)` 是偶函数. 若 :math:`f(x), g(x)` 是奇函数, 那么 :math:`f(-x) = -f(x), g(-x) = -g(x)`, 那么

    .. math::

        h(-x) = f(-x) + g(-x) = -f(x) - g(x) = -(f(x) + g(x)) = -h(x),

    所以 :math:`h(x)` 是奇函数.

    (2). 设 :math:`f(x), g(x)` 是偶函数, 那么 :math:`f(-x) = f(x), g(-x) = g(x)`, 记 :math:`h(x) = f(x) \cdot g(x)`, 那么

    .. math::

        h(-x) = f(-x) \cdot g(-x) = f(x) \cdot g(x) = h(x),

    所以 :math:`h(x)` 是偶函数. 若 :math:`f(x), g(x)` 是奇函数, 那么 :math:`f(-x) = -f(x), g(-x) = -g(x)`, 那么

    .. math::

        h(-x) = f(-x) \cdot g(-x) = -f(x) \cdot (-g(x)) = f(x) \cdot g(x) = h(x),

    所以 :math:`h(x)` 是偶函数. 若 :math:`f(x)` 是偶函数, :math:`g(x)` 是奇函数, 那么 :math:`f(-x) = f(x), g(-x) = -g(x)`, 那么

    .. math::

        h(-x) = f(-x) \cdot g(-x) = f(x) \cdot (-g(x)) = -(f(x) \cdot g(x)) = -h(x),

    所以 :math:`h(x)` 是奇函数.

6. 设函数 :math:`f(x)` 在数集 :math:`X` 上有定义, 试证: 函数 :math:`f(x)` 在 :math:`X` 上有界的充分必要条件是它在 :math:`X` 上既有上界又有下界.

.. proof:proof::

    充分性: 若 :math:`f(x)` 在 :math:`X` 上有界, 那么存在 :math:`M > 0`, 使得 :math:`\forall x \in X` 有 :math:`\lvert f(x) \rvert \leqslant M`,
    那么 :math:`f(x)` 在 :math:`X` 上既有上界 :math:`M`, 又有下界 :math:`-M`.

    必要性: 若 :math:`f(x)` 在 :math:`X` 上既有上界 :math:`M`, 又有下界 :math:`m`, 那么 :math:`\forall x \in X` 有
    :math:`\lvert f(x) \rvert \leqslant \max \{ \lvert m \rvert, \lvert M \rvert \}`, 所以 :math:`f(x)` 在 :math:`X` 上有界
    :math:`\max \{ \lvert m \rvert, \lvert M \rvert \}`.

    .. note::

        这题要注意的就是函数“有界”, “有上界”和“有下界”的确切定义, 以及他们之间的细微差别.

§1.2 函数的极限
--------------------------------

1. 若 :math:`\lim\limits_{n \to \infty} u_n = a`, 证明 :math:`\lim\limits_{n \to \infty} \lvert u_n \rvert = \lvert a \rvert`,
并举例说明反之不成立.

.. proof:proof::

    由 :math:`\lim\limits_{n \to \infty} u_n = a` 知 :math:`\forall \varepsilon > 0, \exists N \in \mathbb{N}^+`, 使得 :math:`\forall n > N` 有
    :math:`\lvert u_n - a \rvert < \varepsilon`. 那么对于 :math:`\forall n > N` 有

    .. math::

        \lvert \lvert u_n \rvert - \lvert a \rvert \rvert \leqslant \lvert u_n - a \rvert < \varepsilon

    所以 :math:`\lim\limits_{n \to \infty} \lvert u_n \rvert = \lvert a \rvert`.

    反之, 有反例 :math:`u_n = (-1)^n`, 那么 :math:`\lim\limits_{n \to \infty} \lvert u_n \rvert = 1`, 但是 :math:`\lim\limits_{n \to \infty} u_n` 不存在.

2. 根据函数极限的定义证明

(1). :math:`\lim\limits_{x \to 2} (2x + 5) = 9`;   (2). :math:`\lim\limits_{x \to \infty} \dfrac{1 + x^3}{2x^3} = \dfrac{1}{2}`.

.. proof:proof::

    (1). 对任意给定的 :math:`\varepsilon > 0`, 取 :math:`\delta = \dfrac{\varepsilon}{2}`, 那么对于 :math:`\forall x \in \mathbb{R}`, 有

    .. math::

        \lvert x - 2 \rvert < \delta \Rightarrow \lvert (2x + 5) - 9 \rvert = \lvert 2(x - 2) \rvert = 2 \lvert x - 2 \rvert < 2 \delta = \varepsilon

    所以 :math:`\lim\limits_{x \to 2} (2x + 5) = 9`.

    (2). 对任意给定的 :math:`\varepsilon > 0`, 取 :math:`X = \dfrac{1}{\sqrt[3]{\varepsilon}}`, 那么对于 :math:`\forall x > X`, 有

    .. math::

        \left\lvert \dfrac{1 + x^3}{2x^3} - \dfrac{1}{2} \right\rvert = \dfrac{1}{2} \left\lvert \dfrac{1}{1 + x^3} \right\rvert < \dfrac{1}{2} \cdot \dfrac{1}{x^3} < \dfrac{1}{2} \cdot \dfrac{1}{X^3} = \varepsilon

    所以 :math:`\lim\limits_{x \to \infty} \dfrac{1 + x^3}{2x^3} = \dfrac{1}{2}`.

3. 证明函数 :math:`f(x) = \lvert x \rvert` 当 :math:`x \to 0` 时的极限为 :math:`0`.

.. proof:proof::

    对任意给定的 :math:`\varepsilon > 0`, 取 :math:`\delta = \varepsilon`, 那么对于 :math:`\forall x \in \mathbb{R}`, 有

    .. math::

        \lvert x - 0 \rvert < \delta \Rightarrow \lvert \lvert x \rvert - 0 \rvert = \lvert x \rvert < \delta = \varepsilon

    所以 :math:`\lim\limits_{x \to 0} \lvert x \rvert = 0`.

§1.3 极限的运算法则
--------------------------------

求下列极限

(2). :math:`\lim\limits_{x \to 0} \dfrac{3x^3 - 5x^2 + 2x}{4x^2 + 3x}`; (4). :math:`\lim\limits_{x \to \infty} \dfrac{x^3 - 1}{3x^3 - x^2 - 1}`;

(6). :math:`\lim\limits_{n \to \infty} \dfrac{(n + 1)(n + 2)(2n + 3)}{4n^3}`; (8). :math:`\lim\limits_{n \to \infty} \left( 1 + \dfrac{1}{3} + \dfrac{1}{9} + \cdots + \dfrac{1}{3^n} \right)`;

(10). :math:`\lim\limits_{x \to +\infty} \sqrt{x} \left( \sqrt{a + x} - \sqrt{x} \right)`.

.. proof:solution::

    (2). :math:`\lim\limits_{x \to 0} \dfrac{3x^3 - 5x^2 + 2x}{4x^2 + 3x} = \lim\limits_{x \to 0} \dfrac{x (3x^2 - 5x + 2)}{x (4x + 3)} = \lim\limits_{x \to 0} \dfrac{3x^2 - 5x + 2}{4x + 3} = \dfrac{2}{3}`.

    (4). :math:`\lim\limits_{x \to \infty} \dfrac{x^3 - 1}{3x^3 - x^2 - 1} = \lim\limits_{x \to \infty} \dfrac{1 - \dfrac{1}{x^3}}{3 - \dfrac{1}{x} - \dfrac{1}{x^3}} = \dfrac{1}{3}`.

    (6). :math:`\lim\limits_{n \to \infty} \dfrac{(n + 1)(n + 2)(2n + 3)}{4n^3} = \lim\limits_{n \to \infty} \dfrac{\left(1 + \dfrac{1}{n}\right) \left(1 + \dfrac{2}{n}\right) \left(2 + \dfrac{3}{n}\right)}{4} = \dfrac{1}{2}`.

    (8). :math:`\lim\limits_{n \to \infty} \left( 1 + \dfrac{1}{3} + \dfrac{1}{9} + \cdots + \dfrac{1}{3^n} \right) = \lim\limits_{n \to \infty} \dfrac{1 - \dfrac{1}{3^{n+1}}}{1 - \dfrac{1}{3}} = \dfrac{3}{2}`.

    (10). :math:`\lim\limits_{x \to +\infty} \sqrt{x} \left( \sqrt{a + x} - \sqrt{x} \right) = \lim\limits_{x \to +\infty} \dfrac{a\sqrt{x}}{\sqrt{a + x} + \sqrt{x}} = \lim\limits_{x \to +\infty} \dfrac{a}{\sqrt{\dfrac{a}{x} + 1} + 1} = \dfrac{a}{2}`.

§1.4 极限存在准则与两个重要极限
--------------------------------------------

1. 求下列极限:

.. math::

    \lim\limits_{n \to \infty} \left( \dfrac{1}{\sqrt{n^2 + 1}} + \dfrac{1}{\sqrt{n^2 + 2}} + \cdots + \dfrac{1}{\sqrt{n^2 + n}} \right)

.. proof:solution::

    有如下不等式恒成立:

    .. math::

        \begin{multline*}
        \dfrac{1}{\sqrt{n^2 + n}} + \dfrac{1}{\sqrt{n^2 + n}} + \cdots + \dfrac{1}{\sqrt{n^2 + n}} < \dfrac{1}{\sqrt{n^2 + 1}} + \dfrac{1}{\sqrt{n^2 + 2}} + \cdots + \dfrac{1}{\sqrt{n^2 + n}} \\
        < \dfrac{1}{\sqrt{n^2 + 1}} + \dfrac{1}{\sqrt{n^2 + 1}} + \cdots + \dfrac{1}{\sqrt{n^2 + 1}}.
        \end{multline*}

    又有

    .. math::

        \begin{align*}
        & \lim\limits_{n \to \infty} \dfrac{1}{\sqrt{n^2 + n}} + \dfrac{1}{\sqrt{n^2 + n}} + \cdots + \dfrac{1}{\sqrt{n^2 + n}} = \lim\limits_{n \to \infty} \dfrac{n}{\sqrt{n^2 + n}} = 1, \\
        & \lim\limits_{n \to \infty} \dfrac{1}{\sqrt{n^2 + 1}} + \dfrac{1}{\sqrt{n^2 + 1}} + \cdots + \dfrac{1}{\sqrt{n^2 + 1}} = \lim\limits_{n \to \infty} \dfrac{n}{\sqrt{n^2 + 1}} = 1,
        \end{align*}

    由夹逼准则知

    .. math::

        \lim\limits_{n \to \infty} \left( \dfrac{1}{\sqrt{n^2 + 1}} + \dfrac{1}{\sqrt{n^2 + 2}} + \cdots + \dfrac{1}{\sqrt{n^2 + n}} \right) = 1.

2. 利用两个重要极限计算下列极限:

(1). :math:`\lim\limits_{x \to 0} \dfrac{\tan x - \sin x}{\sin^3 x}`; (2). :math:`\lim\limits_{x \to 1} (1 - x) \tan \dfrac{\pi x}{2}`;

(3). :math:`\lim\limits_{n \to \infty} 2^n \sin \dfrac{\pi}{2^n}`; (4). :math:`\lim\limits_{x \to \infty} \left( 1 - \dfrac{2}{x} \right)^{3x}`.

.. proof:solution::

    (1).

    .. math::

        \begin{align*}
        \lim\limits_{x \to 0} \dfrac{\tan x - \sin x}{\sin^3 x} & = \lim\limits_{x \to 0} \dfrac{\sin x - \cos x \sin x}{\cos x \sin^3 x} = \lim\limits_{x \to 0} \dfrac{1 - \cos x}{\cos x \sin^2 x} = \lim\limits_{x \to 0} \dfrac{2 \sin^2 \dfrac{x}{2}}{\cos x \left(2 \sin \dfrac{x}{2} \cos \dfrac{x}{2}\right)^2} \\
        & = \lim\limits_{x \to 0} \dfrac{1}{2 \cos x \cos^2 \dfrac{x}{2}} = \dfrac{1}{2}
        \end{align*}

    (2). 令 :math:`t = 1 - x`, 那么有

    .. math::

        \begin{align*}
        \lim\limits_{x \to 1} (1 - x) \tan \dfrac{\pi x}{2} & = \lim\limits_{t \to 0} t \tan \dfrac{\pi (1 - t)}{2} = \lim\limits_{t \to 0} t \cot \dfrac{\pi t}{2} = \lim\limits_{t \to 0} \dfrac{t}{\tan \dfrac{\pi t}{2}} \\
        & = \lim\limits_{t \to 0} \dfrac{t}{\dfrac{\sin \dfrac{\pi t}{2}}{\cos \dfrac{\pi t}{2}}} = \dfrac{2}{\pi} \lim\limits_{t \to 0} \cos \dfrac{\pi t}{2} \cdot \dfrac{\dfrac{\pi t}{2}}{\sin \dfrac{\pi t}{2}} = \dfrac{2}{\pi}
        \end{align*}

    (3).

    .. math::

        \lim\limits_{n \to \infty} 2^n \sin \dfrac{\pi}{2^n} = \pi \lim\limits_{n \to \infty} \dfrac{\sin \dfrac{\pi}{2^n}}{\dfrac{\pi}{2^n}} = \pi

    .. note::

        这里用到了如下的结论, 即若 :math:`\lim\limits_{x \to x_0} f(x) = A`, 同时又有数列 :math:`\{x_n\}` 满足 :math:`\lim\limits_{n \to \infty} x_n = x_0`,
        那么 :math:`\lim\limits_{n \to \infty} f(x_n) = A`. 应用到这题, 就是 :math:`f(x) = \sin x, x_0 = 0, x_n = \dfrac{\pi}{2^n}`.

    (4).

    .. math::

        \begin{align*}
        \lim\limits_{x \to \infty} \left( 1 - \dfrac{2}{x} \right)^{3x} & = \lim\limits_{x \to \infty} \left( 1 + \dfrac{-2}{x} \right)^{3x} = \lim\limits_{x \to \infty} \left( 1 + \dfrac{-2}{x} \right)^{\dfrac{x}{-2} \cdot (-6)} \\
        & = \left( \lim\limits_{x \to \infty} \left( 1 + \dfrac{-2}{x} \right)^{\dfrac{x}{-2}} \right)^{-6} = e^{-6}
        \end{align*}

§1.5 无穷小与无穷大
--------------------------------------------

利用等价无穷小计算下列极限:

(1). :math:`\lim\limits_{x \to 0} \dfrac{\sin x^3}{\sin^2 x}`; (2). :math:`\lim\limits_{x \to 0} \dfrac{\tan x - \sin x}{x \sin^2 x}`;

(3). :math:`\lim\limits_{x \to \infty} \dfrac{3x^2 + 8}{5x + 1} \sin \dfrac{1}{x}`; (4). :math:`\lim\limits_{x \to \infty} x \sin \dfrac{2x}{x^2 + 1}`.

.. proof:solution::

    (1). :math:`\lim\limits_{x \to 0} \dfrac{\sin x^3}{\sin^2 x} = \lim\limits_{x \to 0} \dfrac{x^3}{(x)^2} = \lim\limits_{x \to 0} x = 0`

    (2).

    .. math::

        \begin{align*}
        \lim\limits_{x \to 0} \dfrac{\tan x - \sin x}{x \sin^2 x} & = \lim\limits_{x \to 0} \dfrac{\sin x - \cos x \sin x}{x \cos x \sin^2 x} = \lim\limits_{x \to 0} \dfrac{1 - \cos x}{x \cos x \sin x} \\
        & = \dfrac{1}{2} \lim\limits_{x \to 0} \dfrac{2 \sin^2 \dfrac{x}{2}}{\dfrac{x}{2} \cos x \left(2 \sin \dfrac{x}{2} \cos \dfrac{x}{2}\right)} = \dfrac{1}{2} \lim\limits_{x \to 0} \dfrac{1}{\cos x \cos \dfrac{x}{2}} \\
        & = \dfrac{1}{2}
        \end{align*}

    (3). 令 :math:`t = \dfrac{1}{x}`, 那么有

    .. math::

        \begin{align*}
        \lim\limits_{x \to \infty} \dfrac{3x^2 + 8}{5x + 1} \sin \dfrac{1}{x} & = \lim\limits_{t \to 0} \dfrac{3 + 8t^2}{5t + t^2} \sin t = \lim\limits_{t \to 0} \dfrac{3 + 8t^2}{5t + t^2} \cdot t = \lim\limits_{t \to 0} \dfrac{3 + 8t^2}{5 + t} \\
        & = \dfrac{3}{5}
        \end{align*}

    (4). 令 :math:`t = \dfrac{1}{x}`, 那么有

    .. math::

        \begin{align*}
        \lim\limits_{x \to \infty} x \sin \dfrac{2x}{x^2 + 1} & = \lim\limits_{t \to 0} \dfrac{\sin \dfrac{2t}{t^2 + 1}}{t} = \lim\limits_{t \to 0} \dfrac{\dfrac{2t}{t^2 + 1}}{t} = \lim\limits_{t \to 0} \dfrac{2}{t^2 + 1} = 2
        \end{align*}

§1.6 函数的连续性与连续函数的运算
--------------------------------------------

1. 讨论函数 :math:`f(x) = \begin{cases} \dfrac{\sin x}{x}, & x < 0 \\ a, & x = 0 \\ x \sin \dfrac{1}{x} + b, & x > 0 \end{cases}`, 在 :math:`a, b` 为何值时, :math:`f(x)` 在 :math:`x = 0` 处连续.

.. proof:solution::

    函数 :math:`f(x)` 在 :math:`x = 0` 处的左极限为 :math:`\lim\limits_{x \to 0^-} f(x) = \lim\limits_{x \to 0^-} \dfrac{\sin x}{x} = 1`, 右极限为 :math:`\lim\limits_{x \to 0^+} f(x) = \lim\limits_{x \to 0^+} x \sin \dfrac{1}{x} + b = b`. 要使得 :math:`f(x)` 在 :math:`x = 0` 处连续, 那么必须有左右极限相等且等于该点处的函数值, 即

    .. math::

        1 = b = a

2. 求 :math:`f(x) = \dfrac{x}{\tan x}` 的间断点, 并指出间断点的类型.

.. proof:solution::

    由于 :math:`\tan x` 在 :math:`x = \dfrac{\pi}{2} + k \pi, k \in \mathbb{Z}` 无定义, 所以 :math:`f(x)` 在 :math:`x = \dfrac{\pi}{2} + k \pi` 处间断.
    在 :math:`x = \dfrac{\pi}{2} + k \pi` 附近, 有 :math:`\lim\limits_{x \to \dfrac{\pi}{2} + k \pi} f(x) = \lim\limits_{x \to \dfrac{\pi}{2} + k \pi} \dfrac{x}{\tan x} = 0`,
    所以 :math:`f(x)` 在 :math:`x = \dfrac{\pi}{2} + k \pi` 处间断点为第一类可去间断点.

    :math:`\tan x` 在 :math:`x = k \pi, k \in \mathbb{Z}` 处值为0, 所以函数 :math:`f(x) = \dfrac{x}{\tan x}` 在这些点处无定义, 所以 :math:`f(x)` 在 :math:`x = k \pi` 处间断.
    当 :math:`k = 0` 时, :math:`\lim\limits_{x \to 0} f(x) = \lim\limits_{x \to 0} \dfrac{x}{\tan x} = 1`, 所以 :math:`f(x)` 在 :math:`x = 0` 处间断点为第一类可去间断点.
    当 :math:`k \ne 0` 时, :math:`\lim\limits_{x \to k \pi} f(x) = \lim\limits_{x \to k \pi} \dfrac{x}{\tan x} = \infty`,
    所以 :math:`f(x)` 在 :math:`x = k \pi, k \in \mathbb{Z}, k \neq 0` 处间断点为第二类无穷间断点.

3. 求函数 :math:`f(x) = \dfrac{x + 1}{x^2 - x - 2}` 的间断点, 并判断其类型. 如果是可去间断点, 则补充定义或改变函数的定义, 使它连续.

.. proof:solution::

    函数 :math:`f(x) = \dfrac{x + 1}{x^2 - x - 2}` 的分母多项式 :math:`x^2 - x - 2 = (x - 2)(x + 1)` 在 :math:`x = 2, -1` 处为 :math:`0`, 所以 :math:`f(x)` 在这两个点处间断.
    在 :math:`x = 2` 附近, 有

    .. math::

        \lim\limits_{x \to 2} f(x) = \lim\limits_{x \to 2} \dfrac{x + 1}{x^2 - x - 2} = \infty

    所以 :math:`f(x)` 在 :math:`x = 2` 处间断点为第二类无穷间断点. 在 :math:`x = -1` 附近, 有

    .. math::

        \lim\limits_{x \to -1} f(x) = \lim\limits_{x \to -1} \dfrac{x + 1}{x^2 - x - 2} = \lim\limits_{x \to -1} \dfrac{x + 1}{(x - 2)(x + 1)} = \lim\limits_{x \to -1} \dfrac{1}{x - 2} = -\dfrac{1}{3},

    所以 :math:`f(x)` 在 :math:`x = -1` 处间断点为第一类可去间断点, 可以补充定义 :math:`f(-1) = -\dfrac{1}{3}` 使得 :math:`f(x)` 在 :math:`x = -1` 处连续.

§1.7 初等函数的连续性及闭区间上连续函数的性质
------------------------------------------------------------

1. 设 :math:`a > 0, b > 0`, 试证明方程 :math:`x = a \sin x + b` 至少有一个正根, 且不大于 :math:`a + b`.

.. proof:solution::

    考虑函数 :math:`f(x) = x - a \sin x - b`, 那么

    .. math::

        \begin{align*}
        f(0) & = -b < 0, \\
        f(a + b) & = a + b - a \sin (a + b) - b = a \bigl(1 - \sin (a + b)\bigr) \geqslant 0.
        \end{align*}

    所以或者有 :math:`f(a + b) = 0`, :math:`a + b` 是方程 :math:`x = a \sin x + b` 的一个正根；或者有 :math:`f(a + b) > 0`, 那么由零点存在定理知
    :math:`f(x)` 在 :math:`(0, a + b)` 上至少有一个零点. 这两种情况都说明方程 :math:`x = a \sin x + b` 至少有一个正根, 且不大于 :math:`a + b`.

2. 证明: 方程 :math:`x - 2 \sin x = 0` 在 :math:`\left( \dfrac{\pi}{2}, \pi \right)` 内至少有一个根.

.. proof:proof::

    考虑函数 :math:`f(x) = x - 2 \sin x`, 那么

    .. math::

        \begin{align*}
        f\left( \dfrac{\pi}{2} \right) & = \dfrac{\pi}{2} - 2 < 0, \\
        f(\pi) & = \pi - 2 \sin \pi = \pi > 0.
        \end{align*}

    所以由零点存在定理知 :math:`f(x)` 在 :math:`\left( \dfrac{\pi}{2}, \pi \right)` 内至少有一个零点, 即方程 :math:`x - 2 \sin x = 0` 在 :math:`\left( \dfrac{\pi}{2}, \pi \right)` 内至少有一个根.

    .. note::

        由于 :math:`\sin x` 在 :math:`\left[ \dfrac{\pi}{2}, \pi \right]` 上是单调递减的, 所以 :math:`f(x) = x - 2 \sin x` 在 :math:`\left[ \dfrac{\pi}{2}, \pi \right]`
        上是单调递增的, 那么 :math:`f(x)` 在 :math:`\left( \dfrac{\pi}{2}, \pi \right)` 内的零点就是唯一的.

补充内容
=============

§1.2 函数的极限
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

§1.4 极限存在准则与两个重要极限
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

§1.6 函数的连续性与连续函数的运算
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
