# DivElementMatrixMod (Operator)

## Name

`DivElementMatrixMod` — Divide matrices element-by-element.

## Signature

`static void HOperatorSet.DivElementMatrixMod(HTuple matrixAID, HTuple matrixBID)`

`void HMatrix.DivElementMatrixMod(HMatrix matrixBID)`

## Description

The operator `DivElementMatrixMod` divides the two matrices
`MatrixA` and `MatrixB` element-by-element. The
matrices are given by the matrix handles *`matrixAID`* and
*`matrixBID`*. It is required that both input matrices have
identical dimensions. The input matrix `MatrixA` is
overwritten with the result. Access to the elements of the matrix
is possible e.g., with the operator [`GetFullMatrix`](get_full_matrix.md). The
formula for the calculation of the result is:
$$\texttt{MatrixA}_{ij}=\texttt{MatrixA}_{ij}/\texttt{MatrixB}_{ij}.$$

*Example:*

$$MatrixA = \begin{bmatrix}4.0 & 8.0 & 0.0\\-6.0 & 7.0 & 2.0\\-9.0 & 4.0 & 1.0\end{bmatrix}\nMatrixB = \begin{bmatrix}2.0 & 8.0 & -3.0\\-4.0 & -1.0 & 4.0\\-2.0 & -4.0 & 2.0\end{bmatrix}$$ ![figure](../assets/f5c6f8a0d8e82e22.svg)
$$\rightarrow \text{ MatrixA} = \left[\begin{array}{ccc} 2.0 & 1.0 & 0.0 \\ 1.5 & -7.0 & 0.5 \\ 4.5 & -1.0 & 0.5 \end{array}\right]$$ ![figure](../assets/25febbc36978431c.svg)

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

If the parameters are valid, the operator `DivElementMatrixMod`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Possible Successors

`GetFullMatrix`,
`GetValueMatrix`

## Alternatives

`DivElementMatrix`

## See also

`MultElementMatrix`,
`MultElementMatrixMod`,
`ScaleMatrix`,
`ScaleMatrixMod`

## Module

Foundation
