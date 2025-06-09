第十一章补充材料
^^^^^^^^^^^^^^^^^^^^^^^^^

1. 累次极限与重极限所有可能的取值情况如下

.. list-table::
   :widths: 100 100 100

   * - :math:`\lim\limits_{\substack{x \to x_0\\y \to y_0}} f(x, y)`
     - :math:`\lim\limits_{y \to y_0} \lim\limits_{x \to x_0} f(x, y)`
     - :math:`\lim\limits_{x \to x_0} \lim\limits_{y \to y_0} f(x, y)`
   * - A
     - A
     - A
   * - A
     - A
     - ❌
   * - A
     - ❌
     - A
   * - A
     - ❌
     - ❌
   * - ❌
     - A
     - A
   * - ❌
     - A
     - B
   * - ❌
     - ❌
     - A
   * - ❌
     - A
     - ❌
   * - ❌
     - ❌
     - ❌

2. 有限维赋范线性空间中任意范数等价: 设 :math:`V = \mathbb{R}^n` 是 :math:`n` 维赋范线性空间,
则对任意范数 :math:`\|\cdot\|_{(1)}, \|\cdot\|_{(2)}`, 都存在正实数 :math:`c_1, c_2 > 0`, 使得

.. math::

   c_1 \|x\|_{(1)} \leq \|x\|_{(2)} \leq c_2 \|x\|_{(1)}, ~ \forall ~ x \in V.

证明如下: 我们证明 :math:`V` 上任意范数 :math:`\|\cdot\|` 都与 2-范数等价即可, 即存在正实数 :math:`c_1, c_2 > 0`, 使得

.. math::

   c_1 \|x\|_2 \leq \|x\| \leq c_2 \|x\|_2, ~ \forall ~ x \in V.

其中 :math:`\|x\|_2 = \sqrt{\langle x, x \rangle}` 是 :math:`V` 上的 2-范数.
设 :math:`\{e_1, e_2, \ldots, e_n\}` 是 :math:`V` 的自然基, 则任意向量 :math:`x \in V` 都可以表示为

.. math::

   x = a_1 e_1 + a_2 e_2 + \cdots + a_n e_n, ~ a_i \in \mathbb{R}.

由范数的三角不等式以及数乘相容性, 有

.. math::

   \|x\| & \leqslant \|a_1 e_1\| + \|a_2 e_2\| + \cdots + \|a_n e_n\| \\
   & = |a_1| \|e_1\| + |a_2| \|e_2\| + \cdots + |a_n| \|e_n\| \\
   & \leqslant \sqrt{\|e_1\|^2 + \|e_2\|^2 + \cdots + \|e_n\|^2} \cdot \sqrt{|a_1|^2 + |a_2|^2 + \cdots + |a_n|^2} \\
   & = \sqrt{\|e_1\|^2 + \|e_2\|^2 + \cdots + \|e_n\|^2} \cdot \|x\|_2,

取 :math:`c_2 = \sqrt{\|e_1\|^2 + \|e_2\|^2 + \cdots + \|e_n\|^2}`.

另一方面, 考虑

.. math::

   \| \cdot \| : K = \{ x \in V ~ : ~ \|x\|_2 = 1 \} \rightarrow \mathbb{R}, ~ x \mapsto \|x\|.

由于单位球面 :math:`K` 是紧集, 且 :math:`\| \cdot \|` 是连续函数, 故 :math:`\| \cdot \|` 在 :math:`K` 上取得最大值和最小值.
设 :math:`\displaystyle m = \min_{x \in K} \|x\|`. 由范数的非退化性知 :math:`m > 0`. 那么对任意 :math:`x \in V` 有

.. math::

   \|x\| & = \left\| \|x\|_2 \cdot \frac{x}{\|x\|_2} \right\| \\
   & = \|x\|_2 \cdot \left\| \frac{x}{\|x\|_2} \right\| \\
   & \geqslant \|x\|_2 \cdot m \\
   & = m \cdot \|x\|_2.

取 :math:`c_1 = m`, 则有

.. math::

   c_1 \|x\|_2 \leq \|x\| \leq c_2 \|x\|_2, ~ \forall ~ x \in V.


3. 集合在连续向量值函数 :math:`f: \mathbb{R}^n \rightarrow \mathbb{R}^m` 下的性质:

- 设 :math:`E \subset \mathbb{R}^m` 是 :math:`\mathbb{R}^m` 中开集, 那么 :math:`E` 在 :math:`f` 下的原像

  .. math::

      f^{-1}(E) = \{ x \in \mathbb{R}^n ~ : ~ f(x) \in E \}

  必然是 :math:`\mathbb{R}^n` 中的开集.
- 设 :math:`F \subset \mathbb{R}^n` 是 :math:`\mathbb{R}^n` 中有界闭集 (紧集), 那么 :math:`F` 在 :math:`f` 下的像

  .. math::

      f(F) = \{ y \in \mathbb{R}^m ~ : ~ \exists ~ x \in F, ~ f(x) = y \}

  必然是 :math:`\mathbb{R}^m`. 中有界闭集 (紧集).

相关证明如下:

由开集的定义, 只要证明 :math:`\forall ~ x \in f^{-1}(E)`, :math:`x` 是 :math:`f^{-1}(E)` 的内点即可.
由于 :math:`E` 是开集, 那么 :math:`f(x) \in E` 是 :math:`E` 的内点, 从而存在该点的邻域

.. math::

   O(f(x), \varepsilon) = \{ y \in \mathbb{R}^m ~ : ~ d(y, f(x)) < \varepsilon \} \subset E.

由于 :math:`f` 连续, 故对于取好的 :math:`\varepsilon > 0`, 存在 :math:`\delta > 0`,
使得对任意 :math:`\widetilde{x} \in O(f(x), \delta)`, 总有 :math:`d(f(\widetilde{x}), f(x)) < \varepsilon`,
即 :math:`f(\widetilde{x}) \in O(f(x), \varepsilon)`. 这表明

.. math::

   f(O(f(x), \delta)) \subset O(f(x), \varepsilon) \subset E,

即有

.. math::

   O(f(x), \delta) \subset f^{-1}(E),

这就证明了 :math:`x` 是 :math:`f^{-1}(E)` 的内点.

接下来证明 :math:`f(F)` 是紧集. 任取 :math:`f(F)` 的一个开覆盖

.. math::

   f(F) \subset \bigcup_{i \in I} U_i, ~ U_i \text{ 是 $\mathbb{R}^m$ 中开集}.

那么有 :math:`\displaystyle F \subset \bigcup_{i \in I} f^{-1}(U_i)`. 由于 :math:`f` 连续,
故每一个 :math:`f^{-1}(U_i)` 都是 :math:`\mathbb{R}^n` 中开集, 即 :math:`\displaystyle \bigcup_{i \in I} f^{-1}(U_i)`
构成了 :math:`F` 的一个开覆盖. 由于 :math:`F \subset \mathbb{R}^n` 紧集, 可以从这个开覆盖中选出有限子覆盖

.. math::

   F \subset f^{-1}(U_{i_1}) \cup f^{-1}(U_{i_2}) \cup \cdots \cup f^{-1}(U_{i_n}),

从而有

.. math::

   f(F) \subset U_{i_1} \cup U_{i_2} \cup \cdots \cup U_{i_n}.

也就是说, 对 :math:`f(F)` 的任意开覆盖, 都可以从中选取出它的有限开覆盖, 故 :math:`f(F)` 是紧集, 即有界闭集.
