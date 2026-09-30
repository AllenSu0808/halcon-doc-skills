# get_diagonal_matrix (Operator)

## Name

`get_diagonal_matrix` — Get the diagonal elements of a matrix.

## Signature

`get_diagonal_matrix( : : MatrixID, Diagonal : VectorID)`

## Description

The operator `get_diagonal_matrix` generates a new matrix
`Vector` and copies the diagonal elements of the
`Matrix` to this new matrix. The `Matrix` is
defined by the matrix handle *`MatrixID`*. The matrix
`Vector` has one column and n rows, where n = number of
diagonal elements. The operator returns the matrix handle
*`VectorID`* of the matrix `Vector`. Access to the
elements of the matrix is possible e.g., with the operator
[`get_full_matrix`](get_full_matrix.md).

If *`Diagonal`* = 0, the output of the `Vector` is the
main diagonal of the `Matrix`.

*Example:*

*`Diagonal`* = *0*
$$\mathbf{Matrix} = \begin{bmatrix} 3.0 & 1.0 & -2.0 \\ -5.0 & 7.0 & 2.0 \\ -9.0 & -4.0 & 1.0 \\\end{bmatrix}$$ ![figure](../assets/07fec0586780770d.svg)
$$\to Vector = \left[\begin{array}{c}3.0\\7.0\\1.0\end{array}\right]$$ ![figure](../assets/de2e90f15d7311a8.svg)

If *`Diagonal`* is positive, the output `Vector` is the
*`Diagonal`*-th super-diagonal of the `Matrix`.

*Example:*

*`Diagonal`* = *2*
$$\text{Matrix} = \begin{bmatrix} 3.0 & 1.0 & -2.0 & 1.0 \\ -5.0 & 7.0 & 2.0 & 6.0 \\ -9.0 & -4.0 & 1.0 & -1.0 \end{bmatrix}$$ ![figure](../assets/12b26cfbba735428.svg)
$$\rightarrow Vector = \left[ -2.0 \\ 6.0 \right]$$ ![figure](../assets/b1f7e0482eac4e64.svg)

If *`Diagonal`* is negative, the *`Diagonal`*-th
sub-diagonal of the `Matrix` is copied.

*Example:*

*`Diagonal`* = *-1*
$$\text{Matrix} = \begin{bmatrix} 3.0 & 1.0 & -2.0 & 1.0 \\ -5.0 & 7.0 & 2.0 & 6.0 \\ -9.0 & -4.0 & 1.0 & -1.0 \end{bmatrix}$$ ![figure](../assets/12b26cfbba735428.svg)
$$\rightarrow \quad \text{Vector} = \left[\begin{array}{r}-5.0\\-4.0\end{array}\right]$$ ![figure](../assets/cb2c5de14ff101ac.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MatrixID`** (input_control)  matrix `→`  (handle)

Matrix handle of the input matrix.

**`Diagonal`** (input_control)  integer `→`  (integer)

Number of the desired diagonal.

Default:
0

Suggested values:
-20, -10, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 10, 20

**`VectorID`** (output_control)  matrix `→`  (handle)

Matrix handle containing the diagonal elements.

## Result

If the parameters are valid, the operator
`get_diagonal_matrix` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Predecessors

`create_matrix`

## Possible Successors

`get_full_matrix`,
`get_value_matrix`

## See also

`set_diagonal_matrix`

## Module

Foundation
