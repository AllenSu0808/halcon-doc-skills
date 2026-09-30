# pose_to_dual_quat (Operator)

## Name

`pose_to_dual_quat` — Convert a 3D pose to a unit dual quaternion.

## Signature

`def pose_to_dual_quat(pose: Sequence[Union[float, int]]) -> Sequence[float]`

## Description

The operator `pose_to_dual_quat` converts the input *`pose`*
into its corresponding unit dual quaternion *`dual_quaternion`*.

For a brief introduction to dual quaternions, the used notation, and the
relationship between dual quaternions and screws, see
`“Solution Guide III-C - 3D Vision”`.

Because $\hat{q}$ ![figure](../assets/2e9ecba020103681.svg) and $-\hat{q}$ ![figure](../assets/eeef33b74ca60093.svg) represent the same rigid
transformation, the sign of the resulting dual quaternion
*`dual_quaternion`* is chosen such that the scalar part of the real
part is $\ge0$.

Multiple poses can be passed in *`pose`*, in which case a unit dual
quaternion is returned for each of them.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`pose`** (input_control)  pose(-array) `→` Sequence[Union[float, int]]

3D pose.

**`dual_quaternion`** (output_control)  dual_quaternion(-array) `→` Sequence[float]

Unit dual quaternion.

## Possible Predecessors

`create_pose`,
`read_pose`

## Possible Successors

`dual_quat_compose`,
`dual_quat_interpolate`,
`dual_quat_to_screw`,
`dual_quat_conjugate`

## Alternatives

`pose_to_hom_mat3d`,
`screw_to_dual_quat`

## See also

`dual_quat_to_hom_mat3d`,
`dual_quat_to_pose`,
`dual_quat_normalize`,
`serialize_dual_quat`,
`deserialize_dual_quat`,
`dual_quat_trans_line_3d`,
`dual_quat_trans_point_3d`,
`pose_to_quat`

## Module

Foundation
