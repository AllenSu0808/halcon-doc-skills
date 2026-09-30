# DualQuatInterpolate (Operator)

## Name

`DualQuatInterpolate` — Interpolate two dual quaternions.

## Signature

`static void HOperatorSet.DualQuatInterpolate(HTuple dualQuaternionStart, HTuple dualQuaternionEnd, HTuple interpPos, out HTuple dualQuaternionInterpolated)`

`HDualQuaternion[] HDualQuaternion.DualQuatInterpolate(HDualQuaternion dualQuaternionEnd, HTuple interpPos)`

`HDualQuaternion HDualQuaternion.DualQuatInterpolate(HDualQuaternion dualQuaternionEnd, double interpPos)`

## Description

The operator `DualQuatInterpolate` interpolates the two dual
quaternions *`dualQuaternionStart`* and *`dualQuaternionEnd`*
at the interpolation position *`interpPos`*.

For a brief introduction to dual quaternions, the used notation, and the
relationship between dual quaternions and screws, see
`“Solution Guide III-C - 3D Vision”`.

For interpolations, the position *`interpPos`* must lie within the
interval $[0,1]$. However, values outside this interval are also
possible, which then correspond to an extrapolation. For
*`interpPos`*=0, the interpolated dual quaternion
*`dualQuaternionInterpolated`* corresponds to
*`dualQuaternionStart`*. For *`interpPos`*=1, the
interpolated dual quaternion *`dualQuaternionInterpolated`* corresponds
to *`dualQuaternionEnd`*.

The interpolation is performed by using screw linear interpolation (ScLERP).
If both *`dualQuaternionStart`* and *`dualQuaternionEnd`* are unit
dual quaternions, *`dualQuaternionInterpolated`* will be a unit dual
quaternion as well. Hence, `DualQuatInterpolate` can be used to
smoothly interpolate between two 3D rigid transformations.

Note that the interpolation of the rotation parts of
*`dualQuaternionStart`* and *`dualQuaternionEnd`* is performed
identically to the interpolation of quaternions, i.e., the screw angle
is interpolated linearly (see [`QuatInterpolate`](quat_interpolate.md)). The interpolation
of the translation part is done by linearly interpolating the screw
translation.

It is possible to pass a tuple of values for *`interpPos`*. In this
case, a tuple of interpolated *`dualQuaternionInterpolated`* is
returned, one for each value in *`interpPos`*. This is more
efficient than calling `DualQuatInterpolate` multiple times with
a single value for *`interpPos`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dualQuaternionStart`** (input_control)  dual_quaternion `→` [HDualQuaternion](HDualQuaternion.md), [HTuple](HTuple.md) (*double*)

Dual quaternion as the start point of the
interpolation.

**`dualQuaternionEnd`** (input_control)  dual_quaternion `→` [HDualQuaternion](HDualQuaternion.md), [HTuple](HTuple.md) (*double*)

Dual quaternion as the end point of the interpolation.

**`interpPos`** (input_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Interpolation parameter.

Default:
0.5

Suggested values:
0.0, 0.25, 0.5, 0.75, 1.0

**`dualQuaternionInterpolated`** (output_control)  dual_quaternion(-array) `→` [HDualQuaternion](HDualQuaternion.md), [HTuple](HTuple.md) (*double*)

Interpolated dual quaternion.

## Possible Predecessors

`PoseToDualQuat`,
`ScrewToDualQuat`,
`DualQuatNormalize`

## Possible Successors

`DualQuatToHomMat3d`,
`DualQuatToPose`,
`DualQuatToScrew`

## See also

`DualQuatCompose`,
`DualQuatConjugate`,
`SerializeDualQuat`,
`DeserializeDualQuat`,
`DualQuatTransLine3d`,
`DualQuatTransPoint3d`,
`QuatInterpolate`

## Module

Foundation
