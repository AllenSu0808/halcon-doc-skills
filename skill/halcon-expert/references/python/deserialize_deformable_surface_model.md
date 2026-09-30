# deserialize_deformable_surface_model (Operator)

## Name

`deserialize_deformable_surface_model` — Deserialize a deformable surface model.

## Signature

`def deserialize_deformable_surface_model(serialized_item_handle: HHandle) -> HHandle`

## Description

`deserialize_deformable_surface_model` deserializes a deformable surface model,
that was serialized by [`serialize_deformable_surface_model`](serialize_deformable_surface_model.md) (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized deformable surface model is
defined by the handle *`serialized_item_handle`*.
The deserialized values are stored in an automatically created
deformable surface model with the handle *`deformable_surface_model`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serialized_item_handle`** (input_control)  serialized_item `→` HHandle

Handle of the serialized item.

**`deformable_surface_model`** (output_control)  deformable_surface_model `→` HHandle

Handle of the deformable surface model.

## Result

If the parameters are valid, the operator
`deserialize_deformable_surface_model` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_deformable_surface_model`

## Possible Successors

`find_deformable_surface_model`,
`refine_deformable_surface_model`,
`get_deformable_surface_model_param`,
`clear_deformable_surface_model`

## Alternatives

`create_deformable_surface_model`

## See also

`create_deformable_surface_model`,
`read_deformable_surface_model`,
`write_deformable_surface_model`,
`serialize_deformable_surface_model`

## Module

3D Metrology
