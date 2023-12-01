第四章补充材料
^^^^^^^^^^^^^^^^^^^^^^^^^

1. 令 :math:`\varphi = \chi_{(\alpha, \beta)}`, 其中 :math:`(\alpha, \beta) \subset E = [-\pi, \pi]`, 那么

.. math::

    \varphi_n (x) = \dfrac{1}{\pi} \int_{-\pi}^{\pi} \varphi(x + u) \dfrac{\sin(n + \frac{1}{2})u}{2 \sin \frac{1}{2}u} \mathrm{d}u = \dfrac{1}{\pi} \int_{(\alpha-x))/2}^{(\beta-x)/2} \dfrac{\sin(2n+1)v}{\sin v} \mathrm{d}v

一致有界，即存在常数 :math:`C` 使得 :math:`\|\varphi_n\|_{\infty} \leq C` 对所有 :math:`n` 成立。

.. proof:proof::

    由对称性，只需要考虑 :math:`0 \leqslant \alpha - x \leqslant \beta - x \leqslant \pi` 的情况。此时，
    被积函数 :math:`\dfrac{\sin(2n+1)v}{\sin v}` 的分母在被积区间 :math:`\left(\dfrac{\alpha-x}{2}, \dfrac{\beta-x}{2}\right)` 上非负，
    且单调递增。令

    .. math::

        k_{\alpha} & = \min \{ k \ :\ \dfrac{k}{2n+1} \geqslant \dfrac{\alpha-x}{2} \}, \\
        k_{\alpha, 0} & = \min \{ k \ :\ k \geqslant k_{\alpha}, \text{ 且 } k \text{为偶数} \}, \\
        k_{\alpha, 1} & = \min \{ k \ :\ k \geqslant k_{\alpha}, \text{ 且 } k \text{为奇数} \}, \\
        k_{\beta} & = \max \{ k \ :\ \dfrac{k}{2n+1} \leqslant \dfrac{\beta-x}{2} \}, \\
        k_{\beta, 0} & = \max \{ k \ :\ k \leqslant k_{\beta}, \text{ 且 } k \text{为偶数} \}, \\
        k_{\beta, 1} & = \max \{ k \ :\ k \leqslant k_{\beta}, \text{ 且 } k \text{为奇数} \}

    令区间 :math:`I_k = \left[ \dfrac{k-1}{2n+1}\pi, \dfrac{k}{2n+1}\pi \right]`, 那么在相邻的区间 :math:`I_k` 和 :math:`I_{k+1}` 上有

    .. math::

        \left\lvert \int_{I_k} \dfrac{\sin(2n+1)v}{\sin v} \mathrm{d}v \right\rvert > \left\lvert \int_{I_{k+1}} \dfrac{\sin(2n+1)v}{\sin v} \mathrm{d}v \right\rvert,

    但积分值的符号相反， :math:`k` 为奇数时为正， :math:`k` 为偶数时为负。因此

    .. math::

        \varphi_n(x) & = \dfrac{1}{\pi} \left( \int_{(\alpha-x)/2}^{\pi k_{\alpha, 1}/(2n+1)} + \left( \int_{I_{k_{\alpha, 1}}} + \int_{I_{k_{\alpha, 1} + 1}} \right) + \cdots + \int_{\pi k_{\beta, 1}/(2n+1)}^{(\beta-x)/2} \right) \dfrac{\sin(2n+1)v}{\sin v} \mathrm{d}v \\
        & \geqslant \dfrac{1}{\pi} \left( \int_{(\alpha-x)/2}^{\pi k_{\alpha, 1}/(2n+1)} + \int_{\pi k_{\beta, 1}/(2n+1)}^{(\beta-x)/2} \right) \dfrac{\sin(2n+1)v}{\sin v} \mathrm{d}v,

    同时

    .. math::

        \varphi_n(x) & = \dfrac{1}{\pi} \left( \int_{(\alpha-x)/2}^{\pi k_{\alpha, 0}/(2n+1)} + \left( \int_{I_{k_{\alpha, 0}}} + \int_{I_{k_{\alpha, 0} + 1}} \right) + \cdots + \int_{\pi k_{\beta, 0}/(2n+1)}^{(\beta-x)/2} \right) \dfrac{\sin(2n+1)v}{\sin v} \mathrm{d}v \\
        & \leqslant \dfrac{1}{\pi} \left( \int_{(\alpha-x)/2}^{\pi k_{\alpha, 0}/(2n+1)} + \int_{\pi k_{\beta, 0}/(2n+1)}^{(\beta-x)/2} \right) \dfrac{\sin(2n+1)v}{\sin v} \mathrm{d}v.

    总之，有

    .. math::

        \lvert \varphi_n (x) \rvert \leqslant 2 \cdot \dfrac{1}{\pi} \cdot \max\limits_k \int_{I_k} \dfrac{\sin(2n+1)v}{\sin v} \mathrm{d}v = \dfrac{2}{\pi} \cdot \int_{I_1} \dfrac{\sin(2n+1)v}{\sin v} \mathrm{d}v = \dfrac{2}{\pi} \cdot \int_0^{\frac{\pi}{2n+1}} \dfrac{\sin(2n+1)v}{\sin v} \mathrm{d}v.

    我们知道 :math:`\dfrac{\sin(2n+1)v}{\sin v} = 1 + 2 \sum\limits_{k=1}^n \cos(2kv)`, 其导数为 :math:`-2 \sum\limits_{k=1}^n 2k \sin(2kv)`, 在 :math:`[0, \pi/(2n+1)]` 恒负，因此 :math:`\dfrac{\sin(2n+1)v}{\sin v}` 在 :math:`[0, \pi/(2n+1)]` 上单调递减，
    于是有

    .. math::

        \lvert \varphi_n (x) \rvert \leqslant \dfrac{2}{\pi} \cdot \int_0^{\frac{\pi}{2n+1}} \dfrac{\sin(2n+1)v}{\sin v} \mathrm{d}v \leqslant \dfrac{2}{\pi} \cdot \int_0^{\frac{\pi}{2n+1}} (2n+1) \mathrm{d}v = \dfrac{2}{\pi} \cdot \dfrac{\pi}{2n+1} \cdot (2n+1) = 2.

    这样就证明了 :math:`\varphi_n` 一致有界。

    .. note::

        Dirichlet 核 :math:`\dfrac{\sin\frac{2n+1}{2}v}{\sin\frac{1}{2}v}` 的图像如下所示：

        .. image:: ../_static/images/Dirichlet_kernels.svg
            :align: center
            :width: 80%
