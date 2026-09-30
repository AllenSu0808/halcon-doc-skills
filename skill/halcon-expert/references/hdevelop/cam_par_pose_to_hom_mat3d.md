# cam_par_pose_to_hom_mat3d (Operator)

## Name

`cam_par_pose_to_hom_mat3d` — Convert internal camera parameters and a 3D pose into a 3×4
projection matrix.

## Signature

`cam_par_pose_to_hom_mat3d( : : CameraParam, Pose : HomMat3D)`

## Description

`cam_par_pose_to_hom_mat3d` converts the internal camera
parameters *`CameraParam`* and the 3D pose *`Pose`*, which
represent the external camera parameters, into the 3×4 projection
matrix *`HomMat3D`*, which can be used to project points from
3D to 2D. The conversion can only be performed if the distortion
coefficients in *`CameraParam`* are 0. If necessary,
[`change_radial_distortion_cam_par`](change_radial_distortion_cam_par.md) must be used to achieve
this. The internal camera parameters and the pose are typically
obtained with [`calibrate_cameras`](calibrate_cameras.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`CameraParam`** (input_control)  campar `→`  (real / integer / string)

Internal camera parameters.

**`Pose`** (input_control)  pose `→`  (real / integer)

3D pose.

Number of elements:
7

**`HomMat3D`** (output_control)  hom_mat3d `→`  (real)

3×4 projection matrix.

## Result

`cam_par_pose_to_hom_mat3d` returns 2 (
H_MSG_TRUE)
if all parameter
values are correct. If necessary, an exception is raised

## Possible Predecessors

`calibrate_cameras`,
`change_radial_distortion_cam_par`

## Possible Successors

`project_point_hom_mat3d`,
`project_hom_point_hom_mat3d`

## See also

`create_pose`,
`hom_mat3d_to_pose`,
`project_3d_point`,
`get_line_of_sight`

## Module

Foundation
