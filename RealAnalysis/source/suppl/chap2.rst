第二章补充材料
^^^^^^^^^^^^^^^^^^^^^^^^^

.. _reg_outer_measure:

1. 勒贝格外测度的正则性。对任意集合 :math:`E \subset \mathbb{R}^d`, 存在 :math:`G_{\delta}`-集 :math:`A`,
称为 :math:`E` 的等测包，使得 :math:`E \subset A` 且 :math:`m A = m^* E`.

.. proof:proof::

    由外测度定义，对任意自然数 :math:`n \in \mathbb{N}`, 存在开集 :math:`G_n` 使得 :math:`E \subset G_n`,
    且 :math:`m G_n \le m^* E + \frac{1}{n}`. 令 :math:`A = \bigcap\limits_{n=1}^{\infty} G_n`,
    则 :math:`A` 为一个 :math:`G_{\delta}`-集，且 :math:`E \subset A`. 由（外）测度的单调性，有

    .. math::

        m^* E \le m^* A \le m A \le m G_n \le m^* E + \frac{1}{n}.

    令 :math:`n \to \infty`, 则有 :math:`m^* E = m^* A = m A`.

勒贝格外测度的正则性有一系列重要的推论，这里列举几个：

(1). 设 :math:`\{E_n\}_{n=1}^{\infty}` 为 :math:`\mathbb{R}^d` 中的一列点集，那么

.. math::

    \DeclareMathOperator*\lowlim{\underline{lim}}
    \DeclareMathOperator*\uplim{\overline{lim}}

    m^* \left( \lowlim_{n \to \infty} E_n \right) \le \lowlim_{n \to \infty} m^* E_n.

(2). 设 :math:`\{E_n\}_{n=1}^{\infty}` 为 :math:`\mathbb{R}^d` 中的渐张集列，那么

.. math::

    \lim_{n \to \infty} m^* E_n = m^* \left( \lim_{n \to \infty} E_n \right).
