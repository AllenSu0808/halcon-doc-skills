# copy_matrix (Operator)

## Name

`copy_matrix` — Copy a matrix.

## Signature

`def copy_matrix(matrix_id: HHandle) -> HHandle`

## Description

The operator `copy_matrix` creates the new matrix
`MatrixCopy` and copies all elements of the input
`Matrix` to this new matrix. The input `Matrix` is
defined by the matrix handle *`matrix_id`*. The operator
returns the matrix handle *`matrix_copy_id`* of the matrix
`MatrixCopy`. Access to the elements of the matrix is
possible e.g., with the operator [`get_full_matrix`](get_full_matrix.md).
With this operator a matrix can be saved
before the matrix is modified by the operators
[`set_value_matrix`](set_value_matrix.md), [`set_full_matrix`](set_full_matrix.md),
[`set_sub_matrix`](set_sub_matrix.md), or [`set_diagonal_matrix`](set_diagonal_matrix.md).

*Example:*

$$\text{Matrix} = \begin{bmatrix}3.0 & 1.0 & -2.0\\-5.0 & 7.0 & 2.0\\-9.0 & -4.0 & 1.0\end{bmatrix} \quad\rightarrow\quad \text{MatrixCopy} = \begin{bmatrix}3.0 & 1.0 & -2.0\\-5.0 & 7.0 & 2.0\\-9.0 & -4.0 & 1.0\end{bmatrix}$$ ![figure](../assets/22d68611fb79d8b2.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrix_id`** (input_control)  matrix `→` HHandle

Matrix handle of the input matrix.

**`matrix_copy_id`** (output_control)  matrix `→` HHandle

Matrix handle of the copied matrix.

## Result

If the parameters are valid, the operator `copy_matrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_matrix`

## Possible Successors

`get_full_matrix`,
`get_value_matrix`

## Alternatives

`repeat_matrix`

## Module

Foundation
