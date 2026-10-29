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

   待写.

.. _ex-chap3-sec1-ex2:

2. 设函数 :math:`f(x) = ax + 4`, 若 :math:`f'(1) = 2`, 则 :math:`a =` (   ).

   A. :math:`2` \qquad B. :math:`-2` \qquad C. :math:`3` \qquad D. 不确定

.. proof:solution::

   待写.

.. _ex-chap3-sec1-ex3:

3. 设 :math:`f(x)` 在 :math:`x_0` 处可导, 求下列极限值.

   (1) :math:`\lim\limits_{h \to 0} \dfrac{f(x_0) - f(x_0 - h)}{h}`;

   (2) :math:`\lim\limits_{\Delta x \to 0} \dfrac{f(x_0 + 2\Delta x) - f(x_0 - \Delta x)}{\Delta x}`.

.. proof:solution::

   (1). 待写.

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

   待写.

.. _ex-chap3-sec1-ex5:

5. 求下列函数的导数.

   (1) :math:`y = x^5`; \qquad
   (2) :math:`y = \sqrt{x^3}`; \qquad
   (3) :math:`y = \dfrac{1}{x^3}`;

   (4) :math:`y = \dfrac{1}{\sqrt[3]{x}}`; \qquad
   (5) :math:`y = x^2 \sqrt{x}`; \qquad
   (6) :math:`y = 2^x`.

.. proof:solution::

   待写.

.. _ex-chap3-sec1-ex6:

6. 设 :math:`f(x)` 是定义在 :math:`(-a, a)` 上的奇函数, 若 :math:`f(x)` 可导, 证明 :math:`f'(x)` 是偶函数.

.. proof:solution::

   待写.

.. _ex-chap3-sec1-ex7:

7. 求曲线 :math:`y = \sin x` 在点 :math:`\left( \dfrac{\pi}{4}, \dfrac{\sqrt{2}}{2} \right)` 处的切线方程和法线方程.

.. proof:solution::

   待写.

.. _ex-chap3-sec1-ex8:

8. 求曲线 :math:`y = \ln x` 在点 :math:`(1, 0)` 处的切线方程和法线方程.

.. proof:solution::

   待写.

.. _ex-chap3-sec1-ex9:

9. 求曲线 :math:`y = e^x` 上斜率为 :math:`e` 的切线方程.

.. proof:solution::

   待写.

.. _ex-chap3-sec1-ex10:

10. 若曲线 :math:`y = x^{-\frac{1}{2}}` 在点 :math:`\left( a, a^{-\frac{1}{2}} \right)` (其中 :math:`a > 0`)
    处的切线与两个坐标围成的三角形的面积为 :math:`18`, 求 :math:`a` 的值.

.. proof:solution::

   待写.

.. _ex-chap3-sec1-ex11:

11. 讨论 :math:`f(x) = \begin{cases} 0, & x = 0, \\ x^2 \sin \dfrac{1}{x}, & x \neq 0 \end{cases}`
    的连续性与可导性.

.. proof:solution::

   待写.

.. _ex-chap3-sec1-ex12:

12. 求下列函数在 :math:`x = 0` 处的左导数、右导数, 并判断函数在 :math:`x = 0` 处是否可导.

   (1) :math:`f(x) = \begin{cases} \cos x, & x > 0, \\ e^x, & x \leqslant 0; \end{cases}` \qquad
   (2) :math:`f(x) = \begin{cases} x, & x > 0, \\ x^3, & x \leqslant 0. \end{cases}`

.. proof:solution::

   待写.

.. _ex-chap3-sec1-ex13:

13. 讨论 :math:`f(x) = \lvert x \rvert^3` 在 :math:`x = 0` 处的可导性.

.. proof:solution::

   待写.

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

   待写.

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

   待写.

.. _ex-chap3-sec2-ex2:

2. 由方程 :math:`y \sin x + e^y - x = 1` 确定变量 :math:`y` 为 :math:`x` 的函数, 求导数
   :math:`y' \bigr|_{x=0}`.

.. proof:solution::

   待写.

.. _ex-chap3-sec2-ex3:

3. 求曲线 :math:`xy + \ln y = 1` 在点 :math:`P(1, 1)` 处的切线方程与法线方程.

.. proof:solution::

   待写.

.. _ex-chap3-sec2-ex4:

4. 求下列由参数方程所确定的函数的导数 :math:`\dfrac{\mathrm{d}y}{\mathrm{d}x}`.

   (1) :math:`\begin{cases} x = \cos^4 t, \\ y = \sin^4 t, \end{cases}` 在 :math:`t = 0`, :math:`\dfrac{\pi}{4}` 处;

   (2) :math:`\begin{cases} x = \dfrac{t}{1 + t}, \\ y = \dfrac{1 - t}{1 + t}, \end{cases}` 在 :math:`t = 0` 处.

.. proof:solution::

   待写.

.. _ex-chap3-sec2-ex5:

5. 求下列函数在给定点处的导数.

   (1) :math:`y = 2 \sin x - \cos x`, 求 :math:`y' \bigr|_{x = \frac{\pi}{6}}` 和
       :math:`y' \bigr|_{x = \frac{\pi}{4}}`;

   (2) :math:`\rho = \theta \sin \theta + \dfrac{1}{2} \cos \theta`, 求
       :math:`\dfrac{\mathrm{d}\rho}{\mathrm{d}\theta} \bigr|_{\theta = \frac{\pi}{4}}`;

   (3) :math:`f(x) = \dfrac{1}{4 - x} + \dfrac{x^2}{5}`, 求 :math:`f'(0)` 和 :math:`f'(1)`.

.. proof:solution::

   待写.

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

   待写.

.. _ex-chap3-sec2-ex7:

7. 求曲线 :math:`y = 2 \cos x + x^2` 在横坐标为 :math:`x = 0` 的点处的切线方程和法线方程.

.. proof:solution::

   待写.

.. _ex-chap3-sec2-ex8:

8. 求由下列方程所确定的隐函数的导数.

   (1) :math:`y^2 - 2xy + 9 = 0`; \qquad
   (2) :math:`x^3 + y^3 - 3xy = 0`;

   (3) :math:`xy = e^{x+y}`; \qquad
   (4) :math:`y = 1 - xe^y`.

.. proof:solution::

   待写.

.. _ex-chap3-sec2-ex9:

9. 用对数求导法求下列函数的导数.

   (1) :math:`y = \left( \dfrac{x}{1 + x} \right)^x`;

   (2) :math:`y = \sqrt[5]{\dfrac{x - 5}{\sqrt[5]{x^2 + 2}}}`;

   (3) :math:`y = \dfrac{\sqrt{x+1} (3 - x)^4}{(x + 1)^5}`;

   (4) :math:`y = \sqrt{x \sin x \sqrt{1 - e^x}}`.

.. proof:solution::

   待写.

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

   待写.

.. _ex-chap3-sec3-ex2:

2. 已知 :math:`f(x)` 任意次可导, 求下列复合函数的高阶导数.

   (1) :math:`y = e^{f(x)}`, 求 :math:`y''`;

   (2) :math:`y = f(x^2)`, 求 :math:`y''`;

   (3) :math:`y = f(e^{-x})`, 求 :math:`y''`;

   (4) :math:`y = \ln f(x)`, 求 :math:`y''`.

.. proof:solution::

   待写.

.. _ex-chap3-sec3-ex3:

3. 设 :math:`y = e^x \sin x`, 利用莱布尼茨法则计算 :math:`y^{(n)}`.

.. proof:solution::

   待写.

.. _ex-chap3-sec3-ex4:

4. 对下列隐函数求二阶导数.

   (1) :math:`2y + \sin y = x^2`; \qquad
   (2) :math:`x^3 + y^3 - 3xy = 0`.

.. proof:solution::

   待写.

.. _ex-chap3-sec3-ex5:

5. 求下列参数形式的函数的二阶导数.

   (1) :math:`\begin{cases} x = at^2, \\ y = bt^3; \end{cases}` \qquad
   (2) :math:`\begin{cases} x = \sqrt{1 + t}, \\ y = \sqrt{1 - t}; \end{cases}` \qquad
   (3) :math:`\begin{cases} x = \sin t, \\ y = \cos t. \end{cases}`

.. proof:solution::

   待写.

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

   待写.

.. _ex-chap3-sec4-ex2:

2. 求下列函数的微分.

   (1) :math:`y = e^x \ln x`, 求 :math:`\mathrm{d}y`; \qquad
   (2) :math:`y = \cos e^x`, 求 :math:`\mathrm{d}y`.

.. proof:solution::

   待写.

.. _ex-chap3-sec4-ex3:

3. 近似计算.

   (1) :math:`\sqrt{1.02}`; \qquad
   (2) :math:`\ln 2.7`; \qquad
   (3) :math:`\tan 45^\circ 10'`.

.. proof:solution::

   待写.

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

   待写.

.. _ex-chap3-zong-ex2:

2. 分段函数 :math:`f(x) = \begin{cases} x + \sin x^2, & x \leqslant 0, \\ \ln(1 + x), & x > 0, \end{cases}`
   在 :math:`x = 0` 处, 以下说法正确的是 (   ).

   A. 可导且 :math:`f'(0) = 1` \qquad B. 可导不连续

   C. 连续不可导 \qquad D. 既不连续也不可导

.. proof:solution::

   待写.

.. _ex-chap3-zong-ex3:

3. 函数 :math:`f(x) = \begin{cases} x \sin \dfrac{1}{x}, & x \neq 0, \\ 0, & x = 0, \end{cases}`
   则 :math:`f(x)` 在 :math:`x = 0` 处 (   ).

   A. 可导且连续 \qquad B. 可导但不连续

   C. 不可导也不连续 \qquad D. 不可导但连续

.. proof:solution::

   待写.

.. _ex-chap3-zong-ex4:

4. 设 :math:`f(x)` 在 :math:`x = 0` 的某个邻域内连续, :math:`f(0) = 0`,
   :math:`\lim\limits_{x \to 0} \dfrac{f(x)}{2 \sin^2 \dfrac{x}{2}} = 1`, 则 :math:`f(x)` 在 :math:`x = 0` 处
   (   ).

   A. 不可导 \qquad B. 可导且 :math:`f'(0) = 0`

   C. 可导且 :math:`f'(0) = 1` \qquad D. 可导且 :math:`f'(0) = 2`

.. proof:solution::

   待写.

.. _ex-chap3-zong-ex5:

5. 已知函数 :math:`f(x)` 在区间 :math:`(0, 1)` 内可导, 则以下结论正确的是 (   ).

   A. :math:`f(x)` 在 :math:`x = 0` 处一定连续 \qquad B. :math:`f(x)` 在 :math:`x = 0` 处右导数一定存在

   C. :math:`f(x)` 在 :math:`x = 0.5` 处一定可微 \qquad D. :math:`f(x)` 在 :math:`x = 1` 处一定可导

.. proof:solution::

   待写.

.. _ex-chap3-zong-ex6:

6. 求下列函数的导数.

   (1) :math:`y = 2x^3 - 3x^2 + 6x`; \qquad
   (2) :math:`y = x \ln x`;

   (3) :math:`y = \dfrac{\ln x}{\sqrt{x}}`; \qquad
   (4) :math:`y = \arctan \dfrac{1}{1 + x}`.

.. proof:solution::

   待写.

.. _ex-chap3-zong-ex7:

7. 求下列函数的二阶导数.

   (1) :math:`y = \dfrac{e^x}{x}`; \qquad
   (2) :math:`y = \ln \left( x + \sqrt{1 + x^2} \right)`.

.. proof:solution::

   待写.

.. _ex-chap3-zong-ex8:

8. 求下列函数的 :math:`n` 阶导数.

   (1) :math:`y = \left( \sin \dfrac{x}{2} - \cos \dfrac{x}{2} \right)^2`; \qquad
   (2) :math:`y = \dfrac{\ln x}{x}`.

.. proof:solution::

   待写.

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
