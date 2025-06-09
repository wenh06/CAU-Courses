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

2. 集合在连续向量值函数 :math:`f: \mathbb{R}^n \rightarrow \mathbb{R}^m` 下的性质:

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
