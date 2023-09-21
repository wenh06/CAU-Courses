第一章  集与点集
^^^^^^^^^^^^^^^^^^^^^^^^^

..  contents:: :local:

§1 集及其运算
----------------

1. 证明关系式

(1). :math:`(A \setminus B) \cap (C \setminus D) = (A \cap C) \setminus (B \cup D).`

(2). :math:`(A \cap B) \cup C = (A \cup C) \cap (B \cup C).`

(3). :math:`A \setminus (B \setminus C) \subset (A \setminus B) \cup C.`

(4). :math:`(A \setminus B) \setminus (C \setminus D) \subset (A \setminus C) \cup (D \setminus B).`

(5). :math:`(A \setminus B) \cup C = A \setminus (B \setminus C)` 成立的充要条件是什么？

(6). :math:`A \cup (B \setminus C) = (A \cup B) \setminus C` 是否成立？

.. proof:proof::

    总可以假设上述集合都包含在某个基本集 :math:`X` 中，于是可以将差集写成与相应补集的交集。

    (1). 有

    .. math::

        \begin{align*}
        & (A \setminus B) \cap (C \setminus D) \\
        = & (A \cap \mathcal{C} B) \cap (C \cap \mathcal{C} D) = (A \cap C) \cap (\mathcal{C} B \cap \mathcal{C} D) \\
        = & (A \cap C) \cap \mathcal{C} ( B \cup D) = (A \cap C) \setminus (B \cup D)
        \end{align*}

    (2). 这是集合交、并运算的分配律。

    (3). 有

    .. math::

        \begin{align*}
        & A \setminus (B \setminus C) \\
        = & A \cap \mathcal{C} (B \cap \mathcal{C} C) = A \cap (\mathcal{C} B \cup C) \\
        = & (A \cap \mathcal{C} B) \cup (A \cap C) \subset (A \setminus B) \cup C
        \end{align*}

    (4). 有

    .. math::

        \begin{align*}
        & (A \setminus B) \setminus (C \setminus D) \\
        = & (A \cap \mathcal{C} B) \cap \mathcal{C}(C \cap \mathcal{C} D) = (A \cap \mathcal{C} B) \cap (\mathcal{C} C \cup D) \\
        = & (A \cap \mathcal{C} B \cap \mathcal{C} C) \cup (A \cap \mathcal{C} B \cap D) = ((A \cap \mathcal{C} B) \setminus C) \cup ((D \cap A) \setminus B) \\
        \subset & (A \setminus C) \cup (D \setminus B)
        \end{align*}

    (5). 待写

    (6). 待写

