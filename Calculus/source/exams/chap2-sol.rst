第二章随堂测验答案解析
=========================

1. 设函数 :math:`f(x) = \sqrt{x + \sqrt{x + \sqrt{x}}}`, 求它的导函数 :math:`f'(x)`.

.. proof:solution::

    由复合函数求导的链式法则可得

    .. math::

        f'(x) = \dfrac{1}{2\sqrt{x + \sqrt{x + \sqrt{x}}}} \cdot \left(1 + \dfrac{1}{2\sqrt{x + \sqrt{x}}}\right) \cdot \left(1 + \dfrac{1}{2\sqrt{x}}\right)

2. 设函数 :math:`f(x)` 可微且函数值大于 :math:`0`. 令 :math:`g(x) = \ln f(\sin^2 x)`, 求函数 :math:`g(x)` 的微分.

.. proof:solution::

    .. math::

        \mathrm{d} y & = \mathrm{d} (\ln f(\sin^2 x)) \\
        & = \dfrac{1}{f(\sin^2 x)} \cdot f'(\sin^2 x) \cdot 2\sin x \cos x \cdot \mathrm{d} x \\
        & = \dfrac{\sin 2x}{f(\sin^2 x)} \cdot f'(\sin^2 x) \cdot \mathrm{d} x

3. 令 :math:`y(t) = \left( \dfrac{1}{t + 1} \right)^{\frac{1}{t}}`.

(1). 求 :math:`\lim\limits_{t \to 0} y(t)` 以及 :math:`\lim\limits_{t \to 0} y'(t)`.

(2). 求极限 :math:`\lim\limits_{x \to \infty} x \left( \dfrac{1}{e} - \left( \dfrac{x}{x + 1} \right)^x \right)`.

提示：利用带佩亚诺型余项的麦克劳林公式

.. math::

    & \dfrac{1}{1 - t} = 1 + t + t^2 + o(t^2), \\
    & \ln (1 + t) = t - \dfrac{t^2}{2} + o(t^2).

.. proof:solution::

    (1). :math:`\lim\limits_{t \to 0} y(t) = \lim\limits_{t \to 0} \dfrac{1}{(t + 1)^{\frac{1}{t}}} = \dfrac{1}{e}`.

    对 :math:`\ln y(t) = - \dfrac{\ln (t + 1)}{t}` 两边求导可得

    .. math::

        \dfrac{y'(t)}{y(t)} = - \dfrac{\dfrac{t}{t + 1} - \ln (t + 1)}{t^2}.

    利用带佩亚诺型余项的麦克劳林公式

    .. math::

        & \dfrac{1}{1 - t} = 1 + t + t^2 + o(t^2), \\
        & \ln (1 + t) = t - \dfrac{t^2}{2} + o(t^2),

    可得

    .. math::

        \dfrac{y'(t)}{y(t)} & = - \dfrac{\dfrac{t}{t + 1} - \ln (t + 1)}{t^2} \\
        & = - \dfrac{t(1 - t + o(t)) - (t - \dfrac{t^2}{2} + o(t^2))}{t^2} \\
        & = \dfrac{1}{2} + o(1).

    于是， :math:`\lim\limits_{t \to 0} \dfrac{y'(t)}{y(t)} = \dfrac{1}{2}`, 从而有 :math:`\lim\limits_{t \to 0} y'(t) = \dfrac{1}{2e}`.

    (2). 由于

    .. math::

        \lim\limits_{x \to \infty} \left( \dfrac{x}{x + 1} \right)^x = \lim\limits_{x \to \infty} \dfrac{1}{\left( 1 + \dfrac{1}{x} \right)^x} = \dfrac{1}{e},

    所以这是一个 :math:`\infty \cdot 0` 型的不定式. 令 :math:`t = \dfrac{1}{x}`, 则

    .. math::

        \lim\limits_{x \to \infty} x \left( \dfrac{1}{e} - \left( \dfrac{x}{x + 1} \right)^x \right) = \lim\limits_{t \to 0} \dfrac{\dfrac{1}{e} - \left( \dfrac{1}{1 + t} \right)^{\frac{1}{t}}}{t} = \lim\limits_{t \to 0} \dfrac{\dfrac{1}{e} - y(t)}{t}

    化为了 :math:`\dfrac{0}{0}` 型的不定式。对上式利用洛必达法则可得

    .. math::

        \lim\limits_{t \to 0} \dfrac{\dfrac{1}{e} - y(t)}{t} = \lim\limits_{t \to 0} \dfrac{- y'(t)}{1} = - \dfrac{1}{2e}.

    因此， :math:`\lim\limits_{x \to \infty} x \left( \dfrac{1}{e} - \left( \dfrac{x}{x + 1} \right)^x \right) = - \dfrac{1}{2e}`.

4. 设 :math:`0 < a < b`, 证明存在 :math:`\xi \in (a, b)`, 使得

.. math::

    a e^b - b e^a = (a - b) (1 - \xi)e^\xi.

提示：两边同时除以 :math:`ab`, 构造辅助函数，并在区间 :math:`\left[ \dfrac{1}{b}, \dfrac{1}{a} \right]` 上利用拉格朗日中值定理.

.. proof:solution::

    对 :math:`a e^b - b e^a = (a - b) (1 - \xi)e^\xi` 两边同时除以 :math:`ab` 可得

    .. math::

        \dfrac{e^b}{b} - \dfrac{e^a}{a} = \left(\dfrac{1}{a} - \dfrac{1}{b}\right) \left( 1 - \xi \right) e^\xi.

    考虑函数 :math:`f(x) = x e^{\frac{1}{x}}`, 则 :math:`f'(x) = e^{\frac{1}{x}} \left(1 - \dfrac{1}{x}\right)`, 由拉格朗日中值定理可得，
    存在 :math:`\tau \in \left( \dfrac{1}{b}, \dfrac{1}{a} \right)`, 使得

    .. math::

        f(\dfrac{1}{b}) - f(\dfrac{1}{a}) = f'(\tau) \left(\dfrac{1}{b} - \dfrac{1}{a}\right).

    令 :math:`\xi = \dfrac{1}{\tau}`, 则 :math:`\xi \in (a, b)`, 且

    .. math::

        \dfrac{e^b}{b} - \dfrac{e^a}{a} = \left(\dfrac{1}{a} - \dfrac{1}{b}\right) \left(1 - \dfrac{1}{\tau}\right) e^{\frac{1}{\tau}} = \left(\dfrac{1}{a} - \dfrac{1}{b}\right) \left( 1 - \xi \right) e^\xi.

    上式两边同时乘以 :math:`ab` 即可得到题目要证明的结论：

    .. math::

        a e^b - b e^a = (a - b) (1 - \xi)e^\xi.

5. 求函数 :math:`y = x^{1/x}, x > 0` 的极大值.

.. proof:solution::

    对 :math:`y = x^{1/x}, x > 0` 两边同时取对数可得

    .. math::

        \ln y = \dfrac{\ln x}{x}.

    令 :math:`f(x) = \dfrac{\ln x}{x}`, 则 :math:`f'(x) = \dfrac{1 - \ln x}{x^2}`, 由 :math:`f'(x) = 0` 可得 :math:`x = e`, 由于

    .. math::

        f''(x) = \dfrac{2 \ln x - 3}{x^3},

    所以 :math:`x = e` 是极大值点. 由于 :math:`f(1) = 0`, :math:`f(e) = \dfrac{1}{e}`, 所以 :math:`x = e` 是极大值点，
    且 :math:`y = e^{1 / e}` 是极大值.

    .. note::

        函数 :math:`y = x^{1/x}, x > 0` 的图像如下图所示

        .. tikz:: 函数 :math:`y = x^{1/x}, x > 0` 的图像
            :align: center
            :xscale: 60

            \draw[->] (-0.3, 0) -- (5, 0) node[right] {$x$};
            \draw[->] (0, -0.3) -- (0, 2) node[above] {$y$};
            \draw[domain=0.01:4.7, smooth, variable=\x, blue] plot ({\x}, {exp(ln(\x)/\x)});
