第三章  导数与微分
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. contents:: :local:


.. _exercises-chap3:

课后习题解答
====================================

.. _exercises-chap3-sec1:

§3.1 导数的概念
------------------------------------

.. _exercises-chap3-sec2:

§3.2 求导法则
------------------------------------

.. _exercises-chap3-sec3:

§3.3 高阶导数
------------------------------------

.. _exercises-chap3-sec4:

§3.4 函数的微分
------------------------------------

.. _extra-chap3:

补充内容
====================================

.. _extra-chap3-sec1:

§3.1 导数的概念
------------------------------------

.. _extra-chap3-sec1-topic1:

1. 处处连续, 但处处不可导的函数: Generalized Van der Waerden-Takagi 函数.

   该函数定义如下

   .. math::
      & \varphi(x) = d(x, \mathbb{Z}) = \min_{n \in \mathbb{Z}} |x - n|, \quad x \in \mathbb{R}, \\
      & f(x) = \sum_{n=0}^{\infty} a^n \varphi(b^n x).

   当 :math:`0 < a < 1`, :math:`b \in \mathbb{N}_{\geqslant 2}`, 且 :math:`ab \geqslant 1` 时,
   :math:`f(x)` 是一个在 :math:`\mathbb{R}` 上处处不可导的连续函数.

   那么, 处处可导, 但导函数处处不连续的函数是否存在呢? 答案是不存在.

.. _extra-chap3-sec3:

§3.3 高阶导数
--------------------------------

.. _extra-chap3-sec3-topic1:

1. 莱布尼茨公式 :math:`(uv)^{(n)} = \sum\limits_{k=0}^n C_n^k u^{(k)} v^{(n-k)}` 的证明:

.. proof:proof::

   用数学归纳法证明. 当 :math:`n = 1` 时, :math:`(uv)' = u'v + uv'`, 成立.

   假设当 :math:`n = k` 时, :math:`(uv)^{(k)} = \sum\limits_{i=0}^k C_k^i u^{(i)} v^{(k-i)}` 成立, 那么 :math:`n = k + 1` 时有

   .. math::
      (uv)^{(k + 1)} & = \dfrac{\mathrm{d}}{\mathrm{d} x} \left( \sum\limits_{i=0}^k C_k^i u^{(i)} v^{(k-i)} \right) \\
                     & = \sum\limits_{i=0}^k C_k^i \dfrac{\mathrm{d}}{\mathrm{d} x} \left( u^{(i)} v^{(k-i)} \right) \\
                     & = \sum\limits_{i=0}^k C_k^i \left( u^{(i+1)} v^{(k-i)} + u^{(i)} v^{(k-i+1)} \right) \\
                     & = \sum\limits_{i=0}^k C_k^i u^{(i+1)} v^{(k-i)} + \sum\limits_{i=0}^k C_k^i u^{(i)} v^{(k-i+1)} \\
                     & = \sum\limits_{i=1}^{k+1} C_k^{i-1} u^{(i)} v^{(k-i+1)} + \sum\limits_{i=0}^k C_k^i u^{(i)} v^{(k-i+1)} \\
                     & = u^{(k+1)} v + \sum\limits_{i=1}^k \left( C_k^{i-1} + C_k^i \right) u^{(i)} v^{(k-i+1)} + u v^{(k+1)} \\
                     & = u^{(k+1)} v + \sum\limits_{i=1}^k C_{k+1}^i u^{(i)} v^{(k-i+1)} + u v^{(k+1)} \\
                     & = C_{k+1}^{k+1} u^{(k+1)} v + \sum\limits_{i=0}^k C_{k+1}^i u^{(i)} v^{(k-i+1)} + C_{k+1}^0 u v^{(k+1)} \\
                     & = \sum\limits_{i=0}^{k+1} C_{k+1}^i u^{(i)} v^{((k+1)-i)}

   于是当 :math:`n = k + 1` 时, :math:`(uv)^{(n)} = \sum\limits_{i=0}^n C_n^i u^{(i)} v^{(n-i)}` 成立. 根据数学归纳法原理,
   对于任意的 :math:`n \in \mathbb{N}`, :math:`(uv)^{(n)} = \sum\limits_{i=0}^n C_n^i u^{(i)} v^{(n-i)}` 成立.
