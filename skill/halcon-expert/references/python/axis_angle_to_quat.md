# axis_angle_to_quat (Operator)

## Name

`axis_angle_to_quat` — Create a rotation quaternion.

## Signature

`def axis_angle_to_quat(axis_x: Union[float, int], axis_y: Union[float, int], axis_z: Union[float, int], angle: Union[float, int]) -> Sequence[Union[float, int]]`

## Description

Quaternions are an extension of the complex numbers. The set of quaternions
is given by $\{x_{0}+x_{1}\ast i+x_{2}\ast j+x_{3}\ast k|x_{0},x_{1},x_{2},x_{3}\in R\}$. In HALCON, quaternions are
represented by a tuple containing four elements:
$[x_{0},x_{1},x_{2},x_{3}]$.

Unit quaternions can be used to describe rotations. A quaternion is a unit
quaternion if its norm is 1. A
counterclockwise rotation around an unit vector v
(*`axis_x`*, *`axis_y`*,
*`axis_z`*) by an angle a (*`angle`*) can be described by
the unit quaternion q =(cos(a/2), sin(a/2) v).

The operator `axis_angle_to_quat` can be used to create such a
quaternion. To rotate a point using *`quaternion`* use the operator
[`quat_rotate_point_3d`](quat_rotate_point_3d.md).

Note that two rotations can be concatenated using the operator
[`quat_compose`](quat_compose.md). Further, you can use a rotation quaternion to
set the orientation of the 3D plot in [`set_paint`](set_paint.md).

## Attention

The operator `axis_angle_to_quat` does not check whether the vector
(*`axis_x`*, *`axis_y`*, *`axis_z`*) is of unit length (i.e. of
length 1). If this is not the case, *`quaternion`* will be no valid
rotation quaternion.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`axis_x`** (input_control)  real `→` Union[float, int]

X component of the rotation axis.

**`axis_y`** (input_control)  real `→` Union[float, int]

Y component of the rotation axis.

**`axis_z`** (input_control)  real `→` Union[float, int]

Z component of the rotation axis.

**`angle`** (input_control)  real `→` Union[float, int]

Rotation angle in radians.

**`quaternion`** (output_control)  quaternion `→` Sequence[Union[float, int]]

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

`quat_to_hom_mat3d`,
`quat_to_pose`,
`quat_rotate_point_3d`,
`quat_compose`

## See also

`quat_normalize`,
`quat_conjugate`,
`quat_interpolate`,
`screw_to_dual_quat`

## Module

Foundation
