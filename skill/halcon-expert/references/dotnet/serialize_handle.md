# SerializeHandle (Operator)

## Name

`SerializeHandle` — Serialize the content of a handle.

## Signature

`static void HOperatorSet.SerializeHandle(HTuple handle, out HTuple serializedItem)`

`HSerializedItem HHandle.SerializeHandle()`

## Description

`SerializeHandle` serializes the content of *`handle`* and
returns the serialized item in *`serializedItem`*
(see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization).
The serialized item can later be deserialized with
[`DeserializeHandle`](deserialize_handle.md).

Note that not all handle types support serialization.
To check if a handle can be serializes, use [`TupleIsSerializable`](tuple_is_serializable.md)
or [`TupleIsSerializableElem`](tuple_is_serializable_elem.md).
Handles that have already been cleared cannot be serialized.

Also note that the serialized item created by this operator is compatible
with the type specific deserialization operators, such as
[`DeserializeMatrix`](deserialize_matrix.md) or [`DeserializeShapeModel`](deserialize_shape_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`handle`** (input_control)  handle `→` [HHandle](HHandle.md), [HTuple](HTuple.md) (*IntPtr*)

Handle that should be serialized.

**`serializedItem`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle containing the serialized item.

## Example (HDevelop)

```
create_matrix (3, 3, 0, MatrixID)
serialize_handle (MatrixID, SerializedMatrix)
deserialize_handle (SerializedMatrix, MatrixID2)
```

## Result

If the parameters are valid, the operator `SerializeHandle`
returns the value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Predecessors

`TupleIsSerializable`,
`TupleIsSerializableElem`

## Possible Successors

`DeserializeHandle`,
`FwriteSerializedItem`,
`SendSerializedItem`

## Module

Foundation
