# TransposeMatrix (Operator)

## Name

`TransposeMatrix` — Transpose a matrix.

## Signature

`static void HOperatorSet.TransposeMatrix(HTuple matrixID, out HTuple matrixTransposedID)`

`HMatrix HMatrix.TransposeMatrix()`

## Description

The operator `TransposeMatrix` returns the transpose of the
input `Matrix`. The input matrix is defined by the matrix
handle *`matrixID`*. A new matrix `MatrixTransposed`
is generated with the result and the matrix handle
*`matrixTransposedID`* of this matrix is returned. Access
to the elements of the matrix is possible e.g., with the operator
[`GetFullMatrix`](get_full_matrix.md).

*Example:*

$$\text{Matrix} = \begin{bmatrix}3.0 & 1.0 & -2.0\\-5.0 & 7.0 & 2.0\\-9.0 & -4.0 & 1.0\end{bmatrix} \quad\rightarrow\quad \text{MatrixTransposed} = \begin{bmatrix}3.0 & -5.0 & -9.0\\1.0 & 7.0 & -4.0\\-2.0 & 2.0 & 1.0\end{bmatrix}$$ ![figure](../assets/71ba6d38a3d986c3.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrixID`** (input_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix.

**`matrixTransposedID`** (output_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle with the transpose of the input
matrix.

## Result

If the parameters are valid, the operator `TransposeMatrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Possible Successors

`GetFullMatrix`,
`GetValueMatrix`

## Alternatives

`TransposeMatrixMod`

## See also

`InvertMatrix`,
`InvertMatrixMod`

## References

David Poole: “Linear Algebra: A Modern Introduction”; Thomson;
Belmont; 2006.
  
Gene H. Golub, Charles F. van Loan: “Matrix Computations”; The
Johns Hopkins University Press; Baltimore and London; 1996.

## Module

Foundation
