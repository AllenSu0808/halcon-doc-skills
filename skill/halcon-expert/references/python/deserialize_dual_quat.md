# deserialize_dual_quat (Operator)

## Name

`deserialize_dual_quat` — Deserialize a serialized dual quaternion.

## Signature

`def deserialize_dual_quat(serialized_item_handle: HHandle) -> Sequence[Union[float, int]]`

## Description

`deserialize_dual_quat` deserializes a dual quaternion that was
serialized by [`serialize_dual_quat`](serialize_dual_quat.md) (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized dual quaternion is defined by
the handle *`serialized_item_handle`*. The deserialized values are
stored in *`dual_quaternion`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serialized_item_handle`** (input_control)  serialized_item `→` HHandle

Handle of the serialized item.

**`dual_quaternion`** (output_control)  dual_quaternion `→` Sequence[Union[float, int]]

Dual quaternion.

## Result

If the parameters are valid, the operator `deserialize_dual_quat`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_quat`

## Possible Successors

`dual_quat_to_hom_mat3d`,
`dual_quat_to_pose`,
`dual_quat_compose`

## Module

Foundation
