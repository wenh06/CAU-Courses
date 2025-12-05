第 4 章 随堂习题
------------------------------------------

.. _ex-4-extra-1:

1. 设 :math:`\{f_n(x)\}` 是可测集 :math:`E` 上的非负可测函数列, 证明对任意 :math:`n \in \mathbb{N}`, 有

   .. math::
      \int_E \left( \inf_{k \geqslant n} f_k(x) \right) ~ \mathrm{d} m
      \leqslant \inf_{k \geqslant n} \int_E f_k(x) ~ \mathrm{d} m.

.. _ex-4-extra-2:

2. 设 :math:`\varphi = \chi_{(\alpha, \beta)}`, :math:`(\alpha, \beta) \subset [-\pi, \pi]`,
   其 Fourier 级数为

   .. math::
      :label: eq:fourier-series-chi

      \frac{A_0}{2} + \sum_{n=1}^{\infty} \left( A_n \cos nx + B_n \sin nx \right),

   其中

   .. math::
      A_n & = \frac{1}{\pi} \int_{-\pi}^{\pi} \varphi(x) \cos nx ~ \mathrm{d} x
            = \frac{1}{\pi} \int_{\alpha}^{\beta} \cos nx ~ \mathrm{d} x
            = \frac{1}{n \pi} \left( \sin n\beta - \sin n\alpha \right), \\
      B_n & = \frac{1}{\pi} \int_{-\pi}^{\pi} \varphi(x) \sin nx ~ \mathrm{d} x
            = \frac{1}{\pi} \int_{\alpha}^{\beta} \sin nx ~ \mathrm{d} x
            = \frac{1}{n \pi} \left( \cos n\alpha - \cos n\beta \right).

   考虑级数 :eq:`eq:fourier-series-chi` 的前 :math:`n` 项部分和

   .. math::
      \varphi_n(x) := \frac{A_0}{2} + \sum_{k=1}^{n} \left( A_k \cos kx + B_k \sin kx \right),

   证明 :math:`\varphi_n(x)` 可由 Dirichlet 核
   :math:`D_n(u) = \frac{\sin \left( n + \frac{1}{2} \right) u}{\sin \frac{u}{2}}` 表示为

   .. math::
      \varphi_n(x) = \frac{1}{\pi} \int_{-\pi}^{\pi} \varphi(x+u) D_n(u) ~ \mathrm{d} u
                   = \frac{1}{\pi} \int_{-\pi}^{\pi} \varphi(x+u)
                     \dfrac{\sin \left( n + \frac{1}{2} \right) u}{\sin \frac{u}{2}} ~ \mathrm{d} u.

.. _ex-4-extra-3:

3. 设 :math:`(X, \mathscr{R}), (Y, \mathscr{S})` 是两个可测空间, :math:`E \subset X \times Y`
   是 :math:`X \times Y` 的一个可测集, :math:`f : E \to \mathbb{R}` 是 :math:`E` 上的可测函数.
   证明 :math:`f` 的每个截口都是可测函数.
