# GetPoseType (Operator)

## Name

`GetPoseType` — Get the representation type of a 3D pose.

## Signature

`static void HOperatorSet.GetPoseType(HTuple pose, out HTuple orderOfTransform, out HTuple orderOfRotation, out HTuple viewOfTransform)`

`string HPose.GetPoseType(out string orderOfRotation, out string viewOfTransform)`

## Description

With `GetPoseType`, the representation type of the 3D pose
*`pose`* can be queried. See [`CreatePose`](create_pose.md) for details about 3D
poses, their representation types, and the meaning of the parameters
*`orderOfTransform`*, *`orderOfRotation`*, and
*`viewOfTransform`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`pose`** (input_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

3D pose.

Number of elements:
7

**`orderOfTransform`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Order of rotation and translation.

**`orderOfRotation`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Meaning of the rotation values.

**`viewOfTransform`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

View of transformation.

## Result

[`CreatePose`](create_pose.md) returns 2 (
H_MSG_TRUE)
if all parameter values are
correct. If necessary, an exception is raised.

## Possible Predecessors

`CreatePose`,
`HomMat3dToPose`,
`CameraCalibration`,
`HandEyeCalibration`

## Possible Successors

`ConvertPoseType`

## See also

`CreatePose`,
`ConvertPoseType`,
`WritePose`,
`ReadPose`

## Module

Foundation
