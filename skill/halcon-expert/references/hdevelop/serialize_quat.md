# serialize_quat (Operator)

## Name

`serialize_quat` — Serialize a quaternion.

## Signature

`serialize_quat( : : Quaternion : SerializedItemHandle)`

## Description

`serialize_quat` serializes the data of the *`Quaternion`*
(see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized quaternion is returned by
the handle *`SerializedItemHandle`* and can be deserialized by
[`deserialize_quat`](deserialize_quat.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Quaternion`** (input_control)  quaternion `→`  (real / integer)

Quaternion.

**`SerializedItemHandle`** (output_control)  serialized_item `→`  (handle)

Handle of the serialized item.

## Result

If the parameters are valid, the operator `serialize_quat`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`axis_angle_to_quat`

## Possible Successors

`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_quat`

## Module

Foundation
