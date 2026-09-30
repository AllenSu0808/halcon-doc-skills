# DeserializePose (Operator)

## Name

`DeserializePose` — Deserialize a serialized pose.

## Signature

`static void HOperatorSet.DeserializePose(HTuple serializedItemHandle, out HTuple pose)`

`void HPose.DeserializePose(HSerializedItem serializedItemHandle)`

## Description

`DeserializePose` deserializes a pose, that was serialized
by [`SerializePose`](serialize_pose.md) (see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The
serialized pose is defined by the handle *`serializedItemHandle`*.
The deserialized values are stored in an automatically created
pose with the handle *`pose`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`pose`** (output_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

3D pose.

Number of elements:
7

## Result

If the parameters are valid, the operator
`DeserializePose` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializePose`

## Module

Foundation
