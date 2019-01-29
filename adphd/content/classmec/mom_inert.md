Title: Moments of Inertia
Author: victor
Date: January 28, 2019
Slug: mom-inert
Tags: Classical Mechanics, Molecular Properties
Category: Classical Mechanics
Summary: Deriving a molecule's moments of inertia from its mass distribution.
CSS: tbox.css

$$
    \renewcommand{\vec}[1]{\mathbf{#1}}
$$

<div class="tBox"  markdown>  
  <h4> Matrix outer product: </h4>
  <br>
    The outer product is defined as thethe following vector product:
    \begin{equation}
        \vec{u} \otimes \vec{v} = \vec{u}\vec{v^T} = 
        \begin{bmatrix}
            x   \\  y   \\  z               \\
        \end{bmatrix}
        \begin{bmatrix}
            x    &  y   &   z               \\
        \end{bmatrix}
        =
        \begin{bmatrix}
            x^{2}   &  xy       & xz        \\
            yx      &  y^{2}    & yz        \\ 
            zx      &  zy       & z^{2}     \\
        \end{bmatrix}
    \end{equation}
</div>

Let us consider a **rigid body** rotating with a fixed angular velocity $\omega$ about an axis
passing through the origin, as illustated in fig.

<figure>
  <img src="\..\assets\images\rigid_body.png" alt="Rigid body rotation" style="width:50%; margin-left: auto; margin-right: auto;" />
  <figcaption> Rotating rigid body. </figcaption>
</figure>

The angular momentum of te point given at $\vec{r_{i}}$ is then given by:

\begin{equation}
    \label{angmom}
    \frac{d\vec{r_{i}}}{dt} = \vec{w} \times \vec{r_{i}} \vec{V_{i}}
\end{equation}
