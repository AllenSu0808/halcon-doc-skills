# DualQuatToHomMat3d (Operator)

## Name

`DualQuatToHomMat3d` — Convert a unit dual quaternion into a homogeneous transformation matrix.

## Signature

`static void HOperatorSet.DualQuatToHomMat3d(HTuple dualQuaternion, out HTuple homMat3D)`

`HHomMat3D HDualQuaternion.DualQuatToHomMat3d()`

## Description

The operator `DualQuatToHomMat3d` converts a unit dual quaternion
*`dualQuaternion`*, which represents a 3D rigid transformation,
into its corresponding homogeneous transformation matrix *`homMat3D`*.

For a brief introduction to dual quaternions, the used notation, and the
relationship between dual quaternions and screws, see
`“Solution Guide III-C - 3D Vision”`.

The rotation part of *`homMat3D`* is computed from the
real part of the dual quaternion, as described in [`QuatToHomMat3d`](quat_to_hom_mat3d.md).
The translation part $\mathbf{T}$ of *`homMat3D`* is computed
from the real and dual part of
$\hat{q} = q_r + \varepsilon q_d$ ![figure](../assets/58fb67719e5d2ee1.svg):
$$p = q_d q_r T = \frac{2.0 v_p}{,}$$ ![figure](../assets/ba64ef0d981a111f.svg)
where $\mathbf{v}_{p}$ is the vector part of the quaternion
$p$.

## Attention

*`homMat3D`* will only be a valid rigid transformation matrix if
*`dualQuaternion`* is a unit dual quaternion.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dualQuaternion`** (input_control)  dual_quaternion `→` [HDualQuaternion](HDualQuaternion.md), [HTuple](HTuple.md) (*double*)

Unit dual quaternion.

**`homMat3D`** (output_control)  hom_mat3d `→` [HHomMat3D](HHomMat3D.md), [HTuple](HTuple.md) (*double*)

Transformation matrix.

## Possible Predecessors

`ScrewToDualQuat`,
`DualQuatInterpolate`,
`DualQuatCompose`,
`DualQuatNormalize`

## Possible Successors

`AffineTransPoint3d`

## Alternatives

`DualQuatToPose`,
`DualQuatToScrew`

## See also

`DualQuatCompose`,
`PoseToDualQuat`,
`DualQuatConjugate`,
`SerializeDualQuat`,
`DeserializeDualQuat`,
`DualQuatTransLine3d`,
`DualQuatTransPoint3d`,
`QuatToHomMat3d`

## Module

Foundation
