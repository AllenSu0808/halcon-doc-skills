# quat_compose (Operator)

## Name

`quat_compose` — Multiply two quaternions.

## Signature

`quat_compose( : : QuaternionLeft, QuaternionRight : QuaternionComposed)`

## Description

The operator `quat_compose` multiplies the two quaternions
*`QuaternionLeft`* and *`QuaternionRight`* and returns the
result in *`QuaternionComposed`*.

A quaternion $x$ is given by
$x=x_{0}+x_{1}i+x_{2}j+x_{3}k$.
In HALCON, a quaternion is represented by a four value tuple:
$[x_{0},x_{1},x_{2},x_{3}]$.

The product of two quaternions $x$ and $y$ is defined as:

$$xy = \bigl(x_0y_0 - x_1y_1 - x_2y_2 - x_3y_3\bigr) +\n\quad\bigl(x_0y_1 + x_1y_0 + x_2y_3 - x_3y_2\bigr)i +\n\quad\bigl(x_0y_2 - x_1y_3 + x_2y_0 + x_3y_1\bigr)j +\n\quad\bigl(x_0y_3 + x_1y_2 - x_2y_1 + x_3y_0\bigr)k$$ ![figure](../assets/c60dec85cbc40d20.svg)

As a consequence, the multiplication of two quaternions is not
commutative, i.e. $xy \neq yx$ ![figure](../assets/77631a5b2125e67c.svg).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`QuaternionLeft`** (input_control)  quaternion `→`  (real)

Left quaternion.

**`QuaternionRight`** (input_control)  quaternion `→`  (real)

Right quaternion.

**`QuaternionComposed`** (output_control)  quaternion `→`  (real)

Product of the input quaternions.

## Possible Predecessors

`axis_angle_to_quat`

## Possible Successors

`quat_to_hom_mat3d`,
`quat_to_pose`,
`quat_rotate_point_3d`

## See also

`axis_angle_to_quat`,
`quat_to_hom_mat3d`,
`quat_rotate_point_3d`,
`quat_normalize`,
`quat_conjugate`,
`dual_quat_compose`

## Module

Foundation
