# serialize_ncc_model (Operator)

## Name

`serialize_ncc_model` — Serialize an NCC model.

## Signature

`serialize_ncc_model( : : ModelID : SerializedItemHandle)`

## Description

`serialize_ncc_model` serializes the data of an NCC model
(see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the
basic principle of serialization). The same data that is written
in a file by [`write_ncc_model`](write_ncc_model.md) is converted to a serialized
item. The NCC model is defined by the handle
*`ModelID`*. The serialized NCC model is returned
by the handle *`SerializedItemHandle`* and can be
deserialized by [`deserialize_ncc_model`](deserialize_ncc_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ModelID`** (input_control)  ncc_model `→`  (handle)

Handle of the model.

**`SerializedItemHandle`** (output_control)  serialized_item `→`  (handle)

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
