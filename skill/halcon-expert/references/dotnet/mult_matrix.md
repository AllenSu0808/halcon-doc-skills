# MultMatrix (Operator)

## Name

`MultMatrix` — Multiply two matrices.

## Signature

`static void HOperatorSet.MultMatrix(HTuple matrixAID, HTuple matrixBID, HTuple multType, out HTuple matrixMultID)`

`HMatrix HMatrix.MultMatrix(HMatrix matrixBID, string multType)`

## Description

The operator `MultMatrix` computes the product of the input
matrices `MatrixA` and `MatrixB` defined by the
matrix handles *`matrixAID`* and *`matrixBID`*. A new
matrix `MatrixMult` is generated with the result. The
operator returns the matrix handle *`matrixMultID`* of the
matrix `MatrixMult`. Access to the elements of the matrix
is possible e.g., with the operator [`GetFullMatrix`](get_full_matrix.md). If
desired, one or both input matrices will be transposed for the
multiplication.

The type of multiplication can be selected via *`multType`*:

- ***"AB"*:** —

  The matrices `MatrixA`
  and `MatrixB` will not be transposed. Therefore, the formula
  for the calculation of the result is:

  $$\texttt{MatrixMult}=\texttt{MatrixA}\cdot\texttt{MatrixB}.$$

  The number of columns of the matrix `MatrixA` must be
  identical to the number of rows of the matrix `MatrixB`.

  *Example:*

  $$\mathrm{MatrixA} = \left[\begin{array}{rrr}-3.0 & -3.0 \\ 2.0 & -5.0 \\ -3.0 & 2.0\end{array}\right]\qquad \mathrm{MatrixB} = \left[\begin{array}{rrrr}-3.0 & -3.0 & 1.0 & 1.0 \\ 2.0 & -1.0 & -2.0 & -1.0\end{array}\right]$$ ![figure](../assets/5c6bba51a6f3a7fb.svg)
  $$\rightarrow MatrixMult = \left[\begin{array}{rrrr}3.0 & -6.0 & 9.0 & 6.0\\-4.0 & -1.0 & 12.0 & 7.0\\-5.0 & 7.0 & -7.0 & -5.0\end{array}\right]$$ ![figure](../assets/251e18344957bbbd.svg)
- ***"ATB"*:** —

  The matrix `MatrixA`
  will be transposed. The matrix `MatrixB` will not be
  transposed. Therefore, the formula for the calculation of the
  result is:

  $$\texttt{MatrixMult}=\texttt{MatrixA}^{T}\cdot\texttt{MatrixB}.$$

  The number of rows of the matrix `MatrixA` must be
  identical to the number of rows of the matrix `MatrixB`.

  *Example:*

  $$MatrixA = \begin{bmatrix} 3.0 & 2.0 & -3.0 \\ -3.0 & -5.0 & 2.0 \end{bmatrix} MatrixB = \begin{bmatrix} 3.0 & -3.0 & 1.0 & 1.0 \\ 2.0 & -1.0 & -2.0 & -1.0 \end{bmatrix}$$ ![figure](../assets/e46eb454eda6f05f.svg)
  $$\rightarrow MatrixMult = \left[\begin{array}{rrrr}3.0 & -6.0 & 9.0 & 6.0\\-4.0 & -1.0 & 12.0 & 7.0\\-5.0 & 7.0 & -7.0 & -5.0\end{array}\right]$$ ![figure](../assets/251e18344957bbbd.svg)
- ***"ABT"*:** —

  The matrix `MatrixA`
  will not be transposed. The matrix `MatrixB` will be
  transposed. Therefore, the formula for the calculation of the
  result is:

  $$\texttt{MatrixMult}=\texttt{MatrixA}\cdot\texttt{MatrixB}^{T}.$$

  The number of columns of the matrix `MatrixA` must be
  identical to the number of columns of the matrix
  `MatrixB`.

  *Example:*

  $$\mathrm{MatrixA} = \begin{bmatrix} 3.0 & -3.0 \\ 2.0 & -5.0 \\ -3.0 & 2.0 \end{bmatrix} \mathrm{MatrixB} = \begin{bmatrix} 3.0 & 2.0 \\ -3.0 & -1.0 \\ 1.0 & -2.0 \\ 1.0 & -1.0 \end{bmatrix}$$ ![figure](../assets/27b2d6fe9d3c60e5.svg)
  $$\rightarrow MatrixMult = \left[\begin{array}{rrrr}3.0 & -6.0 & 9.0 & 6.0\\-4.0 & -1.0 & 12.0 & 7.0\\-5.0 & 7.0 & -7.0 & -5.0\end{array}\right]$$ ![figure](../assets/251e18344957bbbd.svg)
- ***"ATBT"*:** —

  The matrix `MatrixA`
  and the matrix `MatrixB` will be transposed. Therefore,
  the formula for the calculation of the result is:

  $$\texttt{MatrixMult}=\texttt{MatrixA}^{T}\cdot\texttt{MatrixB}^{T}.$$

  The number of rows of the matrix `MatrixA` must be
  identical to the number of columns of the matrix
  `MatrixB`.

  *Example:*

  $$MatrixA = \begin{bmatrix} 3.0 & 2.0 & -3.0 \\ -3.0 & -5.0 & 2.0 \end{bmatrix} \\ MatrixB = \begin{bmatrix} 3.0 & 2.0 \\ -3.0 & -1.0 \\ 1.0 & -2.0 \\ 1.0 & -1.0 \end{bmatrix}$$ ![figure](../assets/a5490238640bdda5.svg)
  $$\rightarrow MatrixMult = \left[\begin{array}{rrrr}3.0 & -6.0 & 9.0 & 6.0\\-4.0 & -1.0 & 12.0 & 7.0\\-5.0 & 7.0 & -7.0 & -5.0\end{array}\right]$$ ![figure](../assets/251e18344957bbbd.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrixAID`** (input_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix A.

**`matrixBID`** (input_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix B.

**`multType`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of the input matrices.

Default:
"AB"

List of values:
"AB", "ABT", "ATB", "ATBT"

**`matrixMultID`** (output_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the multiplied matrices.

## Result

If the parameters are valid, the operator `MultMatrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Possible Successors

`GetFullMatrix`,
`GetValueMatrix`

## Alternatives

`MultMatrixMod`

## See also

`MultElementMatrix`,
`MultElementMatrixMod`,
`DivElementMatrix`,
`DivElementMatrixMod`,
`TransposeMatrix`,
`TransposeMatrixMod`

## References

David Poole: “Linear Algebra: A Modern Introduction”; Thomson;
Belmont; 2006.
  
Gene H. Golub, Charles F. van Loan: “Matrix Computations”; The
Johns Hopkins University Press; Baltimore and London; 1996.

## Module

Foundation
