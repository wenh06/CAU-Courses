§1-4 勒贝格积分的引入、性质、积分序列的极限、与黎曼积分的关系
-------------------------------------------------------------------------------------

.. _ex-4-1:

1. 设 :math:`f(x), g(x)` 都是 :math:`E` 上可测函数, :math:`g \in L_E`, 且在 :math:`E` 上几乎处处成立 :math:`f(x) \leqslant g(x)`.
   问 :math:`f` 是否可积?

.. proof:solution::

   不一定. 例如 :math:`E = [0, 1]`, :math:`f(x) = -\dfrac{1}{x}`, :math:`g(x) = 1`, 那么 :math:`f(x) \leqslant g(x)` 处处成立,
   但是 :math:`f` 在 :math:`E` 上不可积.

   这是因为假设 :math:`f` 可积, 那么 :math:`\lvert f(x) \rvert = \dfrac{1}{x}` 也在 :math:`E` 上可积.
   考虑 :math:`E = [0, 1]` 上的非负渐升函数列 :math:`\{ g_n = \lvert f \rvert \cdot \chi_{[1/n, 1]} \}`, 那么由 Levi 定理知

   .. math::

      \int_0^1 \lvert f \rvert ~ \mathrm{d} m
      & = \lim_{n \to \infty} \int_0^1 g_n ~ \mathrm{d} m = \lim_{n \to \infty} \int_{1/n}^1 \lvert f \rvert ~ \mathrm{d} m \\
      & = \lim_{n \to \infty} \int_{1/n}^1 \dfrac{1}{x} ~ \mathrm{d} x = \lim_{n \to \infty} \left( \ln x \right|_{1/n}^1) = \infty,

   这与 :math:`\lvert f \rvert` 在 :math:`E` 上可积矛盾, 所以 :math:`f` 不可积.

   更简单的例子可取 :math:`f \equiv - \infty`.

   .. note::

      这题主要是没有限定非负函数的条件, 所以可以取到 :math:`f` 不可积的情况.

.. _ex-4-2:

2. 设 :math:`f` 于 :math:`E` 上可积, 令 :math:`E_n = E( \lvert f \rvert \geqslant n)`, 证明 :math:`\displaystyle \lim_n m E_n = 0`.

.. proof:proof::

   :math:`f` 于 :math:`E` 上可积, 那么 :math:`\lvert f \rvert` 于 :math:`E` 上可积, 即 :math:`\displaystyle \int_E \lvert f \rvert ~ \mathrm{d} m < \infty`.
   由于 :math:`\{E_n\}_{n \in \mathbb{N}}` 是渐缩列, 故数列 :math:`\{ m E_n \}_{n \in \mathbb{N}}` 是非负单调不增数列,
   所以 :math:`\displaystyle \lim_{n \to \infty} m E_n` 极限存在, 设为 :math:`\alpha`. 假设 :math:`\alpha > 0`, 那么存在 :math:`N \in \mathbb{N}`,
   使得当 :math:`n \geqslant N` 时, 有 :math:`m E_n \geqslant \dfrac{\alpha}{2}`, 于是

   .. math::

      \int_E \lvert f \rvert ~ \mathrm{d} m \geqslant \int_{E_n} \lvert f \rvert ~ \mathrm{d} m \geqslant n \cdot m E_n \geqslant \frac{n \alpha}{2}

   对任意 :math:`n \geqslant N` 成立, 这与 :math:`\displaystyle \int_E \lvert f \rvert ~ \mathrm{d} m < \infty` 矛盾, 所以 :math:`\alpha = 0`.

.. _ex-4-3:

3. 设函数 :math:`f` 在 Cantor 三分集 :math:`P_0` 上定义为零, 而在 :math:`P_0` 的补集中长为 :math:`\dfrac{1}{3^n}` 的构成区间上定义为 :math:`n`,
   :math:`n \in \mathbb{N}.` 试证 :math:`f \in L`, 并求积分值.

.. proof:proof::

   :math:`P_0` 在 :math:`E = [0, 1]` 中的补集 :math:`G_0` 的长为 :math:`\dfrac{1}{3^n}` 的构成区间共有 :math:`2^{n - 1}` 个,
   记为 :math:`I_{n, k}, k = 1, 2, \dots, 2^{n - 1}`. 于是

   .. math::

      f = \sum_{n = 1}^\infty \sum_{k = 1}^{2^{n - 1}} n \cdot \chi_{I_{n, k}}.

   :math:`f` 以及 :math:`\chi_{I_{n, k}}` 都是非负可测函数, 所以由逐项积分定理可得

   .. math::

      \int_E f ~ \mathrm{d} m = \sum_{n = 1}^\infty \sum_{k = 1}^{2^{n - 1}} n \cdot m I_{n, k}
      = \sum_{n = 1}^\infty \dfrac{n \cdot 2^{n - 1}}{3^n} = \dfrac{1}{2} \sum_{n = 1}^\infty n \cdot \left( \dfrac{2}{3} \right)^n.

   以上级数是收敛的, 所以 :math:`f \in L_E`. 记 :math:`I = \displaystyle \int_E f ~ \mathrm{d} m, a = \dfrac{2}{3}`, 那么

   .. math::

      I - a I = \dfrac{1}{2} \sum_{n = 1}^\infty a^n = \dfrac{a}{2(1 - a)},

   因此 :math:`I = \dfrac{a}{2(1 - a)^2} = 3`.

.. _ex-4-4:

4. 设 :math:`f(x) \geqslant 0` 为可测函数, 令

   .. math::

      \{f(x)\}_n = \begin{cases}
         f(x), & \text{ 若 } f(x) \leqslant n, \\
         0, & \text{ 若 } f(x) > n,
      \end{cases}

   证明当 :math:`f(x)` 几乎处处有限时, 有

   .. math::

      \lim_{n \to \infty} \int_E \{f(x)\}_n ~ \mathrm{d} m = \int_E f(x) ~ \mathrm{d} m.

.. proof:proof::

   记 :math:`E^* = E(\lvert f \rvert < \infty)`, 由于 :math:`f(x)` 几乎处处有限, 所以 :math:`m E^* = m E`.
   那么在 :math:`E^*` 上, 有 :math:`\{f(x)\}_n`, :math:`n \in \mathbb{N}`, 构成了非负渐升函数列, 且对任意 :math:`x \in E^*` 有
   :math:`\displaystyle \lim_{n \to \infty} \{f(x)\}_n = f(x)`. 由 Levi 定理知

   .. math::

      \lim_{n \to \infty} \int_{E^*} \{f(x)\}_n ~ \mathrm{d} m = \int_{E^*} f(x) ~ \mathrm{d} m.

   由于 :math:`E \setminus E^*` 是零测集, 所以 :math:`\displaystyle \int_{E^*} \{f(x)\}_n ~ \mathrm{d} m = \int_{E} \{f(x)\}_n ~ \mathrm{d} m`,
   :math:`\displaystyle \int_{E^*} f(x) ~ \mathrm{d} m = \int_{E} f(x) ~ \mathrm{d} m`, 于是

   .. math::

      \lim_{n \to \infty} \int_E \{f(x)\}_n ~ \mathrm{d} m = \int_E f(x) ~ \mathrm{d} m.

.. _ex-4-5:

5. 设由 :math:`[0, 1]` 中取 :math:`n` 个可测子集 :math:`E_1, E_2, \dots, E_n`. 假定 :math:`[0, 1]` 中任一点至少属于这 :math:`n` 个集合中的 :math:`p` 个,
   试证这 :math:`n` 个子集中必有一集, 它的测度不小于 :math:`\dfrac{p}{n}`.

.. proof:proof::

   由于 :math:`[0, 1]` 中任一点至少属于 :math:`E_1, E_2, \dots, E_n` 的 :math:`p` 个, 所以

   .. math::

      \sum_{k = 1}^n \chi_{E_k} (x) \geqslant p, \quad \forall ~ x \in [0, 1],

   于是有

   .. math::

      \sum_{k = 1}^n m E_k = \sum_{k = 1}^n \int_{[0, 1]} \chi_{E_k} (x) ~ \mathrm{d} m
      = \int_{[0, 1]} \sum_{k = 1}^n \chi_{E_k} (x) ~ \mathrm{d} m \geqslant \int_{[0, 1]} p ~ \mathrm{d} m = p.

   所以上式左端的和至少有一项不小于 :math:`\dfrac{p}{n}`, 也即对应的集合的测度不小于 :math:`\dfrac{p}{n}`.

.. _ex-4-6:

6. 设 :math:`m E > 0`, 又设 :math:`E` 上可积函数 :math:`f, g` 满足 :math:`f < g`, 试证

   .. math::

      \int_E f ~ \mathrm{d} m < \int_E g ~ \mathrm{d} m.

.. proof:proof::

   由于可积函数 :math:`f, g` 满足 :math:`f < g`, 所以 :math:`\lvert g - f \rvert = g - f`. 假设 :math:`\displaystyle \int_E f ~ \mathrm{d} m = \int_E g ~ \mathrm{d} m`, 那么

   .. math::

      \int_E \lvert g - f \rvert ~ \mathrm{d} m = \int_E (g - f) ~ \mathrm{d} m = \int_E g ~ \mathrm{d} m - \int_E f ~ \mathrm{d} m = 0.

   由唯一性定理可知 :math:`g - f \sim 0`, 也即 :math:`g(x) = f(x)` a.e. :math:`x \in E`. 这意味着

   .. math::

      0 = m E (g \neq f) = m E,

   这与 :math:`m E > 0` 矛盾, 所以必有 :math:`\displaystyle \int_E f ~ \mathrm{d} m < \int_E g ~ \mathrm{d} m`.

.. _ex-4-7:

7. 设 :math:`f` 为 :math:`E` 上可积函数, 如果对任何有界可测函数 :math:`\varphi`, 都有

   .. math::

      \int_E f \varphi ~ \mathrm{d} m = 0,

   证明 :math:`f \sim 0`.

.. proof:proof::

   :math:`\forall ~ n \in \mathbb{N}`, 令 :math:`E_n = E( \lvert f \rvert \geqslant n)`, 那么 :math:`\displaystyle \lim_{n \to \infty} m E_n = 0`. 令

   .. math::

      \varphi_n (x) = f(x) \cdot \chi_{E \setminus E_n} = \begin{cases}
         f(x), & x \in E \setminus E_n, \\
         0, & x \in E_n,
      \end{cases}

   那么 :math:`\varphi_n` 是 :math:`E` 上有界可测函数 (:math:`\lvert \varphi_n \rvert \leqslant n`), 且依题意有

   .. math::

      0 = \int_E f \varphi_n ~ \mathrm{d} m = \int_{E \setminus E_n} f^2 ~ \mathrm{d} m.

   那么有 :math:`f(x) = 0` a.e. :math:`x \in E \setminus E_n`, 进而有

   .. math::

      f(x) = 0, \quad a.e. ~ x \in \bigcup_{n = 1}^\infty (E \setminus E_n) = E \setminus \bigcap_{n = 1}^\infty E_n.

   由于 :math:`\displaystyle \lim_{n \to \infty} m E_n = 0`, 所以 :math:`\displaystyle m \left( \bigcap_{n = 1}^\infty E_n \right) = 0`,
   那么 :math:`f(x) = 0` a.e. :math:`x \in E`.

.. _ex-4-8:

8. Levi 定理中去掉函数列的非负性假定, 结论是否成立?

.. proof:solution::

   一般不成立. 例如当 :math:`f_n` 的正部与负部积分都是 :math:`\infty` 时, :math:`f_n` 的积分不存在.
   即使当 :math:`f_n` 的积分有定义时, Levi 定理也不一定成立, 例如 :math:`E = [0, \infty)`, :math:`f_n(x) = - \chi_{[n, \infty)}`,
   则 :math:`f_n` 的积分为 :math:`- \infty`, 但是 :math:`f_n` 逐点收敛于 :math:`f = 0`, :math:`f` 的积分为 :math:`0`, 此时

   .. math::

      \int_E f ~ \mathrm{d} m = 0 \neq - \infty = \lim_{n \to \infty} \int_E f_n ~ \mathrm{d} m.

   如果加上 :math:`f_n` 的积分都有定义, 且 :math:`\displaystyle \int_E f_1 ~ \mathrm{d} m > - \infty` 这个条件, Levi 定理就成立了.

.. _ex-4-9:

9. 证明下列等式

   .. math::

      \int_{(0, 1)} \dfrac{x^p}{1 - x} \ln \dfrac{1}{x} ~ \mathrm{d} m = \sum_{n = 1}^\infty \dfrac{1}{(p + n)^2}, \quad p > -1.

.. proof:proof::

   在 :math:`(0, 1)` 上有 :math:`\displaystyle \dfrac{x^p}{1 - x} = \sum_{n = 1}^\infty x^{p + n - 1}`, 于是

   .. math::

      \int_{(0, 1)} \dfrac{x^p}{1 - x} \ln \dfrac{1}{x} ~ \mathrm{d} m
      = \int_{(0, 1)} \sum_{n = 1}^\infty \left( - x^{p + n - 1} \ln x \right) ~ \mathrm{d} m.

   由非负可测函数列的逐项积分定理知

   .. math::
      :label: ex-4-9-eq-1

      \int_{(0, 1)} \dfrac{x^p}{1 - x} \ln \dfrac{1}{x} ~ \mathrm{d} m
      = \sum_{n = 1}^\infty \int_{(0, 1)} - x^{p + n - 1} \ln x ~ \mathrm{d} m.

   对于非负可测函数 :math:`f_n(x) := - x^{p + n - 1} \ln x`, 若其在 :math:`(0, 1)` 上的 (反常) 积分收敛, 那么它在 :math:`(0, 1)` 上是勒贝格可积的,
   且勒贝格积分值等于反常积分值. 由于 :math:`p > -1`, 于是

   .. math::
      :label: ex-4-9-eq-2

      \int_0^1 f_n(x) ~ \mathrm{d} x & = - \int_0^1 x^{p + n - 1} \ln x ~ \mathrm{d} x = - \dfrac{1}{p + n} \int_0^1 \ln x ~ \mathrm{d} x^{p + n} \\
      & = - \dfrac{1}{p + n} \left( x^{p + n} \cdot \ln x \bigg|_0^1 - \int_0^1 x^{p + n} ~ \mathrm{d} \ln x \right) \\
      & = - \dfrac{1}{p + n} \left( 0 - 0 - \int_0^1 x^{p + n - 1} ~ \mathrm{d} x \right) = \dfrac{1}{(p + n)^2}.

   将 :eq:`ex-4-9-eq-2` 代入 :eq:`ex-4-9-eq-1` 中, 即有

   .. math::

      \int_{(0, 1)} \dfrac{x^p}{1 - x} \ln \dfrac{1}{x} ~ \mathrm{d} m = \sum_{n = 1}^\infty \int_{(0, 1)} f_n ~ \mathrm{d} m
      = \sum_{n = 1}^\infty \dfrac{1}{(p + n)^2}.

.. _ex-4-10:

10. 设 :math:`f(x)` 是 :math:`\mathbb{R}` 上可积函数, :math:`f(0) = 0` 且 :math:`f(x)` 在 :math:`x = 0` 处可微,
    试证函数 :math:`f(x) / x \in L(\mathbb{R})`.

.. proof:proof::

   由于 :math:`f(0) = 0` 且 :math:`f(x)` 在 :math:`x = 0` 处可微, 即存在实数 :math:`A \in \mathbb{R}`,
   使得 :math:`\displaystyle \lim_{x \to 0} \dfrac{f(x) - f(0)}{x} = A`. 那么对任意 :math:`\varepsilon > 0`, 存在 :math:`\delta > 0`,
   使得当 :math:`0 < \lvert x \rvert < \delta` 时有 :math:`\lvert f(x) / x - A \rvert < \varepsilon`,
   也即 :math:`\lvert f(x) / x \rvert \leqslant \lvert A \rvert + \varepsilon`, 这表明

   .. math::

      \int_{(-\delta, \delta)} \lvert f(x) / x \rvert ~ \mathrm{d} m < \infty.

   另一方面, 由于 :math:`f(x)` 是 :math:`\mathbb{R}` 上可积函数, 所以 :math:`\lvert f(x) \rvert` 也是 :math:`\mathbb{R}` 上可积函数.
   在 :math:`(-\infty, -\delta)` 上以及在 :math:`(\delta, +\infty)` 上, 有 :math:`\lvert f(x) / x \rvert \leqslant \lvert f(x) \rvert / \delta`,
   于是

   .. math::

      \int_{(-\infty, -\delta)} \lvert f(x) / x \rvert ~ \mathrm{d} m + \int_{(\delta, +\infty)} \lvert f(x) / x \rvert ~ \mathrm{d} m
      \leqslant \dfrac{1}{\delta} \int_{(-\infty, -\delta)} \lvert f(x) \rvert ~ \mathrm{d} m
          + \dfrac{1}{\delta} \int_{(\delta, +\infty)} \lvert f(x) \rvert ~ \mathrm{d} m
      < \infty.

   综上有

   .. math::

      \int_{\mathbb{R}} \lvert f(x) / x \rvert ~ \mathrm{d} m
      = \int_{(-\infty, -\delta)} \lvert f(x) / x \rvert ~ \mathrm{d} m
          + \int_{(-\delta, \delta)} \lvert f(x) / x \rvert ~ \mathrm{d} m
          + \int_{(\delta, +\infty)} \lvert f(x) / x \rvert ~ \mathrm{d} m
      < \infty,

   也即 :math:`\lvert f(x) / x \rvert \in L(\mathbb{R})`, 从而 :math:`f(x) / x \in L(\mathbb{R})`.

.. _ex-4-11:

11. 设 :math:`f(x)` 为 :math:`[0, 1]` 上有限可测函数, 试证
    :math:`\displaystyle \lim_{n \to \infty} \int_{(0, 1)} \lvert \cos (\pi f(x)) \rvert^n ~ \mathrm{d} x` 存在为有限, 并求此极限值.

.. proof:proof::

   令 :math:`f_n(x) = \lvert \cos (\pi f(x)) \rvert^n`, 那么对任意 :math:`x \in (0, 1)` 有

   .. math::

      \lim_{n \to \infty} f_n(x) = \begin{cases}
         1, & f(x) \in \mathbb{Z}, \\
         0, & f(x) \not\in \mathbb{Z}
      \end{cases} =: g(x).

   记 :math:`I = [0, 1]`, :math:`E = I(f \in \mathbb{Z})`, 那么 :math:`E` 是可测集, 且 :math:`g = \chi_E`. 由有界收敛定理有

   .. math::

      \lim_{n \to \infty} \int_{(0, 1)} f_n ~ \mathrm{d} m
      & = \int_{(0, 1)} \lim_{n \to \infty} f_n ~ \mathrm{d} m = \int_{(0, 1)} g ~ \mathrm{d} m \\
      & = \int_{(0, 1)} \chi_E ~ \mathrm{d} m = m E = m I(f \in \mathbb{Z}).

.. _ex-4-12:

12. 证明极限 :math:`\displaystyle \lim_{n \to \infty} \int_{(-n, n)} \left( 1 + \dfrac{x}{n} \right)^n e^{-x^2} ~ \mathrm{d} m` 存在，
    并求其值.

.. proof:proof::

   令 :math:`f_n(x) = \left( 1 + \dfrac{x}{n} \right)^n e^{-x^2} \chi_{(-n, n)}`, 那么有

   .. math::

      \lvert f_n(x) \rvert \leqslant \left( 1 + \dfrac{\lvert x \rvert}{n} \right)^n e^{-x^2} \leqslant e^{-x^2 + \lvert x \rvert} =: g(x).

   令 :math:`g_n(x) = g \cdot \chi_{[-n, n]}`, 那么 :math:`\{ g_n \}` 构成了 :math:`\mathbb{R}` 上的非负渐升函数列, 由 Levi 定理知

   .. math::

      \int_{\mathbb{R}} g ~ \mathrm{d} m
      & = \lim_{n \to \infty} \int_{\mathbb{R}} g_n ~ \mathrm{d} m = \lim_{n \to \infty} \int_{(-n, n)} g ~ \mathrm{d} m \\
      & = \lim_{n \to \infty} (R) \int_{-n}^n g ~ \mathrm{d} m = \int_{-\infty}^{+\infty} g(x) ~ \mathrm{d} x \\
      & = \int_{-\infty}^{+\infty} e^{-x^2 + \lvert x \rvert} ~ \mathrm{d} x
        = \int_{-\infty}^{+\infty} e^{-\left( \lvert x \rvert - \frac{1}{2} \right)^2 + \frac{1}{4}} ~ \mathrm{d} x < \infty.

   上式中的 :math:`\displaystyle \int_{-\infty}^{+\infty} g(x) ~ \mathrm{d} x` 指的是广义积分.
   故 :math:`g` 在 :math:`(-\infty, \infty)` 上是勒贝格可积的, 从而由控制收敛定理可得

   .. math::

      \lim_{n \to \infty} \int_{(-n, n)} \left( 1 + \dfrac{x}{n} \right)^n e^{-x^2} ~ \mathrm{d} m
      = \int_{\mathbb{R}} \lim_{n \to \infty} f_n ~ \mathrm{d} m = \int_{\mathbb{R}} e^{-x^2 + x} ~ \mathrm{d} m.

   令 :math:`f(x) = e^{-x^2 + x}`. 由于 :math:`0 < f \leqslant g`, 所以 :math:`f` 也是 :math:`(-\infty, \infty)` 上的勒贝格可积函数.
   考虑 :math:`f \chi_{[-n, n]}`, 那么 :math:`f \chi_{[-n, n]}` 是 :math:`\mathbb{R}` 上的非负渐升函数列, 由 Levi 定理知

   .. math::

      \int_{\mathbb{R}} f ~ \mathrm{d} m
      & = \lim_{n \to \infty} \int_{\mathbb{R}} f \chi_{[-n, n]} ~ \mathrm{d} m = \lim_{n \to \infty} \int_{-n}^n f ~ \mathrm{d} m \\
      & = \lim_{n \to \infty} (R) \int_{-n}^n f(x) ~ \mathrm{d} x = \int_{-\infty}^{+\infty} f(x) ~ \mathrm{d} x
        = \int_{-\infty}^{+\infty} e^{-x^2 + x} ~ \mathrm{d} x \\
      & = \int_{-\infty}^{+\infty} e^{-\left( x - \frac{1}{2} \right)^2 + \frac{1}{4}} ~ \mathrm{d} x
        = \pi^{1/2} e^{1/4}.

.. _ex-4-13:

13. 试证: 若 :math:`f \in L(\mathbb{R})`, 则对任意的常数 :math:`\alpha > 0` 有
    :math:`\displaystyle n^{-\alpha} f(nx) \xrightarrow{\text{~a.e.~}} 0 ~ (n \to \infty)`.

.. proof:proof::

   由于 :math:`f \in L(\mathbb{R})` 当且仅当 :math:`\lvert f \rvert \in L(\mathbb{R})`,
   并且 :math:`\displaystyle n^{-\alpha} f(nx) \xrightarrow{\text{~a.e.~}} 0 ~ (n \to \infty)` 等价于
   :math:`\displaystyle n^{-\alpha} \lvert f(nx) \rvert \xrightarrow{\text{~a.e.~}} 0 ~ (n \to \infty)`. 所以不妨设 :math:`f \geqslant 0`.

   考虑 :math:`\mathbb{R} \to \mathbb{R}` 的非奇异线性变换 :math:`x \mapsto y = nx`, 那么 :math:`\mathrm{d} y = n \mathrm{d} x`
   (参见 :ref:`第二章第 32 题 <ex-2-32>`), 于是对于 :math:`\displaystyle \int_{\mathbb{R}} n^{-\alpha} f(nx) ~ \mathrm{d} x` 有

   .. math::

      \int_{\mathbb{R}} n^{-\alpha} f(nx) ~ \mathrm{d} x = n^{-\alpha} \int_{\mathbb{R}} f(y) ~ \dfrac{1}{n} ~ \mathrm{d} y
      = \dfrac{1}{n^{1 + \alpha}} \int_{\mathbb{R}} f ~ \mathrm{d} m.

   对上式关于 :math:`n` 求和, 有

   .. math::

      \sum_{n = 1}^\infty \int_{\mathbb{R}} n^{-\alpha} f(nx) ~ \mathrm{d} x
      = \sum_{n = 1}^\infty \dfrac{1}{n^{1 + \alpha}} \int_{\mathbb{R}} f ~ \mathrm{d} m
      = \left( \int_{\mathbb{R}} f ~ \mathrm{d} m \right) \sum_{n = 1}^\infty \dfrac{1}{n^{1 + \alpha}}.

   由于 :math:`\alpha > 0`, 上述等式右边的级数收敛, 记这个级数的和为 :math:`C`. 对于上述等式左边的级数, 由逐项积分定理知

   .. math::

      C = \sum_{n = 1}^\infty \int_{\mathbb{R}} n^{-\alpha} f(nx) ~ \mathrm{d} x
      = \int_{\mathbb{R}} \sum_{n = 1}^\infty n^{-\alpha} f(nx) ~ \mathrm{d} x.

   于是, :math:`\displaystyle g(x) := \sum_{n = 1}^\infty n^{-\alpha} f(nx)` 是 :math:`\mathbb{R}` 上的非负可积函数,
   从而几乎处处有限, 在这些点上, 非负项级数 :math:`\displaystyle \sum_{n = 1}^\infty n^{-\alpha} f(nx)` 的通项必须趋于零,
   即 :math:`\displaystyle n^{-\alpha} f(nx) \xrightarrow{\text{~a.e.~}} 0 ~ (n \to \infty)`.

   .. note::

      可以用 Fatou 引理来证明稍弱一些的结论.

      记 :math:`g_n = n^{-\alpha} f(nx)`, :math:`\displaystyle g = \varliminf_{n \to \infty} g_n`,
      那么 :math:`g, g_n` 都是 :math:`\mathbb{R}` 上的非负可测函数, 由 Fatou 引理知

      .. math::

         \int_{\mathbb{R}} g ~ \mathrm{d} m \leqslant \varliminf_{n \to \infty} \int_{\mathbb{R}} g_n ~ \mathrm{d} m
         = \varliminf_{n \to \infty} n^{-\alpha} \int_{\mathbb{R}} f(nx) ~ \mathrm{d} x.

      所以

      .. math::

         0 \leqslant \int_{\mathbb{R}} g ~ \mathrm{d} m
         \leqslant \varliminf_{n \to \infty} n^{-\alpha - 1} \int_{\mathbb{R}} f(y) ~ \mathrm{d} y = 0.

      即有 :math:`\displaystyle \int_{\mathbb{R}} g ~ \mathrm{d} m = 0`. 由勒贝格积分的唯一性知, :math:`g = 0` a.e. :math:`x \in \mathbb{R}`,
      也即 :math:`\displaystyle \varliminf_{n \to \infty} n^{-\alpha} f(nx) = 0` a.e. :math:`x \in \mathbb{R}`.

.. _ex-4-14:

14. 设 :math:`f` 是区间 :math:`[0, 1]` 上的可积函数, 若对任何 :math:`c \in (0, 1)` 恒有

    .. math::

      \int_0^c f(x) ~ \mathrm{d} m = 0,

证明 :math:`f \sim 0`.

.. proof:proof::

   由 :math:`\displaystyle \int_0^c f ~ \mathrm{d} m = 0` 对所有 :math:`c \in (0, 1)` 成立知,
   对任意开区间 :math:`(a, b) \subset [0, 1]` 有 :math:`\displaystyle \int_a^b f ~ \mathrm{d} m = 0`.
   由勒贝格积分关于被积集合的可列可加性知, 对任意开集 :math:`G \subset [0, 1]` 有 :math:`\displaystyle \int_G f ~ \mathrm{d} m = 0`.

   不失一般性, 可以设 :math:`f(1) = 0`, 那么由控制收敛定理有

   .. math::

      \int_0^1 f ~ \mathrm{d} m = \int_0^1 \left( \lim_{c \to 1 -} f \cdot \chi_{[0, c]} \right) ~ \mathrm{d} m
      = \lim_{c \to 1 -} \int_0^1 f \cdot \chi_{[0, c]} ~ \mathrm{d} m = \lim_{c \to 1 -} \int_0^c f ~ \mathrm{d} m = 0.

   于是, 对于任意闭集 :math:`F \subset [0, 1]`, 有

   .. math::

      \int_F f ~ \mathrm{d} m = \int_{[0, 1]} f ~ \mathrm{d} m - \int_{[0, 1] \setminus F} f ~ \mathrm{d} m = 0 - 0 = 0.

   假设 :math:`f \not\sim 0`, 记 :math:`I = [0, 1]`, 那么集合

   .. math::

      E = I(f \neq 0) = I(f > 0) \cup I(f < 0) = E_+ \cup E_-

   有正测度, 即 :math:`0 < m E = m E_+ + m E_-`. 因此, :math:`E_+` 或者 :math:`E_-` 至少有一个有正测度, 不妨设 :math:`m E_+ > 0`,
   否则考虑 :math:`-f` 即可. 考虑 :math:`E_+` 的等测核 :math:`\displaystyle B = \bigcup_{n = 1}^\infty F_n \subset E_+`, 其中 :math:`F_n` 是闭集,
   且 :math:`m B = m E_+ > 0`. 令 :math:`\displaystyle B_n = \bigcup_{k = 1}^n F_k` 为闭集, 那么 :math:`\{ B_n \}` 是渐升可测集列,
   且 :math:`\displaystyle \bigcup_{n = 1}^\infty B_n = B`. 注意到 :math:`f` 在集合 :math:`B \subset E_+` 上恒正, 所以由 Levi 定理知

   .. math::

      \int_B f ~ \mathrm{d} m = \int_B \left( \lim_{n \to \infty} f \cdot \chi_{B_n} \right) ~ \mathrm{d} m
      = \lim_{n \to \infty} \int_B f \cdot \chi_{B_n} ~ \mathrm{d} m = \lim_{n \to \infty} \int_{B_n} f ~ \mathrm{d} m = \lim_{n \to \infty} 0 = 0.

   但是由勒贝格积分的唯一性知, :math:`f = 0` a.e. :math:`x \in B`, 这与 :math:`m B > 0` 矛盾, 所以 :math:`f \sim 0`.

.. _ex-4-15:

15. 求极限

    .. math::

      \lim_{n \to \infty} (R) \int_0^1 \dfrac{nx^{1/2}}{1 + n^2 x^2} \sin^5 (nx) ~ \mathrm{d} x.

.. proof:proof::

   记 :math:`f_n(x) = \dfrac{nx^{1/2}}{1 + n^2 x} \sin^5 (nx)`, 那么对任意 :math:`x \in [0, 1]` 有

   .. math::

      \lvert f_n(x) \rvert \leqslant \dfrac{nx^{1/2}}{1 + n^2 x^2} \leqslant \dfrac{1}{2 \sqrt{x}} =: g(x).

   如果能证明 :math:`g` 是勒贝格可积的, 那么由于对任意 :math:`x \in [0, 1]` 有

   .. math::

      \lim_{n \to \infty} f_n(x) = 0,

   由控制收敛定理可知

   .. math::

      \lim_{n \to \infty} (R) \int_0^1 f_n(x) ~ \mathrm{d} x & = \lim_{n \to \infty} (L) \int_0^1 f_n(x) ~ \mathrm{d} x \\
      & = (L) \int_0^1 \lim_{n \to \infty} f_n(x) ~ \mathrm{d} x = 0.

   下面证明 :math:`g` 是勒贝格可积的. 令 :math:`g_n = g \cdot \chi_{[1/n, 1]}`, 那么 :math:`{g_n}` 构成了 :math:`[0, 1]` 上的非负渐升函数列,
   且 :math:`\displaystyle \lim_{n \to \infty} g_n = g`. 由 Levi 定理知

   .. math::

      (L) \int_0^1 g ~ \mathrm{d} x
      & = \lim_{n \to \infty} (L) \int_0^1 g_n ~ \mathrm{d} x = \lim_{n \to \infty} (L) \int_{1/n}^1 g ~ \mathrm{d} x \\
      & = \lim_{n \to \infty} (L) \int_{1/n}^1 \dfrac{1}{2 \sqrt{x}} ~ \mathrm{d} x
        = \lim_{n \to \infty} (R) \int_{1/n}^1 \dfrac{1}{2 \sqrt{x}} ~ \mathrm{d} x \\
      & = \lim_{n \to \infty} \left( \left. x^{1/2} \right|_{1/n}^1 \right) = \lim_{n \to \infty} \left( 1 - \dfrac{1}{\sqrt{n}} \right) = 1 < \infty.

   所以 :math:`g` 是勒贝格可积的, 从而有

   .. math::

      \lim_{n \to \infty} (R) \int_0^1 \dfrac{nx^{1/2}}{1 + n^2 x^2} \sin^5 (nx) ~ \mathrm{d} x = 0.

.. _ex-4-16:

16. 设 :math:`f(x)` 在有限区间 :math:`[a, b]` 上可积, 试证: 对每个 :math:`n \in \mathbb{N}`, :math:`[nf(x)]` 可测且有等式

    .. math::

      \lim_{n \to \infty} \dfrac{1}{n} \int_{(a, b)} [nf(x)] ~ \mathrm{d} m = \int_{(a, b)} f(x) ~ \mathrm{d} m,

    其中 :math:`[y]` 表示实数 :math:`y` 的整部 (即不超过 :math:`y` 的最大整数).

.. proof:proof::

   记 :math:`f_n(x) = [nf(x)]`. 对任意 :math:`\alpha \in \mathbb{R}`, 有

   .. math::

      [nf(x)] > \alpha ~ \Leftrightarrow ~ nf(x) \geqslant [\alpha] + 1 ~ \Leftrightarrow ~ f(x) \geqslant \dfrac{[\alpha] + 1}{n}.

   记 :math:`E = [a, b]`, 那么

   .. math::

      E(f_n > \alpha) = E \left( f \geqslant \dfrac{[\alpha] + 1}{n} \right)

   是可测集, 故 :math:`f_n(x)` 是可测函数.

   记 :math:`g_n(x) = \dfrac{1}{n}[nf(x)]`, 容易证明 :math:`\displaystyle \lim_{n \to \infty} g_n(x) = f(x)`. 又由于有

   .. math::

      f(x) - 1 \leqslant \dfrac{nf(x) - 1}{n} \leqslant g_n(x) \leqslant \dfrac{nf(x)}{n} = f(x),

   所以 :math:`\lvert g_n(x) \rvert \leqslant \lvert f(x) \rvert + 1`. 由于 :math:`f` 在 :math:`[a, b]` 上可积, 且 :math:`[a, b]` 是有限测度集,
   所以 :math:`\lvert f \rvert + 1` 在 :math:`[a, b]` 上可积. 于是由控制收敛定理知

   .. math::

      \lim_{n \to \infty} \dfrac{1}{n} \int_{(a, b)} [nf(x)] ~ \mathrm{d} m = \lim_{n \to \infty} \int_{(a, b)} g_n ~ \mathrm{d} m
      = \int_{(a, b)} \lim_{n \to \infty} g_n ~ \mathrm{d} m
      = \int_{(a, b)} f ~ \mathrm{d} m.

.. _ex-4-19:

19. 设对每个 :math:`n \in \mathbb{N}`, :math:`f_n` 在 :math:`E` 上可积, 序列 :math:`\{f_n\}` 几乎处处收敛于 :math:`f, n \to \infty`,
    且一致地有

    .. math::

      \int_E \lvert f_n \rvert ~ \mathrm{d} m \leqslant K, \quad K \text{ 为常数},

    证明 :math:`f` 可积.

.. proof:proof::

   由于 :math:`f_n` 在 :math:`E` 上可积, 序列 :math:`\{f_n\}` 几乎处处收敛于 :math:`f, n \to \infty`,
   所以 :math:`\lvert f_n \rvert` 在 :math:`E` 上可积, 序列 :math:`\{ \lvert f_n \rvert \}` 几乎处处收敛于 :math:`\lvert f \rvert, n \to \infty`.
   令 :math:`\displaystyle E_0 = E \left( \lim_{n \to \infty} \lvert f_n \rvert \neq \lvert f \rvert \right)`, 那么 :math:`m E_0 = 0`.
   对 :math:`E` 上的非负可测函数列 :math:`\{ f_n \}` 应用 Fatou 引理, 有

   .. math::

      K \geqslant \varliminf_{n \to \infty} \int_E \lvert f_n \rvert ~ \mathrm{d} m \geqslant \int_E \varliminf_{n \to \infty} \lvert f_n \rvert ~ \mathrm{d} m
      & = \int_{E_0} \varliminf_{n \to \infty} \lvert f_n \rvert ~ \mathrm{d} m + \int_{E \setminus E_0} \varliminf_{n \to \infty} \lvert f_n \rvert ~ \mathrm{d} m \\
      & = 0 + \int_{E \setminus E_0} \lvert f \rvert ~ \mathrm{d} m \\
      & = \int_{E_0} \lvert f \rvert ~ \mathrm{d} m + \int_{E \setminus E_0} \lvert f \rvert ~ \mathrm{d} m \\
      & = \int_E \lvert f \rvert ~ \mathrm{d} m.

   所以 :math:`\lvert f \rvert` 在 :math:`E` 上可积, 从而知 :math:`f` 可积.

.. _ex-4-21:

21. 设 :math:`f` 在 :math:`(-\infty, \infty)` 上可积, 证明

    .. math::

      \lim_{h \to 0} \int_{-\infty}^\infty \lvert f(x + h) - f(x) \rvert ~ \mathrm{d} m = 0.

.. proof:proof::

   对每个自然数 :math:`k \in \mathbb{N}`, 令 :math:`E_k = [-k, k]`, 那么 :math:`\forall ~ x \in \mathbb{R}`,
   有 :math:`\displaystyle \lim_{k \to \infty} f \cdot \chi_{E_k} (x) = f (x)`. 由于 :math:`f \in L_{\mathbb{R}}`,
   所以 :math:`\lvert f \rvert \in L_{\mathbb{R}}`, 并且 :math:`\lvert f \cdot \chi_{E_k} (x) \rvert \leqslant \lvert f (x) \rvert`
   对所有 :math:`x \in \mathbb{R}` 以及 :math:`k \in \mathbb{N}` 成立. 于是, 由 Lebesgue 控制收敛定理可得

   .. math::

      \lim_{k \to \infty} \int_{E_k} f ~ \mathrm{d} m = \lim_{k \to \infty} \int_{\mathbb{R}} f \cdot \chi_{E_k} ~ \mathrm{d} m
      = \int_{\mathbb{R}} \lim_{k \to \infty} f \cdot \chi_{E_k} ~ \mathrm{d} m = \int_{\mathbb{R}} f ~ \mathrm{d} m.

   那么 :math:`\forall ~ \varepsilon > 0`, 存在 :math:`K \in \mathbb{N}`, 使得当 :math:`k > K` 时, 有

   .. math::

      0 \leqslant \int_{\mathbb{R} \setminus E_{k-1}} \lvert f \rvert ~ \mathrm{d} m
      = \int_{\mathbb{R}} \lvert f \rvert ~ \mathrm{d} m - \int_{E_{k-1}} \lvert f \rvert ~ \mathrm{d} m < \dfrac{\varepsilon}{3}.

   同时, 对于任一取定的 :math:`k > K`, 可以选取定义在 :math:`E_k` 上的简单函数 :math:`\displaystyle \varphi = \sum_{i=1}^n c_i \chi_{e_i}` 使得

   .. math::
      :label: ex-4-21-eq-1

      \int_{E_k} \lvert f - \varphi \rvert ~ \mathrm{d} m \leqslant \int_{E_{k+1}} \lvert f - \varphi \rvert ~ \mathrm{d} m < \dfrac{\varepsilon}{9}.

   这里, :math:`\varphi` 也被视作是 :math:`E_{k+1}` 上的简单函数, :math:`e_i \subset E` 是互不相交的可测集. 对于 :math:`0 < \lvert h \rvert < 1`,
   在 :math:`E_{k+1}` 上有

   .. math::

      \lvert f(x + h) - f(x) \rvert \leqslant \lvert f(x + h) - \varphi(x + h) \rvert + \lvert \varphi(x + h) - \varphi(x) \rvert + \lvert \varphi(x) - f(x) \rvert.

   对于简单函数 :math:`\varphi`, 令 :math:`M = \displaystyle \sup_{x \in E_{k+1}} \lvert \varphi(x) \rvert = \max_{1 \leqslant i \leqslant n} \lvert c_i \rvert`.
   对所有 :math:`1 \leqslant i \leqslant n`, 可以选取开集 :math:`G_i \supset e_i` 使得 :math:`m G_i < m e_i + \dfrac{\varepsilon}{72nM}`.
   那么所有开集 :math:`G_i` 的构成区间形成了紧集 :math:`E_{k+1}` 的一个开覆盖, 从而可以选出有限个开区间 :math:`I_1, I_2, \dots, I_t`,
   使得 :math:`\displaystyle E_{k+1} \subset \bigcup_{j=1}^t I_j`. 令 :math:`\displaystyle \widetilde{\varphi} = \sum_{j=1}^t \widetilde{c}_j \chi_{I_j}`,
   其中 :math:`\widetilde{c}_j = c_i` 若 :math:`I_j \subset G_i`. 对于可能重叠的部分, 任意取定其中某一个值即可.
   那么当 :math:`\displaystyle 0 < h < \min_{1 \leqslant j \leqslant t} m I_j`, 总有

   .. math::

      \int_{E_{k+1}} \lvert \widetilde{\varphi} (x + h) - \widetilde{\varphi} (x) \rvert ~ \mathrm{d} m \leqslant 4 M t \lvert h \rvert.

   进一步缩小 :math:`\lvert h \rvert`, 使其满足 :math:`0 < \lvert h \rvert < \dfrac{\varepsilon}{72 M t}`, 那么有

   .. math::

      \int_{E_{k+1}} \lvert \widetilde{\varphi} (x + h) - \widetilde{\varphi} (x) \rvert ~ \mathrm{d} m < \dfrac{\varepsilon}{18}.

   另一方面有

   .. math::

      \lvert \varphi(x + h) - \varphi(x) \rvert \leqslant \lvert \varphi(x + h) - \widetilde{\varphi}(x + h) \rvert
      + \lvert \widetilde{\varphi} (x + h) - \widetilde{\varphi} (x) \rvert + \lvert \widetilde{\varphi}(x) - \varphi(x) \rvert,

   从而有

   .. math::
      :label: ex-4-21-eq-2

      & \int_{E_k} \lvert \varphi(x + h) - \varphi(x) \rvert ~ \mathrm{d} m \\
      & \leqslant \int_{E_k} \lvert \varphi(x + h) - \widetilde{\varphi}(x + h) \rvert ~ \mathrm{d} m + \int_{E_k} \lvert \widetilde{\varphi} (x + h)
        - \widetilde{\varphi} (x) \rvert ~ \mathrm{d} m + \int_{E_k} \lvert \widetilde{\varphi}(x) - \varphi(x) \rvert ~ \mathrm{d} m \\
      & \leqslant \int_{E_{k+1}} \lvert \varphi(x) - \widetilde{\varphi}(x) \rvert ~ \mathrm{d} m + \int_{E_k} \lvert \widetilde{\varphi} (x + h)
        - \widetilde{\varphi} (x) \rvert ~ \mathrm{d} m + \int_{E_{k+1}} \lvert \widetilde{\varphi}(x) - \varphi(x) \rvert ~ \mathrm{d} m \\
      & \leqslant 2 \cdot 2M \cdot \dfrac{\varepsilon}{72nM} \cdot n + \dfrac{\varepsilon}{18} \\
      & \leqslant \dfrac{\varepsilon}{9}.

   综合式 :eq:`ex-4-21-eq-1` 和 :eq:`ex-4-21-eq-2`, 有

   .. math::

      & \int_{E_k} \lvert f(x + h) - f(x) \rvert ~ \mathrm{d} m \\
      & \leqslant \int_{E_k} \leqslant \lvert f(x + h) - \varphi(x + h) \rvert ~ \mathrm{d} m + \int_{E_k} \lvert \varphi(x + h)
        - \varphi(x) \rvert ~ \mathrm{d} m + \int_{E_k} \lvert \varphi(x) - f(x) \rvert  ~ \mathrm{d} m \\
      & \leqslant \int_{E_{k+1}} \leqslant \lvert f(x) - \varphi(x) \rvert ~ \mathrm{d} m + \int_{E_k} \lvert \varphi(x + h)
        - \varphi(x) \rvert ~ \mathrm{d} m + \int_{E_{k+1}} \lvert \varphi(x) - f(x) \rvert  ~ \mathrm{d} m \\
      & \leqslant \dfrac{\varepsilon}{9} + \dfrac{\varepsilon}{9} + \dfrac{\varepsilon}{9} = \dfrac{\varepsilon}{3}.

   于是有

   .. math::

      \int_{\mathbb{R}} \lvert f(x + h) - f(x) \rvert ~ \mathrm{d} m
      & = \left( \int_{E_k} + \int_{\mathbb{R} \setminus E_k} \right) \lvert f(x + h) - f(x) \rvert ~ \mathrm{d} m \\
      & \leqslant \int_{E_k} \lvert f(x + h) - f(x) \rvert ~ \mathrm{d} m + \int_{\mathbb{R} \setminus E_k} \lvert f(x + h) \rvert + \lvert f(x) \rvert ~ \mathrm{d} m \\
      & \leqslant \dfrac{\varepsilon}{3} + \int_{\mathbb{R} \setminus E_{k-1}} 2 \lvert f(x) \rvert ~ \mathrm{d} m \\
      & \leqslant \dfrac{\varepsilon}{3} + 2 \cdot \dfrac{\varepsilon}{3} = \varepsilon.

   这便证明了 :math:`\displaystyle \lim_{h \to 0} \int_{-\infty}^\infty \lvert f(x + h) - f(x) \rvert ~ \mathrm{d} m = 0.`

   .. note::

      以上性质称作是 Lebesgue 积分的平均连续性.

      以下是来自《实变函数论》(周民强) 的简化证明:

      任给 :math:`\varepsilon > 0`, 做分解

      .. math::

         f = f_1 + f_2,

      其中 :math:`f_1` 是 :math:`\mathbb{R}` 上具有紧支集的连续函数, :math:`f_2` 满足

      .. math::

         \int_{\mathbb{R}} \lvert f_2 \rvert ~ \mathrm{d} m < \dfrac{\varepsilon}{4}.

      由于连续函数 :math:`f_1` 具有紧支集, 从而一致连续, 所以存在 :math:`\delta > 0`, 使得当 :math:`\lvert h \rvert < \delta` 时有

      .. math::

         \int_{\mathbb{R}} \lvert f_1(x + h) - f_1(x) \rvert ~ \mathrm{d} m < \dfrac{\varepsilon}{2}.

      于是, 当 :math:`\lvert h \rvert < \delta` 时有

      .. math::

         \int_{\mathbb{R}} \lvert f(x + h) - f(x) \rvert ~ \mathrm{d} m
         & \leqslant \int_{\mathbb{R}} \lvert f_1(x + h) - f_1(x) \rvert ~ \mathrm{d} m + \int_{\mathbb{R}} \lvert f_2(x + h) - f_2(x) \rvert ~ \mathrm{d} m \\
         & < \dfrac{\varepsilon}{2} + \int_{\mathbb{R}} \lvert f_2(x + h) - f_2(x) \rvert ~ \mathrm{d} m \\
         & \leqslant \dfrac{\varepsilon}{2} + \int_{\mathbb{R}} \lvert f_2(x + h) \rvert  ~ \mathrm{d} m + \int_{\mathbb{R}} \lvert f_2(x) \rvert ~ \mathrm{d} m \\
         & < \dfrac{\varepsilon}{2} + 2 \cdot \dfrac{\varepsilon}{4} = \varepsilon.

      本质上, 我们原来的证明是在具体地构造分解 :math:`f = f_1 + f_2`.

.. _ex-4-23:

23. 设 :math:`f` 是 :math:`\mathbb{R}` 上的可积函数, 试证

    .. math::

      \hat{f} (t) = \int_{\mathbb{R}} e^{-itx} f(x) ~ \mathrm{d} x.

    是 :math:`\mathbb{R}` 上的连续函数, 且

    .. math::

      \hat{f} (t) = \dfrac{~ \mathrm{d}}{~ \mathrm{d} t} \int_{\mathbb{R}} \dfrac{e^{-itx} - 1}{-ix} f(x) ~ \mathrm{d} x.

.. proof:proof::

   由于 :math:`\left\lvert e^{-itx} f(x) \right\rvert = \lvert f(x) \rvert`, 所以由 Lebesgue 控制收敛定理 (分别对实部虚部),
   对任意 :math:`t_0 \in \mathbb{R}` 有

   .. math::

      \lim_{t \to t_0} \hat{f} (t) = \lim_{t \to t_0} \int_{\mathbb{R}} e^{-itx} f(x) ~ \mathrm{d} x
      = \int_{\mathbb{R}} \lim_{t \to t_0} e^{-itx} f(x) ~ \mathrm{d} x = \int_{\mathbb{R}} e^{-it_0x} f(x) ~ \mathrm{d} x = \hat{f} (t_0).

   这说明 :math:`\hat{f}` 在 :math:`\mathbb{R}` 上连续.

   令 :math:`g(x, t) = \dfrac{e^{-itx} - 1}{-ix} f(x)`, 那么

   .. math::

      \left\lvert \dfrac{\partial}{\partial t} g(x, t) \right\rvert = \left\lvert e^{-itx} f(x) \right\rvert = \lvert f(x) \rvert,

   由 :ref:`积分号下求导定理 <thm-differentiation-under-integral-sign>` 可得

   .. math::

      \dfrac{~ \mathrm{d}}{~ \mathrm{d} t} \int_{\mathbb{R}} g(x, t) ~ \mathrm{d} x
      = \int_{\mathbb{R}} \dfrac{\partial}{\partial t} g(x, t) ~ \mathrm{d} x = \int_{\mathbb{R}} e^{-itx} f(x) ~ \mathrm{d} x = \hat{f} (t).

.. _ex-4-25:

25. 设 :math:`f` 是 :math:`\mathbb{R}` 上的可测函数, 令 :math:`\mu (\alpha) = m \mathbb{R}(\lvert f \rvert > \alpha)`, 试证

    .. math::

      \int_{\mathbb{R}} \lvert f \rvert^p ~ \mathrm{d} m = p \int_0^\infty \alpha^{p-1} \mu (\alpha) ~ \mathrm{d} \alpha, \quad 1 \leqslant p < \infty.

.. proof:proof::

   对任意 :math:`x \in \mathbb{R}`, 有

   .. math::

      \lvert f(x) \rvert^p & = \int_0^{\lvert f(x) \rvert^p} ~ \mathrm{d} t = \int_0^{\infty} \chi_{[0, \lvert f(x) \rvert^p]} (t) ~ \mathrm{d} t \\
      & = \int_0^\infty \chi_{\left\{ y \in \mathbb{R} ~:~ \lvert f(y) \rvert^p > t \right\}} (x) ~ \mathrm{d} t.

   对上式两端在 :math:`\mathbb{R}` 上积分, 由 Fubini 定理可得

   .. math::

      \int_{\mathbb{R}} \lvert f \rvert^p ~ \mathrm{d} m
      & = \int_{\mathbb{R}} \left( \int_0^\infty \chi_{\left\{ y \in \mathbb{R} ~:~ \lvert f(y) \rvert^p > t \right\}} (x) ~ \mathrm{d} t \right) ~ \mathrm{d} x \\
      & = \int_0^{\infty} \left( \int_{\mathbb{R}} \chi_{\left\{ y \in \mathbb{R} ~:~ \lvert f(y) \rvert^p > t \right\}} (x) ~ \mathrm{d} x \right) ~ \mathrm{d} t \\
      & = \int_0^{\infty} m \mathbb{R}(\lvert f \rvert^p > t) ~ \mathrm{d} t \\
      (\text{令 } t = \alpha^p) & = \int_0^{\infty} m \mathbb{R}(\lvert f \rvert^p > \alpha^p) ~ \mathrm{d} \alpha^p \\
      & = \int_0^{\infty} m \mathbb{R}(\lvert f \rvert > \alpha) \cdot p \alpha^{p-1} ~ \mathrm{d} \alpha \\
      & = p \int_0^\infty \alpha^{p-1} \mu (\alpha) ~ \mathrm{d} \alpha.

   .. note::

      这题的结论是所谓的 layer cake representation, 可以推广到一般的测度空间 :math:`(X, \mathscr{R}, \mu)` 上的非负可测函数 :math:`f` 上:

      .. math::

         f(x) = \int_0^{\infty} \chi_{\left\{ y\in X ~:~ f(y) > t \right\}}(x) ~ \mathrm{d} t.

      进一步有

      .. math::

         \int_X f ~ \mathrm{d} \mu = \int_0^{\infty} \mu (\left\{ x\in X ~:~ f(x) > t \right\}) ~ \mathrm{d} t.

.. _ex-4-26:

26. 设 :math:`m E < \infty`, 证明函数 :math:`f` 在 :math:`E` 上可积的充分必要条件是级数 :math:`\displaystyle \sum_{n=1}^\infty m E ( \lvert f \rvert \geqslant n)` 收敛.
    当 :math:`m E = \infty` 时, 结论是否成立?

.. proof:proof::

   :math:`\displaystyle \sum_{n=1}^\infty m E ( \lvert f \rvert \geqslant n)` 是非负项级数, 所以它要么收敛, 要么等于 :math:`\infty`.

   充分性: 由于 :math:`\displaystyle \sum_{n=1}^\infty m E ( \lvert f \rvert \geqslant n)` 收敛,
   即 :math:`\displaystyle \sum_{n=1}^\infty m E ( \lvert f \rvert \geqslant n) < \infty`, 那么由逐项积分定理可得

   .. math::

      \int_E \lvert f \rvert ~ \mathrm{d} m & = \int_E \sum_{n=1}^\infty \lvert f \rvert \cdot \chi_{E(n - 1 \leqslant \lvert f \rvert < n)} ~ \mathrm{d} m
      = \sum_{n=1}^\infty \int_{E(n - 1 \leqslant \lvert f \rvert < n)} \lvert f \rvert ~ \mathrm{d} m \\
      & \leqslant \sum_{n=1}^\infty \int_{E(n - 1 \leqslant \lvert f \rvert < n)} n ~ \mathrm{d} m \\
      & = \sum_{n=1}^\infty n \cdot m E (n - 1 \leqslant \lvert f \rvert < n) \\
      & = \sum_{n=1}^\infty m E (n - 1 \leqslant \lvert f \rvert < n) + \sum_{n=2}^\infty (n - 1) \cdot m E (n - 1 \leqslant \lvert f \rvert < n) \\
      & = m E + \sum_{n=1}^\infty n \cdot m E (n \leqslant \lvert f \rvert < n + 1) \\
      & = m E + \sum_{n=1}^\infty E (\lvert f \rvert \geqslant n) \\
      & < \infty.

   这说明 :math:`\lvert f \rvert` 在 :math:`E` 上可积, 从而知 :math:`f` 在 :math:`E` 上可积.

   必要性: 由于 :math:`f` 在 :math:`E` 上可积, 所以 :math:`\lvert f \rvert` 在 :math:`E` 上可积. 类似于充分性的证明, 有

   .. math::

      \infty > \int_E \lvert f \rvert ~ \mathrm{d} m & = \int_E \sum_{n=1}^\infty \lvert f \rvert \cdot \chi_{E(n - 1 \leqslant \lvert f \rvert < n)} ~ \mathrm{d} m
      = \sum_{n=1}^\infty \int_{E(n - 1 \leqslant \lvert f \rvert < n)} \lvert f \rvert ~ \mathrm{d} m \\
      & \geqslant \sum_{n=1}^\infty \int_{E(n - 1 \leqslant \lvert f \rvert < n)} (n - 1) ~ \mathrm{d} m \\
      & = \sum_{n=1}^\infty (n - 1) \cdot m E (n - 1 \leqslant \lvert f \rvert < n) \\
      & = \sum_{n=2}^\infty (n - 1) \cdot m E (n - 1 \leqslant \lvert f \rvert < n) \\
      & = \sum_{n=1}^\infty n \cdot m E (n \leqslant \lvert f \rvert < n + 1) \\
      & = \sum_{n=1}^\infty E (\lvert f \rvert \geqslant n).

   这说明 :math:`\displaystyle \sum_{n=1}^\infty m E ( \lvert f \rvert \geqslant n)` 收敛.

   .. note::

      实际上, 本题使用了如下的不等式:

      .. math::

         \sum_{n=1}^\infty E (\lvert f \rvert \geqslant n) \leqslant \int_E \lvert f \rvert ~ \mathrm{d} m
         \leqslant m E + \sum_{n=1}^\infty E (\lvert f \rvert \geqslant n).

   从上面的证明可以看出, 当 :math:`m E = \infty` 时, 级数 :math:`\displaystyle \sum_{n=1}^\infty m E ( \lvert f \rvert \geqslant n)` 收敛是
   :math:`f` 在 :math:`E` 上可积的必要条件, 但不是充分条件. 相关的反例: 令 :math:`f = \dfrac{1}{2}` 为常值函数,
   那么对任意自然数 :math:`n \in \mathbb{N}`, :math:`E ( \lvert f \rvert \geqslant n) = \emptyset`,
   所以 :math:`\displaystyle \sum_{n=1}^\infty m E ( \lvert f \rvert \geqslant n) = \sum_{n=1}^\infty 0 = 0`,
   但 :math:`\displaystyle \int_E \lvert f \rvert ~ \mathrm{d} m = \dfrac{1}{2} \cdot m E = \infty`, 所以 :math:`f` 在 :math:`E` 上不可积.
