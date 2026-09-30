# deserialize_handle (Operator)

## Name

`deserialize_handle` — Deserialize a serialized item.

## Signature

`deserialize_handle( : : SerializedItem : Handle)`

## Description

`deserialize_handle` deserializes the content of
*`SerializedItem`* and returns the deserialized item in
*`Handle`*
(see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization).

The serialized item must have been created by [`serialize_handle`](serialize_handle.md),
or by the type specific serialization operators, such as
[`serialize_matrix`](serialize_matrix.md) or [`serialize_shape_model`](serialize_shape_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SerializedItem`** (input_control)  serialized_item `→`  (handle)

Handle containing the serialized item to be deserialized.

**`Handle`** (output_control)  handle `→`  (handle)

Handle containing the deserialized item.

## Example (HDevelop)

```
create_matrix (3, 3, 0, MatrixID)
serialize_handle (MatrixID, SerializedMatrix)
deserialize_handle (SerializedMatrix, MatrixID2)
```

## Result

If the parameters are valid, the operator `deserialize_handle`
returns the value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Predecessors

`serialize_handle`,
`fread_serialized_item`,
`receive_serialized_item`

## Module

Foundation
