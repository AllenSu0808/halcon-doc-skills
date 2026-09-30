# AxisAngleToQuat (Operator)

## Name

`AxisAngleToQuat` — Create a rotation quaternion.

## Signature

`static void HOperatorSet.AxisAngleToQuat(HTuple axisX, HTuple axisY, HTuple axisZ, HTuple angle, out HTuple quaternion)`

`public HQuaternion(HTuple axisX, HTuple axisY, HTuple axisZ, HTuple angle)`

`public HQuaternion(double axisX, double axisY, double axisZ, double angle)`

`void HQuaternion.AxisAngleToQuat(HTuple axisX, HTuple axisY, HTuple axisZ, HTuple angle)`

`void HQuaternion.AxisAngleToQuat(double axisX, double axisY, double axisZ, double angle)`

## Description

Quaternions are an extension of the complex numbers. The set of quaternions
is given by $\{x_{0}+x_{1}\ast i+x_{2}\ast j+x_{3}\ast k|x_{0},x_{1},x_{2},x_{3}\in R\}$. In HALCON, quaternions are
represented by a tuple containing four elements:
$[x_{0},x_{1},x_{2},x_{3}]$.

Unit quaternions can be used to describe rotations. A quaternion is a unit
quaternion if its norm is 1. A
counterclockwise rotation around an unit vector v
(*`axisX`*, *`axisY`*,
*`axisZ`*) by an angle a (*`angle`*) can be described by
the unit quaternion q =(cos(a/2), sin(a/2) v).

The operator `AxisAngleToQuat` can be used to create such a
quaternion. To rotate a point using *`quaternion`* use the operator
[`QuatRotatePoint3d`](quat_rotate_point_3d.md).

Note that two rotations can be concatenated using the operator
[`QuatCompose`](quat_compose.md). Further, you can use a rotation quaternion to
set the orientation of the 3D plot in [`SetPaint`](set_paint.md).

## Attention

The operator `AxisAngleToQuat` does not check whether the vector
(*`axisX`*, *`axisY`*, *`axisZ`*) is of unit length (i.e. of
length 1). If this is not the case, *`quaternion`* will be no valid
rotation quaternion.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`axisX`** (input_control)  real `→` [HTuple](HTuple.md) (*double* / int / long)

X component of the rotation axis.

**`axisY`** (input_control)  real `→` [HTuple](HTuple.md) (*double* / int / long)

Y component of the rotation axis.

**`axisZ`** (input_control)  real `→` [HTuple](HTuple.md) (*double* / int / long)

Z component of the rotation axis.

**`angle`** (input_control)  real `→` [HTuple](HTuple.md) (*double* / int / long)

Rotation angle in radians.

**`quaternion`** (output_control)  quaternion `→` [HQuaternion](HQuaternion.md), [HTuple](HTuple.md) (*double* / int / long)

Rotation quaternion.

## Example (HDevelop)

```
** Normalize a vector and create a rotation quaternion
Length := sqrt(AxisX*AxisX+AxisY*AxisY+AxisZ*AxisZ)
AxisX := AxisX/Length
AxisY := AxisY/Length
AxisZ := AxisZ/Length
axis_angle_to_quat (AxisX, AxisY, AxisZ, rad(90), Quaternion)
```

## Possible Successors

`QuatToHomMat3d`,
`QuatToPose`,
`QuatRotatePoint3d`,
`QuatCompose`

## See also

`QuatNormalize`,
`QuatConjugate`,
`QuatInterpolate`,
`ScrewToDualQuat`

## Module

Foundation
