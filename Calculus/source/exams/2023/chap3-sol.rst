第三章随堂测验答案解析
=========================

.. note::

    此次随堂测验未进行。

1. 求不定积分 :math:`\displaystyle \int \dfrac{\arctan x}{x^2 + 1} \mathrm{d} x`.

.. proof:solution::

    .. math::

        \int \dfrac{\arctan x}{x^2 + 1} \mathrm{d} x & = \int \arctan x \mathrm{d} (\arctan x) \\
        & = \dfrac{1}{2} \arctan^2 x + C.

2. 求极限 :math:`\displaystyle \lim\limits_{n \to \infty} \int_0^1 \dfrac{x^n}{1 + \sqrt{x}} \mathrm{d} x`.

.. proof:solution::

    在区间 :math:`[0, 1]` 上有不等式

    .. math::

        0 \leqslant \dfrac{x^n}{1 + \sqrt{x}} \leqslant x^n.

    所以

    .. math::

        0 \leqslant \lim\limits_{n \to \infty} \int_0^1 \dfrac{x^n}{1 + \sqrt{x}} \mathrm{d} x
        & \leqslant \lim\limits_{n \to \infty} \int_0^1 x^n \mathrm{d} x \\
        & = \lim\limits_{n \to \infty} \dfrac{1}{n + 1} \\
        & = 0.

    由夹逼定理知原极限 :math:`\displaystyle \lim\limits_{n \to \infty} \int_0^1 \dfrac{x^n}{1 + \sqrt{x}} \mathrm{d} x = 0`.

3. 求函数 :math:`\displaystyle f(x) = \int_1^{x^3} e^{t^2} \mathrm{d} t` 的导数.

.. proof:solution::

    由导数的定义有

    .. math::

        f'(x) & = \lim\limits_{h \to 0} \dfrac{f(x + h) - f(x)}{h} \\
        & = \lim\limits_{h \to 0} \dfrac{1}{h} \int_1^{(x + h)^3} e^{t^2} \mathrm{d} t - \lim\limits_{h \to 0} \dfrac{1}{h} \int_1^{x^3} e^{t^2} \mathrm{d} t \\
        & = \lim\limits_{h \to 0} \int_{x^3}^{(x + h)^3} e^{t^2} \mathrm{d} t \\

    那么由积分中值定理有

    .. math::

        f'(x) & = \lim\limits_{h \to 0} \int_{x^3}^{(x + h)^3} e^{t^2} \mathrm{d} t \\
        & = \lim\limits_{h \to 0} e^{\xi^2} \int_{x^3}^{(x + h)^3} \mathrm{d} t \\
        & = \lim\limits_{h \to 0} e^{\xi^2} \cdot 3h(x + h)^2 \\
        & = 3x^2 e^{x^6}.

    .. note::

        一般地，如果 :math:`\displaystyle f(x) = \int_{\varphi(x)}^{\psi(x)} g(t) \mathrm{d} t`, 那么

        .. math::

            f'(x) = g(\psi(x)) \psi'(x) - g(\varphi(x)) \varphi'(x).

        可以直接使用这个公式求解上面的题目。

4. 求由曲线 :math:`y = \sqrt{x}` 与 :math:`y = x^2` 所围成的图形的面积.

.. proof:solution::

    解方程 :math:`\sqrt{x} = x^2` 求得曲线 :math:`y = \sqrt{x}` 与 :math:`y = x^2` 的交点为 :math:`(0, 0)` 和 :math:`(1, 1)`.
    那么所求面积为

    .. math::

        S & = \int_0^1 (\sqrt{x} - x^2) \mathrm{d} x \\
        & = \left.\left( \dfrac{2}{3} x^{\frac{3}{2}} - \dfrac{1}{3} x^3 \right) \right|_0^1 \\
        & = \dfrac{2}{3} - \dfrac{1}{3} = \dfrac{1}{3}.

5. 证明 :math:`\displaystyle \int_0^{+\infty} \dfrac{\mathrm{d} x}{(1 + x^2)(1 + x^a)}` 与 :math:`a` 无关.

   提示：先证明积分收敛，然后将积分区域分为 :math:`[0, 1]` 和 :math:`[1, +\infty)` 两部分.

.. proof:proof::

    由于

    .. math::

        0 \leqslant \dfrac{1}{(1 + x^2)(1 + x^a)} \leqslant \dfrac{1}{1 + x^2},

    而 :math:`\displaystyle \int_0^{+\infty} \dfrac{\mathrm{d} x}{1 + x^2} = \dfrac{\pi}{2}` 收敛, 由比较判别法知原积分收敛。那么有

    .. math::

        \int_0^{+\infty} \dfrac{\mathrm{d} x}{(1 + x^2)(1 + x^a)}
        & = \int_0^1 \dfrac{\mathrm{d} x}{(1 + x^2)(1 + x^a)} + \int_1^{+\infty} \dfrac{\mathrm{d} x}{(1 + x^2)(1 + x^a)} \\
        & = \int_{+\infty}^1 \dfrac{\mathrm{d} \frac{1}{x}}{(1 + \frac{1}{x^2})(1 + \frac{1}{x^a})} + \int_1^{+\infty} \dfrac{\mathrm{d} x}{(1 + x^2)(1 + x^a)} \\
        & = -\int_1^{+\infty} \dfrac{\mathrm{d} \frac{1}{x}}{(1 + \frac{1}{x^2})(1 + \frac{1}{x^a})} + \int_1^{+\infty} \dfrac{\mathrm{d} x}{(1 + x^2)(1 + x^a)} \\
        & = \int_1^{+\infty} \dfrac{x^a \mathrm{d} x}{(1 + x^2)(1 + x^a)} + \int_1^{+\infty} \dfrac{\mathrm{d} x}{(1 + x^2)(1 + x^a)} \\
        & = \int_1^{+\infty} \dfrac{(1 + x^a) \mathrm{d} x}{(1 + x^2)(1 + x^a)} \\
        & = \int_1^{+\infty} \dfrac{\mathrm{d} x}{1 + x^2} \\
        & = \dfrac{\pi}{2} - \arctan 1 \\
        & = \dfrac{\pi}{4}.

    以上值与 :math:`a` 无关.
