第三章补充材料
^^^^^^^^^^^^^^^^^^^^^^^^^

.. _measurable_function_supp:

1. 设 :math:`f` 是可测集 :math:`E` 上的函数， :math:`D` 是 :math:`\mathbb{R}` 中稠密集，
若 :math:`\forall \alpha \in D`, :math:`E(f > \alpha)` 都是可测集，则 :math:`f` 是可测函数。

.. proof:proof::

    任取实数 :math:`r \in \mathbb{R}`，由于 :math:`D` 是 :math:`\mathbb{R}` 中稠密集，
    所以存在 :math:`D` 中点列 :math:`\{\alpha_k\}_{k \in \mathbb{N}}` 使得 :math:`\alpha_k > r`,
    且 :math:`\displaystyle \lim_{k \to \infty} \alpha_k = r`. 那么可以断言有

    .. math::

        E(f > r) = \bigcup_{k \in \mathbb{N}} E(f > \alpha_k).

    首先，由于 :math:`\alpha_k > r`，所以 :math:`E(f > r) \supset E(f > \alpha_k)`, 从而知上式左边包含右边。
    另一方面， :math:`\forall x \in E(f > r)`, 有 :math:`f(x) > r`，所以存在 :math:`k_0 \in \mathbb{N}` 使得
    :math:`f(x) \ge \alpha_{k_0} \ge r`，从而 :math:`x \in E(f > \alpha_{k_0})`，所以上式右边包含左边。

    由于 :math:`E(f > \alpha_k)` 都是可测集，所以 :math:`E(f > r)` 也是可测集，这说明 :math:`f` 是可测函数。
