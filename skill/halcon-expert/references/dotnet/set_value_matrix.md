# SetValueMatrix (Operator)

## Name

`SetValueMatrix` — Set one or more elements of a matrix.

## Signature

`static void HOperatorSet.SetValueMatrix(HTuple matrixID, HTuple row, HTuple column, HTuple value)`

`void HMatrix.SetValueMatrix(HTuple row, HTuple column, HTuple value)`

`void HMatrix.SetValueMatrix(int row, int column, double value)`

## Description

The operator `SetValueMatrix` *sets* the
values of the elements of the input `Matrix` at the
positions (*`row`*,*`column`*) to the values specified by
*`value`*. The values can be a tuple of floating point or
integer numbers. Integer numbers are converted to floating point
numbers automatically. The number of values of *`value`* must
match the number of elements of *`row`* and *`column`*. In
addition, the conditions 0 $\le$ *`row`* < size of
`Matrix` in the row direction and
0 $\le$ *`column`* < size of `Matrix` in the column
direction must be satisfied. The `Matrix` is defined by the
matrix handle *`matrixID`*.

*Example:*

*`row`* = *[0,2,1]*,
*`column`* = *[1,0,3]*,
*`value`* = *[1,-9,6]*
$$\mathbf{Matrix} = \begin{bmatrix} 3.0 & 0.0 & -2.0 & 1.0 \\ -5.0 & 7.0 & 2.0 & -2.0 \\ 8.0 & -4.0 & 1.0 & -1.0 \\end{bmatrix}$$ ![figure](../assets/bf941115c3d882a3.svg)
$$\rightarrow \text{ Matrix }=\begin{bmatrix} 3.0 & 1.0 & -2.0 & 1.0 \\ -5.0 & 7.0 & 2.0 & 6.0 \\ -9.0 & -4.0 & 1.0 & -1.0 \end{bmatrix}$$ ![figure](../assets/a5536ebffe60ea69.svg)

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

**`row`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Row numbers of the matrix elements to be modified.

Default:
0

Suggested values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 50, 100

Restriction:
`Row >= 0`

**`column`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Column numbers of the matrix elements to be
modified.

Default:
0

Suggested values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 50, 100

Restriction:
`Column >= 0`

**`value`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Values to be set in the indicated matrix elements.

Default:
0

Suggested values:
0, 1, -1

## Result

If the parameters are valid, the operator `SetValueMatrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Possible Successors

`ClearMatrix`

## See also

`GetValueMatrix`

## Module

Foundation
