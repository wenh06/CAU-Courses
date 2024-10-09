第一章随堂测验答案解析
=========================

1. 求极限 :math:`\lim\limits_{x \to 0} x \left[ \dfrac{1}{x} \right]`, 其中取整函数的定义为

   .. math::

        [x] = \max \{ n \in \mathbb{Z} | n \leqslant x \} = n \text{ 若 } n \leqslant x < n + 1, n \in \mathbb{Z}

.. proof:solution::

    由取整函数的定义知有不等式

    .. math::

        \dfrac{1}{x} - 1 < \left[ \dfrac{1}{x} \right] \leqslant \dfrac{1}{x},

    从而有

    .. math::

        1 - x < x \left[ \dfrac{1}{x} \right] \leqslant 1.

    由夹逼定理知 :math:`\lim\limits_{x \to 0} x \left[ \dfrac{1}{x} \right] = 1`.

2. 求极限 :math:`\lim\limits_{x \to 1} x^{\frac{1}{1 - x}}`

.. proof:solution::

    令 :math:`t = 1 - x`, 则 :math:`x = 1 - t`, 那么有

    .. math::

        \lim\limits_{x \to 1} x^{\frac{1}{1 - x}} = \lim\limits_{t \to 0} (1 - t)^{\frac{1}{t}}
        = \lim\limits_{t \to 0} \left( (1 - t)^{\frac{1}{t}} \right)^{-1}
        = \dfrac{1}{e}.

3. 设 :math:`n \in \mathbb{N}` 为正整数。当 :math:`x \to 0` 时， :math:`(1 - \cos x) \cdot \ln (1 + x^2)` 是比 :math:`x \cdot \tan x^n` 高阶的无穷小，
   而 :math:`x \cdot \arcsin^n x` 是比 :math:`e^{x^2} - 1` 高阶的无穷小。求正整数 :math:`n` 的值。

.. proof:proof::

    有如下的等价无穷小关系

    .. math::

        (1 - \cos x) \cdot \ln (1 + x^2) \sim \dfrac{x^2}{2} \cdot x^2 = \dfrac{x^4}{2}, \\
        x \cdot \tan x^n \sim x \cdot x^n = x^{n+1}, \\
        x \cdot \arcsin^n x \sim x \cdot x^n = x^{n+1}, \\
        e^{x^2} - 1 \sim x^2.

    于是有 :math:`n + 1 < 4`, 以及 :math:`n + 1 > 2`, 即 :math:`2 < n + 1 < 4`, 从而 :math:`n = 2`.

4. 函数 :math:`f(x) = \dfrac{(e^x - e^2) \cos \frac{\pi x}{2}}{\lvert x - 1 \rvert (x - 2)}` 在 :math:`\mathbb{R}` 上是否有间断点？
   若有，列出所有间断点，并判断其类型。若无，请证明之。

.. proof:solution::

    函数 :math:`f(x)` 在 :math:`x = 1, 2` 处无定义，所以 :math:`x = 1, 2` 是函数 :math:`f(x)` 的间断点。

    :math:`x = 1` 处的左极限为

    .. math::

        \lim\limits_{x \to 1^-} f(x)
        = \lim\limits_{x \to 1^-} \dfrac{(e^x - e^2) \cos \frac{\pi x}{2}}{(1 - x) (x - 2)}
        = \lim\limits_{x \to 1^-} \dfrac{(e^x - e^2) \sin \frac{\pi (x - 1)}{2}}{(x - 1) (x - 2)} = \dfrac{(e^2 - e) \pi}{2}.

    :math:`x = 1` 处的右极限为

    .. math::

        \lim\limits_{x \to 1^+} f(x)
        = \lim\limits_{x \to 1^+} \dfrac{(e^x - e^2) \cos \frac{\pi x}{2}}{(x - 1) (x - 2)}
        = -\dfrac{(e^2 - e) \pi}{2}.

    由于左右极限都存在但不相等，所以 :math:`x = 1` 是函数 :math:`f(x)` 的第一类跳跃间断点。

    :math:`x = 2` 处的有极限为

    .. math::

        \lim\limits_{x \to 2} f(x)
        = \lim\limits_{x \to 2} \dfrac{(e^x - e^2) \cos \frac{\pi x}{2}}{\lvert x - 1 \rvert (x - 2)}
        = \lim\limits_{x \to 2} \dfrac{e^2(e^{x - 2} - 1) \cos \frac{\pi x}{2}}{\lvert x - 1 \rvert (x - 2)}
        = e^2 \cos \pi = -e^2.

    于是 :math:`x = 2` 是函数 :math:`f(x)` 的第一类可去间断点。

5. 设函数 :math:`f(x)` 在闭区间 :math:`[a, a + 2b]` 上连续，:math:`b > 0`. 证明：存在 :math:`\xi \in [a, a + b]` 使得

   .. math::

        f(\xi + b) - f(\xi) = \frac{1}{2} \left[ f(a + 2b) - f(a) \right]

.. proof:solution::

    令 :math:`F(x) = f(x + b) - f(x) - \dfrac{1}{2} \left[ f(a + 2b) - f(a) \right]`. 则 :math:`F(x)` 在闭区间 :math:`[a, a + b]` 上连续，且有

    .. math::

        F(a) & = f(a + b) - f(a) - \dfrac{1}{2} \left[ f(a + 2b) - f(a) \right] = f(a + b) - \dfrac{1}{2} \left[ f(a + 2b) + f(a) \right] \\
        F(a + b) & = f(a + 2b) - f(a + b) - \dfrac{1}{2} \left[ f(a + 2b) - f(a) \right] = -f(a + b) + \dfrac{1}{2} \left[ f(a + 2b) + f(a) \right]

    从而有 :math:`F(a) = -F(a + b)`. 若 :math:`F(a) = F(a + b) = 0`，则取 :math:`\xi = a` 或 :math:`\xi = a + b` 即可。
    否则 :math:`F(a), F(a + b)` 异号，由闭区间上连续函数的零点存在定理知，存在 :math:`\xi \in [a, a + b]` 使得 :math:`F(\xi) = 0`，即
    :math:`f(\xi + b) - f(\xi) = \dfrac{1}{2} \left[ f(a + 2b) - f(a) \right]`。
