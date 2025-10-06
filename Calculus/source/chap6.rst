第六章  定积分及其应用
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. contents:: :local:


课后习题解答
====================================

§6.1 定积分的概念
------------------------------------

§6.2 定积分的性质
------------------------------------

§6.3 微积分基本定理
------------------------------------

§6.4 定积分的换元法和分部积分法
------------------------------------

§6.5 广义积分
------------------------------------

§6.6 定积分的几何应用
------------------------------------

补充内容
====================================

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
