# SetOriginPose (Operator)

## Name

`SetOriginPose` — Translate the origin of a 3D pose.

## Signature

`static void HOperatorSet.SetOriginPose(HTuple poseIn, HTuple DX, HTuple DY, HTuple DZ, out HTuple poseNewOrigin)`

`HPose HPose.SetOriginPose(double DX, double DY, double DZ)`

## Description

`SetOriginPose` translates the origin of the 3D pose *`poseIn`*
by the vector given by *`DX`*, *`DY`*, and *`DZ`* and returns
the result in *`poseNewOrigin`*. Note that the translation is performed
relative to the local coordinate system of the pose itself. For example, if
*`poseIn`* describes the pose of an object in camera coordinates,
*`poseNewOrigin`* is obtained by translating the object's coordinate
system by *`DX`* along its own x-axis (and so on for the other axes) and
not along the x-axis of the camera coordinate system. This corresponds to the
following chain of transformations:

$$\text{PoseNewOrigin} = \text{PoseIn} \cdot \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \\ \end{bmatrix} \begin{pmatrix} DX \\ DY \\ DZ \\ 1 \end{pmatrix}$$ ![figure](../assets/bb12e513b0439d43.svg)

Thus, `SetOriginPose` is a shortcut for the following sequence of
operator calls:

|  |
| --- |
| [`PoseToHomMat3d(PoseIn, HomMat3DIn)`](pose_to_hom_mat3d.md) |
| [`HomMat3dTranslateLocal(HomMat3DIn, DX, DY, DZ, HomMat3DNewOrigin)`](hom_mat3d_translate_local.md) |
| [`HomMat3dToPose(HomMat3DNewOrigin, PoseNewOrigin)`](hom_mat3d_to_pose.md) |
|  |

A typical application of this operator when defining a world
coordinate system by placing the standard calibration plate on the plane of
measurements. In this case, the external camera parameters returned by
[`CameraCalibration`](camera_calibration.md) correspond to a coordinate system that lies above
the measurement plane, because the coordinate system of the calibration plate
is located on its surface and the plate has a certain thickness. To correct
the pose, call `SetOriginPose` with the translation vector
(0,0,D), where D is the thickness of the calibration plate.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`poseIn`** (input_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

original 3D pose.

Number of elements:
7

**`DX`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

translation of the origin in x-direction.

Default:
0

**`DY`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

translation of the origin in y-direction.

Default:
0

**`DZ`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

translation of the origin in z-direction.

Default:
0

**`poseNewOrigin`** (output_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

new 3D pose after applying the translation.

Number of elements:
7

## Result

`SetOriginPose` returns 2 (
H_MSG_TRUE)
if all parameter values are
correct. If necessary, an exception is raised.

## Possible Predecessors

`CreatePose`,
`HomMat3dToPose`,
`CameraCalibration`,
`HandEyeCalibration`

## Possible Successors

`WritePose`,
`PoseToHomMat3d`,
`ImagePointsToWorldPlane`,
`ContourToWorldPlaneXld`

## See also

`HomMat3dTranslateLocal`

## Module

Foundation
