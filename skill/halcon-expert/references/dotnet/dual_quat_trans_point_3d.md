# DualQuatTransPoint3d (Operator)

## Name

`DualQuatTransPoint3d` — Transform a 3D point with a unit dual quaternion.

## Signature

`static void HOperatorSet.DualQuatTransPoint3d(HTuple dualQuaternion, HTuple px, HTuple py, HTuple pz, out HTuple tx, out HTuple ty, out HTuple tz)`

`HTuple HDualQuaternion.DualQuatTransPoint3d(HTuple px, HTuple py, HTuple pz, out HTuple ty, out HTuple tz)`

`double HDualQuaternion.DualQuatTransPoint3d(double px, double py, double pz, out double ty, out double tz)`

## Description

The operator `DualQuatTransPoint3d` transforms a 3D point
(*`px`*, *`py`*, *`pz`*) by a 3D rigid
transformation that is given by the unit dual quaternion
*`dualQuaternion`* and returns the transformed 3D point in
(*`tx`*, *`ty`*, *`tz`*).

For a brief introduction to dual quaternions, see `“Solution
Guide III-C - 3D Vision”`.

## Attention

`DualQuatTransPoint3d` returns meaningful results only if
*`dualQuaternion`* is a unit dual quaternion.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`dualQuaternion`** (input_control)  dual_quaternion `→` [HDualQuaternion](HDualQuaternion.md), [HTuple](HTuple.md) (*double* / int / long)

Unit dual quaternion representing the transformation.

**`px`** (input_control)  point3d.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input point(s) (x coordinate).

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`py`** (input_control)  point3d.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input point(s) (y coordinate).

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`pz`** (input_control)  point3d.z(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input point(s) (z coordinate).

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`tx`** (output_control)  point3d.x(-array) `→` [HTuple](HTuple.md) (*double*)

Output point(s) (x coordinate).

**`ty`** (output_control)  point3d.y(-array) `→` [HTuple](HTuple.md) (*double*)

Output point(s) (y coordinate).

**`tz`** (output_control)  point3d.z(-array) `→` [HTuple](HTuple.md) (*double*)

Output point(s) (z coordinate).

## Example (HDevelop)

```
* dual_quat_trans_point_3d (DualQuat, Px, Py, Pz, Tx, Ty, Tz)
* is equivalent to the following code:
dual_quat_to_hom_mat3d (DualQuat, HomMat3D)
affine_trans_point_3d (HomMat3D, Px, Py, Pz, Tx, Ty, Tz)
```

## Possible Predecessors

`DualQuatCompose`,
`PoseToDualQuat`,
`ScrewToDualQuat`

## Alternatives

`DualQuatToHomMat3d`,
`AffineTransPoint3d`

## See also

`DualQuatToPose`,
`DualQuatNormalize`,
`SerializeDualQuat`,
`DeserializeDualQuat`,
`QuatRotatePoint3d`,
`DualQuatTransLine3d`

## Module

Foundation
