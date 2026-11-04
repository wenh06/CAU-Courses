第四章  微分中值定理与导数的应用
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. contents:: :local:


.. _ex-chap4:

课后习题解答
====================================

.. _ex-chap4_sec1:

§4.1 微分中值定理
------------------------------------

.. _ex-chap4_sec1-ex1:

1. 验证函数 :math:`f(x) = x \sqrt{3 - x}` 在区间 :math:`[0, 3]` 上是否满足罗尔中值定理, 若满足, 求出定理中的
   :math:`\xi`.

.. proof:solution::

   :math:`f(x)` 是初等函数, 在 :math:`[0, 3]` 上连续, 在 :math:`(0, 3)` 内可导, 且 :math:`f(0) = 0 = f(3)`,
   满足罗尔中值定理的条件. 求导

   .. math::
      f'(x) = \sqrt{3-x} - \dfrac{x}{2\sqrt{3-x}} = \dfrac{2(3-x) - x}{2\sqrt{3-x}} = \dfrac{6 - 3x}{2\sqrt{3-x}},

   令 :math:`f'(\xi) = 0` 得 :math:`\xi = 2 \in (0, 3)`, 即罗尔中值定理结论成立, 定理中的 :math:`\xi = 2`.

2. 不用求出函数 :math:`f(x) = (x - 2)(x - 3)(x - 4)(x - 5)` 的导数, 说明方程 :math:`f'(x) = 0` 有几个实根,
   并指出它们所在的区间.

.. proof:solution::

   :math:`f(x)` 是多项式, 处处连续可导, 且 :math:`f(2) = f(3) = f(4) = f(5) = 0`. 在区间
   :math:`[2,3]`, :math:`[3,4]`, :math:`[4,5]` 上分别应用罗尔中值定理, 知 :math:`f'(x) = 0` 在
   :math:`(2,3)`, :math:`(3,4)`, :math:`(4,5)` 内各至少有一个实根, 即至少有 3 个实根.

   又 :math:`f'(x)` 是三次多项式, 至多只有 3 个实根. 因此方程 :math:`f'(x) = 0` 恰有 3 个实根,
   分别位于区间 :math:`(2,3)`, :math:`(3,4)`, :math:`(4,5)` 内.

.. _ex-chap4_sec1-ex3:

3. 设 :math:`f(x)` 在 :math:`[0, 1]` 上连续, 在 :math:`(0, 1)` 内可导, 且 :math:`f(1) = 0`, 试证明: 至少存在一点
   :math:`\xi \in (0, 1)` 使得 :math:`\displaystyle f'(\xi) = -\dfrac{2 f(\xi)}{\xi}`.

.. proof:proof::

   构造辅助函数 :math:`g(x) = x^2 f(x)`. 那么 :math:`g(x)` 在 :math:`[0, 1]` 上连续, 在 :math:`(0, 1)` 内可导,
   且 :math:`g(0) = g(1) = 0`.

   .. math::
      g'(x) = 2x f(x) + x^2 f'(x).

   由罗尔定理知, 存在 :math:`\xi \in (0, 1)` 使得

   .. math::
      g'(\xi) = 0 \implies f'(\xi) = -\dfrac{2f(\xi)}{\xi}.

.. _ex-chap4_sec1-ex4:

4. 设 :math:`0 < a < b`, 证明不等式 :math:`\displaystyle \dfrac{b-a}{b} < \ln \dfrac{b}{a} < \dfrac{b-a}{a}`.

.. proof:proof::

   设 :math:`f(x) = \ln x`, 则 :math:`f'(x) = \dfrac{1}{x}`. 由拉格朗日中值定理知, 存在 :math:`\xi \in (a, b)` 使得

   .. math::
      \ln \dfrac{b}{a} = f(b) - f(a) = f'(\xi) \cdot \left( b - a \right) = \dfrac{1}{\xi} \cdot \left( b - a \right).

   由于 :math:`\displaystyle \dfrac{1}{b} < \dfrac{1}{\xi} < \dfrac{1}{a}`, 所以

   .. math::
      \dfrac{b-a}{b} < \ln \dfrac{b}{a} < \dfrac{b-a}{a}.

.. note::

   这些不等式的证明, 都是通过构造某个 (辅助) 函数, 再利用微分中值定理来完成的.
   关键在于, 通过要证明的不等式, 找到 (反推) 合适的辅助函数.

.. _ex-chap4_sec2:

§4.2 洛必达法则
------------------------------------

.. _ex-chap4_sec2-ex1:

1. 用洛必达法则求下列极限.

   (1) :math:`\lim\limits_{x \to 0} \dfrac{\ln(1 + x)}{x}`; \qquad
   (2) :math:`\lim\limits_{x \to 0} \dfrac{e^x - e^{-x}}{\sin x}`;

   (3) :math:`\lim\limits_{x \to 0} \dfrac{\tan x - x}{x - \sin x}`; \qquad
   (4) :math:`\lim\limits_{x \to 0} \dfrac{\sin 3x}{\tan 5x}`;

   (5) :math:`\lim\limits_{x \to a} \dfrac{x^m - a^m}{x^n - a^n}`; \qquad
   (6) :math:`\lim\limits_{x \to 1} \left( \dfrac{2}{x^2 - 1} - \dfrac{1}{x - 1} \right)`;

   (7) :math:`\lim\limits_{x \to \infty} \left( 1 + \dfrac{a}{x} \right)^x`; \qquad
   (8) :math:`\lim\limits_{x \to 0} x^{\sin x}`.

.. proof:solution::

   (1). :math:`\dfrac{0}{0}` 型, 用洛必达法则,

   .. math::
      \lim_{x \to 0} \dfrac{\ln(1+x)}{x} = \lim_{x \to 0} \dfrac{\frac{1}{1+x}}{1} = 1.

   (2). :math:`\dfrac{0}{0}` 型,

   .. math::
      \lim_{x \to 0} \dfrac{e^x - e^{-x}}{\sin x} = \lim_{x \to 0} \dfrac{e^x + e^{-x}}{\cos x} = 2.

   (3). :math:`\dfrac{0}{0}` 型, 用洛必达法则后再化简,

   .. math::
      \lim_{x \to 0} \dfrac{\tan x - x}{x - \sin x}
      = \lim_{x \to 0} \dfrac{\sec^2 x - 1}{1 - \cos x}
      = \lim_{x \to 0} \dfrac{\tan^2 x}{1 - \cos x}
      = \lim_{x \to 0} \dfrac{x^2}{\frac{x^2}{2}} = 2.

   (4). :math:`\dfrac{0}{0}` 型,

   .. math::
      \lim_{x \to 0} \dfrac{\sin 3x}{\tan 5x} = \lim_{x \to 0} \dfrac{3\cos 3x}{5\sec^2 5x} = \dfrac{3}{5}.

   (5). :math:`\dfrac{0}{0}` 型,

   .. math::
      \lim_{x \to a} \dfrac{x^m - a^m}{x^n - a^n} = \lim_{x \to a} \dfrac{m x^{m-1}}{n x^{n-1}} = \dfrac{m}{n} a^{m-n}.

   (6). :math:`\infty - \infty` 型, 先通分化为 :math:`\dfrac{0}{0}` 型,

   .. math::
      \lim_{x \to 1} \left( \dfrac{2}{x^2 - 1} - \dfrac{1}{x - 1} \right)
      = \lim_{x \to 1} \dfrac{2 - (x+1)}{(x-1)(x+1)}
      = \lim_{x \to 1} \dfrac{-1}{x+1}
      = -\dfrac{1}{2}.

   (7). :math:`1^{\infty}` 型, 先取对数: 令 :math:`A = \lim\limits_{x \to \infty} x \ln\left(1 + \dfrac{a}{x}\right)`,
   这是 :math:`\dfrac{0}{0}` 型 (改写为 :math:`\dfrac{\ln(1+a/x)}{1/x}`), 用洛必达法则,

   .. math::
      A = \lim_{x \to \infty} \dfrac{\ln(1+\frac{a}{x})}{\frac{1}{x}}
      = \lim_{x \to \infty} \dfrac{\frac{-a/x^2}{1 + a/x}}{-\frac{1}{x^2}} = a,

   故原极限 :math:`= e^a`.

   (8). 这是 :math:`0^0` 型 (按 :math:`x \to 0^+` 理解). 由 :math:`x^{\sin x} = e^{\sin x \ln x}`, 而

   .. math::
      \lim_{x \to 0^+} \sin x \ln x = \lim_{x \to 0^+} \dfrac{\sin x}{x} \cdot x \ln x = 1 \times 0 = 0

   (其中 :math:`x\ln x \to 0` 可由洛必达法则 :math:`\lim\limits_{x \to 0^+} \dfrac{\ln x}{\frac{1}{x}} = \lim\limits_{x \to 0^+} \dfrac{\frac{1}{x}}{-\frac{1}{x^2}} = \lim\limits_{x \to 0^+} (-x) = 0` 得到),
   故原极限 :math:`= e^0 = 1`.

.. _ex-chap4_sec2-ex2:

2. 验证极限 :math:`\lim\limits_{x \to \infty} \dfrac{x + \sin x}{x}` 存在, 但不能用洛必达法则得出.

.. proof:solution::

   一方面,

   .. math::
      \lim_{x \to \infty} \dfrac{x + \sin x}{x} = \lim_{x \to \infty} \left( 1 + \dfrac{\sin x}{x} \right) = 1,

   极限存在. 另一方面, 若用洛必达法则, 分子分母求导得

   .. math::
      \lim_{x \to \infty} \dfrac{1 + \cos x}{1},

   其中 :math:`\cos x` 在 :math:`[-1, 1]` 上无限振荡, 该极限不存在. 这与洛必达法则的条件
   "导数之比的极限存在 (或为无穷大)" 不符, 因此此处不能使用洛必达法则 (用了也只能说明条件不满足, 并不导致矛盾).

.. _ex-chap4_sec2-ex3:

3. 验证极限 :math:`\lim\limits_{x \to 0} \dfrac{x^2 \sin \dfrac{1}{x}}{\sin x}` 存在, 但不能用洛必达法则得出.

.. proof:solution::

   一方面, 由 :math:`\left| x^2 \sin\dfrac{1}{x} \right| \leqslant x^2` 及 :math:`\sin x \sim x`,

   .. math::
      \left| \dfrac{x^2 \sin\frac{1}{x}}{\sin x} \right| \leqslant \dfrac{x^2}{|\sin x|} \sim |x| \longrightarrow 0,

   故极限存在且为 :math:`0`. 另一方面, 若用洛必达法则, 得

   .. math::
      \lim_{x \to 0} \dfrac{2x \sin\frac{1}{x} - \cos\frac{1}{x}}{\cos x},

   其中 :math:`\cos\dfrac{1}{x}` 在 :math:`x \to 0` 时无限振荡, 极限不存在, 洛必达法则的条件不满足,
   因此不能用洛必达法则求此极限.

.. _ex-chap4_sec3:

§4.3 泰勒公式
------------------------------------

.. _ex-chap4_sec3-ex1:

1. 证明函数 :math:`f(x)` 和它的泰勒多项式 :math:`P_n(x)` 在 :math:`x_0` 处的 :math:`0` 阶, :math:`1` 阶,
   :math:`\cdots`, :math:`n` 阶导数值完全相同.

.. proof:solution::

   泰勒多项式为

   .. math::
      P_n(x) = \sum_{k=0}^{n} \dfrac{f^{(k)}(x_0)}{k!} (x - x_0)^k.

   对任意 :math:`0 \leqslant j \leqslant n`, 逐项求 :math:`j` 阶导数. 对第 :math:`k < j` 项,
   求导 :math:`j` 次后为零; 对第 :math:`k > j` 项, 求导 :math:`j` 次后仍含有因子 :math:`(x - x_0)^{k-j}`,
   在 :math:`x = x_0` 处取值为零; 只有第 :math:`k = j` 项有非零贡献:

   .. math::
      \left[ \dfrac{f^{(j)}(x_0)}{j!} (x - x_0)^j \right]^{(j)} = f^{(j)}(x_0).

   因此 :math:`P_n^{(j)}(x_0) = f^{(j)}(x_0)` 对 :math:`j = 0, 1, \dots, n` 都成立.

.. _ex-chap4_sec3-ex2:

2. 计算函数 :math:`f(x) = \sin x + x^2` 在 :math:`x_0 = \pi` 处的 :math:`0` 阶, :math:`1` 阶, :math:`2` 阶,
   :math:`3` 阶泰勒多项式.

.. proof:solution::

   依次计算各阶导数在 :math:`x_0 = \pi` 处的值:

   .. math::
      f(\pi) = \pi^2, \quad f'(x) = \cos x + 2x, \quad f'(\pi) = 2\pi - 1, \quad
      f''(x) = -\sin x + 2, \quad f''(\pi) = 2, \quad f'''(x) = -\cos x, \quad f'''(\pi) = 1.

   于是

   .. math::
      & P_0(x) = \pi^2; \\
      & P_1(x) = \pi^2 + (2\pi - 1)(x - \pi); \\
      & P_2(x) = \pi^2 + (2\pi - 1)(x - \pi) + (x - \pi)^2; \\
      & P_3(x) = \pi^2 + (2\pi - 1)(x - \pi) + (x - \pi)^2 + \dfrac{1}{6}(x - \pi)^3.

.. _ex-chap4_sec3-ex3:

3. 计算第 2 题中 :math:`3` 阶泰勒多项式在 :math:`x_0 = \pi` 处的 :math:`0` 阶, :math:`1` 阶, :math:`2` 阶,
   :math:`3` 阶导数, 并将它们与 :math:`f(x)` 在 :math:`x_0 = \pi` 处的 :math:`0` 阶, :math:`1` 阶, :math:`2` 阶,
   :math:`3` 阶导数进行对比.

.. proof:solution::

   由 :math:`P_3(x) = \pi^2 + (2\pi - 1)(x-\pi) + (x-\pi)^2 + \dfrac{1}{6}(x-\pi)^3` 逐阶求导并代入 :math:`x = \pi`:

   .. math::
      P_3(\pi) = \pi^2, \quad P_3'(\pi) = 2\pi - 1, \quad P_3''(\pi) = 2, \quad P_3'''(\pi) = 1.

   与第 2 题中 :math:`f(x)` 在 :math:`x_0 = \pi` 处的各阶导数值

   .. math::
      f(\pi) = \pi^2, \quad f'(\pi) = 2\pi - 1, \quad f''(\pi) = 2, \quad f'''(\pi) = 1

   对比, 两者完全相同, 这正是 :ref:`第 1 题 <ex-chap4_sec3-ex1>` 所证明的结论.

.. _ex-chap4_sec3-ex4:

4. 分别计算函数 :math:`f(x) = \sin x` 在 :math:`x_0 = 0` 和 :math:`x_0 = \dfrac{\pi}{2}` 处带有皮亚诺余项的
   泰勒公式, 其中 :math:`n` 是一个自然数.

.. proof:solution::

   在 :math:`x_0 = 0` 处 (麦克劳林公式), :math:`\sin x` 的偶数阶导数在 :math:`0` 处为零, 奇数阶导数依次为
   :math:`\pm 1`, 于是

   .. math::
      \sin x = x - \dfrac{x^3}{3!} + \dfrac{x^5}{5!} - \cdots + (-1)^n \dfrac{x^{2n+1}}{(2n+1)!} + o\left( x^{2n+2} \right).

   在 :math:`x_0 = \dfrac{\pi}{2}` 处, 令 :math:`t = x - \dfrac{\pi}{2}`, 则 :math:`\sin x = \cos t`,
   而 :math:`\cos t` 的偶数阶导数依次为 :math:`(-1)^k`, 奇数阶导数在 :math:`0` 处为零, 于是

   .. math::
      \sin x = 1 - \dfrac{\left( x - \frac{\pi}{2} \right)^2}{2!}
      + \dfrac{\left( x - \frac{\pi}{2} \right)^4}{4!} - \cdots
      + (-1)^n \dfrac{\left( x - \frac{\pi}{2} \right)^{2n}}{(2n)!}
      + o\left( \left( x - \frac{\pi}{2} \right)^{2n+1} \right).

.. _ex-chap4_sec3-ex5:

5. 计算函数 :math:`f(x) = x^3 + 6x - 1` 在 :math:`x_0 = 2` 处的带有拉格朗日余项的 :math:`n` 阶泰勒公式, 其中
   :math:`n \geqslant 3`.

.. proof:solution::

   计算各阶导数: :math:`f(2) = 19`, :math:`f'(x) = 3x^2 + 6` 故 :math:`f'(2) = 18`,
   :math:`f''(x) = 6x` 故 :math:`f''(2) = 12`, :math:`f'''(x) = 6`, 四阶及更高阶导数恒为零. 于是对
   :math:`n \geqslant 3`,

   .. math::
      f(x) = 19 + 18(x-2) + \dfrac{12}{2!}(x-2)^2 + \dfrac{6}{3!}(x-2)^3
      = 19 + 18(x-2) + 6(x-2)^2 + (x-2)^3,

   且拉格朗日余项 :math:`R_n(x) = \dfrac{f^{(n+1)}(\xi)}{(n+1)!}(x-2)^{n+1} = 0` (:math:`n \geqslant 3` 时
   :math:`f^{(n+1)} \equiv 0`), 即泰勒多项式就是 :math:`f(x)` 本身, 展开是精确的.

.. _ex-chap4_sec3-ex6:

6. 考虑 :math:`a` 为实数和 :math:`n` 为自然数, 计算函数 :math:`f(x) = (1 + x)^a` 带有皮亚诺余项的
   :math:`n` 阶麦克劳林公式.

.. proof:solution::

   逐阶求导: :math:`f^{(k)}(x) = a(a-1)\cdots(a-k+1)(1+x)^{a-k}`, 故
   :math:`f^{(k)}(0) = a(a-1)\cdots(a-k+1)`. 于是

   .. math::
      (1+x)^a = 1 + ax + \dfrac{a(a-1)}{2!} x^2 + \cdots
      + \dfrac{a(a-1)\cdots(a-n+1)}{n!} x^n + o(x^n).

   特别地, 当 :math:`a` 为正整数 :math:`m` 且 :math:`n \geqslant m` 时, 上式就是二项式展开 (余项为零).

.. _ex-chap4_sec3-ex7:

7. 利用 :math:`e^x` 带有拉格朗日余项的麦克劳林公式计算 :math:`e` 的近似值, 要求误差不超过 :math:`10^{-3}`.

.. proof:solution::

   :math:`e^x` 的带有拉格朗日余项的麦克劳林公式为

   .. math::
      e^x = 1 + x + \dfrac{x^2}{2!} + \cdots + \dfrac{x^n}{n!} + \dfrac{e^{\xi}}{(n+1)!} x^{n+1}
      \quad (0 < \xi < x).

   取 :math:`x = 1`, 得 :math:`e = \sum\limits_{k=0}^{n} \dfrac{1}{k!} + \dfrac{e^{\xi}}{(n+1)!}`,
   余项满足 :math:`0 < \dfrac{e^{\xi}}{(n+1)!} < \dfrac{3}{(n+1)!}`. 要求误差不超过 :math:`10^{-3}`,
   只需 :math:`\dfrac{3}{(n+1)!} \leqslant 10^{-3}`, 即 :math:`(n+1)! \geqslant 3000`. 取 :math:`n = 6`
   (:math:`7! = 5040 > 3000`), 此时

   .. math::
      e \approx 1 + 1 + \dfrac{1}{2} + \dfrac{1}{6} + \dfrac{1}{24} + \dfrac{1}{120} + \dfrac{1}{720}
      = \dfrac{1957}{720} \approx 2.718,

   误差不超过 :math:`\dfrac{3}{5040} \approx 0.0006 < 10^{-3}`.

.. _ex-chap4_sec3-ex8:

8. 证明当 :math:`x \to 0` 时, 有:

   .. math::
      \ln(\cos x) = -\frac{1}{2}x^2 - \frac{1}{12}x^4 - \frac{1}{45}x^6 + o(x^6).

.. proof:proof::

   由泰勒公式知, 当 :math:`x \to 0` 时, 有

   .. math::
      & \cos x = 1 - \frac{1}{2}x^2 + \frac{1}{24}x^4 - \frac{1}{720}x^6 + o(x^6), \\
      & \ln (1 + u) = {\color{red}u} - {\color{cyan}\frac{1}{2}u^2} + {\color{green}\frac{1}{3}u^3} + o(u^3).

   .. note::
      注意思考为什么 :math:`\ln (1 + u)` 展开到 3 次项就够了.

   将 :math:`u = -\frac{1}{2}x^2 + \frac{1}{24}x^4 - \frac{1}{720}x^6 + o(x^6)` 代入第二式, 得

   .. math::
      \ln(\cos x) = \ln(1 + u) = & {\color{red} -\frac{1}{2}x^2 + \frac{1}{24}x^4 - \frac{1}{720}x^6 + o(x^6)} \\
      & - {\color{cyan} \frac{1}{2}\left(-\frac{1}{2}x^2 + \frac{1}{24}x^4 - \frac{1}{720}x^6 + o(x^6)\right)^2} \\
      & + {\color{green} \frac{1}{3}\left(-\frac{1}{2}x^2 + \frac{1}{24}x^4 - \frac{1}{720}x^6 + o(x^6)\right)^3} + o(u^3) \\
      = & {\color{red} - \frac{1}{2}x^2 + \frac{1}{24}x^4 - \frac{1}{720}x^6 + o(x^6)} \\
      & -{\color{cyan} \frac{1}{2}\left( \frac{1}{4}x^4 - \frac{1}{24}x^6 + o(x^6)\right)} \\
      & +{\color{green} \frac{1}{3}\left( -\frac{1}{8}x^6 + o(x^6)\right)} + o(x^6) \\
      = & {\color{red} -\frac{1}{2}x^2} - \left({\color{cyan}\frac{1}{8}} - {\color{red}\frac{1}{24}}\right) x^4
        - \left({\color{red}\frac{1}{720}} - {\color{cyan}\frac{1}{48}} + {\color{green}\frac{1}{24}}\right) x^6 + o(x^6) \\
      = & -\frac{1}{2}x^2 - \frac{1}{12}x^4 - \frac{1}{45}x^6 + o(x^6).

.. _ex-chap4_sec3-ex9:

9. 用泰勒公式计算极限:

   .. math::
      \lim_{x \to 0} \dfrac{\ln(\cos x)}{x \sin x - \frac{1}{2}(e^x - 1)^2}.

.. proof:solution::

   可以利用 :ref:`上一题 <ex-chap4_sec3-ex8>` 的结果, 先对分子进行等价无穷小替换

   .. math::
      \ln(\cos x) \sim -\frac{1}{2}x^2.

   .. note::
      假设我们不知道 :ref:`上一题 <ex-chap4_sec3-ex8>` 的结果, 我们同样可以做等价无穷小替换

      .. math::
         \ln(\cos x) = \ln(1 + (\cos x - 1)) \sim \cos x - 1 \sim -\frac{1}{2}x^2.

   对于分母中涉及的函数, 有

   .. math::
      & \sin x = x - \frac{1}{6}x^3 + o(x^3), \\
      & e^x = 1 + x + \frac{1}{2}x^2 + o(x^2),

   代入极限式中, 有

   .. math::
      \lim_{x \to 0} \dfrac{\ln(\cos x)}{x \sin x - \frac{1}{2}(e^x - 1)^2}
      = & \lim_{x \to 0} \dfrac{-\frac{1}{2}x^2}{(x^2 - \frac{1}{6}x^4 + o(x^4)) - \frac{1}{2}(x + \frac{1}{2}x^2 + o(x^2))^2} \\
      = & \lim_{x \to 0} \dfrac{-\frac{1}{2}x^2}{(x^2 + o(x^2)) - \frac{1}{2}(x^2 + o(x^2))} \\
      = & \lim_{x \to 0} \dfrac{-\frac{1}{2}x^2}{\frac{1}{2}x^2 + o(x^2)} \\
      = & -1.

.. _ex-chap4_sec4:

§4.4 函数的单调性
------------------------------------

.. _ex-chap4_sec4-ex1:

1. 证明: 开区间上的可微函数是常数当且仅当它的导数在这个区间上恒为 :math:`0`.

.. proof:solution::

   必要性显然: 若 :math:`f(x) \equiv C`, 则 :math:`f'(x) = 0` 处处成立.

   充分性: 设 :math:`f'(x) = 0` 在开区间 :math:`I` 内恒成立. 任取 :math:`x_1 < x_2 \in I`,
   :math:`f` 在 :math:`[x_1, x_2]` 上连续, 在 :math:`(x_1, x_2)` 内可导, 由拉格朗日中值定理, 存在
   :math:`\xi \in (x_1, x_2)`, 使得

   .. math::
      f(x_2) - f(x_1) = f'(\xi)(x_2 - x_1) = 0,

   即 :math:`f(x_1) = f(x_2)`. 由 :math:`x_1, x_2` 的任意性, :math:`f(x)` 在 :math:`I` 上是常数.

.. _ex-chap4_sec4-ex2:

2. 确定函数 :math:`f(x) = 2x^3 - 9x^2 + 12x - 3` 的单调区间.

.. proof:solution::

   :math:`f'(x) = 6x^2 - 18x + 12 = 6(x-1)(x-2)`. 当 :math:`x < 1` 或 :math:`x > 2` 时 :math:`f'(x) > 0`,
   当 :math:`1 < x < 2` 时 :math:`f'(x) < 0`. 故单调增加区间为 :math:`(-\infty, 1]` 与 :math:`[2, +\infty)`,
   单调减少区间为 :math:`[1, 2]`.

.. _ex-chap4_sec4-ex3:

3. 确定函数 :math:`f(x) = \left( x^2 \right)^{\frac{1}{3}}` 的单调区间.

.. proof:solution::

   :math:`f(x) = |x|^{\frac{2}{3}}`, 定义域为 :math:`\mathbb{R}`. 当 :math:`x \neq 0` 时,

   .. math::
      f'(x) = \dfrac{2}{3} |x|^{-\frac{1}{3}} \operatorname{sgn}(x)
      = \begin{cases} -\dfrac{2}{3\sqrt[3]{|x|}}, & x < 0, \\[2mm] \dfrac{2}{3\sqrt[3]{x}}, & x > 0, \end{cases}

   在 :math:`x = 0` 处导数不存在. 于是 :math:`f(x)` 在 :math:`(-\infty, 0]` 上单调减少, 在 :math:`[0, +\infty)` 上单调增加.

.. _ex-chap4_sec5:

§4.5 函数的极值与最值
------------------------------------

.. _ex-chap4_sec5-ex1:

1. 求下列函数的极值.

   (1) :math:`y = x^3 - 3x^2 - 9x + 5`; \qquad
   (2) :math:`y = (x - 1) \sqrt[3]{x^2}`;

   (3) :math:`y = x - 2 \sin x` (:math:`0 \leqslant x \leqslant 2\pi`); \qquad
   (4) :math:`y = x + \sqrt{1 - x}`;

   (5) :math:`y = x^2 \ln x`; \qquad
   (6) :math:`y = \dfrac{\ln^2 x}{x}`.

.. proof:solution::

   (1). :math:`y' = 3x^2 - 6x - 9 = 3(x+1)(x-3)`. 驻点 :math:`x = -1, 3`, 且
   :math:`y'' = 6x - 6`: :math:`y''(-1) = -12 < 0` 为极大, :math:`y''(3) = 12 > 0` 为极小. 故

   .. math::
      \text{极大值} ~ y(-1) = 10, \qquad \text{极小值} ~ y(3) = -22.

   (2). :math:`y' = \sqrt[3]{x^2} + (x-1)\cdot\dfrac{2}{3}x^{-\frac{1}{3}} = \dfrac{3x + 2(x-1)}{3\sqrt[3]{x}} = \dfrac{5x-2}{3\sqrt[3]{x}}`.

   驻点 :math:`x = \dfrac{2}{5}`, 另在 :math:`x = 0` 处导数不存在. 列表分析符号: :math:`x < 0` 时
   :math:`y' > 0`; :math:`0 < x < \dfrac{2}{5}` 时 :math:`y' < 0`; :math:`x > \dfrac{2}{5}` 时 :math:`y' > 0`.
   故

   .. math::
      \text{极大值} ~ y(0) = 0, \qquad \text{极小值} ~ y\left( \dfrac{2}{5} \right) = -\dfrac{3}{5}\sqrt[3]{\dfrac{4}{25}}.

   (3). :math:`y' = 1 - 2\cos x`. 令 :math:`y' = 0` 得 :math:`\cos x = \dfrac{1}{2}`, 在 :math:`[0, 2\pi]` 内
   :math:`x = \dfrac{\pi}{3}, \dfrac{5\pi}{3}`. 由 :math:`y'' = 2\sin x`: :math:`y''\left(\dfrac{\pi}{3}\right) = \sqrt{3} > 0`,
   :math:`y''\left(\dfrac{5\pi}{3}\right) = -\sqrt{3} < 0`. 故

   .. math::
      \text{极小值} ~ y\left( \dfrac{\pi}{3} \right) = \dfrac{\pi}{3} - \sqrt{3}, \qquad
      \text{极大值} ~ y\left( \dfrac{5\pi}{3} \right) = \dfrac{5\pi}{3} + \sqrt{3}.

   (4). 定义域 :math:`x \leqslant 1`. :math:`y' = 1 - \dfrac{1}{2\sqrt{1-x}}`, 令 :math:`y' = 0` 得
   :math:`\sqrt{1-x} = \dfrac{1}{2}`, 即 :math:`x = \dfrac{3}{4}`. 由
   :math:`y'' = -\dfrac{1}{4(1-x)^{\frac{3}{2}}} < 0`, 知

   .. math::
      \text{极大值} ~ y\left( \dfrac{3}{4} \right) = \dfrac{3}{4} + \dfrac{1}{2} = \dfrac{5}{4},

   无极小值.

   (5). 定义域 :math:`x > 0`. :math:`y' = 2x\ln x + x = x(2\ln x + 1)`, 令 :math:`y' = 0` 得 :math:`x = e^{-\frac{1}{2}}`.
   当 :math:`0 < x < e^{-\frac{1}{2}}` 时 :math:`y' < 0`, 当 :math:`x > e^{-\frac{1}{2}}` 时 :math:`y' > 0`, 故

   .. math::
      \text{极小值} ~ y\left( e^{-\frac{1}{2}} \right) = e^{-1} \cdot \left( -\dfrac{1}{2} \right) = -\dfrac{1}{2e},

   无极大值.

   (6). 定义域 :math:`x > 0`. :math:`y' = \dfrac{2\ln x \cdot \frac{1}{x} \cdot x - \ln^2 x}{x^2} = \dfrac{\ln x (2 - \ln x)}{x^2}`,
   令 :math:`y' = 0` 得 :math:`x = 1` 或 :math:`x = e^2`. 当 :math:`0 < x < 1` 时 :math:`y' < 0`,
   当 :math:`1 < x < e^2` 时 :math:`y' > 0`, 当 :math:`x > e^2` 时 :math:`y' < 0`. 故

   .. math::
      \text{极小值} ~ y(1) = 0, \qquad \text{极大值} ~ y(e^2) = \dfrac{4}{e^2}.

.. _ex-chap4_sec5-ex2:

2. 求下列函数在指定区间上的最大值和最小值.

   (1) :math:`y = x^4 - 8x^2 + 6`, :math:`x \in [-1, 3]`; \qquad
   (2) :math:`y = x + \sqrt{1 - x}`, :math:`x \in [-5, 1]`;

   (3) :math:`y = 2 \tan x - \tan^2 x`, :math:`x \in \left[ 0, \dfrac{\pi}{3} \right]`; \qquad
   (4) :math:`y = \lvert x^2 + 3x + 2 \rvert`, :math:`x \in [-3, 3]`;

   (5) :math:`y = \sqrt{x} \ln x`, :math:`x \in (0, +\infty)`; \qquad
   (6) :math:`y = \sin^3 x + \cos^3 x`, :math:`x \in \left[ -\dfrac{\pi}{4}, \dfrac{3\pi}{4} \right]`.

.. proof:solution::

   (1). :math:`y' = 4x^3 - 16x = 4x(x-2)(x+2)`, 在 :math:`[-1, 3]` 内驻点为 :math:`x = 0, 2`.
   计算驻点与端点的函数值:

   .. math::
      y(-1) = -1, \quad y(0) = 6, \quad y(2) = -10, \quad y(3) = 15.

   故最大值为 :math:`y(3) = 15`, 最小值为 :math:`y(2) = -10`.

   (2). :math:`y' = 1 - \dfrac{1}{2\sqrt{1-x}}`, 驻点 :math:`x = \dfrac{3}{4}`. 计算驻点与端点的函数值:

   .. math::
      y(-5) = \sqrt{6} - 5 \approx -2.55, \quad y\left(\dfrac{3}{4}\right) = \dfrac{5}{4}, \quad y(1) = 1.

   故最大值为 :math:`y\left(\dfrac{3}{4}\right) = \dfrac{5}{4}`, 最小值为 :math:`y(-5) = \sqrt{6} - 5`.

   (3). 令 :math:`u = \tan x`, 则 :math:`u \in [0, \sqrt{3}]`, :math:`y = 2u - u^2` 是 :math:`u` 的二次函数,
   在 :math:`u = 1` (即 :math:`x = \dfrac{\pi}{4}`) 处取得最大值 :math:`1`. 端点值 :math:`y(0) = 0`,
   :math:`y\left(\dfrac{\pi}{3}\right) = 2\sqrt{3} - 3 \approx 0.46 > 0`. 故最大值为 :math:`1`
   (在 :math:`x = \dfrac{\pi}{4}` 处), 最小值为 :math:`0` (在 :math:`x = 0` 处).

   (4). :math:`y = |(x+1)(x+2)|`, 零点 :math:`x = -1, -2`. 顶点 :math:`x = -\dfrac{3}{2}` 处
   :math:`y = \dfrac{1}{4}`. 端点值 :math:`y(-3) = |9 - 9 + 2| = 2`, :math:`y(3) = |9 + 9 + 2| = 20`.
   故最大值为 :math:`y(3) = 20`, 最小值为 :math:`0` (在 :math:`x = -1` 与 :math:`x = -2` 处).

   (5). :math:`y' = \dfrac{\ln x}{2\sqrt{x}} + \dfrac{\sqrt{x}}{x} = \dfrac{\ln x + 2}{2\sqrt{x}}`,
   驻点 :math:`x = e^{-2}`. 当 :math:`0 < x < e^{-2}` 时 :math:`y' < 0`, 当 :math:`x > e^{-2}` 时 :math:`y' > 0`,
   故 :math:`x = e^{-2}` 是最小值点,

   .. math::
      y_{\min} = y\left(e^{-2}\right) = e^{-1} \cdot (-2) = -\dfrac{2}{e}.

   又 :math:`x \to +\infty` 时 :math:`y \to +\infty`, 故无最大值.

   (6). :math:`y = (\sin x + \cos x)(1 - \sin x \cos x)`. 令 :math:`s = \sin x + \cos x = \sqrt{2}\sin\left(x + \dfrac{\pi}{4}\right)`,
   当 :math:`x \in \left[-\dfrac{\pi}{4}, \dfrac{3\pi}{4}\right]` 时 :math:`s \in [0, \sqrt{2}]`, 且
   :math:`\sin x \cos x = \dfrac{s^2 - 1}{2}`, 于是

   .. math::
      y = s\left( 1 - \dfrac{s^2-1}{2} \right) = \dfrac{3s - s^3}{2}, \qquad
      \dfrac{\mathrm{d}y}{\mathrm{d}s} = \dfrac{3(1 - s^2)}{2}.

   故 :math:`y` 关于 :math:`s` 在 :math:`[0, 1]` 上增加、在 :math:`[1, \sqrt{2}]` 上减少: 最大值在 :math:`s = 1`
   (即 :math:`x = 0` 或 :math:`x = \dfrac{\pi}{2}`) 处, 为 :math:`1`; 最小值在 :math:`s = 0` (即 :math:`x = -\dfrac{\pi}{4}`
   或 :math:`x = \dfrac{3\pi}{4}`) 处, 为 :math:`0`.

.. _ex-chap4_sec5-ex3:

3. 设 :math:`y = 2x^3 + ax + 3` 在 :math:`x = 1` 处取得极小值, 求 :math:`a` 的值.

.. proof:solution::

   由极值的必要条件, :math:`y'(1) = 0`, 即 :math:`6 + a = 0`, 得 :math:`a = -6`. 此时
   :math:`y'' = 12x`, :math:`y''(1) = 12 > 0`, 确为极小值, 符合题意. 故 :math:`a = -6`
   (此时极小值为 :math:`y(1) = -1`).

.. _ex-chap4_sec5-ex4:

4. 问函数 :math:`f(x) = x^2 - \dfrac{54}{x}` (:math:`x < 0`) 在何处取得最小值?

.. proof:solution::

   :math:`f'(x) = 2x + \dfrac{54}{x^2} = \dfrac{2(x^3 + 27)}{x^2}`, 令 :math:`f'(x) = 0` 得 :math:`x = -3`.
   当 :math:`x < -3` 时 :math:`f'(x) < 0`, 当 :math:`-3 < x < 0` 时 :math:`f'(x) > 0`, 故 :math:`f(x)`
   在 :math:`x = -3` 处取得最小值 (也是唯一极小值) :math:`f(-3) = 9 + 18 = 27`.

.. _ex-chap4_sec5-ex5:

5. 问函数 :math:`f(x) = \dfrac{x}{1 + x^2}` (:math:`x \geqslant 0`) 在何处取得最大值?

.. proof:solution::

   :math:`f'(x) = \dfrac{(1+x^2) - x\cdot 2x}{(1+x^2)^2} = \dfrac{1 - x^2}{(1+x^2)^2}`,
   令 :math:`f'(x) = 0` 得 :math:`x = 1`. 当 :math:`0 \leqslant x < 1` 时 :math:`f'(x) > 0`,
   当 :math:`x > 1` 时 :math:`f'(x) < 0`, 故 :math:`f(x)` 在 :math:`x = 1` 处取得最大值
   :math:`f(1) = \dfrac{1}{2}`.

.. _ex-chap4_sec5-ex6:

6. 讨论二次函数 :math:`f(x) = ax^2 + bx + c` 的最大值与最小值.

.. proof:solution::

   设 :math:`a \neq 0`. :math:`f'(x) = 2ax + b`, 驻点 :math:`x_0 = -\dfrac{b}{2a}`;
   :math:`f''(x) = 2a` 恒定.

   当 :math:`a > 0` 时, :math:`f'' > 0`, :math:`f(x)` 在 :math:`x_0` 处取得最小值

   .. math::
      f\left( -\dfrac{b}{2a} \right) = \dfrac{4ac - b^2}{4a},

   且 :math:`x \to \pm\infty` 时 :math:`f(x) \to +\infty`, 故无最大值.

   当 :math:`a < 0` 时, :math:`f'' < 0`, :math:`f(x)` 在 :math:`x_0` 处取得最大值
   :math:`\dfrac{4ac - b^2}{4a}`, 且无最小值.

   (当 :math:`a = 0` 时, :math:`f(x) = bx + c` 是一次函数: :math:`b \neq 0` 时既无最大值也无最小值;
   :math:`b = 0` 时为常函数, 最大值与最小值都是 :math:`c`.)

.. _ex-chap4_sec5-ex7:

7. 欲做一个底面为长方形的带盖的箱子, 其体积为 :math:`72 \text{ cm}^3`, 其底边宽与长的比为
   :math:`1 : 2`, 问各边的长为多少时, 才能使表面积最小?

.. proof:solution::

   设底面宽为 :math:`x` (cm), 则长为 :math:`2x`, 高为 :math:`h = \dfrac{72}{2x^2} = \dfrac{36}{x^2}`.
   表面积 (有盖)

   .. math::
      S(x) = 2 \cdot 2x^2 + 2 \cdot (x + 2x) h = 4x^2 + \dfrac{216}{x}, \qquad x > 0.

   令 :math:`S'(x) = 8x - \dfrac{216}{x^2} = 0`, 得 :math:`x^3 = 27`, 即 :math:`x = 3`. 由
   :math:`S''(x) = 8 + \dfrac{432}{x^3} > 0` 知 :math:`x = 3` 是最小值点. 此时宽 :math:`3` cm、长 :math:`6` cm、
   高 :math:`\dfrac{36}{9} = 4` cm, 最小表面积 :math:`S = 36 + 72 = 108 \text{ cm}^2`.

.. _ex-chap4_sec5-ex8:

8. 设有一块边长为 :math:`a` 的正方形铁皮, 从四个角截去相同的小方块, 成为一个无盖的方盒子, 问小方块的边长为多少时
   才能使盒子容积最大?

.. proof:solution::

   设截去的小方块边长为 :math:`x` (:math:`0 < x < \dfrac{a}{2}`), 则盒底边长为 :math:`a - 2x`, 容积

   .. math::
      V(x) = x(a - 2x)^2.

   求导

   .. math::
      V'(x) = (a-2x)^2 - 4x(a-2x) = (a-2x)(a-6x),

   令 :math:`V'(x) = 0` 得 :math:`x = \dfrac{a}{6}` (:math:`x = \dfrac{a}{2}` 舍去). 当
   :math:`0 < x < \dfrac{a}{6}` 时 :math:`V'(x) > 0`, 当 :math:`\dfrac{a}{6} < x < \dfrac{a}{2}` 时
   :math:`V'(x) < 0`, 故 :math:`x = \dfrac{a}{6}` 时容积最大, 最大容积

   .. math::
      V = \dfrac{a}{6}\left( a - \dfrac{a}{3} \right)^2 = \dfrac{2a^3}{27}.

   即小方块边长为 :math:`\dfrac{a}{6}` 时盒子容积最大.

.. _ex-chap4_sec5-ex9:

9. 制作一个上、下均有底的圆柱形容器, 要求容积为定值 :math:`V`. 问底半径 :math:`r` 为多大时, 容器的表面积最小?
   并求此最小面积.

.. proof:solution::

   设容器高为 :math:`h`, 由容积 :math:`\pi r^2 h = V` 得 :math:`h = \dfrac{V}{\pi r^2}`. 表面积 (上、下底
   均计入)

   .. math::
      S(r) = 2\pi r^2 + 2\pi r h = 2\pi r^2 + \dfrac{2V}{r}, \qquad r > 0.

   令 :math:`S'(r) = 4\pi r - \dfrac{2V}{r^2} = 0`, 得 :math:`r^3 = \dfrac{V}{2\pi}`, 即
   :math:`r = \sqrt[3]{\dfrac{V}{2\pi}}`. 由 :math:`S''(r) = 4\pi + \dfrac{4V}{r^3} > 0` 知这是最小值点.
   此时 :math:`h = \dfrac{V}{\pi r^2} = 2r`, 最小表面积

   .. math::
      S_{\min} = 2\pi r^2 + \dfrac{2V}{r} = 2\pi r^2 + 4\pi r^2 = 6\pi r^2
      = 6\pi \left( \dfrac{V}{2\pi} \right)^{\frac{2}{3}} = 3\sqrt[3]{2\pi V^2}.

.. _ex-chap4_sec5-ex10:

10. 某仓储设备的库存费与生产准备费之和 :math:`P(x)` 是每批产量 :math:`x` 的函数, 即

    .. math::
       P(x) = \dfrac{ab}{x} + \dfrac{c}{2} x \quad \left[ x \in (0, a) \right],

    其中 :math:`a` 为年产量, :math:`b` 为每批批次的生产准备费, :math:`c` 为每件产品的库存费. 问在生产能力足够大的
    条件下, 每批生产多少件产品时, :math:`P(x)` 最小?

.. proof:solution::

   令 :math:`P'(x) = -\dfrac{ab}{x^2} + \dfrac{c}{2} = 0`, 得 :math:`x^2 = \dfrac{2ab}{c}`, 即
   :math:`x = \sqrt{\dfrac{2ab}{c}}`. 由 :math:`P''(x) = \dfrac{2ab}{x^3} > 0` 知这是最小值点. 故每批生产
   :math:`\sqrt{\dfrac{2ab}{c}}` 件产品时, :math:`P(x)` 最小 (此时最小值为 :math:`\sqrt{2abc}`).

.. _ex-chap4_sec6:

§4.6 函数的凹凸性
------------------------------------

.. _ex-chap4_sec6-ex1:

1. 证明函数 :math:`f(x) = ax^2 + bx + c` 是凸函数, 其中 :math:`a, b, c` 是实数, 且 :math:`a > 0`.

.. proof:solution::

   任取 :math:`x_1 \neq x_2` 与 :math:`0 < t < 1`, 记 :math:`x = t x_1 + (1-t) x_2`. 直接计算

   .. math::
      t f(x_1) + (1-t) f(x_2) - f(x)
      = a t(1-t) (x_1 - x_2)^2 \geqslant 0,

   即 :math:`f\left( t x_1 + (1-t) x_2 \right) \leqslant t f(x_1) + (1-t) f(x_2)`, 故 :math:`f(x)` 是凸函数
   (也可由 :math:`f''(x) = 2a > 0` 直接得到).

.. _ex-chap4_sec6-ex2:

2. 已知函数 :math:`g(x) = 4x^4 - 3x^3 + 2x^2`, 计算其二阶导数, 并证明 :math:`g(x)` 是凸函数.

.. proof:solution::

   .. math::
      g'(x) = 16x^3 - 9x^2 + 4x, \qquad g''(x) = 48x^2 - 18x + 4.

   :math:`g''(x)` 的判别式 :math:`\Delta = (-18)^2 - 4 \times 48 \times 4 = 324 - 768 = -444 < 0`,
   且开口向上, 故对一切 :math:`x` 有 :math:`g''(x) > 0` (例如 :math:`g''(0) = 4 > 0`), 因此 :math:`g(x)`
   在 :math:`\mathbb{R}` 上是凸函数.

.. _ex-chap4_sec6-ex3:

3. 如果 :math:`f(x)` 和 :math:`g(x)` 是两个凸函数, 证明对于任意的 :math:`\alpha, \beta \geqslant 0`, 函数
   :math:`h(x) = \alpha f(x) + \beta g(x)` 也是凸函数.

.. proof:solution::

   任取 :math:`x_1, x_2` 与 :math:`0 \leqslant t \leqslant 1`. 由 :math:`f, g` 是凸函数,

   .. math::
      f\left( t x_1 + (1-t) x_2 \right) \leqslant t f(x_1) + (1-t) f(x_2), \qquad
      g\left( t x_1 + (1-t) x_2 \right) \leqslant t g(x_1) + (1-t) g(x_2).

   两式分别乘 :math:`\alpha, \beta \geqslant 0` 后相加:

   .. math::
      h\left( t x_1 + (1-t) x_2 \right)
      \leqslant \alpha \left[ t f(x_1) + (1-t) f(x_2) \right] + \beta \left[ t g(x_1) + (1-t) g(x_2) \right]
      = t h(x_1) + (1-t) h(x_2),

   故 :math:`h(x)` 是凸函数.

.. _ex-chap4_sec6-ex4:

4. 如果 :math:`f(x)` 和 :math:`g(x)` 是两个凸函数, 请问 :math:`f[g(x)]` 是否也是凸函数?

.. proof:solution::

   不一定. 反例: 取 :math:`f(x) = e^{-x}` 与 :math:`g(x) = x^2`, 两者都是凸函数
   (:math:`f''(x) = e^{-x} > 0`, :math:`g''(x) = 2 > 0`), 但复合函数

   .. math::
      f[g(x)] = e^{-x^2}, \qquad \left( e^{-x^2} \right)'' = (4x^2 - 2) e^{-x^2},

   在 :math:`x = 0` 处为 :math:`-2 < 0`, 故 :math:`e^{-x^2}` 在 :math:`0` 附近不是凸函数
   (它在 :math:`|x| < \frac{1}{\sqrt{2}}` 上是凹的).

   事实上, 只有当外层函数 :math:`f` 是凸函数且单调不减时, 才能保证 :math:`f[g(x)]` 是凸函数.

.. _ex-chap4_sec6-ex5:

5. 利用 :math:`\ln(x)` 的凹凸性证明下面的不等式.

   (1) 算术平均-几何平均不等式: :math:`x_1, x_2, \cdots, x_n > 0`, 有

       .. math::
          \dfrac{x_1 + x_2 + \cdots + x_n}{n} \geqslant \sqrt[n]{x_1 \cdot x_2 \cdots x_n},

       当且仅当所有 :math:`x_i` 相等时等号成立.

   (2) 对数函数的上界: 当 :math:`x > 0` 时有 :math:`\ln(x) \leqslant x - 1`.

.. proof:solution::

   (1). :math:`(\ln x)'' = -\dfrac{1}{x^2} < 0` (:math:`x > 0`), 故 :math:`\ln x` 在 :math:`(0, +\infty)` 上是
   严格凹函数. 由凹函数的 Jensen 不等式,

   .. math::
      \ln\dfrac{x_1 + x_2 + \cdots + x_n}{n}
      \geqslant \dfrac{\ln x_1 + \ln x_2 + \cdots + \ln x_n}{n}
      = \ln\sqrt[n]{x_1 x_2 \cdots x_n},

   再由 :math:`\ln` 单调递增, 得

   .. math::
      \dfrac{x_1 + x_2 + \cdots + x_n}{n} \geqslant \sqrt[n]{x_1 x_2 \cdots x_n}.

   由于 :math:`\ln x` 严格凹, 等号成立当且仅当 :math:`x_1 = x_2 = \cdots = x_n`.

   (2). :math:`\ln x` 是凹函数, 凹函数的图像位于其任一条切线的下方. :math:`\ln x` 在 :math:`x = 1` 处的切线为
   :math:`y = x - 1`, 故对一切 :math:`x > 0` 有 :math:`\ln x \leqslant x - 1`
   (也可令 :math:`g(x) = x - 1 - \ln x`, 由 :math:`g'(x) = 1 - \frac{1}{x}` 知 :math:`g` 在 :math:`x = 1`
   处取最小值 :math:`g(1) = 0`).

.. _ex-chap4_sec6-ex6:

6. 求出下列函数的渐近线.

   (1) :math:`y = \dfrac{x + 1}{x}`; \qquad
   (2) :math:`y = \dfrac{x^3}{x^2 + 2x - 3}`; \qquad
   (3) :math:`y = \dfrac{1}{1 + e^x}`.

.. proof:solution::

   (1). :math:`y = 1 + \dfrac{1}{x}`: :math:`x \to \infty` 时 :math:`y \to 1`, 有水平渐近线 :math:`y = 1`;
   :math:`x \to 0` 时 :math:`y \to \infty`, 有垂直渐近线 :math:`x = 0`. 无斜渐近线.

   (2). 分母 :math:`x^2 + 2x - 3 = (x+3)(x-1)`, 在 :math:`x = -3` 与 :math:`x = 1` 处 :math:`y \to \infty`,
   故有垂直渐近线 :math:`x = -3` 与 :math:`x = 1`. 又

   .. math::
      y = \dfrac{x^3}{x^2+2x-3} = x - 2 + \dfrac{7x-6}{x^2+2x-3},

   当 :math:`x \to \infty` 时最后一项 :math:`\to 0`, 故有斜渐近线 :math:`y = x - 2`. 无水平渐近线.

   (3). :math:`1 + e^x > 0` 处处成立, 无垂直渐近线. :math:`x \to +\infty` 时 :math:`y \to 0`,
   有水平渐近线 :math:`y = 0`; :math:`x \to -\infty` 时 :math:`y \to 1`, 有水平渐近线 :math:`y = 1`.
   无斜渐近线.

.. _ex-chap4_sec7:

§4.7 函数作图
------------------------------------

.. _ex-chap4_sec7-ex1:

1. 绘制函数 :math:`f(x) = x^3 - x^2 - x + 1` 的图像.

.. proof:solution::

   (1) 定义域为 :math:`\mathbb{R}`; :math:`f(x) = (x-1)^2(x+1)`, 零点 :math:`x = -1` 与 :math:`x = 1`
   (二重), :math:`y` 轴截距 :math:`f(0) = 1`.

   (2) :math:`f'(x) = 3x^2 - 2x - 1 = (3x+1)(x-1)`, 驻点 :math:`x = -\dfrac{1}{3}, 1`. 当
   :math:`x < -\dfrac{1}{3}` 或 :math:`x > 1` 时 :math:`f' > 0` (增加), 当 :math:`-\dfrac{1}{3} < x < 1` 时
   :math:`f' < 0` (减少). 极大值 :math:`f\left(-\dfrac{1}{3}\right) = \dfrac{32}{27}`, 极小值 :math:`f(1) = 0`.

   (3) :math:`f''(x) = 6x - 2`, :math:`x = \dfrac{1}{3}` 两侧凹凸性改变, 拐点
   :math:`\left( \dfrac{1}{3}, \dfrac{16}{27} \right)`; :math:`x < \dfrac{1}{3}` 时凸 (向上凸),
   :math:`x > \dfrac{1}{3}` 时凹 (向下凸).

   (4) 无渐近线. 按上述要点描点作图: 曲线过 :math:`(-1, 0)`, 上升到极大值点
   :math:`\left( -\frac{1}{3}, \frac{32}{27} \right)`, 下降过拐点与极小值点 :math:`(1, 0)`,
   随后上升趋于 :math:`+\infty`.

.. _ex-chap4_sec7-ex2:

2. 绘制函数 :math:`f(x) = \dfrac{\cos x}{\cos 2x}` 的图像.

.. proof:solution::

   (1) 定义域为 :math:`\cos 2x \neq 0`, 即 :math:`x \neq \dfrac{\pi}{4} + \dfrac{k\pi}{2}` (:math:`k \in \mathbb{Z}`);
   在 :math:`x = \dfrac{\pi}{4} + \dfrac{k\pi}{2}` 处有垂直渐近线. :math:`f(-x) = f(x)` 是偶函数;
   :math:`f(x + 2\pi) = f(x)`, 以 :math:`2\pi` 为周期, 故只需讨论 :math:`[0, \pi]` 并利用偶性.

   (2) :math:`f'(x) = \dfrac{-\sin x \cos 2x + 2\cos x \sin 2x}{\cos^2 2x} = \dfrac{\sin x (2\cos^2 x + 1)}{\cos^2 2x}`,
   其符号由 :math:`\sin x` 决定: 在 :math:`(0, \pi)` 内各连续段上 :math:`f' > 0`, 即单调增加
   (在 :math:`(-\pi, 0)` 内各段上单调减少).

   (3) 特征值: :math:`f(0) = 1`, :math:`f\left(\dfrac{\pi}{2}\right) = 0`, :math:`f(\pi) = -1`;
   :math:`x \to \dfrac{\pi}{4}^-` 时 :math:`f \to +\infty`, :math:`x \to \dfrac{\pi}{4}^+` 时 :math:`f \to -\infty`.

   (4) 无水平与斜渐近线. 综上: 在 :math:`\left(0, \dfrac{\pi}{4}\right)` 上从 :math:`1` 增至 :math:`+\infty`;
   在 :math:`\left(\dfrac{\pi}{4}, \dfrac{\pi}{2}\right)` 上从 :math:`-\infty` 增至 :math:`0`;
   在 :math:`\left(\dfrac{\pi}{2}, \dfrac{3\pi}{4}\right)` 上从 :math:`0` 增至 :math:`+\infty`;
   在 :math:`\left(\dfrac{3\pi}{4}, \pi\right)` 上从 :math:`-\infty` 增至 :math:`-1`; 再由偶性与周期性对称延拓.

.. _ex-chap4_sec7-ex3:

3. 绘制椭圆 :math:`x^2 - xy + y^2 = 3` 的图像.

.. proof:solution::

   作旋转变换消去交叉项. 令

   .. math::
      u = \dfrac{x - y}{\sqrt{2}}, \qquad v = \dfrac{x + y}{\sqrt{2}}
      \qquad \left( \text{即} ~ x = \dfrac{u+v}{\sqrt{2}}, ~ y = \dfrac{v-u}{\sqrt{2}} \right),

   直接计算得 :math:`x^2 - xy + y^2 = \dfrac{3}{2}u^2 + \dfrac{1}{2}v^2`, 于是方程化为

   .. math::
      \dfrac{u^2}{2} + \dfrac{v^2}{6} = 1.

   这是标准椭圆: 中心在原点, 长轴沿 :math:`v` 方向 (即直线 :math:`y = x`), 半长轴 :math:`\sqrt{6}`;
   短轴沿 :math:`u` 方向 (即直线 :math:`y = -x`), 半短轴 :math:`\sqrt{2}`. 四个顶点为
   :math:`(\sqrt{3}, \sqrt{3})`, :math:`(-\sqrt{3}, -\sqrt{3})`, :math:`(1, -1)`, :math:`(-1, 1)`.
   按此描点即可作出椭圆图像.

.. _ex-chap4_sec7-ex4:

4. (探究光合作用与光照强度) 植物的光合作用速率 :math:`R(I)` (单位: 摩尔葡萄糖/:math:`\text{m}^2 \cdot \text{s}`)
   与光照强度 :math:`I` (单位: 摩尔光子/:math:`\text{m}^2 \cdot \text{s}`) 的关系可以用函数
   :math:`R(I) = \dfrac{aI}{b + I}` 来描述, 其中 :math:`a` 和 :math:`b` 是正常数. 绘制 :math:`R(I)` 的函数图像,
   并选择合适的 :math:`a` 值和 :math:`b` 值来模拟实际的光合作用情况. 解释图像的饱和点代表什么, 并计算光照强度达到
   饱和点一半时光合作用速率. 讨论如何通过图像来估计植物在不同光照强度下的光合作用效率.

.. proof:solution::

   (1) 图像特征 (:math:`I \geqslant 0`): :math:`R(0) = 0`; :math:`R'(I) = \dfrac{ab}{(b+I)^2} > 0`
   单调增加; :math:`R''(I) = -\dfrac{2ab}{(b+I)^3} < 0` 向上凸 (图形上升越来越慢); 当 :math:`I \to +\infty` 时
   :math:`R(I) \to a`, 即有水平渐近线 :math:`R = a` (饱和值).

   (2) 模拟取值: 例如取 :math:`a = 10`, :math:`b = 5`, 则 :math:`R(I) = \dfrac{10I}{5+I}`: 弱光下速率近似
   线性增长 (斜率 :math:`R'(0) = a/b = 2`), 强光下趋于 :math:`10`.

   (3) 饱和点: 水平渐近线 :math:`R = a` 表示光合作用速率的最大潜力 (光饱和现象)——光照再强, 速率也不再超过
   :math:`a`, 此时限制因素不再是光照 (如二氧化碳浓度、酶活性等成为瓶颈). "光饱和点的一半"对应
   :math:`R = \dfrac{a}{2}`, 代入 :math:`\dfrac{aI}{b+I} = \dfrac{a}{2}` 解得 :math:`I = b`, 此时
   光合作用速率为 :math:`\dfrac{a}{2}`, 即最大速率的一半. :math:`b` 称为半饱和常数.

   (4) 效率估计: 由图像读取不同 :math:`I` 对应的 :math:`R(I)`, 比值 :math:`R(I)/I` 即光能利用效率;
   低光强下效率接近初始斜率 :math:`a/b`, 随光照增强效率递减 (:math:`R(I)/I = \dfrac{a}{b+I} \downarrow 0`).
   通过实测若干 :math:`(I, R)` 数据点拟合参数 :math:`a` (饱和速率) 与 :math:`b` (半饱和光照),
   即可由该模型估计任意光照强度下的光合作用效率.

.. _ex-chap4_sec7-ex5:

5. 绘制函数 :math:`g(x) = \dfrac{x^2 + 1}{x - 1}` 的图像, 并讨论其渐近行为. 如果存在的话, 找出函数的垂直渐近线,
   水平渐近线和斜渐近线.

.. note::
   本题原来误录在 :ref:`§4.5 <ex-chap4_sec5>` 之下, 现按教材归位到本节.

.. proof:solution::

   :math:`x = 1` 为奇点, 由于

   .. math::
      \lim_{x \to 1^-} f(x) = -\infty, \quad \lim_{x \to 1^+} f(x) = +\infty,

   故 :math:`x = 1` 为垂直渐近线.

   计算水平渐近线、斜渐近线 :math:`y = kx + b`:

   .. math::
      k & = \lim_{x \to \infty} \dfrac{f(x)}{x} = \lim_{x \to \infty} \dfrac{x^2+1}{x(x-1)} = 1, \\
      b & = \lim_{x \to \infty} \left( f(x) - kx \right) = \lim_{x \to \infty} \left( \dfrac{x^2+1}{x-1} - x \right) = \lim_{x \to \infty} \dfrac{x+1}{x-1} = 1,

   故有斜渐近线 :math:`y = x + 1`.

   .. tikz:: 函数 :math:`\displaystyle f(x) = \dfrac{x^2+1}{x-1}` 的图像
      :align: center
      :xscale: 70

      \begin{axis}[
         width=8cm, height=10cm, axis lines=middle,
         xlabel=$x$, ylabel=$y$,
         smooth, samples=200, minor tick num=4,
         xmin=-5, xmax=7, ymin=-30, ymax=30,
      ]
      \addplot[thick, cyan, domain=-5:0.99] {(\x^2+1)/(\x-1)};
      \addplot[thick, cyan, domain=1.01:7] {(\x^2+1)/(\x-1)};
      \addplot[dashed, red, domain=-5:7] {\x + 1};
      \addplot[dashed, red, domain=-30:30, variable=\y] ({1}, {\y});
      \end{axis}

.. _ex-chap4-zong:

总习题 4
------------------------------------

.. _ex-chap4-zong-ex1:

1. 用洛必达法则求极限.

   (1) :math:`\lim\limits_{x \to 0} \dfrac{e^x - e^{-x}}{\sin x}`; \qquad
   (2) :math:`\lim\limits_{x \to 0} \dfrac{\tan x - x}{x^3}`; \qquad
   (3) :math:`\lim\limits_{x \to 0} \dfrac{\ln \cos x}{x^2}`;

   (4) :math:`\lim\limits_{x \to 0} \dfrac{a^x - 1}{3x}` (:math:`a > 0` 且 :math:`a \neq 1`); \qquad
   (5) :math:`\lim\limits_{x \to \infty} \left[ x^2 \ln \left( 1 + \dfrac{1}{x} \right) - x \right]`.

.. proof:solution::

   (1). :math:`\dfrac{0}{0}` 型,

   .. math::
      \lim_{x \to 0} \dfrac{e^x - e^{-x}}{\sin x} = \lim_{x \to 0} \dfrac{e^x + e^{-x}}{\cos x} = 2.

   (2). :math:`\dfrac{0}{0}` 型,

   .. math::
      \lim_{x \to 0} \dfrac{\tan x - x}{x^3} = \lim_{x \to 0} \dfrac{\sec^2 x - 1}{3x^2}
      = \lim_{x \to 0} \dfrac{\tan^2 x}{3x^2} = \dfrac{1}{3}.

   (3). :math:`\dfrac{0}{0}` 型, 由 :ref:`§4.3 题8 <ex-chap4_sec3-ex8>` 的展开 (或直接用洛必达法则),

   .. math::
      \lim_{x \to 0} \dfrac{\ln \cos x}{x^2} = \lim_{x \to 0} \dfrac{-\frac{1}{2}x^2}{x^2} = -\dfrac{1}{2}.

   (4). :math:`\dfrac{0}{0}` 型,

   .. math::
      \lim_{x \to 0} \dfrac{a^x - 1}{3x} = \lim_{x \to 0} \dfrac{a^x \ln a}{3} = \dfrac{\ln a}{3}.

   (5). 令 :math:`t = \dfrac{1}{x}`, 则 :math:`t \to 0^+`, 且

   .. math::
      x^2 \ln\left( 1 + \dfrac{1}{x} \right) - x = \dfrac{\ln(1+t) - t}{t^2},

   这是 :math:`\dfrac{0}{0}` 型, 用洛必达法则,

   .. math::
      \lim_{t \to 0^+} \dfrac{\ln(1+t) - t}{t^2} = \lim_{t \to 0^+} \dfrac{\frac{1}{1+t} - 1}{2t}
      = \lim_{t \to 0^+} \dfrac{-t}{2t(1+t)} = -\dfrac{1}{2}.

.. _ex-chap4-zong-ex2:

2. 计算函数 :math:`y = e^x` 在 :math:`x = 0` 点的泰勒公式.

.. proof:solution::

   :math:`f^{(k)}(x) = e^x`, 故 :math:`f^{(k)}(0) = 1` 对一切 :math:`k` 成立. 带有皮亚诺余项的 :math:`n`
   阶泰勒公式为

   .. math::
      e^x = 1 + x + \dfrac{x^2}{2!} + \cdots + \dfrac{x^n}{n!} + o(x^n);

   带有拉格朗日余项的形式为

   .. math::
      e^x = 1 + x + \dfrac{x^2}{2!} + \cdots + \dfrac{x^n}{n!} + \dfrac{e^{\xi}}{(n+1)!} x^{n+1}
      \quad (\xi ~ \text{介于} ~ 0 ~ \text{与} ~ x ~ \text{之间}).

.. _ex-chap4-zong-ex3:

3. 证明当 :math:`x > 0` 时, :math:`\dfrac{x}{1 + x^2} < \arctan x < x`.

.. proof:solution::

   先证右边: 令 :math:`h(x) = x - \arctan x`, 则 :math:`h'(x) = 1 - \dfrac{1}{1+x^2} = \dfrac{x^2}{1+x^2} > 0`
   (:math:`x > 0`), 故 :math:`h` 在 :math:`[0, +\infty)` 上单调增加, 又 :math:`h(0) = 0`, 所以 :math:`h(x) > 0`,
   即 :math:`\arctan x < x`.

   再证左边: 令 :math:`g(x) = \arctan x - \dfrac{x}{1+x^2}`, 则

   .. math::
      g'(x) = \dfrac{1}{1+x^2} - \dfrac{(1+x^2) - x \cdot 2x}{(1+x^2)^2}
      = \dfrac{(1+x^2) - (1 - x^2)}{(1+x^2)^2} = \dfrac{2x^2}{(1+x^2)^2} > 0,

   故 :math:`g` 在 :math:`[0, +\infty)` 上单调增加, 又 :math:`g(0) = 0`, 所以 :math:`g(x) > 0`, 即
   :math:`\arctan x > \dfrac{x}{1+x^2}`. 综上, 当 :math:`x > 0` 时不等式成立.

.. _ex-chap4-zong-ex4:

4. 设奇函数 :math:`f(x)` 在 :math:`[0, 1]` 上连续, 在 :math:`(0, 1)` 内可导, 且 :math:`f(1) = 1`, 证明: 存在
   :math:`\xi \in (0, 1)`, 使得 :math:`f'(\xi) = 1`.

.. proof:solution::

   由 :math:`f(x)` 是奇函数得 :math:`f(0) = -f(0)`, 即 :math:`f(0) = 0`.

   作辅助函数 :math:`g(x) = f(x) - x`, 则 :math:`g(x)` 在 :math:`[0, 1]` 上连续, 在 :math:`(0, 1)` 内可导, 且

   .. math::
      g(0) = f(0) - 0 = 0, \qquad g(1) = f(1) - 1 = 0.

   由罗尔中值定理, 存在 :math:`\xi \in (0, 1)`, 使得 :math:`g'(\xi) = 0`, 即 :math:`f'(\xi) = 1`.

.. _ex-chap4-zong-ex5:

5. 证明: 当 :math:`x > 0` 时, :math:`\ln(1 + x) > \dfrac{\arctan x}{1 + x}`.

.. proof:solution::

   由于 :math:`1 + x > 0`, 只需证 :math:`(1+x)\ln(1+x) > \arctan x`. 作辅助函数

   .. math::
      g(x) = (1+x)\ln(1+x) - \arctan x, \qquad x \geqslant 0.

   则 :math:`g(0) = 0`, 且

   .. math::
      g'(x) = \ln(1+x) + 1 - \dfrac{1}{1+x^2}.

   当 :math:`x > 0` 时, :math:`\ln(1+x) > 0` 且 :math:`1 - \dfrac{1}{1+x^2} = \dfrac{x^2}{1+x^2} > 0`,
   故 :math:`g'(x) > 0`, :math:`g(x)` 严格单调增加, 从而 :math:`g(x) > g(0) = 0`. 即

   .. math::
      (1+x)\ln(1+x) > \arctan x, \qquad \text{亦即} ~ \ln(1+x) > \dfrac{\arctan x}{1+x}.

.. _ex-chap4-zong-ex6:

6. 求函数 :math:`f(x) = 4x^2 (1 - x)^2` 在 :math:`[0, 1]` 上的最大值与最小值.

.. proof:solution::

   :math:`f(x) = [2x(1-x)]^2 \geqslant 0`, 且 :math:`f(0) = f(1) = 0`, 故最小值为 :math:`0`
   (在 :math:`x = 0, 1` 处). 求导

   .. math::
      f'(x) = 8x(1-x)^2 - 8x^2(1-x) = 8x(1-x)(1-2x),

   在 :math:`(0, 1)` 内驻点 :math:`x = \dfrac{1}{2}`, 此时 :math:`f\left(\dfrac{1}{2}\right) = 4 \cdot \dfrac{1}{4} \cdot \dfrac{1}{4} = \dfrac{1}{4}`.
   故最大值为 :math:`\dfrac{1}{2}` 的平方 :math:`\dfrac{1}{4}` (在 :math:`x = \dfrac{1}{2}` 处), 最小值为 :math:`0`.

.. _ex-chap4-zong-ex7:

7. 求函数 :math:`y = \dfrac{(\ln x)^2}{x}` 的极值.

.. proof:solution::

   定义域 :math:`x > 0`. :math:`y' = \dfrac{2\ln x \cdot \frac{1}{x} \cdot x - \ln^2 x}{x^2} = \dfrac{\ln x (2 - \ln x)}{x^2}`.

   令 :math:`y' = 0` 得 :math:`x = 1` 或 :math:`x = e^2`. 符号分析: :math:`0 < x < 1` 时 :math:`y' < 0`;
   :math:`1 < x < e^2` 时 :math:`y' > 0`; :math:`x > e^2` 时 :math:`y' < 0`. 故

   .. math::
      \text{极小值} ~ y(1) = 0, \qquad \text{极大值} ~ y(e^2) = \dfrac{4}{e^2}.

.. _ex-chap4-zong-ex8:

8. 设 :math:`a > 0` 为常数, :math:`f(x) = \ln x - \dfrac{x}{e} + a`, 问方程 :math:`f(x) = 0` 有几个实数根?

.. proof:solution::

   定义域 :math:`x > 0`. :math:`f'(x) = \dfrac{1}{x} - \dfrac{1}{e}`, 令 :math:`f'(x) = 0` 得唯一驻点
   :math:`x = e`; 当 :math:`0 < x < e` 时 :math:`f' > 0` (增加), 当 :math:`x > e` 时 :math:`f' < 0` (减少),
   故 :math:`f(e) = 1 - 1 + a = a` 是 :math:`f` 的最大值. 又 :math:`x \to 0^+` 时 :math:`f(x) \to -\infty`,
   :math:`x \to +\infty` 时 :math:`f(x) \to -\infty`, 曲线两端都趋于 :math:`-\infty`.

   于是, 对题设的 :math:`a > 0`: 最大值 :math:`f(e) = a > 0`, 且 :math:`f` 在 :math:`(0, e)` 与
   :math:`(e, +\infty)` 上分别严格单调、两端趋于 :math:`-\infty`. 由零点存在定理与单调性, 方程在
   :math:`(0, e)` 与 :math:`(e, +\infty)` 内各恰有一个实数根, 故方程恰有 :math:`2` 个实数根.

.. _ex-chap4-zong-ex9:

9. 讨论 :math:`y = x^3 - 3x^2 - 1` 的单调性、凸凹性、极值及拐点.

.. proof:solution::

   定义域为 :math:`\mathbb{R}`. :math:`y' = 3x^2 - 6x = 3x(x-2)`, :math:`y'' = 6x - 6 = 6(x-1)`.

   单调性与极值: 当 :math:`x < 0` 或 :math:`x > 2` 时 :math:`y' > 0` (增加), 当 :math:`0 < x < 2` 时
   :math:`y' < 0` (减少). 故极大值 :math:`y(0) = -1`, 极小值 :math:`y(2) = -5`.

   凹凸性与拐点: 当 :math:`x < 1` 时 :math:`y'' < 0`, 图形向上凸; 当 :math:`x > 1` 时 :math:`y'' > 0`,
   图形向下凸; :math:`x = 1` 处两侧凹凸性改变, 拐点为 :math:`(1, -3)`.

.. _ex-chap4-zong-ex10:

10. 求函数 :math:`y = \ln(1 + x^2)` 的图形的凹凸区间及拐点.

.. proof:solution::

   定义域为 :math:`\mathbb{R}`. :math:`y' = \dfrac{2x}{1+x^2}`,

   .. math::
      y'' = \dfrac{2(1+x^2) - 2x \cdot 2x}{(1+x^2)^2} = \dfrac{2(1 - x^2)}{(1+x^2)^2}.

   当 :math:`|x| < 1` 时 :math:`y'' > 0`, 图形向下凸; 当 :math:`|x| > 1` 时 :math:`y'' < 0`,
   图形向上凸. 在 :math:`x = \pm 1` 处凹凸性改变, 拐点为 :math:`\left(1, \ln 2\right)` 与
   :math:`\left(-1, \ln 2\right)`.

.. _ex-chap4-zong-ex11:

11. 确定函数 :math:`y = \dfrac{(x - 2)(3 - x)}{x^2}` 的单调区间, 并求其在区间 :math:`[1, 3]` 上的最值.

.. proof:solution::

   化简 :math:`y = \dfrac{-x^2 + 5x - 6}{x^2} = -1 + \dfrac{5}{x} - \dfrac{6}{x^2}` (:math:`x \neq 0`). 求导

   .. math::
      y' = -\dfrac{5}{x^2} + \dfrac{12}{x^3} = \dfrac{12 - 5x}{x^3}.

   令 :math:`y' = 0` 得 :math:`x = \dfrac{12}{5}`. 符号分析: :math:`x < 0` 时 :math:`y' > 0`;
   :math:`0 < x < \dfrac{12}{5}` 时 :math:`y' > 0`; :math:`x > \dfrac{12}{5}` 时 :math:`y' < 0`. 故单调增加区间为
   :math:`(-\infty, 0)` 与 :math:`\left(0, \dfrac{12}{5}\right]`, 单调减少区间为
   :math:`\left[\dfrac{12}{5}, +\infty\right)`.

   在 :math:`[1, 3]` 上: :math:`y(1) = \dfrac{(-1)\times 2}{1} = -2`, :math:`y\left(\dfrac{12}{5}\right) = \dfrac{\frac{2}{5}\cdot\frac{3}{5}}{\frac{144}{25}} = \dfrac{1}{24}`,
   :math:`y(3) = 0`. 由单调性 (增至 :math:`\dfrac{12}{5}` 再减少), 最大值为 :math:`\dfrac{1}{24}`
   (在 :math:`x = \dfrac{12}{5}` 处), 最小值为 :math:`-2` (在 :math:`x = 1` 处).

.. _ex-chap4-zong-ex12:

12. 设函数 :math:`f(x)` 和 :math:`g(x)` 在 :math:`[a, b]` 上可导, 且 :math:`f(a) = g(b)`, :math:`f(b) = g(a)`,
    :math:`g(x) g'(x) \neq 0`, 试证: 在开区间 :math:`(a, b)` 内至少存在一点 :math:`\xi`, 使
    :math:`\dfrac{f(\xi)}{g(\xi)} = -\dfrac{f'(\xi)}{g'(\xi)}`.

.. proof:solution::

   要证的等式等价于 :math:`f'(\xi)g(\xi) + f(\xi)g'(\xi) = 0`, 即 :math:`\left[ f(x)g(x) \right]' \big|_{x=\xi} = 0`.
   故作辅助函数 :math:`h(x) = f(x)g(x)`, 则 :math:`h(x)` 在 :math:`[a, b]` 上可导 (因而连续), 且

   .. math::
      h(a) = f(a)g(a) = g(b)g(a) = g(a)g(b) = f(b)g(b) = h(b),

   其中用到条件 :math:`f(a) = g(b)` 与 :math:`f(b) = g(a)`. 由罗尔中值定理, 存在 :math:`\xi \in (a, b)`,
   使得

   .. math::
      h'(\xi) = f'(\xi)g(\xi) + f(\xi)g'(\xi) = 0.

   由 :math:`g(\xi)g'(\xi) \neq 0`, 两边除以 :math:`g(\xi)g'(\xi)` 即得

   .. math::
      \dfrac{f(\xi)}{g(\xi)} = -\dfrac{f'(\xi)}{g'(\xi)}.

.. _extra-chap4:

补充内容
====================================

.. _extra-chap4-sec1:

§4.1 微分中值定理
--------------------------------

.. _extra-chap4-sec1-topic1:

1. 设函数 :math:`f(x)` 在区间 :math:`[a, b]` 上二阶可导, 且 :math:`f(0) = f(1)`, 证明存在 :math:`\xi \in (0, 1)`
   使得 :math:`f''(\xi) = \dfrac{2f'(\xi)}{1-\xi}`.

.. proof:proof::

   令

   .. math::
      F(x) = (x - 1)^2 f'(x),

   那么 :math:`F(1) = 0`. 由于 :math:`f(0) = f(1)`, 由罗尔定理知存在 :math:`c \in (0, 1)` 使得 :math:`f'(c) = 0`,
   从而有 :math:`F(c) = (c - 1)^2 f'(c) = 0`. 那么函数 :math:`F(x)` 就是 :math:`[c, 1]` 上连续, :math:`(c, 1)` 上可导的函数,
   并且满足 :math:`F(c) = F(1) = 0`. 再一次利用罗尔定理知, 存在 :math:`\xi \in (c, 1) \subset (0, 1)`, 使得

   .. math::
      0 = F'(\xi) = 2(\xi - 1) f'(\xi) + (\xi - 1)^2 f''(\xi),

   移项得 :math:`f''(\xi) = \dfrac{2f'(\xi)}{1-\xi}`.

.. _extra-chap4-sec2:

§4.2 洛必达法则
--------------------------------

.. _extra-chap4-sec2-topic1:

1. :math:`\dfrac{\infty}{\infty}` 型未定式的洛必达法则证明:

.. proof:proof::

   由于有 :math:`\lim\limits_{x \to x_0} = f(x) = \lim\limits_{x \to x_0} = g(x) = \infty`, 所以可以假定在 :math:`x_0` 的某个小的去心邻域
   :math:`\mathring{U}(x_0, \delta)` 内有 :math:`f(x) \neq 0, g(x) \neq 0`. 对于包含于 :math:`\mathring{U}(x_0, \delta)`
   且在 :math:`x_0` 某一边 (不妨设为右边) 的区间 :math:`[x, y]`, 在其上用柯西中值定理有

   .. math::
      & \dfrac{f(x) - f(y)}{g(x) - g(y)} = \dfrac{f'(\xi)}{g'(\xi)}, \quad \xi \in (x, y) \\
      \implies & f(x) g'(\xi) = f(y)g'(\xi) + (g(x) - g(y)) f'(\xi) \\
      \implies & \dfrac{f(x)}{g(x)} = \dfrac{f(y)}{g(x)} + \left( 1 - \dfrac{g(y)}{g(x)} \right) \dfrac{f'(\xi)}{g'(\xi)}.

   那么由于 :math:`\lim\limits_{x \to x_0} = f(x) = \lim\limits_{x \to x_0} = g(x) = \infty`,
   对任意的 :math:`K = \dfrac{1}{\varepsilon} \in \mathbb{R}^+`,
   以及对任意取定的 :math:`y`, 存在相应的 :math:`x \in (x_0, y) \cap \mathring{U}(x_0, \delta)` 使得

   .. math::
      \lvert g(x) \rvert > K \cdot f(y), \quad \lvert g(x) \rvert > K \cdot g(y),

   即有

   .. math::
      \left\lvert \dfrac{f(y)}{g(x)} \right\rvert < \varepsilon, \quad \left\lvert \dfrac{g(y)}{g(x)} \right\rvert < \varepsilon.

   记以上的极限过程为 :math:`\tau` (即让 :math:`y, x` 都趋于 :math:`x_0`, 但先选好 :math:`y`, 再选 :math:`x`, 使得以上关系成立), 那么有

   .. math::
      \lim_{\tau} \dfrac{f(x)}{g(x)}
      & = \lim_{\tau} \left( \dfrac{f(y)}{g(x)} + \left( 1 - \dfrac{g(y)}{g(x)} \right) \dfrac{f'(\xi)}{g'(\xi)} \right) \\
      & = 0 + (1 - 0) \lim_{\tau} \dfrac{f'(\xi)}{g'(\xi)} = \lim_{\tau} \dfrac{f'(\xi)}{g'(\xi)}.

   在极限过程 :math:`\tau` 中, 同样有 :math:`\xi \to x_0`, 所以

   .. math::
      \lim_{\tau} \dfrac{f'(\xi)}{g'(\xi)} & = \lim_{\xi \to x_0} \dfrac{f'(\xi)}{g'(\xi)} \\
      \lim_{\tau} \dfrac{f(x)}{g(x)} & = \lim_{\xi \to x_0} \dfrac{f'(\xi)}{g'(\xi)}.

   因此 :math:`\lim\limits_{x \to x_0} \dfrac{f(x)}{g(x)} = \lim\limits_{x \to x_0} \dfrac{f'(x)}{g'(x)}` 成立.

.. _extra-chap4-sec3:

§4.3 泰勒公式
--------------------------------

.. _extra-chap4-sec3-topic1:

1. 泰勒公式拉格朗日型余项 :math:`R_n(x) = \dfrac{f^{(n+1)}(\xi)}{(n+1)!} (x - x_0)^{n+1}` 的证明:

.. proof:proof::

   由 :math:`R_n(x) = f(x) - P_n(x) = f(x) - \left( f(x_0) + f'(x_0)(x - x_0) + \cdots + \dfrac{f^{(n)}(x_0)}{n!} (x - x_0)^n \right)`
   容易算得

   .. math::
      & R_n'(x_0) = R_n''(x_0) = \cdots = R_n^{(n)}(x_0) = 0, \\
      & R_n^{(n+1)}(x) = f^{(n+1)}(x).

   对函数 :math:`R_n(x)` 和 :math:`g(x) = (x - x_0)^{n + 1}` 应用 Cauchy 中值定理知, 存在 :math:`x_0` 与 :math:`x`
   之间的某个数 :math:`\xi_1` 使得

   .. math::
      \dfrac{R_n(x)}{(x - x_0)^{n + 1}} = \dfrac{R_n(x) - R_n(x_0)}{(x - x_0)^{n + 1} - (x_0 - x_0)^{n + 1}}
      = \dfrac{R_n'(\xi_1)}{(n + 1)(\xi_1 - x_0)^n}
      = \dfrac{1}{n + 1} \cdot \dfrac{R_n'(\xi_1)}{(\xi_1 - x_0)^n}

   再依次利用 Cauchy 中值定理, 有

   .. math::
      \dfrac{R_n(x)}{(x - x_0)^{n + 1}}
      & = \dfrac{1}{n + 1} \cdot \dfrac{R_n'(\xi_1)}{(\xi_1 - x_0)^n}
        = \dfrac{1}{n + 1} \cdot \dfrac{R_n'(\xi_1) - R_n'(x_0)}{(\xi_1 - x_0)^n - (x_0 - x_0)^n} \\
      & = \dfrac{1}{n + 1} \cdot \dfrac{1}{n} \cdot \dfrac{R_n''(\xi_2)}{(\xi_2 - x_0)^{n-1}}
        = \dfrac{1}{n + 1} \cdot \dfrac{1}{n} \cdot \dfrac{R_n''(\xi_2) - R_n''(x_0)}{(\xi_2 - x_0)^{n-1} - (x_0 - x_0)^{n-1}} \\
      & \vdots \\
      & = \dfrac{1}{n + 1} \cdot \dfrac{1}{n} \cdots \cdot \dfrac{1}{2} \cdot \dfrac{R_n^{(n)}(\xi_n)}{(\xi_n - x_0)}
        = \dfrac{1}{n + 1} \cdot \dfrac{1}{n} \cdots \cdot \dfrac{1}{2} \cdot \dfrac{R_n^{(n)}(\xi_n) - R_n^{(n)}(x_0)}{(\xi_n - x_0) - (x_0 - x_0)} \\
      & = \dfrac{1}{(n + 1)!} R_n^{(n+1)}(\xi_{n+1}),

   其中 :math:`\xi_{k+1}` 在 :math:`\xi_k` 与 :math:`x_0` 之间. 由于 :math:`R_n^{(n+1)}(\xi_{n+1}) = f^{(n+1)}(\xi_{n+1})`,
   所以令 :math:`\xi = \xi_{n+1}` 即有

   .. math::
      R_n(x) = \dfrac{f^{(n+1)}(\xi)}{(n+1)!} (x - x_0)^{n+1}.
