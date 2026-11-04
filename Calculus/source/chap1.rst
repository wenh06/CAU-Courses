第一章  预备知识
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. contents:: :local:

.. _ex-chap1:

课后习题解答
================================

.. _ex-chap1-sec1:

§1.1 函数的概念与性质
--------------------------------

1. 下列给定的各对函数是否相同.

   (1). :math:`y = \ln x^2` 与 :math:`y = 2\ln x`;

   (2). :math:`y = \sqrt{x(1-x)}` 与 :math:`y = \sqrt{x}\sqrt{1-x}`.

.. proof:solution::

   (1). 两者定义域不同: :math:`y = \ln x^2` 只要求 :math:`x \neq 0`, 而 :math:`y = 2\ln x` 要求 :math:`x > 0`, 因此不是相同的函数.

   (2). 两者都要求 :math:`0 \leqslant x \leqslant 1`, 定义域相同, 且在共同定义域内 :math:`\sqrt{x}\sqrt{1-x} = \sqrt{x(1-x)}` 处处成立, 因此是相同的函数.

2. 确定下列函数的定义域.

   (1). :math:`y = \sqrt{4-x^2}`;

   (2). :math:`y = \arcsin\dfrac{x-1}{3}`.

.. proof:solution::

   (1). 要求 :math:`4 - x^2 \geqslant 0`, 故定义域为 :math:`[-2, 2]`.

   (2). 要求 :math:`-1 \leqslant \dfrac{x-1}{3} \leqslant 1`, 即 :math:`-2 \leqslant x \leqslant 4`, 故定义域为 :math:`[-2, 4]`.

.. _ex-chap1-sec1-ex3:

3. 判断下列函数的奇偶性.

   (1). :math:`f(x) = x\sin x`;

   (2). :math:`f(x) = \dfrac{e^x - e^{-x}}{e^x + e^{-x}}`;

   (3). :math:`f(x) = \ln(\sqrt{1+x^2}-x)`;

   (4). :math:`f(x) = 3^x x`.

.. proof:solution::

   (1). :math:`f(-x) = (-x)\sin(-x) = x\sin x = f(x)`, 为偶函数.

   (2). :math:`f(-x) = \dfrac{e^{-x} - e^{x}}{e^{-x} + e^{x}} = \dfrac{-(e^{x} - e^{-x})}{e^{x} + e^{-x}} = -f(x)`, 为奇函数.

   (3). 计算 :math:`f(-x) = \ln(\sqrt{1+(-x)^2}-(-x)) = \ln(\sqrt{1+x^2}+x) = \ln\frac{1}{\sqrt{1+x^2}-x} = -\ln(\sqrt{1+x^2}-x) = -f(x)`, 故为奇函数.

   (4). :math:`f(-x) = 3^{-x}\cdot(-x) = -\dfrac{x}{3^{x}}`, 它既不等于 :math:`f(x) = 3^{x}x`, 也不等于 :math:`-f(x)`, 故既非奇函数也非偶函数.

4. 判断下列函数的单调性.

   (1). :math:`y = 3x + 2`;

   (2). :math:`y = 2^x`;

   (3). :math:`y = \log_{\frac{1}{2}} x`;

   (4). :math:`y = x + \ln x`.

.. proof:solution::

   (1). 一次函数斜率 :math:`3 > 0`, 在 :math:`\mathbb{R}` 上单调增加.

   (2). 指数函数底数 :math:`2 > 1`, 在 :math:`\mathbb{R}` 上单调增加.

   (3). 对数函数底数 :math:`0 < \dfrac{1}{2} < 1`, 在 :math:`(0, +\infty)` 上单调减少.

   (4). 设 :math:`0 < x_1 < x_2`, 则 :math:`x_1 < x_2` 且 :math:`\ln x_1 < \ln x_2`, 两式相加得 :math:`x_1 + \ln x_1 < x_2 + \ln x_2`, 故在 :math:`(0, +\infty)` 上单调增加.

5. 已知 :math:`f(x)` 是周期函数, 判断下列函数是否为周期函数.

   (1). :math:`|f(x)|`;

   (2). :math:`f^2(x)`;

   (3). :math:`f(3x+1)`.

.. proof:solution::

   设 :math:`f(x)` 的一个周期为 :math:`T`, 则:

   (1). :math:`|f(x+T)| = |f(x)|`, 是周期函数.

   (2). :math:`f^2(x+T) = f^2(x)`, 是周期函数.

   (3). :math:`f\left(3\left(x + \dfrac{T}{3}\right) + 1\right) = f(3x + T + 1) = f(3x+1)`, 是周期函数, 且 :math:`\dfrac{T}{3}` 是它的一个周期.

6. 证明下列函数是有界函数.

   (1). :math:`y = \dfrac{x^2}{x^2+1}`;

   (2). :math:`y = \dfrac{x}{x^2+1}`.

.. proof:solution::

   (1). :math:`y = \dfrac{x^2}{x^2+1} = 1 - \dfrac{1}{x^2+1}`, 由 :math:`0 < \dfrac{1}{x^2+1} \leqslant 1` 得 :math:`0 \leqslant y < 1`, 故在 :math:`\mathbb{R}` 上有界.

   (2). 由 :math:`2|x| \leqslant x^2 + 1` 得 :math:`\left|\dfrac{x}{x^2+1}\right| \leqslant \dfrac{1}{2}`, 故在 :math:`\mathbb{R}` 上有界.

.. _ex-chap1-sec2:

§1.2 反函数与复合函数
--------------------------------

1. 求下列函数的反函数.

   (1). :math:`y = \sqrt[3]{x+2}`;

   (2). :math:`y = \dfrac{2-x}{2+x}`;

   (3). :math:`y = 3\sin 2x, ~ x \in \left[-\dfrac{\pi}{4}, \dfrac{\pi}{4}\right]`;

   (4). :math:`y = 2 + \ln(x+1)`.

.. proof:solution::

   (1). 由 :math:`y = \sqrt[3]{x+2}` 解得 :math:`x = y^3 - 2`, 故反函数为 :math:`y = x^3 - 2`, :math:`x \in \mathbb{R}`.

   (2). 由 :math:`y = \dfrac{2-x}{2+x}` 解得 :math:`x = \dfrac{2-2y}{1+y}`, 故反函数为 :math:`y = \dfrac{2-2x}{1+x}`, :math:`x \neq -1`.

   (3). 由 :math:`y = 3\sin 2x` 解得 :math:`x = \dfrac{1}{2}\arcsin\dfrac{y}{3}`, 故反函数为 :math:`y = \dfrac{1}{2}\arcsin\dfrac{x}{3}`, :math:`x \in [-3, 3]`.

   (4). 由 :math:`y = 2 + \ln(x+1)` 解得 :math:`x = e^{y-2} - 1`, 故反函数为 :math:`y = e^{x-2} - 1`, :math:`x \in \mathbb{R}`.

2. 下列函数是由哪些较简单的函数复合而成的.

   (1). :math:`y = \cos^4(1+3x)`;

   (2). :math:`y = \ln\left|\sin\sqrt{1-2x}\right|`.

.. proof:solution::

   (1). 由 :math:`y = u^4`, :math:`u = \cos v`, :math:`v = 1 + 3x` 复合而成.

   (2). 由 :math:`y = \ln u`, :math:`u = |v|`, :math:`v = \sin w`, :math:`w = \sqrt{t}`, :math:`t = 1 - 2x` 复合而成.

.. _ex-chap1-sec2-ex3:

3. 设 :math:`f(x-2) = e^{x^2}`, 求 :math:`f(x)`.

.. proof:solution::

   由 :math:`f(x-2) = e^{x^2} = e^{((x-2)+2)^2} = e^{(x-2)^2 + 4(x-2) + 4}`, 知 :math:`f(x) = e^{x^2 + 4x + 4}`.

4. 设 :math:`f(x) = \begin{cases} 2x, & 0 \leqslant x \leqslant 1 \\ x^2, & 1 < x \leqslant 2, \end{cases}`
   :math:`g(x) = \ln x`, 求 :math:`f[g(x)]`.

.. proof:solution::

   引入中间变量 :math:`u`, 将题目重写为 :math:`f(u) = \begin{cases} 2u, & 0 \leqslant u \leqslant 1 \\ u^2, & 1 < u \leqslant 2, \end{cases}`,
   :math:`u = g(x) = \ln x`, 那么

   .. math::
      f[g(x)] = \begin{cases} 2\ln x, & 1 \leqslant x \leqslant e \\ (\ln x)^2, & e < x \leqslant e^2. \end{cases}

   这里关键是定义域要计算清楚.

.. _ex-chap1-sec3:

§1.3 基本初等函数、初等函数
--------------------------------

1. 设函数 :math:`f(x) = \begin{cases} -x, & x \leqslant 0 \\ 0, & x > 0, \end{cases}`

   (1). 证明: :math:`f(x) = \dfrac{|x|-x}{2}`;

   (2). 请问 :math:`f(x)` 是否为初等函数?

.. proof:solution::

   (1). 当 :math:`x \leqslant 0` 时, :math:`\dfrac{|x|-x}{2} = \dfrac{-x-x}{2} = -x = f(x)`; 当 :math:`x > 0` 时, :math:`\dfrac{|x|-x}{2} = \dfrac{x-x}{2} = 0 = f(x)`. 综上 :math:`f(x) = \dfrac{|x|-x}{2}` 成立.

   (2). 是初等函数. 由 (1), :math:`f(x) = \dfrac{\sqrt{x^2}-x}{2}`, 它由常数函数、幂函数 :math:`u = \sqrt{v}` (:math:`v = x^2`) 与多项式函数经四则运算构成, 因此是初等函数.

.. _ex-chap1-sec3-ex2:

2. 设 :math:`f\left( x - \dfrac{1}{x} \right) = x^2 + \dfrac{1}{x^2}`, 求 :math:`f(x)`.

.. proof:solution::

   将原式变形:

   .. math::
      f\left( x - \dfrac{1}{x} \right) = x^2 + \dfrac{1}{x^2}
      = x^2 + \dfrac{1}{x^2} - 2 + 2 = \left( x - \dfrac{1}{x} \right)^2 + 2,

   所以 :math:`f(x) = x^2 + 2`.

3. 证明: 双曲正弦函数 :math:`\sinh x = \dfrac{e^x - e^{-x}}{2}` 的反函数为 :math:`y = \ln(x + \sqrt{x^2+1})`.

.. proof:solution::

   设 :math:`y = \sinh x = \dfrac{e^x - e^{-x}}{2}`, 从中解出 :math:`x`. 令 :math:`u = e^x > 0`, 则 :math:`2y = u - \dfrac{1}{u}`, 即 :math:`u^2 - 2yu - 1 = 0`, 解得 :math:`u = y + \sqrt{y^2+1}` (负根 :math:`y - \sqrt{y^2+1} < 0` 舍去), 于是 :math:`x = \ln\left(y + \sqrt{y^2+1}\right)`. 因此反函数为 :math:`y = \ln\left(x + \sqrt{x^2+1}\right)`, 其定义域为 :math:`\mathbb{R}`.

.. _ex-chap1-sec4:

§1.4 函数的极坐标方程与参数方程
--------------------------------

1. 已知下列点的极坐标, 求它们的直角坐标.

   :math:`A\left(2, \dfrac{\pi}{6}\right)`;
   :math:`B\left(3, \dfrac{\pi}{2}\right)`;
   :math:`C\left(1, -\dfrac{\pi}{4}\right)`;
   :math:`D\left(4, \dfrac{5\pi}{4}\right)`.

.. proof:solution::

   由 :math:`x = r\cos\theta`, :math:`y = r\sin\theta` 逐点计算:

   :math:`A\left(\sqrt{3}, 1\right)`; :math:`B(0, 3)`; :math:`C\left(\dfrac{\sqrt{2}}{2}, -\dfrac{\sqrt{2}}{2}\right)`; :math:`D\left(-2\sqrt{2}, -2\sqrt{2}\right)`.

2. 已知下列点的直角坐标, 求它们的极坐标.

   :math:`A(1, \sqrt{3})`;
   :math:`B(-\sqrt{3}, 1)`;
   :math:`C(-1, \sqrt{3})`;
   :math:`D(\sqrt{3}, -1)`.

.. proof:solution::

   由 :math:`r = \sqrt{x^2+y^2}`, :math:`\tan\theta = \dfrac{y}{x}` (按点所在象限取 :math:`\theta`) 逐点计算:

   :math:`A\left(2, \dfrac{\pi}{3}\right)`; :math:`B\left(2, \dfrac{5\pi}{6}\right)`; :math:`C\left(2, \dfrac{2\pi}{3}\right)`; :math:`D\left(2, -\dfrac{\pi}{6}\right)`.

3. 将下列直角坐标方程化为极坐标方程 (需要标明 :math:`\theta` 的取值范围).

   (1). :math:`x = 1`;

   (2). :math:`x + y = 1`;

   (3). :math:`(x-1)^2 + y^2 = 1`.

.. proof:solution::

   代入 :math:`x = r\cos\theta`, :math:`y = r\sin\theta`:

   (1). :math:`r\cos\theta = 1`, 即 :math:`r = \dfrac{1}{\cos\theta}`, :math:`\theta \in \left(-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right)`.

   (2). :math:`r(\cos\theta + \sin\theta) = 1`, 即 :math:`r = \dfrac{1}{\cos\theta + \sin\theta}`, :math:`\theta \in \left(-\dfrac{\pi}{4}, \dfrac{3\pi}{4}\right)`.

   (3). 将 :math:`(x-1)^2 + y^2 = 1` 展开得 :math:`x^2 + y^2 = 2x`, 即 :math:`r^2 = 2r\cos\theta`, 故 :math:`r = 2\cos\theta`, :math:`\theta \in \left[-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right]`.

4. 将下列极坐标方程化为直角坐标方程, 并说明方程所表示的曲线类型.

   (1). :math:`r = 1, ~ \theta \in [0, \pi]`;

   (2). :math:`\theta = \dfrac{3\pi}{4}`.

.. proof:solution::

   (1). :math:`r = 1` 即 :math:`x^2 + y^2 = 1`; 又 :math:`\theta \in [0, \pi]` 时 :math:`y = r\sin\theta \geqslant 0`, 故曲线为单位圆的上半圆 (含两端点).

   (2). :math:`\theta = \dfrac{3\pi}{4}` 表示从原点出发、极角为 :math:`\dfrac{3\pi}{4}` 的射线, 即 :math:`y = -x` (:math:`x \leqslant 0`).

5. 将下列参数方程化为直角坐标方程, 并说明方程所表示的曲线类型.

   (1). :math:`\begin{cases} x = t^2 + 1, \\ y = t^2 - 2; \end{cases}`

   (2). :math:`\begin{cases} x = t + t^{-1}, \\ y = t - t^{-1}. \end{cases}`

.. proof:solution::

   (1). 两式相减得 :math:`y = x - 3`; 由 :math:`x = t^2 + 1 \geqslant 1` 知曲线为射线 :math:`y = x - 3` (:math:`x \geqslant 1`).

   (2). 由

   .. math::
      x^2 - y^2 = \left(t + \dfrac{1}{t}\right)^2 - \left(t - \dfrac{1}{t}\right)^2 = 4

   得 :math:`x^2 - y^2 = 4`, 曲线是等轴双曲线; 又 :math:`|x| = \left|t + \dfrac{1}{t}\right| \geqslant 2`, 故为该双曲线的左、右两支.

.. _ex-chap1-zong:

总习题 1
--------------------------------

1. 下列函数不相等的是 (   ).

   A. :math:`y = \cos^2(3x+2)`, :math:`u = 1 - \sin^2(3t+2)`;

   B. :math:`f(x) = \dfrac{x^2-4}{x-2}`, :math:`g(x) = x+2`;

   C. :math:`f(x) = \sqrt{x^2}`, :math:`g(x) = |x|`;

   D. :math:`f(x) = \sqrt[3]{x^3}`, :math:`g(x) = x`.

.. proof:solution::

   选 B. A 中两函数仅变量记号不同, 且 :math:`\cos^2(3x+2) = 1 - \sin^2(3x+2)`, 定义域都是 :math:`\mathbb{R}`, 两函数相等; C 中 :math:`\sqrt{x^2} = |x|`, D 中 :math:`\sqrt[3]{x^3} = x`, 定义域与对应法则都相同, 均相等. 而 B 中 :math:`f(x) = \dfrac{x^2-4}{x-2}` 的定义域为 :math:`x \neq 2`, 与 :math:`g(x) = x+2` 的定义域 :math:`\mathbb{R}` 不同, 故两函数不相等.

.. _extra-chap1:

补充内容
================================

.. _extra-chap1-topic1:

1. 三角函数

   课程中涉及的三角函数图示如下:

   .. tikz:: 三角函数图示
      :align: center
      :xscale: 85
      :libs: angles, quotes, arrows.meta, positioning, fit, calc, decorations.pathreplacing, shapes.misc
      :packages: amsfonts, amsmath, amssymb

      \tikzset{>=Stealth, scale=3.6}

      \definecolor{sinColor}{RGB}{255,0,0}
      \definecolor{cosColor}{RGB}{0,0,255}
      \definecolor{versinColor}{RGB}{0,96,0}
      \definecolor{exsecColor}{RGB}{255,0,255}
      \definecolor{secColor}{RGB}{0,168,192}
      \definecolor{tanColor}{RGB}{165,42,42}
      \definecolor{cotColor}{RGB}{255,165,0}
      \definecolor{excscColor}{RGB}{0,255,0}
      \definecolor{cvsColor}{RGB}{0,255,255}
      \definecolor{cscColor}{RGB}{255,192,203}
      \definecolor{crdColor}{RGB}{128,128,128}
      \definecolor{vercosColor}{RGB}{0,112,192}
      \definecolor{covercosColor}{RGB}{153,50,204}

      \def\myangle{60}
      \pgfmathsetmacro{\costheta}{cos(\myangle)}
      \pgfmathsetmacro{\sintheta}{sin(\myangle)}
      \pgfmathsetmacro{\sectheta}{1/cos(\myangle)}
      \pgfmathsetmacro{\csctheta}{1/sin(\myangle)}
      \pgfmathsetmacro{\cottheta}{cos(\myangle)/sin(\myangle)}
      \pgfmathsetmacro{\versin}{1 - \costheta}
      \pgfmathsetmacro{\exsec}{\sectheta - 1}
      \pgfmathsetmacro{\excsc}{\csctheta - 1}

      \draw[thick] (0,0) circle (1);

      \coordinate (O) at (0,0) node[below left] {$O$};
      \coordinate (A) at (\costheta, \sintheta) node[above right=-0.5ex and 0.1em of A] {$A$};
      \coordinate (B) at (\costheta, -\sintheta) node[below right=0.1ex and 0.1em of B] {$B$};
      \coordinate (C) at (\costheta, 0) node[above right=0.1ex and 0.1em of C] {$C$};
      \coordinate (D) at (1, 0) node[below right=0.1ex and 0.1em of D] {$D$};
      \coordinate (E) at (\sectheta, 0) node[right=0.1em of E] {$E$};
      \coordinate (F) at (0, \csctheta) node[above=0.1ex of F] {$F$};
      \coordinate (G) at (0, \sintheta) node[below left=-0.6ex and -0.2em of G] {$G$};
      \coordinate (H) at (0, 1) node[below right=-0.6ex and -0.3em of H] {$H$};
      \coordinate (K) at (-1, 0) node[left =-0.3ex of K] {$K$};
      \coordinate (L) at (0, -1) node[below =-0.3ex of L] {$L$};
      \coordinate (Z1) at ({1.4*cos(\myangle)},{1.4*sin(\myangle)});
      \coordinate (Z2) at (-0.4, 0);

      \draw[line width=3.2pt] (D) arc[start angle=0, end angle=\myangle, radius=1] node[near start, right] {$\mathrm{arc}$};

      \draw[thick] (O) -- (0.1,0) arc[start angle=0, end angle=\myangle, radius=0.1];
      \node at ({0.15*cos(\myangle/2)},{0.15*sin(\myangle/2)}) {$\theta$};

      \draw[sinColor, ultra thick] (A) -- (C) node[midway, right, draw, thick, inner sep=1.5pt, xshift=0.2em, yshift=-2ex] {$\sin$};
      \draw[sinColor, ultra thick] (O) -- (G);
      % \draw[gray, dashed, ultra thick] (C) -- (B);
      \draw[dashed, ultra thick] (O) -- (B);
      \draw[dashed, ultra thick] (A) -- (Z1);
      \pic[draw, ultra thick, angle radius=0.2cm] {right angle = O--C--A};
      \pic[draw, ultra thick, angle radius=0.2cm] {right angle = F--A--Z1};
      \pic[draw, ultra thick, angle radius=0.2cm] {right angle = O--G--A};

      \draw[cosColor, ultra thick] (O) -- (C) node[midway, below, inner sep=1.5pt, draw, thick, yshift=-0.5ex] {$\cos$};
      \draw[cosColor, ultra thick] (A) -- (G);

      \draw[ultra thick] (O) -- (A) node[midway, right] {$1$};
      \draw[tanColor, ultra thick] (A) -- (E) node[midway, above, sloped, draw, thick, inner sep=1.5pt, yshift=0.5ex] {$\tan$};

      \draw[secColor, dashed, ultra thick] (O) -- (0, -0.4);
      \draw[secColor, dashed, ultra thick] (E) -- ($(E) + (0, -0.4)$);
      \draw[secColor, ultra thick, |<->|] (-0.008, -0.35) -- ($(E) + (0.008, -0.35)$) node[midway, below, sloped, draw, thick, inner sep=1.5pt, yshift=-0.5ex, xshift=2ex] {$\sec$};

      \draw[cscColor, dashed, ultra thick] (O) -- (Z2);
      \draw[cscColor, dashed, ultra thick] (F) -- ($(F) + (Z2)$);
      \draw[cscColor, ultra thick, |<->|] (-0.35, -0.008) -- ($(F) + (-0.35, 0.008)$) node[midway, right, draw, thick, inner sep=1.5pt, xshift=0.2em] {$\csc$};
      \pic[draw, ultra thick, angle radius=0.2cm] {right angle = G--O--Z2};

      \draw[cotColor, ultra thick, sloped] (A) -- (F) node[midway, above, draw, thick, inner sep=1.5pt, yshift=0.5ex] {$\cot$};

      \draw[versinColor, ultra thick] (C) -- (D) node[midway, below] {$\mathrm{versin}$};

      \draw[exsecColor, ultra thick] (D) -- (E) node[midway, below] {$\mathrm{exsec}$};

      \draw[excscColor, ultra thick] (H) -- (F) node[midway, left] {$\mathrm{excsc}$};

      \draw[cvsColor, ultra thick] (H) -- (G) node[midway, left] {$\mathrm{cvs}$};

      \draw[crdColor, ultra thick] (D) -- (A) node[midway, above, sloped, yshift=-0.3ex] {$\mathrm{crd}$};

      \draw[gray, ultra thick, dashed] (-0.4, 0) -- (K);
      \draw[gray, ultra thick, dashed] (0, -0.4) -- (L);

      \draw[vercosColor, ultra thick, dashed] (K) -- ($(K) + (0, -0.7)$);
      \draw[vercosColor, dashed, ultra thick] (C) -- ($(C) + (0, -0.65)$);
      \draw[gray, dashed, ultra thick] ($(C) + (0, -0.65)$) -- (B);
      \draw[vercosColor, ultra thick, |<->|] ($(K) + (-0.008, -0.65)$) -- ($(C) + (0.008, -0.65)$) node[midway, above] {$\mathrm{vercos}$};

      \draw[covercosColor, ultra thick, dashed] (L) -- ($(L) + (-0.7, 0)$);
      \draw[covercosColor, ultra thick, dashed] (G) -- ($(G) + (-0.7, 0)$);
      \draw[covercosColor, ultra thick, |<->|] ($(G) + (-0.65, 0.008)$) -- ($(L) + (-0.65, -0.008)$) node[midway, yshift=-4ex, right] {$\mathrm{covercos}$};

   其中主要需要掌握的是带框的 6 个三角函数:

   - 正弦函数 :math:`\sin`
   - 余弦函数 :math:`\cos`
   - 正切函数 :math:`\tan`
   - 余切函数 :math:`\cot`
   - 正割函数 :math:`\sec`
   - 余割函数 :math:`\csc`

   其他函数如 :math:`\mathrm{versin}, \mathrm{exsec}` 等大部分已经很少使用, 本课程不做要求.
   这些被称作 Obsolete Trigonometric Functions, 大多出现在中世纪阿拉伯数学和 16–18 世纪欧洲数学中,
   后来因为不如 :math:`\sin,\cos,\tan` 等直观，逐渐被淘汰. 这些函数列举如下:

   - 正矢函数 :math:`\mathrm{versin} \theta = 1 - \cos \theta`
   - 余矢函数 :math:`\mathrm{cvs} \theta = 1 - \sin \theta`
   - 正余矢函数 :math:`\mathrm{vercos} \theta = 1 + \cos \theta`
   - 余余矢函数 :math:`\mathrm{covercos} \theta = 1 + \sin \theta`
   - 外割函数 :math:`\mathrm{exsec} \theta = \sec \theta - 1`
   - 外余割函数 :math:`\mathrm{excsc} \theta = \csc \theta - 1`
   - 弦函数 :math:`\mathrm{crd} \theta = 2 \sin \dfrac{\theta}{2}`

.. _extra-chap1-topic2:

2. 椭圆与双曲线的参数方程

   圆 :math:`x^2 + y^2 = r^2` 的参数方程 :math:`x = r\cos t,\ y = r\sin t` 中,
   参数 :math:`t` 就是这点对应的半径与 :math:`x` 轴正方向的夹角.
   椭圆与双曲线的参数方程 :math:`x = a\cos t,\ y = b\sin t` 与
   :math:`x = a\sec t,\ y = b\tan t` 分别来自恒等式
   :math:`\sin^2 t + \cos^2 t = 1` 与 :math:`\sec^2 t - \tan^2 t = 1`,
   但其中的 :math:`t` 都不再是半径 :math:`OP` 与 :math:`x` 轴的夹角,
   其几何意义如下 (记 :math:`P` 为曲线上的点, :math:`\theta` 为 :math:`OP`
   与 :math:`x` 轴正方向的夹角).

   **椭圆** :math:`\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1`:
   以原点为心、:math:`a` 为半径作辅助圆, 椭圆可由辅助圆沿 :math:`y` 轴方向
   压缩 :math:`b/a` 倍得到. 参数 :math:`t` 是辅助圆的半径 :math:`OC` 与
   :math:`x` 轴正方向的夹角: :math:`P` 是辅助圆上的点 :math:`C` 沿竖直方向
   压缩的像, 竖坐标由 :math:`a\sin t` 压缩为 :math:`b\sin t`. 真实夹角满足
   :math:`\tan\theta = \frac{b}{a}\tan t`. 此外 :math:`t` 还与扫过的面积
   成正比: 半径 :math:`OP` 从 :math:`(a, 0)` 扫到 :math:`P`, 掠过的椭圆
   扇形面积恰为 :math:`\frac{ab}{2}t`.

   .. tikz:: 椭圆参数方程的几何意义
      :align: center
      :xscale: 75
      :libs: angles, quotes, arrows.meta, positioning, fit, calc, decorations.pathreplacing, shapes.misc
      :packages: amsfonts, amsmath, amssymb

      \tikzset{>=Stealth, scale=1.5}

      \definecolor{sinColor}{RGB}{255,0,0}
      \definecolor{cosColor}{RGB}{0,0,255}
      \definecolor{ellColor}{RGB}{0,0,255}
      \definecolor{minorColor}{RGB}{0,96,0}
      \definecolor{axisColor}{RGB}{150,150,150}

      \def\ea{2}
      \def\eb{1.2}
      \def\myt{55}
      \pgfmathsetmacro{\ct}{\ea*cos(\myt)}
      \pgfmathsetmacro{\st}{\ea*sin(\myt)}
      \pgfmathsetmacro{\bt}{\eb*sin(\myt)}

      % axes
      \draw[axisColor, ->] (-2.5, 0) -- (2.9, 0);
      \draw[axisColor, ->] (0, -1.8) -- (0, 2.35);

      % auxiliary circle and ellipse
      \draw[thick] (0,0) circle (\ea);
      \draw[ellColor, very thick] (0,0) ellipse [x radius=\ea, y radius=\eb];

      \coordinate (O) at (0,0) node[below left] {$O$};
      \coordinate (C) at (\ct, \st);
      \node at ({\ct + 0.32*cos(\myt)}, {\st + 0.32*sin(\myt)}) {$C$};
      \coordinate (Q) at (\ct, 0) node[below=0.25ex of Q] {$Q$};
      \coordinate (P) at (\ct, \bt);
      \node[right=0.35em of P] {$P$};
      \coordinate (D) at (\ea, 0) node[below right=-0.3ex and -0.3ex of D] {$D$};

      % radius OC and angle t
      \draw[thick] (O) -- (C) node[midway, above, sloped] {$a$};
      \draw[thick] (O) -- (0.15, 0) arc[start angle=0, end angle=\myt, radius=0.15];
      \node at ({0.28*cos(\myt/2)}, {0.28*sin(\myt/2)}) {$t$};

      % OQ = a cos t
      \draw[cosColor, ultra thick] (O) -- (Q) node[pos=0.45, below, draw, thick, inner sep=1.5pt, yshift=-0.4ex] {$a\cos t$};

      % ordinate Q--C (dashed), Q--P solid = b sin t, C->P compression arrow
      \draw[sinColor, dashed, ultra thick] (Q) -- (C);
      \draw[sinColor, ultra thick] (Q) -- (P) node[pos=0.25, right, draw, thick, inner sep=1.5pt, xshift=0.1em] {$b\sin t$};
      \draw[sinColor, dashed, ultra thick, ->] (C) -- (P);

      % right angle at Q
      \pic[draw, thick, angle radius=0.18cm] {right angle = O--Q--C};

      % semi-minor axis b
      \draw[minorColor, ultra thick] (O) -- (0, \eb) node[midway, left] {$b$};

      % curve labels
      \node at ({2.45*cos(118)}, {2.45*sin(118)}) {$x^2+y^2=a^2$};
      \node[ellColor] at (0.55, -1.55) {$\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$};

   **双曲线** :math:`\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 1`:
   从原点作与 :math:`x` 轴夹角为 :math:`t` 的射线, 交辅助圆
   :math:`x^2 + y^2 = a^2` 于点 :math:`C`, 过 :math:`C` 作圆的切线
   (切线垂直于半径 :math:`OC`), 交 :math:`x` 轴于点 :math:`Q`. 则切线的
   截距 :math:`|OQ| = a\sec t`, 切线段 :math:`|CQ| = a\tan t`. 这正是下图
   单位圆中 :math:`\sec` 与 :math:`\tan` 的几何定义放大 :math:`a` 倍.
   双曲线上的点 :math:`P` 位于 :math:`Q` 的正上方: 将横坐标
   :math:`x = a\sec t` 代入双曲线方程, 解得纵坐标
   :math:`y = b\sqrt{\sec^2 t - 1} = b\tan t = \frac{b}{a}|CQ|`,
   即 :math:`P` 的高度恰为切线段 :math:`|CQ|` 沿竖直方向压缩
   :math:`b/a` 倍. 真实夹角满足
   :math:`\tan\theta = \frac{b}{a}\sin t`: 当 :math:`t \to \pm\frac{\pi}{2}`
   时 :math:`P` 沿渐近线 :math:`y = \pm\frac{b}{a}x` 趋向无穷远,
   :math:`\theta` 始终被夹在 :math:`\pm\arctan\frac{b}{a}` 之间,
   而 :math:`t` 可以取遍 :math:`\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)`.

   .. tikz:: 双曲线参数方程的几何意义
      :align: center
      :xscale: 85
      :libs: angles, quotes, arrows.meta, positioning, fit, calc, decorations.pathreplacing, shapes.misc
      :packages: amsfonts, amsmath, amssymb

      \tikzset{>=Stealth, scale=1.5}

      \definecolor{sinColor}{RGB}{255,0,0}
      \definecolor{secColor}{RGB}{0,168,192}
      \definecolor{tanColor}{RGB}{165,42,42}
      \definecolor{hypColor}{RGB}{0,0,255}
      \definecolor{axisColor}{RGB}{150,150,150}

      \def\ea{1.5}
      \def\eb{1.1}
      \def\myt{50}
      \pgfmathsetmacro{\ct}{\ea*cos(\myt)}
      \pgfmathsetmacro{\st}{\ea*sin(\myt)}
      \pgfmathsetmacro{\sectx}{\ea/cos(\myt)}
      \pgfmathsetmacro{\tany}{\eb*tan(\myt)}
      \pgfmathsetmacro{\slope}{\eb/\ea}

      % axes
      \draw[axisColor, ->] (-0.6, 0) -- (3.9, 0);
      \draw[axisColor, ->] (0, -2.35) -- (0, 2.5);

      % asymptotes
      \draw[axisColor, thick, dashed] (0, 0) -- (3.75, {3.75*\slope});
      \draw[axisColor, thick, dashed] (0, 0) -- (3.75, {-3.75*\slope});
      \node[axisColor] at (3.0, 2.62) {\small $y=\dfrac{b}{a}x$};

      % auxiliary circle and hyperbola branch
      \draw[thick] (0,0) circle (\ea);
      \draw[hypColor, very thick] plot[domain=-2.1:2.1, samples=61] ({\ea*sqrt(1+(\x*\x)/(\eb*\eb))}, {\x});

      \coordinate (O) at (0,0) node[below left] {$O$};
      \coordinate (C) at (\ct, \st);
      \node at ({\ct + 0.38*cos(\myt)}, {\st + 0.38*sin(\myt)}) {$C$};
      \coordinate (Q) at (\sectx, 0) node[below=0.25ex of Q] {$Q$};
      \coordinate (P) at (\sectx, \tany);
      \node[left=0.35em of P] {$P$};
      \coordinate (D) at (\ea, 0) node[below right=-0.3ex and -0.3ex of D] {$D$};

      % ray OC and angle t
      \draw[thick] (O) -- (C) node[midway, above, sloped] {$a$};
      \draw[thick] (O) -- (0.15, 0) arc[start angle=0, end angle=\myt, radius=0.15];
      \node at ({0.30*cos(\myt/2)}, {0.30*sin(\myt/2)}) {$t$};

      % tangent at C: solid extension beyond C, dashed C--Q
      % \draw[tanColor, ultra thick] ($(C)!-0.55!(Q)$) -- (C) node[pos=0.15, above, sloped, draw, thick, inner sep=1.5pt] {$a\tan t$};
      \draw[tanColor, dashed, ultra thick] (C) -- ($(C)!1.18!(Q)$);
      \pic[draw, thick, angle radius=0.18cm] {right angle = O--C--Q};

      % OQ = a sec t
      \draw[secColor, ultra thick] (O) -- (Q) node[pos=0.32, below, draw, thick, inner sep=1.5pt, yshift=-0.4ex] {$a\sec t$};

      % ordinate QP = b tan t
      \draw[sinColor, ultra thick] (Q) -- (P) node[pos=0.55, right, draw, thick, inner sep=1.5pt, xshift=0.15em] {$b\tan t$};

      % curve labels
      \node at ({1.95*cos(210)}, {1.95*sin(210)-0.4}) {$x^2+y^2=a^2$};
      \node[hypColor] at (3.7, -1.5) {$\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}=1$};
