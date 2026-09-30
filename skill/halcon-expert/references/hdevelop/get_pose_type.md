# get_pose_type (Operator)

## Name

`get_pose_type` — Get the representation type of a 3D pose.

## Signature

`get_pose_type( : : Pose : OrderOfTransform, OrderOfRotation, ViewOfTransform)`

## Description

With `get_pose_type`, the representation type of the 3D pose
*`Pose`* can be queried. See [`create_pose`](create_pose.md) for details about 3D
poses, their representation types, and the meaning of the parameters
*`OrderOfTransform`*, *`OrderOfRotation`*, and
*`ViewOfTransform`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Pose`** (input_control)  pose `→`  (real / integer)

3D pose.

Number of elements:
7

**`OrderOfTransform`** (output_control)  string `→`  (string)

Order of rotation and translation.

**`OrderOfRotation`** (output_control)  string `→`  (string)

Meaning of the rotation values.

**`ViewOfTransform`** (output_control)  string `→`  (string)

View of transformation.

## Result

[`create_pose`](create_pose.md) returns 2 (
H_MSG_TRUE)
if all parameter values are
correct. If necessary, an exception is raised.

## Possible Predecessors

`create_pose`,
`hom_mat3d_to_pose`,
`camera_calibration`,
`hand_eye_calibration`

## Possible Successors

`convert_pose_type`

## See also

`create_pose`,
`convert_pose_type`,
`write_pose`,
`read_pose`

## Module

Foundation
