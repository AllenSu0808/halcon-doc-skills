# solve_matrix (Operator)

## Name

`solve_matrix` — Compute the solution of a system of equations.

## Signature

`solve_matrix( : : MatrixLHSID, MatrixLHSType, Epsilon, MatrixRHSID : MatrixResultID)`

## Description

The operator `solve_matrix` computes the solution of a system
of linear equations or of a linear least squares problem. The input
matrices `MatrixLHS` and `MatrixRHS` are defined by
the matrix handles *`MatrixLHSID`* and *`MatrixRHSID`*.
The number of rows of matrices `MatrixLHS` and
`MatrixRHS` must be identical. The operator returns the
matrix handle *`MatrixResultID`* of the matrix
`MatrixResult`. Access to the elements of the matrix is
possible e.g., with the operator [`get_full_matrix`](get_full_matrix.md).

For linear equation systems, the equations
$$\texttt{MatrixLHS}\cdot\texttt{MatrixResult}=\texttt{MatrixRHS}$$
are solved. Therefore, the matrix `MatrixLHS` must be a
square matrix and the parameter *`Epsilon`* must be 0. The
type of the matrix `MatrixLHS` can be selected via the
parameter *`MatrixLHSType`*. The following values are
supported: *'general'* for general, *'symmetric'* for
symmetric, *'positive_definite'* for symmetric positive
definite, *'tridiagonal'* for tridiagonal,
*'upper_triangular'* for upper triangular,
*'permuted_upper_triangular'* for permuted upper triangular,
*'lower_triangular'* for lower triangular, and
*'permuted_lower_triangular'* for permuted lower triangular
matrices.

*Example:*

*`MatrixLHSType`* = *'positive_definite'*,
*`Epsilon`* = *0*
$$MatrixLHS = \begin{bmatrix}6.0 & 5.0 & 3.0\\ 5.0 & 7.0 & 3.0\\ 3.0 & 3.0 & 4.0\end{bmatrix} \\\nMatrixRHS = \begin{bmatrix}-1.0 & 6.0\\ 3.0 & -3.0\\ 5.0 & 4.0\end{bmatrix}$$ ![figure](../assets/d8131b2f122e0ee3.svg)
$$\rightarrow MatrixResult = \left[\begin{array}{cc} -2.0 & 3.0 \\\ 1.0 & -3.0 \\\ 2.0 & 1.0 \end{array}\right]$$ ![figure](../assets/f49ac22e336f70ae.svg)

For linear least squares problems or if *`Epsilon`* is not 0,
the matrix `MatrixLHS` need not be a square matrix. The
linear least squares problem is solved using the singular value
decomposition (SVD) of the matrix `MatrixLHS` by minimizing
$$||\texttt{MatrixRHS}-\texttt{MatrixLHS}\cdot\texttt{MatrixResult}||.$$
All singular values less than the value Epsilon $\times$ the
largest singular value are set to 0. For these values no
internal division is done to prevent a division by zero.
Also, the matrix `MatrixLHS` may be rank-deficient. The
type of matrix must be selected via *`MatrixLHSType`* =
*'general'*.

*Example:*

*`MatrixLHSType`* = *'general'*,
*`Epsilon`* = *2.2204e-16*
$$\mathbf{MatrixHS = [6.0\;5.0\;3.0\\ 3.0\;7.0\;-3.0\\ 5.0\;12.0\;4.0\\ 5.0\;4.0\;12.0\\ 4.0\;6.0\;8.0]^{\mathrm{T}}}\n\mathbf{MatrixRHS = [29.0\\ 10.0\\ 35.0\\ 43.0\\ 25.0]^{\mathrm{T}}$$ ![figure](../assets/d03bb53afcd275f1.svg)
$$\rightarrow\ MatrixResult = \begin{bmatrix} 3.4914 \\ 0.7114 \\ 1.6213 \end{bmatrix}$$ ![figure](../assets/d26b68f4c9242be6.svg)

Note: The relative accuracy of the floating point representation of
the used data type (double) is *`Epsilon`* = 2.2204e-16.

## Attention

For *`MatrixLHSType`* = *'symmetric'*,
*'positive_definite'*, or *'upper_triangular'* the
upper triangular part of the input `MatrixLHS` must contain
the relevant information of the matrix. The strictly lower
triangular part of the matrix is not referenced. For
*`MatrixLHSType`* = *'lower_triangular'* the lower
triangular part of the input `MatrixLHS` must contain the
relevant information of the matrix. The strictly upper triangular
part of the matrix is not referenced. For *`MatrixLHSType`* =
*'tridiagonal'*, only the main diagonal, the superdiagonal,
and the subdiagonal of the input `MatrixLHS` are used. The
other parts of the matrix are not referenced. If the referenced
part of the input `MatrixLHS` is not of the specified type,
an exception is raised.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MatrixLHSID`** (input_control)  matrix `→`  (handle)

Matrix handle of the input matrix of the left
hand side.

**`MatrixLHSType`** (input_control)  string `→`  (string)

The type of the input matrix of the left hand side.

Default:
'general'

List of values:
'general', 'lower_triangular', 'permuted_lower_triangular', 'permuted_upper_triangular', 'positive_definite', 'symmetric', 'tridiagonal', 'upper_triangular'

**`Epsilon`** (input_control)  real `→`  (real)

Type of solving and limitation to set singular
values to be 0.

Default:
0.0

Suggested values:
0.0, 2.2204e-16

**`MatrixRHSID`** (input_control)  matrix `→`  (handle)

Matrix handle of the input matrix of right hand
side.

**`MatrixResultID`** (output_control)  matrix `→`  (handle)

New matrix handle with the solution.

## Result

If the parameters are valid, the operator `solve_matrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_matrix`

## Possible Successors

`get_full_matrix`,
`get_value_matrix`

## References

David Poole: “Linear Algebra: A Modern Introduction”; Thomson;
Belmont; 2006.
  
Gene H. Golub, Charles F. van Loan: “Matrix Computations”; The
Johns Hopkins University Press; Baltimore and London; 1996.

## Module

Foundation
