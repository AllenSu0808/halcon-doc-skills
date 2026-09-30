# DeserializeQuat (Operator)

## Name

`DeserializeQuat` — Deserialize a serialized quaternion.

## Signature

`static void HOperatorSet.DeserializeQuat(HTuple serializedItemHandle, out HTuple quaternion)`

`void HQuaternion.DeserializeQuat(HSerializedItem serializedItemHandle)`

## Description

`DeserializeQuat` deserializes a quaternion, that was
serialized by [`SerializeQuat`](serialize_quat.md) (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized quaternion is defined by
the handle *`serializedItemHandle`*. The deserialized values are
stored in *`quaternion`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`quaternion`** (output_control)  quaternion `→` [HQuaternion](HQuaternion.md), [HTuple](HTuple.md) (*double* / int / long)

Quaternion.

## Result

If the parameters are valid, the operator `DeserializeQuat`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeQuat`

## Possible Successors

`QuatToHomMat3d`,
`QuatToPose`,
`QuatRotatePoint3d`,
`QuatCompose`

## Module

Foundation
