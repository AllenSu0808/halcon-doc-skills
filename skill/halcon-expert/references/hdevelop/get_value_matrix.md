# get_value_matrix (Operator)

## Name

`get_value_matrix` — Return one ore more elements of a matrix.

## Signature

`get_value_matrix( : : MatrixID, Row, Column : Value)`

## Description

The operator `get_value_matrix` returns the values of one ore
more elements of the `Matrix` as a tuple of floating point
numbers. The `Matrix` is given by the matrix handle
*`MatrixID`*. The row coordinates of the elements of the
`Matrix` are determined by the tuple *`Row`*, the
column coordinates by the tuple *`Column`*.

*Example:*

*`Row`* = *[0,2,1]*,
*`Column`* = *[1,0,3]*
$$\text{Matrix} = \begin{bmatrix} 3.0 & 1.0 & -2.0 & 1.0 \\ -5.0 & 7.0 & 2.0 & 6.0 \\ -9.0 & -4.0 & 1.0 & -1.0 \end{bmatrix}$$ ![figure](../assets/12b26cfbba735428.svg)
$$\rightarrow\texttt{Value}=[1.0,-9.0,6.0]$$

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MatrixID`** (input_control)  matrix `→`  (handle)

Matrix handle of the input matrix.

**`Row`** (input_control)  integer(-array) `→`  (integer)

Row numbers of matrix elements to be returned.

Default:
0

Suggested values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 50, 100

Restriction:
`Row >= 0`

**`Column`** (input_control)  integer(-array) `→`  (integer)

Column numbers of matrix elements to be returned.

Default:
0

Suggested values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 50, 100

Restriction:
`Column >= 0`

**`Value`** (output_control)  real(-array) `→`  (real)

Values of indicated matrix elements.

## Result

If the parameters are valid, the operator `get_value_matrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_matrix`

## Possible Successors

`clear_matrix`

## See also

`set_value_matrix`

## Module

Foundation
