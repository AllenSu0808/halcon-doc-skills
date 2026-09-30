# serialize_ncc_model (Operator)

## Name

`serialize_ncc_model` — Serialize an NCC model.

## Signature

`def serialize_ncc_model(model_id: HHandle) -> HHandle`

## Description

`serialize_ncc_model` serializes the data of an NCC model
(see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the
basic principle of serialization). The same data that is written
in a file by [`write_ncc_model`](write_ncc_model.md) is converted to a serialized
item. The NCC model is defined by the handle
*`model_id`*. The serialized NCC model is returned
by the handle *`serialized_item_handle`* and can be
deserialized by [`deserialize_ncc_model`](deserialize_ncc_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`model_id`** (input_control)  ncc_model `→` HHandle

Handle of the model.

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_ncc_model` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`create_ncc_model`

## Possible Successors

`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_ncc_model`

## Module

Matching
