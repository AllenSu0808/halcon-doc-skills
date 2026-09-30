# SerializeDualQuat (Operator)

## Name

`SerializeDualQuat` — Serialize a dual quaternion.

## Signature

`static void HOperatorSet.SerializeDualQuat(HTuple dualQuaternion, out HTuple serializedItemHandle)`

`HSerializedItem HDualQuaternion.SerializeDualQuat()`

## Description

`SerializeDualQuat` serializes the data of the
*`dualQuaternion`* (see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The serialized
dual quaternion is returned by the handle *`serializedItemHandle`* and
can be deserialized by [`DeserializeDualQuat`](deserialize_dual_quat.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dualQuaternion`** (input_control)  dual_quaternion `→` [HDualQuaternion](HDualQuaternion.md), [HTuple](HTuple.md) (*double* / int / long)

Dual quaternion.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator `SerializeDualQuat`
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
