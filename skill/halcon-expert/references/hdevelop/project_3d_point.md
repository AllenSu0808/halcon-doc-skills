# project_3d_point (Operator)

## Name

`project_3d_point` — Project 3D points into (sub-)pixel image coordinates.

## Signature

`project_3d_point( : : X, Y, Z, CameraParam : Row, Column)`

## Description

`project_3d_point` projects one or more 3D points (with coordinates
*`X`*, *`Y`*, and *`Z`*) into the image plane (in pixels) and
returns the result in *`Row`* and *`Column`*. The coordinates
*`X`*, *`Y`*, and *`Z`* are given in the camera coordinate
system, i.e., they describe the position of the points relative to the
camera.

The internal camera parameters *`CameraParam`* describe the projection
characteristics of the camera (see [Calibration](toc_calibration.md) for
details).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`X`** (input_control)  point3d.x-array `→`  (real)

X coordinates of the 3D points to be projected in the
camera coordinate system.

**`Y`** (input_control)  point3d.y-array `→`  (real)

Y coordinates of the 3D points to be projected in the
camera coordinate system.

**`Z`** (input_control)  point3d.z-array `→`  (real)

Z coordinates of the 3D points to be projected in the
camera coordinate system.

**`CameraParam`** (input_control)  campar `→`  (real / integer / string)

Internal camera parameters.

**`Row`** (output_control)  point.y-array `→`  (real)

Row coordinates of the projected points (in pixels).

**`Column`** (output_control)  point.x-array `→`  (real)

Column coordinates of the projected points (in pixels).

## Example (HDevelop)

```
* Set internal camera parameters and pose of the world coordinate
* system in camera coordinates.
* Note that, typically, these values are the result of a prior
* calibration.
gen_cam_par_area_scan_division (0.01, -731, 5.2e-006, 5.2e-006, \
                                654, 519, 1280, 1024, CameraParam)
create_pose (0.1, 0.2, 0.3, 40, 50, 60, \
             'Rp+T', 'gba', 'point', WorldPose)
* Convert pose into transformation matrix.
pose_to_hom_mat3d(WorldPose, HomMat3D)
* Transform 3D points from world into the camera coordinate system.
affine_trans_point_3d(HomMat3D, [3.0, 3.2], [4.5, 4.5], [3.8, 4.2], X, Y, Z)
* Project 3D points into image.
project_3d_point(X, Y, Z, CameraParam, Row, Column)
```

## Result

`project_3d_point` returns 2 (
H_MSG_TRUE)
if all parameter values are
correct. If necessary, an exception is raised.

## Possible Predecessors

`read_cam_par`,
`affine_trans_point_3d`

## Possible Successors

`gen_region_points`,
`gen_region_polygon`,
`disp_polygon`

## See also

`camera_calibration`,
`disp_caltab`,
`read_cam_par`,
`get_line_of_sight`,
`affine_trans_point_3d`,
`image_points_to_world_plane`

## Module

Calibration
