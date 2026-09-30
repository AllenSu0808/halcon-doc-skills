# clear_matrix (Operator)

## Name

`clear_matrix` — Free the memory of a matrix.

## Signature

`def clear_matrix(matrix_id: MaybeSequence[HHandle]) -> None`

## Description

The operator `clear_matrix` frees the memory of the matrix
`Matrix` given by the matrix handle *`matrix_id`*.
After calling `clear_matrix`, the `Matrix` can no
longer be used. The matrix handle *`matrix_id`* becomes
invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- matrix_id

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`matrix_id`** (input_control, state is modified)  matrix(-array) `→` MaybeSequence[HHandle]

Matrix handle.

## Result

If the parameters are valid, the operator `clear_matrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_matrix`

## Module

Foundation
