# dual_quat_to_screw (Operator)

## Name

`dual_quat_to_screw` — Convert a unit dual quaternion into a screw.

## Signature

`dual_quat_to_screw( : : DualQuaternion, ScrewFormat : AxisDirectionX, AxisDirectionY, AxisDirectionZ, AxisMomentOrPointX, AxisMomentOrPointY, AxisMomentOrPointZ, Rotation, Translation)`

## Description

The operator `dual_quat_to_screw` converts the input unit dual
quaternion *`DualQuaternion`*, which represents a 3D rigid
transformation, into the parameters of the corresponding screw.

For a brief introduction to dual quaternions, the used notation, and the
relationship between dual quaternions and screws, see
`“Solution Guide III-C - 3D Vision”`.

If *`ScrewFormat`* is set to *'moment'*, these parameters
are returned in the corresponding parameters *`AxisDirectionX`*,
*`AxisDirectionY`*, *`AxisDirectionZ`*, *`AxisMomentOrPointX`*,
*`AxisMomentOrPointY`*, *`AxisMomentOrPointZ`*, *`Rotation`*,
and *`Translation`*.

For convenience reasons, it is also possible to query the point
on the screw axis that is closest to the origin instead of the moment of the
screw axis. For this, *`ScrewFormat`* must be set to *'point'*.
In this case, the coordinates of the point are returned in
*`AxisMomentOrPointX`*, *`AxisMomentOrPointY`*, and
*`AxisMomentOrPointZ`*.

## Attention

`dual_quat_to_screw` assumes that the input *`DualQuaternion`*
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

**`DualQuaternion`** (input_control)  dual_quaternion `→`  (real)

Unit dual quaternion.

**`ScrewFormat`** (input_control)  string `→`  (string)

Format of the screw parameters.

Default:
'moment'

List of values:
'moment', 'point'

**`AxisDirectionX`** (output_control)  point3d.x `→`  (real)

X component of the direction vector of the screw axis.

**`AxisDirectionY`** (output_control)  point3d.y `→`  (real)

Y component of the direction vector of the screw axis.

**`AxisDirectionZ`** (output_control)  point3d.z `→`  (real)

Z component of the direction vector of the screw axis.

**`AxisMomentOrPointX`** (output_control)  point3d.x `→`  (real)

X component of the moment vector or a point on the
screw axis.

**`AxisMomentOrPointY`** (output_control)  point3d.y `→`  (real)

Y component of the moment vector or a point on the
screw axis.

**`AxisMomentOrPointZ`** (output_control)  point3d.z `→`  (real)

Z component of the moment vector or a point on the
screw axis.

**`Rotation`** (output_control)  angle.rad `→`  (real)

Rotation angle in radians.

**`Translation`** (output_control)  real `→`  (real)

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
