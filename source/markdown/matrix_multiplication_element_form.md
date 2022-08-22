Visualisation might help. I'll use your notations and dimensions of the given matrices:

> If $A=(a_{ij})\in M_{mn}(\Bbb F), B=(b_{ij})\in M_{np}(\Bbb F)$ then $C=A\times B=(c_{ij})\in M_{mp}(\Bbb F)$.
> $c_{ij}=\sum_{k=1}^{n} a_{ik}b_{kj}$ where $i=1,...m, j=1,...p$

You say you know how to multiply matrices, so take a look at one specific element in the product $C=AB$, namely the element on position $(i,j)$, i.e. in the $i$th row and $j$th column.

To obtain this element, you:

 - first **multiply** all elements of the *$i$th row* of the matrix $A$ _pairwise_ with all the elements of the *$j$th column* of the matrix $B$;
 - and then you **add** these $n$ products.

You have to repeat this procedure for every element of $C$, but let's zoom in on that one specific (but arbitrary) element on position $(i,j)$ for now:

$$\begin{pmatrix}
a_{11} &\ldots  &a_{1n}\\
\vdots& \ddots &\vdots\\
\color{blue}{\mathbf{a_{i1}}} &\color{blue}{\rightarrow}  &\color{blue}{\mathbf{a_{in}}}\\
\vdots&  \ddots &\vdots\\
a_{m1} &\ldots &a_{mn}
\end{pmatrix}
\cdot
\begin{pmatrix}
b_{11}&\ldots &\color{red}{\mathbf{b_{1j}}} &\ldots &b_{1p}\\
\vdots& \ddots &\color{red}{\downarrow} &  \ddots  &\vdots\\
b_{n1}&\ldots &\color{red}{\mathbf{b_{nj}}}&\ldots &b_{np}
\end{pmatrix}
=
\begin{pmatrix}
c_{11}&\ldots& c_{1j} &\ldots &c_{1p}\\
\vdots&  \ddots & & &\vdots\\
c_{i1}& & \color{purple}{\mathbf{c_{ij}}} & &c_{ip}\\
\vdots& &  & \ddots &\vdots\\
c_{m1} &\ldots& c_{mj} &\ldots &c_{mp}
\end{pmatrix}$$
with element $\color{purple}{\mathbf{c_{ij}}}$ equal to:
$$\mathbf{\color{purple}{c_{ij}}  =  \color{blue}{a_{i1}} \color{red}{b_{1j}}  + \color{blue}{a_{i2}} \color{red}{b_{2j}}  +  \cdots  + \color{blue}{a_{in}} \color{red}{b_{nj}}}$$

Now notice that in the sum above, the left outer index is always $i$ ($i$th row of $A$) and the right outer index is always $j$ ($j$th column of $B$). The inner indices run from $1$ to $n$ so you can introduce a summation index $k$ and write this sum compactly using summation notation:
$$\color{purple}{\mathbf{c_{ij}}}=\sum_{k=1}^{n} \color{blue}{\mathbf{a_{ik}}}\color{red}{\mathbf{b_{kj}}}$$

The formula above thus gives you the element on position $(i,j)$ in the product matrix $C=AB$ and therefore completely defines $C$ by letting $i=1,...,m$ and $j=1,...,p$.

---

> Can someone explain what that represents by giving me an example? And how did we get that formula?

The illustration above should give you an idea of the general formula, but here's a concrete example where I took $3 \times 3$ matrices for $A$ and $B$ and focus on the element on position $(2,3)$:

$$\begin{pmatrix}
a_{11} & a_{12}  &a_{13}\\
\color{blue}{1} &\color{blue}{2}  &\color{blue}{3}\\
a_{31} & a_{32} &a_{33}
\end{pmatrix}
\cdot
\begin{pmatrix}
b_{11}&b_{12} &\color{red}{6}\\
b_{21}&b_{22} &\color{red}{5}\\
b_{31}&b_{32} &\color{red}{4}
\end{pmatrix}
=
\begin{pmatrix}
c_{11}& c_{12} &c_{13}\\
c_{21}& c_{22} &\color{purple}{\mathbf{c_{23}}}\\
c_{31}& c_{32} &c_{33}
\end{pmatrix}$$
with element $\color{purple}{\mathbf{c_{23}}}$ equal to:
$$\begin{array}{rccccccc}
\color{purple}{c_{23}}
& = & \color{blue}{a_{21}} \color{red}{b_{13}}  &+& \color{blue}{a_{22}} \color{red}{b_{23}}  &+& \color{blue}{a_{23}} \color{red}{b_{33}}
& = &  \displaystyle \sum_{k=1}^{3} \color{blue}{a_{2k}}\color{red}{b_{k3}} \\
& = & \color{blue}{1} \cdot \color{red}{6}  &+& \color{blue}{2}  \cdot \color{red}{5} &+& \color{blue}{3}  \cdot  \color{red}{4} \\[8pt]
& = & 6&+&10&+&12 & =&  28
\end{array}$$

1. [https://math.stackexchange.com/questions/2063241/matrix-multiplication-notation](https://math.stackexchange.com/questions/2063241/matrix-multiplication-notation)