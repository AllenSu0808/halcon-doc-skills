# dual_quat_to_screw (Operator)

## Name

`dual_quat_to_screw` — Convert a unit dual quaternion into a screw.

## Signature

`def dual_quat_to_screw(dual_quaternion: Sequence[float], screw_format: str) -> Tuple[float, float, float, float, float, float, float, float]`

## Description

The operator `dual_quat_to_screw` converts the input unit dual
quaternion *`dual_quaternion`*, which represents a 3D rigid
transformation, into the parameters of the corresponding screw.

For a brief introduction to dual quaternions, the used notation, and the
relationship between dual quaternions and screws, see
`“Solution Guide III-C - 3D Vision”`.

If *`screw_format`* is set to *"moment"*, these parameters
are returned in the corresponding parameters *`axis_direction_x`*,
*`axis_direction_y`*, *`axis_direction_z`*, *`axis_moment_or_point_x`*,
*`axis_moment_or_point_y`*, *`axis_moment_or_point_z`*, *`rotation`*,
and *`translation`*.

For convenience reasons, it is also possible to query the point
on the screw axis that is closest to the origin instead of the moment of the
screw axis. For this, *`screw_format`* must be set to *"point"*.
In this case, the coordinates of the point are returned in
*`axis_moment_or_point_x`*, *`axis_moment_or_point_y`*, and
*`axis_moment_or_point_z`*.

## Attention

`dual_quat_to_screw` assumes that the input *`dual_quaternion`*
is a unit dual quaternion, and hence represents a 3D rigid
transformation. Otherwise the returned screw parameters are not meaningful.
Further note that the screw axis for an identity transformation, i.e.,
no rotation and no translation, is undefined. In this case
$\text{L}$ is arbitrarily set to $(1,0,0)^{T}$.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dual_quaternion`** (input_control)  dual_quaternion `→` Sequence[float]

Unit dual quaternion.

**`screw_format`** (input_control)  string `→` str

Format of the screw parameters.

Default:
"moment"

List of values:
"moment", "point"

**`axis_direction_x`** (output_control)  point3d.x `→` float

X component of the direction vector of the screw axis.

**`axis_direction_y`** (output_control)  point3d.y `→` float

Y component of the direction vector of the screw axis.

**`axis_direction_z`** (output_control)  point3d.z `→` float

Z component of the direction vector of the screw axis.

**`axis_moment_or_point_x`** (output_control)  point3d.x `→` float

X component of the moment vector or a point on the
screw axis.

**`axis_moment_or_point_y`** (output_control)  point3d.y `→` float

Y component of the moment vector or a point on the
screw axis.

**`axis_moment_or_point_z`** (output_control)  point3d.z `→` float

Z component of the moment vector or a point on the
screw axis.

**`rotation`** (output_control)  angle.rad `→` float

Rotation angle in radians.

**`translation`** (output_control)  real `→` float

Translation.

## Possible Predecessors

`dual_quat_compose`,
`dual_quat_conjugate`,
`dual_quat_interpolate`

## Alternatives

`dual_quat_to_pose`,
`dual_quat_to_hom_mat3d`

## See also

`pose_to_dual_quat`,
`dual_quat_normalize`,
`serialize_dual_quat`,
`deserialize_dual_quat`,
`dual_quat_trans_line_3d`,
`dual_quat_trans_point_3d`,
`screw_to_dual_quat`

## Module

Foundation
