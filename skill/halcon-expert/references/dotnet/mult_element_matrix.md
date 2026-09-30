# MultElementMatrix (Operator)

## Name

`MultElementMatrix` — Multiply matrices element-by-element.

## Signature

`static void HOperatorSet.MultElementMatrix(HTuple matrixAID, HTuple matrixBID, out HTuple matrixMultID)`

`HMatrix HMatrix.MultElementMatrix(HMatrix matrixBID)`

## Description

The operator `MultElementMatrix` multiplies the two matrices
`MatrixA` and `MatrixB` element-by-element. The
matrices are defined by the matrix handles *`matrixAID`* and
*`matrixBID`*. It is required that both input matrices have
identical dimensions. A new matrix `MatrixMult` is
generated with the result. The operator returns the matrix handle
*`matrixMultID`* of the matrix `MatrixMult`. Access
to the elements of the matrix is possible e.g., with the operator
[`GetFullMatrix`](get_full_matrix.md). The formula for the calculation of the
result is:
$$\texttt{MatrixMult}_{ij}=\texttt{MatrixA}_{ij}\cdot\texttt{MatrixB}_{ij}.$$

*Example:*

$$MatrixA = \begin{bmatrix}4.0 & 8.0 & 0.0\\-6.0 & 7.0 & 2.0\\-9.0 & 4.0 & 1.0\end{bmatrix}\nMatrixB = \begin{bmatrix}2.0 & 8.0 & -3.0\\-4.0 & -1.0 & 4.0\\-2.0 & -4.0 & 2.0\end{bmatrix}$$ ![figure](../assets/f5c6f8a0d8e82e22.svg)
$$\rightarrow\ MatrixMulti = \begin{bmatrix}8.0 & 64.0 & 0.0\\24.0 & -7.0 & 8.0\\18.0 & -16.0 & 2.0\end{bmatrix}$$ ![figure](../assets/7d205145af4b0ef0.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrixAID`** (input_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix A.

**`matrixBID`** (input_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix B.

**`matrixMultID`** (output_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle with the multiplied values of the
input matrices.

## Result

If the parameters are valid, the operator
`MultElementMatrix` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Possible Successors

`GetFullMatrix`,
`GetValueMatrix`

## Alternatives

`MultElementMatrixMod`

## See also

`DivElementMatrix`,
`DivElementMatrixMod`,
`ScaleMatrix`,
`ScaleMatrixMod`

## Module

Foundation
