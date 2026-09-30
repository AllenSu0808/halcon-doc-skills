# QuatToHomMat3d (Operator)

## Name

`QuatToHomMat3d` — Convert a quaternion into the corresponding rotation matrix.

## Signature

`static void HOperatorSet.QuatToHomMat3d(HTuple quaternion, out HTuple rotationMatrix)`

`HHomMat3D HQuaternion.QuatToHomMat3d()`

## Description

The operator `QuatToHomMat3d` converts a unit quaternion
*`quaternion`* into its corresponding rotation matrix
*`rotationMatrix`*.

The *`rotationMatrix`* for a quaternion
$x=x_{0}+x_{1}i+x_{2}j+x_{3}k$
is given by:

$$\left(\begin{array}{ccc} x_0^2 + x_1^2 - x_2^2 - x_3^2 & 2x_1x_2 - 2x_0x_3 & 2x_0x_2 + 2x_1x_3 \\ 2x_0x_3 + 2x_1x_2 & x_0^2 - x_1^2 + x_2^2 - x_3^2 & 2x_2x_3 - 2x_0x_1 \\ 2x_1x_3 - 2x_0x_2 & 2x_0x_1 + 2x_2x_3 & x_0^2 - x_1^2 - x_2^2 + x_3^2 \end{array}\right)$$ ![figure](../assets/578a92bc9b8abd3c.svg)

## Attention

*`rotationMatrix`* will only be a valid rotation matrix if
*`quaternion`* is a unit quaternion.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`quaternion`** (input_control)  quaternion `→` [HQuaternion](HQuaternion.md), [HTuple](HTuple.md) (*double*)

Rotation quaternion.

**`rotationMatrix`** (output_control)  hom_mat3d `→` [HHomMat3D](HHomMat3D.md), [HTuple](HTuple.md) (*double*)

Rotation matrix.

## Possible Predecessors

`AxisAngleToQuat`,
`QuatCompose`

## Possible Successors

`AffineTransPoint3d`

## See also

`AxisAngleToQuat`,
`QuatRotatePoint3d`,
`QuatToPose`,
`QuatNormalize`,
`QuatConjugate`,
`QuatInterpolate`

## Module

Foundation
