第 1-4 章随堂测验答案解析
=========================

1. 设函数 :math:`f(x) = \ln(\sqrt{x^2 + 1} + x)`, 求它的导函数 :math:`f'(x)`.

.. proof:solution::

   由复合函数求导的链式法则可得

   .. math::
      f'(x) = \dfrac{1}{\sqrt{x^2 + 1} + x} \cdot \left( \dfrac{x}{\sqrt{x^2 + 1}} + 1 \right)

   化简得

   .. math::
      f'(x) = \dfrac{1}{\sqrt{x^2 + 1}}

2. 设函数 :math:`y = y(x)` 由方程 :math:`e^{x+y} - xy = 1` 确定, 求 :math:`\dfrac{dy}{dx}` 在点 :math:`(0,0)` 处的值.

.. proof:solution::

   对方程两边关于 :math:`x` 求导，得

   .. math::
      e^{x+y} \cdot \left(1 + \dfrac{dy}{dx}\right) - \left(y + x\dfrac{dy}{dx}\right) = 0

   代入点 :math:`(0,0)`，得

   .. math::
      e^0 \cdot \left(1 + \dfrac{dy}{dx}\right) - (0 + 0) = 0

   解得

   .. math::
      \left. \dfrac{dy}{dx} \right|_{(0,0)} = -1

3. 设 :math:`f(x) = \arctan x`, 请写出 :math:`f(x)` 在 :math:`x = 0` 处带皮亚诺余项的泰勒公式（展开到 :math:`x^3` 项）.

.. proof:solution::

   计算各阶导数：

   .. math::
      f(x) &= \arctan x, & f(0) &= 0 \\
      f'(x) &= \dfrac{1}{1+x^2}, & f'(0) &= 1 \\
      f''(x) &= -\dfrac{2x}{(1+x^2)^2}, & f''(0) &= 0 \\
      f'''(x) &= \dfrac{6x^2-2}{(1+x^2)^3}, & f'''(0) &= -2

   因此泰勒公式为

   .. math::
      \arctan x = x - \dfrac{1}{3}x^3 + o(x^3)

4. 设函数 :math:`f(x)` 在闭区间 :math:`[a, b]` 上连续, 在开区间 :math:`(a, b)` 内可导, 且 :math:`f(a) = f(b) = 0`.
   证明存在 :math:`\xi \in (a, b)` 使得 :math:`f'(\xi) + f(\xi) = 0`.

.. proof:proof::

   构造辅助函数 :math:`F(x) = e^x f(x)`

   由于 :math:`f(x)` 在 :math:`[a, b]` 上连续，在 :math:`(a, b)` 内可导，且指数函数处处连续可导，
   故 :math:`F(x)` 在 :math:`[a, b]` 上连续，在 :math:`(a, b)` 内可导

   计算端点值：

   .. math::
      F(a) = e^a f(a) = 0, \quad F(b) = e^b f(b) = 0

   由罗尔定理，存在 :math:`\xi \in (a, b)`，使得 :math:`F'(\xi) = 0`

   计算导数：

   .. math::
      F'(x) = e^x f(x) + e^x f'(x) = e^x [f(x) + f'(x)]

   因此

   .. math::
      F'(\xi) = e^\xi [f(\xi) + f'(\xi)] = 0

   由于 :math:`e^\xi \neq 0`，故

   .. math::
      f'(\xi) + f(\xi) = 0

5. 设函数 :math:`f(x) = x e^{-x}`, 求 :math:`f(x)` 的单调区间, 极值点, 凹凸区间, 拐点及渐近线.

.. proof:solution::

   **单调区间与极值点：**

   求一阶导数：

   .. math::
      f'(x) = e^{-x} - x e^{-x} = (1-x)e^{-x}

   令 :math:`f'(x) = 0`，得 :math:`x = 1`

   - 当 :math:`x < 1` 时，:math:`f'(x) > 0`，函数单调递增
   - 当 :math:`x > 1` 时，:math:`f'(x) < 0`，函数单调递减
   - :math:`x = 1` 是极大值点，极大值为 :math:`f(1) = e^{-1} = \dfrac{1}{e}`

   **凹凸区间与拐点：**

   求二阶导数：

   .. math::
      f''(x) = -e^{-x} - (1-x)e^{-x} = (x-2)e^{-x}

   令 :math:`f''(x) = 0`，得 :math:`x = 2`

   - 当 :math:`x < 2` 时，:math:`f''(x) < 0`，函数凸 (下凸)
   - 当 :math:`x > 2` 时，:math:`f''(x) > 0`，函数凹 (上凸)
   - :math:`x = 2` 是拐点，拐点坐标为 :math:`(2, 2e^{-2})`

   **渐近线：**

   - 水平渐近线：:math:`\lim\limits_{x \to +\infty} x e^{-x} = 0`，故有水平渐近线 :math:`y = 0`
   - 垂直渐近线：无
   - 斜渐近线：无
