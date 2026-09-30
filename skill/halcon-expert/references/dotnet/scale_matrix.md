# ScaleMatrix (Operator)

## Name

`ScaleMatrix` — Scale a matrix.

## Signature

`static void HOperatorSet.ScaleMatrix(HTuple matrixID, HTuple factor, out HTuple matrixScaledID)`

`HMatrix HMatrix.ScaleMatrix(HTuple factor)`

`HMatrix HMatrix.ScaleMatrix(double factor)`

## Description

The operator `ScaleMatrix` scales the `Matrix` by a
constant factor. The matrix is defined by the matrix handle
*`matrixID`*. A new matrix `MatrixScaled` is generated
with the result. The operator returns the matrix handle
*`matrixScaledID`*. Access to the elements of the matrix is
possible e.g., with the operator [`GetFullMatrix`](get_full_matrix.md). The
formula for the calculation of the result is:
$$\texttt{MatrixScaled}_{ij}=\texttt{Factor}\cdot\texttt{Matrix}_{ij}.$$

*Example:*

*`factor`* = *1.5*
$$\text{Matrix} = \begin{bmatrix} 3.0 & 1.0 & -2.0 \\ -2.0 & 6.0 & 2.0 \\ -5.0 & -4.0 & 1.0 \end{bmatrix}$$ ![figure](../assets/f76a2100d54acda9.svg)
$$\rightarrow MatrixScaled = \begin{bmatrix} 4.5 & 1.5 & -3.0 \\ -3.0 & 9.0 & 3.0 \\ -7.5 & -6.0 & 1.5 \end{bmatrix}$$ ![figure](../assets/2d007a46d60e27b9.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrixID`** (input_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix.

**`factor`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Scale factor.

Default:
2.0

Suggested values:
0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0

**`matrixScaledID`** (output_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle with the scaled elements.

## Result

If the parameters are valid, the operator `ScaleMatrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Possible Successors

`GetFullMatrix`,
`GetValueMatrix`

## Alternatives

`ScaleMatrixMod`

## See also

`MultElementMatrix`,
`MultElementMatrixMod`,
`DivElementMatrix`,
`DivElementMatrixMod`

## Module

Foundation
