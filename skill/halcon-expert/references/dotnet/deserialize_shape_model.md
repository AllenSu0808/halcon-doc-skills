# DeserializeShapeModel (Operator)

## Name

`DeserializeShapeModel` — Deserialize a serialized shape model.

## Signature

`static void HOperatorSet.DeserializeShapeModel(HTuple serializedItemHandle, out HTuple modelID)`

`void HShapeModel.DeserializeShapeModel(HSerializedItem serializedItemHandle)`

## Description

`DeserializeShapeModel` deserializes a shape model, that was
serialized by [`SerializeShapeModel`](serialize_shape_model.md) (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized shape model is
defined by the handle *`serializedItemHandle`*.
The deserialized values are stored in an automatically created
shape model with the handle *`modelID`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`modelID`** (output_control)  shape_model `→` [HShapeModel](HShapeModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

## Result

If the parameters are valid, the operator
`DeserializeShapeModel` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeShapeModel`

## Possible Successors

`FindGenericShapeModel`

## Module

Matching
