# PowScalarElementMatrix (Operator)

## Name

`PowScalarElementMatrix` — Compute the power functions of the elements of a matrix.

## Signature

`static void HOperatorSet.PowScalarElementMatrix(HTuple matrixID, HTuple power, out HTuple matrixPowID)`

`HMatrix HMatrix.PowScalarElementMatrix(HTuple power)`

`HMatrix HMatrix.PowScalarElementMatrix(double power)`

## Description

The operator `PowScalarElementMatrix` computes the power of all
elements of the input `Matrix` by a constant value. The
input `Matrix` is given by the matrix handle
*`matrixID`*. The power value `Power` is given by the parameter
*`power`*. A new matrix `MatrixPow` is generated
with the result. The operator returns the matrix handle
*`matrixPowID`* of the matrix `MatrixPow`. Access
to the elements of the matrix is possible e.g., with the operator
[`GetFullMatrix`](get_full_matrix.md). The formula for the calculation of the
result is:

$$MatrixPower_{ij} = MatrixPower_{ij}$$ ![figure](../assets/c80736e01789be5a.svg)

*Example:*

*`power`* = *[2.0]*
$$\mathcal{Matrix} = \begin{bmatrix} 3.0 & 1.0 & 2.0 \\ 5.0 & 7.0 & 2.0 \\ 9.0 & 4.0 & 1.0 \\end{bmatrix}$$ ![figure](../assets/85a3cf83fb20e313.svg)
$$\rightarrow\ MatrixPow = \left[\begin{array}{ccc}9.0 & 1.0 & 4.0\\ 25.0 & 49.0 & 4.0\\ 81.0 & 16.0 & 1.0\end{array}\right]$$ ![figure](../assets/c2e003b9d67653dd.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrixID`** (input_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix.

**`power`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

The power.

Default:
2.0

Suggested values:
0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0

**`matrixPowID`** (output_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle with the raised power of the input
matrix.

## Result

If the parameters are valid, the operator
`PowScalarElementMatrix` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Possible Successors

`GetFullMatrix`,
`GetValueMatrix`

## Alternatives

`PowScalarElementMatrixMod`,
`PowElementMatrix`,
`PowElementMatrixMod`

## See also

`SqrtMatrix`,
`SqrtMatrixMod`

## Module

Foundation
