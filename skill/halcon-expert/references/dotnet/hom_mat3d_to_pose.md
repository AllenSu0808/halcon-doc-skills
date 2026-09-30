# HomMat3dToPose (Operator)

## Name

`HomMat3dToPose` — Convert a homogeneous transformation matrix into a 3D pose.

## Signature

`static void HOperatorSet.HomMat3dToPose(HTuple homMat3D, out HTuple pose)`

`HPose HHomMat3D.HomMat3dToPose()`

## Description

`HomMat3dToPose` converts a homogeneous transformation matrix into
the corresponding 3D pose with type code 0. For details about 3D poses and
the corresponding transformation matrices please refer to
[`CreatePose`](create_pose.md).

A typical application of `HomMat3dToPose` is that a 3D pose was
converted into a homogeneous transformation matrix to further transform it,
e.g., with [`HomMat3dRotate`](hom_mat3d_rotate.md) or [`HomMat3dTranslate`](hom_mat3d_translate.md), and now
must be converted back into a pose to use it as input for operators like
[`ImagePointsToWorldPlane`](image_points_to_world_plane.md).

## Attention

`HomMat3dToPose` only supports rigid transformations in
*`homMat3D`*. For non-rigid transformations, the operator attempts to
return a pose that is close to *`homMat3D`*. If *`homMat3D`*
deviates significantly from a rigid transformation, the generated pose
may also deviate significantly from *`homMat3D`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`homMat3D`** (input_control)  hom_mat3d `→` [HHomMat3D](HHomMat3D.md), [HTuple](HTuple.md) (*double*)

Homogeneous transformation matrix.

**`pose`** (output_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

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

`HomMat3dToPose` returns 2 (
H_MSG_TRUE)
if all parameter values are
correct. If necessary, an exception is raised

## Possible Predecessors

`HomMat3dRotate`,
`HomMat3dTranslate`,
`HomMat3dInvert`

## Possible Successors

`CameraCalibration`,
`WritePose`,
`DispCaltab`,
`SimCaltab`

## See also

`CreatePose`,
`CameraCalibration`,
`DispCaltab`,
`SimCaltab`,
`WritePose`,
`ReadPose`,
`PoseToHomMat3d`,
`Project3dPoint`,
`GetLineOfSight`,
`HomMat3dRotate`,
`HomMat3dTranslate`,
`HomMat3dInvert`,
`AffineTransPoint3d`

## Module

Foundation
