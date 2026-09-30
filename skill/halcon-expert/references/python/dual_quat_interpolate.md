# dual_quat_interpolate (Operator)

## Name

`dual_quat_interpolate` — Interpolate two dual quaternions.

## Signature

`def dual_quat_interpolate(dual_quaternion_start: Sequence[float], dual_quaternion_end: Sequence[float], interp_pos: MaybeSequence[float]) -> Sequence[float]`

## Description

The operator `dual_quat_interpolate` interpolates the two dual
quaternions *`dual_quaternion_start`* and *`dual_quaternion_end`*
at the interpolation position *`interp_pos`*.

For a brief introduction to dual quaternions, the used notation, and the
relationship between dual quaternions and screws, see
`“Solution Guide III-C - 3D Vision”`.

For interpolations, the position *`interp_pos`* must lie within the
interval $[0,1]$. However, values outside this interval are also
possible, which then correspond to an extrapolation. For
*`interp_pos`*=0, the interpolated dual quaternion
*`dual_quaternion_interpolated`* corresponds to
*`dual_quaternion_start`*. For *`interp_pos`*=1, the
interpolated dual quaternion *`dual_quaternion_interpolated`* corresponds
to *`dual_quaternion_end`*.

The interpolation is performed by using screw linear interpolation (ScLERP).
If both *`dual_quaternion_start`* and *`dual_quaternion_end`* are unit
dual quaternions, *`dual_quaternion_interpolated`* will be a unit dual
quaternion as well. Hence, `dual_quat_interpolate` can be used to
smoothly interpolate between two 3D rigid transformations.

Note that the interpolation of the rotation parts of
*`dual_quaternion_start`* and *`dual_quaternion_end`* is performed
identically to the interpolation of quaternions, i.e., the screw angle
is interpolated linearly (see [`quat_interpolate`](quat_interpolate.md)). The interpolation
of the translation part is done by linearly interpolating the screw
translation.

It is possible to pass a tuple of values for *`interp_pos`*. In this
case, a tuple of interpolated *`dual_quaternion_interpolated`* is
returned, one for each value in *`interp_pos`*. This is more
efficient than calling `dual_quat_interpolate` multiple times with
a single value for *`interp_pos`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dual_quaternion_start`** (input_control)  dual_quaternion `→` Sequence[float]

Dual quaternion as the start point of the
interpolation.

**`dual_quaternion_end`** (input_control)  dual_quaternion `→` Sequence[float]

Dual quaternion as the end point of the interpolation.

**`interp_pos`** (input_control)  real(-array) `→` MaybeSequence[float]

Interpolation parameter.

Default:
0.5

Suggested values:
0.0, 0.25, 0.5, 0.75, 1.0

**`dual_quaternion_interpolated`** (output_control)  dual_quaternion(-array) `→` Sequence[float]

Interpolated dual quaternion.

## Possible Predecessors

`pose_to_dual_quat`,
`screw_to_dual_quat`,
`dual_quat_normalize`

## Possible Successors

`dual_quat_to_hom_mat3d`,
`dual_quat_to_pose`,
`dual_quat_to_screw`

## See also

`dual_quat_compose`,
`dual_quat_conjugate`,
`serialize_dual_quat`,
`deserialize_dual_quat`,
`dual_quat_trans_line_3d`,
`dual_quat_trans_point_3d`,
`quat_interpolate`

## Module

Foundation
