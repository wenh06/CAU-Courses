第二章随堂测验答案解析
=========================

1. 设函数 :math:`f(x) = \ln(\ln(\ln x))`, 求它的导函数 :math:`f'(x)`.

.. proof:solution::

   由复合函数求导的链式法则知,

   .. math::
      f'(x) = \dfrac{1}{\ln(\ln x)} \cdot \dfrac{1}{\ln x} \cdot \dfrac{1}{x}

2. 设有参数方程 :math:`\begin{cases} x \cos t + x^2 \sin t = 1  \\ y - e^y \sin t = 2 \end{cases}` ,
   求 :math:`\displaystyle \left.\dfrac{dy}{dx}\right|_{t = 0}`.

.. proof:solution::

   对 :math:`x \cos t + x^2 \sin t = 1` 微分得

   .. math::
      \cos t \mathrm{d}x - x \sin t \mathrm{d}t + 2x \sin t \mathrm{d}x + x^2 \cos t \mathrm{d}t = 0,

   从而有

   .. math::
      \dfrac{\mathrm{d}x}{\mathrm{d}t} = \dfrac{x \sin t - x^2 \cos t}{\cos t + 2x \sin t}.

   对 :math:`y - e^y \sin t = 2` 微分得

   .. math::
      \mathrm{d}y - e^y \cos t \mathrm{d}t - e^y \sin t \mathrm{d}y = 0,

   从而有

   .. math::
      \dfrac{\mathrm{d}y}{\mathrm{d}t} = \dfrac{e^y \cos t}{1 - e^y \sin t}.

   那么

   .. math::
      \dfrac{\mathrm{d}y}{\mathrm{d}x} = \dfrac{\mathrm{d}y}{\mathrm{d}t} \left/ \dfrac{\mathrm{d}x}{\mathrm{d}t} \right.
      = \dfrac{e^y \cos t}{1 - e^y \sin t} \left/ \dfrac{x \sin t - x^2 \cos t}{\cos t + 2x \sin t} \right.

   将 :math:`t = 0` 代入参数方程得 :math:`x = 1, y = 2`, 再代入上式得

   .. math::
      \left.\dfrac{dy}{dx}\right|_{t = 0} = \dfrac{e^2}{-1} = -e^2.

3. 设 :math:`f(x) = e^{3x-x^2}`, 请写出 :math:`f(x)` 在 :math:`x = 1` 处带皮亚诺余项的泰勒公式 (展开到 :math:`(x-1)^3` 即可)

.. proof:solution::

   .. math::
      f(x) = & e^{3x-x^2} = e^{2 + (x-1) - (x-1)^2} \\
      = & e^2 \left( 1 + \left[(x-1) - (x-1)^2\right] + \dfrac{\left[(x-1) - (x-1)^2\right]^2}{2!}
          + \dfrac{\left[(x-1) - (x-1)^2\right]^3}{3!} \right) \\
        & + o((x-1)^3) \\
      = & e^2 \left( 1 + (x-1) - \frac{1}{2}(x-1)^2 - \frac{5}{6}(x-1)^3 \right) + o((x-1)^3)

4. 设函数 :math:`f(x)` 是开区间 :math:`I = (a_0, b_0)` 上的函数且处处可导. 设闭区间 :math:`[a, b] \subset I` 包含于该开区间,
   即 :math:`a_0 < a < b < b_0`. 请证明 :math:`f(x)` 的导函数 :math:`f'(x)` (**注意, 导函数未必连续**),
   在闭区间 :math:`[a, b]` 上可取遍 :math:`f'(a)` 与 :math:`f'(b)` 之间的所有值.

.. proof:solution::

   不妨设 :math:`f'(a) < f'(b)`. 任取 :math:`f'(a)` 与 :math:`f'(b)` 之间的实数 :math:`t`, 即 :math:`f'(a) < t < f'(b)`, 令

   .. math::
      g(x) = f(x) - tx,

   那么 :math:`g(x)` 是开区间 :math:`I = (a_0, b_0)` 上处处可导的函数, 且 :math:`g'(x) = f'(x) - t`.

   由闭区间上连续函数 (:math:`g(x)` 可导, 从而连续) 的最大最小值定理知, 存在 :math:`\xi \in [a, b]`, 使得 :math:`g(\xi)` 取到闭区间 :math:`[a, b]` 上的最小值.
   由于 :math:`g'(a) < 0, g'(b) > 0`, 所以 :math:`\xi` 不能是 :math:`a, b` 中任何一个, 由费马引理知, :math:`g'(\xi) = 0`, 即 :math:`f'(\xi) = t`.

   .. note::
      由于 :math:`\displaystyle g'(a) = g'_+(a) = \lim_{x \to a+} \dfrac{g(x) - g(a)}{x - a} < 0`, 由极限的保号性知, 存在足够小的正数 :math:`\delta_1 > 0`,
      使得对任意 :math:`x \in (a, a + \delta_1)` 都有 :math:`g(x) < g(a)`, 所以 :math:`a` 不是最小值点.
      同理, 由于 :math:`\displaystyle g'(b) = g'_-(b) = \lim_{x \to b-} \dfrac{g(x) - g(b)}{x - b} > 0`, 存在足够小的正数 :math:`\delta_2 > 0`,
      使得对任意 :math:`x \in (b - \delta_2, b)` 都有 :math:`g(x) < g(b)`, 所以 :math:`b` 也不是最小值点.

   .. note::
      这题如果假设 :math:`f'(a) > f'(b)`, 则相应地要取 :math:`\xi` 为 :math:`g(x)` 在闭区间 :math:`[a, b]` 上的最大值点.

5. 设 :math:`\displaystyle f(x) = \lvert x + 2 \rvert e^{-\frac{1}{x}}`, 求 :math:`f(x)` 的单调区间, 极值点, 凹凸区间, 拐点, 渐近线.

.. proof:proof::

   :math:`f(x)` 在 :math:`x = -2` 处不可导, 是可能的极值点与拐点.

   :math:`f(x)` 的导函数为

   .. math::
      f'(x) = \begin{cases}
         - \dfrac{x^2 + x + 2}{x^2} e^{-\frac{1}{x}}, & x < -2 \\
         \dfrac{x^2 + x + 2}{x^2} e^{-\frac{1}{x}}, & x > -2 ~ \text{且} ~ x \neq 0
         \end{cases}


   - 当 :math:`x < -2` 时, :math:`f'(x) < 0`, :math:`f(x)` 单调递减;
   - 当 :math:`-2 < x < 0` 时, :math:`f'(x) > 0`, :math:`f(x)` 单调递增;
   - 当 :math:`x > 0` 时, :math:`f'(x) > 0`, :math:`f(x)` 单调递增.

   :math:`f(x)` 在 :math:`x = -2` 处取到极小值 :math:`f(-2) = 0`. 由于 :math:`f(x)` 取值恒非负, 所以 :math:`x = -2` 也是最小值点.

   :math:`f(x)` 的二阶导函数为

   .. math::
      f''(x) = \begin{cases}
         - \dfrac{2 - 3x}{x^4} e^{-\frac{1}{x}}, & x < -2 \\
         \dfrac{2 - 3x}{x^4}  e^{-\frac{1}{x}}, & x > -2 ~ \text{且} ~ x \neq 0
         \end{cases}

   - 当 :math:`x < -2` 时, :math:`f''(x) < 0`, :math:`f(x)` 上凸;
   - 当 :math:`-2 < x < 0` 时, :math:`f''(x) > 0`, :math:`f(x)` 下凸;
   - 当 :math:`0 < x < \dfrac{2}{3}` 时, :math:`f''(x) > 0`, :math:`f(x)` 下凸;
   - 当 :math:`x > \dfrac{2}{3}` 时, :math:`f''(x) < 0`, :math:`f(x)` 上凸.

   :math:`f''(x)` 在其零点 :math:`x = \dfrac{2}{3}` 附近符号变化, 所以 :math:`\left(\dfrac{2}{3}, f\left(\dfrac{2}{3}\right)\right)` 是拐点.
   在 :math:`f''(x)` 不存在的点 :math:`x = -2` 附近, :math:`f''(x)` 符号也发生变化, 所以 :math:`(-2, 0)` 是拐点.

   - 由于 :math:`\displaystyle \lim_{x \to 0-} f(x) = +\infty`, 所以有垂直渐近线 :math:`x = 0`.
   - 由于 :math:`\displaystyle \lim_{x \to +\infty} \dfrac{f(x)}{x} = 1`, 以及 :math:`\displaystyle \lim_{x \to +\infty} (f(x) - x) = 1`, 所以有斜渐近线 :math:`y = x + 1`.
   - 又有 :math:`\displaystyle \lim_{x \to -\infty} f(x) = -1`, 以及 :math:`\displaystyle \lim_{x \to -\infty} (f(x) + x) = -1`, 所以有斜渐近线 :math:`y = -x - 1`.

   .. tikz:: 函数 :math:`\lvert x + 2 \rvert e^{-\frac{1}{x}}` 的图像
      :align: center
      :xscale: 50

      \begin{axis}[samples=500, domain = -10:10, smooth, variable = \x, axis lines=middle, restrict y to domain = -1:21]
      \addplot[very thick, blue] plot ({\x}, {abs(\x + 2) * exp(-1/\x)});
      \end{axis}
