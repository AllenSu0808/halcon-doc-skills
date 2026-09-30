# quat_to_pose (Operator)

## Name

`quat_to_pose` — Convert a quaternion into the corresponding 3D pose.

## Signature

`def quat_to_pose(quaternion: Sequence[float]) -> Sequence[Union[float, int]]`

## Description

The operator `quat_to_pose` converts the input quaternion
*`quaternion`* into its corresponding 3D pose *`pose`*. Note that
the translation of *`pose`* is zero in any case.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`quaternion`** (input_control)  quaternion `→` Sequence[float]

Rotation quaternion.

**`pose`** (output_control)  pose `→` Sequence[Union[float, int]]

3D Pose.

## Possible Predecessors

`axis_angle_to_quat`,
`quat_compose`,
`quat_conjugate`

## Possible Successors

`camera_calibration`,
`write_pose`,
`disp_caltab`,
`sim_caltab`

## See also

`pose_to_quat`,
`axis_angle_to_quat`,
`quat_compose`,
`quat_rotate_point_3d`,
`quat_to_hom_mat3d`,
`quat_normalize`,
`dual_quat_to_pose`

## Module

Foundation
