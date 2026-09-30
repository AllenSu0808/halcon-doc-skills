# SerializeShapeModel (Operator)

## Name

`SerializeShapeModel` — Serialize a shape model.

## Signature

`static void HOperatorSet.SerializeShapeModel(HTuple modelID, out HTuple serializedItemHandle)`

`HSerializedItem HShapeModel.SerializeShapeModel()`

## Description

`SerializeShapeModel` serializes the data of a shape model
(see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the
basic principle of serialization). The same data that is written
in a file by [`WriteShapeModel`](write_shape_model.md) is converted to a serialized
item. The shape model is defined by the handle
*`modelID`*. The serialized shape model is returned by the
handle *`serializedItemHandle`* and can be deserialized by
[`DeserializeShapeModel`](deserialize_shape_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`modelID`** (input_control)  shape_model `→` [HShapeModel](HShapeModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeShapeModel` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`CreateGenericShapeModel`

## Possible Successors

`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeShapeModel`

## Module

Matching
