# ScaleMatrixMod (Operator)

## Name

`ScaleMatrixMod` — Scale a matrix.

## Signature

`static void HOperatorSet.ScaleMatrixMod(HTuple matrixID, HTuple factor)`

`void HMatrix.ScaleMatrixMod(HTuple factor)`

`void HMatrix.ScaleMatrixMod(double factor)`

## Description

The operator [`ScaleMatrix`](scale_matrix.md) scales the `Matrix` by a
constant factor. The matrix is defined by the matrix handle
*`matrixID`*. The input matrix is overwritten with the
result. Access to the elements of the matrix is possible e.g., with
the operator [`GetFullMatrix`](get_full_matrix.md). The formula for the
calculation of the result is:
$$\texttt{Matrix}_{ij}=\texttt{Factor}\cdot\texttt{Matrix}_{ij}.$$

*Example:*

*`factor`* = *1.5*
$$\text{Matrix} = \begin{bmatrix} 3.0 & 1.0 & -2.0 \\ -2.0 & 6.0 & 2.0 \\ -5.0 & -4.0 & 1.0 \end{bmatrix}$$ ![figure](../assets/f76a2100d54acda9.svg)
$$\rightarrow\; \text{Matrix} = \left[\begin{array}{ccc} 4.5 & 1.5 & -3.0 \\ -3.0 & 9.0 & 3.0 \\ -7.5 & -6.0 & 1.5 \end{array}\right]$$ ![figure](../assets/cf2a62f9c0a87b8f.svg)

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

**`factor`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Scale factor.

Default:
2.0

Suggested values:
0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0

## Result

If the parameters are valid, the operator `ScaleMatrixMod`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Possible Successors

`GetFullMatrix`,
`GetValueMatrix`

## Alternatives

`ScaleMatrix`

## See also

`MultElementMatrix`,
`MultElementMatrixMod`,
`DivElementMatrix`,
`DivElementMatrixMod`

## Module

Foundation
