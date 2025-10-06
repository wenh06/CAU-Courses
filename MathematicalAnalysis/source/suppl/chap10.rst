第十章补充材料
^^^^^^^^^^^^^^^^^^^^^^^^^

.. _generalized-vanderwaerden-tagaki-function:

1. Generalized Van der Waerden-Takagi 函数定义如下

.. math::
   & \varphi(x) = d(x, \mathbb{Z}) = \min_{n \in \mathbb{Z}} |x - n|, \quad x \in \mathbb{R}, \\
   & f(x) = \sum_{n=0}^{\infty} a^n \varphi(b^n x).

当 :math:`0 < a < 1`, :math:`b \in \mathbb{N}_{\geqslant 2}`, 且 :math:`ab \geqslant 1` 时,
:math:`f(x)` 是一个在 :math:`\mathbb{R}` 上处处不可导的连续函数.

首先来说明 :math:`f(x)` 在 :math:`\mathbb{R}` 上连续: 由于 :math:`0 \leqslant \varphi(x) \leqslant 1/2`,
所以 :math:`0 \leqslant a^n \varphi(b^n x) \leqslant a^n/2`. 由于正项级数 :math:`\displaystyle \sum_{n=0}^{\infty} a^n` 收敛,
于是由 Weierstraß 判别法, 函数项级数 :math:`\displaystyle \sum_{n=0}^{\infty} a^n \varphi(b^n x)` 一致收敛.
进一步由一致收敛函数项级数和函数的连续性定理知, 和函数 :math:`f(x)` 在 :math:`\mathbb{R}` 上连续.

接下来说明 :math:`f(x)` 在 :math:`\mathbb{R}` 上处处不可导: 由于 :math:`\varphi` 是周期为 1 的函数,
所以 :math:`f` 也以 1 为周期, 所以只要对任意 :math:`x \in [0, 1)` 证明 :math:`f` 在 :math:`x` 处不可导即可.
希望可以选取序列 :math:`u_n \rightarrow x \leftarrow v_n`, 使得

.. math::
   \dfrac{f(u_n) - f(v_n)}{u_n - v_n}
   = \dfrac{\sum\limits_{m=0}^{\infty} a^m (\varphi(b^m u_n) - \varphi(b^m v_n))}{u_n - v_n}

发散. 由于 :math:`2 b^n x` 是非负实数, 所以存在非负整数 :math:`k_n`, 使得 :math:`k_n \leqslant 2 b^n x < k_n + 1`, 即

.. math::
   \dfrac{k_n}{2 b^n} \leqslant x < \dfrac{k_n + 1}{2 b^n}.

取 :math:`u_n = \dfrac{k_n}{2 b^n}, v_n = \dfrac{k_n + 1}{2 b^n}`.
对于和式 :math:`\displaystyle \sum\limits_{m=0}^{\infty} a^m (\varphi(b^m u_n) - \varphi(b^m v_n))`, 分为两部分讨论:

:math:`1^{\circ}` 当 :math:`0 \leqslant m < n` 时, 由于

.. math::
   b^m u_n = \dfrac{k_n}{2} \cdot \dfrac{1}{b^{n-m}}, ~~ b^m v_n = \dfrac{k_n + 1}{2} \cdot \dfrac{1}{b^{n-m}},

从而存在非负整数 :math:`z`, 使得 :math:`b^m u_n, b^m v_n` 同时属于 :math:`[z, z+1/2]` 或 :math:`[z+1/2, z+1]`, 那么

.. math::
   \varphi(b^m u_n) - \varphi(b^m v_n) = \pm (b^m u_n - b^m v_n) = \pm \dfrac{1}{2 b^{n-m}},

从而有

.. math::
   \dfrac{a^m (\varphi(b^m u_n) - \varphi(b^m v_n))}{u_n - v_n}
   = \pm a^m \dfrac{1}{2 b^{n-m}} \left/ \left( \dfrac{1}{2 b^n}\right) \right.
   = \pm (ab)^m.

:math:`2^{\circ}` 当 :math:`m \geqslant n` 时, 有

.. math::
   b^m u_n = \dfrac{b^{m-n} \cdot k_n}{2}, ~~ b^m v_n = \dfrac{b^{m-n} \cdot (k_n+1)}{2}.

:math:`2.1^{\circ}` 当 :math:`b` 为偶数时, 若 :math:`m > n`, 则 :math:`b^m u_n, b^m v_n` 都是整数;
若 :math:`m = n`, 则 :math:`b^m u_n = \dfrac{k_n}{2}, b^m v_n = \dfrac{k_n + 1}{2}` 其中一个为整数,
另一个为半整数 (即 :math:`\dfrac{1}{2} +` 整数). 于是

.. math::
   \dfrac{a^m (\varphi(b^m u_n) - \varphi(b^m v_n))}{u_n - v_n}
   = \begin{cases}
      0, & \text{当 } m > n \text{ 时}, \\
      \dfrac{\pm a^m / 2}{1 / (2 b^{m})} = \pm (ab)^m, & \text{当 } m = n \text{ 时}.
   \end{cases}

:math:`2.2^{\circ}` 当 :math:`b` 为奇数时, :math:`b^{m-n}` 恒为奇数,
所以 :math:`b^m u_n, b^m v_n` 其中一个为整数, 另一个为半整数, 所以

.. math::
   \dfrac{a^m (\varphi(b^m u_n) - \varphi(b^m v_n))}{u_n - v_n}
   = \dfrac{\pm a^m / 2}{1 / (2 b^{n})} = \pm a^m b^n,

上述符号 :math:`\pm` 固定, 只与 :math:`k_n` 的奇偶性有关, 与 :math:`m` 无关. 于是

.. math::
   \dfrac{f(u_n) - f(v_n)}{u_n - v_n}
   & = \dfrac{\sum\limits_{m=0}^{\infty} a^m (\varphi(b^m u_n) - \varphi(b^m v_n))}{u_n - v_n} \\
   & = \begin{cases}
      \sum\limits_{m=1}^n \left( \pm (ab)^m \right), & \text{若 $b$ 为偶数}, \\
      \sum\limits_{m=1}^{n-1} \left( \pm (ab)^m \right) + \sum\limits_{m=n}^{\infty} (\pm a^m b^n), & \text{若 $b$ 为奇数}
   \end{cases} \\
   & = \begin{cases}
      \sum\limits_{m=1}^n \left( \pm (ab)^m \right), & \text{若 $b$ 为偶数}, \\
      \sum\limits_{m=1}^{n-1} \left( \pm (ab)^m \right) \pm \dfrac{(ab)^n}{1 - a}, & \text{若 $b$ 为奇数}
   \end{cases}

容易看出, 当 :math:`b` 为正偶数, 或者 :math:`ab = 1` 时, 上式当 :math:`n \to \infty` 时发散.
:math:`b` 为奇数且 :math:`ab > 1` 的情况需进一步讨论.

.. _summable-series:

2. 三种意义下可和 (summable) 的 (数项) 级数 :math:`\displaystyle \sum_{n=1}^{\infty} a_n`:

首先是 Abel 意义下的可和, 也就是极限 :math:`\displaystyle \lim_{x \to 1^-} \sum_{n=1}^{\infty} a_n x^n` 存在.

其次是 Cesàro :math:`(c, 1)` 意义下的可和, 也就是极限
:math:`\displaystyle \lim_{n \to \infty} \sigma_n^{(1)} = \lim_{n \to \infty} \dfrac{1}{n} \sum_{k=1}^{n} \sum_{j=1}^{k} a_j` 存在,
进而可以归纳定义 Cesàro :math:`(c, r), ~ r \geqslant 1,` 意义下的可和性, 即极限
:math:`\displaystyle \lim_{n \to \infty} \sigma_n^{(r)} = \lim_{n \to \infty} \dfrac{1}{n} \sum_{k=1}^{n} \sigma_k^{(r-1)}` 存在.

最后是通常意义下的可和, 也就是部分和极限 :math:`\displaystyle \lim_{n \to \infty} s_n = \lim_{n \to \infty} \sum_{k=1}^{n} a_k` 存在.

这三种意义下可和的级数之间有如下关系:

.. tikz:: 三种意义下可和的级数关系图
   :align: center
   :xscale: 100
   :libs: arrows.meta, positioning, decorations.pathmorphing
   :packages: amsfonts, amsmath, amssymb, [slantfont,boldfont]xeCJK

   \tikzset{
      baseline=(current bounding box.center),
      every node/.style={font=\Large},
      arrow/.style={-{Stealth[scale=1.2]}, thick, bend left=20}
   }

   \node (A) at (0,0) {$\{\text{Abel 可和}\}$};
   \node (A1) [right=.5cm of A] {$\supsetneqq$};
   \node (B) [right=.5cm of A1] {$\{(c, r) ~ \text{可和}\}$};
   \node (B1) [right=.5cm of B] {$\supsetneqq$};
   \node (C) [right=.5cm of B1] {$\{(c, 1) ~ \text{可和}\}$};
   \node (C1) [right=.5cm of C] {$\supsetneqq$};
   \node (D) [right=.5cm of C1] {$\{\text{通常可和}\}$};

   \draw[arrow, dashed] (A) to[bend left=40]
    node[midway, above] {$a_n = o\left(\frac{1}{n}\right)$} node[midway, below] {\smaller T1} (D);
   \draw[arrow, dashed] (C) to[bend left=30]
      node[near start, above] {$a_n = o\left(\frac{1}{n}\right)$} node[midway, below] {\smaller T2} (D);
   \draw[arrow, dashed] (C) to[bend right=40]
      node[midway, below] {$a_n = O\left(\frac{1}{n}\right)$} node[midway, above] {\smaller T3} (D);

上图虚线表示的是添加了相应“正则性”条件的 Tauber 型定理. 后两个包含关系可以用 Stolz 公式证明. 第一个包含关系的证明如下:

假设 :math:`\displaystyle \sigma_n = \dfrac{1}{n} \sum_{k=1}^{n} s_k` 极限为 :math:`A`, 那么

.. math::
   \varlimsup_{n\to\infty} \sqrt[\leftroot{-3}\uproot{3}n]{|n \sigma_n|}
   = \sqrt[\leftroot{-1}\uproot{18}n]{\sum_{k=1}^{n} s_k} = 1,

即幂级数 :math:`\displaystyle \sum_{n=1}^{\infty} n \sigma_n x^n` 收敛半径为 1.
对于任意的 :math:`|x| < 1`, 上述幂级数绝对收敛, 因此有

.. math::
   \sum_{n=1}^{\infty} n \sigma_n x^n
   & = \sum_{n=1}^{\infty} \left( \sum_{k=1}^{n} s_k \right) x^n
      = \sum_{n=1}^{\infty} \left( S_1 + S_2 + \cdots + s_n \right) x^n \\
   & = S_1 x (1 + x + x^2 + \cdots) + S_2 x^2 (1 + x + x^2 + \cdots) + \cdots \\
   & = \sum_{n=1}^{\infty} s_n x^n \dfrac{1}{1-x}

上式也表明了 :math:`\displaystyle \sum_{n=1}^{\infty} s_n x^n` 收敛半径 :math:`\geqslant 1`,
故在 :math:`|x| < 1` 范围内绝对收敛. 于是类似地有

.. math::
   \sum_{n=1}^{\infty} s_n x^n
   & = \sum_{n=1}^{\infty} \left( a_1 + a_2 + \cdots + a_n \right) x^n
      = \sum_{n=1}^{\infty} a_n x^n (1 + x + x^2 + \cdots) \\
   & = \sum_{n=1}^{\infty} a_n x^n \dfrac{1}{1-x}.

那么 :math:`\displaystyle \sum_{n=1}^{\infty} n \sigma_n x^n = \dfrac{1}{(1-x)^2} \sum_{n=1}^{\infty} a_n x^n`
对 :math:`|x| < 1` 恒成立.

接下来, 我们要证明

.. math::
   \lim_{x\to 1-} (1-x)^2 \sum_{n=1}^{\infty} n \sigma_n x^n = \lim_{x\to 1-} \sum_{n=1}^{\infty} a_n x^n = A.

对定义在 :math:`|x| < 1` 上的幂级数展开 :math:`\displaystyle (1-x)^{-1} = \sum_{n=0}^\infty x^n` 用应用逐项求导定理,
有 :math:`\displaystyle (1-x)^{-2} = \sum_{n=0}^\infty (n+1) x^n`, 那么

.. math::
   (1-x)^2 \sum_{n=1}^{\infty} n \sigma_n x^n - A
   & = (1-x)^2 \sum_{n=1}^{\infty} n \sigma_n x^n - (1-x)^2 \sum_{n=0}^\infty (n+1) x^n A \\
   & = (1-x)^2 \sum_{n=1}^{\infty} (n \sigma_n - (n+1)A) x^n - (1-x)^2 A \\
   & = (1-x)^2 \sum_{n=1}^{\infty} n (\sigma_n - A) x^n - (1-x)^2 \sum_{n=1}^{\infty} A x^n - (1-x)^2 A.

上式后两项关于 :math:`x \to 1-` 的极限很容易看出都是 0.
我们最终约化到了证明第一项 :math:`\displaystyle (1-x)^2 \sum_{n=1}^{\infty} n (\sigma_n - A) x^n`
关于 :math:`x \to 1-` 的极限也是 0.

由于 :math:`\sigma_n \to A`, 所以 :math:`\varepsilon > 0, ~ \exists N`, 使得 :math:`\forall n > N`,
有 :math:`|\sigma_n - A| < \varepsilon / 2`.
记 :math:`\displaystyle M = \max_{1 \leqslant n \leqslant N} n |\sigma_n - A|`, 那么有

.. math::
   \left\lvert (1-x)^2 \sum_{n=1}^{\infty} n (\sigma_n - A) x^n \right\rvert
   & \leqslant \sum_{n=1}^{\infty} n |\sigma_n - A| (1-x)^2x^n \\
   & = \sum_{n=1}^{N} n |\sigma_n - A| (1-x)^2x^n + \sum_{n=N+1}^{\infty} n |\sigma_n - A|(1-x)^2x^n \\
   & \leqslant M \sum_{n=1}^{N} (1-x)^2x^n + \dfrac{\varepsilon}{2} \sum_{n=N+1}^{\infty} n (1-x)^2x^n \\
   & \leqslant M x(1-x)(1-x^N) + \dfrac{\varepsilon}{2} \sum_{n=0}^{\infty} (n + 1) (1-x)^2x^n \\
   & \leqslant M(1 - x) + \dfrac{\varepsilon}{2}.

对取定的 :math:`\varepsilon`, 任取 :math:`1 - \dfrac{\varepsilon}{2M} < x < 1`, 即有

.. math::
   \left\lvert (1-x)^2 \sum_{n=1}^{\infty} n (\sigma_n - A) x^n \right\rvert
   \leqslant M(1 - x) + \dfrac{\varepsilon}{2} < \varepsilon,

这样, 我们就证明了

.. math::
   \lim_{x\to 1-} \sum_{n=1}^{\infty} a_n x^n = \lim_{x\to 1-} (1-x)^2 \sum_{n=1}^{\infty} n \sigma_n x^n = A.

第一个严格包含关系的例子: :math:`a_n = (-1)^{n+1} (n+1)`. 由逐项求导定理, 容易看出

.. math::
   \sum_{n=1}^{\infty} (-1)^{n+1} (n+1) x^n = \left( \sum_{n=1}^{\infty} (-x)^{n+1} \right)'
   = \left( \dfrac{x^2}{1 + x} \right)' = \dfrac{2x + x^2}{(1+x)^2} \to \dfrac{3}{4} ~~ (x \to 1-).

但 :math:`s_n = \begin{cases} k + 1, & n = 2k - 1, \\ -k, & n = 2k, \end{cases}`
故 :math:`\displaystyle \lim_{n \to \infty} \dfrac{s_n}{n}` 极限不存在,
不满足级数 Cesàro $(c, 1)$ 可和的必要条件 :math:`\displaystyle \lim_{n \to \infty} \dfrac{s_n}{n} = 0`.

第三个严格包含关系的例子: :math:`a_n = (-1)^{n+1}`.
容易算得 :math:`s_n = \begin{cases} 1, & n = 2k - 1, \\ 0, & n = 2k, \end{cases}`
于是 :math:`\sigma_{n} \to \dfrac{1}{2} ~~ (n \to \infty)`.
即通常意义下发散的级数 :math:`\displaystyle \sum_{n=1}^{\infty} (-1)^{n+1}` 是 Cesàro $(c, 1)$ 可和的.

Tauber 型定理 T2 的证明本质上还是利用 Stolz 公式; Tauber 型定理 T3 的证明稍微复杂一些,
具体见 :ref:`第九章补充材料 <cesaro-tauber>`.

.. _power-series-tanx:

3. :math:`f(x) = \tan x` 在 :math:`x = 0` 附近的幂级数展开及其收敛半径:

方法一: 直接利用泰勒公式展开:

.. math::
   \tan x = \sum_{n=0}^{\infty} c_n x^n = \sum_{n=0}^{\infty} \dfrac{f^{(n)}(0)}{n!} x^n,

接下来计算 :math:`f(x) = \tan x` 的各阶导函数及其在 :math:`x = 0` 处的值即可.
这种方法较难求出 :math:`c_n` 的通项, 以及相应的收敛半径.

方法二: 利用待定系数法, 令 :math:`\displaystyle f(x) = \tan x = \sum_{n=0}^\infty c_n x^n`, 那么
由 :math:`\sin x = \tan x \cos x` 有

.. math::
   \sum_{n=0}^\infty \dfrac{(-1)^n}{(2n+1)!} x^{2n+1}
   = \left( \sum_{n=0}^\infty c_n x^n \right) \cdot \left( \dfrac{(-1)^n}{(2n)!} x^{2n} \right)

通过比较上式两边系数可以对 :math:`c_n` 进行递归求解. 这种方法还是难以求出 :math:`c_n` 的通项, 以及相应的收敛半径.

方法三: 利用三角函数作为复函数的表达:

.. math::
   \sin x = \dfrac{e^{ix} - e^{-ix}}{2i}, \quad \cos x = \dfrac{e^{ix} + e^{-ix}}{2},

那么有

.. math::
   x \cot x = x \dfrac{\cos x}{\sin x} = ix \dfrac{e^{2ix} + 1}{e^{2ix} - 1}
   = ix \left( \dfrac{2}{e^{2ix} - 1} + 1 \right)
   = ix + \dfrac{2}{e^{2ix} - 1}.

由 :math:`\displaystyle \dfrac{z}{e^z - 1} = \sum_{n=0}^\infty \dfrac{B_n z^n}{n!}`,
其中 :math:`B_n` 为 Bernoulli 数, 代入 :math:`z = 2ix` 即有

.. math::
   x \cot x = \sum_{n=1}^\infty \dfrac{(-4)^n B_{2n}}{(2n)!} x^{2n},

或等价地有

.. math::
   \cot x = \dfrac{1}{x} + \sum_{n=1}^\infty \dfrac{(-4)^n B_{2n}}{(2n)!} x^{2n-1}.

接下来, 利用 :math:`\tan x = \cot x - 2 \cot 2x,` 将上式代入, 有

.. math::
   \tan x
   & = \dfrac{1}{x} + \sum_{n=1}^\infty \dfrac{(-4)^n B_{2n}}{(2n)!} x^{2n-1}
       - 2\dfrac{1}{2x} + 2\sum_{n=1}^\infty \dfrac{(-4)^n B_{2n}}{(2n)!} (2x)^{2n-1} \\
   & = \sum_{n=1}^\infty \dfrac{(-4)^n (1 - 4^n) B_{2n}}{(2n)!} x^{2n-1}.

利用这种方法, 我们可以求得 :math:`\tan x` 幂级数展开的通项表达, 但收敛半径还是不方便计算.

方法四: 利用 :math:`\displaystyle \dfrac{\sin \pi x}{\pi x}` 的在 :math:`|x| < 1` 范围内的无穷乘积展开

.. math::
   \dfrac{\sin \pi x}{\pi x} = \prod_{n=1}^\infty \left( 1 - \dfrac{x^2}{n^2} \right),

两边取对数导数 :math:`\displaystyle \dfrac{1}{\pi} \cdot \dfrac{\mathrm{d}}{\mathrm{d} x} \left( \ln (\cdot) \right)` 有

.. math::
   \dfrac{\cos \pi x}{\sin \pi x} - \dfrac{1}{\pi x}
   = -\dfrac{1}{\pi} \sum_{n=1}^\infty \dfrac{2x}{n^2} \cdot \left( 1 - \dfrac{x^2}{n^2} \right)^{-1},

从而有

.. math::
   \pi x \cot \pi x
   & = 1 - 2 \sum_{n=1}^\infty \dfrac{x^2}{n^2} \cdot \left( 1 - \dfrac{x^2}{n^2} \right)^{-1} \\
   & = 1 - 2 \sum_{n=1}^\infty \dfrac{x^2}{n^2} \cdot \left( \sum_{k=0}^\infty \left( \dfrac{x^2}{n^2} \right)^k \right) \\
   & = 1 - 2 \sum_{n=1}^\infty \sum_{k=1}^\infty \left( \dfrac{x^2}{n^2} \right)^k \\
   & = 1 - 2 \sum_{k=1}^\infty \left( \sum_{n=1}^\infty \dfrac{1}{n^{2k}} \right) x^{2k} \\
   & = 1 - 2 \sum_{k=1}^\infty \zeta(2k) x^{2k}.

其中 :math:`\displaystyle \zeta(s) := \sum_{n=1}^\infty \dfrac{1}{n^{s}}` 为 Riemann zeta 函数. 由此可求得

.. math::
   \cot x = \dfrac{1}{x} - 2 \sum_{k=1}^\infty \dfrac{\zeta(2k)}{\pi^{2k}} x^{2k-1},

代入 :math:`\tan x = \cot x - 2 \cot 2x` 可得

.. math::
   \tan x = 2 \sum_{k=1}^\infty \dfrac{(4^k - 1)\zeta(2k)}{\pi^{2k}} x^{2k-1}.

进一步利用 :math:`\displaystyle \lim_{n\to\infty} \zeta(n) = 1`, 可得

.. math::
   \dfrac{1}{R^2} = \lim_{k\to\infty} \dfrac{(4^{k+1} - 1)\zeta(2k+2)}{\pi^{2k+2}}
      \cdot \dfrac{\pi^{2k}}{(4^k - 1)\zeta(2k)}
   = \dfrac{4}{\pi^2},

从而知 :math:`\tan x` 的收敛半径 :math:`\displaystyle R = \dfrac{\pi}{2}`.
