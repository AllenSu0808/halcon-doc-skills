# DeserializeDualQuat (Operator)

## Name

`DeserializeDualQuat` — Deserialize a serialized dual quaternion.

## Signature

`static void HOperatorSet.DeserializeDualQuat(HTuple serializedItemHandle, out HTuple dualQuaternion)`

`void HDualQuaternion.DeserializeDualQuat(HSerializedItem serializedItemHandle)`

## Description

`DeserializeDualQuat` deserializes a dual quaternion that was
serialized by [`SerializeDualQuat`](serialize_dual_quat.md) (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized dual quaternion is defined by
the handle *`serializedItemHandle`*. The deserialized values are
stored in *`dualQuaternion`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`dualQuaternion`** (output_control)  dual_quaternion `→` [HDualQuaternion](HDualQuaternion.md), [HTuple](HTuple.md) (*double* / int / long)

Dual quaternion.

## Result

If the parameters are valid, the operator `DeserializeDualQuat`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeQuat`

## Possible Successors

`DualQuatToHomMat3d`,
`DualQuatToPose`,
`DualQuatCompose`

## Module

Foundation
