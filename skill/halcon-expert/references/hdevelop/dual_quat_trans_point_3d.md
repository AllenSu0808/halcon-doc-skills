# dual_quat_trans_point_3d (Operator)

## Name

`dual_quat_trans_point_3d` — Transform a 3D point with a unit dual quaternion.

## Signature

`dual_quat_trans_point_3d( : : DualQuaternion, Px, Py, Pz : Tx, Ty, Tz)`

## Description

The operator `dual_quat_trans_point_3d` transforms a 3D point
(*`Px`*, *`Py`*, *`Pz`*) by a 3D rigid
transformation that is given by the unit dual quaternion
*`DualQuaternion`* and returns the transformed 3D point in
(*`Tx`*, *`Ty`*, *`Tz`*).

For a brief introduction to dual quaternions, see `“Solution
Guide III-C - 3D Vision”`.

## Attention

`dual_quat_trans_point_3d` returns meaningful results only if
*`DualQuaternion`* is a unit dual quaternion.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`DualQuaternion`** (input_control)  dual_quaternion `→`  (real / integer)

Unit dual quaternion representing the transformation.

**`Px`** (input_control)  point3d.x(-array) `→`  (real / integer)

Input point(s) (x coordinate).

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`Py`** (input_control)  point3d.y(-array) `→`  (real / integer)

Input point(s) (y coordinate).

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`Pz`** (input_control)  point3d.z(-array) `→`  (real / integer)

Input point(s) (z coordinate).

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`Tx`** (output_control)  point3d.x(-array) `→`  (real)

Output point(s) (x coordinate).

**`Ty`** (output_control)  point3d.y(-array) `→`  (real)

Output point(s) (y coordinate).

**`Tz`** (output_control)  point3d.z(-array) `→`  (real)

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
