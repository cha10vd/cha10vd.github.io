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

### Cartesian components of fractional basis vectors

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

The cancellation of factors of $\eucnorm{a}$ in eq. \ref{cdota} results in an expression for $c_{x}$.

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

Having established $c_{x}$ and $c_{y}$, we may insert these into our equation for the square of the
Euclidean norm of the $\vec{c}$ vector, as per eq. $\ref{cdotc}$, rearranging for $c_{z}^{2}$:

\begin{align}
  \label{czsq}
    c_{z}^{2} & = \eucnorm{c}^{2} - c_{x}^{2} - c_{y}^{2} \nonumber \\
              & = \eucnorm{c}^{2} \Bigg\{ 1 - cos^{2}(\beta) - \frac{[cos(\alpha)-cos(\beta)cos(\gamma)]^2}
                                                         {sin^{2}(\gamma)}  \Bigg\} \nonumber \\
              & = \eucnorm{c}^{2} \Bigg\{\frac{\sin^{2}(\gamma)
                                     - cos^{2}(\beta) sin^{2}(\gamma) 
                                     - [cos(\alpha)-cos(\beta)cos(\gamma)]^2}
                                    {sin^{2}(\gamma)}  \Bigg\} \\
\end{align}

At this point we shift our focus to the numerator as we aim to simplify the myriad of trigonometric 
terms using basic trig identities. we expand out the square brackets to give us a resulting numerator of:

\begin{align}
    \sin^{2}(\gamma) & - cos^{2}(\beta) sin^{2}(\gamma) - cos^{2}(\alpha) \nonumber \\
                     & + 2cos(\alpha) cos(\beta)cos(\gamma) - cos^2(\beta) cos^2(\gamma)
\end{align}


The first simplification is: $cos^{2}(\theta) + sin^{2}(\theta) = 1$, which we get from pythagoras.

\begin{alignat}{2}
  cos^{2}(\beta) sin^{2}(\gamma) +  cos^2(\beta) cos^2(\gamma) & = [sin^{2}(\gamma) +  cos^2(\gamma)] &&\, cos^2(\beta) \nonumber \\
                                                               & =                                    &&\, cos^2(\beta)
\end{alignat}

Plugging this back into our equation leaves us with:

\begin{align}
    \sin^{2}(\gamma) & - cos^{2}(\beta) - cos^{2}(\alpha) + 2cos(\alpha)cos(\beta)cos(\gamma)
\end{align}

Finally, as far as second-order terms go, we have two negative square cosines and a positive square sine.
by the identity $sin^{2}(\theta) = 1 - cos^{2}(\theta)$, we make all second-order terms into negative cosines.

\begin{align}
    1 - \cos^{2}(\alpha) & - cos^{2}(\beta) - cos^{2}(\gamma) + 2cos(\alpha)cos(\beta)cos(\gamma)
\end{align}

We plug back into our equation for $c_{z}^{2}$ to get:

\begin{align}
  \label{cz}
    c_{z}^{2} & = \eucnorm{c}^{2} \frac{1 - \cos^{2}(\alpha)  - cos^{2}(\beta) - cos^{2}(\gamma) + 2cos(\alpha)cos(\beta)cos(\gamma)}
                             {sin^{2}(\gamma)} \\
\end{align}

\begin{alignat}{2}
  c_{z}          & = \frac{\eucnorm{c}}{sin(\gamma)} (1 - cos^{2}(\alpha) &&  - cos^{2}(\beta) - cos^{2}(\gamma) \nonumber \\
  \label{zcompc} &                                                        &&  + 2cos(\alpha)cos(\beta)cos(\gamma))^{1/2} \\
\end{alignat}


### Cell surfaces, volumes and Cartesian components of an arbitrary vectors in fractional space

We have now formulated the Cartesian components of vectors $\vec{a}, \vec{b}, \vec{c}$, we can calculate the volume of our cell.
we can take the surface area of our base using the cross product:

\begin{equation}
  \sigma_{c} = \vec{a} \times \vec{b}
\end{equation}

the volume is then derived by taking the perpendicular component of the remaining vector with respect to the base:

\begin{equation}
  \Omega = \sigma_{c} \cdot \vec{c}
\end{equation}

Now suppose we do the dot-product of our base surface area with an arbitrary vector in fractional coordinate space:

\begin{equation}
  \vec{r} \cdot \sigma_{c} = u\vec{a} \cdot \sigma_{c} + v\vec{b} \cdot \sigma_{c} + w\vec{c} \cdot \sigma_{c}
\end{equation}

Now, by the definition of $\rho_{c}$, the first two terms in our dot product evaluate to 0 ans we're left with:

\begin{align}
  \vec{r} \cdot \sigma_{c} & =  w\vec{c} \cdot \sigma_{c} \nonumber \\
                         & =  w \Omega                \\
  w & = \frac{1}{\Omega} \vec{r} \cdot \sigma_{c}         \nonumber \\
\end{align}

Now by the simple permutation of indices, we get the further relations:

\begin{align}
  \label{xcompr} u & = \frac{1}{\Omega} \vec{r} \cdot \sigma_{a} \\
  \label{ycompr} v & = \frac{1}{\Omega} \vec{r} \cdot \sigma_{b} \\
  \label{zcompr} w & = \frac{1}{\Omega} \vec{r} \cdot \sigma_{c}
\end{align}

and derive the cartesian components of a vector in the fractional space of a  lattice.


### Breaking down the volume of a unit cell into length and angle components

We have now derived all geometric parameters of interest regarding our coordinate system. We can express
the unit-cell in terms of the surface area of the base formed by vectos $\vec{a}$ and $\vec{b}$, dotted 
with the remaining vector: $\sigma_{c} \cdot \vec{c}$.

This gives us:

\begin{align}
  \Omega & = \vec{c} \cdot \sigma_{c} \nonumber \\
         & = c_z \eucnorm{\sigma_{c}}
\end{align}

we substitute $c_{z}$ for eqn. $\ref{zcompc}$ and subsitute in the definition for the magnitude of the 
cross-product:

\begin{alignat}{3}
  \Omega           & = c_z \eucnorm{\sigma_{c}}  && = \eucnorm{a} \eucnorm{b} \eucnorm{c} (1 - cos^{2}(\alpha) &&&  - cos^{2}(\beta) - cos^{2}(\gamma) \nonumber \\
  \label{crystvol} &                             &&                                                            &&&  + 2cos(\alpha)cos(\beta)cos(\gamma))^{1/2} \\
\end{alignat}


$\eucnorm{a} \eucnorm{b} \eucnorm{c}$ constitutes the **length-component** of the volume of our 
unit-cell, and translates to the volume the cell would have if our basis vectors were orthogonal.

The effect on volume accounter for by the system's non-orthogonality is then given by:

\begin{equation*}
  \eucnorm{a} \eucnorm{b} \eucnorm{c} - \Omega
\end{equation*}

or:

\begin{alignat}{3}
  \eucnorm{a} \eucnorm{b} \eucnorm{c} (cos^{2}(\alpha) &  + cos^{2}(\beta) + cos^{2}(\gamma) \nonumber \\
                                                       &  - 2cos(\alpha)cos(\beta)cos(\gamma))^{1/2} \\
\end{alignat}


Which constitutes the **angle-component** of the system.

### Matrices for coordinate-system interconversion

The keen observer will have realised that the matrix for conversion from fractional coordinates to 
Cartesian coordinates is implicit in equations \ref{xcompr} - \ref{zcompr}.

\begin{equation}
  \begin{bmatrix} x \\ y \\ z \end{bmatrix} = 
  \begin{bmatrix} a & b cos(\gamma ) & c cos(\beta)                                               \\ 
                  0 & b sin(\gamma)  & c \frac{cos(\alpha)-cos(\beta) cos(\gamma)}{sin(\gamma)} \\
                  0 & 0              & \frac{\Omega}{ab sin(\gamma)}
  \end{bmatrix}
  \begin{bmatrix} u \\ v \\ w \end{bmatrix}
\end{equation}
