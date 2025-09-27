第二章补充材料
^^^^^^^^^^^^^^^^^^^^^^^^^

.. _reg-outer-measure:

1. 勒贝格外测度的正则性. 对任意集合 :math:`E \subset \mathbb{R}^d`, 存在 :math:`G_{\delta}`-集 :math:`A`,
   称为 :math:`E` 的等测包, 使得 :math:`E \subset A` 且 :math:`m A = m^* E`.

.. proof:proof::

   由外测度定义, 对任意自然数 :math:`n \in \mathbb{N}`, 存在开集 :math:`G_n` 使得 :math:`E \subset G_n`,
   且 :math:`m G_n \leqslant m^* E + \frac{1}{n}`. 令 :math:`A = \bigcap\limits_{n=1}^{\infty} G_n`,
   则 :math:`A` 为一个 :math:`G_{\delta}`-集, 且 :math:`E \subset A`. 由 (外) 测度的单调性, 有

   .. math::

      m^* E \leqslant m^* A \leqslant m A \leqslant m G_n \leqslant m^* E + \frac{1}{n}.

   令 :math:`n \to \infty`, 则有 :math:`m^* E = m^* A = m A`.

   .. note::

      勒贝格外测度的正则性有一系列重要的推论, 这里列举几个:

      (1). 设 :math:`\{E_n\}_{n=1}^{\infty}` 为 :math:`\mathbb{R}^d` 中的一列点集, 那么

      .. math::

         \DeclareMathOperator*\lowlim{\underline{lim}}
         \DeclareMathOperator*\uplim{\overline{lim}}

         m^* \left( \lowlim_{n \to \infty} E_n \right) \leqslant \lowlim_{n \to \infty} m^* E_n.

      (2). 设 :math:`\{E_n\}_{n=1}^{\infty}` 为 :math:`\mathbb{R}^d` 中的渐张集列, 那么

      .. math::

            \lim_{n \to \infty} m^* E_n = m^* \left( \lim_{n \to \infty} E_n \right).

.. _sigma_ring:

2. 设 :math:`\mathscr{E}` 为基本集 :math:`X` 的子集族, 那么它生成的环 :math:`\mathscr{R}(\mathscr{E})` 包含于

   .. math::

      \mathscr{R} :=
      \left\{ E \subset X ~ : ~ E \subset \bigcup\limits_{k=1}^{n} E_k, ~ n \in \mathbb{N}, E_1, \dots, E_n \in \mathscr{E} \right\}.

   首先, 验证 :math:`\mathscr{R}` 是一个环. 它关于有限并运算的封闭性显然, 只需验证它关于差运算的封闭性. 对任意 :math:`E \subset \bigcup\limits_{k=1}^{n} E_k`,
   :math:`F \subset \bigcup\limits_{j=1}^{m} F_j \in \mathscr{R}`, 有

   .. math::

      E \setminus F \subset E \subset \bigcup\limits_{k=1}^{n} E_k,

   从而知 :math:`E \setminus F \in \mathscr{R}`.

   其次, 由于 :math:`\mathscr{R}(\mathscr{E})` 是包含 :math:`\mathscr{E}` 的最小环, 所以 :math:`\mathscr{R}(\mathscr{E}) \subset \mathscr{R}`.

.. _measure-extension:

3. 测度扩张

   .. tikz::
      :align: center
      :xscale: 100
      :libs: arrows.meta,positioning,calc
      :packages: mathrsfs

      \newcommand{\verteq}{\rotatebox{90}{$\,=$}}

      \begin{scope}[
         transform shape,
         node distance=0.5cm and 1.25cm, % Vertical and horizontal distance
         boxnode/.style={draw, rectangle, minimum height=0.8cm, text width=2.5cm, align=center, font=\small},
         textnode/.style={text width=2.1cm, align=center, font=\small},
         measurenode/.style={text width=2.5cm, align=center, font=\small},
         mathnode/.style={font=\large},
         tinytext/.style={font=\tiny, align=left},
      ]

      \node (E) [mathnode] {环 $\mathscr{E}$};
      \node (RE) [mathnode, right=of E] {$\mathscr{R}_{\sigma}(\mathscr{E})$};
      \node (M) [mathnode, right=of RE] {$\mathscr{M}$};
      \node (SE) [mathnode, right=of M] {$\mathscr{S}(\mathscr{E}) = \mathscr{P}(\mathbb{R}^n)$};
      \node (verteq) [textnode, above=of SE, yshift=-1.7em, xshift=-0.8cm] {$\verteq$};
      \node [above=of verteq, yshift=-2.1em, xshift=0.75cm] {\smaller[1] $\{ E ~:~ E \subset \bigcup\limits_{n=1}^{\infty} A_n, A_n \in \mathscr{E} \}$};

      \node (subset1) at ($(E.east)!0.5!(RE.west)$) {$\subsetneqq$};
      \node (subset2) at ($(RE.east)!0.5!(M.west)$) {$\subsetneqq$};
      \node (subset3) at ($(M.east)!0.5!(SE.west)$) {$\subsetneqq$};

      \node (basis) [measurenode, below=of E, yshift=0.5cm] {\smaller[1] 半开闭矩体有限并, 及 $\emptyset$};
      \node (borel_set) [measurenode, below=of RE, yshift=0.5cm] {\smaller[1] Borel 集类};
      \node (sigma_gen) [textnode, above=of RE, yshift=-1.2em] {\smaller[1] 由 $\mathcal{E}$ 生成的 $\sigma$ 环};
      \node (non_borel) [textnode, above=of subset2, yshift=0.4cm] {存在非 Borel 集的可测集};
      \node (lebesgue_measure) [measurenode, below=of M, yshift=0.5cm] {\smaller[1] Lebesgue 可测集类};
      \node (non_meas) [textnode, above=of subset3, yshift=0.4cm] {存在不可测集};
      \node (all_subsets) [measurenode, below=of SE, yshift=0.5cm] {\smaller[1] $\mathbb{R}^n$ 全体子集};

      \node (mu1) [mathnode, below=of E, yshift=-3em, anchor=center] {$\mu$};
      \node (tilde_mu1) [mathnode, below=of RE, yshift=-3em, anchor=center] {$\tilde{\mu}$};
      \node (tilde_mu2) [mathnode, below=of M, yshift=-3em, anchor=center] {$\tilde{\mu}$};
      \node (mu_star) [mathnode, below=of SE, yshift=-3em, anchor=center] {
      $\mu^* E = \inf\limits_{E \subset \bigcup A_n} \sum_n \mu(A_n)$
      };
      \node (mu_final) [mathnode, below=of mu_star, yshift=-2cm] {};

      \draw[->] (non_borel) -- (subset2);
      \draw[->] (non_meas) -- (subset3);

      \draw[->] (tilde_mu1) to [bend right] (mu1);
      \draw[->] (tilde_mu2) to [bend right] (tilde_mu1);
      \draw[->] ([yshift=-0.5em]mu_star.north west) to [bend right] (tilde_mu2);

      \draw[->] (mu1.south) to [bend right] (mu_star.south west);
      \end{scope}
