# get_sub_matrix (Operator)

## Name

`get_sub_matrix` — Get a sub-matrix of a matrix.

## Signature

`def get_sub_matrix(matrix_id: HHandle, row: int, column: int, rows_sub: int, columns_sub: int) -> HHandle`

## Description

The operator `get_sub_matrix` generates a new matrix
`MatrixSub` and copies to this matrix a part of the input
`Matrix` defined by the matrix handle *`matrix_id`*.
The part of the `Matrix` is determined by the upper left
corner (*`row`*,*`column`*) and the sub-matrix dimensions
(*`rows_sub`*, *`columns_sub`*). The operator returns the
matrix handle *`matrix_sub_id`* of the matrix
`MatrixSub`. Access to the elements of the matrix is
possible e.g., with the operator [`get_full_matrix`](get_full_matrix.md).

*Example:*

*`row`* = *0*,
*`column`* = *1*,
*`rows_sub`* = *3*,
*`columns_sub`* = *2*
$$\text{Matrix} = \begin{bmatrix} 3.0 & 1.0 & -2.0 & 1.0 \\ -5.0 & 7.0 & 2.0 & 6.0 \\ -9.0 & -4.0 & 1.0 & -1.0 \end{bmatrix}$$ ![figure](../assets/12b26cfbba735428.svg)
$$\rightarrow \mathrm{MatrixSub} = \left[\begin{array}{rr} 1.0 & -2.0 \\ 7.0 & 2.0 \\ -4.0 & 1.0 \end{array}\right]$$ ![figure](../assets/8c0b5ead89ea75bb.svg)

## Attention

The conditions 0 $\le$ *`row`* < size of
`Matrix` in row direction, *`row`* + *`rows_sub`*
$\le$ size of `Matrix` in the row direction, 0
$\le$ *`column`* < size of `Matrix` in the
column direction, and *`column`* + *`columns_sub`*
$\le$ size of matrix `Matrix` in the column
direction must be satisfied.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrix_id`** (input_control)  matrix `→` HHandle

Matrix handle of the input matrix.

**`row`** (input_control)  integer `→` int

Upper row position of the sub-matrix in the input
matrix.

Default:
0

Suggested values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 50, 100

Restriction:
`Row >= 0`

**`column`** (input_control)  integer `→` int

Left column position of the sub-matrix in the input
matrix.

Default:
0

Suggested values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 50, 100

Restriction:
`Column >= 0`

**`rows_sub`** (input_control)  integer `→` int

Number of rows of the sub-matrix.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 50, 100

Restriction:
`RowsSub >= 1`

**`columns_sub`** (input_control)  integer `→` int

Number of columns of the sub-matrix.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 50, 100

Restriction:
`ColumnsSub >= 1`

**`matrix_sub_id`** (output_control)  matrix `→` HHandle

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
