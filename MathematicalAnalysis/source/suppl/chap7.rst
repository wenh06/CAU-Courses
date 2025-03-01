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
