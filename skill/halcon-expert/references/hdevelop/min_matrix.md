# min_matrix (Operator)

## Name

`min_matrix` — Returns the elementwise minimum of a matrix.

## Signature

`min_matrix( : : MatrixID, MinType : MatrixMinID)`

## Description

The operator `min_matrix` returns the minimum values of the
elements of the `Matrix` defined by the matrix handle
*`MatrixID`*. A new matrix `MatrixMin` is generated
with the result and the matrix handle *`MatrixMinID`* of this
matrix is returned. Access to the elements of the matrix is
possible e.g., with the operator [`get_full_matrix`](get_full_matrix.md).

The type of minimum determination of the matrix can be selected via
the parameter *`MinType`*:

- ***'columns'*:** —

  The minimum is returned for
  each column of the `Matrix` separately. The resulting
  matrix `MatrixMin` has one row and the identical number of
  columns as the input matrix.

  *Example:*

  *`MinType`* = *'columns'*
  $$\mathbf{Matrix} = \\[ \\begin{bmatrix} 8.0 & 4.0 & -3.0 \\ -6.0 & 2.0 & 7.0 \\end{bmatrix} \\]$$ ![figure](../assets/91bfcace47a57121.svg)
  $$\rightarrow\ MatrixMin = [ -6.0 \ 2.0 \ -3.0 ]$$ ![figure](../assets/ed0d82333428962d.svg)
- ***'rows'*:** —

  The minimum is returned for
  each row of the `Matrix` separately. The resulting matrix
  `MatrixMin` has the identical number of rows as the input
  matrix and one column.

  *Example:*

  *`MinType`* = *'rows'*
  $$\mathbf{Matrix} = \\[ \\begin{bmatrix} 8.0 & 4.0 & -3.0 \\ -6.0 & 2.0 & 7.0 \\end{bmatrix} \\]$$ ![figure](../assets/91bfcace47a57121.svg)
  / -3.0 \
  -> MatrixMin = \ -6.0 /
  \[
  \to \qquad \texttt{MatrixMin} =
  \left[ \begin{array}{r}
  -3.0   
  -6.0
  \end{array} \right]
  \]
- ***'full'*:** —

  The minimum is returned using
  all elements of the `Matrix`. The resulting matrix
  `MatrixMin` has one row and one column.

  *Example:*

  *`MinType`* = *'full'*
  $$MatrixA = \begin{bmatrix}8.0 & 4.0 & -3.0\\ -6.0 & 2.0 & 7.0\end{bmatrix}$$ ![figure](../assets/c06416208bc42e7a.svg)
  $$\rightarrow \mathrm{MatrixMin}=\left[-6.0\right]$$ ![figure](../assets/1392faab642e4202.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MatrixID`** (input_control)  matrix `→`  (handle)

Matrix handle of the input matrix.

**`MinType`** (input_control)  string `→`  (string)

Type of minimum determination.

Default:
'columns'

List of values:
'columns', 'full', 'rows'

**`MatrixMinID`** (output_control)  matrix `→`  (handle)

Matrix handle with the minimum values of the input
matrix.

## Result

If the parameters are valid, the operator `min_matrix` returns
the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_matrix`

## Possible Successors

`get_full_matrix`,
`get_value_matrix`

## See also

`max_matrix`

## Module

Foundation
