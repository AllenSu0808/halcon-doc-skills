# quat_interpolate (Operator)

## Name

`quat_interpolate` — Interpolation of two quaternions.

## Signature

`def quat_interpolate(quaternion_start: Sequence[float], quaternion_end: Sequence[float], interp_pos: Sequence[float]) -> Sequence[float]`

## Description

The operator `quat_interpolate` interpolates the two quaternions
*`quaternion_start`* and *`quaternion_end`* at the
interpolation position *`interp_pos`*. This position must lie
within the interval [0,1]. In the case of *`interp_pos`*=0,
the interpolated quaternion *`quaternion_interpolated`* corresponds to
*`quaternion_start`*. In the case of *`interp_pos`*=1,
the interpolated quaternion *`quaternion_interpolated`* corresponds to
*`quaternion_end`*.

The interpolation is done using spherical linear interpolation. As a
consequence if both *`quaternion_start`* and *`quaternion_end`* are
rotation quaternions, *`quaternion_interpolated`* will
be a rotation quaternion as well. Further, if *`interp_pos`*
is increased at constant speed, a point on the unit sphere that is
rotated using *`quaternion_interpolated`* travels with constant speed on
an arc on the unit sphere.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`quaternion_start`** (input_control)  quaternion `→` Sequence[float]

Start quaternion.

**`quaternion_end`** (input_control)  quaternion `→` Sequence[float]

End quaternion.

**`interp_pos`** (input_control)  real-array `→` Sequence[float]

Interpolation parameter.

Default:
0.5

Suggested values:
0.0, 0.25, 0.5, 0.75, 1.0

**`quaternion_interpolated`** (output_control)  quaternion `→` Sequence[float]

Interpolated quaternion.

## Possible Predecessors

`axis_angle_to_quat`,
`quat_normalize`

## Possible Successors

`quat_to_hom_mat3d`,
`quat_rotate_point_3d`,
`quat_to_pose`

## See also

`quat_rotate_point_3d`,
`quat_conjugate`,
`quat_compose`,
`dual_quat_interpolate`

## Module

Foundation
