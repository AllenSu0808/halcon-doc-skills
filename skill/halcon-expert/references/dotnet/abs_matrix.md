# AbsMatrix (Operator)

## Name

`AbsMatrix` — Compute the absolute values of the elements of a matrix.

## Signature

`static void HOperatorSet.AbsMatrix(HTuple matrixID, out HTuple matrixAbsID)`

`HMatrix HMatrix.AbsMatrix()`

## Description

The operator `AbsMatrix` computes the absolute values of all
elements of the input `Matrix` given by the matrix handle
*`matrixID`*. A new matrix `MatrixAbs` is generated
with the result. The operator returns the matrix handle
*`matrixAbsID`* of the matrix `MatrixAbs`. Access
to the elements of the matrix is possible e.g., with the operator
[`GetFullMatrix`](get_full_matrix.md). The formula for the calculation of the
result is:
$$\texttt{MatrixAbs}_{ij}=|\texttt{Matrix}_{ij}|.$$

*Example:*

$$\text{Matrix} = \begin{bmatrix}3.0 & 1.0 & -2.0\\-5.0 & 7.0 & 2.0\\-9.0 & -4.0 & 1.0\end{bmatrix} \quad\rightarrow\quad \text{MatrixAbs} = \begin{bmatrix}3.0 & 1.0 & 2.0\\5.0 & 7.0 & 2.0\\9.0 & 4.0 & 1.0\end{bmatrix}$$ ![figure](../assets/144398b506625bdd.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrixID`** (input_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix.

**`matrixAbsID`** (output_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle with the absolute values of the input
matrix.

## Result

If the parameters are valid, the operator `AbsMatrix` returns
the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Possible Successors

`GetFullMatrix`,
`GetValueMatrix`

## Alternatives

`AbsMatrixMod`

## Module

Foundation
