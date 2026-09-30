# sum_matrix (Operator)

## Name

`sum_matrix` — Returns the elementwise sum of a matrix.

## Signature

`sum_matrix( : : MatrixID, SumType : MatrixSumID)`

## Description

The operator `sum_matrix` returns the sum of the elements of
the `Matrix` defined by the matrix handle *`MatrixID`*.
A new matrix `MatrixSum` is generated with the result and
the matrix handle *`MatrixSumID`* of this matrix is returned.
Access to the elements of the matrix is possible e.g., with the
operator [`get_full_matrix`](get_full_matrix.md).

The type of sum determination of the matrix can be selected via the
parameter *`SumType`*:

- ***'columns'*:** —

  The sum is returned for
  each column of the `Matrix` separately. The resulting
  matrix `MatrixSum` has one row and the identical number of
  columns as the input matrix.

  *Example:*

  *`SumType`* = *'columns'*
  $$\mathbf{Matrix} = \\[ \\begin{bmatrix} 8.0 & 4.0 & -3.0 \\ -6.0 & 2.0 & 7.0 \\end{bmatrix} \\]$$ ![figure](../assets/91bfcace47a57121.svg)
  $$\rightarrow \text{ MatrixSum } = \left[ 2.0 \quad 6.0 \quad 4.0 \right]$$ ![figure](../assets/7e48e1d4e8dd3962.svg)
- ***'rows'*:** —

  The sum is returned for each
  row of the `Matrix` separately. The resulting matrix
  `MatrixSum` has the identical number of rows as the input
  matrix and one column.

  *Example:*

  *`SumType`* = *'rows'*
  $$\mathbf{Matrix} = \\[ \\begin{bmatrix} 8.0 & 4.0 & -3.0 \\ -6.0 & 2.0 & 7.0 \\end{bmatrix} \\]$$ ![figure](../assets/91bfcace47a57121.svg)
  $$\rightarrow \text{ MatrixSum} = \left[\begin{array}{r}9.0\\3.0\end{array}\right]$$ ![figure](../assets/518bcd3ee5833df6.svg)
- ***'full'*:** —

  The sum is returned using all
  elements of the `Matrix`. The resulting matrix
  `MatrixSum` has one row and one column.

  *Example:*

  *`SumType`* = *'full'*
  $$\mathbf{Matrix} = \\[ \\begin{bmatrix} 8.0 & 4.0 & -3.0 \\ -6.0 & 2.0 & 7.0 \\end{bmatrix} \\]$$ ![figure](../assets/91bfcace47a57121.svg)
  $$\rightarrow \mathrm{MatrixSum} = \left[ 12.0 \right]$$ ![figure](../assets/6a2abb32a6b75a3f.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MatrixID`** (input_control)  matrix `→`  (handle)

Matrix handle of the input matrix.

**`SumType`** (input_control)  string `→`  (string)

Type of summation.

Default:
'columns'

List of values:
'columns', 'full', 'rows'

**`MatrixSumID`** (output_control)  matrix `→`  (handle)

Matrix handle with the sum of the input matrix.

## Result

If the parameters are valid, the operator `sum_matrix` returns
the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_matrix`

## Possible Successors

`get_full_matrix`,
`get_value_matrix`

## See also

`norm_matrix`

## Module

Foundation
