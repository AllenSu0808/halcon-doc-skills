# GetValueMatrix (Operator)

## Name

`GetValueMatrix` — Return one ore more elements of a matrix.

## Signature

`static void HOperatorSet.GetValueMatrix(HTuple matrixID, HTuple row, HTuple column, out HTuple value)`

`HTuple HMatrix.GetValueMatrix(HTuple row, HTuple column)`

`double HMatrix.GetValueMatrix(int row, int column)`

## Description

The operator `GetValueMatrix` returns the values of one ore
more elements of the `Matrix` as a tuple of floating point
numbers. The `Matrix` is given by the matrix handle
*`matrixID`*. The row coordinates of the elements of the
`Matrix` are determined by the tuple *`row`*, the
column coordinates by the tuple *`column`*.

*Example:*

*`row`* = *[0,2,1]*,
*`column`* = *[1,0,3]*
$$\text{Matrix} = \begin{bmatrix} 3.0 & 1.0 & -2.0 & 1.0 \\ -5.0 & 7.0 & 2.0 & 6.0 \\ -9.0 & -4.0 & 1.0 & -1.0 \end{bmatrix}$$ ![figure](../assets/12b26cfbba735428.svg)
$$\rightarrow\texttt{Value}=[1.0,-9.0,6.0]$$

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrixID`** (input_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix.

**`row`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Row numbers of matrix elements to be returned.

Default:
0

Suggested values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 50, 100

Restriction:
`Row >= 0`

**`column`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Column numbers of matrix elements to be returned.

Default:
0

Suggested values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 50, 100

Restriction:
`Column >= 0`

**`value`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Values of indicated matrix elements.

## Result

If the parameters are valid, the operator `GetValueMatrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Possible Successors

`ClearMatrix`

## See also

`SetValueMatrix`

## Module

Foundation
