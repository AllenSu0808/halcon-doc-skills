# QuatCompose (Operator)

## Name

`QuatCompose` — Multiply two quaternions.

## Signature

`static void HOperatorSet.QuatCompose(HTuple quaternionLeft, HTuple quaternionRight, out HTuple quaternionComposed)`

`HQuaternion HQuaternion.QuatCompose(HQuaternion quaternionRight)`

## Description

The operator `QuatCompose` multiplies the two quaternions
*`quaternionLeft`* and *`quaternionRight`* and returns the
result in *`quaternionComposed`*.

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

**`quaternionLeft`** (input_control)  quaternion `→` [HQuaternion](HQuaternion.md), [HTuple](HTuple.md) (*double*)

Left quaternion.

**`quaternionRight`** (input_control)  quaternion `→` [HQuaternion](HQuaternion.md), [HTuple](HTuple.md) (*double*)

Right quaternion.

**`quaternionComposed`** (output_control)  quaternion `→` [HQuaternion](HQuaternion.md), [HTuple](HTuple.md) (*double*)

Product of the input quaternions.

## Possible Predecessors

`AxisAngleToQuat`

## Possible Successors

`QuatToHomMat3d`,
`QuatToPose`,
`QuatRotatePoint3d`

## See also

`AxisAngleToQuat`,
`QuatToHomMat3d`,
`QuatRotatePoint3d`,
`QuatNormalize`,
`QuatConjugate`,
`DualQuatCompose`

## Module

Foundation
