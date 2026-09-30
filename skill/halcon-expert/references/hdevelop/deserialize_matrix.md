# deserialize_matrix (Operator)

## Name

`deserialize_matrix` — Deserialize a serialized matrix.

## Signature

`deserialize_matrix( : : SerializedItemHandle : MatrixID)`

## Description

`deserialize_matrix` deserializes a matrix, that was serialized
by [`serialize_matrix`](serialize_matrix.md) (see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The
serialized matrix is defined by the handle *`SerializedItemHandle`*.
The deserialized values are stored in an automatically created
matrix with the handle *`MatrixID`*. Access to the
elements of the matrix is possible e.g., with the operator
[`get_full_matrix`](get_full_matrix.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SerializedItemHandle`** (input_control)  serialized_item `→`  (handle)

Handle of the serialized item.

**`MatrixID`** (output_control)  matrix `→`  (handle)

Matrix handle.

## Result

If the parameters are valid, the operator
`deserialize_matrix` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_matrix`

## Possible Successors

`get_full_matrix`

## Module

Foundation
