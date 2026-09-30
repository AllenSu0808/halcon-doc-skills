# DeserializeSurfaceModel (Operator)

## Name

`DeserializeSurfaceModel` — Deserialize a surface model.

## Signature

`static void HOperatorSet.DeserializeSurfaceModel(HTuple serializedItemHandle, out HTuple surfaceModelID)`

`void HSurfaceModel.DeserializeSurfaceModel(HSerializedItem serializedItemHandle)`

## Description

`DeserializeSurfaceModel` deserializes a surface model,
that was serialized by [`SerializeSurfaceModel`](serialize_surface_model.md) (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized surface model is
defined by the handle *`serializedItemHandle`*.
The deserialized values are stored in an automatically created
surface model with the handle *`surfaceModelID`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`surfaceModelID`** (output_control)  surface_model `→` [HSurfaceModel](HSurfaceModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the surface model.

## Result

If the parameters are valid, the operator
`DeserializeSurfaceModel` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`ReadObjectModel3d`,
`XyzToObjectModel3d`,
`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeSurfaceModel`

## Possible Successors

`FindSurfaceModel`,
`RefineSurfaceModelPose`,
`GetSurfaceModelParam`,
`ClearSurfaceModel`,
`FindSurfaceModelImage`,
`RefineSurfaceModelPoseImage`

## Alternatives

`CreateSurfaceModel`

## See also

`CreateSurfaceModel`,
`ReadSurfaceModel`,
`WriteSurfaceModel`

## Module

3D Metrology
