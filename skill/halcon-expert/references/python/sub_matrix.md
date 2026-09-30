# sub_matrix (Operator)

## Name

`sub_matrix` — Subtract two matrices.

## Signature

`def sub_matrix(matrix_aid: HHandle, matrix_bid: HHandle) -> HHandle`

## Description

The operator `sub_matrix` computes the difference of the input
matrices `MatrixA` and `MatrixB` given by the matrix
handles *`matrix_aid`* and *`matrix_bid`*. Both matrices
must have identical dimensions. A new matrix `MatrixSub` is
generated with the result. The operator returns the matrix handle
*`matrix_sub_id`* of the matrix `MatrixSub`. Access
to the elements of the matrix is possible e.g., with the operator
[`get_full_matrix`](get_full_matrix.md). The formula for the calculation of the
result is:
$$\texttt{MatrixSub}=\texttt{MatrixA}-\texttt{MatrixB}.$$

*Example:*

$$MatrixA = \begin{bmatrix}3.0 & 1.0 & -2.0\\-5.0 & 7.0 & 2.0\\-9.0 & -4.0 & 1.0\end{bmatrix} \\ MatrixB = \begin{bmatrix}2.0 & 8.0 & -3.0\\-4.0 & -1.0 & 5.0\\2.0 & -4.0 & 7.0\end{bmatrix}$$ ![figure](../assets/fcc47e502c3725e8.svg)
$$\rightarrow\quad \mathrm{MatrixSub} = \left[\begin{array}{ccc} 1.0 & -7.0 & 1.0 \\ -1.0 & 8.0 & -3.0 \\ -11.0 & 0.0 & -6.0 \end{array}\right]$$ ![figure](../assets/bdb58297056593e4.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrix_aid`** (input_control)  matrix `→` HHandle

Matrix handle of the input matrix A.

**`matrix_bid`** (input_control)  matrix `→` HHandle

Matrix handle of the input matrix B.

**`matrix_sub_id`** (output_control)  matrix `→` HHandle

Matrix handle with the difference of the input
matrices.

## Result

If the parameters are valid, the operator `sub_matrix` returns
the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_matrix`

## Possible Successors

`get_full_matrix`,
`get_value_matrix`

## Alternatives

`sub_matrix_mod`

## See also

`add_matrix`,
`add_matrix_mod`

## Module

Foundation
