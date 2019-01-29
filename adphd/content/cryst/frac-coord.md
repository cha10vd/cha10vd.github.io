Title:		The Fractional Coordinate System
Author:		victor
Date:		January 21, 2019
Slug: 		frac-coord
Category:   Crystallography
Tags:       Linear Algebra, Crystallography
Summary:    Formulation of interconversion between Fractional and Cartesian coordinates.

# Working in Fractional Coordinates

$$
    \renewcommand{\vec}[1]{\mathbf{#1}}
    \newcommand{\eucnorm}[1]{\left|\mathbf{#1}\right|}
    \newcommand{\veccomp}[1]{({#1}_{x}, {#1}_{y}, {#1}_{z})}
    \newcommand{\subsup}[3]{#1_{#2}^{#3}}
    \let\oldref\ref
    \renewcommand{\ref}[1]{(\oldref{#1})}
$$

In describing a physical system, one usually has many choices as to the coordinate system in which 
to formulate a problem, and intuitively it makes sense to choose one in which we may exploit the 
natural symmetry of the system.

A coordinate system is composed of an *origin* and a *basis* of three linearly independent (non-coplanar) 
basis vectors $\vec{a}, \vec{b}, \vec{c}$.

Just as for problems with spherical symmetry we move from Cartesian to polar coordinates, there is 
likewise a particular coordinate system especially suited for dealing with non-orthogonal repeating
systems. This is the *fractional coordinate system*.

The idea here is to take three vectors which connect repeats in our infinitely repeating system and
use these as our basis vectors for representing space. In our fractional coordinates our basis is 
given by $a,b,c$, as opposed to $x,y,z$. These will have mutual angles of $\alpha, \beta, \gamma$.

<figure>
  <img src="/../assets/images/cryst/unit_cell.png" alt="my alt text"/>
  <figcaption>Fractional coordinate system embedded in Cartesian axis.</figcaption>
</figure>

The question then becomes: **How is this coordinate system connectected to the one we're acustomed to?**

If we imagine the "box" formed from the three vectors in each coordinate system, we can start
by simply aligning one of the fractional vectors to one of its Cartesian counterparts, giving them 
a one-to-one correspondence. We set *a* to lie along the positive x-axis direction and choose *b* 
to lie in the *x,y*-plane, givings us the following relations:

\begin{equation}
    \label{veca}
    \vec{a} = (\eucnorm{a},0,0)
\end{equation}
\begin{equation}
    \label{vecb}
    \vec{b} = (\eucnorm{b}\cos(\gamma), \eucnorm{b}\sin(\gamma), 0)
\end{equation}

Having used up all our degrees of freedom, *c* is constrained by the directions of *a* and *b* and
the angles it makes with them.

\begin{align}
    \label{cdota}
    \vec{c} \cdot  \vec{a}  &= \eucnorm{a}  \eucnorm{c}\ cos(\beta) \\ \nonumber
                            &= \eucnorm{a}\  c_{x}                  \\
\end{align}

\begin{align}
    \vec{c} \cdot  \vec{b}  &= \eucnorm{b}  \eucnorm{c}  cos(\alpha)                         \label{cdotb1}  \\ 
                            &= \veccomp{c} (\eucnorm{b}\cos(\gamma), \eucnorm{b}\sin(\gamma), 0)  \nonumber  \\ 
                            &= c_{x} \eucnorm{b}\cos(\gamma) + c_y \eucnorm{b}\sin(\gamma)   \label{cdotb2}  \\
\end{align}

\begin{equation}
    \label{cdotc}
    \vec{c} \cdot \vec{c}    = \eucnorm{c}^{2} = \subsup{c}{x}{2} + \subsup{c}{y}{2}, + \subsup{c}{z}{2}
\end{equation}

from equations $\ref{veca}$ through to $\ref{cdotc}$ we can deduce the identities of the cartesian components of $\vec{c}$.

The cancellation of factors of $\eucnorm{a}$ in eq. \ref{cdota} results in an expression for $c{x}$.

\begin{equation}
    \label{cx}
    c_x = \eucnorm{c} cos(\beta)
\end{equation}

In deriving $c_{y}$, we combine equations \ref{cdotb1} and \ref{cdotb2} as follows:

\begin{equation}
    \eucnorm{b} \eucnorm{c} cos(\alpha) = c_{x} \eucnorm{b}\cos(\gamma) + c_{y} \eucnorm{b}\sin(\gamma), \nonumber
\end{equation}

cancelling the common factor of $\eucnorm{b}$, rearranging and finally subbing in eq. \ref{cx} the to yield:

\begin{equation}
    \label{cy}
    c_{y} = \eucnorm{c} \frac{cos(\alpha) - \cos(\beta) \cos(\gamma)}{sin(\gamma)}                           \\
\end{equation}

Having established $c_{x}$ and $c_{y}$, we may insert these into our equation for the square of the Euclidean norm of the $\vec{c}$ vector, as per eq. $\ref{cdotc}$: 


