第三章  导数与微分
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. contents:: :local:


.. _ex-chap3:

课后习题解答
====================================

.. _ex-chap3-sec1:

§3.1 导数的概念
------------------------------------

.. _ex-chap3-sec1-ex1:

1. 设 :math:`f(x) = 5x^2`, 根据导数的定义求 :math:`f'(2)`.

.. proof:solution::

   由导数的定义,

   .. math::
      f'(2) = \lim_{x \to 2} \dfrac{f(x) - f(2)}{x - 2}
      = \lim_{x \to 2} \dfrac{5x^2 - 20}{x - 2}
      = \lim_{x \to 2} 5(x + 2) = 20.

.. _ex-chap3-sec1-ex2:

2. 设函数 :math:`f(x) = ax + 4`, 若 :math:`f'(1) = 2`, 则 :math:`a =` (   ).

   A. :math:`2` \qquad B. :math:`-2` \qquad C. :math:`3` \qquad D. 不确定

.. proof:solution::

   选 A. 一次函数 :math:`f(x) = ax + 4` 的导数 :math:`f'(x) = a` 处处相同, 故 :math:`f'(1) = a = 2`.

.. _ex-chap3-sec1-ex3:

3. 设 :math:`f(x)` 在 :math:`x_0` 处可导, 求下列极限值.

   (1) :math:`\lim\limits_{h \to 0} \dfrac{f(x_0) - f(x_0 - h)}{h}`;

   (2) :math:`\lim\limits_{\Delta x \to 0} \dfrac{f(x_0 + 2\Delta x) - f(x_0 - \Delta x)}{\Delta x}`.

.. proof:solution::

   (1). 令 :math:`t = -h`, 则 :math:`h \to 0` 等价于 :math:`t \to 0`, 于是

   .. math::
      \lim_{h \to 0} \dfrac{f(x_0) - f(x_0 - h)}{h}
      = \lim_{t \to 0} \dfrac{f(x_0 + t) - f(x_0)}{t}
      = f'(x_0).

   (2). 由可导的定义, 有

   .. math::
      f(x_0 + 2\Delta x) = f(x_0) + f'(x_0) \cdot 2\Delta x + o(\Delta x), \\
      f(x_0 - \Delta x) = f(x_0) - f'(x_0) \cdot \Delta x + o(\Delta x).

   因此

   .. math::
      & \lim\limits_{\Delta x \to 0} \dfrac{f(x_0 + 2\Delta x) - f(x_0 - \Delta x)}{\Delta x} \\
      = & \lim\limits_{\Delta x \to 0} \dfrac{f(x_0) + f'(x_0) \cdot 2\Delta x + o(\Delta x)
        - \left( f(x_0) - f'(x_0) \cdot \Delta x + o(\Delta x) \right)}{\Delta x} \\
      = & \lim\limits_{\Delta x \to 0} \dfrac{3 f'(x_0) \cdot \Delta x + o(\Delta x)}{\Delta x} = 3 f'(x_0).

.. _ex-chap3-sec1-ex4:

4. 设 :math:`f(0) = 0`, :math:`f'(0) = 2`, 求 :math:`\lim\limits_{x \to 0} \dfrac{f(x)}{x}`.

.. proof:solution::

   由 :math:`f(0) = 0`, 所求极限正是 :math:`f(x)` 在 :math:`x = 0` 处的导数定义式:

   .. math::
      \lim_{x \to 0} \dfrac{f(x)}{x} = \lim_{x \to 0} \dfrac{f(x) - f(0)}{x - 0} = f'(0) = 2.

.. _ex-chap3-sec1-ex5:

5. 求下列函数的导数.

   (1) :math:`y = x^5`; \qquad
   (2) :math:`y = \sqrt{x^3}`; \qquad
   (3) :math:`y = \dfrac{1}{x^3}`;

   (4) :math:`y = \dfrac{1}{\sqrt[3]{x}}`; \qquad
   (5) :math:`y = x^2 \sqrt{x}`; \qquad
   (6) :math:`y = 2^x`.

.. proof:solution::

   按幂函数与指数函数的求导公式逐项求导:

   (1). :math:`y' = 5x^4`.

   (2). :math:`y = x^{\frac{3}{2}}`, :math:`y' = \dfrac{3}{2} x^{\frac{1}{2}} = \dfrac{3\sqrt{x}}{2}`.

   (3). :math:`y = x^{-3}`, :math:`y' = -3x^{-4} = -\dfrac{3}{x^4}`.

   (4). :math:`y = x^{-\frac{1}{3}}`, :math:`y' = -\dfrac{1}{3} x^{-\frac{4}{3}} = -\dfrac{1}{3x\sqrt[3]{x}}`.

   (5). :math:`y = x^{\frac{5}{2}}`, :math:`y' = \dfrac{5}{2} x^{\frac{3}{2}} = \dfrac{5}{2} x\sqrt{x}`.

   (6). :math:`y' = 2^x \ln 2`.

.. _ex-chap3-sec1-ex6:

6. 设 :math:`f(x)` 是定义在 :math:`(-a, a)` 上的奇函数, 若 :math:`f(x)` 可导, 证明 :math:`f'(x)` 是偶函数.

.. proof:solution::

   任取 :math:`x \in (-a, a)`. 由 :math:`f(x)` 是奇函数, 有 :math:`f(-t) = -f(t)`. 按导数定义,

   .. math::
      f'(-x) = \lim_{h \to 0} \dfrac{f(-x + h) - f(-x)}{h}
      = \lim_{h \to 0} \dfrac{-f(x - h) + f(x)}{h}
      = \lim_{h \to 0} \dfrac{f(x) - f(x - h)}{h}
      = f'(x).

   最后一个等号即导数定义的等价形式 (参见 :ref:`习题3.1 题3(1) <ex-chap3-sec1-ex3>`).
   因此对一切 :math:`x \in (-a, a)` 有 :math:`f'(-x) = f'(x)`, 即 :math:`f'(x)` 是偶函数.

.. _ex-chap3-sec1-ex7:

7. 求曲线 :math:`y = \sin x` 在点 :math:`\left( \dfrac{\pi}{4}, \dfrac{\sqrt{2}}{2} \right)` 处的切线方程和法线方程.

.. proof:solution::

   :math:`y' = \cos x`, 切线斜率 :math:`k = \cos\dfrac{\pi}{4} = \dfrac{\sqrt{2}}{2}`, 法线斜率为 :math:`-\sqrt{2}`. 切线方程为

   .. math::
      y - \dfrac{\sqrt{2}}{2} = \dfrac{\sqrt{2}}{2}\left( x - \dfrac{\pi}{4} \right),

   法线方程为

   .. math::
      y - \dfrac{\sqrt{2}}{2} = -\sqrt{2}\left( x - \dfrac{\pi}{4} \right).

.. _ex-chap3-sec1-ex8:

8. 求曲线 :math:`y = \ln x` 在点 :math:`(1, 0)` 处的切线方程和法线方程.

.. proof:solution::

   :math:`y' = \dfrac{1}{x}`, 切线斜率 :math:`k = 1`, 法线斜率为 :math:`-1`. 切线方程为 :math:`y = x - 1`,
   法线方程为 :math:`y = 1 - x`.

.. _ex-chap3-sec1-ex9:

9. 求曲线 :math:`y = e^x` 上斜率为 :math:`e` 的切线方程.

.. proof:solution::

   :math:`y' = e^x`. 由 :math:`e^x = e` 得切点横坐标 :math:`x = 1`, 切点为 :math:`(1, e)`. 切线方程为

   .. math::
      y - e = e(x - 1), \qquad \text{即} ~ y = ex.

.. _ex-chap3-sec1-ex10:

10. 若曲线 :math:`y = x^{-\frac{1}{2}}` 在点 :math:`\left( a, a^{-\frac{1}{2}} \right)` (其中 :math:`a > 0`)
    处的切线与两个坐标围成的三角形的面积为 :math:`18`, 求 :math:`a` 的值.

.. proof:solution::

   :math:`y' = -\dfrac{1}{2} x^{-\frac{3}{2}}`, 切线在点 :math:`\left( a, a^{-\frac{1}{2}} \right)` 处的斜率为
   :math:`-\dfrac{1}{2a^{\frac{3}{2}}}`, 方程为

   .. math::
      y - \dfrac{1}{\sqrt{a}} = -\dfrac{1}{2a^{\frac{3}{2}}} (x - a).

   令 :math:`y = 0` 得横截距 :math:`x = 3a`; 令 :math:`x = 0` 得纵截距 :math:`y = \dfrac{3}{2\sqrt{a}}`.
   于是三角形面积为

   .. math::
      \dfrac{1}{2} \cdot 3a \cdot \dfrac{3}{2\sqrt{a}} = \dfrac{9}{4}\sqrt{a} = 18,

   解得 :math:`\sqrt{a} = 8`, 即 :math:`a = 64`.

.. _ex-chap3-sec1-ex11:

11. 讨论 :math:`f(x) = \begin{cases} 0, & x = 0, \\ x^2 \sin \dfrac{1}{x}, & x \neq 0 \end{cases}`
    的连续性与可导性.

.. proof:solution::

   当 :math:`x \neq 0` 时, :math:`f(x) = x^2 \sin\dfrac{1}{x}` 是初等函数, 连续且可导, 且

   .. math::
      f'(x) = 2x \sin\dfrac{1}{x} - \cos\dfrac{1}{x}.

   在 :math:`x = 0` 处: 由 :math:`\left| x^2 \sin\dfrac{1}{x} \right| \leqslant x^2 \to 0` 得
   :math:`\lim\limits_{x \to 0} f(x) = 0 = f(0)`, 故 :math:`f(x)` 在 :math:`x = 0` 处连续. 又

   .. math::
      f'(0) = \lim_{x \to 0} \dfrac{f(x) - f(0)}{x - 0}
      = \lim_{x \to 0} x \sin\dfrac{1}{x} = 0,

   故 :math:`f(x)` 在 :math:`x = 0` 处可导. 综上, :math:`f(x)` 在 :math:`\mathbb{R}` 上处处连续且处处可导.

.. _ex-chap3-sec1-ex12:

12. 求下列函数在 :math:`x = 0` 处的左导数、右导数, 并判断函数在 :math:`x = 0` 处是否可导.

   (1) :math:`f(x) = \begin{cases} \cos x, & x > 0, \\ e^x, & x \leqslant 0; \end{cases}` \qquad
   (2) :math:`f(x) = \begin{cases} x, & x > 0, \\ x^3, & x \leqslant 0. \end{cases}`

.. proof:solution::

   (1). :math:`f(0) = e^0 = 1`. 右导数

   .. math::
      f'_+(0) = \lim_{x \to 0^+} \dfrac{\cos x - 1}{x} = \lim_{x \to 0^+} \dfrac{-\frac{x^2}{2}}{x} = 0;

   左导数

   .. math::
      f'_-(0) = \lim_{x \to 0^-} \dfrac{e^x - 1}{x} = 1.

   因 :math:`f'_+(0) \neq f'_-(0)`, 故 :math:`f(x)` 在 :math:`x = 0` 处不可导.

   (2). :math:`f(0) = 0`. 右导数 :math:`f'_+(0) = \lim\limits_{x \to 0^+} \dfrac{x - 0}{x} = 1`;
   左导数 :math:`f'_-(0) = \lim\limits_{x \to 0^-} \dfrac{x^3 - 0}{x} = \lim\limits_{x \to 0^-} x^2 = 0`.
   因 :math:`f'_+(0) \neq f'_-(0)`, 故 :math:`f(x)` 在 :math:`x = 0` 处不可导.

.. _ex-chap3-sec1-ex13:

13. 讨论 :math:`f(x) = \lvert x \rvert^3` 在 :math:`x = 0` 处的可导性.

.. proof:solution::

   :math:`f(0) = 0`, 分别计算左右导数:

   .. math::
      f'_+(0) = \lim_{x \to 0^+} \dfrac{x^3 - 0}{x} = \lim_{x \to 0^+} x^2 = 0, \qquad
      f'_-(0) = \lim_{x \to 0^-} \dfrac{(-x)^3 - 0}{x} = \lim_{x \to 0^-} (-x^2) = 0.

   因 :math:`f'_+(0) = f'_-(0) = 0`, 故 :math:`f(x)` 在 :math:`x = 0` 处可导, 且 :math:`f'(0) = 0`.

.. _ex-chap3-sec1-ex14:

14. 已知 :math:`f(x) = \begin{cases} \sin x, & x > 0, \\ e^x, & x \leqslant 0, \end{cases}` 求 :math:`f'(x)`.

.. proof:solution::

   当 :math:`x > 0` 时, :math:`f(x) = \sin x`, 因此 :math:`f'(x) = \cos x`.

   当 :math:`x < 0` 时, :math:`f(x) = e^x`, 因此 :math:`f'(x) = e^x`.

   当 :math:`x = 0` 时, :math:`\lim\limits_{x \to 0^+} f(x) = \lim\limits_{x \to 0^+} \sin x = 0`,
   :math:`\lim\limits_{x \to 0^-} f(x) = \lim\limits_{x \to 0^-} e^x = 1`, 因此 :math:`f(x)`
   在 :math:`x = 0` 处不连续, 故不可导. 综上所述, 有

   .. math::
      f'(x) = \begin{cases}
         \cos x, & x > 0, \\
         \text{不存在}, & x = 0, \\
         e^x, & x < 0.
      \end{cases}

   .. note::
      这题要注意的地方是, 不要把导函数的单边极限 :math:`\lim\limits_{x \to 0^+} f'(x)`,
      :math:`\lim\limits_{x \to 0^-} f'(x)`, 和单边导数 :math:`f'_+(0)`, :math:`f'_-(0)` 搞混了.

.. _ex-chap3-sec1-ex15:

15. 已知 :math:`f(x) = \begin{cases} \sin x, & x < 0, \\ ax + b, & x \geqslant 0, \end{cases}`
    在 :math:`x = 0` 处连续且可导, 求 :math:`a, b` 的值.

.. proof:solution::

   先用连续性: :math:`f(0) = b`, 左极限 :math:`\lim\limits_{x \to 0^-} \sin x = 0`, 故 :math:`b = 0`.

   再用可导性: 左导数

   .. math::
      f'_-(0) = \lim_{x \to 0^-} \dfrac{\sin x - b}{x} = \lim_{x \to 0^-} \dfrac{\sin x}{x} = 1,

   右导数

   .. math::
      f'_+(0) = \lim_{x \to 0^+} \dfrac{ax + b - b}{x} = a.

   由 :math:`f'_+(0) = f'_-(0)` 得 :math:`a = 1`. 综上 :math:`a = 1`, :math:`b = 0`.

.. _ex-chap3-sec2:

§3.2 求导法则
------------------------------------

.. _ex-chap3-sec2-ex1:

1. 求下列函数的导数.

   (1) :math:`y = x^3 - 4x^2 + 5x - 2`; \qquad
   (2) :math:`y = \dfrac{2}{x^3} + \dfrac{7}{x^2} + 6`;

   (3) :math:`y = x^2 \ln x`; \qquad
   (4) :math:`y = \sin x \cdot \cos x`;

   (5) :math:`y = (2 + 5x)(4 - 3x)`; \qquad
   (6) :math:`y = (\arcsin x)^2`;

   (7) :math:`y = \arctan e^x`; \qquad
   (8) :math:`y = \dfrac{1}{3 + x + x^2}`;

   (9) :math:`y = \ln(\ln x)`; \qquad
   (10) :math:`y = \ln \left[ \ln(\ln x) \right]`.

.. proof:solution::

   (1). :math:`y' = 3x^2 - 8x + 5`.

   (2). :math:`y = 2x^{-3} + 7x^{-2} + 6`, :math:`y' = -6x^{-4} - 14x^{-3} = -\dfrac{6}{x^4} - \dfrac{14}{x^3}`.

   (3). :math:`y' = 2x\ln x + x^2 \cdot \dfrac{1}{x} = 2x\ln x + x`.

   (4). :math:`y = \dfrac{1}{2}\sin 2x`, :math:`y' = \cos 2x`.

   (5). :math:`y' = 5(4-3x) + (2+5x)(-3) = 20 - 15x - 6 - 15x = 14 - 30x`.

   (6). :math:`y' = \dfrac{2\arcsin x}{\sqrt{1-x^2}}`.

   (7). :math:`y' = \dfrac{e^x}{1 + e^{2x}}`.

   (8). :math:`y' = -\dfrac{(3+x+x^2)'}{(3+x+x^2)^2} = -\dfrac{1+2x}{(3+x+x^2)^2}`.

   (9). 由复合函数求导法则 (由外向内), :math:`y' = \dfrac{1}{\ln x} \cdot \dfrac{1}{x} = \dfrac{1}{x\ln x}`.

   (10). :math:`y' = \dfrac{1}{\ln(\ln x)} \cdot \dfrac{1}{\ln x} \cdot \dfrac{1}{x} = \dfrac{1}{x \ln x \ln(\ln x)}`.

.. _ex-chap3-sec2-ex2:

2. 由方程 :math:`y \sin x + e^y - x = 1` 确定变量 :math:`y` 为 :math:`x` 的函数, 求导数
   :math:`y' \bigr|_{x=0}`.

.. proof:solution::

   方程两边对 :math:`x` 求导 (:math:`y` 是 :math:`x` 的函数), 得

   .. math::
      y' \sin x + y \cos x + e^y y' - 1 = 0,

   解出

   .. math::
      y' = \dfrac{1 - y\cos x}{\sin x + e^y}.

   将 :math:`x = 0` 代入原方程: :math:`y \cdot 0 + e^y - 0 = 1`, 得 :math:`y = 0`. 于是

   .. math::
      y' \bigr|_{x=0} = \dfrac{1 - 0}{0 + 1} = 1.

.. _ex-chap3-sec2-ex3:

3. 求曲线 :math:`xy + \ln y = 1` 在点 :math:`P(1, 1)` 处的切线方程与法线方程.

.. proof:solution::

   方程两边对 :math:`x` 求导, 得

   .. math::
      y + x y' + \dfrac{y'}{y} = 0,

   解出 :math:`y' = -\dfrac{y^2}{xy + 1}`. 在点 :math:`P(1, 1)` 处, :math:`y' \bigr|_{P} = -\dfrac{1}{2}`.
   切线方程为

   .. math::
      y - 1 = -\dfrac{1}{2}(x - 1), \qquad \text{即} ~ x + 2y - 3 = 0;

   法线斜率为 :math:`2`, 法线方程为 :math:`y - 1 = 2(x-1)`, 即 :math:`y = 2x - 1`.

.. _ex-chap3-sec2-ex4:

4. 求下列由参数方程所确定的函数的导数 :math:`\dfrac{\mathrm{d}y}{\mathrm{d}x}`.

   (1) :math:`\begin{cases} x = \cos^4 t, \\ y = \sin^4 t, \end{cases}` 在 :math:`t = 0`, :math:`\dfrac{\pi}{4}` 处;

   (2) :math:`\begin{cases} x = \dfrac{t}{1 + t}, \\ y = \dfrac{1 - t}{1 + t}, \end{cases}` 在 :math:`t = 0` 处.

.. proof:solution::

   (1). :math:`\dfrac{\mathrm{d}x}{\mathrm{d}t} = -4\cos^3 t \sin t`, :math:`\dfrac{\mathrm{d}y}{\mathrm{d}t} = 4\sin^3 t \cos t`,
   于是当 :math:`\sin t, \cos t` 都不为零时,

   .. math::
      \dfrac{\mathrm{d}y}{\mathrm{d}x} = \dfrac{4\sin^3 t \cos t}{-4\cos^3 t \sin t} = -\tan^2 t.

   在 :math:`t = \dfrac{\pi}{4}` 处, :math:`\dfrac{\mathrm{d}y}{\mathrm{d}x} = -1`. 在 :math:`t = 0` 处
   :math:`\dfrac{\mathrm{d}x}{\mathrm{d}t} = \dfrac{\mathrm{d}y}{\mathrm{d}t} = 0`, 公式不能直接代入; 此时
   :math:`\cos^2 t = \sqrt{x}`, 故 :math:`y = \sin^4 t = (1 - \sqrt{x})^2`, 从而

   .. math::
      \dfrac{\mathrm{d}y}{\mathrm{d}x} = 2(1 - \sqrt{x}) \cdot \left( -\dfrac{1}{2\sqrt{x}} \right) = 1 - \dfrac{1}{\sqrt{x}},
      \qquad \dfrac{\mathrm{d}y}{\mathrm{d}x} \Bigr|_{x=1} = 0.

   (2). :math:`\dfrac{\mathrm{d}x}{\mathrm{d}t} = \dfrac{1}{(1+t)^2}`,
   :math:`\dfrac{\mathrm{d}y}{\mathrm{d}t} = \dfrac{-(1+t) - (1-t)}{(1+t)^2} = -\dfrac{2}{(1+t)^2}`, 于是

   .. math::
      \dfrac{\mathrm{d}y}{\mathrm{d}x} = -2,

   它是常数, 在 :math:`t = 0` 处也为 :math:`-2`.

.. _ex-chap3-sec2-ex5:

5. 求下列函数在给定点处的导数.

   (1) :math:`y = 2 \sin x - \cos x`, 求 :math:`y' \bigr|_{x = \frac{\pi}{6}}` 和
       :math:`y' \bigr|_{x = \frac{\pi}{4}}`;

   (2) :math:`\rho = \theta \sin \theta + \dfrac{1}{2} \cos \theta`, 求
       :math:`\dfrac{\mathrm{d}\rho}{\mathrm{d}\theta} \bigr|_{\theta = \frac{\pi}{4}}`;

   (3) :math:`f(x) = \dfrac{1}{4 - x} + \dfrac{x^2}{5}`, 求 :math:`f'(0)` 和 :math:`f'(1)`.

.. proof:solution::

   (1). :math:`y' = 2\cos x + \sin x`, 故

   .. math::
      y' \Bigr|_{x = \frac{\pi}{6}} = 2 \cdot \dfrac{\sqrt{3}}{2} + \dfrac{1}{2} = \sqrt{3} + \dfrac{1}{2}, \qquad
      y' \Bigr|_{x = \frac{\pi}{4}} = 2 \cdot \dfrac{\sqrt{2}}{2} + \dfrac{\sqrt{2}}{2} = \dfrac{3\sqrt{2}}{2}.

   (2). :math:`\dfrac{\mathrm{d}\rho}{\mathrm{d}\theta} = \sin\theta + \theta\cos\theta - \dfrac{1}{2}\sin\theta
   = \dfrac{1}{2}\sin\theta + \theta\cos\theta`, 故

   .. math::
      \dfrac{\mathrm{d}\rho}{\mathrm{d}\theta} \Bigr|_{\theta = \frac{\pi}{4}}
      = \dfrac{1}{2} \cdot \dfrac{\sqrt{2}}{2} + \dfrac{\pi}{4} \cdot \dfrac{\sqrt{2}}{2}
      = \dfrac{\sqrt{2}}{8}(2 + \pi).

   (3). :math:`f'(x) = \dfrac{1}{(4-x)^2} + \dfrac{2x}{5}`, 故 :math:`f'(0) = \dfrac{1}{16}`,
   :math:`f'(1) = \dfrac{1}{9} + \dfrac{2}{5} = \dfrac{23}{45}`.

.. _ex-chap3-sec2-ex6:

6. 求下列函数的导数.

   (1) :math:`y = (3x + 6)^4`; \qquad
   (2) :math:`y = \cos(4 - 3x)`;

   (3) :math:`y = e^{-x^2}`; \qquad
   (4) :math:`y = \ln(1 + x^2)`;

   (5) :math:`y = 4 \sin^2 x`; \qquad
   (6) :math:`y = \sqrt{a^2 - x^2}`;

   (7) :math:`y = x \tan^2 x`; \qquad
   (8) :math:`y = \ln \cos x`.

.. proof:solution::

   (1). :math:`y' = 4(3x+6)^3 \cdot 3 = 12(3x+6)^3`.

   (2). :math:`y' = -\sin(4-3x) \cdot (-3) = 3\sin(4-3x)`.

   (3). :math:`y' = e^{-x^2} \cdot (-2x) = -2x e^{-x^2}`.

   (4). :math:`y' = \dfrac{2x}{1+x^2}`.

   (5). :math:`y' = 8\sin x\cos x = 4\sin 2x`.

   (6). :math:`y' = \dfrac{-2x}{2\sqrt{a^2-x^2}} = -\dfrac{x}{\sqrt{a^2-x^2}}`.

   (7). :math:`y' = \tan^2 x + x \cdot 2\tan x \cdot \sec^2 x = \tan^2 x + 2x\tan x\sec^2 x`.

   (8). :math:`y' = \dfrac{-\sin x}{\cos x} = -\tan x`.

.. _ex-chap3-sec2-ex7:

7. 求曲线 :math:`y = 2 \cos x + x^2` 在横坐标为 :math:`x = 0` 的点处的切线方程和法线方程.

.. proof:solution::

   :math:`x = 0` 时 :math:`y = 2`, 切点为 :math:`(0, 2)`. :math:`y' = -2\sin x + 2x`, 故切线斜率
   :math:`k = y'(0) = 0`. 切线方程为 :math:`y = 2`; 法线垂直于切线, 方程为 :math:`x = 0`.

.. _ex-chap3-sec2-ex8:

8. 求由下列方程所确定的隐函数的导数.

   (1) :math:`y^2 - 2xy + 9 = 0`; \qquad
   (2) :math:`x^3 + y^3 - 3xy = 0`;

   (3) :math:`xy = e^{x+y}`; \qquad
   (4) :math:`y = 1 - xe^y`.

.. proof:solution::

   (1). 两边对 :math:`x` 求导: :math:`2yy' - 2(y + xy') = 0`, 解得 :math:`y' = \dfrac{y}{y - x}`.

   (2). 两边对 :math:`x` 求导: :math:`3x^2 + 3y^2 y' - 3(y + xy') = 0`, 解得 :math:`y' = \dfrac{y - x^2}{y^2 - x}`.

   (3). 两边对 :math:`x` 求导: :math:`y + xy' = e^{x+y}(1 + y')`, 注意 :math:`e^{x+y} = xy`, 故
   :math:`y + xy' = xy(1 + y')`, 解得 :math:`y' = \dfrac{y(x-1)}{x(1-y)}`.

   (4). 两边对 :math:`x` 求导: :math:`y' = -e^y - xe^y y'`, 解得 :math:`y' = -\dfrac{e^y}{1 + xe^y}`
   (利用原方程也可写成 :math:`y' = -\dfrac{e^y}{2 - y}`).

.. _ex-chap3-sec2-ex9:

9. 用对数求导法求下列函数的导数.

   (1) :math:`y = \left( \dfrac{x}{1 + x} \right)^x`;

   (2) :math:`y = \sqrt[5]{\dfrac{x - 5}{\sqrt[5]{x^2 + 2}}}`;

   (3) :math:`y = \dfrac{\sqrt{x+1} (3 - x)^4}{(x + 1)^5}`;

   (4) :math:`y = \sqrt{x \sin x \sqrt{1 - e^x}}`.

.. proof:solution::

   (1). 两边取对数: :math:`\ln y = x\left[ \ln x - \ln(1+x) \right]`, 两边对 :math:`x` 求导:

   .. math::
      \dfrac{y'}{y} = \ln \dfrac{x}{1+x} + x\left( \dfrac{1}{x} - \dfrac{1}{1+x} \right)
      = \ln \dfrac{x}{1+x} + \dfrac{1}{1+x},

   故 :math:`y' = \left( \dfrac{x}{1+x} \right)^x \left[ \ln\dfrac{x}{1+x} + \dfrac{1}{1+x} \right]`.

   (2). 取对数: :math:`\ln y = \dfrac{1}{5}\ln(x-5) - \dfrac{1}{25}\ln(x^2+2)`, 求导得

   .. math::
      \dfrac{y'}{y} = \dfrac{1}{5(x-5)} - \dfrac{2x}{25(x^2+2)},

   故 :math:`y' = \sqrt[5]{\dfrac{x-5}{\sqrt[5]{x^2+2}}} \left[ \dfrac{1}{5(x-5)} - \dfrac{2x}{25(x^2+2)} \right]`.

   (3). 取对数: :math:`\ln y = \dfrac{1}{2}\ln(x+1) + 4\ln(3-x) - 5\ln(x+1)`, 求导得

   .. math::
      \dfrac{y'}{y} = -\dfrac{9}{2(x+1)} - \dfrac{4}{3-x},

   故 :math:`y' = \dfrac{\sqrt{x+1}\,(3-x)^4}{(x+1)^5} \left[ -\dfrac{9}{2(x+1)} - \dfrac{4}{3-x} \right]`.

   (4). 取对数: :math:`\ln y = \dfrac{1}{2}\ln x + \dfrac{1}{2}\ln\sin x + \dfrac{1}{4}\ln(1-e^x)`, 求导得

   .. math::
      \dfrac{y'}{y} = \dfrac{1}{2x} + \dfrac{\cos x}{2\sin x} - \dfrac{e^x}{4(1-e^x)},

   故 :math:`y' = \sqrt{x\sin x\sqrt{1-e^x}} \left[ \dfrac{1}{2x} + \dfrac{1}{2}\cot x - \dfrac{e^x}{4(1-e^x)} \right]`.

.. _ex-chap3-sec3:

§3.3 高阶导数
------------------------------------

.. _ex-chap3-sec3-ex1:

1. 求下列函数的高阶导数.

   (1) :math:`y = x^2 - 3x + 1`, 求 :math:`y''`, :math:`y'''`;

   (2) :math:`y = x^2 \sin x`, 求 :math:`y''`;

   (3) :math:`y = x^2 e^x`, 求 :math:`y''`;

   (4) :math:`y = \dfrac{\ln x}{x}`, 求 :math:`y''`.

.. proof:solution::

   (1). :math:`y' = 2x - 3`, 故 :math:`y'' = 2`, :math:`y''' = 0`.

   (2). :math:`y' = 2x\sin x + x^2\cos x`, 故

   .. math::
      y'' = 2\sin x + 2x\cos x + 2x\cos x - x^2\sin x
      = 2\sin x + 4x\cos x - x^2\sin x.

   (3). :math:`y' = 2x e^x + x^2 e^x = (x^2 + 2x)e^x`, 故

   .. math::
      y'' = (2x + 2)e^x + (x^2 + 2x)e^x = (x^2 + 4x + 2)e^x.

   (4). :math:`y' = \dfrac{\frac{1}{x} \cdot x - \ln x}{x^2} = \dfrac{1 - \ln x}{x^2}`, 故

   .. math::
      y'' = \dfrac{-\frac{1}{x} \cdot x^2 - (1 - \ln x) \cdot 2x}{x^4}
      = \dfrac{-1 - 2(1 - \ln x)}{x^3}
      = \dfrac{2\ln x - 3}{x^3}.

.. _ex-chap3-sec3-ex2:

2. 已知 :math:`f(x)` 任意次可导, 求下列复合函数的高阶导数.

   (1) :math:`y = e^{f(x)}`, 求 :math:`y''`;

   (2) :math:`y = f(x^2)`, 求 :math:`y''`;

   (3) :math:`y = f(e^{-x})`, 求 :math:`y''`;

   (4) :math:`y = \ln f(x)`, 求 :math:`y''`.

.. proof:solution::

   (1). :math:`y' = f'(x) e^{f(x)}`, 故

   .. math::
      y'' = f''(x) e^{f(x)} + \left[ f'(x) \right]^2 e^{f(x)}
      = \left[ f''(x) + \left( f'(x) \right)^2 \right] e^{f(x)}.

   (2). :math:`y' = 2x f'(x^2)`, 故

   .. math::
      y'' = 2 f'(x^2) + 2x \cdot f''(x^2) \cdot 2x = 2 f'(x^2) + 4x^2 f''(x^2).

   (3). :math:`y' = -e^{-x} f'(e^{-x})`, 故

   .. math::
      y'' = e^{-x} f'(e^{-x}) - e^{-x} \cdot f''(e^{-x}) \cdot (-e^{-x})
      = e^{-x} f'(e^{-x}) + e^{-2x} f''(e^{-x}).

   (4). :math:`y' = \dfrac{f'(x)}{f(x)}`, 故

   .. math::
      y'' = \dfrac{f''(x) f(x) - \left[ f'(x) \right]^2}{f^2(x)}.

.. _ex-chap3-sec3-ex3:

3. 设 :math:`y = e^x \sin x`, 利用莱布尼茨法则计算 :math:`y^{(n)}`.

.. proof:solution::

   记 :math:`u = \sin x`, :math:`v = e^x`, 则 :math:`u^{(k)} = \sin\left( x + \dfrac{k\pi}{2} \right)`,
   :math:`v^{(n-k)} = e^x`. 由莱布尼茨公式,

   .. math::
      y^{(n)} = \sum_{k=0}^{n} C_n^k \sin\left( x + \dfrac{k\pi}{2} \right) e^x
      = e^x \sum_{k=0}^{n} C_n^k \sin\left( x + \dfrac{k\pi}{2} \right).

   为求和, 利用复数记法 :math:`\sin\left( x + \dfrac{k\pi}{2} \right)` 是 :math:`e^{i\left( x + \frac{k\pi}{2} \right)}` 的虚部:

   .. math::
      \sum_{k=0}^{n} C_n^k e^{i\left( x + \frac{k\pi}{2} \right)}
      = e^{ix} \left( 1 + e^{i\frac{\pi}{2}} \right)^n
      = e^{ix} (1 + i)^n
      = e^{ix} \left( \sqrt{2} \right)^n e^{i\frac{n\pi}{4}},

   取虚部得 :math:`\sum\limits_{k=0}^{n} C_n^k \sin\left( x + \dfrac{k\pi}{2} \right) = \left( \sqrt{2} \right)^n \sin\left( x + \dfrac{n\pi}{4} \right)`.
   因此

   .. math::
      y^{(n)} = \left( \sqrt{2} \right)^n e^x \sin\left( x + \dfrac{n\pi}{4} \right).

.. _ex-chap3-sec3-ex4:

4. 对下列隐函数求二阶导数.

   (1) :math:`2y + \sin y = x^2`; \qquad
   (2) :math:`x^3 + y^3 - 3xy = 0`.

.. proof:solution::

   (1). 两边对 :math:`x` 求导: :math:`(2 + \cos y)y' = 2x`, 得 :math:`y' = \dfrac{2x}{2 + \cos y}`. 再求导:

   .. math::
      y'' = \dfrac{2(2 + \cos y) + 2x\sin y \cdot y'}{(2 + \cos y)^2}
      = \dfrac{2(2 + \cos y) + 2x\sin y \cdot \frac{2x}{2+\cos y}}{(2 + \cos y)^2}
      = \dfrac{2}{2 + \cos y} + \dfrac{4x^2 \sin y}{(2 + \cos y)^3}.

   (2). 两边对 :math:`x` 求导 (参见 :ref:`习题3.2 题8 <ex-chap3-sec2-ex8>`): :math:`y' = \dfrac{y - x^2}{y^2 - x}`. 再求导:

   .. math::
      y'' = \dfrac{(y' - 2x)(y^2 - x) - (y - x^2)(2yy' - 1)}{(y^2 - x)^2}.

   代入 :math:`y'` 并整理, 得

   .. math::
      y'' = \dfrac{2\left[ (y - x^2)(y^2 - x) - x(y^2-x)^2 - y(y-x^2)^2 \right]}{(y^2 - x)^3}.

   展开方括号: :math:`(y-x^2)(y^2-x) - x(y^2-x)^2 - y(y-x^2)^2 = -xy\left[ 1 + x^3 + y^3 - 3xy \right]`,
   由原方程 :math:`x^3 + y^3 = 3xy`, 方括号恰为 :math:`-xy`. 因此

   .. math::
      y'' = -\dfrac{2xy}{(y^2 - x)^3}.

.. _ex-chap3-sec3-ex5:

5. 求下列参数形式的函数的二阶导数.

   (1) :math:`\begin{cases} x = at^2, \\ y = bt^3; \end{cases}` \qquad
   (2) :math:`\begin{cases} x = \sqrt{1 + t}, \\ y = \sqrt{1 - t}; \end{cases}` \qquad
   (3) :math:`\begin{cases} x = \sin t, \\ y = \cos t. \end{cases}`

.. proof:solution::

   (1). :math:`\dfrac{\mathrm{d}y}{\mathrm{d}x} = \dfrac{3bt^2}{2at} = \dfrac{3bt}{2a}`, 故

   .. math::
      \dfrac{\mathrm{d}^2 y}{\mathrm{d}x^2}
      = \dfrac{\dfrac{\mathrm{d}}{\mathrm{d}t}\left( \dfrac{3bt}{2a} \right)}{\dfrac{\mathrm{d}x}{\mathrm{d}t}}
      = \dfrac{\frac{3b}{2a}}{2at} = \dfrac{3b}{4a^2 t}.

   (2). :math:`\dfrac{\mathrm{d}y}{\mathrm{d}x} = \dfrac{-\frac{1}{2\sqrt{1-t}}}{\frac{1}{2\sqrt{1+t}}} = -\sqrt{\dfrac{1+t}{1-t}}`, 故

   .. math::
      \dfrac{\mathrm{d}^2 y}{\mathrm{d}x^2}
      = \dfrac{\dfrac{\mathrm{d}}{\mathrm{d}t}\left( -\sqrt{\dfrac{1+t}{1-t}} \right)}{\dfrac{1}{2\sqrt{1+t}}}
      = \dfrac{-\dfrac{1}{\sqrt{1-t}} \cdot \dfrac{1}{(1-t)}}{\dfrac{1}{2\sqrt{1+t}}}
      = -\dfrac{2}{(1-t)^{\frac{3}{2}}},

   其中 :math:`\dfrac{\mathrm{d}}{\mathrm{d}t}\left( -\sqrt{\dfrac{1+t}{1-t}} \right) = -\dfrac{1}{(1-t)^{\frac{3}{2}}\sqrt{1+t}}`.

   (3). :math:`\dfrac{\mathrm{d}y}{\mathrm{d}x} = \dfrac{-\sin t}{\cos t} = -\tan t`, 故

   .. math::
      \dfrac{\mathrm{d}^2 y}{\mathrm{d}x^2}
      = \dfrac{-\sec^2 t}{\cos t} = -\dfrac{1}{\cos^3 t}.

.. _ex-chap3-sec3-ex6:

6. 证明: 函数

   .. math::
      f(x) = \begin{cases}
         e^{-\frac{1}{x^2}}, & x \neq 0, \\
         0, & x = 0,
      \end{cases}

   在 :math:`x = 0` 处 :math:`n` 阶可导且 :math:`f^{(n)}(0) = 0`, 其中 :math:`n` 是任意的正整数.

.. proof:proof::

   由题意可知, 当 :math:`x \neq 0` 时, :math:`f(x) = e^{-\frac{1}{x^2}}` 是一个初等函数, 因此在 :math:`x \neq 0` 时,
   :math:`f(x)` 存在任意阶导数.

   下面用数学归纳法证明 :math:`f(x)` 在 :math:`x = 0` 处 :math:`n` 阶可导且 :math:`f^{(n)}(0) = 0`.

   当 :math:`n = 1` 时, 有

   .. math::
      f'(0) = \lim\limits_{x \to 0} \dfrac{f(x) - f(0)}{x - 0}
      = \lim\limits_{x \to 0} \dfrac{e^{-\frac{1}{x^2}} - 0}{x}
      \xlongequal{t = \frac{1}{x}} \lim\limits_{t \to \infty} \dfrac{t}{e^{t^2}} = 0.

   假设当 :math:`n = k` 时, :math:`f^{(k)}(0) = 0` 成立, 那么当 :math:`n = k + 1` 时, 有

   .. math::
      f^{(k+1)}(0) = \lim\limits_{x \to 0} \dfrac{f^{(k)}(x) - f^{(k)}(0)}{x - 0}
      = \lim\limits_{x \to 0} \dfrac{f^{(k)}(x) - 0}{x}.

   注意到 :math:`f^{(k)}(x)` 是由初等函数通过有限次求导得到的函数, 其中前几项为

   .. math::
      f'(x) & = \dfrac{2}{x^3} e^{-\frac{1}{x^2}}, \\
      f''(x) & = \left( \dfrac{4}{x^6} - \dfrac{6}{x^4} \right) e^{-\frac{1}{x^2}}, \\
      f^{(3)}(x) & = \left( \dfrac{8}{x^9} - \dfrac{36}{x^7} + \dfrac{24}{x^5} \right) e^{-\frac{1}{x^2}}, \\
      \cdots

   因此可以归纳地得到 (用数学归纳法验证), 对任意的正整数 :math:`k`, 有

   .. math::
      f^{(k)}(x) = P_k\left( \dfrac{1}{x} \right) e^{-\frac{1}{x^2}},

   其中 :math:`P_k(t)` 是关于 :math:`t` 的多项式. 验证
   :math:`f^{(k+1)}(x) = P_{k+1}\left( \dfrac{1}{x} \right) e^{-\frac{1}{x^2}}`:

   .. math::
      f^{(k+1)}(x)
      & = \dfrac{\mathrm{d}}{\mathrm{d} x} \left( P_k\left( \dfrac{1}{x} \right) e^{-\frac{1}{x^2}} \right) \\
      & = P_k'\left( \dfrac{1}{x} \right) \cdot \left( -\dfrac{1}{x^2} \right) e^{-\frac{1}{x^2}}
      + P_k\left( \dfrac{1}{x} \right) \cdot \dfrac{2}{x^3} e^{-\frac{1}{x^2}} \\
      & = \left( -\dfrac{1}{x^2} P_k'\left( \dfrac{1}{x} \right)
         + \dfrac{2}{x^3} P_k\left( \dfrac{1}{x} \right) \right) e^{-\frac{1}{x^2}} \\
      & = P_{k+1}\left( \dfrac{1}{x} \right) e^{-\frac{1}{x^2}}.

   这里, :math:`P_{k+1}(t) = -t^2 P_k'(t) + 2t^3 P_k(t)`. 因此

   .. math::
      f^{(k+1)}(0) & = \lim\limits_{x \to 0} \dfrac{P_k\left( \dfrac{1}{x} \right) e^{-\frac{1}{x^2}}}{x}
         \xlongequal{t = \frac{1}{x}} \lim\limits_{t \to \infty} t P_k(t) e^{-t^2} \\
      & = \lim\limits_{t \to \infty} \dfrac{t P_k(t)}{e^{t^2}} = 0.

.. _ex-chap3-sec4:

§3.4 函数的微分
------------------------------------

.. _ex-chap3-sec4-ex1:

1. 求下列函数的微分.

   (1) :math:`y = e^{ax} \sin bx`; \qquad
   (2) :math:`y = \arcsin \sqrt{1 - x}`; \qquad
   (3) :math:`y = \dfrac{x}{1 - x}`.

.. proof:solution::

   (1). :math:`y' = a e^{ax}\sin bx + b e^{ax}\cos bx = e^{ax}(a\sin bx + b\cos bx)`, 故

   .. math::
      \mathrm{d}y = e^{ax}(a\sin bx + b\cos bx) ~ \mathrm{d}x.

   (2). :math:`y' = \dfrac{1}{\sqrt{1-(1-x)}} \cdot \dfrac{-1}{2\sqrt{1-x}} = -\dfrac{1}{2\sqrt{x(1-x)}}`, 故

   .. math::
      \mathrm{d}y = -\dfrac{\mathrm{d}x}{2\sqrt{x(1-x)}}.

   (3). :math:`y' = \dfrac{(1-x) + x}{(1-x)^2} = \dfrac{1}{(1-x)^2}`, 故

   .. math::
      \mathrm{d}y = \dfrac{\mathrm{d}x}{(1-x)^2}.

.. _ex-chap3-sec4-ex2:

2. 求下列函数的微分.

   (1) :math:`y = e^x \ln x`, 求 :math:`\mathrm{d}y`; \qquad
   (2) :math:`y = \cos e^x`, 求 :math:`\mathrm{d}y`.

.. proof:solution::

   (1). :math:`y' = e^x\ln x + e^x \cdot \dfrac{1}{x}`, 故

   .. math::
      \mathrm{d}y = e^x\left( \ln x + \dfrac{1}{x} \right) \mathrm{d}x.

   (2). :math:`y' = -\sin e^x \cdot e^x`, 故 :math:`\mathrm{d}y = -e^x \sin e^x ~ \mathrm{d}x`.

.. _ex-chap3-sec4-ex3:

3. 近似计算.

   (1) :math:`\sqrt{1.02}`; \qquad
   (2) :math:`\ln 2.7`; \qquad
   (3) :math:`\tan 45^\circ 10'`.

.. proof:solution::

   利用微分近似公式 :math:`f(x_0 + \Delta x) \approx f(x_0) + f'(x_0)\Delta x`:

   (1). 取 :math:`f(x) = \sqrt{x}`, :math:`x_0 = 1`, :math:`\Delta x = 0.02`:
   :math:`\sqrt{1.02} \approx 1 + \dfrac{1}{2}\times 0.02 = 1.01`.

   (2). 取 :math:`f(x) = \ln x`, :math:`x_0 = e \approx 2.718`, :math:`\Delta x = 2.7 - e \approx -0.018`:
   :math:`\ln 2.7 \approx 1 + \dfrac{1}{e}(2.7 - e) \approx 1 - 0.0066 = 0.993`.

   (3). :math:`45^\circ 10' = \dfrac{\pi}{4} + \dfrac{10}{60} \cdot \dfrac{\pi}{180} = \dfrac{\pi}{4} + \dfrac{\pi}{540}`.
   取 :math:`f(x) = \tan x`, :math:`x_0 = \dfrac{\pi}{4}`, :math:`\Delta x = \dfrac{\pi}{540} \approx 0.00582`:
   :math:`\tan 45^\circ 10' \approx \tan\dfrac{\pi}{4} + \sec^2\dfrac{\pi}{4} \cdot \dfrac{\pi}{540} = 1 + 2 \times 0.00582 \approx 1.012`.

.. _ex-chap3-zong:

总习题 3
------------------------------------

.. _ex-chap3-zong-ex1:

1. 设 :math:`f(x)` 在 :math:`x = a` 的某邻域中有定义, 则 :math:`f(x)` 在 :math:`x = a` 处可导的一个充分条件是
   (   ).

   A. :math:`\lim\limits_{h \to +\infty} h \left[ f\left( a + \dfrac{1}{h} \right) - f(a) \right]` 存在 \qquad
   B. :math:`\lim\limits_{h \to 0} \dfrac{f(a + 2h) - f(a + h)}{h}` 存在

   C. :math:`\lim\limits_{h \to 0} \dfrac{f(a) - f(a - h)}{h}` 存在 \qquad
   D. :math:`\lim\limits_{h \to 0} \dfrac{f(a + h) - f(a - h)}{2h}` 存在

.. proof:solution::

   选 C. 选项 C 的极限即

   .. math::
      \lim_{h \to 0} \dfrac{f(a) - f(a-h)}{h}
      = \lim_{h \to 0} \dfrac{f(a-h) - f(a)}{-h}
      = f'(a),

   正是导数的定义, 因而是可导的充分条件.

   其余选项都不充分:

   A 中 :math:`h \to +\infty` 时 :math:`\dfrac{1}{h} \to 0^+`, 该极限至多是右导数
   :math:`f'_+(a)` (例如 :math:`f(x) = |x|`, :math:`a = 0` 时它存在但 :math:`f` 在 :math:`0` 不可导);

   B 的极限式中不出现 :math:`f(a)`, 例如 :math:`f(x) = \begin{cases} x, & x \neq 0, \\ 1, & x = 0 \end{cases}`
   在 :math:`a = 0` 处不连续, 但该极限存在 (值为 :math:`1`);

   D 中对称差商存在不足以保证可导, 例如 :math:`f(x) = |x|` 在 :math:`a = 0` 处,
   :math:`\dfrac{|h| - |-h|}{2h} = 0` 极限存在, 但 :math:`f(x)` 在 :math:`0` 处不可导.

.. _ex-chap3-zong-ex2:

2. 分段函数 :math:`f(x) = \begin{cases} x + \sin x^2, & x \leqslant 0, \\ \ln(1 + x), & x > 0, \end{cases}`
   在 :math:`x = 0` 处, 以下说法正确的是 (   ).

   A. 可导且 :math:`f'(0) = 1` \qquad B. 可导不连续

   C. 连续不可导 \qquad D. 既不连续也不可导

.. proof:solution::

   选 A. :math:`f(0) = 0`, 右极限 :math:`\lim\limits_{x \to 0^+} \ln(1+x) = 0 = f(0)`, 连续. 左导数

   .. math::
      f'_-(0) = \lim_{x \to 0^-} \dfrac{x + \sin x^2}{x} = \lim_{x \to 0^-} \left( 1 + \dfrac{\sin x^2}{x} \right)
      = 1 + \lim_{x \to 0^-} \dfrac{x^2}{x} = 1,

   右导数 :math:`f'_+(0) = \lim\limits_{x \to 0^+} \dfrac{\ln(1+x)}{x} = 1`. 左右导数相等, 故 :math:`f'(0) = 1`, 可导.

.. _ex-chap3-zong-ex3:

3. 函数 :math:`f(x) = \begin{cases} x \sin \dfrac{1}{x}, & x \neq 0, \\ 0, & x = 0, \end{cases}`
   则 :math:`f(x)` 在 :math:`x = 0` 处 (   ).

   A. 可导且连续 \qquad B. 可导但不连续

   C. 不可导也不连续 \qquad D. 不可导但连续

.. proof:solution::

   选 D. 由 :math:`\left| x\sin\dfrac{1}{x} \right| \leqslant |x| \to 0` 得 :math:`\lim\limits_{x \to 0} f(x) = 0 = f(0)`,
   故连续. 但

   .. math::
      \lim_{x \to 0} \dfrac{f(x) - f(0)}{x} = \lim_{x \to 0} \sin\dfrac{1}{x}

   不存在 (在 :math:`-1` 与 :math:`1` 之间振荡), 故 :math:`f(x)` 在 :math:`x = 0` 处不可导.

.. _ex-chap3-zong-ex4:

4. 设 :math:`f(x)` 在 :math:`x = 0` 的某个邻域内连续, :math:`f(0) = 0`,
   :math:`\lim\limits_{x \to 0} \dfrac{f(x)}{2 \sin^2 \dfrac{x}{2}} = 1`, 则 :math:`f(x)` 在 :math:`x = 0` 处
   (   ).

   A. 不可导 \qquad B. 可导且 :math:`f'(0) = 0`

   C. 可导且 :math:`f'(0) = 1` \qquad D. 可导且 :math:`f'(0) = 2`

.. proof:solution::

   选 B. 注意 :math:`2\sin^2\dfrac{x}{2} = 1 - \cos x \sim \dfrac{x^2}{2}` (:math:`x \to 0`). 由 :math:`f(0) = 0`,

   .. math::
      f'(0) = \lim_{x \to 0} \dfrac{f(x)}{x}
      = \lim_{x \to 0} \left[ \dfrac{f(x)}{2\sin^2 \frac{x}{2}} \cdot \dfrac{2\sin^2 \frac{x}{2}}{x} \right]
      = 1 \cdot \lim_{x \to 0} \dfrac{x^2/2}{x}
      = \lim_{x \to 0} \dfrac{x}{2} = 0.

   故 :math:`f(x)` 在 :math:`x = 0` 处可导且 :math:`f'(0) = 0`.

.. _ex-chap3-zong-ex5:

5. 已知函数 :math:`f(x)` 在区间 :math:`(0, 1)` 内可导, 则以下结论正确的是 (   ).

   A. :math:`f(x)` 在 :math:`x = 0` 处一定连续 \qquad B. :math:`f(x)` 在 :math:`x = 0` 处右导数一定存在

   C. :math:`f(x)` 在 :math:`x = 0.5` 处一定可微 \qquad D. :math:`f(x)` 在 :math:`x = 1` 处一定可导

.. proof:solution::

   选 C. 可导必可微, 而 :math:`x = 0.5` 是区间 :math:`(0, 1)` 的内点, :math:`f(x)` 在该点可导, 因而一定可微.

   A 与 B 都不成立: 可导性只在开区间内部保证, 对端点没有任何保证. 例如 :math:`f(x) = \dfrac{1}{x}` 在
   :math:`(0, 1)` 内可导, 但 :math:`x \to 0^+` 时 :math:`f(x) \to +\infty`, 在 :math:`x = 0` 处既不连续
   (无论如何补充定义) 也无右导数. D 同理不成立: 例如 :math:`f(x) = \dfrac{1}{x-1}` 在 :math:`(0,1)` 内可导,
   但 :math:`x \to 1^-` 时 :math:`f(x) \to -\infty`, 在 :math:`x = 1` 处不可能可导.

.. _ex-chap3-zong-ex6:

6. 求下列函数的导数.

   (1) :math:`y = 2x^3 - 3x^2 + 6x`; \qquad
   (2) :math:`y = x \ln x`;

   (3) :math:`y = \dfrac{\ln x}{\sqrt{x}}`; \qquad
   (4) :math:`y = \arctan \dfrac{1}{1 + x}`.

.. proof:solution::

   (1). :math:`y' = 6x^2 - 6x + 6`.

   (2). :math:`y' = \ln x + x \cdot \dfrac{1}{x} = \ln x + 1`.

   (3). :math:`y' = \dfrac{\frac{1}{x}\cdot\sqrt{x} - \ln x \cdot \frac{1}{2\sqrt{x}}}{x}
   = \dfrac{1}{\sqrt{x}} \cdot \dfrac{1 - \frac{1}{2}\ln x}{x}
   = \dfrac{2 - \ln x}{2x^{\frac{3}{2}}}`.

   (4). :math:`y' = \dfrac{1}{1 + \frac{1}{(1+x)^2}} \cdot \left( -\dfrac{1}{(1+x)^2} \right)
   = -\dfrac{1}{(1+x)^2 + 1} = -\dfrac{1}{x^2 + 2x + 2}`.

.. _ex-chap3-zong-ex7:

7. 求下列函数的二阶导数.

   (1) :math:`y = \dfrac{e^x}{x}`; \qquad
   (2) :math:`y = \ln \left( x + \sqrt{1 + x^2} \right)`.

.. proof:solution::

   (1). :math:`y' = \dfrac{e^x x - e^x}{x^2} = \dfrac{e^x(x-1)}{x^2}`, 故

   .. math::
      y'' = \dfrac{\left[ e^x(x-1) + e^x \right] x^2 - e^x(x-1) \cdot 2x}{x^4}
      = \dfrac{e^x x^2 - 2e^x(x-1)}{x^3}
      = \dfrac{e^x (x^2 - 2x + 2)}{x^3}.

   (2). :math:`y' = \dfrac{1 + \frac{x}{\sqrt{1+x^2}}}{x + \sqrt{1+x^2}} = \dfrac{1}{\sqrt{1+x^2}}`, 故

   .. math::
      y'' = -\dfrac{1}{2}(1+x^2)^{-\frac{3}{2}} \cdot 2x = -\dfrac{x}{(1+x^2)^{\frac{3}{2}}}.

.. _ex-chap3-zong-ex8:

8. 求下列函数的 :math:`n` 阶导数.

   (1) :math:`y = \left( \sin \dfrac{x}{2} - \cos \dfrac{x}{2} \right)^2`; \qquad
   (2) :math:`y = \dfrac{\ln x}{x}`.

.. proof:solution::

   (1). 先化简:

   .. math::
      y = \sin^2 \dfrac{x}{2} - 2\sin\dfrac{x}{2}\cos\dfrac{x}{2} + \cos^2\dfrac{x}{2}
      = 1 - \sin x.

   由 :math:`(\sin x)^{(n)} = \sin\left( x + \dfrac{n\pi}{2} \right)`, 得

   .. math::
      y^{(n)} = -\sin\left( x + \dfrac{n\pi}{2} \right) \qquad (n \geqslant 1).

   (2). 由莱布尼茨公式 (:math:`u = \ln x`, :math:`v = x^{-1}`), 注意
   :math:`(\ln x)^{(k)} = \dfrac{(-1)^{k-1}(k-1)!}{x^k}` (:math:`k \geqslant 1`),
   :math:`(x^{-1})^{(m)} = \dfrac{(-1)^m m!}{x^{m+1}}`:

   .. math::
      y^{(n)} & = (x^{-1})^{(n)} \ln x + \sum_{k=1}^{n} C_n^k (x^{-1})^{(n-k)} (\ln x)^{(k)} \\
      & = \dfrac{(-1)^n n!}{x^{n+1}} \ln x
        + \sum_{k=1}^{n} \dfrac{n!}{k!(n-k)!} \cdot \dfrac{(-1)^{n-k}(n-k)!}{x^{n-k+1}} \cdot \dfrac{(-1)^{k-1}(k-1)!}{x^k} \\
      & = \dfrac{(-1)^n n!}{x^{n+1}} \ln x
        + \dfrac{(-1)^{n-1} n!}{x^{n+1}} \sum_{k=1}^{n} \dfrac{1}{k} \\
      & = \dfrac{(-1)^{n-1} n!}{x^{n+1}} \left( \sum_{k=1}^{n} \dfrac{1}{k} - \ln x \right).

   (验证: :math:`n=1` 时得 :math:`\dfrac{1-\ln x}{x^2}`, :math:`n=2` 时得 :math:`\dfrac{2\ln x - 3}{x^3}`, 与直接求导一致.)

.. _extra-chap3:

补充内容
====================================

.. _extra-chap3-sec1:

§3.1 导数的概念
------------------------------------

.. _extra-chap3-sec1-topic1:

1. 处处连续, 但处处不可导的函数: Generalized Van der Waerden-Takagi 函数.

   该函数定义如下

   .. math::
      & \varphi(x) = d(x, \mathbb{Z}) = \min_{n \in \mathbb{Z}} |x - n|, \quad x \in \mathbb{R}, \\
      & f(x) = \sum_{n=0}^{\infty} a^n \varphi(b^n x).

   当 :math:`0 < a < 1`, :math:`b \in \mathbb{N}_{\geqslant 2}`, 且 :math:`ab \geqslant 1` 时,
   :math:`f(x)` 是一个在 :math:`\mathbb{R}` 上处处不可导的连续函数.

   那么, 处处可导, 但导函数处处不连续的函数是否存在呢? 答案是不存在.

.. _extra-chap3-sec3:

§3.3 高阶导数
--------------------------------

.. _extra-chap3-sec3-topic1:

1. 莱布尼茨公式 :math:`(uv)^{(n)} = \sum\limits_{k=0}^n C_n^k u^{(k)} v^{(n-k)}` 的证明:

.. proof:proof::

   用数学归纳法证明. 当 :math:`n = 1` 时, :math:`(uv)' = u'v + uv'`, 成立.

   假设当 :math:`n = k` 时, :math:`(uv)^{(k)} = \sum\limits_{i=0}^k C_k^i u^{(i)} v^{(k-i)}` 成立, 那么 :math:`n = k + 1` 时有

   .. math::
      (uv)^{(k + 1)} & = \dfrac{\mathrm{d}}{\mathrm{d} x} \left( \sum\limits_{i=0}^k C_k^i u^{(i)} v^{(k-i)} \right) \\
                     & = \sum\limits_{i=0}^k C_k^i \dfrac{\mathrm{d}}{\mathrm{d} x} \left( u^{(i)} v^{(k-i)} \right) \\
                     & = \sum\limits_{i=0}^k C_k^i \left( u^{(i+1)} v^{(k-i)} + u^{(i)} v^{(k-i+1)} \right) \\
                     & = \sum\limits_{i=0}^k C_k^i u^{(i+1)} v^{(k-i)} + \sum\limits_{i=0}^k C_k^i u^{(i)} v^{(k-i+1)} \\
                     & = \sum\limits_{i=1}^{k+1} C_k^{i-1} u^{(i)} v^{(k-i+1)} + \sum\limits_{i=0}^k C_k^i u^{(i)} v^{(k-i+1)} \\
                     & = u^{(k+1)} v + \sum\limits_{i=1}^k \left( C_k^{i-1} + C_k^i \right) u^{(i)} v^{(k-i+1)} + u v^{(k+1)} \\
                     & = u^{(k+1)} v + \sum\limits_{i=1}^k C_{k+1}^i u^{(i)} v^{(k-i+1)} + u v^{(k+1)} \\
                     & = C_{k+1}^{k+1} u^{(k+1)} v + \sum\limits_{i=0}^k C_{k+1}^i u^{(i)} v^{(k-i+1)} + C_{k+1}^0 u v^{(k+1)} \\
                     & = \sum\limits_{i=0}^{k+1} C_{k+1}^i u^{(i)} v^{((k+1)-i)}

   于是当 :math:`n = k + 1` 时, :math:`(uv)^{(n)} = \sum\limits_{i=0}^n C_n^i u^{(i)} v^{(n-i)}` 成立. 根据数学归纳法原理,
   对于任意的 :math:`n \in \mathbb{N}`, :math:`(uv)^{(n)} = \sum\limits_{i=0}^n C_n^i u^{(i)} v^{(n-i)}` 成立.
