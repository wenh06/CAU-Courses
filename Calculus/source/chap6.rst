第六章  定积分及其应用
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. contents:: :local:


.. _ex-chap6:

课后习题解答
====================================

.. _ex-chap6-sec1:

§6.1 定积分的概念
------------------------------------

.. _ex-chap6-sec2:

§6.2 定积分的性质
------------------------------------

.. _ex-chap6-sec2-ex7:

7. 已知函数 :math:`f(x)` 在区间 :math:`[0,1]` 上具有 2 阶导数, 且 :math:`f(0) = 0`, :math:`f(1) = 1`,
   :math:`\displaystyle \int_0^1 f(x) ~ \mathrm{d}x = 1`, 试证明:
   (1) 存在 :math:`\xi \in (0, 1)`, 使得 :math:`f'(\xi) = 0`;
   (2) 存在 :math:`\eta \in (0, 1)`, 使得 :math:`f''(\eta) < -2`.

.. proof:solution::

   (1) 由积分中值定理, 存在 :math:`x_0 \in (0, 1)`, 使得

   .. math::
      1 = \int_0^1 f(x) ~ \mathrm{d}x = f(x_0) (1 - 0) = f(x_0).

   又由于 :math:`f(1) = 1`, 由罗尔定理, 存在 :math:`\xi \in (x_0, 1) \subset (0, 1)`, 使得 :math:`f'(\xi) = 0`.

   (2) 令 :math:`g(x) = f(x) + x^2`, 希望证明 :math:`g''(x) = f''(x) + 2 < 0` 在某点成立.

   若能证明存在 :math:`x_1 < x_2 \in (0, 1)`, 使得 :math:`g'(x_1) > g'(x_2)`, 则由拉格朗日中值定理,
   存在 :math:`\eta \in (x_1, x_2) \subset (0, 1)`, 使得 :math:`g''(\eta) < 0`, 即 :math:`f''(\eta) < -2`.

   下证存在这样的 :math:`x_1, x_2`. 对 (1) 中的 :math:`x_0`, 在区间 :math:`[0, x_0]` 以及 :math:`[x_0, 1]` 上分别应用拉格朗日中值定理,
   则存在 :math:`x_1 \in (0, x_0)`, :math:`x_2 \in (x_0, 1)`, 使得

   .. math::
      g'(x_1) & = \frac{g(x_0) - g(0)}{x_0 - 0} = \frac{f(x_0) + x_0^2}{x_0} = \frac{1}{x_0} + x_0, \\
      g'(x_2) & = \frac{g(1) - g(x_0)}{1 - x_0} = \frac{2 - (f(x_0) + x_0^2)}{1 - x_0} = \frac{1 - x_0^2}{1 - x_0} = 1 + x_0.

   因为 :math:`0 < x_0 < 1`, 所以 :math:`\dfrac{1}{x_0} + x_0 > 1 + x_0`, 即 :math:`g'(x_1) > g'(x_2)`, 证毕.

.. _ex-chap6-sec3:

§6.3 微积分基本定理
------------------------------------

.. _ex-chap6-sec4:

§6.4 定积分的换元法和分部积分法
------------------------------------

.. _ex-chap6-sec5:

§6.5 广义积分
------------------------------------

.. _ex-chap6-sec6:

§6.6 定积分的几何应用
------------------------------------

.. _extra-chap6:

补充内容
====================================

.. _extra-chap6-topic1:

1. 求定积分 :math:`\displaystyle \int_{-1}^1 \dfrac{e^x + e^{-x}}{1 + 3^x} \mathrm{d}x`.

.. proof:solution::

   .. math::
      \int_{-1}^1 \dfrac{e^x + e^{-x}}{1 + 3^x} \mathrm{d}x & = \left(\int_{-1}^0 + \int_0^1 \right) \dfrac{e^x + e^{-x}}{1 + 3^x} \mathrm{d}x \\
      & = \int_{1}^0 \dfrac{e^{-x} + e^{x}}{1 + 3^{-x}} \mathrm{d}(-x) + \int_0^1 \dfrac{e^x + e^{-x}}{1 + 3^x} \mathrm{d}x \\
      & = \int_0^1 3^x \cdot \dfrac{e^{-x} + e^{x}}{1 + 3^x} \mathrm{d}x + \int_0^1 \dfrac{e^x + e^{-x}}{1 + 3^x} \mathrm{d}x \\
      & = \int_0^1 \left( 3^x + 1 \right) \cdot \dfrac{e^{-x} + e^{x}}{1 + 3^x} \mathrm{d}x \\
      & = \int_0^1 e^{-x} + e^{x} \mathrm{d}x \\
      & = \left. \left( -e^{-x} + e^{x} \right) \right|_0^1 \\
      & = e - \dfrac{1}{e}.

   .. note::
      被积函数 :math:`\dfrac{e^x + e^{-x}}{1 + 3^x}` 分母里的 :math:`3` 替换为任何正实数, 定积分的值都是 :math:`e - \dfrac{1}{e}`.

.. _extra-chap6-topic2:

2. 极坐标下曲线 :math:`r = r(\theta)` 求曲线长公式推导.

.. proof:solution::

   由定义, 弧长为折线段长度和的极限, 记 :math:`\mathrm{d} \ell` 为弧长元素 (折线长), 那么 :math:`r(\theta)`, :math:`r(\theta + \mathrm{d} \theta)`,
   :math:`\mathrm{d} \ell` 三者构成一个三角形, 由余弦定理有

   .. math::
      (\mathrm{d} \ell)^2 = r^2(\theta) + r^2(\theta + \mathrm{d} \theta) - 2 r(\theta) r(\theta + \mathrm{d} \theta) \cos \mathrm{d} \theta.

   假设 :math:`r(\theta)` 在 :math:`[\alpha, \beta]` 上足够光滑 (连续可导), 那么

   .. math::
      r(\theta + \mathrm{d} \theta) = r(\theta) + r'(\theta) \mathrm{d} \theta + o(\mathrm{d} \theta),

   于是有

   .. math::
      (\mathrm{d} \ell)^2
      & = r^2(\theta) + r^2(\theta + \mathrm{d} \theta) - 2 r(\theta) r(\theta + \mathrm{d} \theta) \cos \mathrm{d} \theta \\
      & = (r(\theta) - r(\theta + \mathrm{d} \theta))^2 + 2 r(\theta) r(\theta + \mathrm{d} \theta) (1 - \cos \mathrm{d} \theta) \\
      & = (r'(\theta) \mathrm{d} \theta + o(\mathrm{d} \theta))^2
          + r(\theta) (r(\theta) + r'(\theta) \mathrm{d} \theta + o(\mathrm{d} \theta)) ((\mathrm{d} \theta)^2 + o((\mathrm{d} \theta)^2)) \\
      & = (r'(\theta))^2 (\mathrm{d} \theta)^2 + {\color{red} 2 r'(\theta) \mathrm{d} \theta o(\mathrm{d} \theta)} + o((\mathrm{d} \theta)^2) \\
      &   \phantom{===} + r^2(\theta) (\mathrm{d} \theta)^2 + {\color{red} r^2(\theta) o((\mathrm{d} \theta)^2)}
          + {\color{red} r(\theta) r'(\theta) (\mathrm{d} \theta)^3} \\
      &   \phantom{===} + {\color{red} r(\theta) r'(\theta) \mathrm{d} \theta o((\mathrm{d} \theta)^2)}
          + {\color{red} r(\theta) (\mathrm{d} \theta)^2 o(\mathrm{d} \theta)} + {\color{red} r(\theta) o((\mathrm{d} \theta)^3)} \\
      & = (r'(\theta))^2 (\mathrm{d} \theta)^2 + r^2(\theta) (\mathrm{d} \theta)^2 + o((\mathrm{d} \theta)^2) \\
      & = (r'(\theta)^2 + r^2(\theta) + o(1)) (\mathrm{d} \theta)^2.

   以上倒数第二个等式成立是因为红色的项都是 :math:`(\mathrm{d} \theta)^2` 的高阶无穷小,
   第三个等式用到了 :math:`\cos \mathrm{d} \theta` 的麦克劳林展开式 (的变形)

   .. math::
      2(1 - \cos \mathrm{d} \theta) = (\mathrm{d} \theta)^2 + o((\mathrm{d} \theta)^2),

   所以有

   .. math::
      \mathrm{d} \ell = \sqrt{r'(\theta)^2 + r^2(\theta)} \mathrm{d} \theta.

   我们也可以发现, 对于以 :math:`r(\theta)` 为半径, :math:`\mathrm{d} \theta` 为角度的圆弧, 其弧长平方 :math:`r^2(\theta) (\mathrm{d} \theta)^2` 与折线平方的误差为

   .. math::
      r'(\theta)^2) (\mathrm{d} \theta)^2.

   究其原因, 就是因为圆弧, 折线, 以及 :math:`r(\theta + \mathrm{d} \theta)` 相对于 :math:`r(\theta)` 的增量 (或减量) :math:`r'(\theta) \mathrm{d} \theta`
   几乎构成了一个以折线为斜边的直角三角形, 从而导致了这个误差.
