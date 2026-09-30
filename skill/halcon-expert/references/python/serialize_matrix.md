# serialize_matrix (Operator)

## Name

`serialize_matrix` — Serialize a matrix.

## Signature

`def serialize_matrix(matrix_id: HHandle) -> HHandle`

## Description

`serialize_matrix` serializes the data of a matrix (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The same data that is written in a
file by [`write_matrix`](write_matrix.md) is converted to a serialized item.
The matrix is defined by the handle *`matrix_id`*. The
serialized matrix is returned by the handle
*`serialized_item_handle`* and can be deserialized by
[`deserialize_matrix`](deserialize_matrix.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrix_id`** (input_control)  matrix `→` HHandle

Matrix handle.

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_matrix` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`create_matrix`

## Possible Successors

`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_matrix`

## Module

Foundation
