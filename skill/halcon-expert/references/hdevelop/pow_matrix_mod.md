# pow_matrix_mod (Operator)

## Name

`pow_matrix_mod` — Compute the power functions of a matrix.

## Signature

`pow_matrix_mod( : : MatrixID, MatrixType, Power : )`

## Description

The operator `pow_matrix_mod` computes the power of the input
`Matrix` by a constant value. The input `Matrix`
is given by the matrix handle *`MatrixID`*. The power value
is given by the parameter *`Power`*. The input matrix is
overwritten with the result. Access to the elements of the matrix
is possible e.g., with the operator [`get_full_matrix`](get_full_matrix.md).

The type of the `Matrix` can be selected via
*`MatrixType`*. The following values are supported:
*'general'* for general, *'symmetric'* for symmetric,
*'positive_definite'* for symmetric positive definite,
*'upper_triangular'* for upper triangular,
*'permuted_upper_triangular'* for permuted upper triangular,
*'lower_triangular'* for lower triangular, and
*'permuted_lower_triangular'* for permuted lower triangular
matrices. The formula for the calculation of the
result is:

$$\mathbf{Matrix} = \mathbf{Matrix}^\mathrm{Power}.$$ ![figure](../assets/2eb1fb3f7499544b.svg)

*Example:*

*`Power`* = *[2.0]*,
*`MatrixType`* = *'general'*
$$\mathcal{Matrix} = \begin{bmatrix} 3.0 & 1.0 & 2.0 \\ 5.0 & 7.0 & 2.0 \\ 9.0 & 4.0 & 1.0 \\end{bmatrix}$$ ![figure](../assets/85a3cf83fb20e313.svg)
$$\rightarrow\ Matrix = \left[\begin{array}{ccc}32.0 & 18.0 & 10.0\\ 68.0 & 62.0 & 26.0\\ 56.0 & 41.0 & 27.0\end{array}\right]$$ ![figure](../assets/ab16a2b34653532d.svg)

## Attention

For *`MatrixType`* = *'symmetric'*,
*'positive_definite'*, or *'upper_triangular'* the
upper triangular part of the input `Matrix` must contain
the relevant information of the matrix. The strictly lower
triangular part of the matrix is not referenced. For
*`MatrixType`* = *'lower_triangular'* the lower
triangular part of the input `Matrix` must contain the
relevant information of the matrix. The strictly upper triangular
part of the matrix is not referenced. If the referenced part of
the input `Matrix` is not of the specified type, an
exception is raised.

`pow_matrix_mod` modifies the content of an already
existing matrix.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- MatrixID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`MatrixID`** (input_control, state is modified)  matrix `→`  (handle)

Matrix handle of the input matrix.

**`MatrixType`** (input_control)  string `→`  (string)

The type of the input matrix.

Default:
'general'

List of values:
'general', 'lower_triangular', 'permuted_lower_triangular', 'permuted_upper_triangular', 'positive_definite', 'symmetric', 'upper_triangular'

**`Power`** (input_control)  number `→`  (real / integer)

The power.

Default:
2.0

Suggested values:
0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0

## Result

If the parameters are valid, the operator `pow_matrix_mod`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_matrix`

## Possible Successors

`get_full_matrix`,
`get_value_matrix`

## Alternatives

`pow_matrix`,
`eigenvalues_symmetric_matrix`,
`eigenvalues_general_matrix`

## See also

`sqrt_matrix`,
`sqrt_matrix_mod`

## Module

Foundation
