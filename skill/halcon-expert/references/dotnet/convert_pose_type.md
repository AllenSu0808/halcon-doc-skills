# ConvertPoseType (Operator)

## Name

`ConvertPoseType` — Change the representation type of a 3D pose.

## Signature

`static void HOperatorSet.ConvertPoseType(HTuple poseIn, HTuple orderOfTransform, HTuple orderOfRotation, HTuple viewOfTransform, out HTuple poseOut)`

`HPose HPose.ConvertPoseType(string orderOfTransform, string orderOfRotation, string viewOfTransform)`

## Description

`ConvertPoseType` converts the 3D pose *`poseIn`* into
a 3D pose *`poseOut`* with a different representation type. See
[`CreatePose`](create_pose.md) for details about 3D poses, their representation
types, and the meaning of the parameters *`orderOfTransform`*,
*`orderOfRotation`*, and *`viewOfTransform`*.

Note that `ConvertPoseType` only changes the representation of a 3D
pose, but not the rigid transformation described by the pose.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`poseIn`** (input_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

Original 3D pose.

Number of elements:
7

**`orderOfTransform`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Order of rotation and translation.

Default:
"Rp+T"

Suggested values:
"Rp+T", "R(p-T)"

**`orderOfRotation`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Meaning of the rotation values.

Default:
"gba"

Suggested values:
"gba", "abg", "rodriguez"

**`viewOfTransform`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

View of transformation.

Default:
"point"

Suggested values:
"point", "coordinate_system"

**`poseOut`** (output_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

3D transformation.

Number of elements:
7

## Example (HDevelop)

```
* Define a pose.
create_pose (0.1, 0.1, 0.1, 90, 90, 90, 'Rp+T', 'gba', 'point', Pose)
* Convert pose to a pose with desired semantic.
convert_pose_type (Pose, 'Rp+T', 'abg', 'point', Pose2)
```

## Result

`ConvertPoseType` returns 2 (
H_MSG_TRUE)
if all parameter values are
correct. If necessary, an exception is raised.

## Possible Predecessors

`CreatePose`,
`HomMat3dToPose`,
`CameraCalibration`,
`HandEyeCalibration`

## Possible Successors

`WritePose`

## See also

`CreatePose`,
`GetPoseType`,
`WritePose`,
`ReadPose`

## Module

Foundation
