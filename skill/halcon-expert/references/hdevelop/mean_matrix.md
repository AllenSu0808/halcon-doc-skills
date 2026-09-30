# mean_matrix (Operator)

## Name

`mean_matrix` — Returns the elementwise mean of a matrix.

## Signature

`mean_matrix( : : MatrixID, MeanType : MatrixMeanID)`

## Description

The operator `mean_matrix` returns the mean values of the
elements of the `Matrix` defined by the matrix handle
*`MatrixID`*. A new matrix `MatrixMean` is generated
with the result and the matrix handle *`MatrixMeanID`* of this
matrix is returned. Access to the elements of the matrix is
possible e.g., with the operator [`get_full_matrix`](get_full_matrix.md).

The type of mean determination of the matrix can be selected via the
parameter *`MeanType`*:

- ***'columns'*:** —

  The mean is returned for
  each column of the `Matrix` separately. The resulting
  matrix `MatrixMean` has one row and the identical number
  of columns as the input matrix.

  *Example:*

  *`MeanType`* = *'columns'*
  $$\mathbf{Matrix} = \\[ \\begin{bmatrix} 8.0 & 4.0 & -3.0 \\ -6.0 & 2.0 & 7.0 \\end{bmatrix} \\]$$ ![figure](../assets/91bfcace47a57121.svg)
  $$\rightarrow\ Mathrm{MatrixMean} = \left[ \ 1.0 \ 3.0 \ 2.0 \ ]$$ ![figure](../assets/fa522fd03f3acba3.svg)
- ***'rows'*:** —

  The mean is returned for each
  row of the `Matrix` separately. The resulting matrix
  `MatrixMean` has the identical number of rows as the input
  matrix and one column.

  *Example:*

  *`MeanType`* = *'rows'*
  $$\mathbf{Matrix} = \\[ \\begin{bmatrix} 8.0 & 4.0 & -3.0 \\ -6.0 & 2.0 & 7.0 \\end{bmatrix} \\]$$ ![figure](../assets/91bfcace47a57121.svg)
  $$\rightarrow MatrixMean = \left[\begin{array}{c}3.0\\1.0\end{array}\right]$$ ![figure](../assets/e629c8975e1bc960.svg)
- ***'full'*:** —

  The mean is returned using all
  elements of the `Matrix`. The resulting matrix
  `MatrixMean` has one row and one column.

  *Example:*

  *`MeanType`* = *'full'*
  $$\mathbf{Matrix} = \\[ \\begin{bmatrix} 8.0 & 4.0 & -3.0 \\ -6.0 & 2.0 & 7.0 \\end{bmatrix} \\]$$ ![figure](../assets/91bfcace47a57121.svg)
  $$\rightarrow\quad \mathrm{MatrixMean} = \left[ 2.0 \right]$$ ![figure](../assets/b3a4873f899f4ab2.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MatrixID`** (input_control)  matrix `→`  (handle)

Matrix handle of the input matrix.

**`MeanType`** (input_control)  string `→`  (string)

Type of mean determination.

Default:
'columns'

List of values:
'columns', 'full', 'rows'

**`MatrixMeanID`** (output_control)  matrix `→`  (handle)

Matrix handle with the mean values of the input
matrix.

## Result

If the parameters are valid, the operator `mean_matrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_matrix`

## Possible Successors

`get_full_matrix`,
`get_value_matrix`

## See also

`norm_matrix`,
`sum_matrix`

## Module

Foundation
