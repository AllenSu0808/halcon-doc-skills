# add_matrix (Operator)

## Name

`add_matrix` — Add two matrices.

## Signature

`add_matrix( : : MatrixAID, MatrixBID : MatrixSumID)`

## Description

The operator `add_matrix` computes the sum of the input
matrices `MatrixA` and `MatrixB` given by the matrix
handles *`MatrixAID`* and *`MatrixBID`*. Both matrices
must have identical dimensions. A new matrix
`MatrixSum` is generated with the result. The operator
returns the matrix handle *`MatrixSumID`* of the matrix
`MatrixSum`. Access to the elements of the matrix is
possible e.g., with the operator [`get_full_matrix`](get_full_matrix.md). The
formula for the calculation of the result is:
$$\texttt{MatrixSum}=\texttt{MatrixA}+\texttt{MatrixB}.$$

*Example:*

$$MatrixA = \begin{bmatrix}3.0 & 1.0 & -2.0\\-5.0 & 7.0 & 2.0\\-9.0 & -4.0 & 1.0\end{bmatrix} \\ MatrixB = \begin{bmatrix}2.0 & 8.0 & -3.0\\-4.0 & -1.0 & 5.0\\2.0 & -4.0 & 7.0\end{bmatrix}$$ ![figure](../assets/fcc47e502c3725e8.svg)
$$\rightarrow\ Vertex\ MatrixSum = \begin{bmatrix} 5.0 & 9.0 & -5.0 \\ -9.0 & 6.0 & 7.0 \\ -7.0 & -8.0 & 8.0 \end{bmatrix}$$ ![figure](../assets/73c88f9cfe509b25.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MatrixAID`** (input_control)  matrix `→`  (handle)

Matrix handle of the input matrix A.

**`MatrixBID`** (input_control)  matrix `→`  (handle)

Matrix handle of the input matrix B.

**`MatrixSumID`** (output_control)  matrix `→`  (handle)

Matrix handle with the sum of the input matrices.

## Result

If the parameters are valid, the operator `add_matrix` returns
the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_matrix`

## Possible Successors

`get_full_matrix`,
`get_value_matrix`

## Alternatives

`add_matrix_mod`

## See also

`sub_matrix`,
`sub_matrix_mod`

## Module

Foundation
