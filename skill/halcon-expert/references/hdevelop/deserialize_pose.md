# deserialize_pose (Operator)

## Name

`deserialize_pose` — Deserialize a serialized pose.

## Signature

`deserialize_pose( : : SerializedItemHandle : Pose)`

## Description

`deserialize_pose` deserializes a pose, that was serialized
by [`serialize_pose`](serialize_pose.md) (see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The
serialized pose is defined by the handle *`SerializedItemHandle`*.
The deserialized values are stored in an automatically created
pose with the handle *`Pose`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SerializedItemHandle`** (input_control)  serialized_item `→`  (handle)

Handle of the serialized item.

**`Pose`** (output_control)  pose `→`  (real / integer)

3D pose.

Number of elements:
7

## Result

If the parameters are valid, the operator
`deserialize_pose` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_pose`

## Module

Foundation
