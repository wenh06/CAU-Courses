第五章  不定积分
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. contents:: :local:


.. _ex-chap5:

课后习题解答
====================================

.. _ex-chap5-sec1:

5.1 不定积分的概念与性质
------------------------------------

.. _ex-chap5-sec1-ex1:

1. 求下列不定积分.

   (1) :math:`\displaystyle \int \dfrac{1}{x^2 \sqrt{x}} ~ \mathrm{d}x`; \qquad
   (2) :math:`\displaystyle \int \left( x^2 - 3x + 2 \right) \mathrm{d}x`;

   (3) :math:`\displaystyle \int \dfrac{(1 - x)^2}{\sqrt{x}} ~ \mathrm{d}x`; \qquad
   (4) :math:`\displaystyle \int \left( 2e^x + \dfrac{3}{x} \right) \mathrm{d}x`;

   (5) :math:`\displaystyle \int \left( \dfrac{3}{1 + x^2} - \dfrac{2}{\sqrt{1 - x^2}} \right) \mathrm{d}x`; \qquad
   (6) :math:`\displaystyle \int \sec x (\sec x - \tan x) ~ \mathrm{d}x`;

   (7) :math:`\displaystyle \int \cos^2 \dfrac{x}{2} ~ \mathrm{d}x`; \qquad
   (8) :math:`\displaystyle \int \dfrac{1}{1 + \cos 2x} ~ \mathrm{d}x`;

   (9) :math:`\displaystyle \int \dfrac{3x^4 + 2x^2}{x^2 + 1} ~ \mathrm{d}x`; \qquad
   (10) :math:`\displaystyle \int \dfrac{1}{x^4 + x^6} ~ \mathrm{d}x`;

   (11) :math:`\displaystyle \int \left( \sqrt{\dfrac{1 - x}{1 + x}} + \sqrt{\dfrac{1 + x}{1 - x}} \right) \mathrm{d}x`; \qquad
   (12) :math:`\displaystyle \int \dfrac{1 + \cos^2 x}{1 + \cos 2x} ~ \mathrm{d}x`.

.. proof:solution::

   待写.

.. _ex-chap5-sec1-ex2:

2. 设 :math:`\displaystyle \int x f(x) ~ \mathrm{d}x = \arccos x + C`, 求 :math:`f(x)`.

.. proof:solution::

   待写.

.. _ex-chap5-sec1-ex3:

3. 设 :math:`f'(x) = \sin x`, 求 :math:`f(x)` 的全体原函数.

.. proof:solution::

   由不定积分的定义, 有

   .. math::
      f(x) = \int \sin x ~ \mathrm{d}x = -\cos x + C.

   那么, :math:`f(x)` 的全体原函数, 即它的不定积分为

   .. math::
      \int f(x) ~ \mathrm{d}x = \int \left( -\cos x + C \right) ~ \mathrm{d}x = -\sin x + Cx + D,

   其中 :math:`C, D` 为任意常数.

   .. note::
      这题是已知函数的导函数, 求它的原函数, 不是求该函数本身, 注意文字上的细微差别.

.. _ex-chap5-sec1-ex4:

4. 一曲线通过点 :math:`\left( e^2, 3 \right)`, 且在任一点处的切线的斜率等于该点横坐标的倒数, 求该曲线的方程.

.. proof:solution::

   待写.

.. _ex-chap5-sec1-ex5:

5. 一物体由静止开始运动, 经 :math:`t` s 后的速度是 :math:`3t^2` m/s, 问:

   (1) 在 :math:`3` s 后物体离开出发点的距离是多少?

   (2) 物体走完 :math:`360` m 需要多少时间?

.. proof:solution::

   待写.

.. _ex-chap5-sec2:

§5.2 换元积分法
------------------------------------

.. _ex-chap5-sec2-ex1:

1. 在下列各式等号右端的横线处填入适当的系数, 使等式成立.

   (1) :math:`\mathrm{d}x =` :math:`\underline{\hspace{1.5em}}` :math:`\mathrm{d}(ax)`; \qquad
   (2) :math:`\mathrm{d}x =` :math:`\underline{\hspace{1.5em}}` :math:`\mathrm{d}(7x - 3)`;

   (3) :math:`x ~ \mathrm{d}x =` :math:`\underline{\hspace{1.5em}}` :math:`\mathrm{d}(x^2)`; \qquad
   (4) :math:`x ~ \mathrm{d}x =` :math:`\underline{\hspace{1.5em}}` :math:`\mathrm{d}(5x^2)`;

   (5) :math:`x ~ \mathrm{d}x =` :math:`\underline{\hspace{1.5em}}` :math:`\mathrm{d}(1 - x^2)`; \qquad
   (6) :math:`x^3 ~ \mathrm{d}x =` :math:`\underline{\hspace{1.5em}}` :math:`\mathrm{d}(3x^4 - 2)`;

   (7) :math:`e^{2x} ~ \mathrm{d}x =` :math:`\underline{\hspace{1.5em}}` :math:`\mathrm{d}(e^{2x})`; \qquad
   (8) :math:`e^{-\frac{x}{2}} ~ \mathrm{d}x =` :math:`\underline{\hspace{1.5em}}` :math:`\mathrm{d}\left( 1 + e^{-\frac{x}{2}} \right)`;

   (9) :math:`\sin \dfrac{3}{2} x ~ \mathrm{d}x =` :math:`\underline{\hspace{1.5em}}` :math:`\mathrm{d}\left( \cos \dfrac{3}{2} x \right)`; \qquad
   (10) :math:`\dfrac{\mathrm{d}x}{x} =` :math:`\underline{\hspace{1.5em}}` :math:`\mathrm{d}(5 \ln \lvert x \rvert)`;

   (11) :math:`\dfrac{\mathrm{d}x}{x} =` :math:`\underline{\hspace{1.5em}}` :math:`\mathrm{d}(3 - 5 \ln \lvert x \rvert)`; \qquad
   (12) :math:`\dfrac{\mathrm{d}x}{1 + 9x^2} =` :math:`\underline{\hspace{1.5em}}` :math:`\mathrm{d}(\arctan 3x)`;

   (13) :math:`\dfrac{\mathrm{d}x}{\sqrt{1 - x^2}} =` :math:`\underline{\hspace{1.5em}}` :math:`\mathrm{d}(1 - \arcsin x)`; \qquad
   (14) :math:`\dfrac{x ~ \mathrm{d}x}{\sqrt{1 - x^2}} =` :math:`\underline{\hspace{1.5em}}` :math:`\mathrm{d}\left( \sqrt{1 - x^2} \right)`;

   (15) :math:`\dfrac{1}{\sqrt{t}} \mathrm{d}t =` :math:`\underline{\hspace{1.5em}}` :math:`\mathrm{d}(\sqrt{t})`; \qquad
   (16) :math:`\dfrac{\mathrm{d}x}{\cos^2 2x} =` :math:`\underline{\hspace{1.5em}}` :math:`\mathrm{d}(\tan 2x)`.

.. proof:solution::

   待写.

.. _ex-chap5-sec2-ex2:

2. 求下列不定积分.

   (1) :math:`\displaystyle \int e^{5x} ~ \mathrm{d}x`; \qquad
   (2) :math:`\displaystyle \int (3 - 2x)^3 ~ \mathrm{d}x`;

   (3) :math:`\displaystyle \int \dfrac{1}{1 - 2x} ~ \mathrm{d}x`; \qquad
   (4) :math:`\displaystyle \int \dfrac{1}{\sqrt[3]{2 - 3x}} ~ \mathrm{d}x`;

   (5) :math:`\displaystyle \int \left( \sin ax - e^{\frac{x}{b}} \right) \mathrm{d}x`; \qquad
   (6) :math:`\displaystyle \int \dfrac{\sin \sqrt{t}}{\sqrt{t}} ~ \mathrm{d}t`;

   (7) :math:`\displaystyle \int x e^{-x^2} ~ \mathrm{d}x`; \qquad
   (8) :math:`\displaystyle \int x \cos(x^2) ~ \mathrm{d}x`;

   (9) :math:`\displaystyle \int \dfrac{x}{\sqrt{2 - 3x^2}} ~ \mathrm{d}x`; \qquad
   (10) :math:`\displaystyle \int \dfrac{3x^3}{1 - x^4} ~ \mathrm{d}x`;

   (11) :math:`\displaystyle \int \dfrac{x + 1}{x^2 + 2x + 5} ~ \mathrm{d}x`; \qquad
   (12) :math:`\displaystyle \int \dfrac{\sin x}{\cos^3 x} ~ \mathrm{d}x`;

   (13) :math:`\displaystyle \int \dfrac{\sin x + \cos x}{\sqrt[3]{\sin x - \cos x}} ~ \mathrm{d}x`; \qquad
   (14) :math:`\displaystyle \int \tan^{10} x \sec^2 x ~ \mathrm{d}x`;

   (15) :math:`\displaystyle \int \dfrac{1}{(\arcsin x)^2 \sqrt{1 - x^2}} ~ \mathrm{d}x`; \qquad
   (16) :math:`\displaystyle \int \tan \sqrt{1 + x^2} \cdot \dfrac{x}{\sqrt{1 + x^2}} ~ \mathrm{d}x`;

   (17) :math:`\displaystyle \int \dfrac{\arctan \sqrt{x}}{\sqrt{x} (1 + x)} ~ \mathrm{d}x`; \qquad
   (18) :math:`\displaystyle \int \dfrac{1 + \ln x}{(x \ln x)^2} ~ \mathrm{d}x`;

   (19) :math:`\displaystyle \int \dfrac{1}{\sin x \cos x} ~ \mathrm{d}x`; \qquad
   (20) :math:`\displaystyle \int \dfrac{\ln \tan x}{\cos x \sin x} ~ \mathrm{d}x`;

   (21) :math:`\displaystyle \int \cos^3 x ~ \mathrm{d}x`; \qquad
   (22) :math:`\displaystyle \int \cos^2 (\omega t + \varphi) ~ \mathrm{d}t`;

   (23) :math:`\displaystyle \int \tan^3 x \sec x ~ \mathrm{d}x`; \qquad
   (24) :math:`\displaystyle \int \dfrac{1}{e^x + e^{-x}} ~ \mathrm{d}x`;

   (25) :math:`\displaystyle \int \dfrac{1 - x}{\sqrt{9 - 4x^2}} ~ \mathrm{d}x`; \qquad
   (26) :math:`\displaystyle \int \dfrac{x^3}{9 + x^2} ~ \mathrm{d}x`;

   (27) :math:`\displaystyle \int \dfrac{x^2}{\sqrt{a^2 - x^2}} ~ \mathrm{d}x` (:math:`a > 0`); \qquad
   (28) :math:`\displaystyle \int \dfrac{1}{\sqrt{(x^2 + 1)^3}} ~ \mathrm{d}x`;

   (29) :math:`\displaystyle \int \dfrac{1}{1 + \sqrt{2x}} ~ \mathrm{d}x`; \qquad
   (30) :math:`\displaystyle \int \dfrac{1}{1 + \sqrt{1 - x^2}} ~ \mathrm{d}x`;

   (31) :math:`\displaystyle \int \dfrac{x - 1}{x^2 + 2x + 3} ~ \mathrm{d}x`; \qquad
   (32) :math:`\displaystyle \int \dfrac{1}{x \sqrt{x^2 - 1}} ~ \mathrm{d}x`;

   (33) :math:`\displaystyle \int \dfrac{\sqrt{x^2 - 9}}{x} ~ \mathrm{d}x`; \qquad
   (34) :math:`\displaystyle \int \dfrac{x^3 + 1}{(x^2 + 1)^2} ~ \mathrm{d}x`.

.. proof:solution::

   待写.

.. _ex-chap5-sec3:

§5.3 分部积分法
------------------------------------

.. _ex-chap5-sec3-ex1:

1. 求下列不定积分.

   (1) :math:`\displaystyle \int x \sin x ~ \mathrm{d}x`; \qquad
   (2) :math:`\displaystyle \int \dfrac{\ln x}{x^2} ~ \mathrm{d}x`;

   (3) :math:`\displaystyle \int \dfrac{\ln \ln x}{x} ~ \mathrm{d}x`; \qquad
   (4) :math:`\displaystyle \int x^2 \cos x ~ \mathrm{d}x`;

   (5) :math:`\displaystyle \int y e^{-2y} ~ \mathrm{d}y`; \qquad
   (6) :math:`\displaystyle \int \arcsin x ~ \mathrm{d}x`;

   (7) :math:`\displaystyle \int (\arcsin x)^2 ~ \mathrm{d}x`; \qquad
   (8) :math:`\displaystyle \int x \tan^2 x ~ \mathrm{d}x`;

   (9) :math:`\displaystyle \int (\arccos x)^2 ~ \mathrm{d}x`; \qquad
   (10) :math:`\displaystyle \int \dfrac{\ln \cos x}{\cos^2 x} ~ \mathrm{d}x`.

.. proof:solution::

   待写.

.. _ex-chap5-sec3-ex2:

2. 已知 :math:`f(x) = \frac{e^x}{x}`, 求 :math:`\displaystyle \int x f''(x) ~ \mathrm{d}x`.

.. proof:solution::

   利用分部积分法, 有

   .. math::
      \int x f''(x) ~ \mathrm{d}x & = \int x ~ \mathrm{d} f'(x) = x f'(x) - \int f'(x) ~ \mathrm{d}x \\
      & = x f'(x) - f(x) + C.

   将 :math:`f(x) = \frac{e^x}{x}` 代入上式, 得

   .. math::
      \int x f''(x) ~ \mathrm{d}x = x \left( \frac{e^x}{x} \right)' - \frac{e^x}{x} + C
      = x \cdot \frac{(x - 1) e^x}{x^2} - \frac{e^x}{x} + C = \frac{(x - 2) e^x}{x} + C.

.. _ex-chap5-sec4:

§5.4 几种特殊类型函数的不定积分
------------------------------------

.. _ex-chap5-sec4-ex1:

1. 求下列不定积分.

   (1) :math:`\displaystyle \int \dfrac{1}{\sqrt[3]{(x + 1)^2 (x - 1)^4}} ~ \mathrm{d}x`; \qquad
   (2) :math:`\displaystyle \int \dfrac{x^4}{x + 2} ~ \mathrm{d}x`;

   (3) :math:`\displaystyle \int \dfrac{x^7}{x^4 + 2} ~ \mathrm{d}x`; \qquad
   (4) :math:`\displaystyle \int \dfrac{\cos x}{2 \sin x + \cos x} ~ \mathrm{d}x`;

   (5) :math:`\displaystyle \int \dfrac{1}{5 - 3 \cos x} ~ \mathrm{d}x`; \qquad
   (6) :math:`\displaystyle \int \dfrac{\cos^5 x}{\sin^4 x} ~ \mathrm{d}x`;

   (7) :math:`\displaystyle \int \dfrac{\sqrt[3]{1 + \sqrt[4]{x}}}{\sqrt{x}} ~ \mathrm{d}x`; \qquad
   (8) :math:`\displaystyle \int \dfrac{1}{(2x^2 + 1) \sqrt{x^2 + 1}} ~ \mathrm{d}x`.

.. proof:solution::

   待写.

.. _ex-chap5-sec4-ex2:

2. 试不用万用转换公式计算 :math:`\displaystyle \int \dfrac{1}{\sin^4 x} ~ \mathrm{d}x`.

.. proof:solution::

   注意到 :math:`\dfrac{1}{\sin^4 x} = \csc^4 x`, 因此有

   .. math::
      \int \dfrac{1}{\sin^4 x} ~ \mathrm{d}x
      & = \int \csc^4 x ~ \mathrm{d}x = \int \csc^2 x \cdot \csc^2 x ~ \mathrm{d}x \\
      & = - \int (1 + \cot^2 x) ~ \mathrm{d} (\cot x) \\
      & = - \cot x - \dfrac{1}{3} \cot^3 x + C.

.. _ex-chap5-sec4-ex3:

3. 求 :math:`\displaystyle \int \dfrac{f'(\ln x)}{x \sqrt{f(\ln x)}} ~ \mathrm{d}x`.

.. proof:solution::

   待写.

.. _extra-chap5:

补充内容
====================================

.. _extra-chap5-topic1:

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

.. _extra-chap5-topic2:

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
