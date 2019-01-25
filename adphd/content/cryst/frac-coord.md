Title:		The Fractional Coordinate System
Author:		victor
Date:		January 21, 2019
Slug: 		frac-coord

# Working in Fractional Coordinates

$$
    \renewcommand{\vec}[1]{\mathbf{#1}}
    \newcommand{\eucnorm}[1]{\left|\mathbf{#1}\right|}
    \newcommand{\veccomp}[1]{({#1}_{x}, {#1}_{y}, {#1}_{z})}
$$

In describing a physical system, one usually has many choices as to the coordinate system in which 
to formulate a problem, and intuitively it makes sense to choose one in which we may exploit the 
natural symmetry of the system.

A coordinate system is composed of an *origin* and a *basis* of three linearly independent (non-coplanar) 
basis vectors $\vec{a}, \vec{b}, \vec{c}$.

Just as for problems with spherical symmetry we move from cartesian to polar coordinates, there is 
likewise a particular coordinate system especially suited for dealing with non-orthogonal repeating
systems.  This is the *fractional coordinate system*.

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
    \vec{a} = (a,0,0)
\end{equation}
\begin{equation}
    \label{vecb}
    \vec{b} = (b\ cos(x), b\  sin(y), 0)
\end{equation}

Having used up all our degrees of freedom, *c* is constrained by the directions of *a* and *b* and
the angles it makes with them.

\begin{equation}
    \label{cdota}
    \vec{c} \cdot  \vec{a} = \eucnorm{a}\ \eucnorm{c}\ cos(\beta) = a\  c_{x}
\end{equation}

\begin{align}
    	\vec{c} \cdot  \vec{b}  &= \eucnorm{b}  \eucnorm{c}  cos(\alpha) \\
                                &= \veccomp{c} \\
\end{align}
