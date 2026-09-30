# RepeatMatrix (Operator)

## Name

`RepeatMatrix` — Repeat a matrix.

## Signature

`static void HOperatorSet.RepeatMatrix(HTuple matrixID, HTuple rows, HTuple columns, out HTuple matrixRepeatedID)`

`HMatrix HMatrix.RepeatMatrix(int rows, int columns)`

## Description

The operator `RepeatMatrix` creates the new matrix
`MatrixRepeated` and copies all elements of the input
`Matrix` n times to this new matrix, where n =
*`rows`* $\cdot$ *`columns`*. The new matrix has
dimensions *`rows`* $\times$ rows of the input
`Matrix` and *`columns`* $\times$ columns of the
input `Matrix`. The input `Matrix` is defined by
the matrix handle *`matrixID`*. The operator returns the
matrix handle *`matrixRepeatedID`* of the matrix
`MatrixRepeated`. Access to the elements of the matrix
is possible e.g., with the operator [`GetFullMatrix`](get_full_matrix.md).

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

**`matrixID`** (input_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix.

**`rows`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of copies of input matrix in row direction.

Default:
2

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20

Restriction:
`Rows >= 1`

**`columns`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of copies of input matrix in column
direction.

Default:
2

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20

Restriction:
`Columns >= 1`

**`matrixRepeatedID`** (output_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the repeated copied matrix.

## Result

If the parameters are valid, the operator `RepeatMatrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Possible Successors

`GetFullMatrix`,
`GetValueMatrix`

## See also

`CopyMatrix`

## Module

Foundation
