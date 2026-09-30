# deserialize_shape_model (Operator)

## Name

`deserialize_shape_model` — Deserialize a serialized shape model.

## Signature

`def deserialize_shape_model(serialized_item_handle: HHandle) -> HHandle`

## Description

`deserialize_shape_model` deserializes a shape model, that was
serialized by [`serialize_shape_model`](serialize_shape_model.md) (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized shape model is
defined by the handle *`serialized_item_handle`*.
The deserialized values are stored in an automatically created
shape model with the handle *`model_id`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serialized_item_handle`** (input_control)  serialized_item `→` HHandle

Handle of the serialized item.

**`model_id`** (output_control)  shape_model `→` HHandle

Handle of the model.

## Result

If the parameters are valid, the operator
`deserialize_shape_model` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_shape_model`

## Possible Successors

`find_generic_shape_model`

## Module

Matching
