# TransposeMatrixMod (Operator)

## Name

`TransposeMatrixMod` — Transpose a matrix.

## Signature

`static void HOperatorSet.TransposeMatrixMod(HTuple matrixID)`

`void HMatrix.TransposeMatrixMod()`

## Description

The operator `TransposeMatrixMod` returns the transpose of
the input `Matrix`. The input matrix is defined by the
matrix handle *`matrixID`*. The input matrix is overwritten
with the result. Access to the elements of the matrix is possible
e.g., with the operator [`GetFullMatrix`](get_full_matrix.md).

*Example:*

$$\mathbf{Matrix}=\begin{bmatrix}3.0 & 1.0 & -2.0\\-5.0 & 7.0 & 2.0\\-9.0 & -4.0 & 1.0\end{bmatrix} \quad\rightarrow\quad \mathbf{Matrix}=\begin{bmatrix}3.0 & -5.0 & -9.0\\1.0 & 7.0 & -4.0\\-2.0 & 2.0 & 1.0\end{bmatrix}$$ ![figure](../assets/112a08e61d4347d3.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- matrixID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`matrixID`** (input_control, state is modified)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix.

## Result

If the parameters are valid, the operator `TransposeMatrixMod`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Possible Successors

`GetFullMatrix`,
`GetValueMatrix`

## Alternatives

`TransposeMatrix`

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
