# serialize_deformable_model (Operator)

## Name

`serialize_deformable_model` — Serialize a deformable model.

## Signature

`serialize_deformable_model( : : ModelID : SerializedItemHandle)`

## Description

`serialize_deformable_model` serializes the data of a deformable
model (see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the
basic principle of serialization). The same data that is written
in a file by [`write_deformable_model`](write_deformable_model.md) is converted to a serialized
item. The deformable model is defined by the handle
*`ModelID`*. The serialized deformable model is returned by the
handle *`SerializedItemHandle`* and can be deserialized
by [`deserialize_deformable_model`](deserialize_deformable_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ModelID`** (input_control)  deformable_model `→`  (handle)

Handle of a model to be saved.

**`SerializedItemHandle`** (output_control)  serialized_item `→`  (handle)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_deformable_model` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`create_planar_uncalib_deformable_model`,
`create_planar_calib_deformable_model`,
`create_local_deformable_model`

## Possible Successors

`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_deformable_model`

## Module

Matching
