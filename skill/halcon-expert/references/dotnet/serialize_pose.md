# SerializePose (Operator)

## Name

`SerializePose` — Serialize a pose.

## Signature

`static void HOperatorSet.SerializePose(HTuple pose, out HTuple serializedItemHandle)`

`HSerializedItem HPose.SerializePose()`

## Description

`SerializePose` serializes the data of a pose (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The same data that is written in a
file by [`WritePose`](write_pose.md) is converted to a serialized item.
The pose is defined by the handle *`pose`*. The
serialized pose is returned by the handle
*`serializedItemHandle`* and can be deserialized by
[`DeserializePose`](deserialize_pose.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`pose`** (input_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

3D pose.

Number of elements:
7

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializePose` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Successors

`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializePose`

## Module

Foundation
