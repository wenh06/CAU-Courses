§1 集及其运算
----------------

.. _ex-1-1:

1. 证明关系式

   (1). :math:`(A \setminus B) \cap (C \setminus D) = (A \cap C) \setminus (B \cup D).`

   (2). :math:`(A \cap B) \cup C = (A \cup C) \cap (B \cup C).`

   (3). :math:`A \setminus (B \setminus C) \subset (A \setminus B) \cup C.`

   (4). :math:`(A \setminus B) \setminus (C \setminus D) \subset (A \setminus C) \cup (D \setminus B).`

   (5). :math:`(A \setminus B) \cup C = A \setminus (B \setminus C)` 成立的充要条件是什么?

   (6). :math:`A \cup (B \setminus C) = (A \cup B) \setminus C` 是否成立?

.. proof:proof::

   总可以假设上述集合都包含在某个基本集 :math:`X` 中, 于是可以将差集写成与相应补集的交集.

   (1). 有

   .. math::

      \begin{align*}
      & (A \setminus B) \cap (C \setminus D) \\
      = & (A \cap \mathscr{C} B) \cap (C \cap \mathscr{C} D) = (A \cap C) \cap (\mathscr{C} B \cap \mathscr{C} D) \\
      = & (A \cap C) \cap \mathscr{C} ( B \cup D) = (A \cap C) \setminus (B \cup D)
      \end{align*}

   (2). 这是集合交、并运算的分配律.

   (3). 有

   .. math::

      \begin{align*}
      & A \setminus (B \setminus C) \\
      = & A \cap \mathscr{C} (B \cap \mathscr{C} C) = A \cap (\mathscr{C} B \cup C) \\
      = & (A \cap \mathscr{C} B) \cup (A \cap C) \subset (A \setminus B) \cup C
      \end{align*}

   (4). 有

   .. math::

      \begin{align*}
      & (A \setminus B) \setminus (C \setminus D) \\
      = & (A \cap \mathscr{C} B) \cap \mathscr{C}(C \cap \mathscr{C} D) = (A \cap \mathscr{C} B) \cap (\mathscr{C} C \cup D) \\
      = & (A \cap \mathscr{C} B \cap \mathscr{C} C) \cup (A \cap \mathscr{C} B \cap D) = ((A \cap \mathscr{C} B) \setminus C) \cup ((D \cap A) \setminus B) \\
      \subset & (A \setminus C) \cup (D \setminus B)
      \end{align*}

   (5). 等式的左边化为集合交、并的形式为

   .. math::
      :label: 1-5-left

      \begin{align*}
      & (A \setminus B) \cup C \\
      = & (A \cap \mathscr{C} B) \cup C = (A \cup C) \cap (\mathscr{C} B \cup C) \\
      = & (A \cap (\mathscr{C} B \cup C)) \cup (C \cap (\mathscr{C} B \cup C)) \\
      = & (A \cap (\mathscr{C} B \cup C)) \cup C
      \end{align*}

   等式的右边化为集合交、并的形式为

   .. math::
      :label: 1-5-right

      A \cap \mathscr{C} (B \cap \mathscr{C} C) = A \cap (\mathscr{C} B \cup C)

   比较式 :eq:`1-5-left` 与式 :eq:`1-5-right`, 若要使等式成立, 必须有 :math:`(A \cap (\mathscr{C} B \cup C)) \cup C = A \cap (\mathscr{C} B \cup C)`,
   这要求 :math:`C \subset A \cap (\mathscr{C} B \cup C)`. 因为 :math:`C \subset \mathscr{C} B \cup C` 是显然的, 故上式等价于 :math:`C \subset A`.

   (6). 不成立. 因为集合 :math:`A` 是左边 :math:`A \cup (B \setminus C)` 的一个子集, 但如果 :math:`A \cap C \neq \emptyset` 的话,
   集合 :math:`A` 不是右边 :math:`(A \cup B) \setminus C` 的子集.

.. _ex-1-3:

3. 设给出集 :math:`E` 与任一集族 :math:`A_{\alpha}, \alpha \in I`, 问关系式

   .. math::

      E \cup \bigcap_{\alpha \in I} A_{\alpha} = \bigcap_{\alpha \in I} (E \cup A_{\alpha})

是否恒成立?

.. proof:proof::

   首先证明左边包含于右边. 任取 :math:`x \in E \cup \bigcap\limits_{\alpha \in I} A_{\alpha}`, 若 :math:`x \in E`,
   那么由于 :math:`E \subset E \cup A_{\alpha}, \forall \alpha \in I`, 从而有 :math:`x \in E \cup A_{\alpha}, \forall \alpha \in I`,
   那么有 :math:`x \in \bigcap\limits_{\alpha \in I} (E \cup A_{\alpha})`. 若 :math:`x \not\in E`, 那么 :math:`x \in \bigcap\limits_{\alpha \in I} A_{\alpha}`,
   从而 :math:`x \in E \cup A_{\alpha}, \forall \alpha \in I`, 所以 :math:`x \in \bigcap\limits_{\alpha \in I} (E \cup A_{\alpha})`.

   再证明右边包含于左边. 任取 :math:`x \in \bigcap\limits_{\alpha \in I} (E \cup A_{\alpha})`, 那么 :math:`x \in E \cup A_{\alpha}, \forall \alpha \in I`.
   即对任意 :math:`\alpha \in I`, 或有 :math:`x \in E`, 或有 :math:`x \in A_{\alpha}`. 若 :math:`x \in E`, 那么 :math:`x \in E \cup \bigcap\limits_{\alpha \in I} A_{\alpha}`.
   若 :math:`x \not\in E`, 那么就必须有 :math:`x \in A_{\alpha}, \forall \alpha \in I`, 从而 :math:`x \in \bigcap\limits_{\alpha \in I} A_{\alpha}`, 这种情况下同样有
   :math:`x \in E \cup \bigcap\limits_{\alpha \in I} A_{\alpha}`.

.. _ex-1-5:

5. 定义集 :math:`A, B` 的 **对称差** 为 :math:`A \triangle B = (A \setminus B) \cup (B \setminus A)`. 试证对任意集 :math:`A, B, C` 有

   (1). :math:`A = B` 的充分必要条件为 :math:`A \triangle B = \emptyset`.

   (2). :math:`A \cup B = (A \cap B) \cup (A \triangle B)`.

   (3). :math:`A \triangle B \subset (A \triangle C) \cup (C \triangle B)`.

.. proof:proof::

   (1). :math:`A = B \Longleftrightarrow A \setminus B = \emptyset \land B \setminus A = \emptyset \Longleftrightarrow A \triangle B = (A \setminus B) \cup (B \setminus A) = \emptyset`.

   (2). 容易知道, 对任意两个集合 :math:`A, B`, 总有 :math:`A \cup (B \setminus A) = A \cup B`, 于是有

   .. math::

      \begin{align*}
      & (A \cap B) \cup (A \triangle B) \\
      = & (A \cap B) \cup \Bigl((A \setminus B) \cup (B \setminus A)\Bigr) \\
      = & \Bigl(\bigl(A \cup (B \setminus A)\bigr) \cup (A \setminus B)\Bigr) \cap \Bigl(\bigl(B \cup (A \setminus B)\bigr) \cup (B \setminus A)\Bigr) \\
      = & \Bigl((A \cup B) \cup (A \setminus B)\Bigr) \cap \Bigl((B \cup A) \cup (B \setminus A)\Bigr) \\
      = & (A \cup B) \cap (B \cup A) \\
      = & A \cup B
      \end{align*}

   (3). 任取 :math:`x \in A \triangle B`, 要么有 :math:`x \in A \setminus (A \cap B)`, 要么有 :math:`x \in B \setminus (A \cap B)`,
   这两种情况有且只有一种成立. 以下对 :math:`x` 是否属于集合 :math:`C` 分两种情况讨论.

   情况1. 若 :math:`x \not\in C`, 那么

      情况1.1. 若 :math:`x \in A \setminus (A \cap B)`, 那么此时有 :math:`(x \in A) \land (x \not\in C)`,
      即有 :math:`x \in A \setminus C \subset A \triangle C \subset (A \triangle C) \cup (C \triangle B)`.

      情况1.2. 若 :math:`x \in B \setminus (A \cap B)`, 那么此时有 :math:`(x \in B) \land (x \not\in C)`,
      即有 :math:`x \in B \setminus C \subset B \triangle C \subset (A \triangle C) \cup (C \triangle B)`.

   情况2. 若 :math:`x \in C`, 那么

      情况2.1. 若 :math:`x \in A \setminus (A \cap B)`, 那么此时有 :math:`(x \not \in B) \land (x \in C)`,
      即有 :math:`x \in C \setminus B \subset C \triangle B \subset (A \triangle C) \cup (C \triangle B)`.

      情况2.2. 若 :math:`x \in B \setminus (A \cap B)`, 那么此时有 :math:`(x \not \in A) \land (x \in C)`,
      即有 :math:`x \in C \setminus A \subset C \triangle A \subset (A \triangle C) \cup (C \triangle B)`.

   综上所述, 对任意 :math:`x \in A \triangle B`, 总有 :math:`x \in (A \triangle C) \cup (C \triangle B)`,
   从而有 :math:`A \triangle B \subset (A \triangle C) \cup (C \triangle B)`.

.. _ex-1-6:

6. 设 :math:`E_n = \left\{ m / n : m \in \mathbb{Z} \right\}, n \in \mathbb{N}`, 证明 :math:`\varliminf\limits_{n} E_n = \mathbb{Z}`,
   :math:`\varlimsup\limits_{n} E_n = \mathbb{Q}`. 这里的 **上限集、下限集** 分别定义为
   :math:`\varliminf\limits_{n} E_n = \bigcup\limits\limits_{k=1}^{\infty} \bigcap\limits_{n=k}^{\infty} E_n`, 以及
   :math:`\varlimsup\limits_{n} E_n = \bigcap\limits\limits_{k=1}^{\infty} \bigcup\limits_{n=k}^{\infty} E_n`.

.. proof:proof::

   对任意 :math:`n \in \mathbb{N}`, 考虑 :math:`m \in n \mathbb{Z}`, 那么总有 :math:`\mathbb{Z} = \left\{ m / n : m \in n\mathbb{Z} \right\} \subset E_n`,
   从而有 :math:`\mathbb{Z} \subset \bigcap\limits_{n=1}^{\infty} E_n`,
   于是有 :math:`\mathbb{Z} \subset \bigcup\limits\limits_{k=1}^{\infty} \bigcap\limits_{n=k}^{\infty} E_n = \varliminf\limits_{n} E_n`.
   另一方面, 任取 :math:`x \in \varliminf\limits_{n} E_n = \bigcup\limits\limits_{k=1}^{\infty} \bigcap\limits_{n=k}^{\infty} E_n`,
   那么存在 :math:`k \in \mathbb{N}`, 使得 :math:`x \in \bigcap\limits_{n=k}^{\infty} E_n`. 将 :math:`x = \dfrac{p}{q}, q > 0` 写为既约分数的形式,
   那么 :math:`\forall n \geqslant k, n \in \mathbb{N}`, 都有 :math:`x = \dfrac{p}{q} \in E_n = \left\{ m / n : m \in \mathbb{Z} \right\}`. 假设 :math:`q \neq 1`,
   那么取 :math:`n \in \mathbb{N}`, 使得 :math:`n > k` 且不被 :math:`q` 的某个素因子 :math:`p_0 > 1` 整除. 那么由 :math:`\dfrac{p}{q} = \dfrac{m}{n}`,
   即 :math:`p n = q m`, 两边不可能有相同的素因子组 (例如 :math:`p_0` 不是左边的素因子, 但是是右边的素因子). 所以 :math:`q \neq 1` 的假设不成立, 也就是说
   :math:`\varliminf\limits_{n} E_n` 中任何元素写成既约分数的形式时, 分母都是1, 也就是说 :math:`\varliminf\limits_{n} E_n \subset \mathbb{Z}`.
   综上所述, 有 :math:`\varliminf\limits_{n} E_n = \mathbb{Z}`.

   由于对任意 :math:`n \in \mathbb{N}`, 都有 :math:`E_n \subset \mathbb{Q}`, 于是 :math:`\bigcup\limits_{k=n}^{\infty} E_n \subset \mathbb{Q}`
   对任意 :math:`k \in \mathbb{N}` 成立, 进而有
   :math:`\varlimsup\limits_{n} E_n = \bigcap\limits_{k=1}^{\infty} \bigcup\limits_{n=k}^{\infty} E_n \subset \mathbb{Q}`. 反过来,
   任取 :math:`x = \dfrac{p}{q} \in \mathbb{Q}, q > 0`, 并设其为既约分数. 令 :math:`n = k \cdot q`, 那么有
   :math:`x = \dfrac{p}{q} = \dfrac{kp}{kq} = \dfrac{kp}{n} \in E_n = \left\{ m / n : m \in \mathbb{Z} \right\}`,
   这就证明了 :math:`x \in \bigcup\limits_{k=n}^{\infty} E_n` 对任意 :math:`k \in \mathbb{N}` 成立. 那么有 :math:`\mathbb{Q} \subset \varlimsup\limits_{n} E_n`.
   综上所述, 有 :math:`\varlimsup\limits_{n} E_n = \mathbb{Q}`.

   .. note::

      我们通常可将 :math:`E_n` 简写为 :math:`\dfrac{1}{n} \mathbb{Z}`, 那么这题的结论可以用数学符号更简洁地表达为

      .. math::

         \varliminf\limits_{n} \dfrac{1}{n} \mathbb{Z} = \mathbb{Z}, \quad \varlimsup\limits_{n} \dfrac{1}{n} \mathbb{Z} = \mathbb{Q}.
