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
