# CamParPoseToHomMat3d (Operator)

## Name

`CamParPoseToHomMat3d` — Convert internal camera parameters and a 3D pose into a 3×4
projection matrix.

## Signature

`static void HOperatorSet.CamParPoseToHomMat3d(HTuple cameraParam, HTuple pose, out HTuple homMat3D)`

`HHomMat3D HCamPar.CamParPoseToHomMat3d(HPose pose)`

`HHomMat3D HPose.CamParPoseToHomMat3d(HCamPar cameraParam)`

## Description

`CamParPoseToHomMat3d` converts the internal camera
parameters *`cameraParam`* and the 3D pose *`pose`*, which
represent the external camera parameters, into the 3×4 projection
matrix *`homMat3D`*, which can be used to project points from
3D to 2D. The conversion can only be performed if the distortion
coefficients in *`cameraParam`* are 0. If necessary,
[`ChangeRadialDistortionCamPar`](change_radial_distortion_cam_par.md) must be used to achieve
this. The internal camera parameters and the pose are typically
obtained with [`CalibrateCameras`](calibrate_cameras.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`cameraParam`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Internal camera parameters.

**`pose`** (input_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

3D pose.

Number of elements:
7

**`homMat3D`** (output_control)  hom_mat3d `→` [HHomMat3D](HHomMat3D.md), [HTuple](HTuple.md) (*double*)

3×4 projection matrix.

## Result

`CamParPoseToHomMat3d` returns 2 (
H_MSG_TRUE)
if all parameter
values are correct. If necessary, an exception is raised

## Possible Predecessors

`CalibrateCameras`,
`ChangeRadialDistortionCamPar`

## Possible Successors

`ProjectPointHomMat3d`,
`ProjectHomPointHomMat3d`

## See also

`CreatePose`,
`HomMat3dToPose`,
`Project3dPoint`,
`GetLineOfSight`

## Module

Foundation
