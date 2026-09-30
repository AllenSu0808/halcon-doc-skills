# get_size_matrix (Operator)

## Name

`get_size_matrix` — Get the size of a matrix.

## Signature

`def get_size_matrix(matrix_id: HHandle) -> Tuple[int, int]`

## Description

The operator `get_size_matrix` returns the number of rows
*`rows`* and columns *`columns`* of the input
`Matrix`. The input `Matrix` is defined by the
matrix handle *`matrix_id`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrix_id`** (input_control)  matrix `→` HHandle

Matrix handle of the input matrix.

**`rows`** (output_control)  integer `→` int

Number of rows of the matrix.

**`columns`** (output_control)  integer `→` int

Number of columns of the matrix.

## Result

If the parameters are valid, the operator `get_size_matrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_matrix`

## Possible Successors

`clear_matrix`

## Module

Foundation
