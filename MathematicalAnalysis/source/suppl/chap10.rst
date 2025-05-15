第十章补充材料
^^^^^^^^^^^^^^^^^^^^^^^^^

1. Generalized Van der Waerden-Takagi 函数定义如下

.. math::

    & \varphi(x) = d(x, \mathbb{Z}) = \min_{n \in \mathbb{Z}} |x - n|, \quad x \in \mathbb{R}, \\
    & f(x) = \sum_{n=0}^{\infty} a^n \varphi(b^n x).

当 :math:`0 < a < 1`, :math:`b \in \mathbb{N}_{\geqslant 2}`, 且 :math:`ab \geqslant 1` 时,
:math:`f(x)` 是一个在 :math:`\mathbb{R}` 上处处不可导的连续函数.

首先来说明 :math:`f(x)` 在 :math:`\mathbb{R}` 上连续: 由于 :math:`0 \leqslant \varphi(x) \leqslant 1/2`,
所以 :math:`0 \leqslant a^n \varphi(b^n x) \leqslant a^n/2`. 由于正项级数 :math:`\displaystyle \sum_{n=0}^{\infty} a^n` 收敛,
于是由 Weierstraß 判别法, 函数项级数 :math:`\displaystyle \sum_{n=0}^{\infty} a^n \varphi(b^n x)` 一致收敛.
进一步由一致收敛函数项级数和函数的连续性定理知, 和函数 :math:`f(x)` 在 :math:`\mathbb{R}` 上连续.

接下来说明 :math:`f(x)` 在 :math:`\mathbb{R}` 上处处不可导: 由于 :math:`\varphi` 是周期为 1 的函数,
所以 :math:`f` 也以 1 为周期, 所以只要对任意 :math:`x \in [0, 1)` 证明 :math:`f` 在 :math:`x` 处不可导即可.
希望可以选取序列 :math:`u_n \rightarrow x \leftarrow v_n`, 使得

.. math::

    \dfrac{f(u_n) - f(v_n)}{u_n - v_n}
    = \dfrac{\sum\limits_{m=0}^{\infty} a^m (\varphi(b^m u_n) - \varphi(b^m v_n))}{u_n - v_n}

发散. 由于 :math:`2 b^n x` 是非负实数, 所以存在非负整数 :math:`k_n`, 使得 :math:`k_n \leqslant 2 b^n x < k_n + 1`, 即

.. math::

    \dfrac{k_n}{2 b^n} \leqslant x < \dfrac{k_n + 1}{2 b^n}.

取 :math:`u_n = \dfrac{k_n}{2 b^n}, v_n = \dfrac{k_n + 1}{2 b^n}`.
对于和式 :math:`\displaystyle \sum\limits_{m=0}^{\infty} a^m (\varphi(b^m u_n) - \varphi(b^m v_n))`, 分为两部分讨论:

:math:`1^{\circ}` 当 :math:`0 \leqslant m < n` 时, 由于

.. math::

    b^m u_n = \dfrac{k_n}{2} \cdot \dfrac{1}{b^{n-m}}, ~~ b^m v_n = \dfrac{k_n + 1}{2} \cdot \dfrac{1}{b^{n-m}},

从而存在非负整数 :math:`z`, 使得 :math:`b^m u_n, b^m v_n` 同时属于 :math:`[z, z+1/2]` 或 :math:`[z+1/2, z+1]`, 那么

.. math::

    \varphi(b^m u_n) - \varphi(b^m v_n) = \pm (b^m u_n - b^m v_n) = \pm \dfrac{1}{2 b^{n-m}},

从而有

.. math::

    \dfrac{a^m (\varphi(b^m u_n) - \varphi(b^m v_n))}{u_n - v_n}
    = \pm a^m \dfrac{1}{2 b^{n-m}} \left/ \left( \dfrac{1}{2 b^n}\right) \right.
    = \pm (ab)^m.

:math:`2^{\circ}` 当 :math:`m \geqslant n` 时, 有

.. math::

    b^m u_n = \dfrac{b^{m-n} \cdot k_n}{2}, ~~ b^m v_n = \dfrac{b^{m-n} \cdot (k_n+1)}{2}.

:math:`2.1^{\circ}` 当 :math:`b` 为偶数时, 若 :math:`m > n`, 则 :math:`b^m u_n, b^m v_n` 都是整数;
若 :math:`m = n`, 则 :math:`b^m u_n = \dfrac{k_n}{2}, b^m v_n = \dfrac{k_n + 1}{2}` 其中一个为整数,
另一个为半整数 (即 :math:`\dfrac{1}{2} +` 整数). 于是

.. math::

    \dfrac{a^m (\varphi(b^m u_n) - \varphi(b^m v_n))}{u_n - v_n}
    = \begin{cases}
        0, & \text{当 } m > n \text{ 时}, \\
        \dfrac{\pm a^m / 2}{1 / (2 b^{m})} = \pm (ab)^m, & \text{当 } m = n \text{ 时}.
    \end{cases}

:math:`2.2^{\circ}` 当 :math:`b` 为奇数时, :math:`b^{m-n}` 恒为奇数,
所以 :math:`b^m u_n, b^m v_n` 其中一个为整数, 另一个为半整数, 所以

.. math::

    \dfrac{a^m (\varphi(b^m u_n) - \varphi(b^m v_n))}{u_n - v_n}
    = \dfrac{\pm a^m / 2}{1 / (2 b^{n})} = \pm a^m b^n,

上述符号 :math:`\pm` 固定, 只与 :math:`k_n` 的奇偶性有关, 与 :math:`m` 无关. 于是

.. math::

    \dfrac{f(u_n) - f(v_n)}{u_n - v_n}
    & = \dfrac{\sum\limits_{m=0}^{\infty} a^m (\varphi(b^m u_n) - \varphi(b^m v_n))}{u_n - v_n} \\
    & = \begin{cases}
      \sum\limits_{m=1}^n \left( \pm (ab)^m \right), & \text{若 $b$ 为偶数}, \\
      \sum\limits_{m=1}^{n-1} \left( \pm (ab)^m \right) + \sum\limits_{m=n}^{\infty} (\pm a^m b^n), & \text{若 $b$ 为奇数}
    \end{cases} \\
    & = \begin{cases}
      \sum\limits_{m=1}^n \left( \pm (ab)^m \right), & \text{若 $b$ 为偶数}, \\
      \sum\limits_{m=1}^{n-1} \left( \pm (ab)^m \right) \pm \dfrac{(ab)^n}{1 - a}, & \text{若 $b$ 为奇数}
    \end{cases}

    容易看出, 当 :math:`b` 为正偶数, 或者 :math:`ab = 1` 时, 上式当 :math:`n \to \infty` 时发散.
    :math:`b` 为奇数且 :math:`ab > 1` 的情况需进一步讨论.
