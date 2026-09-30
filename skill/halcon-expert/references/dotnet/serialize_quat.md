# SerializeQuat (Operator)

## Name

`SerializeQuat` — Serialize a quaternion.

## Signature

`static void HOperatorSet.SerializeQuat(HTuple quaternion, out HTuple serializedItemHandle)`

`HSerializedItem HQuaternion.SerializeQuat()`

## Description

`SerializeQuat` serializes the data of the *`quaternion`*
(see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized quaternion is returned by
the handle *`serializedItemHandle`* and can be deserialized by
[`DeserializeQuat`](deserialize_quat.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`quaternion`** (input_control)  quaternion `→` [HQuaternion](HQuaternion.md), [HTuple](HTuple.md) (*double* / int / long)

Quaternion.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator `SerializeQuat`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`AxisAngleToQuat`

## Possible Successors

`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeQuat`

## Module

Foundation
