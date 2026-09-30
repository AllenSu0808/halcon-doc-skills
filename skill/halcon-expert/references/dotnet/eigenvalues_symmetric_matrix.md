# EigenvaluesSymmetricMatrix (Operator)

## Name

`EigenvaluesSymmetricMatrix` — Compute the eigenvalues and optionally eigenvectors of a symmetric
matrix.

## Signature

`static void HOperatorSet.EigenvaluesSymmetricMatrix(HTuple matrixID, HTuple computeEigenvectors, out HTuple eigenvaluesID, out HTuple eigenvectorsID)`

`HMatrix HMatrix.EigenvaluesSymmetricMatrix(string computeEigenvectors, out HMatrix eigenvectorsID)`

## Description

The operator `EigenvaluesSymmetricMatrix` computes all
eigenvalues and, optionally, eigenvectors of the symmetric
`Matrix`. The matrix is defined by the matrix handle
*`matrixID`*. On output, a new matrix `Eigenvalues`
with the eigenvalues in ascending order and, optionally, a new matrix
`Eigenvectors` with the eigenvectors is created. The
operator returns the matrix handles *`eigenvaluesID`* and
*`eigenvectorsID`* of the matrices `Eigenvalues` and
`Eigenvectors`. Access to the elements of the matrices is
possible e.g., with the operator [`GetFullMatrix`](get_full_matrix.md).

The computation of eigenvectors can be selected via
*`computeEigenvectors`* = *"true"* or
*`computeEigenvectors`* = *"false"*.

*Example:*

*`computeEigenvectors`* = *"true"*
$$\mathrm{Matrix} = \begin{bmatrix}6.0 & 5.0 & 3.0\\ 5.0 & 7.0 & 3.0\\ 3.0 & 3.0 & 4.0\end{bmatrix}$$ ![figure](../assets/3e558ea955b87de4.svg)
$$\Rightarrow\\ Eigenvalues = \begin{bmatrix}1.4195\\2.1507\\13.4298\end{bmatrix} \\ Eigenvectors = \begin{bmatrix}0.7842 & 0.0626 & 0.6174\\-0.5667 & 0.4776 & 0.6714\\-0.2529 & -0.8763 & 0.4100\end{bmatrix}$$ ![figure](../assets/2db08116f7014ff1.svg)

## Attention

The upper triangular part of the input `Matrix` must
contain the relevant information of the matrix. The strictly
lower triangular part of the matrix is not referenced. If the
referenced part of the input `Matrix` is not of the
specified type, an exception is raised.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrixID`** (input_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix.

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
`EigenvaluesSymmetricMatrix` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Possible Successors

`GetFullMatrix`,
`GetValueMatrix`

## Alternatives

`EigenvaluesGeneralMatrix`

## See also

`GeneralizedEigenvaluesSymmetricMatrix`,
`GeneralizedEigenvaluesGeneralMatrix`

## References

David Poole: “Linear Algebra: A Modern Introduction”; Thomson;
Belmont; 2006.
  
Gene H. Golub, Charles F. van Loan: “Matrix Computations”; The
Johns Hopkins University Press; Baltimore and London; 1996.

## Module

Foundation
