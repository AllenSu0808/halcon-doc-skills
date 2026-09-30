# convert_pose_type (Operator)

## Name

`convert_pose_type` — Change the representation type of a 3D pose.

## Signature

`def convert_pose_type(pose_in: Sequence[Union[int, float]], order_of_transform: str, order_of_rotation: str, view_of_transform: str) -> Sequence[Union[int, float]]`

## Description

`convert_pose_type` converts the 3D pose *`pose_in`* into
a 3D pose *`pose_out`* with a different representation type. See
[`create_pose`](create_pose.md) for details about 3D poses, their representation
types, and the meaning of the parameters *`order_of_transform`*,
*`order_of_rotation`*, and *`view_of_transform`*.

Note that `convert_pose_type` only changes the representation of a 3D
pose, but not the rigid transformation described by the pose.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`pose_in`** (input_control)  pose `→` Sequence[Union[int, float]]

Original 3D pose.

Number of elements:
7

**`order_of_transform`** (input_control)  string `→` str

Order of rotation and translation.

Default:
"Rp+T"

Suggested values:
"Rp+T", "R(p-T)"

**`order_of_rotation`** (input_control)  string `→` str

Meaning of the rotation values.

Default:
"gba"

Suggested values:
"gba", "abg", "rodriguez"

**`view_of_transform`** (input_control)  string `→` str

View of transformation.

Default:
"point"

Suggested values:
"point", "coordinate_system"

**`pose_out`** (output_control)  pose `→` Sequence[Union[int, float]]

3D transformation.

Number of elements:
7

## Result

`convert_pose_type` returns 2 (
H_MSG_TRUE)
if all parameter values are
correct. If necessary, an exception is raised.

## Possible Predecessors

`create_pose`,
`hom_mat3d_to_pose`,
`camera_calibration`,
`hand_eye_calibration`

## Possible Successors

`write_pose`

## See also

`create_pose`,
`get_pose_type`,
`write_pose`,
`read_pose`

## Module

Foundation
