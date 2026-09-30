# dual_quat_trans_point_3d (Operator)

## Name

`dual_quat_trans_point_3d` — Transform a 3D point with a unit dual quaternion.

## Signature

`def dual_quat_trans_point_3d(dual_quaternion: Sequence[Union[float, int]], px: MaybeSequence[Union[float, int]], py: MaybeSequence[Union[float, int]], pz: MaybeSequence[Union[float, int]]) -> Tuple[Sequence[float], Sequence[float], Sequence[float]]`

`def dual_quat_trans_point_3d_s(dual_quaternion: Sequence[Union[float, int]], px: MaybeSequence[Union[float, int]], py: MaybeSequence[Union[float, int]], pz: MaybeSequence[Union[float, int]]) -> Tuple[float, float, float]`

## Description

The operator `dual_quat_trans_point_3d` transforms a 3D point
(*`px`*, *`py`*, *`pz`*) by a 3D rigid
transformation that is given by the unit dual quaternion
*`dual_quaternion`* and returns the transformed 3D point in
(*`tx`*, *`ty`*, *`tz`*).

For a brief introduction to dual quaternions, see `“Solution
Guide III-C - 3D Vision”`.

## Attention

`dual_quat_trans_point_3d` returns meaningful results only if
*`dual_quaternion`* is a unit dual quaternion.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`dual_quaternion`** (input_control)  dual_quaternion `→` Sequence[Union[float, int]]

Unit dual quaternion representing the transformation.

**`px`** (input_control)  point3d.x(-array) `→` MaybeSequence[Union[float, int]]

Input point(s) (x coordinate).

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`py`** (input_control)  point3d.y(-array) `→` MaybeSequence[Union[float, int]]

Input point(s) (y coordinate).

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`pz`** (input_control)  point3d.z(-array) `→` MaybeSequence[Union[float, int]]

Input point(s) (z coordinate).

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`tx`** (output_control)  point3d.x(-array) `→` Sequence[float]

Output point(s) (x coordinate).

**`ty`** (output_control)  point3d.y(-array) `→` Sequence[float]

Output point(s) (y coordinate).

**`tz`** (output_control)  point3d.z(-array) `→` Sequence[float]

Output point(s) (z coordinate).

## Example (HDevelop)

```
* dual_quat_trans_point_3d (DualQuat, Px, Py, Pz, Tx, Ty, Tz)
* is equivalent to the following code:
dual_quat_to_hom_mat3d (DualQuat, HomMat3D)
affine_trans_point_3d (HomMat3D, Px, Py, Pz, Tx, Ty, Tz)
```

## Possible Predecessors

`dual_quat_compose`,
`pose_to_dual_quat`,
`screw_to_dual_quat`

## Alternatives

`dual_quat_to_hom_mat3d`,
`affine_trans_point_3d`

## See also

`dual_quat_to_pose`,
`dual_quat_normalize`,
`serialize_dual_quat`,
`deserialize_dual_quat`,
`quat_rotate_point_3d`,
`dual_quat_trans_line_3d`

## Module

Foundation
