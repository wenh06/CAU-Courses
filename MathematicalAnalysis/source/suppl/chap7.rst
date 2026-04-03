第七章补充材料
^^^^^^^^^^^^^^^^^^^^^^^^^

1. 黎曼可积函数列极限 (逐点极限) 是黎曼不可积函数的例子

记 :math:`\mathbb{Q} \cap [0, 1] = \{r_1, r_2, \dots, \}`, 考虑如下定义在闭区间 :math:`[0, 1]` 上的函数列

.. math::
   f_n(x) = \begin{cases}
      1, & \text{ 若 } x \in \{r_1, \dots, r_n\}; \\
      0, & \text{ 其余情况 }.
   \end{cases}

那么, 每个函数 :math:`f_n` 在闭区间 :math:`[0, 1]` 只有有限个不连续点, 从而是黎曼可积的.
容易证明, 对于任意有理数 :math:`x \in \mathbb{Q} \cap [0, 1]`, 有 :math:`\displaystyle \lim_{n \to \infty} f_n(x) = 1`;
另一方面, 对于任意无理数 :math:`x \in [0, 1] \setminus \mathbb{Q}`, 有 :math:`\displaystyle \lim_{n \to \infty} f_n(x) = 0`,
即

.. math::
   \lim_{n \to \infty} f_n(x) = \begin{cases}
      1, & \text{ 若 } x \in \mathbb{Q} \cap [0, 1]; \\
      0, & \text{ 若 } x \in [0, 1] \setminus \mathbb{Q}.
   \end{cases}

也就是说, 函数列 :math:`\{f_n\}` 在闭区间 :math:`[0, 1]` 上的逐点极限函数是狄利克雷函数, 是一个黎曼不可积函数.

2. 闭区间上处处可导, 且导函数有界, 但导函数黎曼不可积的函数:

首先, 构造闭区间 :math:`[0, 1]` 内的特殊子集, 类 Cantor 集: 取定一个常数 :math:`c`, 满足 :math:`0 < c \leqslant 1/3`.
在构造的第 :math:`1` 步, 从闭区间 :math:`[0, 1]` 的正中间挖掉长为 :math:`c` 的开区间; 此后的第 :math:`n` 步,
对于上一步剩下的 :math:`2^{n-1}` 个闭区间, 在每个闭区间正中间挖掉长为 :math:`c^n` 的开区间. 最终剩下的集合被称作一个类 Cantor 集.
这个集合中的元素正好是每一步所得的闭区间的端点 (或者说每一步挖去的开区间的端点, 再并上 :math:`0, 1` 这两点).

以上构造过程的第 :math:`n` 步挖去的 :math:`2^{n-1}` 个开区间并起来 (是不交并) 的长度和为

.. math::
   2^{n-1} \cdot c^n = (2c)^n / 2,

所得类 Cantor 集的 "长度" (实际是所谓的测度) 等于

.. math::
   1 - \sum_{n=1}^{\infty} (2c)^n / 2 = 1 - \dfrac{2c}{1 - 2c} \cdot \dfrac{1}{2} = \dfrac{1 - 3c}{1 - 2c}.

当 :math:`c` 满足 :math:`0 < c < 1/3` 时, 这个集合的测度是正的, 也就是说它不是零测集. 以下都假设 :math:`0 < c < 1/3`.

接下来, 构造满足导函数有界, 但导函数黎曼不可积的, 定义在 :math:`[0, 1]` 上的所谓的 Volterra 函数:
考虑定义在 :math:`\mathbb{R}` 上的函数

.. math::
   \varphi(x) = \begin{cases} x^{2}\sin(1/x), & x \neq 0; \\ 0, & x = 0. \end{cases}

这个函数的导函数为

.. math::
   \varphi'(x) = \begin{cases} 2x\sin(1/x) - \cos(1/x), & x \neq 0; \\ 0, & x = 0. \end{cases}

它在 :math:`x = 0` 处不连续. 令

.. math::
   x_1 = \max \{ x \in [0, c/2] ~ : ~ \varphi'(x) = 0 \}.

定义支集包含于 :math:`[0, c]` 的函数

.. math::
   g_1(x) = \begin{cases}
      \varphi(x), & 0 \leqslant x < x_1; \\
      \varphi(x_1), & x_1 \leqslant x \leqslant c - x_1; \\
      \varphi(c - x), & c - x_1 < x \leqslant c; \\
      0, & x \not\in [0, c].
   \end{cases}

也就是说, :math:`g_1(x)` 是由 :math:`\varphi(x)|_{[0, x_1]}` 以常值 :math:`\varphi(x_1)` 延拓到 :math:`[x_1, c/2]` 上,
并以常值 :math:`0` 延拓到 :math:`(-\infty, 0]` 上, 接着以 :math:`x = c/2` 做镜面反射得到的支集包含于 :math:`[0, c]` 的函数.
将 :math:`g_1(x)` 往右平移 :math:`1 - 2c`, 函数 :math:`f_{1,1}(x)`. 注意, 函数 :math:`f_{1,1}(x)` 的支集,
正好包含于构造类 Cantor 集的第一步挖去的开区间 (再加上其端点). 注意, 函数 :math:`f_{1,1}(x)` 在这两个端点处取值是 :math:`0`,
其导函数 :math:`f_{1,1}'(x)` 有界, 且在这两个端点处不连续.

仿照此方法, 可以构造只在 :math:`[0, c^n]` 上取非零值的函数 :math:`g_n(x)`, 将其做 :math:`2^{n-1}` 次平移,
得到 :math:`2^{n-1}` 个函数 :math:`f_{n,k}(x)`, :math:`k = 1, 2, \dots, 2^{n-1}`,
使得其支集, 正好包含于构造类 Cantor 集的第 :math:`n` 步挖去的那 :math:`2^{n-1}` 个开区间 (再加上其端点). 最后, 定义 Volterra 函数为

.. math::
   f(x) = \sum_{n=1}^{\infty} \sum_{k=1}^{2^{n-1}} f_{n,k}(x).

注意, :math:`f(x)` 在 :math:`[0, 1]` 之外取值为零, 并且对任意 :math:`x \in [0, 1]`, 上述和式中实际上至多只有一项是非零的, 因此是良定义的.
:math:`f(x)` 在 :math:`[0, 1]` 上处处可导, 并且其导函数 :math:`f'(x)` 正好在类 Cantor 集上 (也就是挖去开区间的端点) 不连续,
因此由函数黎曼可积的勒贝格判别法, 知 :math:`f'(x)` 在 :math:`[0, 1]` 上黎曼不可积.

3. :math:`[a, b]` 区间上的连续函数 :math:`f(x)` 的 :math:`p` 范数的极限等于其无穷范数:

设 :math:`f(x)` 是定义在 :math:`[a, b]` 上的连续函数, 那么 :math:`|f(x)|` 可以取到最大值 :math:`M`, 即 :math:`f(x)` 的无穷范数.

首先, 由积分的保序性, 有

.. math::
   \left( \int_{a}^{b} |f(x)|^p ~ \mathrm{d}x \right)^{1/p}
   \leqslant \left( \int_{a}^{b} M^p ~ \mathrm{d}x \right)^{1/p} = M (b - a)^{1/p}.

另一方面, 设 :math:`f(x_0) = M`, 那么对于任意 :math:`\varepsilon > 0`, 由连续性存在 :math:`\delta > 0`,
使得当 :math:`|x - x_0| < \delta` 时, 有 :math:`|f(x) - M| < \varepsilon`. 于是

.. math::
   \left( \int_{a}^{b} |f(x)|^p ~ \mathrm{d}x \right)^{1/p}
   \geqslant \left( \int_{x_0 - \delta}^{x_0 + \delta} (M - \varepsilon)^p ~ \mathrm{d}x \right)^{1/p}
   = (M - \varepsilon) (2\delta)^{1/p}.

综上有

.. math::
   (M - \varepsilon) (2\delta)^{1/p} \leqslant \left( \int_{a}^{b} |f(x)|^p ~ \mathrm{d}x \right)^{1/p} \leqslant M (b - a)^{1/p},

对 :math:`p` 取极限 :math:`p \to \infty`, 即有

.. math::
   M - \varepsilon \leqslant \lim_{p \to \infty} \lVert f \rVert_p \leqslant M,

再对 :math:`\varepsilon` 取极限 :math:`\varepsilon \to 0+`, 即有

.. math::
   M \leqslant \lim_{p \to \infty} \lVert f \rVert_p \leqslant M,

即 :math:`\displaystyle \lim_{p \to \infty} \lVert f \rVert_p = M`.

4. 定积分连续性 :math:`\displaystyle \lim_{h \to 0} \int_a^b |f(x+h) - f(x)| ~ \mathrm{d} x = 0` 的证明:

不妨设 :math:`|h| < 1`, 以及 :math:`f(x)` 在 :math:`[a-1, b+1]` 上黎曼可积. 那么由振幅判别法, 对任意 :math:`\varepsilon > 0`,
总存在 :math:`\delta > 0`, 使得对 :math:`[a-1, b+1]` 区间上任意满足 :math:`\lambda(P) < \delta` 的划分 :math:`P`, 总有

.. math::
   \sum_{i=1}^n \omega(f; [x_{i-1}, x_i]) \cdot (x_i - x_{i-1}) < \varepsilon,
   \quad \omega(f; [x_{i-1}, x_i]) := \sup_{t_1, t_2 \in [x_{i-1}, x_i]} |f(t_2) - f(t_1)|.

任取 :math:`h` 满足 :math:`|h| < \delta / 2`, 并取 :math:`[a, b]` 的划分

.. math::
   a < a + |h| < a + 2|h| < \cdots < a + k |h| < b, \quad k = \left\lceil \frac{b-a}{|h|} \right\rceil - 1.

为了记号方便, 以下不妨设 :math:`h > 0`. 那么在区间 :math:`[a + (i-1)h, a + ih]` 上恒有

.. math::
   |f(x+h) - f(x)| \leqslant \omega(f; [a + (i-1)h, a + (i+1)h]),

从而有

.. math::
   \int_a^b |f(x+h) - f(x)| ~ \mathrm{d} x
   & = \sum_{i=1}^k \int_{a + (i-1)h}^{a + ih} |f(x+h) - f(x)| ~ \mathrm{d} x
      + \int_{a + kh}^{b} |f(x+h) - f(x)| ~ \mathrm{d} x \\
   & \leqslant \sum_{i=1}^{k+1} \int_{a + (i-1)h}^{a + ih} |f(x+h) - f(x)| ~ \mathrm{d} x \\
   & \leqslant \sum_{i=1}^{k+1} \int_{a + (i-1)h}^{a + ih} \omega(f; [a + (i-1)h, a + (i+1)h]) ~ \mathrm{d} x \\
   & = \sum_{i=1}^{k+1} \omega(f; [a + (i-1)h, a + (i+1)h]) \cdot h \\
   & = \dfrac{1}{2} \sum_{i=1}^{k+1} \omega(f; [a + (i-1)h, a + (i+1)h]) \cdot ((a + (i+1)h) - a + (i-1)h) \\
   & < \dfrac{1}{2} \cdot 2\varepsilon = \varepsilon.

最后一行的不等式是因为, 分点 :math:`a, a + 2h, a + 4h, \dots` 以及 :math:`a + h, a + 3h, \dots` 都分别可以扩充成
:math:`[a-1, b+1]` 区间上的划分 :math:`P_1, P_2`, 满足 :math:`\lambda(P_1), \lambda(P_2) < \delta`,
从而上述和式是相应振幅和的部分和.
所以 :math:`\displaystyle \lim_{h \to 0} \int_a^b |f(x+h) - f(x)| ~ \mathrm{d} x = 0`

.. note::
   这题可以从更高的层次来看: 以后会学到闭区间上黎曼可积的函数都是勒贝格可积的, 那么就可以利用勒贝格积分理论中的有界收敛定理,
   即若函数族 :math:`g_h(x)` (勒贝格, 下同) 可积, :math:`h` 是某个指标集 (例如 :math:`\mathbb{N}` 或 :math:`(-1, 1)` 区间等),
   并且存在正的常数 :math:`M`, 使得 :math:`|g_h(x)| \leqslant M` 恒成立, 那么积分和取极限能交换次序, 即

   .. math::
      \lim_{h \to h_0} \int_a^b g_h(x) ~ \mathrm{d} x = \int_a^b \lim_{h \to h_0} g_h(x) ~ \mathrm{d} x,

   这里的 :math:`h_0` 是指标集的聚点 (例如若指标集是 :math:`\mathbb{N}`, :math:`h_0` 是 :math:`+\infty`;
   指标集是 :math:`(-1, 1)` 区间 :math:`h_0` 是 :math:`0` 等情况).

   在这题里, 就可以取 :math:`g_h(x) = |f(x+h) - f(x)|`, 相应的极限函数 :math:`\displaystyle \lim_{h \to h_0} g_h(x)` 几乎处处等于 :math:`0`,
   其勒贝格积分就等于 :math:`0`. 当然, 几乎处处等于 :math:`0` 的函数未必黎曼可积, 这是要注意的.

5. :math:`n` 步 Newton-Cotes 求积公式中的 Cotes 系数:

Cotes 系数依定义为

.. math::
   c_i^{(n)} = \dfrac{1}{n} \cdot \dfrac{(-1)^{n-i}}{i!(n-i)!} \int_0^n
               \prod_{\substack{j = 0 \\ j \neq i}}^n (t - j) ~ \mathrm{d} t.

考虑如下的 :math:`n` 次多项式序列:

.. math::
   \ell_i^{(n)}(t) = \dfrac{(-1)^{n-i}}{i!(n-i)!} \prod_{\substack{j = 0 \\ j \neq i}}^n (t - j),

它们满足

.. math::
   \ell_i^{(n)}(j) = \begin{cases}
      1, & j = i, \\
      0, & j \neq i.
   \end{cases}

这 :math:`n + 1` 个 :math:`n` 次多项式构成了 :math:`n + 1` 维线性空间

.. math::
   \mathbb{R}_n [t] := \{ f \in \mathbb{R}[t] ~ : ~ \deg f \leqslant n \}

的一组基, 其中 :math:`\mathbb{R}[t]` 是 :math:`\mathbb{R}` 系数多项式全体. 这是因为假设

.. math::
   \lambda_0 \ell_0^{(n)}(t) + \lambda_1 \ell_1^{(n)}(t) + \cdots + \lambda_n \ell_n^{(n)}(t) = 0,

分别代 :math:`t = 0, 1, \dots, n`, 可对应推出 :math:`\lambda_0 = 0, \lambda_1 = 0, \dots, \lambda_n = 0`.
:math:`\mathbb{R}_n [t]` 另外还有一组基是 :math:`1, t, t^2, \dots, t^n`, 于是有可逆阵
:math:`A \in M_{n+1}(\mathbb{R})` 使得

.. math::
   \begin{pmatrix} 1 \\ t \\ \vdots \\ t^n \end{pmatrix}
   = A \begin{pmatrix} \ell_0^{(n)}(t) \\ \ell_1^{(n)}(t) \\ \vdots \\ \ell_n^{(n)}(t) \end{pmatrix}.

在上式中分别取 :math:`t = 0, 1, \dots, n` 可得

.. math::
   \begin{pmatrix}
   1 & 1 & 1 & \cdots & 1 \\ 0 & 1 & 2 & \cdots & n \\ 0 & 1 & 2^2 & \cdots & n^2 \\
   \vdots & \vdots & \vdots & & \vdots \\ 0 & 1 & 2^n & \cdots & n^n
   \end{pmatrix}
   = A \begin{pmatrix}
   1 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1
   \end{pmatrix} = A.

记 :math:`A` 的逆矩阵 :math:`A^{-1} = B = (b_{ij})_{0 \leqslant i,j \leqslant n}`, 那么

.. math::
   \ell_i^{(n)}(t) = b_{i0} + b_{i1} t + \cdots + b_{in} t^n,

从而有

.. math::
   c_i^{(n)}
   & = \dfrac{1}{n} \int_0^n \left( b_{i0} + b_{i1} t + \cdots + b_{in} t^n \right) ~ \mathrm{d} t \\
   & = \dfrac{1}{n} \sum_{j = 0}^n b_{ij} \dfrac{n^{j+1}}{j+1}.

6. 连续函数与黎曼可积函数复合后不可积的例子

构造定义在闭区间 :math:`[0,1]` 上的函数 :math:`f, g`, 使得:

* :math:`f` 连续;
* :math:`g` 在 :math:`[0,1]` 上黎曼可积;
* 但复合函数 :math:`g(f(x))` 在 :math:`[0,1]` 上黎曼不可积.

首先, 取标准三分 Cantor 集 :math:`C \subset [0,1]`. 该集合具有如下性质:

* :math:`C` 为闭集;
* :math:`m(C) = 0`;
* :math:`C` 无内点, 且 :math:`\partial C = C`.

定义函数

.. math::
   g(x) = \chi_C(x) = \begin{cases}
   1, & x \in C; \
   0, & x \notin C.
   \end{cases}

由于 :math:`g` 的不连续点集合恰为 :math:`C`, 且 :math:`m(C)=0`, 由黎曼可积的勒贝格判别法可知,
:math:`g` 在 :math:`[0,1]` 上黎曼可积.

接下来构造连续函数 :math:`f`.

设 :math:`\Phi(x)` 为 Cantor 函数, 定义

.. math::
   \Psi(x) = \frac{x + \Phi(x)}{2}, \quad x \in [0,1].

函数 :math:`\Psi` 具有如下性质:

* :math:`\Psi` 连续;
* :math:`\Psi` 严格单调递增;
* :math:`\Psi([0,1]) = [0,1]`;

因此, :math:`\Psi` 是 :math:`[0,1]` 到自身的双射, 且其逆函数 :math:`f = \Psi^{-1}` 连续.

下面分析集合在 :math:`\Psi` 下的像.

注意, Cantor 集的补集 :math:`C^c` 是可数个两两不交开区间的并. 在每个这样的开区间 :math:`I` 上,
函数 :math:`\Phi` 为常数, 因此

.. math::
   \Psi(x) = \frac{x + \text{const}}{2}, \quad x \in I,

从而 :math:`\Psi` 在 :math:`I` 上为斜率为 :math:`1/2` 的线性函数. 因此, 长度缩小为原来的一半.

于是有

.. math::
   m(\Psi(C^c)) = \frac{1}{2} m(C^c) = \frac{1}{2}.

从而

.. math::
   m(\Psi(C)) = 1 - \frac{1}{2} = \frac{1}{2}.

考虑复合函数

.. math::
   g(f(x)) = \chi_C(f(x)) = \chi_{\Psi(C)}(x).

即

.. math::
   g \circ f = \chi_{\Psi(C)}.

由于 :math:`\Psi` 为连续严格单调函数, 集合 :math:`\Psi(C)` 仍为闭集, 且无内点, 因此

.. math::
   \partial(\Psi(C)) = \Psi(C).

从而函数 :math:`g \circ f` 的不连续点集合为 :math:`\Psi(C)`, 其测度为

.. math::
   m(\Psi(C)) = \frac{1}{2} > 0.

因此, :math:`g \circ f` 在 :math:`[0,1]` 上的不连续点集合具有正测度, 由黎曼可积判别准则可知,
该函数在 :math:`[0,1]` 上黎曼不可积.

综上, 构造了连续函数 :math:`f` 与黎曼可积函数 :math:`g`, 使得复合函数 :math:`g \circ f` 黎曼不可积.

.. note::
   Cantor 三分集的构造方法是: 从闭区间 :math:`[0,1]` 的正中间挖掉开区间 :math:`(1/3, 2/3)`, 得到两个闭区间 :math:`[0, 1/3]`
   与 :math:`[2/3, 1]`; 接着在每个剩下的闭区间的正中间挖掉长度为 :math:`1/9` 的开区间, 得到 :math:`4` 个闭区间; 以此类推, 在第 :math:`n` 步, 在每个剩下的闭区间的正中间挖掉长度为 :math:`1/3^n` 的开区间, 最终剩下的集合就是 Cantor 三分集. Cantor 三分集
   的元素在 3 进制下的表示方法是: 只包含 :math:`0` 与 :math:`2` 的数, 即

   .. math::
      C = \left\{ \sum_{n=1}^{\infty} \dfrac{2 a_n}{3^n} ~ : ~ a_n \in \{0, 1\} \right\}.

   Cantor 函数的定义: 首先在 Cantor 三分集上定义函数 :math:`\phi` 为

   .. math::
      \phi \left( \sum_{n=1}^{\infty} \dfrac{2 a_n}{3^n} \right) = \sum_{n=1}^{\infty} \dfrac{a_n}{2^{n}}.

   接下来就可以定义 Cantor 函数 :math:`\Phi` 为

   .. math::
      \Phi(x) = \sup_{t \in C, t \leqslant x} \phi(t).
