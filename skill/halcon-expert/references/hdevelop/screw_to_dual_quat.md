# screw_to_dual_quat (Operator)

## Name

`screw_to_dual_quat` — Convert a screw into a dual quaternion.

## Signature

`screw_to_dual_quat( : : ScrewFormat, AxisDirectionX, AxisDirectionY, AxisDirectionZ, AxisMomentOrPointX, AxisMomentOrPointY, AxisMomentOrPointZ, Rotation, Translation : DualQuaternion)`

## Description

The operator `screw_to_dual_quat` converts the screw parameters
to the unit dual quaternion *`DualQuaternion`*, which represents a 3D
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

If *`ScrewFormat`* is set to *'moment'*, these parameters
can be passed in the corresponding parameters *`AxisDirectionX`*,
*`AxisDirectionY`*, *`AxisDirectionZ`*, *`AxisMomentOrPointX`*,
*`AxisMomentOrPointY`*, *`AxisMomentOrPointZ`*, *`Rotation`*,
and *`Translation`*.

For convenience reasons, it is also possible to specify an arbitrary point
on the screw axis instead of the moment of the screw axis. For this,
*`ScrewFormat`* must be set to *'point'* and the
coordinates of the points must be passed in *`AxisMomentOrPointX`*,
*`AxisMomentOrPointY`*, and *`AxisMomentOrPointZ`*.

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

**`ScrewFormat`** (input_control)  string `→`  (string)

Format of the screw parameters.

Default:
'moment'

List of values:
'moment', 'point'

**`AxisDirectionX`** (input_control)  point3d.x `→`  (real / integer)

X component of the direction vector of the screw axis.

**`AxisDirectionY`** (input_control)  point3d.y `→`  (real / integer)

Y component of the direction vector of the screw axis.

**`AxisDirectionZ`** (input_control)  point3d.z `→`  (real / integer)

Z component of the direction vector of the screw axis.

**`AxisMomentOrPointX`** (input_control)  point3d.x `→`  (real / integer)

X component of the moment vector or a point on the
screw axis.

**`AxisMomentOrPointY`** (input_control)  point3d.y `→`  (real / integer)

Y component of the moment vector or a point on the
screw axis.

**`AxisMomentOrPointZ`** (input_control)  point3d.z `→`  (real / integer)

Z component of the moment vector or a point on the
screw axis.

**`Rotation`** (input_control)  angle.rad `→`  (real / integer)

Rotation angle in radians.

**`Translation`** (input_control)  real `→`  (real / integer)

Translation.

**`DualQuaternion`** (output_control)  dual_quaternion `→`  (real / integer)

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
