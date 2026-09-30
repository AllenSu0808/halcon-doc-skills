# pow_scalar_element_matrix (Operator)

## Name

`pow_scalar_element_matrix` — Compute the power functions of the elements of a matrix.

## Signature

`def pow_scalar_element_matrix(matrix_id: HHandle, power: Union[int, float]) -> HHandle`

## Description

The operator `pow_scalar_element_matrix` computes the power of all
elements of the input `Matrix` by a constant value. The
input `Matrix` is given by the matrix handle
*`matrix_id`*. The power value `Power` is given by the parameter
*`power`*. A new matrix `MatrixPow` is generated
with the result. The operator returns the matrix handle
*`matrix_pow_id`* of the matrix `MatrixPow`. Access
to the elements of the matrix is possible e.g., with the operator
[`get_full_matrix`](get_full_matrix.md). The formula for the calculation of the
result is:

$$MatrixPower_{ij} = MatrixPower_{ij}$$ ![figure](../assets/c80736e01789be5a.svg)

*Example:*

*`power`* = *[2.0]*
$$\mathcal{Matrix} = \begin{bmatrix} 3.0 & 1.0 & 2.0 \\ 5.0 & 7.0 & 2.0 \\ 9.0 & 4.0 & 1.0 \\end{bmatrix}$$ ![figure](../assets/85a3cf83fb20e313.svg)
$$\rightarrow\ MatrixPow = \left[\begin{array}{ccc}9.0 & 1.0 & 4.0\\ 25.0 & 49.0 & 4.0\\ 81.0 & 16.0 & 1.0\end{array}\right]$$ ![figure](../assets/c2e003b9d67653dd.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrix_id`** (input_control)  matrix `→` HHandle

Matrix handle of the input matrix.

**`power`** (input_control)  number `→` Union[int, float]

The power.

Default:
2.0

Suggested values:
0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0

**`matrix_pow_id`** (output_control)  matrix `→` HHandle

Matrix handle with the raised power of the input
matrix.

## Result

If the parameters are valid, the operator
`pow_scalar_element_matrix` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`create_matrix`

## Possible Successors

`get_full_matrix`,
`get_value_matrix`

## Alternatives

`pow_scalar_element_matrix_mod`,
`pow_element_matrix`,
`pow_element_matrix_mod`

## See also

`sqrt_matrix`,
`sqrt_matrix_mod`

## Module

Foundation
