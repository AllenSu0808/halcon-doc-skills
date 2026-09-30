# deserialize_shape_model_3d (Operator)

## Name

`deserialize_shape_model_3d` — Deserialize a serialized 3D shape model.

## Signature

`def deserialize_shape_model_3d(serialized_item_handle: HHandle) -> HHandle`

## Description

`deserialize_shape_model_3d` deserializes a 3D shape model, that was
serialized by [`serialize_shape_model_3d`](serialize_shape_model_3d.md) (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized 3D shape model is
defined by the handle *`serialized_item_handle`*.
The deserialized values are stored in an automatically created
3D shape model with the handle *`shape_model_3did`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serialized_item_handle`** (input_control)  serialized_item `→` HHandle

Handle of the serialized item.

**`shape_model_3did`** (output_control)  shape_model_3d `→` HHandle

Handle of the 3D shape model.

## Result

If the parameters are valid, the operator
`deserialize_shape_model_3d` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_shape_model_3d`

## Possible Successors

`find_shape_model_3d`,
`get_shape_model_3d_params`

## See also

`create_shape_model_3d`,
`clear_shape_model_3d`

## Module

3D Metrology
