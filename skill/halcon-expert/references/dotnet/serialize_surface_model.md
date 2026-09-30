# SerializeSurfaceModel (Operator)

## Name

`SerializeSurfaceModel` — Serialize a surface_model.

## Signature

`static void HOperatorSet.SerializeSurfaceModel(HTuple surfaceModelID, out HTuple serializedItemHandle)`

`HSerializedItem HSurfaceModel.SerializeSurfaceModel()`

## Description

`SerializeSurfaceModel` serializes the data of a surface model
(see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the
basic principle of serialization). The same data that is written
in a file by [`WriteSurfaceModel`](write_surface_model.md) is converted to a serialized
item. The surface model is defined by the handle
*`surfaceModelID`*. The serialized surface model is returned by the
handle *`serializedItemHandle`* and can be deserialized by
[`DeserializeSurfaceModel`](deserialize_surface_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`surfaceModelID`** (input_control)  surface_model `→` [HSurfaceModel](HSurfaceModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the surface model.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeSurfaceModel` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`ReadSurfaceModel`,
`CreateSurfaceModel`,
`GetSurfaceModelParam`

## Possible Successors

`ClearSurfaceModel`,
`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeSurfaceModel`

## See also

`CreateSurfaceModel`,
`ReadSurfaceModel`,
`WriteSurfaceModel`

## Module

3D Metrology
