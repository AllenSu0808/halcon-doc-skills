# contour_to_world_plane_xld (Operator)

## Name

`contour_to_world_plane_xld` — Transform an XLD contour into the plane z=0 of a world coordinate system.

## Signature

`contour_to_world_plane_xld(Contours : ContoursTrans : CameraParam, WorldPose, Scale : )`

## Description

The operator `contour_to_world_plane_xld` transforms contour points
given in *`Contours`* into the plane z=0 in a world coordinate system
and returns the 3D contour points in *`ContoursTrans`*. The world
coordinate system is chosen by passing its 3D pose relative to the camera
coordinate system in *`WorldPose`*.
Hence, latter one is expected in the form
$\mathrm{CCS} P_{\mathrm{wcs}}$ ![figure](../assets/4c18b1c4fb564c93.svg), where
*ccs* denotes the camera coordinate system and
*wcs* the world coordinate system
(see [Transformations / Poses](toc_transformations_poses.md)
and `“Solution Guide III-C - 3D Vision”`).
In *`CameraParam`* you must pass the internal camera parameters
(see [Calibration](toc_calibration.md) for the sequence of the parameters and
the underlying camera model).

In many cases *`CameraParam`* and *`WorldPose`* are the result of
calibrating the camera with the operator [`calibrate_cameras`](calibrate_cameras.md). See
below for an example.

With the parameter *`Scale`* you can scale the resulting 3D
coordinates.
The parameter *`Scale`* must be specified as the ratio *desired
unit/original unit*. The original unit is determined by the coordinates of
the calibration object. If the original unit is meters (which is the case if
you use the standard calibration plate), you can set the desired unit
directly by selecting *'m'*, *'cm'*, *'mm'* or
*'um'* for the parameter *`Scale`*.

Internally, the operator first computes the line of sight between the
projection center and the image point in the camera coordinate system,
taking into account the radial distortions.
The line of sight is then transformed
into the world coordinate system specified in *`WorldPose`*. By
intersecting the plane z=0 with the line of sight the 3D coordinates of the
transformed contour *`ContoursTrans`* are obtained.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Contours`** (input_object)  xld_cont(-array) `→` object

Input XLD contours to be transformed in image
coordinates.

**`ContoursTrans`** (output_object)  xld_cont(-array) `→` object

Transformed XLD contours in world coordinates.

**`CameraParam`** (input_control)  number-array `→`  (real / integer / string)

Internal camera parameters.

**`WorldPose`** (input_control)  pose `→`  (real / integer)

3D pose of the world coordinate system in camera
coordinates.

Number of elements:
7

**`Scale`** (input_control)  number `→`  (string / integer / real)

Scale or dimension

Default:
'm'

Suggested values:
'm', 'cm', 'mm', 'microns', 'um', 1.0, 0.01, 0.001, 1.0e-6, 0.0254, 0.3048, 0.9144

Restriction:
`Scale > 0`

## Example (HDevelop)

```
*  Perform camera calibration (with standard calibration plate).
calibrate_cameras (CalibDataID, Error)
get_calib_data (CalibDataID, 'camera', 0, 'params', CamParam)
* Get reference pose (pose 2 of calibration object 0).
get_calib_data (CalibDataID, 'calib_obj_pose', [0,2], 'pose', WorldPose)
*  Compensate thickness of plate.
set_origin_pose(ObjInCameraPose, 0, 0, 0.0006, WorldPose)
*  Transform contours into world coordinate system (unit mm).
contour_to_world_plane_xld(Contours, ContoursTrans, CamParam, \
                           WorldPose, 'mm')
```

## Result

`contour_to_world_plane_xld` returns 2 (
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

`image_points_to_world_plane`

## Module

Calibration
