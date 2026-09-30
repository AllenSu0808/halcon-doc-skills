# SetSubMatrix (Operator)

## Name

`SetSubMatrix` — Set a sub-matrix of a matrix.

## Signature

`static void HOperatorSet.SetSubMatrix(HTuple matrixID, HTuple matrixSubID, HTuple row, HTuple column)`

`void HMatrix.SetSubMatrix(HMatrix matrixSubID, int row, int column)`

## Description

The operator `SetSubMatrix` *overwrites* a
part of the `Matrix` with the matrix `MatrixSub`.
The input matrices are defined by the matrix handles
*`matrixID`* and *`matrixSubID`*. The parameters
*`row`* and *`column`* determine the position of the upper
left corner of the sub-matrix `MatrixSub` in
`Matrix`.

*Example:*

*`row`* = *0*,
*`column`* = *1*
$$\text{Matrix} = \begin{bmatrix} 3.0 & 0.0 & 9.0 & 1.0 \\ -5.0 & 3.0 & 1.0 & 6.0 \\ -9.0 & 0.0 & 1.0 & -1.0 \end{bmatrix}, \text{MatrixSub} = \begin{bmatrix} 1.0 & -2.0 \\ 7.0 & 2.0 \\ -4.0 & 1.0 \end{bmatrix}$$ ![figure](../assets/2ab01588d94b5ef8.svg)
$$\rightarrow \text{ Matrix }=\begin{bmatrix} 3.0 & 1.0 & -2.0 & 1.0 \\ -5.0 & 7.0 & 2.0 & 6.0 \\ -9.0 & -4.0 & 1.0 & -1.0 \end{bmatrix}$$ ![figure](../assets/a5536ebffe60ea69.svg)

## Attention

The conditions 0 $\le$ *`row`* < size of matrix
`Matrix` in the row direction, *`row`* + size of
matrix `MatrixSub` in the row direction $\le$ size
of matrix `Matrix` in the row direction, 0 $\le$
*`column`* < size of `Matrix` in the column direction,
and *`column`* + size of matrix `MatrixSub` in the
columns direction $\le$ size of `Matrix` in the
column direction must be satisfied.

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

**`matrixSubID`** (input_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input sub-matrix.

**`row`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Upper row position of the sub-matrix in the
matrix.

Default:
0

Suggested values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 50, 100

Restriction:
`Row >= 0`

**`column`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Left column position of the sub-matrix in the
matrix.

Default:
0

Suggested values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 50, 100

Restriction:
`Column >= 0`

## Result

If the parameters are valid, the operator `SetSubMatrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Possible Successors

`GetFullMatrix`,
`GetValueMatrix`

## See also

`GetSubMatrix`

## Module

Foundation
