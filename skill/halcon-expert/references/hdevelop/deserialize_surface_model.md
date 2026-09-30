# deserialize_surface_model (Operator)

## Name

`deserialize_surface_model` — Deserialize a surface model.

## Signature

`deserialize_surface_model( : : SerializedItemHandle : SurfaceModelID)`

## Description

`deserialize_surface_model` deserializes a surface model,
that was serialized by [`serialize_surface_model`](serialize_surface_model.md) (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized surface model is
defined by the handle *`SerializedItemHandle`*.
The deserialized values are stored in an automatically created
surface model with the handle *`SurfaceModelID`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SerializedItemHandle`** (input_control)  serialized_item `→`  (handle)

Handle of the serialized item.

**`SurfaceModelID`** (output_control)  surface_model `→`  (handle)

Handle of the surface model.

## Result

If the parameters are valid, the operator
`deserialize_surface_model` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`read_object_model_3d`,
`xyz_to_object_model_3d`,
`fread_serialized_item`,
`receive_serialized_item`,
`serialize_surface_model`

## Possible Successors

`find_surface_model`,
`refine_surface_model_pose`,
`get_surface_model_param`,
`clear_surface_model`,
`find_surface_model_image`,
`refine_surface_model_pose_image`

## Alternatives

`create_surface_model`

## See also

`create_surface_model`,
`read_surface_model`,
`write_surface_model`

## Module

3D Metrology
