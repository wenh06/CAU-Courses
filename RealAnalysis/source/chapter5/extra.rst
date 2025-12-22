第 5 章 随堂习题
------------------------------------------

.. _ex-5-extra-1:

1. 证明 :math:`L^{\infty}(E)` 是线性空间, 其中 :math:`E` 是 :math:`\mathbb{R}` 中的可测集,

   .. math::
      L^{\infty}(E) := \left\{ f : E \to \mathbb{R} ~:~ f \text{ 在 } E \text{ 上可测且 } \exists M \geqslant 0,
      \text{ 使得 } |f(x)| \leqslant M \text{ 几乎处处成立} \right\}

   是 :math:`E` 上的本性有界函数全体.

.. _ex-5-extra-2:

2. 证明 Hölder 不等式对于 :math:`p = 1, q = \infty` 的情形也成立, 即证明
   对任意 :math:`f \in L^1(E), g \in L^{\infty}(E)`, 有

   .. math::
      \| f g \|_1 \leqslant \| f \|_1 \| g \|_{\infty},

   其中

   .. math::
      \| f \|_1 & := \int_E |f(x)| ~ \mathrm{d} m, \\
      \| g \|_{\infty} & := \inf \left\{ M \geqslant 0 ~:~ |g(x)| \leqslant M
      \text{ 几乎处处成立} \right\} = \inf_{m e = 0} \sup_{x \in E \setminus e} |g(x)|.
