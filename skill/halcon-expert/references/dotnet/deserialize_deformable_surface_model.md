# DeserializeDeformableSurfaceModel (Operator)

## Name

`DeserializeDeformableSurfaceModel` — Deserialize a deformable surface model.

## Signature

`static void HOperatorSet.DeserializeDeformableSurfaceModel(HTuple serializedItemHandle, out HTuple deformableSurfaceModel)`

`void HDeformableSurfaceModel.DeserializeDeformableSurfaceModel(HSerializedItem serializedItemHandle)`

## Description

`DeserializeDeformableSurfaceModel` deserializes a deformable surface model,
that was serialized by [`SerializeDeformableSurfaceModel`](serialize_deformable_surface_model.md) (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized deformable surface model is
defined by the handle *`serializedItemHandle`*.
The deserialized values are stored in an automatically created
deformable surface model with the handle *`deformableSurfaceModel`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`deformableSurfaceModel`** (output_control)  deformable_surface_model `→` [HDeformableSurfaceModel](HDeformableSurfaceModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the deformable surface model.

## Result

If the parameters are valid, the operator
`DeserializeDeformableSurfaceModel` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeDeformableSurfaceModel`

## Possible Successors

`FindDeformableSurfaceModel`,
`RefineDeformableSurfaceModel`,
`GetDeformableSurfaceModelParam`,
`ClearDeformableSurfaceModel`

## Alternatives

`CreateDeformableSurfaceModel`

## See also

`CreateDeformableSurfaceModel`,
`ReadDeformableSurfaceModel`,
`WriteDeformableSurfaceModel`,
`SerializeDeformableSurfaceModel`

## Module

3D Metrology
