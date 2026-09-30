# deserialize_ncc_model (Operator)

## Name

`deserialize_ncc_model` — Deserialize an NCC model.

## Signature

`def deserialize_ncc_model(serialized_item_handle: HHandle) -> HHandle`

## Description

`deserialize_ncc_model` deserializes an NCC model,
that was serialized by [`serialize_ncc_model`](serialize_ncc_model.md) (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized NCC model
model is defined by the handle *`serialized_item_handle`*.
The deserialized values are stored in an automatically created
NCC model with the handle *`model_id`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serialized_item_handle`** (input_control)  serialized_item `→` HHandle

Handle of the serialized item.

**`model_id`** (output_control)  ncc_model `→` HHandle

Handle of the model.

## Result

If the parameters are valid, the operator
`deserialize_ncc_model` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_ncc_model`

## Possible Successors

`find_ncc_model`

## See also

`create_ncc_model`,
`clear_ncc_model`

## Module

Matching
