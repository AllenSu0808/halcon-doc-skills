# quat_normalize (Operator)

## Name

`quat_normalize` — Normalize a quaternion.

## Signature

`def quat_normalize(quaternion: Sequence[float]) -> Sequence[float]`

## Description

The operator `quat_normalize` scales the input quaternion
*`quaternion`* such that its norm is 1. The result is returned
in *`normalized_quaternion`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`quaternion`** (input_control)  quaternion `→` Sequence[float]

Input quaternion.

**`normalized_quaternion`** (output_control)  quaternion `→` Sequence[float]

Normalized quaternion.

## Possible Predecessors

`axis_angle_to_quat`

## Possible Successors

`quat_to_hom_mat3d`,
`quat_rotate_point_3d`

## See also

`axis_angle_to_quat`,
`quat_interpolate`,
`quat_compose`,
`quat_conjugate`,
`dual_quat_to_hom_mat3d`

## Module

Foundation
