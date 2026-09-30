# QuatInterpolate (Operator)

## Name

`QuatInterpolate` — Interpolation of two quaternions.

## Signature

`static void HOperatorSet.QuatInterpolate(HTuple quaternionStart, HTuple quaternionEnd, HTuple interpPos, out HTuple quaternionInterpolated)`

`HQuaternion HQuaternion.QuatInterpolate(HQuaternion quaternionEnd, HTuple interpPos)`

## Description

The operator `QuatInterpolate` interpolates the two quaternions
*`quaternionStart`* and *`quaternionEnd`* at the
interpolation position *`interpPos`*. This position must lie
within the interval [0,1]. In the case of *`interpPos`*=0,
the interpolated quaternion *`quaternionInterpolated`* corresponds to
*`quaternionStart`*. In the case of *`interpPos`*=1,
the interpolated quaternion *`quaternionInterpolated`* corresponds to
*`quaternionEnd`*.

The interpolation is done using spherical linear interpolation. As a
consequence if both *`quaternionStart`* and *`quaternionEnd`* are
rotation quaternions, *`quaternionInterpolated`* will
be a rotation quaternion as well. Further, if *`interpPos`*
is increased at constant speed, a point on the unit sphere that is
rotated using *`quaternionInterpolated`* travels with constant speed on
an arc on the unit sphere.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`quaternionStart`** (input_control)  quaternion `→` [HQuaternion](HQuaternion.md), [HTuple](HTuple.md) (*double*)

Start quaternion.

**`quaternionEnd`** (input_control)  quaternion `→` [HQuaternion](HQuaternion.md), [HTuple](HTuple.md) (*double*)

End quaternion.

**`interpPos`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Interpolation parameter.

Default:
0.5

Suggested values:
0.0, 0.25, 0.5, 0.75, 1.0

**`quaternionInterpolated`** (output_control)  quaternion `→` [HQuaternion](HQuaternion.md), [HTuple](HTuple.md) (*double*)

Interpolated quaternion.

## Possible Predecessors

`AxisAngleToQuat`,
`QuatNormalize`

## Possible Successors

`QuatToHomMat3d`,
`QuatRotatePoint3d`,
`QuatToPose`

## See also

`QuatRotatePoint3d`,
`QuatConjugate`,
`QuatCompose`,
`DualQuatInterpolate`

## Module

Foundation
