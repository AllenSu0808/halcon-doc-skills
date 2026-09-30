# dual_quat_to_pose (Operator)

## Name

`dual_quat_to_pose` — Convert a dual quaternion to a 3D pose.

## Signature

`dual_quat_to_pose( : : DualQuaternion : Pose)`

## Description

The operator `dual_quat_to_pose` converts the input
*`DualQuaternion`* into its corresponding 3D *`Pose`*.

For a brief introduction to dual quaternions, the used notation, and the
relationship between dual quaternions and screws, see
`“Solution Guide III-C - 3D Vision”`.

Multiple dual quaternions can be passed in *`DualQuaternion`*, in which
case a pose is returned for each of them.

## Attention

`dual_quat_to_pose` assumes that the input *`DualQuaternion`*
is a unit dual quaternion, and hence represents a 3D rigid
transformation. Otherwise the returned pose is not meaningful.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DualQuaternion`** (input_control)  dual_quaternion(-array) `→`  (real)

Unit dual quaternion.

**`Pose`** (output_control)  pose(-array) `→`  (real / integer)

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
