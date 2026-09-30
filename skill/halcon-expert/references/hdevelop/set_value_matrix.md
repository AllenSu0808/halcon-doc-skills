# set_value_matrix (Operator)

## Name

`set_value_matrix` — Set one or more elements of a matrix.

## Signature

`set_value_matrix( : : MatrixID, Row, Column, Value : )`

## Description

The operator `set_value_matrix` *sets* the
values of the elements of the input `Matrix` at the
positions (*`Row`*,*`Column`*) to the values specified by
*`Value`*. The values can be a tuple of floating point or
integer numbers. Integer numbers are converted to floating point
numbers automatically. The number of values of *`Value`* must
match the number of elements of *`Row`* and *`Column`*. In
addition, the conditions 0 $\le$ *`Row`* < size of
`Matrix` in the row direction and
0 $\le$ *`Column`* < size of `Matrix` in the column
direction must be satisfied. The `Matrix` is defined by the
matrix handle *`MatrixID`*.

*Example:*

*`Row`* = *[0,2,1]*,
*`Column`* = *[1,0,3]*,
*`Value`* = *[1,-9,6]*
$$\mathbf{Matrix} = \begin{bmatrix} 3.0 & 0.0 & -2.0 & 1.0 \\ -5.0 & 7.0 & 2.0 & -2.0 \\ 8.0 & -4.0 & 1.0 & -1.0 \\end{bmatrix}$$ ![figure](../assets/bf941115c3d882a3.svg)
$$\rightarrow \text{ Matrix }=\begin{bmatrix} 3.0 & 1.0 & -2.0 & 1.0 \\ -5.0 & 7.0 & 2.0 & 6.0 \\ -9.0 & -4.0 & 1.0 & -1.0 \end{bmatrix}$$ ![figure](../assets/a5536ebffe60ea69.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- MatrixID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`MatrixID`** (input_control, state is modified)  matrix `→`  (handle)

Matrix handle of the input matrix.

**`Row`** (input_control)  integer(-array) `→`  (integer)

Row numbers of the matrix elements to be modified.

Default:
0

Suggested values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 50, 100

Restriction:
`Row >= 0`

**`Column`** (input_control)  integer(-array) `→`  (integer)

Column numbers of the matrix elements to be
modified.

Default:
0

Suggested values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 50, 100

Restriction:
`Column >= 0`

**`Value`** (input_control)  number(-array) `→`  (real / integer)

Values to be set in the indicated matrix elements.

Default:
0

Suggested values:
0, 1, -1

## Result

If the parameters are valid, the operator `set_value_matrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_matrix`

## Possible Successors

`clear_matrix`

## See also

`get_value_matrix`

## Module

Foundation
