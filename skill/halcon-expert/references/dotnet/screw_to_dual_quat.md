# ScrewToDualQuat (Operator)

## Name

`ScrewToDualQuat` — Convert a screw into a dual quaternion.

## Signature

`static void HOperatorSet.ScrewToDualQuat(HTuple screwFormat, HTuple axisDirectionX, HTuple axisDirectionY, HTuple axisDirectionZ, HTuple axisMomentOrPointX, HTuple axisMomentOrPointY, HTuple axisMomentOrPointZ, HTuple rotation, HTuple translation, out HTuple dualQuaternion)`

`public HDualQuaternion(string screwFormat, HTuple axisDirectionX, HTuple axisDirectionY, HTuple axisDirectionZ, HTuple axisMomentOrPointX, HTuple axisMomentOrPointY, HTuple axisMomentOrPointZ, HTuple rotation, HTuple translation)`

`public HDualQuaternion(string screwFormat, double axisDirectionX, double axisDirectionY, double axisDirectionZ, double axisMomentOrPointX, double axisMomentOrPointY, double axisMomentOrPointZ, double rotation, double translation)`

`void HDualQuaternion.ScrewToDualQuat(string screwFormat, HTuple axisDirectionX, HTuple axisDirectionY, HTuple axisDirectionZ, HTuple axisMomentOrPointX, HTuple axisMomentOrPointY, HTuple axisMomentOrPointZ, HTuple rotation, HTuple translation)`

`void HDualQuaternion.ScrewToDualQuat(string screwFormat, double axisDirectionX, double axisDirectionY, double axisDirectionZ, double axisMomentOrPointX, double axisMomentOrPointY, double axisMomentOrPointZ, double rotation, double translation)`

## Description

The operator `ScrewToDualQuat` converts the screw parameters
to the unit dual quaternion *`dualQuaternion`*, which represents a 3D
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

If *`screwFormat`* is set to *"moment"*, these parameters
can be passed in the corresponding parameters *`axisDirectionX`*,
*`axisDirectionY`*, *`axisDirectionZ`*, *`axisMomentOrPointX`*,
*`axisMomentOrPointY`*, *`axisMomentOrPointZ`*, *`rotation`*,
and *`translation`*.

For convenience reasons, it is also possible to specify an arbitrary point
on the screw axis instead of the moment of the screw axis. For this,
*`screwFormat`* must be set to *"point"* and the
coordinates of the points must be passed in *`axisMomentOrPointX`*,
*`axisMomentOrPointY`*, and *`axisMomentOrPointZ`*.

## Attention

`ScrewToDualQuat` assumes that the direction vector of the screw
axis has length 1, i.e.,
$\sqrt{L_x^2 + L_y^2 + L_z^2} = 1$ ![figure](../assets/b3fc2a4fcd81ad01.svg).
Otherwise the returned dual quaternion is not meaningful.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`screwFormat`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Format of the screw parameters.

Default:
"moment"

List of values:
"moment", "point"

**`axisDirectionX`** (input_control)  point3d.x `→` [HTuple](HTuple.md) (*double* / int / long)

X component of the direction vector of the screw axis.

**`axisDirectionY`** (input_control)  point3d.y `→` [HTuple](HTuple.md) (*double* / int / long)

Y component of the direction vector of the screw axis.

**`axisDirectionZ`** (input_control)  point3d.z `→` [HTuple](HTuple.md) (*double* / int / long)

Z component of the direction vector of the screw axis.

**`axisMomentOrPointX`** (input_control)  point3d.x `→` [HTuple](HTuple.md) (*double* / int / long)

X component of the moment vector or a point on the
screw axis.

**`axisMomentOrPointY`** (input_control)  point3d.y `→` [HTuple](HTuple.md) (*double* / int / long)

Y component of the moment vector or a point on the
screw axis.

**`axisMomentOrPointZ`** (input_control)  point3d.z `→` [HTuple](HTuple.md) (*double* / int / long)

Z component of the moment vector or a point on the
screw axis.

**`rotation`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double* / int / long)

Rotation angle in radians.

**`translation`** (input_control)  real `→` [HTuple](HTuple.md) (*double* / int / long)

Translation.

**`dualQuaternion`** (output_control)  dual_quaternion `→` [HDualQuaternion](HDualQuaternion.md), [HTuple](HTuple.md) (*double* / int / long)

Dual quaternion.

## Possible Successors

`DualQuatCompose`,
`DualQuatConjugate`,
`DualQuatInterpolate`

## Alternatives

`PoseToDualQuat`

## See also

`DualQuatToHomMat3d`,
`PoseToDualQuat`,
`DualQuatToScrew`,
`DualQuatToPose`,
`DualQuatNormalize`,
`SerializeDualQuat`,
`DeserializeDualQuat`,
`DualQuatTransLine3d`,
`DualQuatTransPoint3d`,
`AxisAngleToQuat`

## Module

Foundation
