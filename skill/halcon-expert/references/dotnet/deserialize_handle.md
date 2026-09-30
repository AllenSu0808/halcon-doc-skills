# DeserializeHandle (Operator)

## Name

`DeserializeHandle` — Deserialize a serialized item.

## Signature

`static void HOperatorSet.DeserializeHandle(HTuple serializedItem, out HTuple handle)`

`void HHandle.DeserializeHandle(HSerializedItem serializedItem)`

## Description

`DeserializeHandle` deserializes the content of
*`serializedItem`* and returns the deserialized item in
*`handle`*
(see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization).

The serialized item must have been created by [`SerializeHandle`](serialize_handle.md),
or by the type specific serialization operators, such as
[`SerializeMatrix`](serialize_matrix.md) or [`SerializeShapeModel`](serialize_shape_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItem`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle containing the serialized item to be deserialized.

**`handle`** (output_control)  handle `→` [HHandle](HHandle.md), [HTuple](HTuple.md) (*IntPtr*)

Handle containing the deserialized item.

## Example (HDevelop)

```
create_matrix (3, 3, 0, MatrixID)
serialize_handle (MatrixID, SerializedMatrix)
deserialize_handle (SerializedMatrix, MatrixID2)
```

## Result

If the parameters are valid, the operator `DeserializeHandle`
returns the value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Predecessors

`SerializeHandle`,
`FreadSerializedItem`,
`ReceiveSerializedItem`

## Module

Foundation
