§3 可测集的性质
------------------------------------------

9. 设 :math:`E_1, E_2` 均为有界可测集，试证

.. math::

    m (E_1 \cup E_2) = m E_1 + m E_2 - m (E_1 \cap E_2).

.. proof:proof::

    因为:math:`E_1, E_2` 均为有界可测集，所以 :math:`E_1 \cup E_2, E_1 \setminus E_2, E_2 \setminus E_1, E_1 \cap E_2` 均为有界可测集，且

    .. math::

        E_1 \cup E_2 = (E_1 \setminus E_2) \cup (E_2 \setminus E_1) \cup (E_1 \cap E_2)

    为可测集的不交并，所以根据测度的完全可加性有

    .. math::

        m (E_1 \cup E_2) = m (E_1 \setminus E_2) + m (E_2 \setminus E_1) + m (E_1 \cap E_2).

    另一方面，:math:`E_1` 有互斥分解 :math:`E_1 = (E_1 \setminus E_2) \cup (E_1 \cap E_2)`，所以根据测度的完全可加性有 :math:`m E_1 = m (E_1 \setminus E_2) + m (E_1 \cap E_2)`.
    同理 :math:`m E_2 = m (E_2 \setminus E_1) + m (E_1 \cap E_2)`，所以有

    .. math::

        m (E_1 \cup E_2) = m E_1 + m E_2 - m (E_1 \cap E_2).

10. 设 :math:`E` 是 :math:`\mathbb{R}` 中可测集，:math:`A` 是任意，证明

.. math::

    m^* (E \cap A) + m^* (E \cap A) = m E + m^* A;

:math:`E` 不可测时如何？
