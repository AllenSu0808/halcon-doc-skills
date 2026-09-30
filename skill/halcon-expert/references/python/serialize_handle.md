# serialize_handle (Operator)

## Name

`serialize_handle` — Serialize the content of a handle.

## Signature

`def serialize_handle(handle: HHandle) -> HHandle`

## Description

`serialize_handle` serializes the content of *`handle`* and
returns the serialized item in *`serialized_item`*
(see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization).
The serialized item can later be deserialized with
[`deserialize_handle`](deserialize_handle.md).

Note that not all handle types support serialization.
To check if a handle can be serializes, use [`tuple_is_serializable`](tuple_is_serializable.md)
or [`tuple_is_serializable_elem`](tuple_is_serializable_elem.md).
Handles that have already been cleared cannot be serialized.

Also note that the serialized item created by this operator is compatible
with the type specific deserialization operators, such as
[`deserialize_matrix`](deserialize_matrix.md) or [`deserialize_shape_model`](deserialize_shape_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`handle`** (input_control)  handle `→` HHandle

Handle that should be serialized.

**`serialized_item`** (output_control)  serialized_item `→` HHandle

Handle containing the serialized item.

## Example (HDevelop)

```
create_matrix (3, 3, 0, MatrixID)
serialize_handle (MatrixID, SerializedMatrix)
deserialize_handle (SerializedMatrix, MatrixID2)
```

## Result

If the parameters are valid, the operator `serialize_handle`
returns the value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Predecessors

`tuple_is_serializable`,
`tuple_is_serializable_elem`

## Possible Successors

`deserialize_handle`,
`fwrite_serialized_item`,
`send_serialized_item`

## Module

Foundation
