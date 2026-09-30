# hom_mat3d_to_pose (Operator)

## Name

`hom_mat3d_to_pose` — Convert a homogeneous transformation matrix into a 3D pose.

## Signature

`def hom_mat3d_to_pose(hom_mat_3d: Sequence[float]) -> Sequence[Union[int, float]]`

## Description

`hom_mat3d_to_pose` converts a homogeneous transformation matrix into
the corresponding 3D pose with type code 0. For details about 3D poses and
the corresponding transformation matrices please refer to
[`create_pose`](create_pose.md).

A typical application of `hom_mat3d_to_pose` is that a 3D pose was
converted into a homogeneous transformation matrix to further transform it,
e.g., with [`hom_mat3d_rotate`](hom_mat3d_rotate.md) or [`hom_mat3d_translate`](hom_mat3d_translate.md), and now
must be converted back into a pose to use it as input for operators like
[`image_points_to_world_plane`](image_points_to_world_plane.md).

## Attention

`hom_mat3d_to_pose` only supports rigid transformations in
*`hom_mat_3d`*. For non-rigid transformations, the operator attempts to
return a pose that is close to *`hom_mat_3d`*. If *`hom_mat_3d`*
deviates significantly from a rigid transformation, the generated pose
may also deviate significantly from *`hom_mat_3d`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`hom_mat_3d`** (input_control)  hom_mat3d `→` Sequence[float]

Homogeneous transformation matrix.

**`pose`** (output_control)  pose `→` Sequence[Union[int, float]]

Equivalent 3D pose.

Number of elements:
7

## Example (HDevelop)

```
* Calibrate camera.
calibrate_cameras (CalibDataID,Error)
* Get reference pose (pose 2 of calibration object 0).
get_calib_data (CalibDataID, 'calib_obj_pose',\
                [0,2], 'pose', ObjInCameraPose)
*  Convert pose to homogeneous transformation matrix.
pose_to_hom_mat3d(ObjInCameraPose, cam_H_cal)
*  Rotate it 90 degrees around its y-axis to obtain a world coordinate system
*  whose y- and z-axis lie in the plane of the calibration plate while the
*  x-axis point 'upwards': cam_H_w = cam_H_cal * RotY(90).
hom_mat3d_identity(HomMat3DIdent)
hom_mat3d_rotate(HomMat3DIdent, rad(90), 'y', 0, 0, 0, \
                 HomMat3DRotateY)
hom_mat3d_compose(cam_H_cal, HomMat3DRotateY, cam_H_w)
* Convert transformed matrix back to pose.
hom_mat3d_to_pose (cam_H_w, Pose)
```

## Result

`hom_mat3d_to_pose` returns 2 (
H_MSG_TRUE)
if all parameter values are
correct. If necessary, an exception is raised

## Possible Predecessors

`hom_mat3d_rotate`,
`hom_mat3d_translate`,
`hom_mat3d_invert`

## Possible Successors

`camera_calibration`,
`write_pose`,
`disp_caltab`,
`sim_caltab`

## See also

`create_pose`,
`camera_calibration`,
`disp_caltab`,
`sim_caltab`,
`write_pose`,
`read_pose`,
`pose_to_hom_mat3d`,
`project_3d_point`,
`get_line_of_sight`,
`hom_mat3d_rotate`,
`hom_mat3d_translate`,
`hom_mat3d_invert`,
`affine_trans_point_3d`

## Module

Foundation
