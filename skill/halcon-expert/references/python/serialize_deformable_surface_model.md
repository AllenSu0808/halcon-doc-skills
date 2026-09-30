# serialize_deformable_surface_model (Operator)

## Name

`serialize_deformable_surface_model` — Serialize a deformable surface_model.

## Signature

`def serialize_deformable_surface_model(deformable_surface_model: HHandle) -> HHandle`

## Description

`serialize_deformable_surface_model` serializes the data of a
deformable surface model (see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization).
The same data that is written in a file by
[`write_deformable_surface_model`](write_deformable_surface_model.md) is converted to a serialized item.
The deformable surface model is defined by the handle
*`deformable_surface_model`*.
The serialized deformable surface model is returned by the
handle *`serialized_item_handle`* and can be deserialized by
[`deserialize_deformable_surface_model`](deserialize_deformable_surface_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`deformable_surface_model`** (input_control)  deformable_surface_model `→` HHandle

Handle of the deformable surface model.

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_deformable_surface_model` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`read_deformable_surface_model`,
`create_deformable_surface_model`

## Possible Successors

`clear_deformable_surface_model`,
`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_deformable_surface_model`

## See also

`create_deformable_surface_model`,
`read_deformable_surface_model`,
`write_deformable_surface_model`,
`deserialize_deformable_surface_model`

## Module

3D Metrology
