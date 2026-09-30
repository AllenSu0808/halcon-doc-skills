# DecomposeMatrix (Operator)

## Name

`DecomposeMatrix` — Decompose a matrix.

## Signature

`static void HOperatorSet.DecomposeMatrix(HTuple matrixID, HTuple matrixType, out HTuple matrix1ID, out HTuple matrix2ID)`

`HMatrix HMatrix.DecomposeMatrix(string matrixType, out HMatrix matrix2ID)`

## Description

The operator `DecomposeMatrix` decomposes the square input
`Matrix` given by the matrix handle *`matrixID`*. The
results are stored in two generated matrices `Matrix1` and
`Matrix2`. The operator returns the matrix handles
*`matrix1ID`* and *`matrix2ID`*. Access to the elements
of the matrices is possible e.g., with the operator
[`GetFullMatrix`](get_full_matrix.md).

The type of the input `Matrix` can be selected via the
parameter *`matrixType`*. The following values are supported:
*"general"* for general, *"symmetric"* for symmetric,
*"positive_definite"* for symmetric positive definite, and
*"tridiagonal"* for tridiagonal matrices.

The decomposition *`matrixType`* = *"general"* or
*"tridiagonal"* is a LU factorization (Lower/Upper) with the
form
$$\texttt{Matrix}=\texttt{Matrix1}\cdot\texttt{Matrix2}.$$
The output `Matrix1` is a lower triangular matrix with unit
diagonal elements and interchanged rows. The output
`Matrix2` is an upper triangular matrix.

*Example for a factorization of a general matrix:*
$$\begin{bmatrix}5.0 & -3.0 & 1.0\\ 0.0 & 2.0 & -1.0\\ -5.0 & -1.0 & 5.0\end{bmatrix}$$ ![figure](../assets/ac0cda90882eb510.svg)
$$\rightarrow\quad Matrix1 = \begin{bmatrix}1 & 0 & 0\\ 0.0 & -0.5 & 1\\ -1.0 & 1 & 0\end{bmatrix}\quad Matrix2 = \begin{bmatrix}5.0 & -3.0 & 1.0\\ 0 & -4.0 & 6.0\\ 0 & 0 & 2.0\end{bmatrix}$$ ![figure](../assets/31187708ad180b61.svg)

*Example for a factorization of a tridiagonal matrix:*
$$\mathrm{Matrix} = \begin{bmatrix}-8.0 & -8.0 & 0.0 & 0.0\\-8.0 & 6.0 & -4.0 & 0.0\\0.0 & 7.0 & -2.0 & 7.0\\0.0 & 0.0 & 5.0 & -3.0\end{bmatrix}$$ ![figure](../assets/6afd4fd0f1050489.svg)
$$\text{Matrix} \;\text{Matrix1} = \begin{bmatrix}1 & 0 & 0 & 0\\1.0 & 1 & 0 & 0\\0.0 & 0.5 & 0.0 & 1\\0.0 & 0.0 & 1 & 0\end{bmatrix} \qquad \text{Matrix2} = \begin{bmatrix}-8.0 & -8.0 & 0.0 & 0.0\\0 & 14.0 & -4.0 & 0.0\\0 & 0 & 5.0 & -3.0\\0 & 0 & 0 & 7.0\end{bmatrix}$$ ![figure](../assets/9650045154f263d4.svg)

For *`matrixType`* = *"symmetric"* the factorization is
a UDU^T decomposition (Upper/Diagonal/Upper) with the form
$$\texttt{Matrix}=\texttt{Matrix1}\cdot\texttt{Matrix2}\cdot\texttt{Matrix1}^{T}$$
where the output `Matrix1` is an upper triangular matrix
with interchanged columns. The output matrix `Matrix2` is
a symmetric block diagonal matrix with $1\times1$ and
$2\times2$ diagonal blocks.

*Example for a factorization of a symmetric matrix:*
$$\mathrm{Matrix} = \left[\begin{array}{rrrr}3.0 & -2.0 & 7.0 & -1.0\\-2.0 & -2.0 & 4.0 & 0.0\\7.0 & 4.0 & 8.0 & 1.0\\-1.0 & 0.0 & 1.0 & 0.0\end{array}\right]$$ ![figure](../assets/01747d34eb6f2f39.svg)
$$\text{Matrix1} = \left[\begin{array}{rrrr}\;0&0&1&0.0\\0&1&0.0&2.0\\1&-1.0&-1.0&-10.0\\0&0&0&1\end{array}\right] \\ \\text{Matrix2} = \left[\begin{array}{rrrr}27.0&0&0&0\\0&-2.0&0&0\\0&0&3.0&-1.0\\0&0&-1.0&0.0\end{array}\right]$$ ![figure](../assets/f67075fe0dc56e42.svg)

For *`matrixType`* = *"positive_definite"* a Cholesky
factorization is computed with the form
$$\texttt{Matrix}=\texttt{Matrix1}\cdot\texttt{Matrix2}.$$
where the output `Matrix1` is a lower triangular matrix and
the output matrix `Matrix2` is an upper triangular matrix.
Furthermore, the `Matrix2` is the transpose of the matrix
`Matrix1`.

*Example for a factorization of a positive definite matrix:*
$$\mathrm{Matrix} = \begin{bmatrix} 9.0 & 12.0 & -6.0 \\ 12.0 & 17.0 & -7.0 \\ -6.0 & -7.0 & 14.0 \end{bmatrix}$$ ![figure](../assets/6a7b8a43a065b439.svg)
$$\rightarrow \\text{Matrix1} = \left[\begin{array}{ccc}3.0 & 0 & 0 \\ 4.0 & 1.0 & 0 \\ -2.0 & 1.0 & 3.0\end{array}\right] \\text{Matrix2} = \\left[\begin{array}{ccc}3.0 & 4.0 & -2.0 \\ 0 & 1.0 & 1.0 \\ 0 & 0 & 3.0\end{array}\right]$$ ![figure](../assets/73d84e6af57bda80.svg)

It should be noted that in the examples there are differences in the
meaning of the values of the output matrices: If a value is shown as
an integer number, e.g., 0 or 1, the value of this element is per
definition this certain value. If the number is shown as a floating
point number, e.g., 0.0 or 1.0, the value is computed by the
operator.

## Attention

For *`matrixType`* = *"symmetric"* or
*"positive_definite"*, the upper triangular part of the input
`Matrix` must contain the relevant information of the matrix.
The strictly lower triangular part of the matrix is not referenced.
For *`matrixType`* = *"tridiagonal"*, only the main
diagonal, the superdiagonal, and the subdiagonal of the input
`Matrix` are used. The other parts of the matrix are not
referenced. If the referenced part of the input `Matrix` is
not of the specified type, an exception is raised.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrixID`** (input_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix.

**`matrixType`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of the input matrix.

Default:
"general"

List of values:
"general", "positive_definite", "symmetric", "tridiagonal"

**`matrix1ID`** (output_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle with the output matrix 1.

**`matrix2ID`** (output_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle with the output matrix 2.

## Result

If the parameters are valid, the operator `DecomposeMatrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Possible Successors

`GetFullMatrix`,
`GetValueMatrix`

## Alternatives

`OrthogonalDecomposeMatrix`,
`SolveMatrix`

## References

David Poole: “Linear Algebra: A Modern Introduction”; Thomson;
Belmont; 2006.
  
Gene H. Golub, Charles F. van Loan: “Matrix Computations”; The
Johns Hopkins University Press; Baltimore and London; 1996.

## Module

Foundation
