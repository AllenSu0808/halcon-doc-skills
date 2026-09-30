# deserialize_quat (Operator)

## Name

`deserialize_quat` — Deserialize a serialized quaternion.

## Signature

`def deserialize_quat(serialized_item_handle: HHandle) -> Sequence[Union[float, int]]`

## Description

`deserialize_quat` deserializes a quaternion, that was
serialized by [`serialize_quat`](serialize_quat.md) (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized quaternion is defined by
the handle *`serialized_item_handle`*. The deserialized values are
stored in *`quaternion`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serialized_item_handle`** (input_control)  serialized_item `→` HHandle

Handle of the serialized item.

**`quaternion`** (output_control)  quaternion `→` Sequence[Union[float, int]]

Quaternion.

## Result

If the parameters are valid, the operator `deserialize_quat`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_quat`

## Possible Successors

`quat_to_hom_mat3d`,
`quat_to_pose`,
`quat_rotate_point_3d`,
`quat_compose`

## Module

Foundation
