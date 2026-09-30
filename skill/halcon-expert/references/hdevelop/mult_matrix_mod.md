# mult_matrix_mod (Operator)

## Name

`mult_matrix_mod` — Multiply two matrices.

## Signature

`mult_matrix_mod( : : MatrixAID, MatrixBID, MultType : )`

## Description

The operator [`mult_matrix`](mult_matrix.md) computes the product of the input
matrices `MatrixA` and `MatrixB` defined by the
matrix handles *`MatrixAID`* and *`MatrixBID`*. The
input matrix `MatrixA` is overwritten with the result.
Access to the elements of the matrix is possible e.g., with the
operator [`get_full_matrix`](get_full_matrix.md). If desired, one or both input
matrices will be transposed for the multiplication.

The type of multiplication can be selected via *`MultType`*:

- ***'AB'*:** —

  The matrices `MatrixA`
  and `MatrixB` will not be transposed. Therefore, the formula
  for the calculation of the result is:

  $$\texttt{MatrixA}=\texttt{MatrixA}\cdot\texttt{MatrixB}.$$

  The number of columns of the matrix `MatrixA` must be
  identical to the number of rows of the matrix `MatrixB`.

  *Example:*

  $$\mathrm{MatrixA} = \left[\begin{array}{rrr}-3.0 & -3.0 \\ 2.0 & -5.0 \\ -3.0 & 2.0\end{array}\right]\qquad \mathrm{MatrixB} = \left[\begin{array}{rrrr}-3.0 & -3.0 & 1.0 & 1.0 \\ 2.0 & -1.0 & -2.0 & -1.0\end{array}\right]$$ ![figure](../assets/5c6bba51a6f3a7fb.svg)
  $$\rightarrow\quad \mathrm{MatrixA} = \left[\begin{array}{rrrr} 3.0 & -6.0 & 9.0 & 6.0 \\ -4.0 & -1.0 & 12.0 & 7.0 \\ -5.0 & 7.0 & -7.0 & -5.0 \end{array}\right]$$ ![figure](../assets/14326e0fa4bdf08f.svg)
- ***'ATB'*:** —

  The matrix `MatrixA`
  will be transposed. The matrix `MatrixB` will not be
  transposed. Therefore, the formula for the calculation of the
  result is:

  $$\texttt{MatrixA}=\texttt{MatrixA}^{T}\cdot\texttt{MatrixB}.$$

  The number of rows of the matrix `MatrixA` must be
  identical to the number of rows of the matrix `MatrixB`.

  *Example:*

  $$MatrixA = \begin{bmatrix} 3.0 & 2.0 & -3.0 \\ -3.0 & -5.0 & 2.0 \end{bmatrix} MatrixB = \begin{bmatrix} 3.0 & -3.0 & 1.0 & 1.0 \\ 2.0 & -1.0 & -2.0 & -1.0 \end{bmatrix}$$ ![figure](../assets/e46eb454eda6f05f.svg)
  $$\rightarrow\quad \mathrm{MatrixA} = \left[\begin{array}{rrrr} 3.0 & -6.0 & 9.0 & 6.0 \\ -4.0 & -1.0 & 12.0 & 7.0 \\ -5.0 & 7.0 & -7.0 & -5.0 \end{array}\right]$$ ![figure](../assets/14326e0fa4bdf08f.svg)
- ***'ABT'*:** —

  The matrix `MatrixA`
  will not be transposed. The matrix `MatrixB` will be
  transposed. Therefore, the formula for the calculation of the
  result is:

  $$\texttt{MatrixA}=\texttt{MatrixA}\cdot\texttt{MatrixB}^{T}.$$

  The number of columns of the matrix `MatrixA` must be
  identical to the number of columns of the matrix
  `MatrixB`.

  *Example:*

  $$\mathrm{MatrixA} = \begin{bmatrix} 3.0 & -3.0 \\ 2.0 & -5.0 \\ -3.0 & 2.0 \end{bmatrix} \mathrm{MatrixB} = \begin{bmatrix} 3.0 & 2.0 \\ -3.0 & -1.0 \\ 1.0 & -2.0 \\ 1.0 & -1.0 \end{bmatrix}$$ ![figure](../assets/27b2d6fe9d3c60e5.svg)
  $$\rightarrow\quad \mathrm{MatrixA} = \left[\begin{array}{rrrr} 3.0 & -6.0 & 9.0 & 6.0 \\ -4.0 & -1.0 & 12.0 & 7.0 \\ -5.0 & 7.0 & -7.0 & -5.0 \end{array}\right]$$ ![figure](../assets/14326e0fa4bdf08f.svg)
- ***'ATBT'*:** —

  The matrix `MatrixA`
  and the matrix `MatrixB` will be transposed. Therefore,
  the formula for the calculation of the result is:

  $$\texttt{MatrixA}=\texttt{MatrixA}^{T}\cdot\texttt{MatrixB}^{T}.$$

  The number of rows of the matrix `MatrixA` must be
  identical to the number of columns of the matrix
  `MatrixB`.

  *Example:*

  $$MatrixA = \begin{bmatrix} 3.0 & 2.0 & -3.0 \\ -3.0 & -5.0 & 2.0 \end{bmatrix} \\ MatrixB = \begin{bmatrix} 3.0 & 2.0 \\ -3.0 & -1.0 \\ 1.0 & -2.0 \\ 1.0 & -1.0 \end{bmatrix}$$ ![figure](../assets/a5490238640bdda5.svg)
  $$\rightarrow\quad \mathrm{MatrixA} = \left[\begin{array}{rrrr} 3.0 & -6.0 & 9.0 & 6.0 \\ -4.0 & -1.0 & 12.0 & 7.0 \\ -5.0 & 7.0 & -7.0 & -5.0 \end{array}\right]$$ ![figure](../assets/14326e0fa4bdf08f.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- MatrixAID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`MatrixAID`** (input_control, state is modified)  matrix `→`  (handle)

Matrix handle of the input matrix A.

**`MatrixBID`** (input_control)  matrix `→`  (handle)

Matrix handle of the input matrix B.

**`MultType`** (input_control)  string `→`  (string)

Type of the input matrices.

Default:
'AB'

List of values:
'AB', 'ABT', 'ATB', 'ATBT'

## Result

If the parameters are valid, the operator `mult_matrix_mod`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_matrix`

## Possible Successors

`get_full_matrix`,
`get_value_matrix`

## Alternatives

`mult_matrix`

## See also

`mult_element_matrix`,
`mult_element_matrix_mod`,
`div_element_matrix`,
`div_element_matrix_mod`,
`transpose_matrix`,
`transpose_matrix_mod`

## References

David Poole: “Linear Algebra: A Modern Introduction”; Thomson;
Belmont; 2006.
  
Gene H. Golub, Charles F. van Loan: “Matrix Computations”; The
Johns Hopkins University Press; Baltimore and London; 1996.

## Module

Foundation
