# SqrtMatrix (Operator)

## Name

`SqrtMatrix` — Compute the square root values of the elements of a matrix.

## Signature

`static void HOperatorSet.SqrtMatrix(HTuple matrixID, out HTuple matrixSqrtID)`

`HMatrix HMatrix.SqrtMatrix()`

## Description

The operator `SqrtMatrix` computes the square root values of
all elements of the input `Matrix` given by the matrix handle
*`matrixID`*. A new matrix `MatrixSqrt` is generated
with the result. The operator returns the matrix handle
*`matrixSqrtID`* of the matrix `MatrixSqrt`. Access
to the elements of the matrix is possible e.g., with the operator
[`GetFullMatrix`](get_full_matrix.md). The formula for the calculation of the
result is:
$$MatrixSqrt_{ij} = \sqrt{Matrix_{ij}}$$ ![figure](../assets/3a459d01159339ad.svg)

*Example:*

$$\text{Matrix}=\begin{bmatrix}3.0&1.0&2.0\\5.0&7.0&2.0\\9.0&4.0&1.0\end{bmatrix} \quad\rightarrow\quad \text{MatrixSqrt}=\begin{bmatrix}1.7321&1.0000&1.4142\\2.2361&2.6458&1.4142\\3.0000&2.0000&1.0000\end{bmatrix}$$ ![figure](../assets/d4b5058293161a5c.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrixID`** (input_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix.

**`matrixSqrtID`** (output_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle with the square root values of the
input matrix.

## Result

If the parameters are valid, the operator `SqrtMatrix` returns
the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Possible Successors

`GetFullMatrix`,
`GetValueMatrix`

## Alternatives

`SqrtMatrixMod`

## See also

`PowScalarElementMatrix`,
`PowScalarElementMatrixMod`

## Module

Foundation
