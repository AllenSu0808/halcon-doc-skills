# CopyMatrix (Operator)

## Name

`CopyMatrix` — Copy a matrix.

## Signature

`static void HOperatorSet.CopyMatrix(HTuple matrixID, out HTuple matrixCopyID)`

`HMatrix HMatrix.CopyMatrix()`

## Description

The operator `CopyMatrix` creates the new matrix
`MatrixCopy` and copies all elements of the input
`Matrix` to this new matrix. The input `Matrix` is
defined by the matrix handle *`matrixID`*. The operator
returns the matrix handle *`matrixCopyID`* of the matrix
`MatrixCopy`. Access to the elements of the matrix is
possible e.g., with the operator [`GetFullMatrix`](get_full_matrix.md).
With this operator a matrix can be saved
before the matrix is modified by the operators
[`SetValueMatrix`](set_value_matrix.md), [`SetFullMatrix`](set_full_matrix.md),
[`SetSubMatrix`](set_sub_matrix.md), or [`SetDiagonalMatrix`](set_diagonal_matrix.md).

*Example:*

$$\text{Matrix} = \begin{bmatrix}3.0 & 1.0 & -2.0\\-5.0 & 7.0 & 2.0\\-9.0 & -4.0 & 1.0\end{bmatrix} \quad\rightarrow\quad \text{MatrixCopy} = \begin{bmatrix}3.0 & 1.0 & -2.0\\-5.0 & 7.0 & 2.0\\-9.0 & -4.0 & 1.0\end{bmatrix}$$ ![figure](../assets/22d68611fb79d8b2.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrixID`** (input_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix.

**`matrixCopyID`** (output_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the copied matrix.

## Result

If the parameters are valid, the operator `CopyMatrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Possible Successors

`GetFullMatrix`,
`GetValueMatrix`

## Alternatives

`RepeatMatrix`

## Module

Foundation
