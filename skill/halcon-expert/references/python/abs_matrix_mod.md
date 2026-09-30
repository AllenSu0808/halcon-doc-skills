# abs_matrix_mod (Operator)

## Name

`abs_matrix_mod` — Compute the absolute values of the elements of a matrix.

## Signature

`def abs_matrix_mod(matrix_id: HHandle) -> None`

## Description

The operator `abs_matrix_mod` computes the absolute values of
all elements of the input `Matrix` given by the matrix
handle *`matrix_id`*. The input matrix is overwritten with the
result. Access to the elements of the matrix is possible e.g., with
the operator [`get_full_matrix`](get_full_matrix.md). The formula for the
calculation of the result is:
$$\texttt{Matrix}_{ij}=|\texttt{Matrix}_{ij}|.$$

*Example:*

$$\mathrm{Matrix} = \begin{bmatrix} 3.0 & 1.0 & -2.0 \\ -5.0 & 7.0 & 2.0 \\ -9.0 & -4.0 & 1.0 \end{bmatrix} \rightarrow \mathrm{Matrix} = \begin{bmatrix} 3.0 & 1.0 & 2.0 \\ 5.0 & 7.0 & 2.0 \\ 9.0 & 4.0 & 1.0 \end{bmatrix}$$ ![figure](../assets/08fc8b699979d1cb.svg)

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

If the parameters are valid, the operator `abs_matrix_mod` returns
the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_matrix`

## Possible Successors

`get_full_matrix`,
`get_value_matrix`

## Alternatives

`abs_matrix`

## Module

Foundation
