# MultElementMatrixMod (Operator)

## Name

`MultElementMatrixMod` — Multiply matrices element-by-element.

## Signature

`static void HOperatorSet.MultElementMatrixMod(HTuple matrixAID, HTuple matrixBID)`

`void HMatrix.MultElementMatrixMod(HMatrix matrixBID)`

## Description

The operator `MultElementMatrixMod` multiplies the two
matrices `MatrixA` and `MatrixB` element-by-element.
The matrices are defined by the matrix handles *`matrixAID`*
and *`matrixBID`*. It is required that both input matrices
have identical dimensions. The input matrix `MatrixA` is
overwritten with the result. Access to the elements of the matrix
is possible e.g., with the operator [`GetFullMatrix`](get_full_matrix.md). The
formula for the calculation of the result is:
$$\texttt{MatrixA}_{ij}=\texttt{MatrixA}_{ij}\cdot\texttt{MatrixB}_{ij}.$$

*Example:*

$$MatrixA = \begin{bmatrix}4.0 & 8.0 & 0.0\\-6.0 & 7.0 & 2.0\\-9.0 & 4.0 & 1.0\end{bmatrix}\nMatrixB = \begin{bmatrix}2.0 & 8.0 & -3.0\\-4.0 & -1.0 & 4.0\\-2.0 & -4.0 & 2.0\end{bmatrix}$$ ![figure](../assets/f5c6f8a0d8e82e22.svg)
$$\rightarrow MatrixA = \begin{bmatrix} 8.0 & 64.0 & 0.0 \\ 24.0 & -7.0 & 8.0 \\ 18.0 & -16.0 & 2.0 \end{bmatrix}$$ ![figure](../assets/9021e3690b44757b.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- matrixAID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`matrixAID`** (input_control, state is modified)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix A.

**`matrixBID`** (input_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix B.

## Result

If the parameters are valid, the operator
`MultElementMatrixMod` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Possible Successors

`GetFullMatrix`,
`GetValueMatrix`

## Alternatives

`MultElementMatrix`

## See also

`DivElementMatrix`,
`DivElementMatrixMod`,
`ScaleMatrix`,
`ScaleMatrixMod`

## Module

Foundation
