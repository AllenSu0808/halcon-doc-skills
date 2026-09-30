# dual_quat_to_pose (Operator)

## Name

`dual_quat_to_pose` — Convert a dual quaternion to a 3D pose.

## Signature

`def dual_quat_to_pose(dual_quaternion: Sequence[float]) -> Sequence[Union[float, int]]`

## Description

The operator `dual_quat_to_pose` converts the input
*`dual_quaternion`* into its corresponding 3D *`pose`*.

For a brief introduction to dual quaternions, the used notation, and the
relationship between dual quaternions and screws, see
`“Solution Guide III-C - 3D Vision”`.

Multiple dual quaternions can be passed in *`dual_quaternion`*, in which
case a pose is returned for each of them.

## Attention

`dual_quat_to_pose` assumes that the input *`dual_quaternion`*
is a unit dual quaternion, and hence represents a 3D rigid
transformation. Otherwise the returned pose is not meaningful.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dual_quaternion`** (input_control)  dual_quaternion(-array) `→` Sequence[float]

Unit dual quaternion.

**`pose`** (output_control)  pose(-array) `→` Sequence[Union[float, int]]

3D pose.

## Possible Predecessors

`dual_quat_compose`,
`dual_quat_interpolate`,
`screw_to_dual_quat`,
`dual_quat_conjugate`

## Possible Successors

`camera_calibration`,
`hand_eye_calibration`,
`write_pose`,
`disp_caltab`,
`sim_caltab`

## Alternatives

`dual_quat_to_screw`,
`dual_quat_to_hom_mat3d`

## See also

`pose_to_dual_quat`,
`dual_quat_normalize`,
`serialize_dual_quat`,
`deserialize_dual_quat`,
`dual_quat_trans_line_3d`,
`dual_quat_trans_point_3d`,
`quat_to_pose`

## Module

Foundation
