# serialize_pose (Operator)

## Name

`serialize_pose` — Serialize a pose.

## Signature

`serialize_pose( : : Pose : SerializedItemHandle)`

## Description

`serialize_pose` serializes the data of a pose (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The same data that is written in a
file by [`write_pose`](write_pose.md) is converted to a serialized item.
The pose is defined by the handle *`Pose`*. The
serialized pose is returned by the handle
*`SerializedItemHandle`* and can be deserialized by
[`deserialize_pose`](deserialize_pose.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Pose`** (input_control)  pose `→`  (real / integer)

3D pose.

Number of elements:
7

**`SerializedItemHandle`** (output_control)  serialized_item `→`  (handle)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_pose` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Successors

`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_pose`

## Module

Foundation
