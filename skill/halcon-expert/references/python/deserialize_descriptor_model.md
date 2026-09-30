# deserialize_descriptor_model (Operator)

## Name

`deserialize_descriptor_model` — Deserialize a descriptor model.

## Signature

`def deserialize_descriptor_model(serialized_item_handle: HHandle) -> HHandle`

## Description

`deserialize_descriptor_model` deserializes a descriptor
model, that was serialized by [`serialize_descriptor_model`](serialize_descriptor_model.md)
(see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized descriptor model is
defined by the handle *`serialized_item_handle`*.
The deserialized values are stored in an automatically created
descriptor model with the handle *`model_id`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serialized_item_handle`** (input_control)  serialized_item `→` HHandle

Handle of the serialized item.

**`model_id`** (output_control)  descriptor_model `→` HHandle

Handle of the model.

## Result

If the parameters are valid, the operator
`deserialize_descriptor_model` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_descriptor_model`

## Possible Successors

`find_uncalib_descriptor_model`,
`find_calib_descriptor_model`

## See also

`create_calib_descriptor_model`,
`create_uncalib_descriptor_model`

## Module

Matching
