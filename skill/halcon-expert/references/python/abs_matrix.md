# abs_matrix (Operator)

## Name

`abs_matrix` — Compute the absolute values of the elements of a matrix.

## Signature

`def abs_matrix(matrix_id: HHandle) -> HHandle`

## Description

The operator `abs_matrix` computes the absolute values of all
elements of the input `Matrix` given by the matrix handle
*`matrix_id`*. A new matrix `MatrixAbs` is generated
with the result. The operator returns the matrix handle
*`matrix_abs_id`* of the matrix `MatrixAbs`. Access
to the elements of the matrix is possible e.g., with the operator
[`get_full_matrix`](get_full_matrix.md). The formula for the calculation of the
result is:
$$\texttt{MatrixAbs}_{ij}=|\texttt{Matrix}_{ij}|.$$

*Example:*

$$\text{Matrix} = \begin{bmatrix}3.0 & 1.0 & -2.0\\-5.0 & 7.0 & 2.0\\-9.0 & -4.0 & 1.0\end{bmatrix} \quad\rightarrow\quad \text{MatrixAbs} = \begin{bmatrix}3.0 & 1.0 & 2.0\\5.0 & 7.0 & 2.0\\9.0 & 4.0 & 1.0\end{bmatrix}$$ ![figure](../assets/144398b506625bdd.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrix_id`** (input_control)  matrix `→` HHandle

Matrix handle of the input matrix.

**`matrix_abs_id`** (output_control)  matrix `→` HHandle

Matrix handle with the absolute values of the input
matrix.

## Result

If the parameters are valid, the operator `abs_matrix` returns
the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_matrix`

## Possible Successors

`get_full_matrix`,
`get_value_matrix`

## Alternatives

`abs_matrix_mod`

## Module

Foundation
