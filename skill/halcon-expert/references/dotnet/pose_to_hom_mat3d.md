# PoseToHomMat3d (Operator)

## Name

`PoseToHomMat3d` — Convert a 3D pose into a homogeneous transformation matrix.

## Signature

`static void HOperatorSet.PoseToHomMat3d(HTuple pose, out HTuple homMat3D)`

`HHomMat3D HPose.PoseToHomMat3d()`

## Description

`PoseToHomMat3d` converts a 3D pose *`pose`*,
e.g., the external camera parameters, into the
equivalent homogeneous transformation matrix *`homMat3D`*. For details
about 3D poses and the corresponding transformation matrices please refer to
[`CreatePose`](create_pose.md).

A typical application of `PoseToHomMat3d` is that you want
to further transform the pose, e.g., rotate or translate it using
[`HomMat3dRotate`](hom_mat3d_rotate.md) or [`HomMat3dTranslate`](hom_mat3d_translate.md). In case of the
external camera parameters, this can be necessary if the calibration plate
cannot be placed such that its coordinate system coincides with the desired
world coordinate system.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`pose`** (input_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

3D pose.

Number of elements:
7

**`homMat3D`** (output_control)  hom_mat3d `→` [HHomMat3D](HHomMat3D.md), [HTuple](HTuple.md) (*double*)

Equivalent homogeneous transformation matrix.

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

`PoseToHomMat3d` returns 2 (
H_MSG_TRUE)
if all parameter values are
correct. If necessary, an exception is raised

## Possible Predecessors

`CameraCalibration`,
`ReadPose`

## Possible Successors

`AffineTransPoint3d`,
`HomMat3dInvert`,
`HomMat3dTranslate`,
`HomMat3dRotate`,
`HomMat3dToPose`

## Alternatives

`PoseToDualQuat`

## See also

`CreatePose`,
`CameraCalibration`,
`WritePose`,
`ReadPose`,
`HomMat3dToPose`,
`Project3dPoint`,
`GetLineOfSight`,
`HomMat3dRotate`,
`HomMat3dTranslate`,
`HomMat3dInvert`,
`AffineTransPoint3d`

## Module

Foundation
