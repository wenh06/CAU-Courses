第九章补充材料
^^^^^^^^^^^^^^^^^^^^^^^^^

.. _cesaro-tauber:

1. 级数的 Cesàro 求和法及 Tauber 型定理:

设 :math:`s_n = \sum\limits_{k=1}^{n} a_k` 是数项级数 :math:`\sum\limits_{n=1}^{\infty} a_n` 的前 :math:`n` 项和,
记 :math:`\sigma_n = \dfrac{1}{n} \sum\limits_{k=1}^{n} s_k`. 若 :math:`\lim\limits_{n\to\infty} \sigma_n = A \in \mathbb{R}`,
则称级数 :math:`\sum\limits_{n=1}^{\infty} a_n` 在 Cesàro 意义下可和, 或者更准确的说是在 :math:`(c, 1)` 的意义下可和,
并记为 :math:`\sum\limits_{n=1}^{\infty} a_n = A~(c, 1)`. 可以归纳地定义 :math:`(c, r)` 的意义下可和的级数.

关于 Cesàro 可和级数, 有如下的一些结论

a. 设级数 :math:`\sum\limits_{n=1}^{\infty} a_n` 在通常意义下收敛到有限实数 :math:`A`,
   即 :math:`\lim\limits_{n \to \infty} s_n = A`, 那么级数 :math:`\sum\limits_{n=1}^{\infty} a_n` 是 :math:`(c, 1)` 可和的,
   而且有 :math:`\sum\limits_{n=1}^{\infty} a_n = A~(c, 1)`.
b. 若级数 :math:`\sum\limits_{n=1}^{\infty} a_n = A~(c, 1)`, 且当 :math:`n\to\infty` 时,
   :math:`a_n = \mathrm{o} \left( \dfrac{1}{n} \right)`, 那么该级数在通常意义下可和,
   且 :math:`\sum\limits_{n=1}^{\infty} a_n = A`.
c. 若级数 :math:`\sum\limits_{n=1}^{\infty} a_n = A~(c, 1)`, 且当 :math:`n\to\infty` 时,
   :math:`a_n = \mathrm{O} \left( \dfrac{1}{n} \right)`, 那么该级数在通常意义下可和,
   且 :math:`\sum\limits_{n=1}^{\infty} a_n = A`.

后两个结论被称作是所谓的 Tauber 型的定理: 对 :math:`(c, r+1)` 可和的级数, 加上一些额外的限制,
能得到它落在子集, :math:`\{ (c, r) \text{可和级数} \}` 中.

.. proof:proof::

   a. 若 :math:`\sum\limits_{n=1}^{\infty} a_n` 在通常意义下收敛到有限实数 :math:`A`, 那么

   .. math::

      A = \lim\limits_{n \to \infty} s_n = \lim\limits_{n \to \infty} \dfrac{n\sigma_n - (n-1)\sigma_{n-1}}{n - (n-1)},

   于是根据 Stolz 公式 (Stolz–Cesàro 定理), 有

   .. math::

      \lim\limits_{n \to \infty} \sigma_n = \lim\limits_{n \to \infty} \dfrac{n\sigma_n}{n}
      = \lim\limits_{n \to \infty} \dfrac{n\sigma_n - (n-1)\sigma_{n-1}}{n - (n-1)} = A.

   这表明了 :math:`\sum\limits_{n=1}^{\infty} a_n = A~(c, 1)`.

   b. 我们考察 :math:`s_n - \sigma_n`, 有

   .. math::

      s_n - \sigma_n & = \sum\limits_{k=1}^n a_k - \sum\limits_{k=1}^n \left( 1 - \dfrac{k-1}{n} \right) a_k \\
      & = \dfrac{\sum\limits_{k=1}^n (k-1)a_k}{n}.

   由于 :math:`n \to \infty` 时有 :math:`a_n = \mathrm{o}\left( \dfrac{1}{n} \right)`,
   那么 :math:`\lim\limits_{n \to \infty} n a_n = 0`, 这也等价于

   .. math::

      \lim_{n \to \infty} (n - 1) a_n = 0.

   于是对 :math:`\dfrac{\sum\limits_{k=1}^n (k-1)a_k}{n}` 使用 Stolz 公式有:

   .. math::

      \lim\limits_{n \to \infty} (s_n - \sigma_n) & = \lim\limits_{n \to \infty} \dfrac{\sum\limits_{k=1}^n (k-1)a_k}{n} \\
      & = \lim\limits_{n \to \infty} \dfrac{\sum\limits_{k=1}^n (k-1)a_k - \sum\limits_{k=1}^{n-1} (k-1)a_k}{n - (n-1)} \\
      & = \lim\limits_{n \to \infty} \dfrac{(n-1)a_n}{1} = 0.

   这表明 :math:`\sum\limits_{n=1}^{\infty} a_n = \lim\limits_{n \to \infty} s_n = \lim\limits_{n \to \infty} \sigma_n = A`.

   c. 除了已知条件:当 :math:`n\to\infty` 时 :math:`a_n = \mathrm{O} \left( \dfrac{1}{n} \right)`,
   即存在正实数 :math:`M`. 使得对任意自然数 :math:`n` 有 :math:`\rvert n a_n \rvert \leqslant M` 之外,
   我们所拥有的条件是 :math:`\sum\limits_{n=1}^{\infty} a_n = A~(c, 1)`, 即 :math:`\lim\limits_{n\to\infty} \sigma_n = A`,
   这等价于 :math:`\forall \varepsilon > 0`, 存在自然数 :math:`N` 使得
   :math:`\forall n > m > N, \lvert \sigma_n - \sigma_m \vert < \varepsilon`.

   之前 b. 的时候, 我们导出了 :math:`s_n` 与 :math:`\sigma_n` 的关系

   .. math::

      s_n = \sigma_n + \sum\limits_{k = 1}^n \dfrac{(k-1)a_k}{n}.

   由于我们只有 :math:`\rvert n a_n \rvert \leqslant M`, 所以 Stolz 公式不能再用了, 得另想办法.

   想法: 将 :math:`s_n - \sigma_n` 与 :math:`\sigma_n - \sigma_m` 联系上, 并用它控制余项的大小. 假设 :math:`n > m`, 那么有

   .. math::

      \sigma_n - \sigma_m & = \dfrac{1}{n} \sum\limits_{k=1}^n s_k - \dfrac{1}{m} \sum\limits_{k=1}^{m} s_k \\
      & = \dfrac{1}{n} \sum\limits_{k=1}^n s_k - \dfrac{1}{m} \sum\limits_{k=1}^{n} s_k + \dfrac{1}{m} \sum\limits_{k=m+1}^{n} s_k \\
      & = \dfrac{m - n}{nm} \sum\limits_{k=1}^n s_k + \dfrac{1}{m} \sum\limits_{k=m+1}^{n} s_k.

   另一方面, 有

   .. math::

      s_n - \sigma_n = s_n - \dfrac{1}{n} \sum\limits_{k = 1}^n s_k.

   两式通分相减, 有

   .. math::

      & (s_n - \sigma_n) - \dfrac{m}{n - m}(\sigma_n - \sigma_m) \\
      & = s_n - \cancel{\dfrac{1}{n} \sum\limits_{k = 1}^n s_k} + \cancel{\dfrac{1}{n} \sum\limits_{k=1}^n s_k}
         - \dfrac{1}{n-m} \sum\limits_{k=m+1}^{n} s_k \\
      & = s_n - \dfrac{1}{n-m} \sum\limits_{k=m+1}^{n} s_k = \dfrac{1}{n-m} \sum\limits_{k=m+1}^{n} (s_n - s_k).

   整理一下, 有

   .. math::

      s_n - \sigma_n = \underbrace{\dfrac{m}{n - m}(\sigma_n - \sigma_m)}_{\text{第一部分}} +
                       \underbrace{\dfrac{1}{n-m} \sum\limits_{k=m+1}^{n} (s_n - s_k)}_{\text{第二部分}}.

   对于第二部分 :math:`\dfrac{1}{n-m} \sum\limits_{k=m+1}^{n} (s_n - s_k)` 和式中的每一项, 我们有估计

   .. math::

      \begin{multline*}
      \lvert s_n - s_k \rvert = \lvert a_{k+1} + \cdots + a_n \rvert \\
      \leqslant \dfrac{M}{k+1} + \cdots \dfrac{M}{n} \leqslant \dfrac{(n-k)M}{k+1} \leqslant \dfrac{(n-m-1)M}{m+1}
      \end{multline*}

   于是

   .. math::

      \left\lvert \dfrac{1}{n-m} \sum\limits_{k=m+1}^{n} (s_n - s_k) \right\rvert
      \leqslant \dfrac{1}{n-m} (n-m) \dfrac{n-m-1}{m+1} M < \dfrac{n-m}{m} M.

   我们希望有 :math:`\dfrac{n-m}{m} < \dfrac{\varepsilon}{2M}`, 即 :math:`m > \dfrac{n}{1 + \frac{\varepsilon}{2M}}`.
   取 :math:`n` 足够大, 使得 :math:`n - \dfrac{n}{1 + \frac{\varepsilon}{2M}} > 2`, 或者等价地,
   取 :math:`n > \dfrac{2(2M + \varepsilon)}{\varepsilon}`, 即可确保能取到整数

   .. math::

      m \in \left[ \dfrac{n}{1 + \frac{\varepsilon}{2M}}, n \right],

   即有 :math:`\lvert \text{第二部分} \rvert < \dfrac{\varepsilon}{2}`.

   对于 :math:`\text{第一部分} = \dfrac{m}{n - m}(\sigma_n - \sigma_m)`,
   由于已有 :math:`\dfrac{n-m}{m} < \dfrac{\varepsilon}{2M}`, 即 :math:`\dfrac{m}{n-m} > \dfrac{2M}{\varepsilon}`,
   进一步要求 :math:`\dfrac{2M}{\varepsilon} < \dfrac{m}{n-m} < \dfrac{4M}{\varepsilon}`, 即
   :math:`m < \dfrac{n}{1 + \frac{\varepsilon}{4M}}`. 这样的整数 :math:`m` 总是可以取到的,
   只要保证 :math:`\dfrac{n}{1 + \frac{\varepsilon}{4M}} - \dfrac{n}{1 + \frac{\varepsilon}{2M}} > 2` 即可,
   即 :math:`n > \dfrac{8M}{\varepsilon}\left(1 + \frac{\varepsilon}{4M}\right)\left(1 + \frac{\varepsilon}{2M}\right)`.
   于是

   .. math::

      \lvert \text{第一部分} \rvert = \left\lvert \dfrac{m}{n - m}(\sigma_n - \sigma_m) \right\rvert
      \leqslant \dfrac{4M}{\varepsilon} \left\lvert \sigma_n - \sigma_m \right\rvert.

   若取 :math:`N` 充分大, 使得 :math:`\forall n > m > N` 都有
   :math:`\left\lvert \sigma_n - \sigma_m \right\rvert < \dfrac{\varepsilon^2}{8M}`, 那么

   .. math::

      \left\lvert s_n - \sigma_n \right\rvert \leqslant \lvert \text{第一部分} \rvert + \lvert \text{第二部分} \rvert < \varepsilon.

   注意我们的取法: :math:`N` 充分大
   (大于 :math:`\dfrac{8M}{\varepsilon}\left(1 + \frac{\varepsilon}{4M}\right)\left(1 + \frac{\varepsilon}{2M}\right)`),
   :math:`m, n` 满足关系:

   .. math::

      \dfrac{n}{1 + \frac{\varepsilon}{2M}} < m < \dfrac{n}{1 + \frac{\varepsilon}{4M}} < n.
