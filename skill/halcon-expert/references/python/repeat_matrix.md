# repeat_matrix (Operator)

## Name

`repeat_matrix` — Repeat a matrix.

## Signature

`def repeat_matrix(matrix_id: HHandle, rows: int, columns: int) -> HHandle`

## Description

The operator `repeat_matrix` creates the new matrix
`MatrixRepeated` and copies all elements of the input
`Matrix` n times to this new matrix, where n =
*`rows`* $\cdot$ *`columns`*. The new matrix has
dimensions *`rows`* $\times$ rows of the input
`Matrix` and *`columns`* $\times$ columns of the
input `Matrix`. The input `Matrix` is defined by
the matrix handle *`matrix_id`*. The operator returns the
matrix handle *`matrix_repeated_id`* of the matrix
`MatrixRepeated`. Access to the elements of the matrix
is possible e.g., with the operator [`get_full_matrix`](get_full_matrix.md).

*Example:*

*`rows`* = *2*,
*`columns`* = *3*
$$\mathrm{Matrix} = \left[\begin{matrix} 3.0 & -1.0 & -2.0 \\ -5.0 & 7.0 & 2.0 \end{matrix}\right]$$ ![figure](../assets/0f5a777d38b23a56.svg)
$$\text{MatrixRepeated} = \left[\begin{array}{rrrrrrrrr}3.0 & -1.0 & -2.0 & 3.0 & -1.0 & -2.0 & 3.0 & -1.0 & -2.0\\-5.0 & 7.0 & 2.0 & -5.0 & 7.0 & 2.0 & -5.0 & 7.0 & 2.0\\3.0 & -1.0 & -2.0 & 3.0 & -1.0 & -2.0 & 3.0 & -1.0 & -2.0\\-5.0 & 7.0 & 2.0 & -5.0 & 7.0 & 2.0 & -5.0 & 7.0 & 2.0\end{array}\right]$$ ![figure](../assets/e20f816cca43eb34.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrix_id`** (input_control)  matrix `→` HHandle

Matrix handle of the input matrix.

**`rows`** (input_control)  integer `→` int

Number of copies of input matrix in row direction.

Default:
2

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20

Restriction:
`Rows >= 1`

**`columns`** (input_control)  integer `→` int

Number of copies of input matrix in column
direction.

Default:
2

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20

Restriction:
`Columns >= 1`

**`matrix_repeated_id`** (output_control)  matrix `→` HHandle

Matrix handle of the repeated copied matrix.

## Result

If the parameters are valid, the operator `repeat_matrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_matrix`

## Possible Successors

`get_full_matrix`,
`get_value_matrix`

## See also

`copy_matrix`

## Module

Foundation
