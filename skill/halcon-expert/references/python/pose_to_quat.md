# pose_to_quat (Operator)

## Name

`pose_to_quat` — Convert the rotational part of a 3D pose to a quaternion.

## Signature

`def pose_to_quat(pose: Sequence[Union[float, int]]) -> Sequence[float]`

## Description

The operator `pose_to_quat` converts the rotation of the input 3D pose
*`pose`* into its corresponding quaternion *`quaternion`*.
Note that the translation of *`pose`* is ignored.
Multiple poses can be passed in *`pose`*, in which case a quaternion
is returned for each of them.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`pose`** (input_control)  pose(-array) `→` Sequence[Union[float, int]]

3D Pose.

**`quaternion`** (output_control)  quaternion(-array) `→` Sequence[float]

Rotation quaternion.

## Possible Predecessors

`create_pose`,
`read_pose`

## Possible Successors

`quat_compose`,
`quat_rotate_point_3d`,
`quat_interpolate`

## Alternatives

`axis_angle_to_quat`

## See also

`quat_to_pose`,
`quat_to_hom_mat3d`,
`quat_compose`,
`quat_rotate_point_3d`,
`pose_to_dual_quat`

## Module

Foundation
