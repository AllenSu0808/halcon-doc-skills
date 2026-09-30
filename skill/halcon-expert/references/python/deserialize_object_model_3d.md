# deserialize_object_model_3d (Operator)

## Name

`deserialize_object_model_3d` — Deserialize a serialized 3D object model.

## Signature

`def deserialize_object_model_3d(serialized_item_handle: HHandle) -> HHandle`

## Description

`deserialize_object_model_3d` deserializes a 3D object model
that was serialized by [`serialize_object_model_3d`](serialize_object_model_3d.md) (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized 3D object model is
defined by the handle *`serialized_item_handle`*.
The deserialized values are stored in an automatically created
3D object model with the handle *`object_model_3d`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serialized_item_handle`** (input_control)  serialized_item `→` HHandle

Handle of the serialized item.

**`object_model_3d`** (output_control)  object_model_3d `→` HHandle

Handle of the 3D object model.

## Result

If the parameters are valid, the operator
`deserialize_object_model_3d` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`write_object_model_3d`,
`fread_serialized_item`,
`receive_serialized_item`,
`serialize_object_model_3d`

## Possible Successors

`affine_trans_object_model_3d`,
`object_model_3d_to_xyz`,
`prepare_object_model_3d`

## Alternatives

`xyz_to_object_model_3d`

## See also

`write_object_model_3d`,
`clear_object_model_3d`

## Module

3D Metrology
