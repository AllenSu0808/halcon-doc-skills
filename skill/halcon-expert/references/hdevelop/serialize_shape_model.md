# serialize_shape_model (Operator)

## Name

`serialize_shape_model` — Serialize a shape model.

## Signature

`serialize_shape_model( : : ModelID : SerializedItemHandle)`

## Description

`serialize_shape_model` serializes the data of a shape model
(see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the
basic principle of serialization). The same data that is written
in a file by [`write_shape_model`](write_shape_model.md) is converted to a serialized
item. The shape model is defined by the handle
*`ModelID`*. The serialized shape model is returned by the
handle *`SerializedItemHandle`* and can be deserialized by
[`deserialize_shape_model`](deserialize_shape_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ModelID`** (input_control)  shape_model `→`  (handle)

Handle of the model.

**`SerializedItemHandle`** (output_control)  serialized_item `→`  (handle)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_shape_model` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`create_generic_shape_model`

## Possible Successors

`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_shape_model`

## Module

Matching
