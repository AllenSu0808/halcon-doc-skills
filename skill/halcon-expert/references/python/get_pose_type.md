# get_pose_type (Operator)

## Name

`get_pose_type` — Get the representation type of a 3D pose.

## Signature

`def get_pose_type(pose: Sequence[Union[int, float]]) -> Tuple[str, str, str]`

## Description

With `get_pose_type`, the representation type of the 3D pose
*`pose`* can be queried. See [`create_pose`](create_pose.md) for details about 3D
poses, their representation types, and the meaning of the parameters
*`order_of_transform`*, *`order_of_rotation`*, and
*`view_of_transform`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`pose`** (input_control)  pose `→` Sequence[Union[int, float]]

3D pose.

Number of elements:
7

**`order_of_transform`** (output_control)  string `→` str

Order of rotation and translation.

**`order_of_rotation`** (output_control)  string `→` str

Meaning of the rotation values.

**`view_of_transform`** (output_control)  string `→` str

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
