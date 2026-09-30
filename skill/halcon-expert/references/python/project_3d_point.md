# project_3d_point (Operator)

## Name

`project_3d_point` — Project 3D points into (sub-)pixel image coordinates.

## Signature

`def project_3d_point(x: Sequence[float], y: Sequence[float], z: Sequence[float], camera_param: Sequence[Union[int, float, str]]) -> Tuple[Sequence[float], Sequence[float]]`

## Description

`project_3d_point` projects one or more 3D points (with coordinates
*`x`*, *`y`*, and *`z`*) into the image plane (in pixels) and
returns the result in *`row`* and *`column`*. The coordinates
*`x`*, *`y`*, and *`z`* are given in the camera coordinate
system, i.e., they describe the position of the points relative to the
camera.

The internal camera parameters *`camera_param`* describe the projection
characteristics of the camera (see [Calibration](toc_calibration.md) for
details).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`x`** (input_control)  point3d.x-array `→` Sequence[float]

X coordinates of the 3D points to be projected in the
camera coordinate system.

**`y`** (input_control)  point3d.y-array `→` Sequence[float]

Y coordinates of the 3D points to be projected in the
camera coordinate system.

**`z`** (input_control)  point3d.z-array `→` Sequence[float]

Z coordinates of the 3D points to be projected in the
camera coordinate system.

**`camera_param`** (input_control)  campar `→` Sequence[Union[int, float, str]]

Internal camera parameters.

**`row`** (output_control)  point.y-array `→` Sequence[float]

Row coordinates of the projected points (in pixels).

**`column`** (output_control)  point.x-array `→` Sequence[float]

Column coordinates of the projected points (in pixels).

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
