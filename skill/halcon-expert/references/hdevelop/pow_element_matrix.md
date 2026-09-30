# pow_element_matrix (Operator)

## Name

`pow_element_matrix` — Compute the power functions of the elements of a matrix.

## Signature

`pow_element_matrix( : : MatrixID, MatrixExpID : MatrixPowID)`

## Description

The operator `pow_element_matrix` computes the power
of all elements of the input `Matrix` with the elements of
the input matrix `MatrixExp`. The input matrices
`Matrix` and `MatrixExp` are defined by the matrix
handles *`MatrixID`* and *`MatrixExpID`*. Both matrices
must have identical dimensions. A new matrix
`MatrixPow` is generated with the result. The operator
returns the matrix handle *`MatrixPowID`* of the matrix
`MatrixPow`. Access to the elements of the matrix is
possible e.g., with the operator [`get_full_matrix`](get_full_matrix.md). The
formula for the calculation of the result is:

$$MatrixPow_{ij} = MatrixExp_{ij}.$$ ![figure](../assets/0e0d9fb0fd557218.svg)

*Example:*

$$\text{Matrix} = \begin{bmatrix}3.0 & 1.0 & 2.0\\ 5.0 & 7.0 & 2.0\\ 9.0 & 4.0 & 1.0\end{bmatrix} \\\n\text{MatrixExp} = \begin{bmatrix}1.0 & 2.0 & 2.0\\ 2.0 & 0.0 & 3.0\\ 0.5 & 3.0 & 1.0\end{bmatrix}$$ ![figure](../assets/76c8f3ab42968aa2.svg)
$$\rightarrow\quad \mathrm{MatrixPow} = \left[\begin{array}{ccc}3.0 & 1.0 & 4.0\\ 25.0 & 1.0 & 8.0\\ 3.0 & 64.0 & 1.0\end{array}\right]$$ ![figure](../assets/49ef5354f5e502a5.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MatrixID`** (input_control)  matrix `→`  (handle)

Matrix handle of the input matrix of the base.

**`MatrixExpID`** (input_control)  matrix `→`  (handle)

Matrix handle of the input matrix with exponents.

**`MatrixPowID`** (output_control)  matrix `→`  (handle)

Matrix handle with the raised power of the input
matrix.

## Result

If the parameters are valid, the operator `pow_element_matrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_matrix`

## Possible Successors

`get_full_matrix`,
`get_value_matrix`

## Alternatives

`pow_element_matrix_mod`,
`pow_scalar_element_matrix`,
`pow_scalar_element_matrix_mod`

## See also

`sqrt_matrix`,
`sqrt_matrix_mod`

## Module

Foundation
