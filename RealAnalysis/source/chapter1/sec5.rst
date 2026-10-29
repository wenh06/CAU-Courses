\*§5 集的势·序集
------------------------------

.. _ex-1-28:

28. 对 `本章第13题 <ex-1-13>`_ 中的集 :math:`A` 与所指的置换 :math:`f`, 当 :math:`A` 的势为偶数或者无限时,
    试证映射 :math:`f` 可选其满足 :math:`f(f(x)) = x`, 对一切 :math:`x \in A`. 当 :math:`A` 的势为奇数时, 情况如何?

.. proof:solution::

   待写.

   .. note::
      这样的映射称为对合 (involution).

.. _ex-1-29:

29. 设 :math:`A` 为无限集, 试求它的一切置换所成的集的势.

.. proof:solution::

   记 :math:`S(A)` 为 :math:`A` 的所有置换所成的集.

.. _ex-1-30:

30. 设 :math:`f` 为 :math:`[0,1]` 上的实函数, 存在常数 :math:`C` 使对任一自然数 :math:`n` 以及任意
    :math:`n` 个互不相同的数 :math:`x_1, x_2, \cdots, x_n \in [0,1]` 有

    .. math::
       \lvert f(x_1) + f(x_2) + \cdots + f(x_n) \rvert \leqslant C,

    证明集 :math:`E = \{ x \in [0,1] : f(x) \neq 0 \}` 为至多可列的.

    提示: 对每个正数 :math:`\alpha`, 集 :math:`E_{\alpha} = \{ x : f(x) > \alpha \}` 与
    :math:`E_{-\alpha} = \{ x : f(x) < -\alpha \}` 均为有限集.

.. proof:solution::

   待写.

.. _ex-1-31:

31. 设 :math:`E` 是 :math:`\mathbf{R}` 中可数集, 证明存在一点 :math:`a \in \mathbf{R}` 使
    :math:`E \cap (E + a) = \emptyset`.

    提示: 令 :math:`D = \{ x - y : x, y \in E \}`, :math:`D` 可数, 可取 :math:`a \in \mathbf{R} \setminus D`.

.. proof:solution::

   待写.

.. _ex-1-32:

32. 试证开单位圆不能为互不重叠的圆的并所覆盖.

    提示: 假设可能, 则用以覆盖的圆显然有可列个, 圆与圆之间的切点至多也是可列集. 取一个圆的圆心
    :math:`P` 作为出发点, 作过 :math:`P` 与一切切点的单位圆的弦成一可列集 :math:`S`, 那么必有过
    :math:`P` 的一弦 :math:`l \in S`. 下面用 :math:`l` 代替直径 :math:`(-1, 1)`, 依 [26], p.99 例
    32 讨论即得矛盾.

.. proof:solution::

   待写.

.. _ex-1-33:

33. 设 :math:`\alpha` 为无理数, 证明数集 :math:`M = \{ m\alpha + n : m, n \in \mathbb{Z} \}` 在
    :math:`\mathbf{R}` 中稠密.

    提示: 要点是证明对任一 :math:`k \in \mathbb{N}`, 存在点 :math:`x_k \in M` 使
    :math:`x_k \in (0, 1/k)`; 从而知 :math:`M` 的子集 :math:`\{ n x_k : n \in \mathbb{Z}, k \in \mathbb{N} \}`
    在 :math:`\mathbf{R}` 中稠密. 为此设 :math:`\alpha` 的十进表示为
    :math:`\alpha = [\alpha] + 0.\alpha_1 \alpha_2 \cdots`. 考虑含 :math:`k+1` 个元的集

    .. math::
       A = \{ 0. \alpha_{n} \alpha_{n+1} \cdots : r = 1, 2, \cdots, k+1 \}.

    则 :math:`A \subset M \cap (0, 1)`. 可以断定 :math:`A` 中必有两个不同元 :math:`a_1, a_2` 使
    :math:`0 < a_2 - a_1 < 1/k` 且显然 :math:`a_2 - a_1 \in M`.

.. proof:solution::

   待写.

.. _ex-1-34:

34. 设 :math:`n` 为一自然数, 令 :math:`P_n = \{ k \in \mathbb{N} : k` 为 :math:`n` 的约数 :math:`\}`,
    对任意 :math:`a, b \in P_n`, 约定 :math:`a \leqslant b` 的意义为 :math:`a` 是 :math:`b` 的约数.
    试证 :math:`P_n` 以 ":math:`\leqslant`" 为序成一半序集. 又, 欲使 :math:`P_n` 为全序集, 对
    :math:`n` 应有什么要求?

.. proof:solution::

   待写.

.. _ex-1-35:

35. 称 :math:`X` 的子集所成的类 :math:`\mathscr{A}` 有性质 :math:`(\sigma)`: :math:`X` 非
    :math:`\mathscr{A}` 中有限个元的并. 试证: 若 :math:`\mathscr{A}` 有性质 :math:`(\sigma)`, 则存在
    :math:`X` 的子集的极大类 :math:`\mathscr{B}` 具有性质 :math:`(\sigma)` 且包含 :math:`\mathscr{A}`.
    并证明, 若 :math:`A_1, A_2, \cdots, A_n \subset X`, 且
    :math:`A_1 \cap A_2 \cap \cdots \cap A_n \in \mathscr{B}`, 则必有某个 :math:`A_k \in \mathscr{B}`.

.. proof:solution::

   待写.

.. _ex-1-36:

36. 试以定理 5.5 作为出发点来证明定理 5.6.

.. proof:solution::

   待写.

.. _ex-1-37:

37. 设 :math:`\mathscr{A}` 是由给定的集的子集所成的类: :math:`A \in \mathscr{B}` 是指 :math:`A` 的每一
    有限子集属于 :math:`\mathscr{A}`. 试证 :math:`\mathscr{B}` 含有一极大元.

.. proof:solution::

   待写.

.. _ex-1-38:

38. 试证: 设 :math:`X` 为非空半序集, 若 :math:`X` 的每一非空全序子集有上界, 则 :math:`X` 有极大元
    (佐恩引理的另一形式).

.. proof:solution::

   待写.
