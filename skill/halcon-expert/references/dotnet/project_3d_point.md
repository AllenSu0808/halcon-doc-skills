# Project3dPoint (Operator)

## Name

`Project3dPoint` — Project 3D points into (sub-)pixel image coordinates.

## Signature

`static void HOperatorSet.Project3dPoint(HTuple x, HTuple y, HTuple z, HTuple cameraParam, out HTuple row, out HTuple column)`

`void HCamPar.Project3dPoint(HTuple x, HTuple y, HTuple z, out HTuple row, out HTuple column)`

## Description

`Project3dPoint` projects one or more 3D points (with coordinates
*`x`*, *`y`*, and *`z`*) into the image plane (in pixels) and
returns the result in *`row`* and *`column`*. The coordinates
*`x`*, *`y`*, and *`z`* are given in the camera coordinate
system, i.e., they describe the position of the points relative to the
camera.

The internal camera parameters *`cameraParam`* describe the projection
characteristics of the camera (see [Calibration](toc_calibration.md) for
details).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`x`** (input_control)  point3d.x-array `→` [HTuple](HTuple.md) (*double*)

X coordinates of the 3D points to be projected in the
camera coordinate system.

**`y`** (input_control)  point3d.y-array `→` [HTuple](HTuple.md) (*double*)

Y coordinates of the 3D points to be projected in the
camera coordinate system.

**`z`** (input_control)  point3d.z-array `→` [HTuple](HTuple.md) (*double*)

Z coordinates of the 3D points to be projected in the
camera coordinate system.

**`cameraParam`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Internal camera parameters.

**`row`** (output_control)  point.y-array `→` [HTuple](HTuple.md) (*double*)

Row coordinates of the projected points (in pixels).

**`column`** (output_control)  point.x-array `→` [HTuple](HTuple.md) (*double*)

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

`Project3dPoint` returns 2 (
H_MSG_TRUE)
if all parameter values are
correct. If necessary, an exception is raised.

## Possible Predecessors

`ReadCamPar`,
`AffineTransPoint3d`

## Possible Successors

`GenRegionPoints`,
`GenRegionPolygon`,
`DispPolygon`

## See also

`CameraCalibration`,
`DispCaltab`,
`ReadCamPar`,
`GetLineOfSight`,
`AffineTransPoint3d`,
`ImagePointsToWorldPlane`

## Module

Calibration
