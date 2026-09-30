# SubMatrix (Operator)

## Name

`SubMatrix` — Subtract two matrices.

## Signature

`static void HOperatorSet.SubMatrix(HTuple matrixAID, HTuple matrixBID, out HTuple matrixSubID)`

`HMatrix HMatrix.SubMatrix(HMatrix matrixBID)`

## Description

The operator `SubMatrix` computes the difference of the input
matrices `MatrixA` and `MatrixB` given by the matrix
handles *`matrixAID`* and *`matrixBID`*. Both matrices
must have identical dimensions. A new matrix `MatrixSub` is
generated with the result. The operator returns the matrix handle
*`matrixSubID`* of the matrix `MatrixSub`. Access
to the elements of the matrix is possible e.g., with the operator
[`GetFullMatrix`](get_full_matrix.md). The formula for the calculation of the
result is:
$$\texttt{MatrixSub}=\texttt{MatrixA}-\texttt{MatrixB}.$$

*Example:*

$$MatrixA = \begin{bmatrix}3.0 & 1.0 & -2.0\\-5.0 & 7.0 & 2.0\\-9.0 & -4.0 & 1.0\end{bmatrix} \\ MatrixB = \begin{bmatrix}2.0 & 8.0 & -3.0\\-4.0 & -1.0 & 5.0\\2.0 & -4.0 & 7.0\end{bmatrix}$$ ![figure](../assets/fcc47e502c3725e8.svg)
$$\rightarrow\quad \mathrm{MatrixSub} = \left[\begin{array}{ccc} 1.0 & -7.0 & 1.0 \\ -1.0 & 8.0 & -3.0 \\ -11.0 & 0.0 & -6.0 \end{array}\right]$$ ![figure](../assets/bdb58297056593e4.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrixAID`** (input_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix A.

**`matrixBID`** (input_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix B.

**`matrixSubID`** (output_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle with the difference of the input
matrices.

## Result

If the parameters are valid, the operator `SubMatrix` returns
the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Possible Successors

`GetFullMatrix`,
`GetValueMatrix`

## Alternatives

`SubMatrixMod`

## See also

`AddMatrix`,
`AddMatrixMod`

## Module

Foundation
