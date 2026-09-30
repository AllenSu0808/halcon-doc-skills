# serialize_variation_model (Operator)

## Name

`serialize_variation_model` — Serialize a variation model.

## Signature

`def serialize_variation_model(model_id: HHandle) -> HHandle`

## Description

`serialize_variation_model` serializes the data of a variation model
(see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the
basic principle of serialization). The same data that is written
in a file by [`write_variation_model`](write_variation_model.md) is converted to a serialized
item. The variation model is defined by the handle
*`model_id`*. The serialized variation model is returned by the
handle *`serialized_item_handle`* and can be deserialized by
[`deserialize_variation_model`](deserialize_variation_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`model_id`** (input_control)  variation_model `→` HHandle

ID of the variation model.

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_variation_model` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`train_variation_model`

## Possible Successors

`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_variation_model`

## See also

`read_variation_model`,
`write_variation_model`

## Module

Matching
