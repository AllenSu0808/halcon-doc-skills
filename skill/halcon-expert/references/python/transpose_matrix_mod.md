# transpose_matrix_mod (Operator)

## Name

`transpose_matrix_mod` — Transpose a matrix.

## Signature

`def transpose_matrix_mod(matrix_id: HHandle) -> None`

## Description

The operator `transpose_matrix_mod` returns the transpose of
the input `Matrix`. The input matrix is defined by the
matrix handle *`matrix_id`*. The input matrix is overwritten
with the result. Access to the elements of the matrix is possible
e.g., with the operator [`get_full_matrix`](get_full_matrix.md).

*Example:*

$$\mathbf{Matrix}=\begin{bmatrix}3.0 & 1.0 & -2.0\\-5.0 & 7.0 & 2.0\\-9.0 & -4.0 & 1.0\end{bmatrix} \quad\rightarrow\quad \mathbf{Matrix}=\begin{bmatrix}3.0 & -5.0 & -9.0\\1.0 & 7.0 & -4.0\\-2.0 & 2.0 & 1.0\end{bmatrix}$$ ![figure](../assets/112a08e61d4347d3.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- matrix_id

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`matrix_id`** (input_control, state is modified)  matrix `→` HHandle

Matrix handle of the input matrix.

## Result

If the parameters are valid, the operator `transpose_matrix_mod`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_matrix`

## Possible Successors

`get_full_matrix`,
`get_value_matrix`

## Alternatives

`transpose_matrix`

## See also

`invert_matrix`,
`invert_matrix_mod`

## References

David Poole: “Linear Algebra: A Modern Introduction”; Thomson;
Belmont; 2006.
  
Gene H. Golub, Charles F. van Loan: “Matrix Computations”; The
Johns Hopkins University Press; Baltimore and London; 1996.

## Module

Foundation
