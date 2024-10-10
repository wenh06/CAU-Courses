§3 可测集的性质
------------------------------------------

.. _ex-2-9:

9. 设 :math:`E_1, E_2` 均为有界可测集，试证

   .. math::

      m (E_1 \cup E_2) = m E_1 + m E_2 - m (E_1 \cap E_2).

.. proof:proof::

   因为 :math:`E_1, E_2` 均为有界可测集，所以 :math:`E_1 \cup E_2, E_1 \setminus E_2, E_2 \setminus E_1, E_1 \cap E_2` 均为有界可测集，且

   .. math::

      E_1 \cup E_2 = (E_1 \setminus E_2) \cup (E_2 \setminus E_1) \cup (E_1 \cap E_2)

   为可测集的不交并，所以根据测度的完全可加性有

   .. math::

      m (E_1 \cup E_2) = m (E_1 \setminus E_2) + m (E_2 \setminus E_1) + m (E_1 \cap E_2).

   另一方面，:math:`E_1` 有互斥分解 :math:`E_1 = (E_1 \setminus E_2) \cup (E_1 \cap E_2)`,
   所以根据测度的完全可加性有 :math:`m E_1 = m (E_1 \setminus E_2) + m (E_1 \cap E_2)`.
   同理 :math:`m E_2 = m (E_2 \setminus E_1) + m (E_1 \cap E_2)`，所以有

   .. math::

      m (E_1 \cup E_2) = m E_1 + m E_2 - m (E_1 \cap E_2).

.. _ex-2-10:

10. 设 :math:`E` 是 :math:`\mathbb{R}` 中可测集，:math:`A` 是任意集，证明

    .. math::

      m^* (E \cup A) + m^* (E \cap A) = m E + m^* A;

    :math:`E` 不可测时如何？

.. proof:proof::

   由 Carathéodory 条件，对于任意集 :math:`A` 有

   .. math::

      m^* A = m^* (A \cap E) + m^* (A \cap \mathscr{C} E).

   对集 :math:`A \cup E` 再次应用 Carathéodory 条件，有

   .. math::

      m^* (A \cup E) = m^* ((A \cup E) \cap E) + m^* ((A \cup E) \cap \mathscr{C} E) = m E + m^* (A \cap \mathscr{C} E).

   两式消去共同项 :math:`m^* (A \cap \mathscr{C} E)` 即有

   .. math::

      m^* (E \cup A) + m^* (E \cap A) = m E + m^* A.

   当 :math:`E` 不可测时，我们只能根据内测度以及外测度的半可加性得到

   .. math::

      m^* (E \cup A) + m^* (E \cap A) \leqslant m^* E + m^* A, \\
      m_* (E \cup A) + m_* (E \cap A) \geqslant m_* E + m_* A.

.. _ex-2-11:

11. 设 :math:`\{ E_n \}` 为 :math:`[0, 1]` 中的集列，满足

    .. math::

      \sum\limits_{n=1}^\infty m^* E_n = \infty,

   问是否有 :math:`m^* \left( \varlimsup\limits_{n} E_n \right) > 0`?

.. proof:solution::

   不一定。反例如下：令 :math:`E_n = \left[ 0, \dfrac{1}{n} \right]`, 那么有 :math:`m^* E_n = \dfrac{1}{n}`, 从而有

   .. math::

      \sum\limits_{n=1}^\infty m^* E_n = \sum\limits_{n=1}^\infty \dfrac{1}{n} = \infty.

   但是 :math:`\varlimsup\limits_{n} E_n = \{ 0 \}`, 从而有 :math:`m^* \left( \varlimsup\limits_{n} E_n \right) = 0`.

.. _ex-2-12:

12. 设 :math:`E` 为可测集，问二式 :math:`m \overline{E} = m E, m E^{\circ} = m E` 是否成立？这里 :math:`\overline{E}` 是 :math:`E` 的闭包，
    :math:`E^{\circ}` 是由 :math:`E` 的一切内点所成的集 (即 :math:`E` 的内部).

.. proof:solution::

   不一定。反例如下：

   令 :math:`E = \mathbb{Q} \cap [0, 1]`, 那么有 :math:`m E = 0`, 但是 :math:`\overline{E} = [0, 1]`, 从而有 :math:`m \overline{E} = 1`.

   设 :math:`E` 为一个胖 Cantor 集 (具体构造见 :ref:`本节第 20 题 <ex-2-20>`), 那么有 :math:`m E > 0`, 但是 :math:`E^{\circ} = \emptyset`, 从而有 :math:`m E^{\circ} = 0`.

.. _ex-2-13:

13. 设 :math:`G` 是开集， :math:`E` 是零测度集，试证 :math:`\overline{G} = \overline{G \setminus E}`.

.. proof:proof::

   由于 :math:`G \supset G \setminus E`，所以 :math:`\overline{G} \supset \overline{G \setminus E}`. 假设这是一个真包含关系，
   那么存在 :math:`x \in \mathbb{R}` 以及 :math:`x` 的去心邻域 :math:`\mathring{U} (x)`，使得

   .. math::

      \mathring{U} (x) \cap G \neq \emptyset \\
      \mathring{U} (x) \cap (G \setminus E) = \emptyset.

   由于 :math:`G` 是开集，所以 :math:`\mathring{U} (x) \cap G` 也是开集. 任取 :math:`\mathring{U} (x) \cap G` 的一个构成区间 :math:`(a, b)`,
   那么有 :math:`(a, b) \subset E`，这与 :math:`E` 是零测度集矛盾，所以 :math:`\overline{G} = \overline{G \setminus E}`.

.. _ex-2-14:

14. 设 :math:`E_1 \subset E_2 \subset \cdots \subset E_n \subset \cdots`，试证
    :math:`m^* \left( \bigcup\limits_{n=1}^\infty E_n \right) = \lim\limits_{n \to \infty} m^* E_n`.

.. proof:proof::

   令 :math:`S = \bigcup\limits_{n=1}^\infty E_n`, 那么有 :math:`E_n \subset S`. 那么由外测度的单调性有

   .. math::

      m^* E_n \leqslant  m^* S.

   令 :math:`n \to \infty` 即有

   .. math::

      \lim\limits_{n \to \infty} m^* E_n \leqslant m^* S = m^* \left( \bigcup\limits_{n=1}^\infty E_n \right).

   另一方面，由 :ref:`勒贝格外测度的正则性 <reg-outer-measure>`, 即对于任意 :math:`E_n`，存在开集 :math:`G_{\delta}`-集 :math:`A_n \supset E_n`,
   使得 :math:`m A_n = m^* E_n`, 令

   .. math::

      C_n = \bigcap\limits_{k=n}^{\infty} A_k, \quad n \in \mathbb{N}.

   那么 :math:`C_n` 也是 :math:`G_{\delta}`-集，从而可测，而且 :math:`\{C_n\}` 构成（可测集的）渐张列，那么有

   .. math::

      m \left( \bigcup\limits_{n=1}^{\infty} C_n \right) = \lim\limits_{n \to \infty} m C_n.

   又由于有包含关系 :math:`E_n \subset C_n \subset A_n`, 以及 :math:`m A_n = m^* E_n`, 所以有

   .. math::

      m A_n = m C_n = m^* E_n, \quad n \in \mathbb{N},

   而且进一步有不等式

   .. math::

      m^* \left( \bigcup\limits_{n=1}^\infty E_n \right) \leqslant m \left( \bigcup\limits_{n=1}^\infty C_n \right)
      = \lim\limits_{n \to \infty} m C_n = \lim\limits_{n \to \infty} m^* E_n.

   综上所述，有 :math:`m^* \left( \bigcup\limits_{n=1}^\infty E_n \right) = \lim\limits_{n \to \infty} m^* E_n`.

.. _ex-2-15:

15. 给出互不相交的集列 :math:`\{E_n\}_{n \in \mathbb{N}}`，满足

    .. math::

      m^* \left( \bigcup_{n=1}^\infty E_n \right) < \sum_{n=1}^\infty m^* (E_n).

.. proof:proof::

   仿照 :ref:`第一章第 21 题 <ex-1-21>` 中的构造，也是本章第四节定理 4.1 中的构造，定义区间 :math:`[0, 1)` 上的一个等价关系为

   .. math::

      x \sim y \Longleftrightarrow x - y \in \mathbb{Q}, \quad x, y \in [0, 1),

   并从 :math:`[0, 1) / \sim` 的每个等价类中取一个元素，构成集合 :math:`E`, 那么由本章第四节定理 4.1 知 :math:`E` 是一个不可测集，
   从而有 :math:`m^* E > 0`, 否则它就是零测集，从而可测. 令

   .. math::

      E_n = E + r_n \mod 1 = \{ x + r_n \mod 1 : x \in E \},

   :math:`n \in \mathbb{N}, \mathbb{Q} = \{r_n\}_{n \in \mathbb{N}}`, 那么 :math:`E_n` 互不相交，
   且 :math:`\bigcup\limits_{n=1}^\infty E_n = [0, 1)`, 从而有

   .. math::

      m^* \left( \bigcup_{n=1}^\infty E_n \right) = m^* [0, 1) = 1 < \sum_{n=1}^\infty m^* (E_n) = +\infty.

.. _ex-2-17:

17. 试举例说明，存在可测集列 :math:`\{E_n \subset (a, b)\}_{n \in \mathbb{N}}`，使极限 :math:`\lim\limits_{n \to \infty} m E_n` 存在，
    但 :math:`\lim\limits_{n \to \infty} E_n` 不存在.

.. proof:solution::

   可以借用 :ref:`第一章第 6 题 <ex-1-6>` 中的例子，构造如下的可测集列

   .. math::

      E_n = \left\{ m / n : m \in \mathbb{Z} \right\} \cap (a, b), n \in \mathbb{N},

   那么每个 :math:`E_n` 都是有限集，从而 :math:`m E_n = 0`，于是极限 :math:`\lim\limits_{n \to \infty} m E_n` 存在，值为 :math:`0`，但是

   .. math::

      \varliminf\limits_{n} E_n & = \bigcup\limits\limits_{k=1}^{\infty} \bigcap\limits_{n=k}^{\infty} E_n = \mathbb{Z} \cap (a, b), \\
      \varlimsup\limits_{n} E_n & = \bigcap\limits\limits_{k=1}^{\infty} \bigcup\limits_{n=k}^{\infty} E_n = \mathbb{Q} \cap (a, b),

   两者不相等，所以 :math:`\lim\limits_{n \to \infty} E_n` 不存在.

.. _ex-2-18:

18. 设 :math:`A_1, A_2, \cdots, A_n` 是 :math:`[0, 1]` 中 :math:`n` 个可测集，且满足 :math:`\sum\limits_{k=1}^n m A_k > n - 1`，试证

    .. math::

      m \left( \bigcap_{k=1}^n A_k \right) > 0.

.. proof:proof::

   令 :math:`A = \bigcap\limits_{k=1}^n A_k`, 假设 :math:`m A = 0`, 令基本集 :math:`X = [0, 1]`, 那么有

   .. math::

      1 & = m \left( [0, 1] \setminus A \right) = m \left( [0, 1] \cap \mathscr{C} A \right) \\
      & = m \left( [0, 1] \cap \mathscr{C} \left( \bigcap\limits_{k=1}^n A_k \right) \right)
      = m \left( [0, 1] \cap \left( \bigcup\limits_{k=1}^n \mathscr{C} A_k \right) \right) \\
      & = m \left( \bigcup\limits_{k=1}^n \left( [0, 1] \cap \mathscr{C} A_k \right) \right) = m \left( \bigcup\limits_{k=1}^n \mathscr{C} A_k \right) \\
      & \leqslant \sum \limits_{k=1}^n m \mathscr{C} A_k = \sum \limits_{k=1}^n \left( 1 - m A_k \right) \\
      & = n - \sum \limits_{k=1}^n m A_k < 1,

   矛盾，所以 :math:`m A = m \left( \bigcap\limits_{k=1}^n A_k \right) > 0`.

.. _ex-2-19:

19. 设 :math:`m^* E = q > 0`, 证明对任何数 :math:`c \in (0, q)`, 有子集 :math:`E_0 \subset E` 使得 :math:`m E_0 = c`.

.. proof:proof::

   对任意 :math:`c \in (0, q)`, 考虑函数

   .. math::

      \varphi: ~ \mathbb{R}_{\geqslant 0} \rightarrow \mathbb{R}, ~ \varphi (t) = m^* (E \cap [-t, t]).

   对于 :math:`0 \leqslant t_1 < t_2`, 有

   .. math::

      \varphi (t_1) \leqslant \varphi (t_2) & = m^* (E \cap [-t_2, t_2])\\
      & \leqslant m^* ((E \cap [-t_1, t_1]) \cup [-t_2, -t_1] \cup [t_1, t_2]) \\
      & \leqslant m^* (E \cap [-t_1, t_1]) + 2 (t_2 - t_1) = \varphi (t_1) + 2 (t_2 - t_1),

   从而知 :math:`\varphi` 是一个连续单调增函数.

   我们断言可以取到 :math:`t_1 \in \mathbb{R}_{> 0}` 使得 :math:`\varphi (t_1) > c`.
   这是因为如果这样的 :math:`t_1` 不存在，那么必然有 :math:`m^* E \leqslant c`，这与题设矛盾. 于是由连续函数的介值定理有

   .. math::

      \varphi([0, t_0]) \supset [\varphi(0), \varphi(t_0)] = [0, \varphi(t_0)].

   特别地, 存在 :math:`t_0 \in [0, t_1]` 使得 :math:`\varphi(t_0) = c`. 令 :math:`E_0 = E \cap [-t_0, t_0]`，那么有 :math:`m E_0 = \varphi(t_0) = c`.

   .. note::

      若进一步利用 :ref:`勒贝格外测度的正则性 <reg-outer-measure>`，可以找到 :math:`G_{\delta}`-集 :math:`A_0`, 即 :math:`E_0` 的等测包，使得

      .. math::

         m A_0 = m^* E_0 = c.

.. _ex-2-20:

20. 试作一闭集 :math:`F \subset [0, 1]`，使 :math:`F` 中不含任何开区间，而 :math:`m F = 1/2`.

.. proof:solution::

   按如下方法修改 Cantor 三分集的构造：第一次去掉中间的开区间，长度为 :math:`0 < a \leqslant 1/3`; 第二次从剩下的两个闭区间中去掉中间的开区间，
   长度为 :math:`a^2`; 依此构造，第 :math:`n` 次去掉剩下 :math:`2^{n-1}` 个闭区间中间的开区间，长度为 :math:`a^n`.
   这样，被去掉的开区间的总长度为

   .. math::

      \sum\limits_{n=1}^\infty 2^{n-1} a^n = \dfrac{a}{1 - 2a}.

   以上就是从 :math:`[0, 1]` 中挖去的开集的测度. 那么得到的闭集的测度为

   .. math::

      1 - \dfrac{a}{1 - 2a} = \dfrac{1 - 3a}{1 - 2a},

   且不含任何开区间. 当 :math:`a = 1/4` 时，闭集的测度为 :math:`1/2`. 这样的集合被称为胖 Cantor 集, 或者称为 Smith-Volterra-Cantor 集,
   或者 :math:`\varepsilon`-Cantor 集.

.. _ex-2-21:

21. 试证定义在 :math:`(-\infty, \infty)` 上的单调函数的不连续点集至多可列, 因而为零测度集.

.. proof:proof::

   待写

.. _ex-2-22:

22. 设 :math:`\{ E_n \}` 为可测集列且 :math:`\displaystyle \sum\limits_{n=1}^\infty m E_n < \infty`,
    证明 :math:`\displaystyle m \left( \varlimsup\limits_{n} E_n \right) = 0`.

.. proof:proof::

   由于 :math:`\displaystyle \sum\limits_{n=1}^\infty m E_n < \infty`, 所以对任意 :math:`\varepsilon > 0`, 存在 :math:`N \in \mathbb{N}`,
   使得 :math:`\displaystyle \sum\limits_{n=N}^\infty m E_n < \varepsilon`. 那么有

   .. math::

      m \left( \varlimsup\limits_{n} E_n \right) & = m \left( \bigcap\limits_{n=1}^{\infty} \bigcup\limits_{k=n}^{\infty} E_k \right) \\
      & \leqslant m \left( \bigcup\limits_{k=N}^{\infty} E_k \right) \leqslant \sum\limits_{k=N}^{\infty} m E_k < \varepsilon.

   由于 :math:`\varepsilon` 是任意的，所以有 :math:`m \left( \varlimsup\limits_{n} E_n \right) = 0`.

.. _ex-2-23:

23. 试证: 若存在可测集 :math:`X \supset E`, 满足 :math:`m X < \infty` 与 :math:`m X = m^* E + m^* (X \setminus E)`, 则 :math:`E` 是可测的.

.. proof:proof::

   待写
