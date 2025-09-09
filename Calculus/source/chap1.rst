第一章  预备知识
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. contents:: :local:


课后习题解答
================================

§1.1 函数的概念与性质
--------------------------------

§1.2 反函数与复合函数
--------------------------------

§1.3 基本初等函数、初等函数
--------------------------------

§1.4 函数的极坐标方程与参数方程
--------------------------------

补充内容
================================

1. 三角函数

.. tikz:: 三角函数图示
   :align: center
   :xscale: 85
   :libs: angles, quotes, arrows.meta, positioning, fit, calc, decorations.pathreplacing, shapes.misc
   :packages: amsfonts, amsmath, amssymb

   \tikzset{>=Stealth, scale=3.6}

   \definecolor{sinColor}{RGB}{255,0,0}
   \definecolor{cosColor}{RGB}{0,0,255}
   \definecolor{versinColor}{RGB}{0,128,0}
   \definecolor{exsecColor}{RGB}{255,0,255}
   \definecolor{secColor}{RGB}{0,128,128}
   \definecolor{tanColor}{RGB}{165,42,42}
   \definecolor{cotColor}{RGB}{255,165,0}
   \definecolor{excscColor}{RGB}{0,165,0}
   \definecolor{cvsColor}{RGB}{0,255,255}
   \definecolor{cscColor}{RGB}{255,192,203}
   \definecolor{crdColor}{RGB}{128,128,128}

   \def\myangle{60}
   \pgfmathsetmacro{\costheta}{cos(\myangle)}
   \pgfmathsetmacro{\sintheta}{sin(\myangle)}
   \pgfmathsetmacro{\sectheta}{1/cos(\myangle)}
   \pgfmathsetmacro{\csctheta}{1/sin(\myangle)}
   \pgfmathsetmacro{\cottheta}{cos(\myangle)/sin(\myangle)}
   \pgfmathsetmacro{\versin}{1 - \costheta}
   \pgfmathsetmacro{\exsec}{\sectheta - 1}
   \pgfmathsetmacro{\excsc}{\csctheta - 1}

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
   \coordinate (Z1) at ({1.4*cos(\myangle)},{1.4*sin(\myangle)});
   \coordinate (Z2) at (-0.55, 0);

   \draw[line width=3.2pt] (D) arc[start angle=0, end angle=\myangle, radius=1] node[near start, right] {$\mathrm{arc}$};

   \draw[thick] (O) -- (0.1,0) arc[start angle=0, end angle=\myangle, radius=0.1];
   \node at ({0.15*cos(\myangle/2)},{0.15*sin(\myangle/2)}) {$\theta$};

   \draw[sinColor, ultra thick] (A) -- (C) node[midway, right, draw, thick, inner sep=1.5pt, xshift=0.2em, yshift=-2ex] {$\sin$};
   \draw[sinColor, ultra thick] (O) -- (G);
   \draw[gray, dashed, ultra thick] (C) -- (B);
   \draw[dashed, ultra thick] (O) -- (B);
   \draw[dashed, ultra thick] (A) -- (Z1);
   \pic[draw, ultra thick, angle radius=0.2cm] {right angle = O--C--A};
   \pic[draw, ultra thick, angle radius=0.2cm] {right angle = F--A--Z1};
   \pic[draw, ultra thick, angle radius=0.2cm] {right angle = O--G--A};

   \draw[cosColor, ultra thick] (O) -- (C) node[midway, below, inner sep=1.5pt, draw, thick, yshift=-0.5ex] {$\cos$};
   \draw[cosColor, ultra thick] (A) -- (G);

   \draw[ultra thick] (O) -- (A) node[midway, right] {$1$};
   \draw[tanColor, ultra thick] (A) -- (E) node[midway, above, sloped, draw, thick, inner sep=1.5pt, yshift=0.5ex] {$\tan$};

   \draw[secColor, dashed, ultra thick] (O) -- (0, -0.55);
   \draw[secColor, dashed, ultra thick] (E) -- ($(E) + (0, -0.55)$);
   \draw[secColor, ultra thick, |<->|] (-0.008, -0.5) -- ($(E) + (0.008, -0.5)$) node[midway, below, sloped, draw, thick, inner sep=1.5pt, yshift=-0.5ex] {$\sec$};

   \draw[cscColor, dashed, ultra thick] (O) -- (Z2);
   \draw[cscColor, dashed, ultra thick] (F) -- ($(F) + (Z2)$);
   \draw[cscColor, ultra thick, |<->|] (-0.5, -0.008) -- ($(F) + (-0.5, 0.008)$) node[midway, left, draw, thick, inner sep=1.5pt, xshift=-0.2em] {$\csc$};
   \pic[draw, ultra thick, angle radius=0.2cm] {right angle = G--O--Z2};

   \draw[cotColor, ultra thick, sloped] (A) -- (F) node[midway, above, draw, thick, inner sep=1.5pt, yshift=0.5ex] {$\cot$};

   \draw[versinColor, ultra thick] (C) -- (D) node[midway, below] {$\mathrm{versin}$};

   \draw[exsecColor, ultra thick] (D) -- (E) node[midway, below] {$\mathrm{exsec}$};

   \draw[excscColor, ultra thick] (H) -- (F) node[midway, left] {$\mathrm{excsc}$};

   \draw[cvsColor, ultra thick] (H) -- (G) node[midway, left] {$\mathrm{cvs}$};

   \draw[crdColor, ultra thick] (D) -- (A) node[midway, above, sloped, yshift=-0.3ex] {$\mathrm{crd}$};
