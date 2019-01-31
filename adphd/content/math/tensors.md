Author: victor
Title: Intro to Tensors
Slug: intro-tensor
Date: January 30, 2019
Tags: Tensors, Mathematics
Category: Mathematics

$$
  \renewcommand{\r}[0]{\color{red}}
  \renewcommand{\g}[0]{\color{green}}
  \renewcommand{\b}[0]{\color{blue}}
$$


What is a tensor? Is it just a glorified matrix? If not, how do we tell the two appart? To the
neophyte, it's all very confusing, which is why we wish to shed light on some of these 
fundamental questions.

The website [continuummechanics.org](http://www.continuummechanics.org/) has a list of
some fundamental facts:

* If it's a physical quantity, like stress, then it's usually called a tensor. 
  If it's not a physical quantity, then it's usually called a matrix.
+ The vast majority of tensors are symmetric. One common quantity that is not symmetric, 
  and not referred to as a tensor, is a rotation matrix.
+ Tensors are in fact any physical quantity that can be represented by a scalar, vector, or matrix. 
    * Zero-order tensors, like mass, are called scalars, 
    + First-order tensors are called vectors. 
    + Higher-order tensors include stress, strain, and stiffness tensors.
+ The order, or rank, of a matrix or tensor is the number of subscripts it contains. 
  A vector is a 1st rank tensor. A 3x3 stress tensor is 2nd rank

### Tensor notation for familiar concepts:

In looking at how tensor notation refers to entries in a matrix, we'll call our generic matrix **A**
and refer to the entry in the $i^{th}$ row and $j^{th}$ column as $A_{ij}$.

##### Identity matrix:

The only non-zero elements in an identity matrix are ones where the index $i$ and index $j$ are equal.
We may therefore represent an identity matrix in terms of a condition imposed upon its indexes:

\begin{equation}
    \label{kroneck}
    A_{ij} =
    \begin{cases}
            1, &         \text{if } i=j,\\
            0, &         \text{if } i\neq j.
    \end{cases}
\end{equation}

And what we have is the **Kronecker delta**. Therefore, the identity matrix is represented by $\delta_{ij}$.

#### Matrix transpose:

Simply put, in transposing **A**, we interchange columns and rows. Therefore we have:

\begin{equation}
    \label{tenstrans}
    (A_{ij})^{T} = A_{ji}
\end{equation}


#### Matrix determinant:

Consider the determinant of a $3\times3$ matrix:

\begin{align*}
  | {\bf A} | = &
  \left|
  \matrix {
   A_{11} & A_{12} & A_{13} \\
   A_{21} & A_{22} & A_{23} \\
   A_{31} & A_{32} & A_{33}
  } \right| \\
   \\
  = & A_{11} ( A_{22} A_{33} - A_{23} A_{32} ) + \\
    & A_{12} ( A_{23} A_{31} - A_{21} A_{33} ) + \\
    & A_{13} ( A_{21} A_{32} - A_{22} A_{31} ) \\
   \\
  = & A_{\r 11} A_{\g 22} A_{\b 33} - A_{\r 11} A_{\g 23} A_{\b 32} + \\
    & A_{\r 12} A_{\g 23} A_{\b 31} - A_{\r 12} A_{\g 21} A_{\b 33} + \\
    & A_{\r 13} A_{\g 21} A_{\b 32} - A_{\r 13} A_{\g 22} A_{\b 31}
\end{align*}

We see that the **+**'s and **-**'s in the determinant equation alternate in line with how many permutations are
needed to rearrange the $j^{th}$ indices of a given permutation away from the standard $1,2,3$ ordering.

In light of this fact, tensor analysis introduces a symbol whose function is homologous to that of the kronecker
delta for the identity matrix. It returns a value based on the identities of $i$, $j$ and $k$.


\begin{equation}
  \label{lev-civ}
  \epsilon_{ijk}
  \begin{cases}
      +1, &   \text{if } (i,j,k) \text{ is } (1,2,3),(2,3,1) \text{, or } (3,1,2), \\
      -1, &   \text{if } (i,j,k) \text{ is } (3,2,1),(1,3,2) \text{, or } (3,1,2), \\
    \;0, &   \text{if } i = j \text{ or } j=k \text{, or } k=i
  \end{cases}
\end{equation}
