# screw_to_dual_quat (Operator)

## Name

`screw_to_dual_quat` — Convert a screw into a dual quaternion.

## Signature

`def screw_to_dual_quat(screw_format: str, axis_direction_x: Union[float, int], axis_direction_y: Union[float, int], axis_direction_z: Union[float, int], axis_moment_or_point_x: Union[float, int], axis_moment_or_point_y: Union[float, int], axis_moment_or_point_z: Union[float, int], rotation: Union[float, int], translation: Union[float, int]) -> Sequence[Union[float, int]]`

## Description

The operator `screw_to_dual_quat` converts the screw parameters
to the unit dual quaternion *`dual_quaternion`*, which represents a 3D
rigid transformation.

For a brief introduction to dual quaternions, the used notation, and the
relationship between dual quaternions and screws, see
`“Solution Guide III-C - 3D Vision”`.

A screw is described by the direction of the screw axis
$\mathbf{L}=(L_{x},L_{y},L_{z})^{T}$
with $\|\mathbf{L}\|=1$, the moment of the screw axis
$\mathbf{M}=(M_{x},M_{y},M_{z})^{T}$
with $\mathbf{L}\cdot\mathbf{M}=0$,
the screw angle $\theta$, and the screw translation
$d$.

If *`screw_format`* is set to *"moment"*, these parameters
can be passed in the corresponding parameters *`axis_direction_x`*,
*`axis_direction_y`*, *`axis_direction_z`*, *`axis_moment_or_point_x`*,
*`axis_moment_or_point_y`*, *`axis_moment_or_point_z`*, *`rotation`*,
and *`translation`*.

For convenience reasons, it is also possible to specify an arbitrary point
on the screw axis instead of the moment of the screw axis. For this,
*`screw_format`* must be set to *"point"* and the
coordinates of the points must be passed in *`axis_moment_or_point_x`*,
*`axis_moment_or_point_y`*, and *`axis_moment_or_point_z`*.

## Attention

`screw_to_dual_quat` assumes that the direction vector of the screw
axis has length 1, i.e.,
$\sqrt{L_x^2 + L_y^2 + L_z^2} = 1$ ![figure](../assets/b3fc2a4fcd81ad01.svg).
Otherwise the returned dual quaternion is not meaningful.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`screw_format`** (input_control)  string `→` str

Format of the screw parameters.

Default:
"moment"

List of values:
"moment", "point"

**`axis_direction_x`** (input_control)  point3d.x `→` Union[float, int]

X component of the direction vector of the screw axis.

**`axis_direction_y`** (input_control)  point3d.y `→` Union[float, int]

Y component of the direction vector of the screw axis.

**`axis_direction_z`** (input_control)  point3d.z `→` Union[float, int]

Z component of the direction vector of the screw axis.

**`axis_moment_or_point_x`** (input_control)  point3d.x `→` Union[float, int]

X component of the moment vector or a point on the
screw axis.

**`axis_moment_or_point_y`** (input_control)  point3d.y `→` Union[float, int]

Y component of the moment vector or a point on the
screw axis.

**`axis_moment_or_point_z`** (input_control)  point3d.z `→` Union[float, int]

Z component of the moment vector or a point on the
screw axis.

**`rotation`** (input_control)  angle.rad `→` Union[float, int]

Rotation angle in radians.

**`translation`** (input_control)  real `→` Union[float, int]

Translation.

**`dual_quaternion`** (output_control)  dual_quaternion `→` Sequence[Union[float, int]]

Dual quaternion.

## Possible Successors

`dual_quat_compose`,
`dual_quat_conjugate`,
`dual_quat_interpolate`

## Alternatives

`pose_to_dual_quat`

## See also

`dual_quat_to_hom_mat3d`,
`pose_to_dual_quat`,
`dual_quat_to_screw`,
`dual_quat_to_pose`,
`dual_quat_normalize`,
`serialize_dual_quat`,
`deserialize_dual_quat`,
`dual_quat_trans_line_3d`,
`dual_quat_trans_point_3d`,
`axis_angle_to_quat`

## Module

Foundation
