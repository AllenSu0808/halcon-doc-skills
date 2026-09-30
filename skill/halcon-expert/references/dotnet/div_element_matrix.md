# DivElementMatrix (Operator)

## Name

`DivElementMatrix` — Divide matrices element-by-element.

## Signature

`static void HOperatorSet.DivElementMatrix(HTuple matrixAID, HTuple matrixBID, out HTuple matrixDivID)`

`HMatrix HMatrix.DivElementMatrix(HMatrix matrixBID)`

## Description

The operator `DivElementMatrix` divides the two matrices
`MatrixA` and `MatrixB` element-by-element. The
matrices are given by the matrix handles *`matrixAID`* and
*`matrixBID`*. It is required that both input matrices have
identical dimensions. The new created output `MatrixDiv`
contains the result. The operator returns the matrix handle
*`matrixDivID`* of the matrix `MatrixDiv`. Access
to the elements of the matrix is possible e.g., with the operator
[`GetFullMatrix`](get_full_matrix.md). The formula for the calculation of the
result is:
$$\texttt{MatrixDiv}_{ij}=\texttt{MatrixA}_{ij}/\texttt{MatrixB}_{ij}.$$

*Example:*

$$MatrixA = \begin{bmatrix}4.0 & 8.0 & 0.0\\-6.0 & 7.0 & 2.0\\-9.0 & 4.0 & 1.0\end{bmatrix}\nMatrixB = \begin{bmatrix}2.0 & 8.0 & -3.0\\-4.0 & -1.0 & 4.0\\-2.0 & -4.0 & 2.0\end{bmatrix}$$ ![figure](../assets/f5c6f8a0d8e82e22.svg)
$$\rightarrow\quad \mathrm{MatrixDiv} = \left[\begin{array}{ccc}2.0 & 1.0 & 0.0\\ 1.5 & -7.0 & 0.5\\ 4.5 & -1.0 & 0.5\end{array}\right]$$ ![figure](../assets/2ec6ebab689bfaeb.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrixAID`** (input_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix A.

**`matrixBID`** (input_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix B.

**`matrixDivID`** (output_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle with the divided values of input
matrices.

## Result

If the parameters are valid, the operator `DivElementMatrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Possible Successors

`GetFullMatrix`,
`GetValueMatrix`

## Alternatives

`DivElementMatrixMod`

## See also

`MultElementMatrix`,
`MultElementMatrixMod`,
`ScaleMatrix`,
`ScaleMatrixMod`

## Module

Foundation
