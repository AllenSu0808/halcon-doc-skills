# set_sub_matrix (Operator)

## Name

`set_sub_matrix` — Set a sub-matrix of a matrix.

## Signature

`set_sub_matrix( : : MatrixID, MatrixSubID, Row, Column : )`

## Description

The operator `set_sub_matrix` *overwrites* a
part of the `Matrix` with the matrix `MatrixSub`.
The input matrices are defined by the matrix handles
*`MatrixID`* and *`MatrixSubID`*. The parameters
*`Row`* and *`Column`* determine the position of the upper
left corner of the sub-matrix `MatrixSub` in
`Matrix`.

*Example:*

*`Row`* = *0*,
*`Column`* = *1*
$$\text{Matrix} = \begin{bmatrix} 3.0 & 0.0 & 9.0 & 1.0 \\ -5.0 & 3.0 & 1.0 & 6.0 \\ -9.0 & 0.0 & 1.0 & -1.0 \end{bmatrix}, \text{MatrixSub} = \begin{bmatrix} 1.0 & -2.0 \\ 7.0 & 2.0 \\ -4.0 & 1.0 \end{bmatrix}$$ ![figure](../assets/2ab01588d94b5ef8.svg)
$$\rightarrow \text{ Matrix }=\begin{bmatrix} 3.0 & 1.0 & -2.0 & 1.0 \\ -5.0 & 7.0 & 2.0 & 6.0 \\ -9.0 & -4.0 & 1.0 & -1.0 \end{bmatrix}$$ ![figure](../assets/a5536ebffe60ea69.svg)

## Attention

The conditions 0 $\le$ *`Row`* < size of matrix
`Matrix` in the row direction, *`Row`* + size of
matrix `MatrixSub` in the row direction $\le$ size
of matrix `Matrix` in the row direction, 0 $\le$
*`Column`* < size of `Matrix` in the column direction,
and *`Column`* + size of matrix `MatrixSub` in the
columns direction $\le$ size of `Matrix` in the
column direction must be satisfied.

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

**`MatrixSubID`** (input_control)  matrix `→`  (handle)

Matrix handle of the input sub-matrix.

**`Row`** (input_control)  integer `→`  (integer)

Upper row position of the sub-matrix in the
matrix.

Default:
0

Suggested values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 50, 100

Restriction:
`Row >= 0`

**`Column`** (input_control)  integer `→`  (integer)

Left column position of the sub-matrix in the
matrix.

Default:
0

Suggested values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 50, 100

Restriction:
`Column >= 0`

## Result

If the parameters are valid, the operator `set_sub_matrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_matrix`

## Possible Successors

`get_full_matrix`,
`get_value_matrix`

## See also

`get_sub_matrix`

## Module

Foundation
