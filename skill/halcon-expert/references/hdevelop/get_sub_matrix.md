# get_sub_matrix (Operator)

## Name

`get_sub_matrix` — Get a sub-matrix of a matrix.

## Signature

`get_sub_matrix( : : MatrixID, Row, Column, RowsSub, ColumnsSub : MatrixSubID)`

## Description

The operator `get_sub_matrix` generates a new matrix
`MatrixSub` and copies to this matrix a part of the input
`Matrix` defined by the matrix handle *`MatrixID`*.
The part of the `Matrix` is determined by the upper left
corner (*`Row`*,*`Column`*) and the sub-matrix dimensions
(*`RowsSub`*, *`ColumnsSub`*). The operator returns the
matrix handle *`MatrixSubID`* of the matrix
`MatrixSub`. Access to the elements of the matrix is
possible e.g., with the operator [`get_full_matrix`](get_full_matrix.md).

*Example:*

*`Row`* = *0*,
*`Column`* = *1*,
*`RowsSub`* = *3*,
*`ColumnsSub`* = *2*
$$\text{Matrix} = \begin{bmatrix} 3.0 & 1.0 & -2.0 & 1.0 \\ -5.0 & 7.0 & 2.0 & 6.0 \\ -9.0 & -4.0 & 1.0 & -1.0 \end{bmatrix}$$ ![figure](../assets/12b26cfbba735428.svg)
$$\rightarrow \mathrm{MatrixSub} = \left[\begin{array}{rr} 1.0 & -2.0 \\ 7.0 & 2.0 \\ -4.0 & 1.0 \end{array}\right]$$ ![figure](../assets/8c0b5ead89ea75bb.svg)

## Attention

The conditions 0 $\le$ *`Row`* < size of
`Matrix` in row direction, *`Row`* + *`RowsSub`*
$\le$ size of `Matrix` in the row direction, 0
$\le$ *`Column`* < size of `Matrix` in the
column direction, and *`Column`* + *`ColumnsSub`*
$\le$ size of matrix `Matrix` in the column
direction must be satisfied.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MatrixID`** (input_control)  matrix `→`  (handle)

Matrix handle of the input matrix.

**`Row`** (input_control)  integer `→`  (integer)

Upper row position of the sub-matrix in the input
matrix.

Default:
0

Suggested values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 50, 100

Restriction:
`Row >= 0`

**`Column`** (input_control)  integer `→`  (integer)

Left column position of the sub-matrix in the input
matrix.

Default:
0

Suggested values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 50, 100

Restriction:
`Column >= 0`

**`RowsSub`** (input_control)  integer `→`  (integer)

Number of rows of the sub-matrix.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 50, 100

Restriction:
`RowsSub >= 1`

**`ColumnsSub`** (input_control)  integer `→`  (integer)

Number of columns of the sub-matrix.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 50, 100

Restriction:
`ColumnsSub >= 1`

**`MatrixSubID`** (output_control)  matrix `→`  (handle)

Matrix handle of the sub-matrix.

## Result

If the parameters are valid, the operator `get_sub_matrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_matrix`

## Possible Successors

`get_full_matrix`,
`get_value_matrix`

## See also

`set_sub_matrix`

## Module

Foundation
