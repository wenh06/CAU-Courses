第一章随堂测验答案解析
=========================

1. 问函数 :math:`f(x) = x \cos x` 是否是周期函数，如果是，给出它的一个周期；如果不是，说明理由。

.. proof:solution::

    函数 :math:`f(x) = x \cos x` 不是周期函数。

    假设 :math:`f(x)` 是周期函数，那么存在正数 :math:`T > 0` 使得 :math:`f(x + T) = f(x)` 对所有 :math:`x` 成立。
    那么对于 :math:`x = 0`, 有 :math:`f(T) = f(0) = 0`, 即 :math:`T \cos T = 0`, 由于 :math:`T > 0`, 所以 :math:`\cos T = 0`,
    那么必须有 :math:`T = \dfrac{\pi}{2} + k \pi, k \in \mathbb{N}`. 将 :math:`T` 的表达式代入 :math:`f(x) = f(x + T)` 中，得到

    .. math::

        x \cos x = (x + \dfrac{\pi}{2} + k \pi) \cos (x + \dfrac{\pi}{2} + k \pi) = \pm (x + \dfrac{\pi}{2} + k \pi) \sin x

    上式显然不是对所有 :math:`x` 成立，例如 :math:`x = -\dfrac{\pi}{2} + t \pi, t \in \mathbb{N}` 时，上式左边为 :math:`0`,
    而上式右边为 :math:`\pm (t + k) \pi \sin \dfrac{\pi}{2} = \pm (t + k) \pi`, 这两边不相等，所以假设不成立，函数 :math:`f(x) = x \cos x` 不是周期函数。

2. 求函数极限 :math:`\lim\limits_{x \to 0} \dfrac{\sqrt{1 + x} - \sqrt{1 - x}}{x}`.

.. proof:solution::

    .. math::

        \lim\limits_{x \to 0} \dfrac{\sqrt{1 + x} - \sqrt{1 - x}}{x} & = \lim\limits_{x \to 0} \dfrac{\sqrt{1 + x} - \sqrt{1 - x}}{x} \cdot \dfrac{\sqrt{1 + x} + \sqrt{1 - x}}{\sqrt{1 + x} + \sqrt{1 - x}} \\
        & = \lim\limits_{x \to 0} \dfrac{1 + x - (1 - x)}{x \left( \sqrt{1 + x} + \sqrt{1 - x} \right)} \\
        & = \lim\limits_{x \to 0} \dfrac{2x}{x \left( \sqrt{1 + x} + \sqrt{1 - x} \right)} \\
        & = \lim\limits_{x \to 0} \dfrac{2}{\sqrt{1 + x} + \sqrt{1 - x}} = 1

3. 设数列 :math:`\{a_n\}_{n\in\mathbb{N}}` 满足： :math:`0 < a_1 < \pi, a_{n+1} = \sin a_n (n = 1, 2, \ldots)`, 求证数列极限 :math:`\lim\limits_{n \to \infty} a_n` 存在。

.. proof:proof::

    由于 :math:`0 < a_1 < \pi`, 所以 :math:`0 < \sin a_1 < 1`. 由于 :math:`\sin x` 在 :math:`[0, 1] \subset [0, \frac{\pi}{2}]` 上是单调递增的，
    所以 :math:`0 = \sin 0 < a_2 = \sin a_1 < 1 = \sin \frac{\pi}{2}`. 那么容易由数学归纳法知 :math:`0 < a_n < 1` 对所有 :math:`n \geqslant 2` 成立。

    由于在区间 :math:`(0, 1) \subset (0, \frac{\pi}{2})` 上，有 :math:`\sin x < x`, 所以对于任意的 :math:`n \in \mathbb{N}^+`, 有 :math:`0 < a_{n+1} = \sin a_n < a_n`.
    那么由单调有界原理知数列 :math:`\{a_n\}_{n\in\mathbb{N}}` 收敛，即极限 :math:`\lim\limits_{n \to \infty} a_n` 存在。

    .. note::

        我们可以进一步求出这个极限的值（将其记为 :math:`a \in [0, 1]`）：在 :math:`a_{n+1} = \sin a_n` 两边同时对 :math:`n` 取极限，
        得到 :math:`\lim\limits_{n \to \infty} a_{n+1} = \lim\limits_{n \to \infty} \sin a_n`,
        即有 :math:`a = \sin a`, 于是必须有 :math:`a = 0`.

4. 设 :math:`n \in \mathbb{N}` 为正整数。当 :math:`x \to 0` 时， :math:`(1 - \cos x) \cdot \ln (1 + x^2)` 是比 :math:`x \sin x^n` 高阶的无穷小，
而 :math:`x \sin x^n` 是比 :math:`e^{x^2} - 1` 高阶的无穷小。求正整数 :math:`n` 的值。

.. proof:solution::

    当 :math:`x \to 0` 时， :math:`(1 - \cos x) \cdot \ln (1 + x^2)` 是比 :math:`x \sin x^n` 高阶的无穷小，这说明

    .. math::

        \lim\limits_{x \to 0} \dfrac{(1 - \cos x) \cdot \ln (1 + x^2)}{x \sin x^n} = 0

    :math:`(1 - \cos x)` 的等价无穷小是 :math:`\dfrac{x^2}{2}`, :math:`\ln (1 + x^2)` 的等价无穷小是 :math:`x^2`, :math:`\sin x^n` 的等价无穷小是 :math:`x^n`,
    上式可以改写为

    .. math::

        \lim\limits_{x \to 0} \dfrac{\dfrac{x^2}{2} \cdot x^2}{x \cdot x^n} = \lim\limits_{x \to 0} \dfrac{x^{3-n}}{2} = 0

    于是有 :math:`3 - n > 0`, 即 :math:`n < 3`.

    另一方面，有当 :math:`x \to 0` 时， :math:`x \sin x^n` 是比 :math:`e^{x^2} - 1` 高阶的无穷小，即

    .. math::

        \lim\limits_{x \to 0} \dfrac{x \sin x^n}{e^{x^2} - 1} = 0

    :math:`e^{x^2} - 1` 的等价无穷小是 :math:`x^2`, 上式可以改写为

    .. math::

        \lim\limits_{x \to 0} \dfrac{x \cdot x^n}{x^2} = \lim\limits_{x \to 0} x^{n-1} = 0

    于是有 :math:`n - 1 > 0`, 即 :math:`n > 1`.

    综上有 :math:`1 < n < 3`, 由于 :math:`n` 是正整数，所以 :math:`n = 2`.

5. 函数 :math:`f(x) = \dfrac{(x - 1) \sin(x - 2)}{ x \lvert x - 1 \rvert (x - 2)}` 都有哪些间断点？这些间断点的类型分别是什么？

.. proof:solution::

    函数 :math:`f(x)` 的分母的零点为 :math:`x = 0, 1, 2`, 所以 :math:`f(x)` 在这三个点处间断。

    在 :math:`x = 0` 处，函数 :math:`f(x)` 的分子 :math:`(x - 1) \sin(x - 2)` 取值为 :math:`\sin 2 \neq 0`, 所以 :math:`f(x)` 在 :math:`x = 0` 处有
    :math:`\lim\limits_{x \to 0} f(x) = \infty`, 间断点为第二类无穷间断点。

    在 :math:`x = 1` 处，函数 :math:`f(x)` 的分子 :math:`(x - 1) \sin(x - 2)` 取值为 :math:`0`, 所以需要进一步考察 :math:`f(x)` 在 :math:`x = 1` 处的左右极限：

    .. math::

        \lim\limits_{x \to 1^-} f(x) & = \lim\limits_{x \to 1^-} \dfrac{(x - 1) \sin(x - 2)}{ x \lvert x - 1 \rvert (x - 2)} = \lim\limits_{x \to 1^-} \dfrac{-\sin(x - 2)}{ x (x - 2)} = -\sin 1 \\
        \lim\limits_{x \to 1^+} f(x) & = \lim\limits_{x \to 1^+} \dfrac{(x - 1) \sin(x - 2)}{ x \lvert x - 1 \rvert (x - 2)} = \lim\limits_{x \to 1^+} \dfrac{\sin(x - 2)}{ x (x - 2)} = \sin 1

    左右极限存在但不相等，所以 :math:`f(x)` 在 :math:`x = 1` 处间断点为第一类跳跃间断点。

    在 :math:`x = 2` 处，函数 :math:`f(x)` 的分子 :math:`(x - 1) \sin(x - 2)` 取值为 :math:`0`, 所以需要进一步考察 :math:`f(x)` 在 :math:`x = 2` 处的左右极限：

    .. math::

        \lim\limits_{x \to 2} f(x) = \lim\limits_{x \to 2} \dfrac{(x - 1) \sin(x - 2)}{ x \lvert x - 1 \rvert (x - 2)} = \lim\limits_{x \to 2} \dfrac{(x - 1)}{ x \lvert x - 1 \rvert} = \dfrac{1}{2}

    左右极限存在且相等，所以 :math:`f(x)` 在 :math:`x = 2` 处间断点为第一类可去间断点。
