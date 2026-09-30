# GeneralizedEigenvaluesSymmetricMatrix (Operator)

## Name

`GeneralizedEigenvaluesSymmetricMatrix` — Compute the generalized eigenvalues and optionally generalized
eigenvectors of symmetric input matrices.

## Signature

`static void HOperatorSet.GeneralizedEigenvaluesSymmetricMatrix(HTuple matrixAID, HTuple matrixBID, HTuple computeEigenvectors, out HTuple eigenvaluesID, out HTuple eigenvectorsID)`

`HMatrix HMatrix.GeneralizedEigenvaluesSymmetricMatrix(HMatrix matrixBID, string computeEigenvectors, out HMatrix eigenvectorsID)`

## Description

The operator `GeneralizedEigenvaluesSymmetricMatrix`
computes all generalized eigenvalues and, optionally, generalized
eigenvectors of the symmetric matrix `MatrixA` and the
symmetric positive definite matrix `MatrixB`. Both
matrices must have identical dimensions. The matrices are
defined by the matrix handles *`matrixAID`* and
*`matrixBID`*. On output, a new matrix `Eigenvalues`
with the generalized eigenvalues in ascending order and,
optionally, a new matrix
`Eigenvectors` with the generalized eigenvectors is
created. Each jth column of the matrix `Eigenvectors`
contains the related eigenvector to the jth eigenvalue. The
operator returns the matrix handles *`eigenvaluesID`* and
*`eigenvectorsID`* of the matrices `Eigenvalues` and
`Eigenvectors`. Access to the elements of the matrices is
possible, e.g., with the operator [`GetFullMatrix`](get_full_matrix.md) or
[`GetSubMatrix`](get_sub_matrix.md).

The computation of generalized eigenvectors can be selected via
*`computeEigenvectors`* = *"true"*. The formula for
the calculation of the result is
$$\texttt{MatrixA}\cdot x_{j}=\lambda_{j}\cdot\texttt{MatrixB}\cdot x_{j},$$
with $\lambda_{j}$ representing the $j$th eigenvalue and $x_{j}$
represents the corresponding eigenvector.

If *`computeEigenvectors`* = *"false"*, no generalized
eigenvectors are computed. For this, the matrix handle
*`eigenvectorsID`* is invalid.

*Example:*

*`computeEigenvectors`* = *"true"*
$$MatrixA = \begin{bmatrix}4.0 & -3.0 & 2.0\\-3.0 & 1.0 & 4.0\\2.0 & 4.0 & 8.0\end{bmatrix}\nMatrixB = \begin{bmatrix}6.0 & 5.0 & 3.0\\5.0 & 7.0 & 3.0\\3.0 & 3.0 & 4.0\end{bmatrix}$$ ![figure](../assets/37f761fb64921d8f.svg)
$$\rightarrow\enspace\text{Eigenvalues} = \left[\begin{array}{ccc}\,-0.4463\\ 1.8747\\ 4.5472\end{array}\right]\\\enspace\text{Eigenvectors} = \left[\begin{array}{ccc}-0.1579 & 0.1851 & -0.6358\\-0.3377 & -0.2568 & 0.4311\\ 0.2382 & 0.5065 & 0.3185\end{array}\right]$$ ![figure](../assets/6e674dd6d5c73f10.svg)

## Attention

The upper triangular parts of the input matrices `MatrixA`
and `MatrixB` must contain the relevant information of the
matrices. The strictly lower triangular parts of the matrices are
not referenced. If the referenced parts of the input matrices
`MatrixA` or `MatrixB` are not of the specified
type, an exception is raised.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrixAID`** (input_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the symmetric input matrix A.

**`matrixBID`** (input_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the symmetric positive
definite input matrix B.

**`computeEigenvectors`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Computation of the eigenvectors.

Default:
"false"

List of values:
"false", "true"

**`eigenvaluesID`** (output_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle with the eigenvalues.

**`eigenvectorsID`** (output_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle with the eigenvectors.

## Result

If the parameters are valid, the operator
`GeneralizedEigenvaluesSymmetricMatrix` returns the value
2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Possible Successors

`GetFullMatrix`,
`GetValueMatrix`

## Alternatives

`GeneralizedEigenvaluesGeneralMatrix`

## See also

`EigenvaluesSymmetricMatrix`,
`EigenvaluesGeneralMatrix`

## References

David Poole: “Linear Algebra: A Modern Introduction”; Thomson;
Belmont; 2006.
  
Gene H. Golub, Charles F. van Loan: “Matrix Computations”; The
Johns Hopkins University Press; Baltimore and London; 1996.

## Module

Foundation
