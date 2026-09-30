# quat_conjugate (Operator)

## Name

`quat_conjugate` — Generate the conjugation of a quaternion.

## Signature

`def quat_conjugate(quaternion: Sequence[float]) -> Sequence[float]`

## Description

The operator `quat_conjugate` generates the conjugation
*`conjugated_quaternion`* of the input quaternion *`quaternion`*.

The conjugation of a quaternion
$q=x_{0}+x_{1}i+x_{2}j+x_{3}k$
is given by $\bar{q} = x_{0} - x_{1}i - x_{2}j - x_{3}k$ ![figure](../assets/eda74a8cbaca4665.svg).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`quaternion`** (input_control)  quaternion `→` Sequence[float]

Input quaternion.

**`conjugated_quaternion`** (output_control)  quaternion `→` Sequence[float]

Conjugated quaternion.

## Possible Predecessors

`axis_angle_to_quat`

## Possible Successors

`quat_to_hom_mat3d`,
`quat_rotate_point_3d`

## See also

`axis_angle_to_quat`,
`quat_to_hom_mat3d`,
`quat_rotate_point_3d`,
`quat_normalize`,
`quat_compose`,
`quat_interpolate`,
`dual_quat_conjugate`

## Module

Foundation
