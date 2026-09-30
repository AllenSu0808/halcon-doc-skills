# convert_pose_type (Operator)

## Name

`convert_pose_type` — Change the representation type of a 3D pose.

## Signature

`convert_pose_type( : : PoseIn, OrderOfTransform, OrderOfRotation, ViewOfTransform : PoseOut)`

## Description

`convert_pose_type` converts the 3D pose *`PoseIn`* into
a 3D pose *`PoseOut`* with a different representation type. See
[`create_pose`](create_pose.md) for details about 3D poses, their representation
types, and the meaning of the parameters *`OrderOfTransform`*,
*`OrderOfRotation`*, and *`ViewOfTransform`*.

Note that `convert_pose_type` only changes the representation of a 3D
pose, but not the rigid transformation described by the pose.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`PoseIn`** (input_control)  pose `→`  (real / integer)

Original 3D pose.

Number of elements:
7

**`OrderOfTransform`** (input_control)  string `→`  (string)

Order of rotation and translation.

Default:
'Rp+T'

Suggested values:
'Rp+T', 'R(p-T)'

**`OrderOfRotation`** (input_control)  string `→`  (string)

Meaning of the rotation values.

Default:
'gba'

Suggested values:
'gba', 'abg', 'rodriguez'

**`ViewOfTransform`** (input_control)  string `→`  (string)

View of transformation.

Default:
'point'

Suggested values:
'point', 'coordinate_system'

**`PoseOut`** (output_control)  pose `→`  (real / integer)

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
