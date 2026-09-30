# div_element_matrix_mod (Operator)

## Name

`div_element_matrix_mod` — Divide matrices element-by-element.

## Signature

`def div_element_matrix_mod(matrix_aid: HHandle, matrix_bid: HHandle) -> None`

## Description

The operator `div_element_matrix_mod` divides the two matrices
`MatrixA` and `MatrixB` element-by-element. The
matrices are given by the matrix handles *`matrix_aid`* and
*`matrix_bid`*. It is required that both input matrices have
identical dimensions. The input matrix `MatrixA` is
overwritten with the result. Access to the elements of the matrix
is possible e.g., with the operator [`get_full_matrix`](get_full_matrix.md). The
formula for the calculation of the result is:
$$\texttt{MatrixA}_{ij}=\texttt{MatrixA}_{ij}/\texttt{MatrixB}_{ij}.$$

*Example:*

$$MatrixA = \begin{bmatrix}4.0 & 8.0 & 0.0\\-6.0 & 7.0 & 2.0\\-9.0 & 4.0 & 1.0\end{bmatrix}\nMatrixB = \begin{bmatrix}2.0 & 8.0 & -3.0\\-4.0 & -1.0 & 4.0\\-2.0 & -4.0 & 2.0\end{bmatrix}$$ ![figure](../assets/f5c6f8a0d8e82e22.svg)
$$\rightarrow \text{ MatrixA} = \left[\begin{array}{ccc} 2.0 & 1.0 & 0.0 \\ 1.5 & -7.0 & 0.5 \\ 4.5 & -1.0 & 0.5 \end{array}\right]$$ ![figure](../assets/25febbc36978431c.svg)

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

If the parameters are valid, the operator `div_element_matrix_mod`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_matrix`

## Possible Successors

`get_full_matrix`,
`get_value_matrix`

## Alternatives

`div_element_matrix`

## See also

`mult_element_matrix`,
`mult_element_matrix_mod`,
`scale_matrix`,
`scale_matrix_mod`

## Module

Foundation
