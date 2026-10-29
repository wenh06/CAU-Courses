§5–§7 抽象测度与复测度
------------------------------------------

.. note::

   本节标题为暂拟（原书练习册仅以“§5–§7”标出题组，未印节名），待核对教材后可改名.

.. _ex-2-39:

39. 下列各题中给出了在 :math:`\sigma` 环 :math:`\mathscr{R}_\sigma` 上集的集函数 :math:`\lambda`
    的例子, 问哪些是外测度, 哪些不是?

    (1) :math:`X` 是任意非空集, :math:`\mathscr{R}_\sigma` 是 :math:`X` 的一切子集的类. 对于任意
        :math:`E \in \mathscr{R}_\sigma`, 令 :math:`\lambda E = \chi_E (x_0)`, 这里 :math:`x_0` 是
        :math:`X` 中一固定点, :math:`\chi_E` 是集 :math:`E` 的特征函数.

    (2) :math:`X` 是正整数集, :math:`\mathscr{R}_\sigma` 是 :math:`X` 的一切子集的类. 对任意
        :math:`E \in \mathscr{R}_\sigma`, 用 :math:`N(E)` 表示 :math:`E` 中点的个数. 令

        .. math::
          \lambda E = \varlimsup_{n \to \infty} N (E \cap \{ 1, 2, \cdots, n \}) / n,
          \quad E \in \mathscr{R}_\sigma.

    (3) 设 :math:`\mu^*` 是 :math:`\mathscr{R}_\sigma` 上的外测度, :math:`E_0` 是
        :math:`\mathscr{R}_\sigma` 的一确定元. 令 :math:`\lambda E = \mu^* (E \cap E_0)`,
        :math:`E \in \mathscr{R}_\sigma`. (:math:`\lambda` 称为 :math:`\mu^*` 关于 :math:`E_0`
        的吸收.)

    (4) 设 :math:`\mu_1^*, \mu_2^*` 是 :math:`\mathscr{R}_\sigma` 上两个外测度, 令
        :math:`\lambda E = a \mu_1^* E + b \mu_2^* E`, :math:`E \in \mathscr{R}_\sigma`, 这里
        :math:`a, b` 是实常数.

.. proof:solution::

   待写

.. _ex-2-40:

40. 设 :math:`\mathscr{B}` 是基本集 :math:`X` 上的 :math:`\sigma` 代数, 并且 :math:`\mu` 是
    :math:`\mathscr{B}` 上的复函数. 如果对 :math:`E` 在 :math:`\mathscr{B}` 中的任一互斥分解
    :math:`E = \bigvee_{k=1}^{\infty} E_k`, 都有 :math:`\mu E = \sum_{k=1}^{\infty} \mu E_k`,
    则称 :math:`\mu` 是 :math:`X` 上的复测度.

    (1) 若 :math:`\mu` 是 :math:`X` 上的复测度, 证明由
        :math:`\lvert \mu \rvert (E) = \sup \sum\limits_{k=1}^{\infty} \lvert \mu E_k \rvert`
        (:math:`E \in \mathscr{B}`, :math:`E = \bigvee_k E_k` 为 :math:`\mathscr{B}` 中的互斥分解)
        定义的 :math:`\lvert \mu \rvert` 为 :math:`\mathscr{B}` 上的测度.

    (2) 若 :math:`\mu` 是 :math:`X` 上的复测度, 证明 :math:`\lvert \mu \rvert (X) < \infty`.

    (3) 问所述复测度与广义测度有何关系?

.. proof:proof::

   待写

.. _ex-2-41:

41. 设 :math:`\mu` 是 :math:`\sigma` 代数 :math:`\mathscr{B}` 上的复测度,
    :math:`E \in \mathscr{B}`, 并令 :math:`\alpha = \sup \lvert \mu A \rvert`, 这里 :math:`A` 是
    :math:`\mathscr{B}` 中含于 :math:`E` 的任意元, 试证
    :math:`\alpha \leqslant \lvert \mu \rvert (E) \leqslant 4 \alpha`.

.. proof:proof::

   待写

.. _ex-2-42:

42. 设在可测空间 :math:`(X, \mathscr{B})` 上给定两个测度 :math:`\mu_1, \mu_2`, 令
    :math:`\mu = a_1 \mu_1 + a_2 \mu_2`, 这里 :math:`a_1, a_2` 是实数. 试证: 存在 :math:`X` 的
    分解 :math:`X = A \cup B`, :math:`A \cap B = \emptyset`, 使 :math:`A` 为 :math:`\mu` 的
    非负集, :math:`B` 为 :math:`\mu` 的非正集.

.. proof:proof::

   待写
