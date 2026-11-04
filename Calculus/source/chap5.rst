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

   (1). 直接用幂函数积分公式,

   .. math::
      \int \dfrac{1}{x^2 \sqrt{x}} ~ \mathrm{d}x = \int x^{-\frac{5}{2}} ~ \mathrm{d}x
      = \dfrac{x^{-\frac{3}{2}}}{-\frac{3}{2}} + C = -\dfrac{2}{3x\sqrt{x}} + C.

   (2). :math:`\displaystyle \int \left( x^2 - 3x + 2 \right) \mathrm{d}x = \dfrac{x^3}{3} - \dfrac{3x^2}{2} + 2x + C`.

   (3). 展开后逐项积分,

   .. math::
      \int \dfrac{(1 - x)^2}{\sqrt{x}} ~ \mathrm{d}x
      = \int \left( x^{-\frac{1}{2}} - 2x^{\frac{1}{2}} + x^{\frac{3}{2}} \right) \mathrm{d}x
      = 2\sqrt{x} - \dfrac{4}{3}x\sqrt{x} + \dfrac{2}{5}x^2\sqrt{x} + C.

   (4). :math:`\displaystyle \int \left( 2e^x + \dfrac{3}{x} \right) \mathrm{d}x = 2e^x + 3\ln \lvert x \rvert + C`.

   (5). :math:`\displaystyle \int \left( \dfrac{3}{1 + x^2} - \dfrac{2}{\sqrt{1 - x^2}} \right) \mathrm{d}x = 3\arctan x - 2\arcsin x + C`.

   (6). :math:`\displaystyle \int \sec x (\sec x - \tan x) ~ \mathrm{d}x = \int \left( \sec^2 x - \sec x \tan x \right) \mathrm{d}x = \tan x - \sec x + C`.

   (7). 由半角公式 :math:`\cos^2 \dfrac{x}{2} = \dfrac{1 + \cos x}{2}`,

   .. math::
      \int \cos^2 \dfrac{x}{2} ~ \mathrm{d}x = \dfrac{1}{2} \int (1 + \cos x) ~ \mathrm{d}x = \dfrac{x}{2} + \dfrac{\sin x}{2} + C.

   (8). 由 :math:`1 + \cos 2x = 2\cos^2 x`,

   .. math::
      \int \dfrac{1}{1 + \cos 2x} ~ \mathrm{d}x = \dfrac{1}{2} \int \sec^2 x ~ \mathrm{d}x = \dfrac{1}{2} \tan x + C.

   (9). 先做除法 :math:`\dfrac{3x^4 + 2x^2}{x^2 + 1} = 3x^2 - 1 + \dfrac{1}{x^2 + 1}`, 于是

   .. math::
      \int \dfrac{3x^4 + 2x^2}{x^2 + 1} ~ \mathrm{d}x = x^3 - x + \arctan x + C.

   (10). 部分分式分解 :math:`\dfrac{1}{x^4 + x^6} = \dfrac{1}{x^4 (1 + x^2)} = \dfrac{1}{x^4} - \dfrac{1}{x^2} + \dfrac{1}{1 + x^2}`
   (通分即可验证), 于是

   .. math::
      \int \dfrac{1}{x^4 + x^6} ~ \mathrm{d}x
      = \int \left( x^{-4} - x^{-2} + \dfrac{1}{1 + x^2} \right) \mathrm{d}x
      = -\dfrac{1}{3x^3} + \dfrac{1}{x} + \arctan x + C.

   (11). 通分合并: 当 :math:`|x| < 1` 时,

   .. math::
      \sqrt{\dfrac{1 - x}{1 + x}} + \sqrt{\dfrac{1 + x}{1 - x}}
      = \dfrac{(1-x) + (1+x)}{\sqrt{1 - x^2}} = \dfrac{2}{\sqrt{1 - x^2}},

   于是

   .. math::
      \int \left( \sqrt{\dfrac{1 - x}{1 + x}} + \sqrt{\dfrac{1 + x}{1 - x}} \right) \mathrm{d}x = 2\arcsin x + C.

   (12). 由 :math:`1 + \cos 2x = 2\cos^2 x`,

   .. math::
      \int \dfrac{1 + \cos^2 x}{1 + \cos 2x} ~ \mathrm{d}x
      = \int \dfrac{1 + \cos^2 x}{2 \cos^2 x} ~ \mathrm{d}x
      = \dfrac{1}{2} \int \left( \sec^2 x + 1 \right) \mathrm{d}x
      = \dfrac{1}{2} \tan x + \dfrac{x}{2} + C.

.. _ex-chap5-sec1-ex2:

2. 设 :math:`\displaystyle \int x f(x) ~ \mathrm{d}x = \arccos x + C`, 求 :math:`f(x)`.

.. proof:solution::

   由不定积分与微分的关系, 两边对 :math:`x` 求导,

   .. math::
      x f(x) = \left( \arccos x \right)' = -\dfrac{1}{\sqrt{1 - x^2}},

   因此

   .. math::
      f(x) = -\dfrac{1}{x \sqrt{1 - x^2}}.

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

   设曲线方程为 :math:`y = y(x)`, 由题意 :math:`y' = \dfrac{1}{x}`, 于是

   .. math::
      y = \int \dfrac{1}{x} ~ \mathrm{d}x = \ln \lvert x \rvert + C.

   由曲线过点 :math:`\left( e^2, 3 \right)`: :math:`3 = \ln e^2 + C = 2 + C`, 得 :math:`C = 1`.
   故所求曲线方程为 :math:`y = \ln x + 1` (:math:`x > 0`).

.. _ex-chap5-sec1-ex5:

5. 一物体由静止开始运动, 经 :math:`t` s 后的速度是 :math:`3t^2` m/s, 问:

   (1) 在 :math:`3` s 后物体离开出发点的距离是多少?

   (2) 物体走完 :math:`360` m 需要多少时间?

.. proof:solution::

   设 :math:`t = 0` 时物体位于出发点, 则路程函数

   .. math::
      s(t) = \int 3t^2 ~ \mathrm{d}t = t^3 + C,

   由 :math:`s(0) = 0` 得 :math:`C = 0`, 即 :math:`s(t) = t^3`.

   (1). :math:`3` s 后物体离开出发点的距离为 :math:`s(3) = 3^3 = 27` m.

   (2). 令 :math:`t^3 = 360`, 得 :math:`t = \sqrt[3]{360} \approx 7.11` s.

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

   各空所填系数依次为 (由微分公式 :math:`\mathrm{d}[\varphi(x)] = \varphi'(x) ~ \mathrm{d}x` 逐一反推):

   .. math::
      (1) ~ \dfrac{1}{a}; \quad
      (2) ~ \dfrac{1}{7}; \quad
      (3) ~ \dfrac{1}{2}; \quad
      (4) ~ \dfrac{1}{10}; \quad
      (5) ~ -\dfrac{1}{2}; \quad
      (6) ~ \dfrac{1}{12}; \quad
      (7) ~ \dfrac{1}{2}; \quad
      (8) ~ -2;

   .. math::
      (9) ~ -\dfrac{2}{3}; \quad
      (10) ~ \dfrac{1}{5}; \quad
      (11) ~ -\dfrac{1}{5}; \quad
      (12) ~ \dfrac{1}{3}; \quad
      (13) ~ -1; \quad
      (14) ~ -1; \quad
      (15) ~ 2; \quad
      (16) ~ \dfrac{1}{2}.

   例如 (5): :math:`\mathrm{d}(1 - x^2) = -2x ~ \mathrm{d}x`, 故 :math:`x ~ \mathrm{d}x = -\dfrac{1}{2} ~ \mathrm{d}(1 - x^2)`;
   (13): :math:`\mathrm{d}(1 - \arcsin x) = -\dfrac{\mathrm{d}x}{\sqrt{1 - x^2}}`, 故系数为 :math:`-1`.

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

   (1). :math:`\displaystyle \int e^{5x} ~ \mathrm{d}x = \dfrac{1}{5} e^{5x} + C`.

   (2). :math:`\displaystyle \int (3 - 2x)^3 ~ \mathrm{d}x = -\dfrac{(3 - 2x)^4}{8} + C`.

   (3). :math:`\displaystyle \int \dfrac{1}{1 - 2x} ~ \mathrm{d}x = -\dfrac{1}{2} \ln \lvert 1 - 2x \rvert + C`.

   (4). :math:`\displaystyle \int \dfrac{1}{\sqrt[3]{2 - 3x}} ~ \mathrm{d}x = -\dfrac{1}{2} \left( 2 - 3x \right)^{\frac{2}{3}} + C`.

   (5). :math:`\displaystyle \int \left( \sin ax - e^{\frac{x}{b}} \right) \mathrm{d}x = -\dfrac{\cos ax}{a} - b\, e^{\frac{x}{b}} + C` (:math:`a \neq 0`).

   (6). 令 :math:`u = \sqrt{t}`, :math:`\mathrm{d}t = 2u ~ \mathrm{d}u`, 则

   .. math::
      \int \dfrac{\sin \sqrt{t}}{\sqrt{t}} ~ \mathrm{d}t = 2 \int \sin u ~ \mathrm{d}u = -2 \cos \sqrt{t} + C.

   (7). :math:`\displaystyle \int x e^{-x^2} ~ \mathrm{d}x = -\dfrac{1}{2} \int e^{-x^2} ~ \mathrm{d}(-x^2) = -\dfrac{1}{2} e^{-x^2} + C`.

   (8). :math:`\displaystyle \int x \cos(x^2) ~ \mathrm{d}x = \dfrac{1}{2} \int \cos(x^2) ~ \mathrm{d}(x^2) = \dfrac{1}{2} \sin(x^2) + C`.

   (9). :math:`\displaystyle \int \dfrac{x}{\sqrt{2 - 3x^2}} ~ \mathrm{d}x = -\dfrac{1}{6} \int (2 - 3x^2)^{-\frac{1}{2}} ~ \mathrm{d}(2 - 3x^2) = -\dfrac{1}{3} \sqrt{2 - 3x^2} + C`.

   (10). :math:`\displaystyle \int \dfrac{3x^3}{1 - x^4} ~ \mathrm{d}x = -\dfrac{3}{4} \int \dfrac{\mathrm{d}(1 - x^4)}{1 - x^4} = -\dfrac{3}{4} \ln \lvert 1 - x^4 \rvert + C`.

   (11). 分母的导数 :math:`(x^2 + 2x + 5)' = 2x + 2 = 2(x + 1)` 恰为分子的两倍,

   .. math::
      \int \dfrac{x + 1}{x^2 + 2x + 5} ~ \mathrm{d}x = \dfrac{1}{2} \int \dfrac{\mathrm{d}(x^2 + 2x + 5)}{x^2 + 2x + 5}
      = \dfrac{1}{2} \ln \left( x^2 + 2x + 5 \right) + C.

   (12). :math:`\displaystyle \int \dfrac{\sin x}{\cos^3 x} ~ \mathrm{d}x = -\int \cos^{-3} x ~ \mathrm{d}(\cos x) = \dfrac{1}{2 \cos^2 x} + C`.

   (13). 分子恰为分母所含 :math:`\sin x - \cos x` 的导数, 于是

   .. math::
      \int \dfrac{\sin x + \cos x}{\sqrt[3]{\sin x - \cos x}} ~ \mathrm{d}x
      = \int (\sin x - \cos x)^{-\frac{1}{3}} ~ \mathrm{d}(\sin x - \cos x)
      = \dfrac{3}{2} \left( \sin x - \cos x \right)^{\frac{2}{3}} + C.

   (14). :math:`\displaystyle \int \tan^{10} x \sec^2 x ~ \mathrm{d}x = \int \tan^{10} x ~ \mathrm{d}(\tan x) = \dfrac{\tan^{11} x}{11} + C`.

   (15). 令 :math:`u = \arcsin x`, :math:`\mathrm{d}u = \dfrac{\mathrm{d}x}{\sqrt{1 - x^2}}`, 则

   .. math::
      \int \dfrac{1}{(\arcsin x)^2 \sqrt{1 - x^2}} ~ \mathrm{d}x = \int \dfrac{\mathrm{d}u}{u^2} = -\dfrac{1}{\arcsin x} + C.

   (16). 令 :math:`u = \sqrt{1 + x^2}`, :math:`\mathrm{d}u = \dfrac{x ~ \mathrm{d}x}{\sqrt{1 + x^2}}`, 则

   .. math::
      \int \tan \sqrt{1 + x^2} \cdot \dfrac{x}{\sqrt{1 + x^2}} ~ \mathrm{d}x
      = \int \tan u ~ \mathrm{d}u = -\ln \left\lvert \cos \sqrt{1 + x^2} \right\rvert + C.

   (17). 令 :math:`u = \arctan \sqrt{x}`, :math:`\mathrm{d}u = \dfrac{\mathrm{d}x}{2\sqrt{x}(1 + x)}`, 则

   .. math::
      \int \dfrac{\arctan \sqrt{x}}{\sqrt{x} (1 + x)} ~ \mathrm{d}x = 2 \int u ~ \mathrm{d}u = \left( \arctan \sqrt{x} \right)^2 + C.

   (18). 令 :math:`u = x \ln x`, :math:`\mathrm{d}u = (1 + \ln x) ~ \mathrm{d}x`, 则

   .. math::
      \int \dfrac{1 + \ln x}{(x \ln x)^2} ~ \mathrm{d}x = \int \dfrac{\mathrm{d}u}{u^2} = -\dfrac{1}{x \ln x} + C.

   (19). :math:`\displaystyle \int \dfrac{1}{\sin x \cos x} ~ \mathrm{d}x = \int \dfrac{\mathrm{d}(\tan x)}{\tan x} = \ln \lvert \tan x \rvert + C`.

   (20). 令 :math:`u = \ln \tan x`, :math:`\mathrm{d}u = \dfrac{\sec^2 x}{\tan x} ~ \mathrm{d}x = \dfrac{\mathrm{d}x}{\sin x \cos x}`, 则

   .. math::
      \int \dfrac{\ln \tan x}{\cos x \sin x} ~ \mathrm{d}x = \int u ~ \mathrm{d}u = \dfrac{1}{2} \ln^2 \tan x + C.

   (21). :math:`\displaystyle \int \cos^3 x ~ \mathrm{d}x = \int \left( 1 - \sin^2 x \right) \mathrm{d}(\sin x) = \sin x - \dfrac{\sin^3 x}{3} + C`.

   (22). 由 :math:`\cos^2 u = \dfrac{1 + \cos 2u}{2}`,

   .. math::
      \int \cos^2 (\omega t + \varphi) ~ \mathrm{d}t
      = \dfrac{1}{2} \int \left[ 1 + \cos\left( 2\omega t + 2\varphi \right) \right] \mathrm{d}t
      = \dfrac{t}{2} + \dfrac{\sin\left( 2\omega t + 2\varphi \right)}{4\omega} + C \quad (\omega \neq 0).

   (23). :math:`\displaystyle \int \tan^3 x \sec x ~ \mathrm{d}x = \int \tan^2 x ~ \mathrm{d}(\sec x) = \int \left( \sec^2 x - 1 \right) \mathrm{d}(\sec x) = \dfrac{\sec^3 x}{3} - \sec x + C`.

   (24). 分子分母同乘 :math:`e^x`, 令 :math:`u = e^x`,

   .. math::
      \int \dfrac{1}{e^x + e^{-x}} ~ \mathrm{d}x = \int \dfrac{e^x ~ \mathrm{d}x}{e^{2x} + 1} = \int \dfrac{\mathrm{d}u}{u^2 + 1} = \arctan e^x + C.

   (25). 拆成两项分别积分,

   .. math::
      \int \dfrac{1 - x}{\sqrt{9 - 4x^2}} ~ \mathrm{d}x
      = \int \dfrac{\mathrm{d}x}{\sqrt{9 - 4x^2}} - \int \dfrac{x ~ \mathrm{d}x}{\sqrt{9 - 4x^2}}
      = \dfrac{1}{2} \arcsin \dfrac{2x}{3} + \dfrac{1}{4} \sqrt{9 - 4x^2} + C.

   (26). 先做除法 :math:`\dfrac{x^3}{9 + x^2} = x - \dfrac{9x}{9 + x^2}`, 于是

   .. math::
      \int \dfrac{x^3}{9 + x^2} ~ \mathrm{d}x = \dfrac{x^2}{2} - \dfrac{9}{2} \ln \left( 9 + x^2 \right) + C.

   (27). 令 :math:`x = a \sin t` (:math:`t \in \left( -\frac{\pi}{2}, \frac{\pi}{2} \right)`), :math:`\mathrm{d}x = a \cos t ~ \mathrm{d}t`,

   .. math::
      \int \dfrac{x^2}{\sqrt{a^2 - x^2}} ~ \mathrm{d}x
      = \int a^2 \sin^2 t ~ \mathrm{d}t
      = \dfrac{a^2}{2} \int (1 - \cos 2t) ~ \mathrm{d}t
      = \dfrac{a^2}{2} t - \dfrac{a^2}{4} \sin 2t + C
      = \dfrac{a^2}{2} \arcsin \dfrac{x}{a} - \dfrac{x \sqrt{a^2 - x^2}}{2} + C.

   (28). 令 :math:`x = \tan t` (:math:`t \in \left( -\frac{\pi}{2}, \frac{\pi}{2} \right)`), :math:`\sqrt{x^2 + 1} = \sec t`, :math:`\mathrm{d}x = \sec^2 t ~ \mathrm{d}t`,

   .. math::
      \int \dfrac{1}{\sqrt{(x^2 + 1)^3}} ~ \mathrm{d}x
      = \int \dfrac{\sec^2 t}{\sec^3 t} ~ \mathrm{d}t
      = \int \cos t ~ \mathrm{d}t = \sin t + C = \dfrac{x}{\sqrt{1 + x^2}} + C.

   (29). 令 :math:`u = \sqrt{2x}`, 则 :math:`x = \dfrac{u^2}{2}`, :math:`\mathrm{d}x = u ~ \mathrm{d}u`,

   .. math::
      \int \dfrac{1}{1 + \sqrt{2x}} ~ \mathrm{d}x = \int \dfrac{u}{1 + u} ~ \mathrm{d}u
      = \int \left( 1 - \dfrac{1}{1 + u} \right) \mathrm{d}u
      = \sqrt{2x} - \ln \left( 1 + \sqrt{2x} \right) + C.

   (30). 令 :math:`x = \sin t` (:math:`t \in \left( -\frac{\pi}{2}, \frac{\pi}{2} \right)`), 则

   .. math::
      \int \dfrac{1}{1 + \sqrt{1 - x^2}} ~ \mathrm{d}x
      = \int \dfrac{\cos t}{1 + \cos t} ~ \mathrm{d}t
      = \int \left( 1 - \dfrac{1}{1 + \cos t} \right) \mathrm{d}t.

   利用 :math:`\dfrac{1}{1 + \cos t} = \dfrac{1 - \cos t}{\sin^2 t} = \csc^2 t - \csc t \cot t`, 得

   .. math::
      \int \dfrac{1}{1 + \cos t} ~ \mathrm{d}t = -\cot t + \csc t,

   于是

   .. math::
      \int \dfrac{1}{1 + \sqrt{1 - x^2}} ~ \mathrm{d}x = t + \cot t - \csc t + C
      = \arcsin x + \dfrac{\sqrt{1 - x^2} - 1}{x} + C.

   (31). 分子写为 :math:`x - 1 = \dfrac{1}{2}(2x + 2) - 2`, 于是

   .. math::
      \int \dfrac{x - 1}{x^2 + 2x + 3} ~ \mathrm{d}x
      = \dfrac{1}{2} \int \dfrac{\mathrm{d}(x^2 + 2x + 3)}{x^2 + 2x + 3} - 2 \int \dfrac{\mathrm{d}(x + 1)}{(x+1)^2 + 2}
      = \dfrac{1}{2} \ln \left( x^2 + 2x + 3 \right) - \sqrt{2} \arctan \dfrac{x + 1}{\sqrt{2}} + C.

   (32). 当 :math:`x > 1` 时, 令 :math:`x = \sec t` (:math:`t \in \left( 0, \frac{\pi}{2} \right)`), :math:`\sqrt{x^2 - 1} = \tan t`, :math:`\mathrm{d}x = \sec t \tan t ~ \mathrm{d}t`,

   .. math::
      \int \dfrac{1}{x \sqrt{x^2 - 1}} ~ \mathrm{d}x = \int \dfrac{\sec t \tan t}{\sec t \tan t} ~ \mathrm{d}t = t + C = \arccos \dfrac{1}{x} + C;

   当 :math:`x < -1` 时结果为 :math:`-\arccos \dfrac{1}{|x|} + C`. 统一写为 :math:`\operatorname{arcsec} \lvert x \rvert + C`.

   (33). 令 :math:`x = 3 \sec t` (:math:`t \in \left( 0, \frac{\pi}{2} \right)`), :math:`\sqrt{x^2 - 9} = 3\tan t`, :math:`\mathrm{d}x = 3\sec t \tan t ~ \mathrm{d}t`,

   .. math::
      \int \dfrac{\sqrt{x^2 - 9}}{x} ~ \mathrm{d}x = 3 \int \tan^2 t ~ \mathrm{d}t = 3 \int \left( \sec^2 t - 1 \right) \mathrm{d}t
      = 3\tan t - 3t + C = \sqrt{x^2 - 9} - 3 \arccos \dfrac{3}{x} + C.

   (34). 部分分式分解 (:math:`x^3 + 1 = x(x^2+1) + (1 - x)`),

   .. math::
      \dfrac{x^3 + 1}{(x^2 + 1)^2} = \dfrac{x}{x^2 + 1} + \dfrac{1 - x}{(x^2 + 1)^2},

   分别积分: :math:`\displaystyle \int \dfrac{x}{x^2+1} \mathrm{d}x = \dfrac{1}{2}\ln(x^2+1)`;
   :math:`\displaystyle \int \dfrac{x}{(x^2+1)^2} \mathrm{d}x = -\dfrac{1}{2(x^2+1)}`;
   :math:`\displaystyle \int \dfrac{\mathrm{d}x}{(x^2+1)^2} = \dfrac{x}{2(x^2+1)} + \dfrac{1}{2}\arctan x` (令 :math:`x = \tan t`).
   合并得

   .. math::
      \int \dfrac{x^3 + 1}{(x^2 + 1)^2} ~ \mathrm{d}x
      = \dfrac{1}{2} \ln \left( x^2 + 1 \right) + \dfrac{1}{2} \arctan x + \dfrac{x + 1}{2 (x^2 + 1)} + C.

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

   (1). 取 :math:`u = x`, :math:`\mathrm{d}v = \sin x ~ \mathrm{d}x`,

   .. math::
      \int x \sin x ~ \mathrm{d}x = -x \cos x + \int \cos x ~ \mathrm{d}x = \sin x - x \cos x + C.

   (2). 取 :math:`u = \ln x`, :math:`\mathrm{d}v = \dfrac{\mathrm{d}x}{x^2}`, :math:`v = -\dfrac{1}{x}`,

   .. math::
      \int \dfrac{\ln x}{x^2} ~ \mathrm{d}x = -\dfrac{\ln x}{x} + \int \dfrac{1}{x^2} ~ \mathrm{d}x = -\dfrac{\ln x + 1}{x} + C.

   (3). 取 :math:`u = \ln \ln x`, :math:`\mathrm{d}v = \dfrac{\mathrm{d}x}{x}`, :math:`v = \ln x`,

   .. math::
      \int \dfrac{\ln \ln x}{x} ~ \mathrm{d}x = \ln x \cdot \ln \ln x - \int \ln x \cdot \dfrac{1}{x \ln x} ~ \mathrm{d}x
      = \ln x \left( \ln \ln x - 1 \right) + C.

   (4). 两次分部积分,

   .. math::
      \int x^2 \cos x ~ \mathrm{d}x & = x^2 \sin x - 2 \int x \sin x ~ \mathrm{d}x = x^2 \sin x + 2x \cos x - 2 \int \cos x ~ \mathrm{d}x \\
      & = x^2 \sin x + 2x \cos x - 2 \sin x + C.

   (5). 取 :math:`u = y`, :math:`\mathrm{d}v = e^{-2y} ~ \mathrm{d}y`, :math:`v = -\dfrac{1}{2} e^{-2y}`,

   .. math::
      \int y e^{-2y} ~ \mathrm{d}y = -\dfrac{y}{2} e^{-2y} + \dfrac{1}{2} \int e^{-2y} ~ \mathrm{d}y
      = -\dfrac{2y + 1}{4} e^{-2y} + C.

   (6). 取 :math:`u = \arcsin x`, :math:`\mathrm{d}v = \mathrm{d}x`,

   .. math::
      \int \arcsin x ~ \mathrm{d}x = x \arcsin x - \int \dfrac{x}{\sqrt{1 - x^2}} ~ \mathrm{d}x
      = x \arcsin x + \sqrt{1 - x^2} + C.

   (7). 两次分部积分 (同 (6) 的思路),

   .. math::
      \int (\arcsin x)^2 ~ \mathrm{d}x & = x (\arcsin x)^2 - \int x \cdot \dfrac{2 \arcsin x}{\sqrt{1 - x^2}} ~ \mathrm{d}x \\
      & = x (\arcsin x)^2 + 2 \int \arcsin x ~ \mathrm{d}\left( \sqrt{1 - x^2} \right) \\
      & = x (\arcsin x)^2 + 2 \sqrt{1 - x^2} \arcsin x - 2x + C.

   (8). 先用 :math:`\tan^2 x = \sec^2 x - 1`, 再分部,

   .. math::
      \int x \tan^2 x ~ \mathrm{d}x = \int x \left( \sec^2 x - 1 \right) \mathrm{d}x
      = \int x ~ \mathrm{d}(\tan x) - \dfrac{x^2}{2}
      = x \tan x + \ln \left\lvert \cos x \right\rvert - \dfrac{x^2}{2} + C.

   (9). 与 (7) 平行 (:math:`\mathrm{d}(\arccos x) = -\dfrac{\mathrm{d}x}{\sqrt{1 - x^2}}`),

   .. math::
      \int (\arccos x)^2 ~ \mathrm{d}x & = x (\arccos x)^2 + \int x \cdot \dfrac{2 \arccos x}{\sqrt{1 - x^2}} ~ \mathrm{d}x \\
      & = x (\arccos x)^2 - 2 \int \arccos x ~ \mathrm{d}\left( \sqrt{1 - x^2} \right) \\
      & = x (\arccos x)^2 - 2 \sqrt{1 - x^2} \arccos x - 2x + C.

   (10). 取 :math:`u = \ln \cos x`, :math:`\mathrm{d}v = \sec^2 x ~ \mathrm{d}x`, :math:`v = \tan x`,

   .. math::
      \int \dfrac{\ln \cos x}{\cos^2 x} ~ \mathrm{d}x = \tan x \ln \cos x + \int \tan^2 x ~ \mathrm{d}x
      = \tan x \ln \cos x + \tan x - x + C.

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

   (1). 被积函数 :math:`\dfrac{1}{\sqrt[3]{(x + 1)^2 (x - 1)^4}}`. 令 :math:`u = \sqrt[3]{\dfrac{x + 1}{x - 1}}`,
   则 :math:`x = \dfrac{u^3 + 1}{u^3 - 1}`, :math:`\mathrm{d}x = \dfrac{-6u^2}{(u^3 - 1)^2} ~ \mathrm{d}u`, 且
   :math:`x + 1 = \dfrac{2u^3}{u^3 - 1}`, :math:`x - 1 = \dfrac{2}{u^3 - 1}`, 于是

   .. math::
      \sqrt[3]{(x + 1)^2 (x - 1)^4} = \sqrt[3]{\dfrac{4u^6 \cdot 16}{(u^3 - 1)^6}} = \dfrac{4u^2}{(u^3 - 1)^2},

   因此

   .. math::
      \int \dfrac{1}{\sqrt[3]{(x + 1)^2 (x - 1)^4}} ~ \mathrm{d}x
      = \int \dfrac{(u^3 - 1)^2}{4u^2} \cdot \dfrac{-6u^2}{(u^3 - 1)^2} ~ \mathrm{d}u
      = -\dfrac{3}{2} \int \mathrm{d}u
      = -\dfrac{3}{2} \sqrt[3]{\dfrac{x + 1}{x - 1}} + C.

   (2). 先做多项式除法 :math:`\dfrac{x^4}{x + 2} = x^3 - 2x^2 + 4x - 8 + \dfrac{16}{x + 2}`, 于是

   .. math::
      \int \dfrac{x^4}{x + 2} ~ \mathrm{d}x = \dfrac{x^4}{4} - \dfrac{2x^3}{3} + 2x^2 - 8x + 16 \ln \lvert x + 2 \rvert + C.

   (3). :math:`\dfrac{x^7}{x^4 + 2} = x^3 - \dfrac{2x^3}{x^4 + 2}`, 于是

   .. math::
      \int \dfrac{x^7}{x^4 + 2} ~ \mathrm{d}x = \int x^3 ~ \mathrm{d}x - \dfrac{1}{2} \int \dfrac{\mathrm{d}(x^4 + 2)}{x^4 + 2}
      = \dfrac{x^4}{4} - \dfrac{1}{2} \ln \left( x^4 + 2 \right) + C.

   (4). 将分子用「分母 + 分母的导数」表示: :math:`\cos x = \dfrac{1}{5}(2 \sin x + \cos x) + \dfrac{2}{5}(2 \cos x - \sin x)`,
   其中 :math:`(2 \sin x + \cos x)' = 2 \cos x - \sin x`. 于是

   .. math::
      \int \dfrac{\cos x}{2 \sin x + \cos x} ~ \mathrm{d}x
      = \dfrac{1}{5} \int \mathrm{d}x + \dfrac{2}{5} \int \dfrac{(2 \sin x + \cos x)'}{2 \sin x + \cos x} ~ \mathrm{d}x
      = \dfrac{x}{5} + \dfrac{2}{5} \ln \left\lvert 2 \sin x + \cos x \right\rvert + C.

   (5). 令 :math:`t = \tan \dfrac{x}{2}`, 则 :math:`\cos x = \dfrac{1 - t^2}{1 + t^2}`, :math:`\mathrm{d}x = \dfrac{2 ~ \mathrm{d}t}{1 + t^2}`,

   .. math::
      \int \dfrac{1}{5 - 3 \cos x} ~ \mathrm{d}x
      = \int \dfrac{2 ~ \mathrm{d}t}{5(1 + t^2) - 3(1 - t^2)}
      = \int \dfrac{2 ~ \mathrm{d}t}{2 + 8t^2}
      = \int \dfrac{\mathrm{d}t}{1 + 4t^2}
      = \dfrac{1}{2} \arctan \left( 2 \tan \dfrac{x}{2} \right) + C.

   (6). 令 :math:`u = \sin x`, :math:`\mathrm{d}u = \cos x ~ \mathrm{d}x`,

   .. math::
      \int \dfrac{\cos^5 x}{\sin^4 x} ~ \mathrm{d}x = \int \dfrac{(1 - u^2)^2}{u^4} ~ \mathrm{d}u
      = \int \left( \dfrac{1}{u^4} - \dfrac{2}{u^2} + 1 \right) \mathrm{d}u
      = -\dfrac{1}{3 u^3} + \dfrac{2}{u} + u + C

   .. math::
      \phantom{\int \dfrac{\cos^5 x}{\sin^4 x} ~ \mathrm{d}x}
      = -\dfrac{1}{3 \sin^3 x} + \dfrac{2}{\sin x} + \sin x + C.

   (7). 令 :math:`u = \sqrt[4]{x}`, 则 :math:`x = u^4`, :math:`\mathrm{d}x = 4u^3 ~ \mathrm{d}u`, :math:`\sqrt{x} = u^2`,

   .. math::
      \int \dfrac{\sqrt[3]{1 + \sqrt[4]{x}}}{\sqrt{x}} ~ \mathrm{d}x = 4 \int u (1 + u)^{\frac{1}{3}} ~ \mathrm{d}u.

   再令 :math:`v = 1 + u`: :math:`4 \int (v - 1) v^{\frac{1}{3}} ~ \mathrm{d}v = 4 \int \left( v^{\frac{4}{3}} - v^{\frac{1}{3}} \right) \mathrm{d}v
   = \dfrac{12}{7} v^{\frac{7}{3}} - 3 v^{\frac{4}{3}} + C`, 即

   .. math::
      \int \dfrac{\sqrt[3]{1 + \sqrt[4]{x}}}{\sqrt{x}} ~ \mathrm{d}x
      = \dfrac{12}{7} \left( 1 + \sqrt[4]{x} \right)^{\frac{7}{3}} - 3 \left( 1 + \sqrt[4]{x} \right)^{\frac{4}{3}} + C.

   (8). 令 :math:`x = \tan t` (:math:`t \in \left( -\frac{\pi}{2}, \frac{\pi}{2} \right)`), 则 :math:`\sqrt{x^2 + 1} = \sec t`, :math:`\mathrm{d}x = \sec^2 t ~ \mathrm{d}t`,

   .. math::
      \int \dfrac{1}{(2x^2 + 1) \sqrt{x^2 + 1}} ~ \mathrm{d}x
      = \int \dfrac{\sec^2 t}{(2 \tan^2 t + 1) \sec t} ~ \mathrm{d}t
      = \int \dfrac{\cos t}{2 \sin^2 t + \cos^2 t} ~ \mathrm{d}t
      = \int \dfrac{\mathrm{d}(\sin t)}{1 + \sin^2 t}
      = \arctan (\sin t) + C,

   即

   .. math::
      \int \dfrac{1}{(2x^2 + 1) \sqrt{x^2 + 1}} ~ \mathrm{d}x = \arctan \dfrac{x}{\sqrt{1 + x^2}} + C.

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

   令 :math:`u = f(\ln x)`, 则 :math:`\mathrm{d}u = f'(\ln x) \cdot \dfrac{1}{x} ~ \mathrm{d}x`, 恰为分子, 于是

   .. math::
      \int \dfrac{f'(\ln x)}{x \sqrt{f(\ln x)}} ~ \mathrm{d}x = \int \dfrac{\mathrm{d}u}{\sqrt{u}} = 2\sqrt{u} + C = 2 \sqrt{f(\ln x)} + C.

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
