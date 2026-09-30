# DualQuatToScrew (Operator)

## Name

`DualQuatToScrew` — Convert a unit dual quaternion into a screw.

## Signature

`static void HOperatorSet.DualQuatToScrew(HTuple dualQuaternion, HTuple screwFormat, out HTuple axisDirectionX, out HTuple axisDirectionY, out HTuple axisDirectionZ, out HTuple axisMomentOrPointX, out HTuple axisMomentOrPointY, out HTuple axisMomentOrPointZ, out HTuple rotation, out HTuple translation)`

`void HDualQuaternion.DualQuatToScrew(string screwFormat, out double axisDirectionX, out double axisDirectionY, out double axisDirectionZ, out double axisMomentOrPointX, out double axisMomentOrPointY, out double axisMomentOrPointZ, out double rotation, out double translation)`

## Description

The operator `DualQuatToScrew` converts the input unit dual
quaternion *`dualQuaternion`*, which represents a 3D rigid
transformation, into the parameters of the corresponding screw.

For a brief introduction to dual quaternions, the used notation, and the
relationship between dual quaternions and screws, see
`“Solution Guide III-C - 3D Vision”`.

If *`screwFormat`* is set to *"moment"*, these parameters
are returned in the corresponding parameters *`axisDirectionX`*,
*`axisDirectionY`*, *`axisDirectionZ`*, *`axisMomentOrPointX`*,
*`axisMomentOrPointY`*, *`axisMomentOrPointZ`*, *`rotation`*,
and *`translation`*.

For convenience reasons, it is also possible to query the point
on the screw axis that is closest to the origin instead of the moment of the
screw axis. For this, *`screwFormat`* must be set to *"point"*.
In this case, the coordinates of the point are returned in
*`axisMomentOrPointX`*, *`axisMomentOrPointY`*, and
*`axisMomentOrPointZ`*.

## Attention

`DualQuatToScrew` assumes that the input *`dualQuaternion`*
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

**`dualQuaternion`** (input_control)  dual_quaternion `→` [HDualQuaternion](HDualQuaternion.md), [HTuple](HTuple.md) (*double*)

Unit dual quaternion.

**`screwFormat`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Format of the screw parameters.

Default:
"moment"

List of values:
"moment", "point"

**`axisDirectionX`** (output_control)  point3d.x `→` [HTuple](HTuple.md) (*double*)

X component of the direction vector of the screw axis.

**`axisDirectionY`** (output_control)  point3d.y `→` [HTuple](HTuple.md) (*double*)

Y component of the direction vector of the screw axis.

**`axisDirectionZ`** (output_control)  point3d.z `→` [HTuple](HTuple.md) (*double*)

Z component of the direction vector of the screw axis.

**`axisMomentOrPointX`** (output_control)  point3d.x `→` [HTuple](HTuple.md) (*double*)

X component of the moment vector or a point on the
screw axis.

**`axisMomentOrPointY`** (output_control)  point3d.y `→` [HTuple](HTuple.md) (*double*)

Y component of the moment vector or a point on the
screw axis.

**`axisMomentOrPointZ`** (output_control)  point3d.z `→` [HTuple](HTuple.md) (*double*)

Z component of the moment vector or a point on the
screw axis.

**`rotation`** (output_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Rotation angle in radians.

**`translation`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Translation.

## Possible Predecessors

`DualQuatCompose`,
`DualQuatConjugate`,
`DualQuatInterpolate`

## Alternatives

`DualQuatToPose`,
`DualQuatToHomMat3d`

## See also

`PoseToDualQuat`,
`DualQuatNormalize`,
`SerializeDualQuat`,
`DeserializeDualQuat`,
`DualQuatTransLine3d`,
`DualQuatTransPoint3d`,
`ScrewToDualQuat`

## Module

Foundation
