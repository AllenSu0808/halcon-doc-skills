# sub_matrix_mod (Operator)

## Name

`sub_matrix_mod` — Subtract two matrices.

## Signature

`def sub_matrix_mod(matrix_aid: HHandle, matrix_bid: HHandle) -> None`

## Description

The operator `sub_matrix_mod` computes the difference of the input
matrices `MatrixA` and `MatrixB` given by the matrix
handles *`matrix_aid`* and *`matrix_bid`*. Both matrices
must have identical dimensions. The input matrix `MatrixA` is
overwritten with the result. Access to the elements of the matrix
is possible e.g., with the operator [`get_full_matrix`](get_full_matrix.md). The
formula for the calculation of the result is:
$$\texttt{MatrixA}=\texttt{MatrixA}-\texttt{MatrixB}.$$

*Example:*

$$MatrixA = \begin{bmatrix}3.0 & 1.0 & -2.0\\-5.0 & 7.0 & 2.0\\-9.0 & -4.0 & 1.0\end{bmatrix} \\ MatrixB = \begin{bmatrix}2.0 & 8.0 & -3.0\\-4.0 & -1.0 & 5.0\\2.0 & -4.0 & 7.0\end{bmatrix}$$ ![figure](../assets/fcc47e502c3725e8.svg)
$$\rightarrow MatrixA = \left[\begin{array}{ccc}1.0 & -7.0 & 1.0\\ -1.0 & 8.0 & -3.0\\ -11.0 & 0.0 & -6.0\end{array}\right]$$ ![figure](../assets/964f445e117ea175.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- matrix_aid

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`matrix_aid`** (input_control, state is modified)  matrix `→` HHandle

Matrix handle of the input matrix A.

**`matrix_bid`** (input_control)  matrix `→` HHandle

Matrix handle of the input matrix B.

## Result

If the parameters are valid, the operator `sub_matrix_mod` returns
the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_matrix`

## Possible Successors

`get_full_matrix`,
`get_value_matrix`

## Alternatives

`sub_matrix`

## See also

`add_matrix`,
`add_matrix_mod`

## Module

Foundation
