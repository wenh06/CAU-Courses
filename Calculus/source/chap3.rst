第三章  导数与微分
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. contents:: :local:


.. _exercises-chap3:

课后习题解答
====================================

.. _exercises-chap3-sec1:

§3.1 导数的概念
------------------------------------

.. _exercises-chap3-sec1-3:

3. 设 :math:`f(x)` 在 :math:`x_0` 处可导, 求下列极限值.

   (2) :math:`\lim\limits_{\Delta x \to 0} \dfrac{f(x_0 + 2\Delta x) - f(x_0 - \Delta x)}{\Delta x}`.

.. proof:solution::

   由可导的定义, 有

   .. math::
      f(x_0 + 2\Delta x) = f(x_0) + f'(x_0) \cdot 2\Delta x + o(\Delta x), \\
      f(x_0 - \Delta x) = f(x_0) - f'(x_0) \cdot \Delta x + o(\Delta x).

   因此

   .. math::
      & \lim\limits_{\Delta x \to 0} \dfrac{f(x_0 + 2\Delta x) - f(x_0 - \Delta x)}{\Delta x} \\
      = & \lim\limits_{\Delta x \to 0} \dfrac{f(x_0) + f'(x_0) \cdot 2\Delta x + o(\Delta x)
        - \left( f(x_0) - f'(x_0) \cdot \Delta x + o(\Delta x) \right)}{\Delta x} \\
      = & \lim\limits_{\Delta x \to 0} \dfrac{3 f'(x_0) \cdot \Delta x + o(\Delta x)}{\Delta x} = 3 f'(x_0).

.. _exercises-chap3-sec2:

§3.2 求导法则
------------------------------------

.. _exercises-chap3-sec3:

§3.3 高阶导数
------------------------------------

.. _exercises-chap3-sec3-6:

6. 证明: 函数

   .. math::
      y = \dfrac{e^x}{\cos x}

   的第 :math:`n` 阶导数为

   .. math::
      f(x) = \begin{cases}
         e^{-\frac{1}{x^2}}, & x \neq 0, \\
         0, & x = 0,
      \end{cases}

   在 :math:`x = 0` 处 :math:`n` 阶可导且 :math:`f^{(n)}(0) = 0`, 其中 :math:`n` 是任意的正整数.

.. proof:proof::

   由题意可知, 当 :math:`x \neq 0` 时, :math:`f(x) = e^{-\frac{1}{x^2}}` 是一个初等函数, 因此在 :math:`x \neq 0` 时,
   :math:`f(x)` 存在任意阶导数.

   下面用数学归纳法证明 :math:`f(x)` 在 :math:`x = 0` 处 :math:`n` 阶可导且 :math:`f^{(n)}(0) = 0`.

   当 :math:`n = 1` 时, 有

   .. math::
      f'(0) = \lim\limits_{x \to 0} \dfrac{f(x) - f(0)}{x - 0}
      = \lim\limits_{x \to 0} \dfrac{e^{-\frac{1}{x^2}} - 0}{x}
      \xlongequal{t = \frac{1}{x}} \lim\limits_{t \to \infty} \dfrac{t}{e^{t^2}} = 0.

   假设当 :math:`n = k` 时, :math:`f^{(k)}(0) = 0` 成立, 那么当 :math:`n = k + 1` 时, 有

   .. math::
      f^{(k+1)}(0) = \lim\limits_{x \to 0} \dfrac{f^{(k)}(x) - f^{(k)}(0)}{x - 0}
      = \lim\limits_{x \to 0} \dfrac{f^{(k)}(x) - 0}{x}.

   注意到 :math:`f^{(k)}(x)` 是由初等函数通过有限次求导得到的函数, 其中前几项为

   .. math::
      f'(x) & = \dfrac{2}{x^3} e^{-\frac{1}{x^2}}, \\
      f''(x) & = \left( \dfrac{4}{x^6} - \dfrac{6}{x^4} \right) e^{-\frac{1}{x^2}}, \\
      f^{(3)}(x) & = \left( \dfrac{8}{x^9} - \dfrac{36}{x^7} + \dfrac{24}{x^5} \right) e^{-\frac{1}{x^2}}, \\
      \cdots

   因此可以归纳地得到 (用数学归纳法验证), 对任意的正整数 :math:`k`, 有

   .. math::
      f^{(k)}(x) = P_k\left( \dfrac{1}{x} \right) e^{-\frac{1}{x^2}},

   其中 :math:`P_k(t)` 是关于 :math:`t` 的多项式. 因此

   .. math::
      f^{(k+1)}(0) & = \lim\limits_{x \to 0} \dfrac{P_k\left( \dfrac{1}{x} \right) e^{-\frac{1}{x^2}}}{x}
         \xlongequal{t = \frac{1}{x}} \lim\limits_{t \to \infty} t P_k(t) e^{-t^2} \\
      & = \lim\limits_{t \to \infty} \dfrac{t P_k(t)}{e^{t^2}} = 0.

   .. note::
      验证 :math:`f^{(k+1)}(x) = P_{k+1}\left( \dfrac{1}{x} \right) e^{-\frac{1}{x^2}}`:

      .. math::
         f^{(k+1)}(x)
         & = \dfrac{\mathrm{d}}{\mathrm{d} x} \left( P_k\left( \dfrac{1}{x} \right) e^{-\frac{1}{x^2}} \right) \\
         & = P_k'\left( \dfrac{1}{x} \right) \cdot \left( -\dfrac{1}{x^2} \right) e^{-\frac{1}{x^2}}
         + P_k\left( \dfrac{1}{x} \right) \cdot \dfrac{2}{x^3} e^{-\frac{1}{x^2}} \\
         & = \left( -\dfrac{1}{x^2} P_k'\left( \dfrac{1}{x} \right)
            + \dfrac{2}{x^3} P_k\left( \dfrac{1}{x} \right) \right) e^{-\frac{1}{x^2}} \\
         & = P_{k+1}\left( \dfrac{1}{x} \right) e^{-\frac{1}{x^2}}.

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
