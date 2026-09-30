# quat_interpolate (Operator)

## Name

`quat_interpolate` — Interpolation of two quaternions.

## Signature

`quat_interpolate( : : QuaternionStart, QuaternionEnd, InterpPos : QuaternionInterpolated)`

## Description

The operator `quat_interpolate` interpolates the two quaternions
*`QuaternionStart`* and *`QuaternionEnd`* at the
interpolation position *`InterpPos`*. This position must lie
within the interval [0,1]. In the case of *`InterpPos`*=0,
the interpolated quaternion *`QuaternionInterpolated`* corresponds to
*`QuaternionStart`*. In the case of *`InterpPos`*=1,
the interpolated quaternion *`QuaternionInterpolated`* corresponds to
*`QuaternionEnd`*.

The interpolation is done using spherical linear interpolation. As a
consequence if both *`QuaternionStart`* and *`QuaternionEnd`* are
rotation quaternions, *`QuaternionInterpolated`* will
be a rotation quaternion as well. Further, if *`InterpPos`*
is increased at constant speed, a point on the unit sphere that is
rotated using *`QuaternionInterpolated`* travels with constant speed on
an arc on the unit sphere.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`QuaternionStart`** (input_control)  quaternion `→`  (real)

Start quaternion.

**`QuaternionEnd`** (input_control)  quaternion `→`  (real)

End quaternion.

**`InterpPos`** (input_control)  real-array `→`  (real)

Interpolation parameter.

Default:
0.5

Suggested values:
0.0, 0.25, 0.5, 0.75, 1.0

**`QuaternionInterpolated`** (output_control)  quaternion `→`  (real)

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
