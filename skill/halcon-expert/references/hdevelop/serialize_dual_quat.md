# serialize_dual_quat (Operator)

## Name

`serialize_dual_quat` — Serialize a dual quaternion.

## Signature

`serialize_dual_quat( : : DualQuaternion : SerializedItemHandle)`

## Description

`serialize_dual_quat` serializes the data of the
*`DualQuaternion`* (see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The serialized
dual quaternion is returned by the handle *`SerializedItemHandle`* and
can be deserialized by [`deserialize_dual_quat`](deserialize_dual_quat.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DualQuaternion`** (input_control)  dual_quaternion `→`  (real / integer)

Dual quaternion.

**`SerializedItemHandle`** (output_control)  serialized_item `→`  (handle)

Handle of the serialized item.

## Result

If the parameters are valid, the operator `serialize_dual_quat`
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
