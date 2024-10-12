第二章随堂测验
=======================

1. 设函数 :math:`f(x) = \sqrt{x + \sqrt{x + \sqrt{x}}}`, 求它的导函数 :math:`f'(x)`.

2. 设函数 :math:`f(x)` 可微且函数值大于 :math:`0`. 令 :math:`g(x) = \ln f(\sin^2 x)`, 求函数 :math:`g(x)` 的微分.

3. 令 :math:`y(t) = \left( \dfrac{1}{t + 1} \right)^{\frac{1}{t}}`.

   (1). 求 :math:`\lim\limits_{t \to 0} y(t)` 以及 :math:`\lim\limits_{t \to 0} y'(t)`.

   (2). 求极限 :math:`\lim\limits_{x \to \infty} x \left( \dfrac{1}{e} - \left( \dfrac{x}{x + 1} \right)^x \right)`.

   提示: 利用带佩亚诺型余项的麦克劳林公式

   .. math::

        & \dfrac{1}{1 - t} = 1 + t + t^2 + o(t^2), \\
        & \ln (1 + t) = t - \dfrac{t^2}{2} + o(t^2).

4. 设 :math:`0 < a < b`, 证明存在 :math:`\xi \in (a, b)`, 使得

   .. math::

        a e^b - b e^a = (a - b) (1 - \xi)e^\xi.

   提示: 两边同时除以 :math:`ab`, 构造辅助函数, 并在区间 :math:`\left[ \dfrac{1}{b}, \dfrac{1}{a} \right]` 上利用拉格朗日中值定理.

5. 求函数 :math:`y = x^{1/x}, x > 0` 的极大值.
