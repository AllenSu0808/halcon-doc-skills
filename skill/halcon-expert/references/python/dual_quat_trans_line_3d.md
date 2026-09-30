# dual_quat_trans_line_3d (Operator)

## Name

`dual_quat_trans_line_3d` — Transform a 3D line with a unit dual quaternion.

## Signature

`def dual_quat_trans_line_3d(dual_quaternion: Sequence[Union[float, int]], line_format: str, line_direction_x: MaybeSequence[Union[float, int]], line_direction_y: MaybeSequence[Union[float, int]], line_direction_z: MaybeSequence[Union[float, int]], line_moment_or_point_x: MaybeSequence[Union[float, int]], line_moment_or_point_y: MaybeSequence[Union[float, int]], line_moment_or_point_z: MaybeSequence[Union[float, int]]) -> Tuple[Sequence[Union[float, int]], Sequence[Union[float, int]], Sequence[Union[float, int]], Sequence[Union[float, int]], Sequence[Union[float, int]], Sequence[Union[float, int]]]`

`def dual_quat_trans_line_3d_s(dual_quaternion: Sequence[Union[float, int]], line_format: str, line_direction_x: MaybeSequence[Union[float, int]], line_direction_y: MaybeSequence[Union[float, int]], line_direction_z: MaybeSequence[Union[float, int]], line_moment_or_point_x: MaybeSequence[Union[float, int]], line_moment_or_point_y: MaybeSequence[Union[float, int]], line_moment_or_point_z: MaybeSequence[Union[float, int]]) -> Tuple[Union[float, int], Union[float, int], Union[float, int], Union[float, int], Union[float, int], Union[float, int]]`

## Description

The operator `dual_quat_trans_line_3d` transforms a 3D line that
is represented by its Plücker coordinates by a 3D rigid transformation that
is given by the unit dual quaternion *`dual_quaternion`*.

For a brief introduction to dual quaternions, Plücker coordinates and the
used notation, see `“Solution Guide III-C - 3D Vision”`.

If *`line_format`* is set to *"moment"*, the moment of
the line must be passed in *`line_moment_or_point_x`*,
*`line_moment_or_point_y`*, and *`line_moment_or_point_z`*.

If *`line_format`* is set to *"point"*, instead of the moment
an arbitrary point on the line can be passed in *`line_moment_or_point_x`*,
*`line_moment_or_point_y`*, and *`line_moment_or_point_z`*.

The parameters of the transformed line are returned in
*`trans_line_direction_x`*, *`trans_line_direction_y`*,
*`trans_line_direction_z`*, *`trans_line_moment_or_point_x`*,
*`trans_line_moment_or_point_y`*, and *`trans_line_moment_or_point_z`* in the
format that was specified in *`line_format`*.
If *`line_format`* is set to *"point"*, the point on the line
that is closest to the origin of the coordinate system is returned.

## Attention

`dual_quat_trans_line_3d` returns meaningful results only if
*`dual_quaternion`* is a unit dual quaternion and the length of
the line direction is 1.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dual_quaternion`** (input_control)  dual_quaternion `→` Sequence[Union[float, int]]

Unit dual quaternion representing the transformation.

**`line_format`** (input_control)  string `→` str

Format of the line parameters.

Default:
"moment"

List of values:
"moment", "point"

**`line_direction_x`** (input_control)  point3d.x(-array) `→` MaybeSequence[Union[float, int]]

X component of the direction vector of the line.

**`line_direction_y`** (input_control)  point3d.y(-array) `→` MaybeSequence[Union[float, int]]

Y component of the direction vector of the line.

**`line_direction_z`** (input_control)  point3d.z(-array) `→` MaybeSequence[Union[float, int]]

Z component of the direction vector of the line.

**`line_moment_or_point_x`** (input_control)  point3d.x(-array) `→` MaybeSequence[Union[float, int]]

X component of the moment vector or a point on the line.

**`line_moment_or_point_y`** (input_control)  point3d.y(-array) `→` MaybeSequence[Union[float, int]]

Y component of the moment vector or a point on the line.

**`line_moment_or_point_z`** (input_control)  point3d.z(-array) `→` MaybeSequence[Union[float, int]]

Z component of the moment vector or a point on the line.

**`trans_line_direction_x`** (output_control)  point3d.x(-array) `→` Sequence[Union[float, int]]

X component of the direction vector of the
transformed line.

**`trans_line_direction_y`** (output_control)  point3d.y(-array) `→` Sequence[Union[float, int]]

Y component of the direction vector of the
transformed line.

**`trans_line_direction_z`** (output_control)  point3d.z(-array) `→` Sequence[Union[float, int]]

Z component of the direction vector of the
transformed line.

**`trans_line_moment_or_point_x`** (output_control)  point3d.x(-array) `→` Sequence[Union[float, int]]

X component of the moment vector or a point on the
transformed line.

**`trans_line_moment_or_point_y`** (output_control)  point3d.y(-array) `→` Sequence[Union[float, int]]

Y component of the moment vector or a point on the
transformed line.

**`trans_line_moment_or_point_z`** (output_control)  point3d.z(-array) `→` Sequence[Union[float, int]]

Z component of the moment vector or a point on the
transformed line.

## Possible Predecessors

`points_to_pluecker_line`,
`point_direction_to_pluecker_line`

## Possible Successors

`dual_quat_compose`,
`dual_quat_conjugate`,
`pose_to_dual_quat`

## Alternatives

`affine_trans_point_3d`,
`dual_quat_trans_point_3d`

## See also

`dual_quat_to_hom_mat3d`,
`dual_quat_to_screw`,
`dual_quat_to_pose`,
`dual_quat_normalize`,
`serialize_dual_quat`,
`deserialize_dual_quat`,
`quat_rotate_point_3d`

## Module

Foundation
