# SerializeDeformableSurfaceModel (Operator)

## Name

`SerializeDeformableSurfaceModel` — Serialize a deformable surface_model.

## Signature

`static void HOperatorSet.SerializeDeformableSurfaceModel(HTuple deformableSurfaceModel, out HTuple serializedItemHandle)`

`HSerializedItem HDeformableSurfaceModel.SerializeDeformableSurfaceModel()`

## Description

`SerializeDeformableSurfaceModel` serializes the data of a
deformable surface model (see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization).
The same data that is written in a file by
[`WriteDeformableSurfaceModel`](write_deformable_surface_model.md) is converted to a serialized item.
The deformable surface model is defined by the handle
*`deformableSurfaceModel`*.
The serialized deformable surface model is returned by the
handle *`serializedItemHandle`* and can be deserialized by
[`DeserializeDeformableSurfaceModel`](deserialize_deformable_surface_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`deformableSurfaceModel`** (input_control)  deformable_surface_model `→` [HDeformableSurfaceModel](HDeformableSurfaceModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the deformable surface model.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeDeformableSurfaceModel` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`ReadDeformableSurfaceModel`,
`CreateDeformableSurfaceModel`

## Possible Successors

`ClearDeformableSurfaceModel`,
`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeDeformableSurfaceModel`

## See also

`CreateDeformableSurfaceModel`,
`ReadDeformableSurfaceModel`,
`WriteDeformableSurfaceModel`,
`DeserializeDeformableSurfaceModel`

## Module

3D Metrology
