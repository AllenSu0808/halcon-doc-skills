# serialize_descriptor_model (Operator)

## Name

`serialize_descriptor_model` — Serialize a descriptor model.

## Signature

`def serialize_descriptor_model(model_id: HHandle) -> HHandle`

## Description

`serialize_descriptor_model` serializes the data of a descriptor
model (see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the
basic principle of serialization). The same data that is written
in a file by [`write_descriptor_model`](write_descriptor_model.md) is converted to a serialized
item. The descriptor model is defined by the handle
*`model_id`*. The serialized descriptor model is returned by the
handle *`serialized_item_handle`* and can be deserialized by
[`deserialize_descriptor_model`](deserialize_descriptor_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`model_id`** (input_control)  descriptor_model `→` HHandle

Handle of a model to be saved.

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_descriptor_model` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`points_lepetit`,
`create_uncalib_descriptor_model`,
`create_calib_descriptor_model`

## Possible Successors

`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_descriptor_model`

## See also

`create_uncalib_descriptor_model`,
`create_calib_descriptor_model`

## Module

Matching
