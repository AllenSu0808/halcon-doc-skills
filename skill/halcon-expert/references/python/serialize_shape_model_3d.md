# serialize_shape_model_3d (Operator)

## Name

`serialize_shape_model_3d` — Serialize a 3D shape model.

## Signature

`def serialize_shape_model_3d(shape_model_3did: HHandle) -> HHandle`

## Description

`serialize_shape_model_3d` serializes the data of a 3D shape model
(see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the
basic principle of serialization). The same data that is written
in a file by [`write_shape_model_3d`](write_shape_model_3d.md) is converted to a serialized
item. The 3D shape model is defined by the handle
*`shape_model_3did`*. The serialized 3D shape model is returned by the
handle *`serialized_item_handle`* and can be deserialized by
[`deserialize_shape_model_3d`](deserialize_shape_model_3d.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`shape_model_3did`** (input_control)  shape_model_3d `→` HHandle

Handle of the 3D shape model.

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_shape_model_3d` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`create_shape_model_3d`

## Possible Successors

`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_shape_model_3d`

## Module

3D Metrology
