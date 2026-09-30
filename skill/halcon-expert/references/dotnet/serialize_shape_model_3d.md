# SerializeShapeModel3d (Operator)

## Name

`SerializeShapeModel3d` — Serialize a 3D shape model.

## Signature

`static void HOperatorSet.SerializeShapeModel3d(HTuple shapeModel3DID, out HTuple serializedItemHandle)`

`HSerializedItem HShapeModel3D.SerializeShapeModel3d()`

## Description

`SerializeShapeModel3d` serializes the data of a 3D shape model
(see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the
basic principle of serialization). The same data that is written
in a file by [`WriteShapeModel3d`](write_shape_model_3d.md) is converted to a serialized
item. The 3D shape model is defined by the handle
*`shapeModel3DID`*. The serialized 3D shape model is returned by the
handle *`serializedItemHandle`* and can be deserialized by
[`DeserializeShapeModel3d`](deserialize_shape_model_3d.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`shapeModel3DID`** (input_control)  shape_model_3d `→` [HShapeModel3D](HShapeModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D shape model.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeShapeModel3d` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`CreateShapeModel3d`

## Possible Successors

`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeShapeModel3d`

## Module

3D Metrology
