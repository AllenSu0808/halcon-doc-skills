# dual_quat_interpolate (Operator)

## Name

`dual_quat_interpolate` — Interpolate two dual quaternions.

## Signature

`dual_quat_interpolate( : : DualQuaternionStart, DualQuaternionEnd, InterpPos : DualQuaternionInterpolated)`

## Description

The operator `dual_quat_interpolate` interpolates the two dual
quaternions *`DualQuaternionStart`* and *`DualQuaternionEnd`*
at the interpolation position *`InterpPos`*.

For a brief introduction to dual quaternions, the used notation, and the
relationship between dual quaternions and screws, see
`“Solution Guide III-C - 3D Vision”`.

For interpolations, the position *`InterpPos`* must lie within the
interval $[0,1]$. However, values outside this interval are also
possible, which then correspond to an extrapolation. For
*`InterpPos`*=0, the interpolated dual quaternion
*`DualQuaternionInterpolated`* corresponds to
*`DualQuaternionStart`*. For *`InterpPos`*=1, the
interpolated dual quaternion *`DualQuaternionInterpolated`* corresponds
to *`DualQuaternionEnd`*.

The interpolation is performed by using screw linear interpolation (ScLERP).
If both *`DualQuaternionStart`* and *`DualQuaternionEnd`* are unit
dual quaternions, *`DualQuaternionInterpolated`* will be a unit dual
quaternion as well. Hence, `dual_quat_interpolate` can be used to
smoothly interpolate between two 3D rigid transformations.

Note that the interpolation of the rotation parts of
*`DualQuaternionStart`* and *`DualQuaternionEnd`* is performed
identically to the interpolation of quaternions, i.e., the screw angle
is interpolated linearly (see [`quat_interpolate`](quat_interpolate.md)). The interpolation
of the translation part is done by linearly interpolating the screw
translation.

It is possible to pass a tuple of values for *`InterpPos`*. In this
case, a tuple of interpolated *`DualQuaternionInterpolated`* is
returned, one for each value in *`InterpPos`*. This is more
efficient than calling `dual_quat_interpolate` multiple times with
a single value for *`InterpPos`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DualQuaternionStart`** (input_control)  dual_quaternion `→`  (real)

Dual quaternion as the start point of the
interpolation.

**`DualQuaternionEnd`** (input_control)  dual_quaternion `→`  (real)

Dual quaternion as the end point of the interpolation.

**`InterpPos`** (input_control)  real(-array) `→`  (real)

Interpolation parameter.

Default:
0.5

Suggested values:
0.0, 0.25, 0.5, 0.75, 1.0

**`DualQuaternionInterpolated`** (output_control)  dual_quaternion(-array) `→`  (real)

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
