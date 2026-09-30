# scale_matrix_mod (Operator)

## Name

`scale_matrix_mod` — Scale a matrix.

## Signature

`def scale_matrix_mod(matrix_id: HHandle, factor: Union[int, float]) -> None`

## Description

The operator [`scale_matrix`](scale_matrix.md) scales the `Matrix` by a
constant factor. The matrix is defined by the matrix handle
*`matrix_id`*. The input matrix is overwritten with the
result. Access to the elements of the matrix is possible e.g., with
the operator [`get_full_matrix`](get_full_matrix.md). The formula for the
calculation of the result is:
$$\texttt{Matrix}_{ij}=\texttt{Factor}\cdot\texttt{Matrix}_{ij}.$$

*Example:*

*`factor`* = *1.5*
$$\text{Matrix} = \begin{bmatrix} 3.0 & 1.0 & -2.0 \\ -2.0 & 6.0 & 2.0 \\ -5.0 & -4.0 & 1.0 \end{bmatrix}$$ ![figure](../assets/f76a2100d54acda9.svg)
$$\rightarrow\; \text{Matrix} = \left[\begin{array}{ccc} 4.5 & 1.5 & -3.0 \\ -3.0 & 9.0 & 3.0 \\ -7.5 & -6.0 & 1.5 \end{array}\right]$$ ![figure](../assets/cf2a62f9c0a87b8f.svg)

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

**`factor`** (input_control)  number `→` Union[int, float]

Scale factor.

Default:
2.0

Suggested values:
0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0

## Result

If the parameters are valid, the operator `scale_matrix_mod`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_matrix`

## Possible Successors

`get_full_matrix`,
`get_value_matrix`

## Alternatives

`scale_matrix`

## See also

`mult_element_matrix`,
`mult_element_matrix_mod`,
`div_element_matrix`,
`div_element_matrix_mod`

## Module

Foundation
