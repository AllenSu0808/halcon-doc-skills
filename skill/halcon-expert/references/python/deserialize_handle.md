# deserialize_handle (Operator)

## Name

`deserialize_handle` — Deserialize a serialized item.

## Signature

`def deserialize_handle(serialized_item: HHandle) -> HHandle`

## Description

`deserialize_handle` deserializes the content of
*`serialized_item`* and returns the deserialized item in
*`handle`*
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

**`serialized_item`** (input_control)  serialized_item `→` HHandle

Handle containing the serialized item to be deserialized.

**`handle`** (output_control)  handle `→` HHandle

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
