# GetDiagonalMatrix (Operator)

## Name

`GetDiagonalMatrix` — Get the diagonal elements of a matrix.

## Signature

`static void HOperatorSet.GetDiagonalMatrix(HTuple matrixID, HTuple diagonal, out HTuple vectorID)`

`HMatrix HMatrix.GetDiagonalMatrix(int diagonal)`

## Description

The operator `GetDiagonalMatrix` generates a new matrix
`Vector` and copies the diagonal elements of the
`Matrix` to this new matrix. The `Matrix` is
defined by the matrix handle *`matrixID`*. The matrix
`Vector` has one column and n rows, where n = number of
diagonal elements. The operator returns the matrix handle
*`vectorID`* of the matrix `Vector`. Access to the
elements of the matrix is possible e.g., with the operator
[`GetFullMatrix`](get_full_matrix.md).

If *`diagonal`* = 0, the output of the `Vector` is the
main diagonal of the `Matrix`.

*Example:*

*`diagonal`* = *0*
$$\mathbf{Matrix} = \begin{bmatrix} 3.0 & 1.0 & -2.0 \\ -5.0 & 7.0 & 2.0 \\ -9.0 & -4.0 & 1.0 \\\end{bmatrix}$$ ![figure](../assets/07fec0586780770d.svg)
$$\to Vector = \left[\begin{array}{c}3.0\\7.0\\1.0\end{array}\right]$$ ![figure](../assets/de2e90f15d7311a8.svg)

If *`diagonal`* is positive, the output `Vector` is the
*`diagonal`*-th super-diagonal of the `Matrix`.

*Example:*

*`diagonal`* = *2*
$$\text{Matrix} = \begin{bmatrix} 3.0 & 1.0 & -2.0 & 1.0 \\ -5.0 & 7.0 & 2.0 & 6.0 \\ -9.0 & -4.0 & 1.0 & -1.0 \end{bmatrix}$$ ![figure](../assets/12b26cfbba735428.svg)
$$\rightarrow Vector = \left[ -2.0 \\ 6.0 \right]$$ ![figure](../assets/b1f7e0482eac4e64.svg)

If *`diagonal`* is negative, the *`diagonal`*-th
sub-diagonal of the `Matrix` is copied.

*Example:*

*`diagonal`* = *-1*
$$\text{Matrix} = \begin{bmatrix} 3.0 & 1.0 & -2.0 & 1.0 \\ -5.0 & 7.0 & 2.0 & 6.0 \\ -9.0 & -4.0 & 1.0 & -1.0 \end{bmatrix}$$ ![figure](../assets/12b26cfbba735428.svg)
$$\rightarrow \quad \text{Vector} = \left[\begin{array}{r}-5.0\\-4.0\end{array}\right]$$ ![figure](../assets/cb2c5de14ff101ac.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrixID`** (input_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix.

**`diagonal`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of the desired diagonal.

Default:
0

Suggested values:
-20, -10, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 10, 20

**`vectorID`** (output_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle containing the diagonal elements.

## Result

If the parameters are valid, the operator
`GetDiagonalMatrix` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Possible Successors

`GetFullMatrix`,
`GetValueMatrix`

## See also

`SetDiagonalMatrix`

## Module

Foundation
