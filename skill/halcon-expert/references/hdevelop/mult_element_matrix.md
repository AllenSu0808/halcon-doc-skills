# mult_element_matrix (Operator)

## Name

`mult_element_matrix` — Multiply matrices element-by-element.

## Signature

`mult_element_matrix( : : MatrixAID, MatrixBID : MatrixMultID)`

## Description

The operator `mult_element_matrix` multiplies the two matrices
`MatrixA` and `MatrixB` element-by-element. The
matrices are defined by the matrix handles *`MatrixAID`* and
*`MatrixBID`*. It is required that both input matrices have
identical dimensions. A new matrix `MatrixMult` is
generated with the result. The operator returns the matrix handle
*`MatrixMultID`* of the matrix `MatrixMult`. Access
to the elements of the matrix is possible e.g., with the operator
[`get_full_matrix`](get_full_matrix.md). The formula for the calculation of the
result is:
$$\texttt{MatrixMult}_{ij}=\texttt{MatrixA}_{ij}\cdot\texttt{MatrixB}_{ij}.$$

*Example:*

$$MatrixA = \begin{bmatrix}4.0 & 8.0 & 0.0\\-6.0 & 7.0 & 2.0\\-9.0 & 4.0 & 1.0\end{bmatrix}\nMatrixB = \begin{bmatrix}2.0 & 8.0 & -3.0\\-4.0 & -1.0 & 4.0\\-2.0 & -4.0 & 2.0\end{bmatrix}$$ ![figure](../assets/f5c6f8a0d8e82e22.svg)
$$\rightarrow\ MatrixMulti = \begin{bmatrix}8.0 & 64.0 & 0.0\\24.0 & -7.0 & 8.0\\18.0 & -16.0 & 2.0\end{bmatrix}$$ ![figure](../assets/7d205145af4b0ef0.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MatrixAID`** (input_control)  matrix `→`  (handle)

Matrix handle of the input matrix A.

**`MatrixBID`** (input_control)  matrix `→`  (handle)

Matrix handle of the input matrix B.

**`MatrixMultID`** (output_control)  matrix `→`  (handle)

Matrix handle with the multiplied values of the
input matrices.

## Result

If the parameters are valid, the operator
`mult_element_matrix` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Predecessors

`create_matrix`

## Possible Successors

`get_full_matrix`,
`get_value_matrix`

## Alternatives

`mult_element_matrix_mod`

## See also

`div_element_matrix`,
`div_element_matrix_mod`,
`scale_matrix`,
`scale_matrix_mod`

## Module

Foundation
