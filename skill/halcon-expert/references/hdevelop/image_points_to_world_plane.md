# image_points_to_world_plane (Operator)

## Name

`image_points_to_world_plane` — Transform image points into the plane z=0 of a world coordinate system.

## Signature

`image_points_to_world_plane( : : CameraParam, WorldPose, Rows, Cols, Scale : X, Y)`

## Description

The operator `image_points_to_world_plane` transforms image points
which are given in *`Rows`* and *`Cols`* into the plane z=0 in a
world coordinate system and returns their 3D coordinates in *`X`* and
*`Y`*. The world coordinate system is chosen by passing its pose
relative to the camera coordinate system in *`WorldPose`*.
Hence, latter one is expected in the form
$\mathrm{CCS} P_{\mathrm{wcs}}$ ![figure](../assets/4c18b1c4fb564c93.svg), where
*ccs* denotes the camera coordinate system and
*wcs* the world coordinate system (see
[Transformations / Poses](toc_transformations_poses.md)
and `“Solution Guide III-C - 3D Vision”`).
In *`CameraParam`* you must pass the internal camera parameters
(see [Calibration](toc_calibration.md) for the sequence of the parameters
and the underlying camera model).

In many cases *`CameraParam`* and *`WorldPose`* are the result of
calibrating the camera with the operator [`calibrate_cameras`](calibrate_cameras.md). See
below for an example.

With the parameter *`Scale`* you can scale the resulting 3D coordinates.
The parameter *`Scale`* must be specified as the ratio *desired
unit/original unit*. The original unit is determined by the coordinates of
the calibration object. If the original unit is meters (which is the case if
you use the standard calibration plate), you can set the desired unit
directly by selecting *'m'*, *'cm'*, *'mm'* or
*'um'* for the parameter *`Scale`*.

Internally, the operator first computes the line of sight between the
projection center and the image contour points in the camera coordinate
system, taking into account the radial distortions. The line of sight is
then transformed into the world coordinate system specified in
*`WorldPose`*. By intersecting the plane z=0 with the line of sight the
3D coordinates *`X`* and *`Y`* are obtained.

It is recommended to use only those image points *`Rows`* and
*`Cols`*, that lie within the calibrated image size. The mathematical
model does only work well for image points, that lie within the calibration
range.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`CameraParam`** (input_control)  campar `→`  (real / integer / string)

Internal camera parameters.

**`WorldPose`** (input_control)  pose `→`  (real / integer)

3D pose of the world coordinate system in camera
coordinates.

Number of elements:
7

**`Rows`** (input_control)  coordinates.y-array `→`  (real / integer)

Row coordinates of the points to be transformed.

Default:
100.0

**`Cols`** (input_control)  coordinates.x-array `→`  (real / integer)

Column coordinates of the points to be transformed.

Default:
100.0

**`Scale`** (input_control)  number `→`  (string / integer / real)

Scale or dimension

Default:
'm'

Suggested values:
'm', 'cm', 'mm', 'microns', 'um', 1.0, 0.01, 0.001, 1.0e-6, 0.0254, 0.3048, 0.9144

Restriction:
`Scale > 0`

**`X`** (output_control)  coordinates.x-array `→`  (real)

X coordinates of the points in the world coordinate
system.

**`Y`** (output_control)  coordinates.y-array `→`  (real)

Y coordinates of the points in the world coordinate
system.

## Example (HDevelop)

```
*  Perform camera calibration (with standard calibration plate).
calibrate_cameras (CalibDataID, Error)
get_calib_data (CalibDataID, 'camera', 0, 'params', CamParam)
* Get reference pose (pose 2 of calibration object 0).
get_calib_data (CalibDataID, 'calib_obj_pose',\
                [0,2], 'pose', WorldPose)
*  Compensate thickness of plate.
set_origin_pose(ObjInCameraPose, 0, 0, 0.0006, WorldPose)
*  Transform image points into world coordinate system (unit mm).
image_points_to_world_plane(CamParam, WorldPose, PointRows, PointColumns, \
                            'mm', PointXCoord, PointYCoord)
```

## Result

`image_points_to_world_plane` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct. If necessary, an exception is raised.

## Possible Predecessors

`create_pose`,
`hom_mat3d_to_pose`,
`camera_calibration`,
`hand_eye_calibration`,
`set_origin_pose`

## See also

`contour_to_world_plane_xld`,
`project_3d_point`

## Module

Calibration
