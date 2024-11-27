第二章  导数与微分
^^^^^^^^^^^^^^^^^^^^^^^^^

.. contents:: :local:


课后习题解答
=================

§2.1 函数的导数
--------------------------------

2. 设 :math:`f(x) = ax^2 + bx + c`, 用定义求 :math:`f'(x)`.

.. proof:solution::

   .. math::

      f'(x) &= \lim_{\Delta x \to 0} \frac{f(x + \Delta x) - f(x)}{\Delta x} \\
            &= \lim_{\Delta x \to 0} \frac{a(x + \Delta x)^2 + b(x + \Delta x) + c - (ax^2 + bx + c)}{\Delta x} \\
            &= \lim_{\Delta x \to 0} \frac{a(x^2 + 2x\Delta x + \Delta x^2) + bx + b\Delta x + c - ax^2 - bx - c}{\Delta x} \\
            &= \lim_{\Delta x \to 0} \frac{2ax\Delta x + a\Delta x^2 + b\Delta x}{\Delta x} \\
            &= \lim_{\Delta x \to 0} 2ax + a\Delta x + b \\
            &= 2ax + b

4. 求曲线 :math:`y = 2^x` 在点 :math:`(1, 2)` 处的切线方程和法线方程.

.. proof:solution::

   :math:`y = 2^x` 的导函数为 :math:`y' = 2^x \ln 2`, 所以在点 :math:`(1, 2)` 处切线斜率, 即该点处的导数值为 :math:`y'|_{x=1} = 2 \ln 2`.
   所以切线方程为 :math:`y - 2 = 2 \ln 2 (x - 1)`, 即 :math:`y = 2 \ln 2 x - 2 \ln 2 + 2`.

   法线的斜率为 :math:`-\frac{1}{2 \ln 2}`, 所以法线方程为 :math:`y - 2 = -\frac{1}{2 \ln 2} (x - 1)`, 即 :math:`y = -\frac{1}{2 \ln 2} x + \frac{1}{2 \ln 2} + 2`.

5. 函数 :math:`f(x) = \begin{cases} a \sin x, & x \leqslant 0 \\ e^x + b, & x > 0 \end{cases}` 可导, 求 :math:`a, b`.

.. proof:solution::

   :math:`f(x)` 在 :math:`x = 0` 处可导, 所以 :math:`f(x)` 在 :math:`x = 0` 处连续, 即 :math:`a \sin 0 = e^0 + b`, 解得 :math:`b = -1`.

   :math:`f'_{-}(0) = a \cos 0 = a`, :math:`f'_{+}(0) = e^0 = 1`, 所以 :math:`a = 1`.

6. 已知函数可导, 将下列极限用导数表示出来:

   (3). 设 :math:`f(0) = 0`, 求 :math:`\lim_{h \to 0} \frac{f(h)}{h}`.

.. proof:solution::

   .. math::

      \lim_{h \to 0} \frac{f(h)}{h} = \lim_{h \to 0} \frac{f(h) - f(0)}{h - 0} = f'(0)

7. 讨论函数在 :math:`x = 0` 处的可导性:

   (2). :math:`f(x) = \begin{cases} x^2 \cos \dfrac{1}{x}, & x \ne 0 \\ 0, & x = 0 \end{cases}`.

.. proof:solution::

   首先, :math:`f(x)` 在 :math:`x = 0` 处连续, 因为 :math:`\lim\limits_{x \to 0} f(x) = \lim\limits_{x \to 0} x^2 \cos \dfrac{1}{x} = 0 = f(0)`.
   接下来考虑 :math:`f(x)` 在 :math:`x = 0` 处的左右导数是否相等:

   .. math::

      f'_{-}(0) &= \lim_{h \to 0^{-}} \dfrac{f(0 + h) - f(0)}{h} = \lim_{h \to 0^{-}} \dfrac{h^2 \cos \dfrac{1}{h}}{h} \\
               &= \lim_{h \to 0^{-}} h \cos \dfrac{1}{h} \\
               &= 0

   .. math::

      f'_{+}(0) &= \lim_{h \to 0^{+}} \dfrac{f(0 + h) - f(0)}{h} = \lim_{h \to 0^{+}} \dfrac{h^2 \cos \dfrac{1}{h}}{h} \\
               &= \lim_{h \to 0^{+}} h \cos \dfrac{1}{h} \\
               &= 0

   所以 :math:`f'(0) = 0`, :math:`f(x)` 在 :math:`x = 0` 处可导.

§2.2 函数的求导法则
--------------------------------

1. 求下列函数的导数:

   (2). :math:`y = x^5 \left( \dfrac{1}{x} + \sqrt{x} \right)`; (4) :math:`y = (1 + \tan x) \ln x`;

   (6). :math:`y = e^x (x^3 - 3x^2 + 6x - 6)`; (8). :math:`y = \dfrac{\cos x}{1 + \ln x}`;

   (10). :math:`y = \dfrac{1 + \ln x}{x^2}`; (12). :math:`y = \dfrac{1 - x}{1 + x}`;

   (14). :math:`y = \dfrac{2\sec x}{1 + x^2}`.

.. proof:solution::

   (2).

   .. math::

      y' &= 5x^4 \left( \dfrac{1}{x} + \sqrt{x} \right) + x^5 \left( -\dfrac{1}{x^2} + \dfrac{1}{2 \sqrt{x}} \right) \\
         &= 5x^3 + 5x^{9/2} - x^3 + \dfrac{1}{2} x^{9/2} \\
         &= 4x^3 + \dfrac{11}{2} x^{9/2}

   (4).

   .. math::

      y' = \dfrac{1}{\cos^2 x} \ln x + (1 + \tan x) \cdot \dfrac{1}{x}

   (6).

   .. math::

      y' = e^x (x^3 - 3x^2 + 6x - 6) + e^x (3x^2 - 6x + 6) = e^x x^3

   (8).

   .. math::

      y' = \dfrac{-\sin x}{1 + \ln x} - \dfrac{\cos x}{(1 + \ln x)^2} \cdot \dfrac{1}{x} = - \dfrac{\cos x + x \sin x (1 + \ln x)}{x(1 + \ln x)^2}

   (10).

   .. math::

      y' = \dfrac{\dfrac{1}{x} \cdot x^2 - (1 + \ln x) \cdot 2x}{x^4} = \dfrac{1 - 2 - 2 \ln x}{x^3} = - \dfrac{2 \ln x + 1}{x^3}

   (12).

   .. math::

      y' = \dfrac{-1 \cdot (1 + x) - (1 - x) \cdot 1}{(1 + x)^2} = - \dfrac{2}{(1 + x)^2}

   (14).

   .. math::

      y' = \dfrac{2 (\sec x \tan x) \cdot (1 + x^2) - 2 \sec x \cdot 2x}{(1 + x^2)^2} = 2 \sec x \left( \dfrac{(1 + x^2) \tan x - 2x}{(1 + x^2)^2} \right)

2. 求函数在给定点的导数

   (1). :math:`y = \sin x + \cos x`, 求 :math:`y'|_{x = \frac{\pi}{4}}`;

   (3). :math:`y = \dfrac{x + \sqrt{x}}{1 + \sqrt{x}}`, 求 :math:`y'|_{x = 1}`;

   (5). 设 :math:`\varphi(x)` 是连续函数, :math:`f(x) = (1 - x^2) \varphi(x)`, 求 :math:`f'(1)`.

.. proof:solution::

   (1). :math:`y' = \cos x - \sin x`, 所以 :math:`y'|_{x = \frac{\pi}{4}} = \cos \frac{\pi}{4} - \sin \frac{\pi}{4} = \frac{\sqrt{2}}{2} - \frac{\sqrt{2}}{2} = 0`.

   (3). :math:`y' = \left( \dfrac{\sqrt{x} (1 + \sqrt{x})}{1 + \sqrt{x}} \right)' = \left( \sqrt{x} \right)' = \dfrac{1}{2 \sqrt{x}}`, 所以 :math:`y'|_{x = 1} = \dfrac{1}{2}`.

   (5). 由于 :math:`\varphi` 只是连续函数, 不知道是否可导, 所以需要用定义求 :math:`f(x) = (1 - x^2) \varphi(x)` 的导数

   .. math::

      f'(x) & = \lim_{\Delta x \to 0} \dfrac{f(x + \Delta x) - f(x)}{\Delta x} \\
            & = \lim_{\Delta x \to 0} \dfrac{(1 - (x + \Delta x)^2) \varphi(x + \Delta x) - (1 - x^2) \varphi(x)}{\Delta x} \\
            & = \lim_{\Delta x \to 0} \dfrac{(1 - x^2 - 2x \Delta x - \Delta x^2) \varphi(x + \Delta x) - (1 - x^2) \varphi(x)}{\Delta x} \\
            & = \lim_{\Delta x \to 0} \dfrac{(1 - x^2) \varphi(x + \Delta x) - (1 - x^2) \varphi(x) - 2x \Delta x \varphi(x + \Delta x) - \Delta x^2 \varphi(x + \Delta x)}{\Delta x} \\
            & = \lim_{\Delta x \to 0} \dfrac{(1 - x^2) (\varphi(x + \Delta x) - \varphi(x))}{\Delta x} - \lim_{\Delta x \to 0} 2x \varphi(x + \Delta x) - \lim_{\Delta x \to 0} \Delta x \varphi(x + \Delta x) \\
            & = \lim_{\Delta x \to 0} \dfrac{(1 - x^2) (\varphi(x + \Delta x) - \varphi(x))}{\Delta x} - 2x \varphi(x) - 0 \\

   上式代 :math:`x = 1` 有 :math:`f'(1) = \lim\limits_{\Delta x \to 0} 0 - 2 \cdot 1 \cdot \varphi(1) = -2 \varphi(1)`.

3. 求曲线 :math:`y = x - \dfrac{1}{x}` 在与坐标轴交点处的切线方程和法线方程.

.. proof:solution::

   先求曲线与坐标轴交点. 由于曲线在 :math:`x = 0` 处无定义, 即与 :math:`y` 轴无交点, 所以只需求 :math:`x` 轴交点. 曲线与 :math:`x` 轴交点为 :math:`x - \dfrac{1}{x} = 0`,
   解得 :math:`x = \pm 1`, 所以曲线与坐标轴交点为 :math:`(-1, 0)` 和 :math:`(1, 0)`.

   曲线 :math:`y = x - \dfrac{1}{x}` 的导函数为 :math:`y' = 1 + \dfrac{1}{x^2}`, 所以在点 :math:`(-1, 0)` 处切线斜率, 即该点处的导数值为 :math:`y'|_{x=-1} = 1 + \dfrac{1}{(-1)^2} = 2`,
   所以切线方程为 :math:`y - 0 = 2 (x + 1)`, 即 :math:`y = 2x + 2`; 法线的斜率为 :math:`-\dfrac{1}{2}`, 所以法线方程为 :math:`y - 0 = -\dfrac{1}{2} (x + 1)`,
   即 :math:`y = -\dfrac{1}{2} x - \dfrac{1}{2}`. 类似可求得曲线在点 :math:`(1, 0)` 处的切线方程为 :math:`y = 2x - 2`, 法线方程为 :math:`y = -\dfrac{1}{2} x + \dfrac{1}{2}`.

4. 求下列函数的导数:

   (2). :math:`y = \sin x^5`; (4). :math:`y = e^{\cos 2x}`;

   (6). :math:`y = \sin (nx) \sin^n x`; (8). :math:`y = \arctan \dfrac{1 + x}{1 - x}`.

.. proof:solution::

   (2). :math:`y' = \cos x^5 \cdot 5x^4`.

   (4). :math:`y' = e^{\cos 2x} \cdot (-\sin 2x) \cdot 2 = -2 e^{\cos 2x} \sin 2x`.

   (6).

   .. math::

      y' & = n \cos (nx) \sin^n x + \sin (nx) \cdot n \sin^{n-1} x \cdot \cos x \\
         & = n \sin^{n-1} x (\cos (nx) \sin x + \sin (nx) \cos x) \\
         & = n \sin^{n-1} x \sin (nx + x).

   (8). :math:`y' = \dfrac{1}{1 + \left( \dfrac{1 + x}{1 - x} \right)^2} \cdot \dfrac{(1 - x) + (1 + x)}{(1 - x)^2} = \dfrac{2}{(1 - x)^2 + (1 + x)^2} = \dfrac{1}{1 + x^2}`.

§2.3 高阶导数
--------------------------------

1. 求下列函数的二阶导数:

   (2). :math:`y = \ln (x + \sqrt{x^2 + 4})`;

   (4). :math:`y = \ln (x^2 + 1)`;

   (6). :math:`y = \sin 2x`.

.. proof:solution::

   (2).

   .. math::

      y' & = \dfrac{1}{x + \sqrt{x^2 + 4}} \cdot (1 + \dfrac{1}{2 \sqrt{x^2 + 4}} \cdot 2x)
           = \dfrac{1}{x + \sqrt{x^2 + 4}} \cdot \dfrac{x + \sqrt{x^2 + 4}}{\sqrt{x^2 + 4}} = \dfrac{1}{\sqrt{x^2 + 4}} \\
      y'' & = -\dfrac{1}{2} (x^2 + 4)^{-3/2} \cdot 2x = -\dfrac{x}{(x^2 + 4)^{3/2}}

   (4).

   .. math::

      y' & = \dfrac{2x}{x^2 + 1} \\
      y'' & = \dfrac{2(x^2 + 1) - 2x \cdot 2x}{(x^2 + 1)^2} = \dfrac{2(1 - x^2)}{(x^2 + 1)^2}

   (6).

   .. math::

      y' & = 2 \cos 2x \\
      y'' & = -4 \sin 2x

2. 若 :math:`f(x)` 的二阶导数存在, 求下列函数 :math:`y` 的二阶导数 :math:`\dfrac{\mathrm{d}^2 y}{\mathrm{d} x^2}`:

   (2). :math:`y = \ln f(x)`.

.. proof:solution::

   .. math::

      y' & = \dfrac{1}{f(x)} \cdot f'(x) \\
      y'' & = \dfrac{1}{f(x)} \cdot f''(x) - \dfrac{1}{f^2(x)} \cdot (f'(x))^2 = \dfrac{f''(x) f(x) - (f'(x))^2}{f^2(x)}

3. 验证函数关系式:

   (2). :math:`y = \dfrac{x - 3}{x - 4}` 满足关系式 :math:`2y'^2 = (y - 1) y''`.

.. proof:proof::

   .. math::

      y' & = \dfrac{(x - 4) - (x - 3)}{(x - 4)^2} = -\dfrac{1}{(x - 4)^2} \\
      y'' & = 2(x - 4)^{-3} = \dfrac{2}{(x - 4)^3}

   所以

   .. math::

      2y'^2 & = 2 \cdot \dfrac{1}{(x - 4)^4} = \dfrac{2}{(x - 4)^4} \\
      (y - 1) y'' & = \dfrac{(x - 3) - (x - 4)}{x - 4} \cdot \dfrac{2}{(x - 4)^3} = \dfrac{2}{(x - 4)^4}

   所以 :math:`2y'^2 = (y - 1) y''`.

4. 求下列函数的高阶导数:

   (2). :math:`y = x (e^{x} + e^{-x})`, 求 :math:`y^{(99)}`.

.. proof:solution::

   .. math::

      y' & = e^x + e^{-x} + x (e^x - e^{-x}) \\
      y'' & = e^x - e^{-x} + e^x - e^{-x} + x (e^x + e^{-x}) = 2(e^x - e^{-x}) + x (e^x + e^{-x}) \\
      y^{(3)} & = 2(e^x + e^{-x}) + e^x + e^{-x} + x (e^x - e^{-x}) = 3(e^x + e^{-x}) + x (e^x - e^{-x})

   所以可以猜测 :math:`y^{(n)} = n(e^x + (-1)^{n - 1} e^{-x}) + x (e^x + (-1)^n e^{-x})`, 用数学归纳法证明:

   .. math::

      y^{(n + 1)} & = \dfrac{d \left( n(e^x + (-1)^{n - 1} e^{-x}) + x (e^x + (-1)^n e^{-x}) \right)}{\mathrm{d} x} \\
      & = n(e^x + (-1)^{n} e^{-x}) + (e^x + (-1)^n e^{-x}) + x (e^x + (-1)^{n + 1} e^{-x}) \\
      & = (n + 1)(e^x + (-1)^{n} e^{-x}) + x (e^x + (-1)^{n + 1} e^{-x}) \\
      & = (n + 1)(e^x + (-1)^{(n + 1) - 1} e^{-x}) + x (e^x + (-1)^{n + 1} e^{-x})

   所以 :math:`y^{(n)} = n(e^x + (-1)^{n - 1} e^{-x}) + x (e^x + (-1)^n e^{-x})`. 令 :math:`n = 99` 有

   .. math::

      y^{(99)} = 99(e^x + (-1)^{98} e^{-x}) + x (e^x + (-1)^{99} e^{-x}) = 99(e^x + e^{-x}) + x (e^x - e^{-x}).

   另解: 利用 Leibniz 公式 :math:`(uv)^{(n)} = \sum\limits_{k = 0}^n C_n^k u^{(k)} v^{(n - k)}`, 有

   .. math::

      y^{(n)} & = (x (e^{x} + e^{-x}))^{(n)} = C_n^0 x^{(0)} (e^{x} + e^{-x})^{(n)} + C_n^1 x^{(1)} (e^{x} + e^{-x})^{(n - 1)} + 0 + \cdots + 0 \\
      & = x (e^{x} + (-1)^n e^{-x}) + n (e^{x} + (-1)^{n - 1} e^{-x}).

   因此 :math:`y^{(99)} = 99(e^x + (-1)^{98} e^{-x}) + x (e^x + (-1)^{99} e^{-x}) = 99(e^x + e^{-x}) + x (e^x - e^{-x})`.

§2.4 隐函数与参数方程所确定的函数的导数
------------------------------------------

1. 求下列隐函数所确定的函数的导数:

   (1). :math:`x^3 + y^3 - 3xy = 0`;

   (3). :math:`e^{x + y} - xy = 1`;

   (5). :math:`y = \tan (x + y)`.

.. proof:solution::

   (1). 方程两边对 :math:`x` 求导有 :math:`3 x^2 + 3 y^2 y' - 3 (x y' + y) = 0`, 所以 :math:`y' = \dfrac{y - x^2}{y^2 - x}`.

   (3). 方程两边对 :math:`x` 求导有 :math:`e^{x + y} (1 + y') - y - xy' = 0`, 所以 :math:`y' = \dfrac{y - e^{x + y}}{e^{x + y} - x} = \dfrac{y - xy - 1}{1 + xy -x}`.

   (5). 方程两边对 :math:`x` 求导有 :math:`y' = \dfrac{1}{\cos^2 (x + y)} (1 + y')`, 所以 :math:`y' = \dfrac{1}{\cos^2 (x + y) - 1} = -\dfrac{1}{\sin^2 (x + y)}`.

3. :math:`y = 1 + x e^y`, 求 :math:`y'|_{x = 0}, y''|_{x = 0}`.

.. proof:solution::

   首先将 :math:`x = 0` 代入方程 :math:`y = 1 + x e^y` 得 :math:`y|_{x = 0} = 1`.

   方程 :math:`y = 1 + x e^y` 两边对 :math:`x` 求导有 :math:`y' = e^y + x e^y y'`, 所以 :math:`y' = \dfrac{e^y}{1 - x e^y}`. 所以 :math:`y'|_{x = 0} = e^{1} = e`.

   :math:`y' = \dfrac{e^y}{1 - x e^y} = \dfrac{e^y}{2 - y}` 两边对 :math:`x` 求二阶导有

   .. math::

      y'' & = \dfrac{e^y y' (2 - y) - e^y (-y')}{(2 - y)^2} = \dfrac{e^y y' (2 - y) + e^y y'}{(2 - y)^2} \\
         & = \dfrac{3 e^y y' - y y' e^y}{(2 - y)^2}

   将 :math:`y|_{x = 0} = 1` 和 :math:`y'|_{x = 0} = e` 代入上式得 :math:`y''|_{x = 0} = \dfrac{3 e^2 - e^2}{(1 - 0)^2} = 2 e^2`.

4. 用对数求导法求下列导数:

   (1). :math:`y = x^x`.

   (2). :math:`\displaystyle y = \sqrt[\leftroot{-3}\uproot{15}3]{\dfrac{(x + 1) (x^2 + 2)}{x (2x - 1)^2}}`.

.. proof:solution::

   (1). 由于 :math:`\ln y = \ln x^x = x \ln x`, 所以 :math:`y' = (x \ln x)' \cdot y = (\ln x + 1) x^x`.

   (2). 由于

   .. math::

      \ln y & = \ln \left( \dfrac{(x + 1) (x^2 + 2)}{x (2x - 1)^2} \right)^{1/3} = \dfrac{1}{3} \ln \left( \dfrac{(x + 1) (x^2 + 2)}{x (2x - 1)^2} \right) \\
      & = \dfrac{1}{3} \left( \ln (x + 1) + \ln (x^2 + 2) - \ln x - 2 \ln (2x - 1) \right),

   所以

   .. math::

      y' & = \dfrac{1}{3} \left( \dfrac{1}{x + 1} + \dfrac{2x}{x^2 + 2} - \dfrac{1}{x} - \dfrac{2}{2x - 1} \right) \cdot y \\
      & = \dfrac{1}{3} \left( \dfrac{1}{x + 1} + \dfrac{2x}{x^2 + 2} - \dfrac{1}{x} - \dfrac{2}{2x - 1} \right)
          \cdot \sqrt[\leftroot{-3}\uproot{15}3]{\dfrac{(x + 1) (x^2 + 2)}{x (2x - 1)^2}}.

6. 设参数方程为 :math:`\begin{cases} x = e^t \sin t \\ y = e^t \cos t \end{cases}`,

   (1). 求曲线在 :math:`t = \dfrac{\pi}{3}` 处的切线方程和法线方程;

   (2). 验证函数满足关系式 :math:`\dfrac{d^2 y}{\mathrm{d} x^2} (x + y)^2 = 2 \left( x \dfrac{\mathrm{d} y}{\mathrm{d} x} - y \right)`.

.. proof:solution::

   (1). :math:`\dfrac{\mathrm{d} y}{\mathrm{d} x} = \left. \left( \dfrac{\mathrm{d} y}{\mathrm{d} t} \right) \right/ \left( \dfrac{\mathrm{d} x}{\mathrm{d} t} \right) = \dfrac{e^t \cos t - e^t \sin t}{e^t \sin t + e^t \cos t} = \dfrac{\cos t - \sin t}{\sin t + \cos t}`.
   曲线在 :math:`t = \dfrac{\pi}{3}` 处的切线斜率为 :math:`\left. \dfrac{\mathrm{d} y}{\mathrm{d} x} \right|_{t = \dfrac{\pi}{3}} = \dfrac{\dfrac{1}{2} - \dfrac{\sqrt{3}}{2}}{\dfrac{\sqrt{3}}{2} + \dfrac{1}{2}} = \sqrt{3} - 2`.
   曲线在 :math:`t = \dfrac{\pi}{3}` 处过点 :math:`(e^{\frac{\pi}{3}} \sin \frac{\pi}{3}, e^{\frac{\pi}{3}} \cos \frac{\pi}{3})`,
   所以切线方程为 :math:`y - e^{\frac{\pi}{3}} \cos \frac{\pi}{3} = (\sqrt{3} - 2) (x - e^{\frac{\pi}{3}} \sin \frac{\pi}{3})`,
   即 :math:`y = (\sqrt{3} - 2) x + e^{\frac{\pi}{3}} (\sqrt{3} - 1)`.

   法线斜率为 :math:`-\dfrac{1}{\sqrt{3} - 2}`, 所以法线方程为 :math:`y - e^{\frac{\pi}{3}} \cos \frac{\pi}{3} = -\dfrac{1}{\sqrt{3} - 2} (x - e^{\frac{\pi}{3}} \sin \frac{\pi}{3})`,
   即 :math:`y = (2 + \sqrt{3}) x - e^{\frac{\pi}{3}} (1 + \sqrt{3})`.

   (2). 由于 :math:`\dfrac{\mathrm{d} y}{\mathrm{d} x} = \dfrac{\cos t - \sin t}{\cos t + \sin t}`, 所以

   .. math::

      \dfrac{d^2 y}{\mathrm{d} x^2}
      & = \dfrac{\dfrac{d}{\mathrm{d} t} \left( \dfrac{\mathrm{d} y}{\mathrm{d} x} \right)}{\dfrac{\mathrm{d} x}{\mathrm{d} t}}
        = \dfrac{\dfrac{d}{\mathrm{d} t} \left( \dfrac{\cos t - \sin t}{\cos t + \sin t} \right)}{e^t \sin t + e^t \cos t} \\
      & = \dfrac{\left( \dfrac{-(\cos t + \sin t) \cdot (\cos t + \sin t) - (\cos t - \sin t) \cdot (\cos t - \sin t)}{(\cos t + \sin t)^2} \right)}{e^t \sin t + e^t \cos t} \\
      & = \dfrac{-2}{e^t (\sin t + \cos t)^3}.

   所以

   .. math::

      \dfrac{d^2 y}{\mathrm{d} x^2} (x + y)^2 & = \dfrac{-2}{e^t (\sin t + \cos t)^3} \cdot (e^t \sin t + e^t \cos t)^2 = - \dfrac{2 e^t}{\sin t + \cos t} \\
      2 \left( x \dfrac{\mathrm{d} y}{\mathrm{d} x} - y \right) & = 2 \left( e^t \sin t \cdot \dfrac{\cos t - \sin t}{\cos t + \sin t} - e^t \cos t \right)
      = - \dfrac{2 e^t}{\sin t + \cos t}

   于是有 :math:`\dfrac{d^2 y}{\mathrm{d} x^2} (x + y)^2 = 2 \left( x \dfrac{\mathrm{d} y}{\mathrm{d} x} - y \right)`.

§2.5 函数的微分
--------------------------------

1. 已知 :math:`y = x^2 + 1`, 计算在 :math:`x = 1` 点处当 :math:`\Delta x = 0.1` 和 :math:`0.01` 时的 :math:`\Delta y` 和 :math:`\mathrm{d} y`.

.. proof:solution::

   函数 :math:`y = x^2 + 1` 的微分为 :math:`\mathrm{d} y = 2x \mathrm{d} x`, 所以当 :math:`x = 1` 时 :math:`\mathrm{d} y = 2 \mathrm{d} x`.

   当 :math:`\Delta x = 0.1` 时, :math:`\Delta y = f(1 + 0.1) - f(1) = 2.21 - 2 = 0.21, \mathrm{d} y = 2 \cdot 0.1 = 0.2`.

   当 :math:`\Delta x = 0.01` 时, :math:`\Delta y = f(1 + 0.01) - f(1) = 2.0201 - 2 = 0.0201, \mathrm{d} y = 2 \cdot 0.01 = 0.02`.

2. 求下列函数的微分:

   (1). :math:`y = x^2 + \sqrt{x}`;

   (3). :math:`y = e^{x^2 + x}`;

   (5). :math:`y = \ln (1 + x^2)`;

   (7). :math:`y = \arctan \dfrac{1 - x}{1 + x}`;

   (9). :math:`x^3 + y^3 -3x^2y - 3y^2x = 4a^2`.

.. proof:solution::

   (1). :math:`\mathrm{d} y = 2x \mathrm{d} x + \dfrac{1}{2 \sqrt{x}} \mathrm{d} x = (2x + \dfrac{1}{2 \sqrt{x}}) \mathrm{d} x`.

   (3). :math:`\mathrm{d} y = (2x + 1) e^{x^2 + x} \mathrm{d} x`.

   (5). :math:`\mathrm{d} y = \dfrac{2x}{1 + x^2} \mathrm{d} x`.

   (7). :math:`\left( \arctan\dfrac{1 - x}{1 + x} \right)' = \dfrac{1}{1 + \left( \dfrac{1 - x}{1 + x} \right)^2} \cdot \dfrac{-(1 + x) - (1 - x)}{(1 + x)^2} = \dfrac{-1}{1 + x^2}`,
   所以 :math:`\mathrm{d} y = \dfrac{1}{1 + x^2} \mathrm{d} x`.

   (9). 对等式两边求微分有 :math:`3x^2 \mathrm{d} x + 3y^2 \mathrm{d} y - 6xy \mathrm{d} x - 3x^2 \mathrm{d} y - 6xy \mathrm{d} y - 3y^2 \mathrm{d} x = 0`,
   所以 :math:`(y^2 - 2xy - x^2) \mathrm{d} y = (2xy - x^2 + y^2) \mathrm{d} x`, 即有 :math:`\mathrm{d} y = \dfrac{y^2 + 2xy - x^2}{y^2 - 2xy + x^2} \mathrm{d} x`.

3. 将适当的函数填入括号中, 使得下列等式成立:

   (2). :math:`\mathrm{d} (\quad) = \dfrac{1}{x^2} \mathrm{d} x`;

   (4). :math:`\mathrm{d} (\quad) = e^{-2x} \mathrm{d} x`;

   (6). :math:`\mathrm{d} (\quad) = \dfrac{\arctan x}{x^2 + 1} \mathrm{d} x`.

.. proof:solution::

   (2). 由于 :math:`\left( \dfrac{1}{x} \right)' = -\dfrac{1}{x^2}`, 所以 :math:`\mathrm{d} \left( -\dfrac{1}{x} + C \right) = \dfrac{1}{x^2} \mathrm{d} x`.

   (4). 由于 :math:`\left( -\dfrac{1}{2} e^{-2x} \right)' = e^{-2x}`, 所以 :math:`\mathrm{d} \left( -\dfrac{1}{2} e^{-2x} + C \right) = e^{-2x} \mathrm{d} x`.

   (6). 由于 :math:`\left( \dfrac{1}{2} \arctan^2 x \right)' = \dfrac{\arctan x}{x^2 + 1}`,
   所以 :math:`\mathrm{d} \left( \dfrac{1}{2} \arctan^2 x + C \right) = \dfrac{\arctan x}{x^2 + 1} \mathrm{d} x`.

   以上的 :math:`C` 为常数.

   .. note::

      一般地, 可以把 :math:`\mathrm{d} x` 变形, 将整个表示式变成基本初等函数的微分. 例如第 (6) 题:

      .. math::

         \dfrac{\arctan x}{x^2 + 1} \mathrm{d} x & = \arctan x \cdot \dfrac{1}{x^2 + 1} \mathrm{d} x \\
         & = \arctan x \cdot \mathrm{d} (\arctan x) \\
         & = \mathrm{d} \left( \dfrac{1}{2} \arctan^2 x + C \right).

4. 求下列近似值:

   (2). :math:`e^{1.01}`.

.. proof:solution::

   由于 :math:`e^x` 在 :math:`x = 1` 处的导数为 :math:`e^x`, 在 :math:`x = 1` 附近有 :math:`e^{x + \Delta x} \approx e^x + e^x \cdot \Delta x`,
   那么 :math:`e^{1.01} \approx e^1 + e^1 \cdot 0.01 \approx 2.71828 + 2.71828 \cdot 0.01 = 2.74546`.

5. 当 :math:`x` 很小时, 证明近似公式:

   (2). :math:`\ln (1 + \sin x) \approx x`.

.. proof:solution::

   由于 :math:`\ln (1 + \sin x)` 在 :math:`x = 0` 处的值为 :math:`0`, 导数为 :math:`\left.\dfrac{\cos x}{1 + \sin x}\right|_{x = 0} = 1`,
   所以在 :math:`x = 0` 附近有 :math:`\ln (1 + \sin x) \approx 0 + 1 \cdot x = x`.

7. 已知单摆的运动规律为 :math:`y = 2\pi \sqrt{\dfrac{x}{g}}`, 其中 :math:`y` 是运动周期, :math:`g` 为重力加速度, :math:`x` 为摆长. 如果摆长增加 :math:`1\%`, 单摆的运动周期约增加多少?

.. proof:solution::

   单摆运动周期 :math:`y = 2\pi \sqrt{\dfrac{x}{g}}` 关于摆长 :math:`x` 的导数为 :math:`\dfrac{\pi}{\sqrt{g x}}`, 那么当摆长增加 :math:`1\%` 时, 单摆的运动周期增加约
   :math:`\dfrac{\pi}{\sqrt{g x}} \cdot 0.01 x = \pi \sqrt{\dfrac{x}{g}} \cdot 0.01 = \dfrac{y}{2} \cdot 0.01 = y \cdot 0.005`, 所以单摆的运动周期约 :math:`0.5\%`.

   另解: 直接利用弹性函数, 当 :math:`x` 增加 :math:`1\%` 时, :math:`y` 增加比例为

   .. math::

      y'\dfrac{x}{y}\% = \left( \dfrac{\pi}{\sqrt{g x}} \cdot \dfrac{x}{2\pi \sqrt{\dfrac{x}{g}}} \right)\% = \dfrac{1}{2} \% = 0.5\%.

§2.6 微分中值定理
--------------------------------

1. 验证函数 :math:`f(x) = x \sqrt{1 - x^2}` 在 :math:`[-1, 1]` 满足罗尔定理.

.. proof:solution::

   (1). :math:`f(x) = x \sqrt{1 - x^2}` 是初等函数, 在定义区间 :math:`[-1, 1]` 上连续.

   (2). :math:`f'(x) = \sqrt{1 - x^2} - \dfrac{x^2}{\sqrt{1 - x^2}}`, 其在开区间 :math:`(-1, 1)` 内有定义, 所以 :math:`f(x)` 在开区间 :math:`(-1, 1)` 内可导.

   (3). :math:`f(-1) = f(1) = 0`.

3. 设 :math:`f(x)` 在 :math:`[a, b]` 连续可微, 在 :math:`(a, b)` 二阶可微, 且 :math:`f(a) = f(b) = f'(a) = 0`, 证明 :math:`f''(x) = 0` 在 :math:`(a, b)` 内至少有一个根.

.. proof:proof::

   由于 :math:`f(a) = f(b) = 0`, 所以根据罗尔定理, 存在 :math:`\xi \in (a, b)` 使得 :math:`f'(\xi) = 0`.

   考察函数 :math:`f'(x)`, 它在闭区间 :math:`[a, \xi]` 上连续, 在开区间 :math:`(a, \xi)` 内可导, 且 :math:`f'(a) = f'(\xi) = 0`, 所以根据罗尔定理,
   存在 :math:`\eta \in (a, \xi)` 使得 :math:`f''(\eta) = 0`.

   注意: 这题用了两次罗尔定理.

4. 已知 :math:`c_0 + \dfrac{c_1}{2} + \cdots + \dfrac{c_n}{n + 1} = 0`, 证明 :math:`p(x) = c_0 + c_1 x + \cdots + c_n x^n = 0` 至少有一正实根.

.. proof:proof::

   考察函数 :math:`f(x) = c_0 x + \dfrac{c_1}{2} x^2 + \cdots + \dfrac{c_n}{n + 1} x^{n + 1}`, 它是一个多项式, 因此在闭区间 :math:`[0, 1]` 上连续, 在开区间 :math:`(0, 1)` 内可导,
   而且 :math:`f(0) = f(1) = 0`, 所以根据罗尔定理, 存在 :math:`\xi \in (0, 1)` 使得 :math:`0 = f'(\xi) = c_0 + c_1 \xi + \cdots + c_n \xi^n`, 即 :math:`p(\xi) = 0`.
   因此, :math:`p(x)` 至少有一正实根 :math:`\xi`.

6. 求证 :math:`\arcsin x + \arccos x \equiv \dfrac{\pi}{2} (\lvert x \rvert \leqslant 1)`.

.. proof:proof::

   考虑函数 :math:`f(x) = \arcsin x + \arccos x, \lvert x \rvert \leqslant 1`. 它的导数为 :math:`f'(x) = \dfrac{1}{\sqrt{1 - x^2}} - \dfrac{1}{\sqrt{1 - x^2}} = 0`,
   所以 :math:`f(x)` 在闭区间 :math:`[-1, 1]` 上是常数函数. 易知 :math:`f(0) = \dfrac{\pi}{2}`, 所以 :math:`f(x) \equiv \dfrac{\pi}{2}`.

7. 证明: 当 :math:`a > b > 0` 时, :math:`\dfrac{a - b}{a} < \ln \dfrac{a}{b} < \dfrac{a - b}{b}`.

.. proof:proof::

   考虑函数 :math:`f(x) = \ln x, x > 0`. 它的导数为 :math:`f'(x) = \dfrac{1}{x}`. 对 函数 :math:`f(x)` 在区间 :math:`[b, a]` 上应用拉格朗日中值定理, 存在 :math:`\xi \in (b, a)` 使得

   .. math::

      \ln a - \ln b = \dfrac{1}{\xi} (a - b).

   所以

   .. math::

      \dfrac{a - b}{a} = \left. \dfrac{1}{\xi} (a - b) \right|_{\xi = a} < \ln \dfrac{a}{b} < \left. \dfrac{1}{\xi} (a - b) \right|_{\xi = b} = \dfrac{a - b}{b}.

9. 设函数 :math:`f(x)` 在区间 :math:`[a, b]` 上连续, 在 :math:`(a, b)` 内可导, 且有 :math:`f(a) = f(b) = 0`.
   利用 :math:`g(x) = e^{-x} f(x)` 证明存在 :math:`\xi \in (a, b)` 使得 :math:`f(\xi) - f'(\xi) = 0`.

.. proof:proof::

   由于函数 :math:`f(x)` 在区间 :math:`[a, b]` 上连续, 在 :math:`(a, b)` 内可导, 那么函数 :math:`g(x) = e^{-x} f(x)` 也在区间 :math:`[a, b]` 上连续, 在 :math:`(a, b)` 内可导,
   而且 :math:`g(a) = g(b) = 0`. 根据罗尔定理, 存在 :math:`\xi \in (a, b)` 使得 :math:`g'(\xi) = e^{-\xi}(f'(\xi) - f(\xi)) = 0`, 即有 :math:`f(\xi) - f'(\xi) = 0`.

10. 求证: 设 :math:`f(x)` 在 :math:`[a, b] (b > a > 0)` 上连续, 在 :math:`(a, b)` 内可导, 则存在 :math:`\xi \in (a, b)` 使得

    .. math::

      f(b) - f(a) = \xi f'(\xi) \ln \dfrac{b}{a}.

.. proof:proof::

   考虑函数 :math:`g(u) = f(e^{u})`. 由于 :math:`f(x)` 在 :math:`[a, b] (b > a > 0)` 上连续, 在 :math:`(a, b)` 内可导, 那么函数 :math:`g(u)` 在 :math:`[\ln a, \ln b]` 上连续,
   在 :math:`(\ln a, \ln b)` 内可导. 那么根据拉格朗日中值定理, 存在 :math:`\eta \in (\ln a, \ln b)` 使得

   .. math::

      \dfrac{g(\ln b) - g(\ln a)}{\ln b - \ln a} = g'(\eta) = f'(e^{\eta}) e^{\eta}.

   令 :math:`\xi = e^{\eta}`, 那么 :math:`\xi \in (a, b)`, 且

   .. math::

      f(b) - f(a) = \xi f'(\xi) \ln \dfrac{b}{a}.

§2.7 洛必达法则
--------------------------------

1. 应用洛必达法则求下列 :math:`\dfrac{0}{0}` 或 :math:`\dfrac{\infty}{\infty}` 型未定式的极限:

   (2). :math:`\lim\limits_{x \to 0} \dfrac{1 - \cos x^2}{x^3 \sin x}`;

   (4). :math:`\lim\limits_{x \to 0} \dfrac{\tan x - x}{x - \sin x}`;

   (6). :math:`\lim\limits_{x \to 0} \dfrac{e^{-2x} - e^{-5x}}{x}`;

   (8). :math:`\lim\limits_{x \to \frac{\pi}{6}} \dfrac{1 - 2\sin x}{\cos 3x}`;

   (10). :math:`\lim\limits_{x \to +\infty} \dfrac{x^b}{e^{ax}} ~~ (a, b > 0)`;

   (12). :math:`\lim\limits_{x \to 0^+} \dfrac{\ln x}{\cot x}`.

.. proof:solution::

   (2).

   .. math::

      \lim\limits_{x \to 0} \dfrac{1 - \cos x^2}{x^3 \sin x}
      & = \lim\limits_{x \to 0} \dfrac{2x \sin x^2}{3x^2 \sin x + x^3 \cos x} = \lim\limits_{x \to 0} \dfrac{2 \sin x^2}{3x \sin x + x^2 \cos x} \\
      & = \lim\limits_{x \to 0} \dfrac{4x \cos x^2}{3 \sin x + 3 x \cos x + 2x \cos x - x^2 \sin x} \\
      & = \lim\limits_{x \to 0} \dfrac{4 \cos x^2}{3 + 5 \cos x - x \sin x} \\
      & = \dfrac{4}{8} = \dfrac{1}{2}.

   (4).

   .. math::

      \lim\limits_{x \to 0} \dfrac{\tan x - x}{x - \sin x} & = \lim\limits_{x \to 0} \dfrac{\sec^2 x - 1}{1 - \cos x} = \lim\limits_{x \to 0} \dfrac{ 2 \sec x \cdot (\sec x \tan x)}{\sin x} \\
      & = \lim\limits_{x \to 0} \dfrac{ 2 \sec^2 x}{\cos x} = \dfrac{2}{1} = 2.

   (6).

   .. math::

      \lim\limits_{x \to 0} \dfrac{e^{-2x} - e^{-5x}}{x} = \lim\limits_{x \to 0} \dfrac{-2e^{-2x} + 5e^{-5x}}{1} = -2 + 5 = 3.

   (8).

   .. math::

      \lim\limits_{x \to \frac{\pi}{6}} \dfrac{1 - 2\sin x}{\cos 3x} = \lim\limits_{x \to \frac{\pi}{6}} \dfrac{2\cos x}{3\sin 3x} = \dfrac{\sqrt{3}}{3}.

   (10). 若 :math:`b > 0` 为正整数, 那么

   .. math::

      \lim\limits_{x \to +\infty} \dfrac{x^b}{e^{ax}} & = \lim\limits_{x \to +\infty} \dfrac{bx^{b-1}}{ae^{ax}} = \cdots \\
      & = \lim\limits_{x \to +\infty} \dfrac{b!}{a^b e^{ax}} = 0.

   若 :math:`b > 0` 不是正整数, 那么

   .. math::

      \lim\limits_{x \to +\infty} \dfrac{x^b}{e^{ax}} & = \lim\limits_{x \to +\infty} \dfrac{b x^{b-1}}{a e^{ax}} = \cdots \\
      & = \lim\limits_{x \to +\infty} \dfrac{b(b-1)\cdots(b-[b])}{a^{[b]} e^{ax} x^{[b]+1-b}} = 0.

   (12).

   .. math::

      \lim\limits_{x \to 0^+} \dfrac{\ln x}{\cot x} = \lim\limits_{x \to 0^+} \dfrac{\dfrac{1}{x}}{-\csc^2 x} = \lim\limits_{x \to 0^+} -x \sin^2 x = 0.

2. 应用洛必达法则求下列极限:

   (1). :math:`\lim\limits_{x \to \pi} (\pi - x) \tan \dfrac{x}{2}`;

   (3). :math:`\lim\limits_{x \to 0^+} \sin x \ln x`;

   (5). :math:`\lim\limits_{x \to 1} \left(\dfrac{1}{\ln x} - \dfrac{1}{x - 1} \right)`;

   (7). :math:`\lim\limits_{x \to +\infty} \left( \sqrt[3]{x^3 + 3x^2} - \sqrt{x^2 - 2x} \right)`.

   (9). :math:`\lim\limits_{x \to 1} x^{\frac{1}{1-x}}`;

   (11). :math:`\lim\limits_{x \to 0^+} \left( \ln \dfrac{1}{x} \right)^x`.

.. proof:solution::

   (1).

   .. math::

      \lim\limits_{x \to \pi} (\pi - x) \tan \dfrac{x}{2} & = \lim\limits_{x \to \pi} \dfrac{(\pi - x) \sin \dfrac{x}{2}}{\cos \dfrac{x}{2}} \\
      & = \lim\limits_{x \to \pi} \dfrac{-\sin \dfrac{x}{2} + (\pi - x) \cdot \dfrac{1}{2} \cos \dfrac{x}{2}}{-\dfrac{1}{2}\sin \dfrac{x}{2}} \\
      & = \dfrac{-1}{-\dfrac{1}{2}} = 2

   (3).

   .. math::

      \lim\limits_{x \to 0^+} \sin x \ln x & = \lim\limits_{x \to 0^+} \dfrac{\ln x}{\csc x} = \lim\limits_{x \to 0^+} \dfrac{\dfrac{1}{x}}{-\csc x \cot x} \\
      & = - \lim\limits_{x \to 0^+} \dfrac{\sin^2 x}{x \cos x} = - \lim\limits_{x \to 0^+} \dfrac{2 \sin x \cos x}{\cos x - x \sin x} \\
      & = 0

   (5).

   .. math::

      \lim\limits_{x \to 1} \left(\dfrac{1}{\ln x} - \dfrac{1}{x - 1} \right) & = \lim\limits_{x \to 1} \dfrac{x - \ln x - 1}{(x - 1) \ln x} = \lim\limits_{x \to 1} \dfrac{1 - \dfrac{1}{x}}{\ln x + \dfrac{x - 1}{x}} \\
      & = \lim\limits_{x \to 1} \dfrac{x - 1}{x \ln x + x - 1} = \lim\limits_{x \to 1} \dfrac{1}{\ln x + 2} \\
      & = \dfrac{1}{2}

   (7).

   .. math::

      \lim\limits_{x \to +\infty} \left( \sqrt[3]{x^3 + 3x^2} - \sqrt{x^2 - 2x} \right) & = \lim\limits_{x \to +\infty} x \left( \sqrt[3]{1 + 3\dfrac{1}{x}} - \sqrt{1 - 2\dfrac{1}{x}} \right) \\
      & = \lim\limits_{x \to 0^+} \dfrac{\sqrt[3]{1 + 3x} - \sqrt{1 - 2x}}{x} \\
      & = \lim\limits_{x \to 0^+} \dfrac{(1 + 3x)^{-\frac{2}{3}} + (1 - 2x)^{-\frac{1}{2}}}{1} \\
      & = 1 + 1 = 2

   (9). 因为

   .. math::

      \lim\limits_{x \to 1} \dfrac{1}{1-x} \cdot \ln x = \lim\limits_{x \to 1} \frac{\dfrac{1}{x}}{-1} = -1,

   所以 :math:`\lim\limits_{x \to 1} x^{\frac{1}{1-x}} = e^{-1}`.

   (11). 因为

   .. math::

      \lim\limits_{x \to 0^+} x \cdot \ln \left( \ln \dfrac{1}{x} \right) = \lim\limits_{x \to +\infty} \dfrac{\ln (\ln x)}{x}
      = \lim\limits_{x \to +\infty} \dfrac{\dfrac{1}{\ln x} \cdot \dfrac{1}{x}}{1} = 0,

   所以 :math:`\lim\limits_{x \to 0^+} \left( \ln \dfrac{1}{x} \right)^x = e^0 = 1`.

3. 求 :math:`\lim\limits_{x \to 0} \dfrac{x^2 \sin \dfrac{1}{x}}{\sin x}` 极限, 并验证计算时不能应用洛必达法则.

.. proof:solution::

   :math:`\lim\limits_{x \to 0} \dfrac{x^2 \sin \dfrac{1}{x}}{\sin x} = \lim\limits_{x \to 0} \dfrac{x}{\sin x} \cdot \left( x \sin \dfrac{1}{x} \right)`.
   由于 :math:`\lim\limits_{x \to 0} \dfrac{x}{\sin x} = 1`, :math:`\lim\limits_{x \to 0} x \sin \dfrac{1}{x} = 0`, 所以有

   .. math::

      \lim\limits_{x \to 0} \dfrac{x^2 \sin \dfrac{1}{x}}{\sin x} = 0.

   如果使用洛必达法则, 这是 :math:`\dfrac{0}{0}` 型未定式, 那么有

   .. math::

      \lim\limits_{x \to 0} \dfrac{x^2 \sin \dfrac{1}{x}}{\sin x} = \lim\limits_{x \to 0} \dfrac{2x \sin \dfrac{1}{x} - \cos \dfrac{1}{x}}{\cos x}.

   上式分子 :math:`2x \sin \dfrac{1}{x} - \cos \dfrac{1}{x}` 极限 (当 :math:`x \to 0`）不存在, 所以不能使用洛必达法则.

§2.8 泰勒公式
--------------------------------

1. 求函数 :math:`f(x) = \dfrac{1}{3 - x}` 在指定点 :math:`x_0 = 2` 的泰勒展开式.

.. proof:solution::

   函数 :math:`f(x) = \dfrac{1}{3 - x} = -(x - 3)^{-1}` 的 :math:`k` 阶导函数为 :math:`f^{(k)}(x) = k! (x - 3)^{-k-1} = \dfrac{k!}{(3 - x)^{k+1}}`.
   将 :math:`x_0 = 2` 代入有

   .. math::

      f^{(k)}(x_0) = - (-1)^k k! (2 - 3)^{-k-1} = k!,

   所以在点 :math:`x_0 = 2` 处函数 :math:`f(x) = \dfrac{1}{3 - x}` 的 :math:`n` 阶泰勒展开式为

   .. math::

      f(x) = \sum\limits_{k=0}^{n} \dfrac{f^{(k)}(x_0)}{k!} (x - x_0)^k + R_n = \sum\limits_{k=0}^{k} (x - 2)^n + R_n,

   其中 :math:`R_n = \dfrac{f^{(n+1)}(\xi)}{(n+1)!} (x - x_0)^{n+1} = \dfrac{(n+1)!}{(3 - \xi)^{n+2}} (x - 2)^{n+1}` 为拉格朗日余项,
   :math:`\xi` 介于 :math:`x_0` 和 :math:`x` 之间.

   另解:

   由于 :math:`f(x) = \dfrac{1}{3 - x} = \dfrac{1}{1 - (x - 2)}`, 所以可以利用 :math:`\dfrac{1}{1 - t}` 在 :math:`t = 0` 附近的泰勒展开式

   .. math::

      \dfrac{1}{1 - t} = 1 + t + t^2 + \cdots + t^n + o(t^n),

   通过间接法求得 :math:`f(x)` 带佩亚诺型余项的泰勒展开式为

   .. math::

      f(x) & = \dfrac{1}{3 - x} = \dfrac{1}{1 - (x - 2)} \\
      & = 1 + (x - 2) + (x - 2)^2 + \cdots + (x - 2)^n + o((x - 2)^n).

2. 将下面函数的麦克劳林展开式写出来:

   (1). :math:`f(x) = e^{x^2}`;

   (2). :math:`f(x) = \sin^2 x`;

   (3). :math:`f(x) = \dfrac{x}{1 + x - 2x^2}`.

.. proof:solution::

   (1). 因为函数 :math:`g(x) = e^x` 的泰勒展开前 :math:`n` 项和为

   .. math::

      1 + x + \dfrac{x^2}{2!} + \dfrac{x^3}{3!} + \cdots + \dfrac{x^n}{n!}

   所以函数 :math:`f(x) = e^{x^2}` 的麦克劳林展开式为

   .. math::

      e^{x^2} = 1 + x^2 + \dfrac{x^4}{2!} + \dfrac{x^6}{3!} + \cdots + \dfrac{x^{2n}}{n!} + o(x^{2n}).

   (2). 因为函数 :math:`f(x) = \sin^2 x = \dfrac{1 - \cos 2x}{2}` 的 :math:`k` 阶导函数为 :math:`f^{(k)}(x) = -2^{k-1} \cos (2x + \dfrac{k\pi}{2})`,
   所以 :math:`f(x)` 的麦克劳林展开式为

   .. math::

      \sin^2 x & = \dfrac{1}{2} - \dfrac{1}{2} \cos 2x \\
      & = \dfrac{1}{2} - \dfrac{1}{2} \left( 1 - \dfrac{(2x)^2}{2!} + \dfrac{(2x)^4}{4!} - \cdots + (-1)^n \dfrac{(2x)^{2n}}{(2n)!} \right) + o(x^{2n}) \\
      & = x^2 - \dfrac{x^4}{3} + \cdots + (-1)^{n+1} \dfrac{x^{2n}}{(2n+1)!} + o(x^{2n}).

   (3). 因为函数 :math:`f(x) = \dfrac{x}{1 + x - 2x^2} = \dfrac{1}{3} \cdot \dfrac{3x}{(1 + 2x)(1 - x)} = \dfrac{1}{3} \cdot \dfrac{1}{1 - x} - \dfrac{1}{3} \cdot \dfrac{2}{1 + 2x}`,
   又有

   .. math::

      \dfrac{1}{1 - x} & = 1 + x + x^2 + x^3 + \cdots + x^n + o(x^n) \\
      \dfrac{1}{1 + 2x} & = 1 - 2x + 4x^2 - 8x^3 + \cdots + (-2)^{n} x^n + o(x^n),

   所以 :math:`f(x)` 的麦克劳林展开式为

   .. math::

      f(x) & = \dfrac{1}{3} \cdot \dfrac{1}{1 - x} - \dfrac{1}{3} \cdot \dfrac{2}{1 + 2x} \\
      & = \dfrac{1}{3} \left( 1 + x + x^2 + \cdots + x^n \right) - \dfrac{1}{3} \left( 1 - 2x + 4x^2 \cdots + (-2)^{n} x^n \right) + o(x^n) \\
      & = x - x^2 + \cdots + \dfrac{1 - (-2)^{n}}{3} x^n + o(x^n).

§2.9 函数的单调性与曲线的凹凸性
--------------------------------

.. note::

   课本中定义的凹凸性与目前主流教材与科研文献中的凹凸性是正好相反的. 以下跟随课本, 凹指的是下凸, 凸指的是上凸.

1. 确定下列函数的单调区间:

   (2). :math:`y = \sqrt{2x - x^2}`;

   (4). :math:`y = x^n e^{-x} \quad (n > 0, x \geqslant 0)`.

.. proof:solution::

   (2). :math:`y = \sqrt{2x - x^2}` 的定义域为 :math:`[0, 2]`, 导函数为 :math:`y' = \dfrac{1 - x}{\sqrt{2x - x^2}}`. 令 :math:`y' = 0` 解得 :math:`x = 1`.
   当 :math:`0 \leqslant x \leqslant 1` 时, :math:`y' = \dfrac{1 - x}{\sqrt{2x - x^2}} > 0`, 所以 :math:`y` 在 :math:`[0, 1]` 上单调递增；
   当 :math:`1 \leqslant x \leqslant 2` 时, :math:`y' = \dfrac{1 - x}{\sqrt{2x - x^2}} < 0`, 所以 :math:`y` 在 :math:`[1, 2]` 上单调递减.

   (4). :math:`y = x^n e^{-x} \quad (n > 0, x \geqslant 0)` 的导函数为 :math:`y' = x^{n-1} e^{-x} (n - x)`. 令 :math:`y' = 0` 解得 :math:`x = n`.
   当 :math:`0 \leqslant x \leqslant n` 时, :math:`y' = x^{n-1} e^{-x} (n - x) > 0`, 所以 :math:`y` 在 :math:`[0, n]` 上单调递增；
   当 :math:`n \leqslant x` 时, :math:`y' = x^{n-1} e^{-x} (n - x) < 0`, 所以 :math:`y` 在 :math:`[n, +\infty)` 上单调递减.

2. 应用函数的单调性证明下列不等式:

   (1). :math:`2 \sqrt{x} > 3 - \dfrac{1}{x}, \quad x > 1`;

   (3). :math:`\dfrac{2}{\pi} x < \sin x < x, \quad 0 < x < \dfrac{\pi}{2}`.

.. proof:proof::

   (1). 令 :math:`f(x) = 2 \sqrt{x} - (3 - \dfrac{1}{x})`, 那么当 :math:`x \geqslant 1`时有 :math:`f'(x) = \dfrac{1}{\sqrt{x}} + \dfrac{1}{x^2} > 0`,
   所以 :math:`f(x)` 在 :math:`[1, +\infty)` 上单调递增, 故 :math:`f(x) > f(1) = 0` 对一切 :math:`x > 1` 成立.

   (3). 令 :math:`f(x) = \sin x - \dfrac{2}{\pi} x`, 那么 :math:`f(x)` 的导函数为 :math:`f'(x) = \cos x - \dfrac{2}{\pi}`. 令 :math:`f'(x) = 0`,
   解得 :math:`x = \arccos \dfrac{2}{\pi}`. 在区间 :math:`[0, \arccos \dfrac{2}{\pi})` 上有 :math:`f'(x) > 0`,
   所以 :math:`f(x)` 在 :math:`[0, \arccos \dfrac{2}{\pi}]` 上单调递增, 从而有 :math:`f(x) > f(0) = 0` 对一切 :math:`0 < x \leqslant \arccos \dfrac{2}{\pi}` 成立.
   在区间 :math:`[\arccos \dfrac{2}{\pi}, \dfrac{\pi}{2})` 上有 :math:`f'(x) < 0`, 所以 :math:`f(x)` 在 :math:`[\arccos \dfrac{2}{\pi}, \dfrac{\pi}{2}]` 上单调递减,
   从而有 :math:`f(x) > f(\dfrac{\pi}{2}) = 0` 对一切 :math:`\arccos \dfrac{2}{\pi} \leqslant x < \dfrac{\pi}{2}` 成立.
   于是 :math:`f(x) > 0` 对一切 :math:`0 < x < \dfrac{\pi}{2}` 成立.

   另一方面, 令 :math:`g(x) = x - \sin x`, 那么 :math:`g(x)` 的导函数为 :math:`g'(x) = 1 - \cos x`. 在区间 :math:`(0, \dfrac{\pi}{2})` 上恒有 :math:`g'(x) > 0`,
   所以 :math:`g(x)` 在 :math:`(0, \dfrac{\pi}{2})` 上单调递增, 从而有 :math:`g(x) > g(0) = 0` 对一切 :math:`0 < x < \dfrac{\pi}{2}` 成立.

   综上所述, :math:`\dfrac{2}{\pi} x < \sin x < x, \quad 0 < x < \dfrac{\pi}{2}` 成立.

3. 确定下列函数确定曲线的凹凸区间与拐点:

   (3). :math:`y = (x^2 + 2x - 1) e^{-x}`.

.. proof:solution::

   :math:`y = (x^2 + 2x - 1) e^{-x}` 的定义域为 :math:`(-\infty, +\infty)`, 导函数以及二阶导函数分别为

   .. math::

      y' & = (2x + 2) e^{-x} - (x^2 + 2x - 1) e^{-x} = (3 - x^2) e^{-x} \\
      y'' & = (-2x) e^{-x} - (3 - x^2) e^{-x} = (x^2 - 2x - 3) e^{-x}.

   令 :math:`y'' = 0` 解得 :math:`x = -1, x = 3`, 相应函数值分别为 :math:`y(-1) = -2e, y(3) = 14e^{-3}`. 当 :math:`-\infty < x < -1` 时, :math:`y'' > 0`,
   所以曲线 在 :math:`(-\infty, -1)` 上是凹的；当 :math:`-1 < x < 3` 时, :math:`y'' < 0`, 所以曲线 在 :math:`(-1, 3)` 上是凸的；当 :math:`3 < x < +\infty` 时,
   :math:`y'' > 0`, 所以曲线 在 :math:`(3, +\infty)` 上是凹的. 相应地, 拐点为 :math:`(-1, -2e), (3, 14e^{-3})`.

4. 求参数 :math:`h > 0`, 使曲线 :math:`y = \dfrac{h}{\pi} e^{-h^2x^2}` 在 :math:`x = \pm \sigma` (:math:`\sigma > 0` 为给定的常数) 处有拐点.

.. proof:solution::

   函数 :math:`y = \dfrac{h}{\sqrt{\pi}} e^{-h^2x^2}` 的二阶导函数为 :math:`y'' = \dfrac{2h^3(2h^2x^2 - 1)}{\sqrt{\pi}} e^{-h^2x^2}`.
   令 :math:`y'' = 0` 解得 :math:`x = \pm \dfrac{1}{\sqrt{2} h}`. 在 :math:`x \in (-\infty, -\dfrac{1}{\sqrt{2} h})` 时, :math:`y'' > 0`,
   曲线 在 :math:`(-\infty, -\dfrac{1}{\sqrt{2} h})` 上是凹的；在 :math:`x \in (-\dfrac{1}{\sqrt{2} h}, \dfrac{1}{\sqrt{2} h})` 时, :math:`y'' < 0`,
   曲线 在 :math:`(-\dfrac{1}{\sqrt{2} h}, \dfrac{1}{\sqrt{2} h})` 上是凸的；在 :math:`x \in (\dfrac{1}{\sqrt{2} h}, +\infty)` 时, :math:`y'' > 0`,
   曲线 在 :math:`(\dfrac{1}{\sqrt{2} h}, +\infty)` 上是凹的. 因此, 当 :math:`h = \dfrac{1}{\sqrt{2} \sigma}` 时, 曲线在 :math:`x = \pm \sigma` 处有拐点.

5. 证明: 若 :math:`f(x)` 二阶可导, 且 :math:`f''(x) > 0, f(0) = 0`, 则 :math:`F(x) = \dfrac{f(x)}{x}` 在 :math:`(0, +\infty)` 上单调递增.

.. proof:proof::

   函数 :math:`F(x) = \dfrac{f(x)}{x}` 的导函数为 :math:`F'(x) = \dfrac{f'(x) x - f(x)}{x^2}`. 令 :math:`g(x) = f'(x) x - f(x)`, 那么

   .. math::

      g'(x) = f''(x) x + f'(x) - f'(x) = f''(x) x > 0,

   所以 :math:`g(x)` 在 :math:`(0, +\infty)` 上单调递增, 从而有 :math:`g(x) > g(0) = 0` 对一切 :math:`x > 0` 成立. 因此 :math:`F'(x) > 0` 对一切 :math:`x > 0` 成立,
   即知 :math:`F(x)` 在 :math:`(0, +\infty)` 上单调递增.


§2.10 函数的极值与最大值最小值
--------------------------------

1. 求下列函数的极值:

   (1). :math:`y = 2x^3 - 3x^2 - 12x + 20`;

   (3). :math:`y = 1 - (1 - x)^{\frac{2}{3}}`;

   (5). :math:`y = x - \ln x`.

.. proof:solution::

   (1). 函数 :math:`y = 2x^3 - 3x^2 - 12x + 20` 的导函数为 :math:`y' = 6x^2 - 6x - 12`. 令 :math:`y' = 0` 解得 :math:`x = -1, x = 2`.
   函数 :math:`y = 2x^3 - 3x^2 - 12x + 20` 的二阶导函数为 :math:`y'' = 12x - 6`. 当 :math:`x = -1` 时, :math:`y'' = -18 < 0`, 所以 :math:`x = -1` 为极大值点,
   相应的极大值为 :math:`y(-1) = 27`; 当 :math:`x = 2` 时, :math:`y'' = 18 > 0`, 所以 :math:`x = 2` 为极小值点, 相应的极小值为 :math:`y(2) = 0`.

   (3). 函数 :math:`y = 1 - (1 - x)^{\frac{2}{3}}` 的导函数为 :math:`y' = \dfrac{2}{3} (1 - x)^{-\frac{1}{3}}`, 其在 :math:`x_0 = 1` 处不存在.
   在不可导点 :math:`x_0 = 1` 的左侧 (即 :math:`x \in (-\infty, 1)`) 有 :math:`y' > 0`; 在右侧 (即 :math:`x \in (1, +\infty)`) 有 :math:`y' < 0`.
   于是 :math:`x_0 = 1` 为极大值点, 相应的极大值为 :math:`y(1) = 1`.

   (5). 函数 :math:`y = x - \ln x` 的导函数为 :math:`y' = 1 - \dfrac{1}{x}, x > 0`, 令 :math:`y' = 0` 解得 :math:`x = 1`.
   函数 :math:`y = x - \ln x` 的二阶导函数为 :math:`y'' = \dfrac{1}{x^2}`. 当 :math:`x = 1` 时, :math:`y'' = 1 > 0`, 所以 :math:`x = 1` 为极小值点,
   相应的极小值为 :math:`y(1) = 1`.

2. 设 :math:`f(x) = a \ln x + bx^2 + x` 在 :math:`x_1 = 1, x_2 = 2` 处有极值, 求 :math:`a, b` 的值, 并确定是取得极大值还是极小值.

.. proof:solution::

   函数 :math:`f(x) = a \ln x + bx^2 + x` 的定义域为 :math:`(0, +\infty)`, 导函数为 :math:`f'(x) = \dfrac{a}{x} + 2bx + 1, x > 0`.
   因为 :math:`x_1 = 1, x_2 = 2` 是函数 :math:`f(x)` 的极值点, 所以有 :math:`f'(x_1) = f'(x_2) = 0`, 即

   .. math::

      a + 2b + 1 = 0 \\
      \dfrac{a}{2} + 4b + 1 = 0

   解得 :math:`a = -\dfrac{2}{3}, b = -\dfrac{1}{6}`.那么函数 :math:`f(x) = -\dfrac{2}{3} \ln x - \dfrac{1}{6} x^2 + x`,
   其二阶导函数为 :math:`f''(x) = \dfrac{2}{3x^2} - \dfrac{1}{3}`. 因为 :math:`f''(x_1) = \dfrac{1}{3} > 0`, 所以 :math:`x_1 = 1` 为极小值点,
   相应的极小值为 :math:`f(1) = \dfrac{5}{6}`; :math:`f''(x_2) = -\dfrac{1}{6} < 0`, 所以 :math:`x_2 = 2` 为极大值点,
   相应的极大值为 :math:`f(2) = \dfrac{4 - 2 \ln 2}{3}`.

3. 设 :math:`f(x)` 对应的曲线为区间 :math:`I` 上的凹的, 证明: 若 :math:`x_0 \in I` 为 :math:`f(x)` 的极小值点, 则 :math:`x_0` 为 :math:`f(x)` 在 :math:`I` 上的最小值点.

.. proof:proof::

   由于函数 :math:`f(x)` 对应的曲线为区间 :math:`I` 上的凹的, 所以在区间 :math:`I` 上任取两点 :math:`x, y` 有

   .. math::

      \lambda f(x) + (1 - \lambda) f(y) \geqslant f(\lambda x + (1 - \lambda) y), \quad \lambda \in [0, 1].

   特别地, 取 :math:`y = x_0, t = \frac{1}{2}`, 那么有

   .. math::

      f(x) \geqslant 2 f \left( \dfrac{x + x_0}{2} \right) - f(x_0) \geqslant 2 f(x_0) - f(x_0) = f(x_0).

4. 求下列函数在指定区间上的最大值最小值:

   (3). :math:`y = \sqrt{x} \ln x, \quad (0, +\infty)`.

.. proof:solution::

   函数 :math:`y = \sqrt{x} \ln x` 的导函数为 :math:`y' = \dfrac{1}{2 \sqrt{x}} \ln x + \dfrac{1}{\sqrt{x}}, x > 0`.
   令 :math:`y' = 0` 解得 :math:`x = e^{-2}`. 函数 :math:`y = \sqrt{x} \ln x` 的二阶导函数为
   :math:`y'' = -\dfrac{\ln x}{4x\sqrt{x}} + \dfrac{1}{2x\sqrt{x}} - \dfrac{1}{2x\sqrt{x}} = -\dfrac{\ln x}{4x\sqrt{x}}`.
   因为 :math:`y''(e^{-2}) = \dfrac{1}{2e^{-3}} > 0`, 所以 :math:`x = e^{-2}` 为极小值点,
   相应的极小值为 :math:`y(e^{-2}) = -\dfrac{2}{e}`. 这是唯一的极值点, 所以也是最小值点.

7. 求内接于上半椭圆 :math:`\dfrac{x^2}{3^2} + \dfrac{y^2}{4^2} = 1, y \geqslant 0` 的矩形的最大面积.

.. proof:solution::

   设矩形在第一象限的顶点为 :math:`(x, y) = (3\cos t, 4\sin t), t \in (0, \dfrac{\pi}{2})`,
   那么矩形的面积为 :math:`S = 24 \sin t \cos t = 12 \sin 2t`. 容易看出 :math:`S` 在 :math:`t = \dfrac{\pi}{4}`,
   即 :math:`(x, y) = (\dfrac{3}{\sqrt{2}}, \dfrac{4}{\sqrt{2}})` 处取得最大值 :math:`S = 12`.

§2.11 函数作图
--------------------------------

1. 求下列曲线的渐近线:

   (1). :math:`y = \dfrac{2x^3 - 3}{(x - 2)^2}`;

   (2). :math:`y = \sqrt{4x^2 + 4x - 1}`;

   (3). :math:`y = x + \ln x`;

   (4). :math:`y = \dfrac{e^x + x^2}{e^x + 2x}`.

.. proof:solution::

   (1). 由于 :math:`\lim\limits_{x \to 2} \dfrac{2x^3 - 3}{(x - 2)^2} = +\infty`, 所以 :math:`x = 2` 为 :math:`y = \dfrac{2x^3 - 3}{(x - 2)^2}` 的垂直渐近线.

   接下来求斜渐近线. 斜率

   .. math::

      k = \lim\limits_{x \to \infty} \dfrac{y}{x} = \lim\limits_{x \to +\infty} \dfrac{2x^3 - 3}{(x - 2)^2 x} = 2,

   截距

   .. math::

      b & = \lim\limits_{x \to \infty} (y - kx) = \lim\limits_{x \to \infty} \dfrac{2x^3 - 3}{(x - 2)^2} - 2x \\
      & = \lim\limits_{x \to \infty} \dfrac{2x^3 - 3 - 2x^3 + 8x^2 - 8x}{(x - 2)^2} = 8,

   所以 :math:`y = 2x + 8` 为 :math:`y = \dfrac{2x^3 - 3}{(x - 2)^2}` 的斜渐近线.

   (2). 需要区分 :math:`x \to +\infty` 和 :math:`x \to -\infty` 两种情况. 当 :math:`x \to +\infty` 时, 有斜率

   .. math::

      k = \lim\limits_{x \to +\infty} \dfrac{y}{x} = \lim\limits_{x \to +\infty} \dfrac{\sqrt{4x^2 + 4x - 1}}{x} = \lim\limits_{x \to +\infty} \sqrt{4 + \dfrac{4}{x} - \dfrac{1}{x^2}} = 2,

   截距

   .. math::

      b & = \lim\limits_{x \to +\infty} (y - kx) = \lim\limits_{x \to +\infty} \sqrt{4x^2 + 4x - 1} - 2x \\
      & = \lim\limits_{x \to +\infty} \dfrac{4x^2 + 4x - 1 - 4x^2}{\sqrt{4x^2 + 4x - 1} + 2x} = \lim\limits_{x \to +\infty} \dfrac{4 - \frac{1}{x}}{\sqrt{4 + 4\frac{1}{x} - \frac{1}{x^2}} + 2} \\
      & = 1.

   当 :math:`x \to -\infty` 时, 有斜率

   .. math::

      k = \lim\limits_{x \to -\infty} \dfrac{y}{x} = \lim\limits_{x \to -\infty} \dfrac{\sqrt{4x^2 + 4x - 1}}{x} = \lim\limits_{x \to -\infty} - \sqrt{4 + \dfrac{4}{x} - \dfrac{1}{x^2}} = -2,

   截距

   .. math::

      b & = \lim\limits_{x \to -\infty} (y - kx) = \lim\limits_{x \to -\infty} \sqrt{4x^2 + 4x - 1} + 2x \\
      & = \lim\limits_{x \to -\infty} \dfrac{4x^2 + 4x - 1 + 4x^2}{\sqrt{4x^2 + 4x - 1} - 2x} = \lim\limits_{x \to -\infty} \dfrac{4 + \frac{4}{x}}{-\sqrt{4 + 4\frac{1}{x} - \frac{1}{x^2}} - 2} \\
      & = -1.

   所以 :math:`y = \sqrt{4x^2 + 4x - 1}` 的斜渐近线有两条, 分别为 :math:`y = 2x + 1` 和 :math:`y = -2x - 1`.

   (3). 由于 :math:`\lim\limits_{x \to 0^+} \ln x = -\infty`, 所以 :math:`y = x + \ln x` 的垂直渐近线为 :math:`x = 0`. 假设 :math:`y = x + \ln x` 有斜渐近线, 那么斜率

   .. math::

      k = \lim\limits_{x \to +\infty} \dfrac{y}{x} = \lim\limits_{x \to +\infty} \dfrac{x + \ln x}{x} = \lim\limits_{x \to +\infty} \left( 1 + \dfrac{\ln x}{x} \right) = 1,

   截距

   .. math::

      b & = \lim\limits_{x \to +\infty} (y - kx) = \lim\limits_{x \to +\infty} (x + \ln x - x) \\
      & = \lim\limits_{x \to +\infty} \ln x = +\infty,

   所以 :math:`y = x + \ln x` 没有斜渐近线.

   (4). 需要区分 :math:`x \to +\infty` 和 :math:`x \to -\infty` 两种情况. 当 :math:`x \to -\infty` 时, 有斜率

   .. math::

      k = \lim\limits_{x \to -\infty} \dfrac{y}{x} = \lim\limits_{x \to -\infty} \dfrac{e^x + x^2}{xe^x + 2x^2} = \lim\limits_{x \to -\infty} \dfrac{1 + \frac{e^x}{x^2}}{2 + \frac{e^x}{x}} = \dfrac{1}{2},

   截距

   .. math::

      b & = \lim\limits_{x \to -\infty} (y - kx) = \lim\limits_{x \to -\infty} \dfrac{e^x + x^2}{e^x + 2x} - \dfrac{1}{2} x \\
      & = \lim\limits_{x \to -\infty} \dfrac{e^x + x^2 - \frac{1}{2} x (e^x + 2x)}{e^x + 2x} \\
      & = \lim\limits_{x \to -\infty} \dfrac{e^x + x^2 - \frac{1}{2} x e^x - x^2}{e^x + 2x} \\
      & = \lim\limits_{x \to -\infty} \dfrac{e^x - \frac{1}{2} x e^x}{e^x + 2x} \\
      & = 0,

   当 :math:`x \to +\infty` 时, 有斜率

   .. math::

      k = \lim\limits_{x \to +\infty} \dfrac{y}{x} = \lim\limits_{x \to +\infty} \dfrac{e^x + x^2}{xe^x + 2x^2} = \lim\limits_{x \to +\infty} \dfrac{\frac{1}{x} + \frac{x}{e^x}}{1 + \frac{2x}{e^x}} = 0,

   截距

   .. math::

      b & = \lim\limits_{x \to +\infty} (y - kx) = \lim\limits_{x \to +\infty} \dfrac{e^x + x^2}{e^x + 2x} \\
      & = \lim\limits_{x \to +\infty} \dfrac{1 + \frac{x^2}{e^x}}{1 + \frac{2x}{e^x}} \\
      & = 1,

   所以 :math:`y = \dfrac{e^x + x^2}{e^x + 2x}` 的斜渐近线有两条, 分别为 :math:`y = \dfrac{1}{2} x` 和 :math:`y = 1` (水平渐近线).

   此外, 令 :math:`x_0` 为 :math:`e^x + 2x = 0` 的解, 那么

   .. math::

      \lim\limits_{x \to x_0} \dfrac{e^x + x^2}{e^x + 2x} = \infty,

   所以 :math:`y = \dfrac{e^x + x^2}{e^x + 2x}` 的垂直渐近线为 :math:`x = x_0`.

2. 讨论函数性质并作图:

   (1). :math:`y = x^3 - x`;

   (2). :math:`y = \dfrac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}}`;

   (3). :math:`y = x e^x`.

.. proof:solution::

   (1). 函数 :math:`y = x^3 - x` 的导函数为 :math:`y' = 3x^2 - 1`, 令 :math:`y' = 0` 解得 :math:`x = \pm \dfrac{1}{\sqrt{3}}`.
   函数 :math:`y = x^3 - x` 的二阶导函数为 :math:`y'' = 6x`. 当 :math:`x = -\dfrac{1}{\sqrt{3}}` 时, :math:`y'' = -2\sqrt{3} < 0`,
   所以 :math:`x = -\dfrac{1}{\sqrt{3}}` 为极大值点, 相应的极大值为 :math:`y(-\dfrac{1}{\sqrt{3}}) = \dfrac{2}{3\sqrt{3}}`;
   当 :math:`x = \dfrac{1}{\sqrt{3}}` 时, :math:`y'' = 2\sqrt{3} > 0`, 所以 :math:`x = \dfrac{1}{\sqrt{3}}` 为极小值点,
   相应的极小值为 :math:`y(\dfrac{1}{\sqrt{3}}) = -\dfrac{2}{3\sqrt{3}}`.

   在区间 :math:`(-\infty, -\dfrac{1}{\sqrt{3}})` 上有 :math:`y' > 0`, 所以曲线在 :math:`(-\infty, -\dfrac{1}{\sqrt{3}})` 上单调递增；
   在区间 :math:`(-\dfrac{1}{\sqrt{3}}, \dfrac{1}{\sqrt{3}})` 上有 :math:`y' < 0`, 所以曲线在 :math:`(-\dfrac{1}{\sqrt{3}}, \dfrac{1}{\sqrt{3}})` 上单调递减；
   在区间 :math:`(\dfrac{1}{\sqrt{3}}, +\infty)` 上有 :math:`y' > 0`, 所以曲线在 :math:`(\dfrac{1}{\sqrt{3}}, +\infty)` 上单调递增.

   令 :math:`y'' = 0` 解得 :math:`x = 0`, 相应的函数值为 :math:`y(0) = 0`. 当 :math:`x < 0` 时, :math:`y'' < 0`, 曲线在 :math:`(-\infty, 0)` 上是凸的；
   当 :math:`x > 0` 时, :math:`y'' > 0`, 曲线在 :math:`(0, +\infty)` 上是凹的. 因此 :math:`x = 0` 为拐点.

   .. tikz:: 函数 :math:`y = x^3 - x` 的图像
      :align: center
      :xscale: 50

      \draw[->] (-2, 0) -- (2, 0) node[right] {$x$};
      \draw[->] (0, -2.5) -- (0, 2.5) node[above] {$y$};
      \draw[domain=-1.5:1.5, smooth, variable=\x, blue] plot ({\x}, {\x*\x*\x - \x});

   (2). 函数 :math:`y = \dfrac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}}` 的导函数为 :math:`y' = -\dfrac{1}{\sqrt{2\pi}} x e^{-\frac{x^2}{2}}`,
   令 :math:`y' = 0` 解得 :math:`x = 0`. 函数 :math:`y = \dfrac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}}` 的二阶导函数为
   :math:`y'' = \dfrac{1}{\sqrt{2\pi}} (x^2 - 1) e^{-\frac{x^2}{2}}`. 当 :math:`x = 0` 时, :math:`y'' = -\dfrac{1}{\sqrt{2\pi}} < 0`,
   所以 :math:`x = 0` 为极大值点, 相应的极大值为 :math:`y(0) = \dfrac{1}{\sqrt{2\pi}}`.

   在区间 :math:`(-\infty, 0)` 上有 :math:`y' > 0`, 所以曲线在 :math:`(-\infty, 0)` 上单调递增；在区间 :math:`(0, +\infty)` 上有 :math:`y' < 0`,
   所以曲线在 :math:`(0, +\infty)` 上单调递减.

   令 :math:`y'' = 0` 解得 :math:`x = \pm 1`. 当 :math:`x < -1` 时, :math:`y'' > 0`, 曲线在 :math:`(-\infty, -1)` 上是凹的；
   当 :math:`-1 < x < 1` 时, :math:`y'' < 0`, 曲线在 :math:`(-1, 1)` 上是凸的；当 :math:`x > 1` 时, :math:`y'' > 0`, 曲线在 :math:`(1, +\infty)` 上是凹的.
   因此 :math:`x = \pm 1` 为拐点.

   .. tikz:: 函数 :math:`y = \dfrac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}}` 的图像
      :align: center
      :xscale: 50

      \draw[->] (-2.3, 0) -- (2.3, 0) node[right] {$x$};
      \draw[->] (0, -0.5) -- (0, 0.8) node[above] {$y$};
      \draw[domain=-2:2, smooth, variable=\x, blue] plot ({\x}, {1/sqrt(2*pi) * exp(-\x*\x/2)});

   (3). 函数 :math:`y = x e^x` 的导函数为 :math:`y' = (x + 1) e^x`, 令 :math:`y' = 0` 解得 :math:`x = -1`.
   函数 :math:`y = x e^x` 的二阶导函数为 :math:`y'' = (x + 2) e^x`. 当 :math:`x = -1` 时, :math:`y'' = e^{-1} > 0`,
   所以 :math:`x = -1` 为极小值点, 相应的极小值为 :math:`y(-1) = -\dfrac{1}{e}`.

   在区间 :math:`(-\infty, -1)` 上有 :math:`y' < 0`, 所以曲线在 :math:`(-\infty, -1)` 上单调递减；在区间 :math:`(-1, +\infty)` 上有 :math:`y' > 0`,
   所以曲线在 :math:`(-1, +\infty)` 上单调递增.

   令 :math:`y'' = 0` 解得 :math:`x = -2`. 当 :math:`x < -2` 时, :math:`y'' < 0`, 曲线在 :math:`(-\infty, -2)` 上是凸的；
   当 :math:`x > -2` 时, :math:`y'' > 0`, 曲线在 :math:`(-2, +\infty)` 上是凹的. 因此 :math:`x = -2` 为拐点.

   .. tikz:: 函数 :math:`y = x e^x` 的图像
      :align: center
      :xscale: 50

      \draw[->] (-3.3, 0) -- (1, 0) node[right] {$x$};
      \draw[->] (0, -1) -- (0, 2) node[above] {$y$};
      \draw[domain=-3:0.7, smooth, variable=\x, blue] plot ({\x}, {\x * exp(\x)});

补充内容
=================

§2.3 高阶导数
--------------------------------

莱布尼茨公式 :math:`(uv)^{(n)} = \sum\limits_{k=0}^n C_n^k u^{(k)} v^{(n-k)}` 的证明:

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

§2.6 微分中值定理
--------------------------------

设函数 :math:`f(x)` 在区间 :math:`[a, b]` 上二阶可导, 且 :math:`f(0) = f(1)`, 证明存在 :math:`\xi \in (0, 1)` 使得 :math:`f''(\xi) = \dfrac{2f'(\xi)}{1-\xi}`.

.. proof:proof::

   令

   .. math::

      F(x) = (x - 1)^2 f'(x),

   那么 :math:`F(1) = 0`. 由于 :math:`f(0) = f(1)`, 由罗尔定理知存在 :math:`c \in (0, 1)` 使得 :math:`f'(c) = 0`,
   从而有 :math:`F(c) = (c - 1)^2 f'(c) = 0`. 那么函数 :math:`F(x)` 就是 :math:`[c, 1]` 上连续, :math:`(c, 1)` 上可导的函数, 并且满足 :math:`F(c) = F(1) = 0`.
   再一次利用罗尔定理知, 存在 :math:`\xi \in (c, 1) \subset (0, 1)`, 使得

   .. math::

      0 = F'(\xi) = 2(\xi - 1) f'(\xi) + (\xi - 1)^2 f''(\xi),

   移项得 :math:`f''(\xi) = \dfrac{2f'(\xi)}{1-\xi}`.

§2.7 洛必达法则
--------------------------------

:math:`\dfrac{\infty}{\infty}` 型未定式的洛必达法则证明:

由于有 :math:`\lim\limits_{x \to x_0} = f(x) = \lim\limits_{x \to x_0} = g(x) = \infty`, 所以可以假定在 :math:`x_0` 的某个小的去心邻域
:math:`\mathring{U}(x_0, \delta)` 内有 :math:`f(x) \neq 0, g(x) \neq 0`. 对于包含于 :math:`\mathring{U}(x_0, \delta)`
且在 :math:`x_0` 某一边 (不妨设为右边) 的区间 :math:`[x, y]`, 在其上用柯西中值定理有

.. math::

   & \dfrac{f(x) - f(y)}{g(x) - g(y)} = \dfrac{f'(\xi)}{g'(\xi)}, \quad \xi \in (x, y) \\
   \Longrightarrow & f(x) g'(\xi) = f(y)g'(\xi) + (g(x) - g(y)) f'(\xi) \\
   \Longrightarrow & \dfrac{f(x)}{g(x)} = \dfrac{f(y)}{g(x)} + \left( 1 - \dfrac{g(y)}{g(x)} \right) \dfrac{f'(\xi)}{g'(\xi)}.

那么由于 :math:`\lim\limits_{x \to x_0} = f(x) = \lim\limits_{x \to x_0} = g(x) = \infty`, 对任意的 :math:`K = \dfrac{1}{\varepsilon} \in \mathbb{R}^+`,
以及对任意取定的 :math:`y`, 存在相应的 :math:`x \in (x_0, y) \cap \mathring{U}(x_0, \delta)` 使得

.. math::

   \lvert g(x) \rvert > K \cdot f(y), \quad \lvert g(x) \rvert > K \cdot g(y),

即有

.. math::

   \left\lvert \dfrac{f(y)}{g(x)} \right\rvert < \varepsilon, \quad \left\lvert \dfrac{g(y)}{g(x)} \right\rvert < \varepsilon.

记以上的极限过程为 :math:`\tau` (即让 :math:`y, x` 都趋于 :math:`x_0`, 但先选好 :math:`y`, 再选 :math:`x`, 使得以上关系成立), 那么有

.. math::

   \lim_{\tau} \dfrac{f(x)}{g(x)} & = \lim_{\tau} \left( \dfrac{f(y)}{g(x)} + \left( 1 - \dfrac{g(y)}{g(x)} \right) \dfrac{f'(\xi)}{g'(\xi)} \right) \\
   & = 0 + (1 - 0) \lim_{\tau} \dfrac{f'(\xi)}{g'(\xi)} = \lim_{\tau} \dfrac{f'(\xi)}{g'(\xi)}.

在极限过程 :math:`\tau` 中, 同样有 :math:`\xi \to x_0`, 所以

.. math::

   \lim_{\tau} \dfrac{f'(\xi)}{g'(\xi)} & = \lim_{\xi \to x_0} \dfrac{f'(\xi)}{g'(\xi)} \\
   \lim_{\tau} \dfrac{f(x)}{g(x)} & = \lim_{\xi \to x_0} \dfrac{f'(\xi)}{g'(\xi)}.

因此 :math:`\lim\limits_{x \to x_0} \dfrac{f(x)}{g(x)} = \lim\limits_{x \to x_0} \dfrac{f'(x)}{g'(x)}` 成立.

§2.8 泰勒公式
--------------------------------

泰勒公式拉格朗日型余项 :math:`R_n(x) = \dfrac{f^{(n+1)}(\xi)}{(n+1)!} (x - x_0)^{n+1}` 的证明:

.. proof:proof::

   由 :math:`R_n(x) = f(x) - P_n(x) = f(x) - \left( f(x_0) + f'(x_0)(x - x_0) + \cdots + \dfrac{f^{(n)}(x_0)}{n!} (x - x_0)^n \right)` 容易算得

   .. math::

      & R_n'(x_0) = R_n''(x_0) = \cdots = R_n^{(n)}(x_0) = 0, \\
      & R_n^{(n+1)}(x) = f^{(n+1)}(x).

   由 Cauchy 中值定理知, 存在 :math:`x_0` 与 :math:`x` 之间的某个数 :math:`\xi_1` 使得

   .. math::

      \dfrac{R_n(x)}{(x - x_0)^{n + 1}} = \dfrac{R_n(x) - R_n(x_0)}{(x - x_0)^{n + 1} - (x_0 - x_0)^{n + 1}} = \dfrac{R_n'(\xi_1)}{(n + 1)(\xi_1 - x_0)^n}
      = \dfrac{1}{n + 1} \cdot \dfrac{R_n'(\xi_1)}{(\xi_1 - x_0)^n}

   再依次利用 Cauchy 中值定理, 有

   .. math::

      \dfrac{R_n(x)}{(x - x_0)^{n + 1}}
      & = \dfrac{1}{n + 1} \cdot \dfrac{R_n'(\xi_1)}{(\xi_1 - x_0)^n}
        = \dfrac{1}{n + 1} \cdot \dfrac{R_n'(\xi_1) - R_n'(x_0)}{(\xi_1 - x_0)^n - (x_0 - x_0)^n} \\
      & = \dfrac{1}{n + 1} \cdot \dfrac{1}{n} \cdot \dfrac{R_n''(\xi_2)}{(\xi_2 - x_0)^{n-1}}
        = \dfrac{1}{n + 1} \cdot \dfrac{1}{n} \cdot \dfrac{R_n''(\xi_2) - R_n''(x_0)}{(\xi_2 - x_0)^{n-1} - (x_0 - x_0)^{n-1}} \\
      & \vdots \\
      & = \dfrac{1}{n + 1} \cdot \dfrac{1}{n} \cdots \cdot \dfrac{1}{2} \cdot \dfrac{R_n^{(n)}(\xi_n)}{(\xi_n - x_0)}
        = \dfrac{1}{n + 1} \cdot \dfrac{1}{n} \cdots \cdot \dfrac{1}{2} \cdot \dfrac{R_n^{(n)}(\xi_n) - R_n^{(n)}(x_0)}{(\xi_n - x_0) - (x_0 - x_0)} \\
      & = \dfrac{1}{(n + 1)!} R_n^{(n+1)}(\xi_{n+1}),

   其中 :math:`\xi_{k+1}` 在 :math:`\xi_k` 与 :math:`x_0` 之间. 由于 :math:`R_n^{(n+1)}(\xi_{n+1}) = f^{(n+1)}(\xi_{n+1})`,
   所以令 :math:`\xi = \xi_{n+1}` 即有

   .. math::

      R_n(x) = \dfrac{f^{(n+1)}(\xi)}{(n+1)!} (x - x_0)^{n+1}.
