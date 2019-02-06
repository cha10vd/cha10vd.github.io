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
  \renewcommand{\unit}[1]{\mathbf{\hat{#1}}}
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

##### The vector dot-product and the summation convention

Tensor notation, interestingly, translates to how loops are written in programming.

Consider the tensor representation of the dot-product:

\begin{equation}
    a_i b_i \equiv a_1 b_1 + a_2 b_2 + a_3 b_3
\end{equation}

any index equates to a loop counter iterating from 1 to 3. Where the index is repeated, it should
also be summed over.  Here the $i$ is repeated, so in Python the dot product would read:

```python
dot_prod = 0
for i in range(0,3):
    dot_prod += a[i] + b[i]
```

We shall see that this arbitrarily simple example holds true for more complex calculations.

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

##### Matrix transpose:

Simply put, in transposing **A**, we interchange columns and rows. Therefore we have:

\begin{equation}
    \label{tenstrans}
    (A_{ij})^{T} = A_{ji}
\end{equation}


##### Matrix determinant:

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
needed to rearrange the $j^{th}$ indices in $A_{ij}$ of a given permutation away from the standard $1,2,3$ ordering.

In light of this fact, tensor analysis introduces a symbol whose function is homologous to that of the kronecker
delta for the identity matrix. It returns a value based on the identities of $i$, $j$ and $k$. We thus present the
Levi-Civita symbol, $\epsilon_{ijk}$:


\begin{equation}
  \label{lev-civ}
  \epsilon_{ijk}
  \begin{cases}
      +1, &   \text{if } (i,j,k) \text{ is } (1,2,3),(2,3,1) \text{, or } (3,1,2), \\
      -1, &   \text{if } (i,j,k) \text{ is } (3,2,1),(1,3,2) \text{, or } (3,1,2), \\
    \;0, &   \text{if } i = j \text{ or } j=k \text{, or } k=i
  \end{cases}
\end{equation}

a useful diagramatic representation of this is presented below:

<figure>
  <img src="/../assets/images/math/permutation_indices_3d_numerical.png", alt="", style="width:50%; margin-left: auto; margin-right: auto;"/>
  <figcaption>Even permutations are given by the orange cycle, odd, by the red.</figcaption>
</figure>

We can thus prepend the matrix-element multiplications in our determinant equation by $\epsilon_{ijk}$, 
leaving us with a simple sum:

\begin{align}
  | {\bf A} |
  = & \epsilon_{123} A_{\r 11} A_{\g 22} A_{\b 33} + \epsilon_{132} A_{\r 11} A_{\g 23} A_{\b 32} + \nonumber \\
    & \epsilon_{231} A_{\r 12} A_{\g 23} A_{\b 31} + \epsilon_{213} A_{\r 12} A_{\g 21} A_{\b 33} + \nonumber \\
    & \epsilon_{312} A_{\r 13} A_{\g 21} A_{\b 32} + \epsilon_{321} A_{\r 13} A_{\g 22} A_{\b 31}
\end{align}

Finally, we collapse this large sum into the compact tensor notation:

\begin{equation}
  | {\bf A} | = \epsilon_{ijk}A_{1i}A_{2j}A_{3k}
\end{equation}

or, by the determinant's invariance over transposition of the matrix:

\begin{equation}
  | {\bf A} | = \epsilon_{ijk}A_{i1}A_{j2}A_{k3}
\end{equation}


Here all three indices appear twice in the tensor representation. Therefore, if we were to write a
python loop we would have:

```python
detA = 0
for i in range(0,3):
  for j in range(0,3):
    for k in range(0,3):
      detA += LeviCivita(i,j,k)*A[i,1]*A[j,2]*A[k3]
```

We can equally imagine a simple implementation of the Levi-Civita fucntion:

```python
def LeviCivita(i,j,k):
  if any([i == j, i == k, j == k]):  
    return(0)

  indices = [i,j,k]
  start   = indices.index(1)

  if indices[(start+1) % 3] == 2:
    return( 1)
  else:
    return(-1)
```

##### The cross-product

\begin{align}
  \label{tensorCross}
    \vec{a} \times \vec{b} = \vec{c} = & 
    \left[
    \matrix{
        \unit{x} & \unit{y} & \unit{z}                  \\
        a_{x} & a_{y} & a_{z}                           \\
        b_{x} & b_{y} & b_{z}
    }
    \right]\\
    \nonumber \\
     = & \unit{x}(a_{y}b_{z} - a_{z}b_{y}) + \nonumber  \\
       & \unit{y}(a_{z}b_{x} - a_{x}b_{z}) + \nonumber  \\
       & \unit{x}(a_{x}b_{y} - a_{y}b_{x})              \\
    \nonumber \\
  c_{i} = & \epsilon_{ijk}a_{j}b_{k}
\end{align}

We once againask ourselves how the tensor notation translates to code. We have three indices, $i,j$
and $k$. We therefore expect three nested loops. $j$ and $k$ each appear twice, so these must be
summed over.


```python
cVec = [0,0,0] # Cross product vector
for i in range(0,3):
  for j in range(0,3):
    for k in range(0,3):
      cVec[i] += LeviCivita(i,j,k) * aVec[j] * bVec[k]
```

##### The Vector Diadic Product

After a few examples of deriving tensor notation, we should be pretty good at this. The vector diadic
product is nothing other than the outer product. from two $3\times1$ vectors we get a $3\times3$ matrix.

\begin{equation}
  \label{diad}
    C_{ij} = a_{i}b_{j}
\end{equation}

There's no repetition of indices, so there's no summation and each term in the nested loops will give rise
to a new term in our resulting matrix.

```python
diadProd = [[0,0,0],
            [0,0,0],
            [0,0,0]]

for i in range(0,3):
  for j in range(0,3):
    diadProd[i][j] = aVec[i] * aVec[j]
```
