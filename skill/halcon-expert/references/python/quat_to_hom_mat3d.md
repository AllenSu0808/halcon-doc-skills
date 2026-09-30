# quat_to_hom_mat3d (Operator)

## Name

`quat_to_hom_mat3d` — Convert a quaternion into the corresponding rotation matrix.

## Signature

`def quat_to_hom_mat3d(quaternion: Sequence[float]) -> Sequence[float]`

## Description

The operator `quat_to_hom_mat3d` converts a unit quaternion
*`quaternion`* into its corresponding rotation matrix
*`rotation_matrix`*.

The *`rotation_matrix`* for a quaternion
$x=x_{0}+x_{1}i+x_{2}j+x_{3}k$
is given by:

$$\left(\begin{array}{ccc} x_0^2 + x_1^2 - x_2^2 - x_3^2 & 2x_1x_2 - 2x_0x_3 & 2x_0x_2 + 2x_1x_3 \\ 2x_0x_3 + 2x_1x_2 & x_0^2 - x_1^2 + x_2^2 - x_3^2 & 2x_2x_3 - 2x_0x_1 \\ 2x_1x_3 - 2x_0x_2 & 2x_0x_1 + 2x_2x_3 & x_0^2 - x_1^2 - x_2^2 + x_3^2 \end{array}\right)$$ ![figure](../assets/578a92bc9b8abd3c.svg)

## Attention

*`rotation_matrix`* will only be a valid rotation matrix if
*`quaternion`* is a unit quaternion.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`quaternion`** (input_control)  quaternion `→` Sequence[float]

Rotation quaternion.

**`rotation_matrix`** (output_control)  hom_mat3d `→` Sequence[float]

Rotation matrix.

## Possible Predecessors

`axis_angle_to_quat`,
`quat_compose`

## Possible Successors

`affine_trans_point_3d`

## See also

`axis_angle_to_quat`,
`quat_rotate_point_3d`,
`quat_to_pose`,
`quat_normalize`,
`quat_conjugate`,
`quat_interpolate`

## Module

Foundation
