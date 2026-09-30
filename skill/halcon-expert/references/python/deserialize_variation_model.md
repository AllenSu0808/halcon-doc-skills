# deserialize_variation_model (Operator)

## Name

`deserialize_variation_model` — Deserialize a variation model.

## Signature

`def deserialize_variation_model(serialized_item_handle: HHandle) -> HHandle`

## Description

`deserialize_variation_model` deserializes a variation model,
that was serialized by [`serialize_variation_model`](serialize_variation_model.md) (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized variation model is
defined by the handle *`serialized_item_handle`*.
The deserialized values are stored in an automatically created
variation model with the handle *`model_id`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serialized_item_handle`** (input_control)  serialized_item `→` HHandle

Handle of the serialized item.

**`model_id`** (output_control)  variation_model `→` HHandle

ID of the variation model.

## Result

If the parameters are valid, the operator
`deserialize_variation_model` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_variation_model`

## Possible Successors

`compare_variation_model`,
`compare_ext_variation_model`

## See also

`read_variation_model`,
`write_variation_model`

## Module

Matching
