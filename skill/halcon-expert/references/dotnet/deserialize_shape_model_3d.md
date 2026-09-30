# DeserializeShapeModel3d (Operator)

## Name

`DeserializeShapeModel3d` — Deserialize a serialized 3D shape model.

## Signature

`static void HOperatorSet.DeserializeShapeModel3d(HTuple serializedItemHandle, out HTuple shapeModel3DID)`

`void HShapeModel3D.DeserializeShapeModel3d(HSerializedItem serializedItemHandle)`

## Description

`DeserializeShapeModel3d` deserializes a 3D shape model, that was
serialized by [`SerializeShapeModel3d`](serialize_shape_model_3d.md) (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized 3D shape model is
defined by the handle *`serializedItemHandle`*.
The deserialized values are stored in an automatically created
3D shape model with the handle *`shapeModel3DID`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`shapeModel3DID`** (output_control)  shape_model_3d `→` [HShapeModel3D](HShapeModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D shape model.

## Result

If the parameters are valid, the operator
`DeserializeShapeModel3d` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeShapeModel3d`

## Possible Successors

`FindShapeModel3d`,
`GetShapeModel3dParams`

## See also

`CreateShapeModel3d`,
`ClearShapeModel3d`

## Module

3D Metrology
