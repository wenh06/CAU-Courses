§2 可测函数列的收敛性
------------------------------------------

13. 试给出关于可测函数列当极限函数为无穷大情形的相应 Egorov 定理的陈述并加以证明.

.. proof:solution::

    待写

14. 设 :math:`x \in [0, 1)`, 其二进表示为 :math:`\displaystyle x = \sum_{i=1}^\infty \frac{x_i}{2^i}`,
:math:`x_i \in \{0, 1\}`, 并约定用有尽表示。定义函数 :math:`\displaystyle \varphi (x) = \sum_{i=1}^\infty \frac{2x_i}{3^i}`,
再取 :math:`[0, 1]` 的一不可测子集 :math:`E`, 并在 :math:`\mathbb{R}` 上定义函数

.. math::

    \psi (x) = \begin{cases}
        \varphi (x), & x \in E, \\
        0, & \text{其余情形}.
    \end{cases}

试证 :math:`\varphi, \psi` 均可测, 但 :math:`\psi \circ \varphi` 不可测。

.. proof:proof::

    待写

17. 设函数列 :math:`\{f_n\}_{n \in \mathbb{N}}` 在 :math:`E` 上依测度收敛于 :math:`f`, 且在 :math:`E` 上几乎处处有 :math:`f_n \le g`,
:math:`n \in \mathbb{N}`. 试证在 :math:`E` 上几乎处处有 :math:`f \le g`.

.. proof:proof::

    待写

21. 试构造 :math:`[0, 1]` 上的连续函数列 :math:`\{f_n\}_{n \in \mathbb{N}}`, 使满足
(i) :math:`\{f_n\}_{n \in \mathbb{N}}` 在 :math:`[0, 1]` 上几乎处处收敛于 :math:`0`,
但 (ii) :math:`\{f_n\}_{n \in \mathbb{N}}` 在任何子区间上不一致收敛于 :math:`0`.

.. proof:solution::

    待写

22. 设 :math:`f, f_n (n \in \mathbb{N})` 是定义在区间 :math:`E = [a, b]` 上的实函数， :math:`r` 为自然数，
用记号 :math:`E(\lvert f_n - f \rvert \le 1 / r)` 表示 :math:`E` 中满足 :math:`\lvert f_n (x) - f (x) \rvert \le 1 / r` 的点所成的集。
试证集 :math:`\displaystyle \cap_{r=1}^\infty E(\lvert f_n - f \rvert \le 1 / r)` 是 :math:`E` 中使
:math:`\{f_n\}_{n \in \mathbb{N}}` 收敛于 :math:`f` （当 :math:`n \to \infty` ）的点集。
