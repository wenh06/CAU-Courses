第二章补充材料
^^^^^^^^^^^^^^^^^^^^^^^^^

.. _reg-outer-measure:

1. 勒贝格外测度的正则性. 对任意集合 :math:`E \subset \mathbb{R}^d`, 存在 :math:`G_{\delta}`-集 :math:`A`,
   称为 :math:`E` 的等测包, 使得 :math:`E \subset A` 且 :math:`m A = m^* E`.

.. proof:proof::

    由外测度定义, 对任意自然数 :math:`n \in \mathbb{N}`, 存在开集 :math:`G_n` 使得 :math:`E \subset G_n`,
    且 :math:`m G_n \leqslant m^* E + \frac{1}{n}`. 令 :math:`A = \bigcap\limits_{n=1}^{\infty} G_n`,
    则 :math:`A` 为一个 :math:`G_{\delta}`-集, 且 :math:`E \subset A`. 由 (外) 测度的单调性, 有

    .. math::

        m^* E \leqslant m^* A \leqslant m A \leqslant m G_n \leqslant m^* E + \frac{1}{n}.

    令 :math:`n \to \infty`, 则有 :math:`m^* E = m^* A = m A`.

勒贝格外测度的正则性有一系列重要的推论, 这里列举几个:

(1). 设 :math:`\{E_n\}_{n=1}^{\infty}` 为 :math:`\mathbb{R}^d` 中的一列点集, 那么

     .. math::

         \DeclareMathOperator*\lowlim{\underline{lim}}
         \DeclareMathOperator*\uplim{\overline{lim}}

         m^* \left( \lowlim_{n \to \infty} E_n \right) \leqslant \lowlim_{n \to \infty} m^* E_n.

(2). 设 :math:`\{E_n\}_{n=1}^{\infty}` 为 :math:`\mathbb{R}^d` 中的渐张集列, 那么

     .. math::

         \lim_{n \to \infty} m^* E_n = m^* \left( \lim_{n \to \infty} E_n \right).

.. _sigma_ring:

2. 设 :math:`\mathscr{E}` 为基本集 :math:`X` 的子集族, 那么它生成的环 :math:`\mathscr{R}(\mathscr{E})` 包含于

   .. math::

      \mathscr{R} :=
      \left\{ E \subset X ~ : ~ E \subset \bigcup\limits_{k=1}^{n} E_k, ~ n \in \mathbb{N}, E_1, \dots, E_n \in \mathscr{E} \right\}.

   首先, 验证 :math:`\mathscr{R}` 是一个环. 它关于有限并运算的封闭性显然, 只需验证它关于差运算的封闭性. 对任意 :math:`E \subset \bigcup\limits_{k=1}^{n} E_k`,
   :math:`F \subset \bigcup\limits_{j=1}^{m} F_j \in \mathscr{R}`, 有

   .. math::

      E \setminus F \subset E \subset \bigcup\limits_{k=1}^{n} E_k,

   从而知 :math:`E \setminus F \in \mathscr{R}`.

   其次, 由于 :math:`\mathscr{R}(\mathscr{E})` 是包含 :math:`\mathscr{E}` 的最小环, 所以 :math:`\mathscr{R}(\mathscr{E}) \subset \mathscr{R}`.
