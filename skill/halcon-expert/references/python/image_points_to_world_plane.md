# image_points_to_world_plane (Operator)

## Name

`image_points_to_world_plane` — Transform image points into the plane z=0 of a world coordinate system.

## Signature

`def image_points_to_world_plane(camera_param: Sequence[Union[int, float, str]], world_pose: Sequence[Union[int, float]], rows: Sequence[Union[int, float]], cols: Sequence[Union[int, float]], scale: Union[int, float, str]) -> Tuple[Sequence[float], Sequence[float]]`

## Description

The operator `image_points_to_world_plane` transforms image points
which are given in *`rows`* and *`cols`* into the plane z=0 in a
world coordinate system and returns their 3D coordinates in *`x`* and
*`y`*. The world coordinate system is chosen by passing its pose
relative to the camera coordinate system in *`world_pose`*.
Hence, latter one is expected in the form
$\mathrm{CCS} P_{\mathrm{wcs}}$ ![figure](../assets/4c18b1c4fb564c93.svg), where
*ccs* denotes the camera coordinate system and
*wcs* the world coordinate system (see
[Transformations / Poses](toc_transformations_poses.md)
and `“Solution Guide III-C - 3D Vision”`).
In *`camera_param`* you must pass the internal camera parameters
(see [Calibration](toc_calibration.md) for the sequence of the parameters
and the underlying camera model).

In many cases *`camera_param`* and *`world_pose`* are the result of
calibrating the camera with the operator [`calibrate_cameras`](calibrate_cameras.md). See
below for an example.

With the parameter *`scale`* you can scale the resulting 3D coordinates.
The parameter *`scale`* must be specified as the ratio *desired
unit/original unit*. The original unit is determined by the coordinates of
the calibration object. If the original unit is meters (which is the case if
you use the standard calibration plate), you can set the desired unit
directly by selecting *"m"*, *"cm"*, *"mm"* or
*"um"* for the parameter *`scale`*.

Internally, the operator first computes the line of sight between the
projection center and the image contour points in the camera coordinate
system, taking into account the radial distortions. The line of sight is
then transformed into the world coordinate system specified in
*`world_pose`*. By intersecting the plane z=0 with the line of sight the
3D coordinates *`x`* and *`y`* are obtained.

It is recommended to use only those image points *`rows`* and
*`cols`*, that lie within the calibrated image size. The mathematical
model does only work well for image points, that lie within the calibration
range.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`camera_param`** (input_control)  campar `→` Sequence[Union[int, float, str]]

Internal camera parameters.

**`world_pose`** (input_control)  pose `→` Sequence[Union[int, float]]

3D pose of the world coordinate system in camera
coordinates.

Number of elements:
7

**`rows`** (input_control)  coordinates.y-array `→` Sequence[Union[int, float]]

Row coordinates of the points to be transformed.

Default:
100.0

**`cols`** (input_control)  coordinates.x-array `→` Sequence[Union[int, float]]

Column coordinates of the points to be transformed.

Default:
100.0

**`scale`** (input_control)  number `→` Union[int, float, str]

Scale or dimension

Default:
"m"

Suggested values:
"m", "cm", "mm", "microns", "um", 1.0, 0.01, 0.001, 1.0e-6, 0.0254, 0.3048, 0.9144

Restriction:
`Scale > 0`

**`x`** (output_control)  coordinates.x-array `→` Sequence[float]

X coordinates of the points in the world coordinate
system.

**`y`** (output_control)  coordinates.y-array `→` Sequence[float]

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
