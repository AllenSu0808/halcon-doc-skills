# GetSubMatrix (Operator)

## Name

`GetSubMatrix` — Get a sub-matrix of a matrix.

## Signature

`static void HOperatorSet.GetSubMatrix(HTuple matrixID, HTuple row, HTuple column, HTuple rowsSub, HTuple columnsSub, out HTuple matrixSubID)`

`HMatrix HMatrix.GetSubMatrix(int row, int column, int rowsSub, int columnsSub)`

## Description

The operator `GetSubMatrix` generates a new matrix
`MatrixSub` and copies to this matrix a part of the input
`Matrix` defined by the matrix handle *`matrixID`*.
The part of the `Matrix` is determined by the upper left
corner (*`row`*,*`column`*) and the sub-matrix dimensions
(*`rowsSub`*, *`columnsSub`*). The operator returns the
matrix handle *`matrixSubID`* of the matrix
`MatrixSub`. Access to the elements of the matrix is
possible e.g., with the operator [`GetFullMatrix`](get_full_matrix.md).

*Example:*

*`row`* = *0*,
*`column`* = *1*,
*`rowsSub`* = *3*,
*`columnsSub`* = *2*
$$\text{Matrix} = \begin{bmatrix} 3.0 & 1.0 & -2.0 & 1.0 \\ -5.0 & 7.0 & 2.0 & 6.0 \\ -9.0 & -4.0 & 1.0 & -1.0 \end{bmatrix}$$ ![figure](../assets/12b26cfbba735428.svg)
$$\rightarrow \mathrm{MatrixSub} = \left[\begin{array}{rr} 1.0 & -2.0 \\ 7.0 & 2.0 \\ -4.0 & 1.0 \end{array}\right]$$ ![figure](../assets/8c0b5ead89ea75bb.svg)

## Attention

The conditions 0 $\le$ *`row`* < size of
`Matrix` in row direction, *`row`* + *`rowsSub`*
$\le$ size of `Matrix` in the row direction, 0
$\le$ *`column`* < size of `Matrix` in the
column direction, and *`column`* + *`columnsSub`*
$\le$ size of matrix `Matrix` in the column
direction must be satisfied.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrixID`** (input_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix.

**`row`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Upper row position of the sub-matrix in the input
matrix.

Default:
0

Suggested values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 50, 100

Restriction:
`Row >= 0`

**`column`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Left column position of the sub-matrix in the input
matrix.

Default:
0

Suggested values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 50, 100

Restriction:
`Column >= 0`

**`rowsSub`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of rows of the sub-matrix.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 50, 100

Restriction:
`RowsSub >= 1`

**`columnsSub`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of columns of the sub-matrix.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 50, 100

Restriction:
`ColumnsSub >= 1`

**`matrixSubID`** (output_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the sub-matrix.

## Result

If the parameters are valid, the operator `GetSubMatrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Possible Successors

`GetFullMatrix`,
`GetValueMatrix`

## See also

`SetSubMatrix`

## Module

Foundation
