# deserialize_deformable_model (Operator)

## Name

`deserialize_deformable_model` — Deserialize a deformable model.

## Signature

`deserialize_deformable_model( : : SerializedItemHandle : ModelID)`

## Description

`deserialize_deformable_model` deserializes a deformable model,
that was serialized by [`serialize_deformable_model`](serialize_deformable_model.md) (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized deformable model is
defined by the handle *`SerializedItemHandle`*.
The deserialized values are stored in an automatically created
deformable model with the handle *`ModelID`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SerializedItemHandle`** (input_control)  serialized_item `→`  (handle)

Handle of the serialized item.

**`ModelID`** (output_control)  deformable_model `→`  (handle)

Handle of the model.

## Result

If the parameters are valid, the operator
`deserialize_deformable_model` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_deformable_model`

## Possible Successors

`find_planar_uncalib_deformable_model`,
`find_planar_calib_deformable_model`,
`find_local_deformable_model`

## See also

`create_planar_uncalib_deformable_model`,
`create_planar_calib_deformable_model`,
`create_local_deformable_model`

## Module

Matching
