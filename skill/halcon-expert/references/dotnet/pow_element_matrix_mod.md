# PowElementMatrixMod (Operator)

## Name

`PowElementMatrixMod` — Compute the power functions of the elements of a matrix.

## Signature

`static void HOperatorSet.PowElementMatrixMod(HTuple matrixID, HTuple matrixExpID)`

`void HMatrix.PowElementMatrixMod(HMatrix matrixExpID)`

## Description

The operator `PowElementMatrixMod` computes the power of
all elements of the input `Matrix` with the elements of
the input matrix `MatrixExp`. The input matrices
`Matrix` and `MatrixExp` are defined by the matrix
handles *`matrixID`* and *`matrixExpID`*. Both matrices
must have identical dimensions. The input `Matrix` is
overwritten with the result. Access to the elements of the matrix
is possible e.g., with the operator [`GetFullMatrix`](get_full_matrix.md). The
formula for the calculation of the result is:
$$\mathrm{Matrix}_{ij} = \mathrm{Matrix}_{ij} \, \mathrm{MatrixExp}_{ij}.$$ ![figure](../assets/ed13181a27e35160.svg)

*Example:*

$$\text{Matrix} = \begin{bmatrix}3.0 & 1.0 & 2.0\\ 5.0 & 7.0 & 2.0\\ 9.0 & 4.0 & 1.0\end{bmatrix} \\\n\text{MatrixExp} = \begin{bmatrix}1.0 & 2.0 & 2.0\\ 2.0 & 0.0 & 3.0\\ 0.5 & 3.0 & 1.0\end{bmatrix}$$ ![figure](../assets/76c8f3ab42968aa2.svg)
$$\rightarrow\quad\text{Matrix}=\left[\begin{array}{ccc}3.0 & 1.0 & 4.0\\ 25.0 & 1.0 & 8.0\\ 3.0 & 64.0 & 1.0\end{array}\right]$$ ![figure](../assets/9423f1394904e698.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- matrixID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`matrixID`** (input_control, state is modified)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix of the base.

**`matrixExpID`** (input_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix with exponents.

## Result

If the parameters are valid, the operator
`PowElementMatrixMod` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Possible Successors

`GetFullMatrix`,
`GetValueMatrix`

## Alternatives

`PowElementMatrix`,
`PowScalarElementMatrix`,
`PowScalarElementMatrixMod`

## See also

`SqrtMatrix`,
`SqrtMatrixMod`

## Module

Foundation
