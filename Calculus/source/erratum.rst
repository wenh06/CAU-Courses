.. role:: strike

课本勘误
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _erratum_1:

1. 第 7 页, 1.3.1.5 三角函数, "余切函数 :math:`y = \cot x` ... 无界的 :strike:`偶函数` 奇函数"

.. _erratum_2:

2. 第 43 页, 习题 4.2 第 4 题, "... :math:`x_2 = \sqrt{ a + \cancel{\sqrt{x_1}} x_1}`, ...,
   :math:`x_{n+1} = \sqrt{ a + \cancel{\sqrt{x_n}} x_n}`, ..."

.. _erratum_3:

3. 第 51 页, 习题 2.5 第 2 题 第 (5) 小题, :math:`\lim\limits_{x \to +\infty} x[\ln(x + 1) - x]`
   应改为 :math:`\lim\limits_{x \to +\infty} x[\ln(x + 1) - \ln x]`, 见 :ref:`解答 <ex-chap2-sec5-ex2>`.

.. _erratum_4:

4. 第 94 页, 最后一行的公式 :

   .. math::

      f'(\xi) = \dfrac{1}{\xi} = \dfrac{f(h) - f(0)}{h - 0} = \dfrac{\ln(1+h)}{h}

   应改为 :

   .. math::

      f'(\xi) = \dfrac{1}{\xi} = \dfrac{f(1+h) - f(1)}{(1+h) - 1} = \dfrac{\ln(1+h)}{h}

.. _erratum_5:

5. 第 192 页, 原算式:

   .. math::

      \int_{0}^{+\infty} \dfrac{\ln x}{1 + x^2} ~ \mathrm{d}x
      & = \int_{0}^{1} \dfrac{\ln x}{1 + x^2} ~ \mathrm{d}x + \int_{1}^{+\infty} \dfrac{\ln x}{1 + x^2} ~ \mathrm{d}x \\
      & = \cdots = \int_{0}^{1} \dfrac{\ln x}{1 + x^2} ~ \mathrm{d}x - \int_{0}^{1} \dfrac{\ln t}{1 + t^2} ~ \mathrm{d}t = 0.

   实际是, 最后一个等号之前, 应先验证 :math:`\displaystyle \int_{0}^{1} \dfrac{\ln x}{1 + x^2} ~ \mathrm{d}x` 收敛,
   然后才能得出结果为 0. 等价地, 我们证明 :math:`\displaystyle \int_{1}^{+\infty} \dfrac{\ln x}{1 + x^2} ~ \mathrm{d}x` 收敛.
   为此, 我们利用 **非负函数广义积分的比较判别法**. 注意到当 :math:`x \to +\infty` 时, 有:

   .. math::

      \lim_{x \to +\infty} \dfrac{\ln x}{1 + x^2} \Big/ \dfrac{1}{x^{3/2}}
      = \lim_{x \to +\infty} \dfrac{\ln x}{x^{1/2}} = \lim_{x \to +\infty} \dfrac{1/x}{(1/2)x^{-1/2}}
      = \lim_{x \to +\infty} \dfrac{2}{x^{1/2}} = 0.

   由于 :math:`\displaystyle \int_{1}^{+\infty} \dfrac{1}{x^{3/2}} ~ \mathrm{d}x` 收敛, 故由比较判别法可知
   :math:`\displaystyle \int_{1}^{+\infty} \dfrac{\ln x}{1 + x^2} ~ \mathrm{d}x` 收敛. 因此, 原式成立.
