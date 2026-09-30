# repeat_matrix (Operator)

## Name

`repeat_matrix` — Repeat a matrix.

## Signature

`repeat_matrix( : : MatrixID, Rows, Columns : MatrixRepeatedID)`

## Description

The operator `repeat_matrix` creates the new matrix
`MatrixRepeated` and copies all elements of the input
`Matrix` n times to this new matrix, where n =
*`Rows`* $\cdot$ *`Columns`*. The new matrix has
dimensions *`Rows`* $\times$ rows of the input
`Matrix` and *`Columns`* $\times$ columns of the
input `Matrix`. The input `Matrix` is defined by
the matrix handle *`MatrixID`*. The operator returns the
matrix handle *`MatrixRepeatedID`* of the matrix
`MatrixRepeated`. Access to the elements of the matrix
is possible e.g., with the operator [`get_full_matrix`](get_full_matrix.md).

*Example:*

*`Rows`* = *2*,
*`Columns`* = *3*
$$\mathrm{Matrix} = \left[\begin{matrix} 3.0 & -1.0 & -2.0 \\ -5.0 & 7.0 & 2.0 \end{matrix}\right]$$ ![figure](../assets/0f5a777d38b23a56.svg)
$$\text{MatrixRepeated} = \left[\begin{array}{rrrrrrrrr}3.0 & -1.0 & -2.0 & 3.0 & -1.0 & -2.0 & 3.0 & -1.0 & -2.0\\-5.0 & 7.0 & 2.0 & -5.0 & 7.0 & 2.0 & -5.0 & 7.0 & 2.0\\3.0 & -1.0 & -2.0 & 3.0 & -1.0 & -2.0 & 3.0 & -1.0 & -2.0\\-5.0 & 7.0 & 2.0 & -5.0 & 7.0 & 2.0 & -5.0 & 7.0 & 2.0\end{array}\right]$$ ![figure](../assets/e20f816cca43eb34.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MatrixID`** (input_control)  matrix `→`  (handle)

Matrix handle of the input matrix.

**`Rows`** (input_control)  integer `→`  (integer)

Number of copies of input matrix in row direction.

Default:
2

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20

Restriction:
`Rows >= 1`

**`Columns`** (input_control)  integer `→`  (integer)

Number of copies of input matrix in column
direction.

Default:
2

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20

Restriction:
`Columns >= 1`

**`MatrixRepeatedID`** (output_control)  matrix `→`  (handle)

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
