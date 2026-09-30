# serialize_surface_model (Operator)

## Name

`serialize_surface_model` — Serialize a surface_model.

## Signature

`serialize_surface_model( : : SurfaceModelID : SerializedItemHandle)`

## Description

`serialize_surface_model` serializes the data of a surface model
(see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the
basic principle of serialization). The same data that is written
in a file by [`write_surface_model`](write_surface_model.md) is converted to a serialized
item. The surface model is defined by the handle
*`SurfaceModelID`*. The serialized surface model is returned by the
handle *`SerializedItemHandle`* and can be deserialized by
[`deserialize_surface_model`](deserialize_surface_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SurfaceModelID`** (input_control)  surface_model `→`  (handle)

Handle of the surface model.

**`SerializedItemHandle`** (output_control)  serialized_item `→`  (handle)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_surface_model` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`read_surface_model`,
`create_surface_model`,
`get_surface_model_param`

## Possible Successors

`clear_surface_model`,
`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_surface_model`

## See also

`create_surface_model`,
`read_surface_model`,
`write_surface_model`

## Module

3D Metrology
