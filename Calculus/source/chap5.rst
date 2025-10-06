第五章  不定积分
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. contents:: :local:


课后习题解答
====================================

5.1 不定积分的概念与性质
------------------------------------

§5.2 换元积分法
------------------------------------

§5.3 分部积分法
------------------------------------

§5.4 几种特殊类型函数的不定积分
------------------------------------

补充内容
====================================

1. 求不定积分 :math:`\displaystyle \int \dfrac{\sqrt{1-x} \arctan \sqrt{1-x}}{2 - x} \mathrm{d}x`.

.. proof:solution::

   令 :math:`t = \sqrt{1-x}`, 那么 :math:`x = 1 - t^2`, 于是

   .. math::
      \int \dfrac{\sqrt{1-x} \arctan \sqrt{1-x}}{2 - x} \mathrm{d}x & = \int \dfrac{t \arctan t}{1 + t^2} (-2t) \mathrm{d}t \\
      & = -2 \int \dfrac{t^2 \arctan t}{1 + t^2} \mathrm{d}t \\
      & = -2 \int \left( 1 - \dfrac{1}{1 + t^2} \right) \arctan t \mathrm{d}t \\
      & = 2 \int \arctan t \mathrm d (\arctan t) - 2 \int \arctan t \mathrm{d}t \\
      & = \arctan^2 t - 2 \int \arctan t \mathrm{d}t \\
      & = \arctan^2 t -2 t \arctan t + 2 \int \dfrac{t}{1 + t^2} \mathrm{d}t \\
      & = \arctan^2 t -2 t \arctan t + \ln(1 + t^2) + C

   回代 :math:`t = \sqrt{1-x}`, 得

   .. math::
      \int \dfrac{\sqrt{1-x} \arctan \sqrt{1-x}}{2 - x} \mathrm{d}x = \arctan^2 \sqrt{1-x} -2 \sqrt{1-x} \arctan \sqrt{1-x} + \ln(2 - x) + C.

2. 求不定积分

   (1). :math:`\displaystyle \int x^2 \sqrt{x} ~ \mathrm{d}x`

   (2). :math:`\displaystyle \int \dfrac{1}{x^4 \sqrt{x^2 + 1}} ~ \mathrm{d}x`

   (3). :math:`\displaystyle \int \dfrac{1}{\sin^2 x \cos^2 x} ~ \mathrm{d}x`

   (4). :math:`\displaystyle \int \dfrac{1}{x^2 - 8x + 25} ~ \mathrm{d}x`

   (5). :math:`\displaystyle \int \dfrac{x^5}{\sqrt{1 + x^2}} ~ \mathrm{d}x`

   (6). :math:`\displaystyle \int x^3 \ln x ~ \mathrm{d}x`

.. proof:solution::

   (1). 做变量替换 :math:`t = \sqrt{x}`, 那么 :math:`x = t^2`, :math:`\mathrm{d}x = 2t \mathrm{d}t`, 从而有

   .. math::
      \int x^2 \sqrt{x} ~ \mathrm{d}x = \int t^4 \cdot t \cdot 2t ~ \mathrm{d}t = 2 \int t^6 ~ \mathrm{d}t
      = \dfrac{2}{7} t^7 + C = \dfrac{2}{7} x^{\frac{7}{2}} + C

   这题也可以直接做:

   .. math::
      \int x^2 \sqrt{x} ~ \mathrm{d}x = \int x^{\frac{5}{2}} ~ \mathrm{d}x = \dfrac{2}{7} x^{\frac{7}{2}} + C

   (2). 做变量替换 :math:`t = 1/x`, 那么有

   .. math::
      \int \dfrac{1}{x^4 \sqrt{x^2 + 1}} ~ \mathrm{d}x & = -\int \dfrac{t^4}{\sqrt{\frac{1}{t^2} + 1}} \cdot \dfrac{1}{t^2} ~ \mathrm{d}t \\
      & = -\dfrac{1}{2} \int \dfrac{t^2 + 1 - 1}{\sqrt{t^2 + 1}} ~ \mathrm{d}(t^2 + 1) \\
      & = -\dfrac{1}{2} \int \sqrt{t^2 + 1} ~ \mathrm{d}(t^2 + 1) + \dfrac{1}{2} \int \dfrac{1}{\sqrt{t^2 + 1}} ~ \mathrm{d}(t^2 + 1) \\
      & = -\dfrac{1}{3} (t^2 + 1)^{\frac{3}{2}} + \sqrt{t^2 + 1} + C \\
      & = -\dfrac{1}{3} \left( \dfrac{1}{x^2} + 1 \right)^{\frac{3}{2}} + \sqrt{\dfrac{1}{x^2} + 1} + C \\
      & = -\dfrac{(x^2 + 1) \sqrt{x^2 + 1}}{3x^3} + \dfrac{\sqrt{x^2 + 1}}{x} + C \\
      & = \dfrac{2x^2 - 1}{3x^3} \sqrt{x^2 + 1} + C

   (3). 注意到 :math:`1 = \sin^2 x + \cos^2 x`, 从而有

   .. math::
      \int \dfrac{1}{\sin^2 x \cos^2 x} ~ \mathrm{d}x
      & = \int \dfrac{\sin^2 x + \cos^2 x}{\sin^2 x \cos^2 x} ~ \mathrm{d}x
        = \int \left( \dfrac{1}{\sin^2 x} + \dfrac{1}{\cos^2 x} \right) ~ \mathrm{d}x \\
      & = - \cot x + \tan x + C

   (4).

   .. math::
      \int \dfrac{1}{x^2 - 8x + 25} ~ \mathrm{d}x = \int \dfrac{1}{(x - 4)^2 + 3^2} ~ \mathrm{d}(x - 4)
      = \dfrac{1}{3} \arctan \dfrac{x - 4}{3} + C

   (5).

   .. math::
      \int \dfrac{x^5}{\sqrt{1 + x^2}} ~ \mathrm{d}x & = \dfrac{1}{2} \int \dfrac{x^4 ~ \mathrm{d}(x^2 + 1)}{\sqrt{x^2 + 1}} \\
      & = \dfrac{1}{2} \int \dfrac{(x^2 + 1 - 1)^2 ~ \mathrm{d}(x^2 + 1)}{\sqrt{x^2 + 1}} \\
      & = \dfrac{1}{2} \int \left( (x^2 + 1)^{\frac{3}{2}} - 2 (x^2 + 1)^{\frac{1}{2}} + (x^2 + 1)^{-\frac{1}{2}} \right) ~ \mathrm{d}(x^2 + 1) \\
      & = \dfrac{1}{2} \left( \dfrac{2}{5} (x^2 + 1)^{\frac{5}{2}} - \dfrac{4}{3} (x^2 + 1)^{\frac{3}{2}} + 2 \sqrt{x^2 + 1} \right) + C \\
      & = \dfrac{3 x^4 - 4 x^2 + 8}{15} \sqrt{x^2 + 1} + C

   (6).

   .. math::
      \int x^3 \ln x ~ \mathrm{d}x & = \dfrac{1}{4} \int \ln x ~ \mathrm{d}(x^4) = \dfrac{1}{4} x^4 \ln x - \dfrac{1}{4} \int x^3 ~ \mathrm{d}x \\
      & = \dfrac{1}{4} x^4 \ln x - \dfrac{1}{16} x^4 + C
