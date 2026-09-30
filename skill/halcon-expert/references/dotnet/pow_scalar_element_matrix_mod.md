# PowScalarElementMatrixMod (Operator)

## Name

`PowScalarElementMatrixMod` — Compute the power functions of the elements of a matrix.

## Signature

`static void HOperatorSet.PowScalarElementMatrixMod(HTuple matrixID, HTuple power)`

`void HMatrix.PowScalarElementMatrixMod(HTuple power)`

`void HMatrix.PowScalarElementMatrixMod(double power)`

## Description

The operator `PowScalarElementMatrixMod` computes the
power of all elements of the input `Matrix` by a constant
value. The input `Matrix` is given by the matrix handle
*`matrixID`*. The power value is given by the parameter
*`power`*. The input matrix is overwritten with the result.
Access to the elements of the matrix is possible e.g., with the
operator [`GetFullMatrix`](get_full_matrix.md). The formula for the calculation
of the result is:

$$\mathrm{Matrix}_{ij} = \mathrm{Matrix}_{ij} \text{Power}.$$ ![figure](../assets/414a5c71610ee169.svg)

*Example:*

*`power`* = *[2.0]*
$$\mathcal{Matrix} = \begin{bmatrix} 3.0 & 1.0 & 2.0 \\ 5.0 & 7.0 & 2.0 \\ 9.0 & 4.0 & 1.0 \\end{bmatrix}$$ ![figure](../assets/85a3cf83fb20e313.svg)
$$\rightarrow\; \text{Matrix} = \begin{bmatrix} 9.0 & 1.0 & 4.0 \\ 25.0 & 49.0 & 4.0 \\ 81.0 & 16.0 & 1.0 \end{bmatrix}$$ ![figure](../assets/336fad898e34b05c.svg)

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

**`power`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

The power.

Default:
2.0

Suggested values:
0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0

## Result

If the parameters are valid, the operator
`PowScalarElementMatrixMod` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Possible Successors

`GetFullMatrix`,
`GetValueMatrix`

## Alternatives

`PowScalarElementMatrix`,
`PowElementMatrix`,
`PowElementMatrixMod`

## See also

`SqrtMatrix`,
`SqrtMatrixMod`

## Module

Foundation
