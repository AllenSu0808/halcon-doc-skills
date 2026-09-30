# serialize_quat (Operator)

## Name

`serialize_quat` — Serialize a quaternion.

## Signature

`def serialize_quat(quaternion: Sequence[Union[float, int]]) -> HHandle`

## Description

`serialize_quat` serializes the data of the *`quaternion`*
(see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized quaternion is returned by
the handle *`serialized_item_handle`* and can be deserialized by
[`deserialize_quat`](deserialize_quat.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`quaternion`** (input_control)  quaternion `→` Sequence[Union[float, int]]

Quaternion.

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

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
