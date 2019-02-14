Title: An Introduction to Potential Theory
Author: victor
Date: January 28, 2019
Slug: intro-pot-theory
Tags: Classical Mechanics, Multipoles
Category: Classical Mechanics

$$
    \renewcommand{\vec}[1]{\mathbf{#1}}
    \renewcommand{\uvec}[1]{\hat{\mathbf{#1}}}
    \newcommand{\eucnorm}[1]{\left|\mathbf{#1}\right|}
    \newcommand{\subject}{{\Bigg(\frac{ \eucnorm{r_{j}}}{\eucnorm{r}}}\Bigg)^2 - 2 \uvec{r} \cdot \uvec{r_{j}} \left(\frac{\eucnorm{r_{j}}}{\eucnorm{r}}\right)}
$$

In potential theory, we concern ourselves not with the determination of motion of particles given
known forces, but rather with the problem of finding forces from a knowledge of the position of 
other bodies in our system.

In molecular systems, we concern ourselves at the intermolecular level with exchange, repulsion and
electrostatic forces. The latter, being the strongest of conrtibutions with lowest distance
dependence, is subject to the inverse square law, determined by the positions of other masses and 
their charges.

### Gravitational and Electrostatic Potentials

\begin{equation}
    \label{eq:gravpot}
    \Phi (\vec{r}) = - \sum \limits_{j} \frac{G m_j}{\left|\vec{r}-\vec{r_j}\right|}
\end{equation}

\begin{equation}
    \label{eq:elcstatpot}
    \phi (\vec{r}) = \sum \limits_{j} \frac{q_{j}}{4 \pi \epsilon_{0}\left| \vec{r} - \vec{r_{j}} \right|}
\end{equation}

### The dipole and quadrupole

Suppose that a collection of charges are centered at the origin, thus minimizing $\Sigma_{j}$. We may also
minimize notaional cluttering by standardizing our units, such that equation \ref{eq:elcstatpot} reduces to: 

\begin{equation}
    \label{eq:elcstatpot_simp}
    \phi (\vec{r}) = \sum \limits_{j} \frac{q_{j}}{\left|\vec{r} - \vec{r_{j}} \right|}
\end{equation}

This is pictured below:

<figure>
  <img src="\..\assets\images\pot_theo\multipole_expansion.png" alt="" style="width:80%; margin-left: auto; margin-right: auto;"/>
  <figcaption>Schematic representation of system modelled with multipoles.<figcaption/>
</figure>



We proceed to write out the Euclidean norm out in full:

\begin{align}
    \left|\vec{r} - \vec{r_{j}} \right| &= \sqrt{(\vec{r} - \vec{r_{j}})^{2}} \nonumber \\
                                        &= \sqrt{\eucnorm{r}^2 + \eucnorm{r_{j}}^2 -2\eucnorm{r} \eucnorm{r_{j}} \uvec{r} \cdot \uvec{r_{j}}} \\
\end{align}

otherwise written as:


\begin{equation}
    \left|\vec{r} - \vec{r_{j}} \right|  = \eucnorm{r} \sqrt{1 +
                                           {\Bigg(\frac{ \eucnorm{r_{j}}}{\eucnorm{r}}}\Bigg)^2 -
                                           2 \uvec{r} \cdot \uvec{r_{j}} \frac{\eucnorm{r_{j}}}{\eucnorm{r}}} \\
\end{equation}

Consider the binomial expansion of $(1+\delta)^{n}$.

\begin{align}
  \label{eq:binom}
  (1+\delta)^{n} &= \sum \limits_{k=0}^{n}  \binom{n}{k} 1^{n-k} \delta^{k} \nonumber                 \\
                 &= \sum \limits_{k=0}^{n}  \frac{n!}{k!(n-k)!}  \delta^{k} \nonumber                 \\
                 &= 1 + n\delta + \frac{n(n-1)}{2} \delta^{2} + \frac{n(n-1)(n-2)}{6}\delta^{3} + ... \\
\end{align}

We can expand $\left|\vec{r} - \vec{r_{j}} \right|$ in terms of the above equation by making the
following substitutions:

\begin{align}
  \delta &= \subject    \nonumber \\
  n      &= -1/2,       \nonumber \\
\end{align}

producing:

\begin{align}
    & 1 && -\left(\frac{1}{2}\right) \delta + \frac{1}{2}\left(\frac{1}{2}\right)\left(\frac{3}{2}\right) \delta^{2} 
    -\frac{1}{6}\left(\frac{1}{2}\right)\left(\frac{3}{2}\right)\left(\frac{5}{2}\right) \delta^{3} + ...                \nonumber \\
 =\,& 1 && -\left(\frac{1}{2}\right) \delta + \left(\frac{3}{8}\right) \delta^{2} - \left(\frac{5}{16}\right)\delta^{3} + ... \nonumber \\
 =\,& 1 && -\left(\frac{1}{2}\right) \left(\subject\right) \nonumber \\
    &   && + \left(\frac{3}{8}\right) \left(\subject\right)^{2} \nonumber \\
    &   && - \left(\frac{5}{16}\right)\left(\subject\right)^{3} \nonumber \\
    &   && + ...     \\
\end{align}

In addition,
suppose also that the probe used to evaluate the potential at a given point is considerabily further from 
the origin than any of the $j$ charges. This leads to the situation where $\vec{r} >> \vec{r_{j}}$and 
consequently $\left| \vec{r} - \vec{r_{j}} \right| \approx \left| \vec{r} \right |$. 

When this is the case, we are able to expand the potential in powers of 1/r.
