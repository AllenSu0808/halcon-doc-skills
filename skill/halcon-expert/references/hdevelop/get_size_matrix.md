# get_size_matrix (Operator)

## Name

`get_size_matrix` — Get the size of a matrix.

## Signature

`get_size_matrix( : : MatrixID : Rows, Columns)`

## Description

The operator `get_size_matrix` returns the number of rows
*`Rows`* and columns *`Columns`* of the input
`Matrix`. The input `Matrix` is defined by the
matrix handle *`MatrixID`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MatrixID`** (input_control)  matrix `→`  (handle)

Matrix handle of the input matrix.

**`Rows`** (output_control)  integer `→`  (integer)

Number of rows of the matrix.

**`Columns`** (output_control)  integer `→`  (integer)

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
