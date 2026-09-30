# max_matrix (Operator)

## Name

`max_matrix` — Returns the elementwise maximum of a matrix.

## Signature

`def max_matrix(matrix_id: HHandle, max_type: str) -> HHandle`

## Description

The operator `max_matrix` returns the maximum values of the
elements of the `Matrix` defined by the matrix handle
*`matrix_id`*. A new matrix `MatrixMax` is generated
with the result and the matrix handle *`matrix_max_id`* of this
matrix is returned. Access to the elements of the matrix is
possible e.g., with the operator [`get_full_matrix`](get_full_matrix.md).

The type of maximum determination of the matrix can be selected via
the parameter *`max_type`*:

- ***"columns"*:** —

  The maximum is returned for
  each column of the `Matrix` separately. The resulting
  matrix `MatrixMax` has one row and the identical number of
  columns as the input matrix.

  *Example:*

  *`max_type`* = *"columns"*
  $$\mathbf{Matrix} = \\[ \\begin{bmatrix} 8.0 & 4.0 & -3.0 \\ -6.0 & 2.0 & 7.0 \\end{bmatrix} \\]$$ ![figure](../assets/91bfcace47a57121.svg)
  $$\\rightarrow \\mathrm{MatrixMax} = \\left[ 8.0 \\ 4.0 \\ 7.0 \\right]$$ ![figure](../assets/01433f92e77a618a.svg)
- ***"rows"*:** —

  The maximum is returned for
  each row of the `Matrix` separately. The resulting matrix
  `MatrixMax` has the identical number of rows as the input
  matrix and one column.

  *Example:*

  *`max_type`* = *"rows"*
  $$\mathbf{Matrix} = \\[ \\begin{bmatrix} 8.0 & 4.0 & -3.0 \\ -6.0 & 2.0 & 7.0 \\end{bmatrix} \\]$$ ![figure](../assets/91bfcace47a57121.svg)
  $$\rightarrow \text{MatrixMax} = \left[\begin{array}{c} 8.0 \\ 7.0 \end{array}\right]$$ ![figure](../assets/fb94ea0a0ad2e71e.svg)
- ***"full"*:** —

  The maximum is returned using
  all elements of the `Matrix`. The resulting matrix
  `MatrixMax` has one row and one column.

  *Example:*

  *`max_type`* = *"full"*
  $$\mathbf{Matrix} = \\[ \\begin{bmatrix} 8.0 & 4.0 & -3.0 \\ -6.0 & 2.0 & 7.0 \\end{bmatrix} \\]$$ ![figure](../assets/91bfcace47a57121.svg)
  $$\rightarrow \mathrm{MatrixMax} = [8.0]$$ ![figure](../assets/473f967ce43eba4a.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrix_id`** (input_control)  matrix `→` HHandle

Matrix handle of the input matrix.

**`max_type`** (input_control)  string `→` str

Type of maximum determination.

Default:
"columns"

List of values:
"columns", "full", "rows"

**`matrix_max_id`** (output_control)  matrix `→` HHandle

Matrix handle with the maximum values of the input
matrix.

## Result

If the parameters are valid, the operator `max_matrix` returns
the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_matrix`

## Possible Successors

`get_full_matrix`,
`get_value_matrix`

## See also

`min_matrix`

## Module

Foundation
