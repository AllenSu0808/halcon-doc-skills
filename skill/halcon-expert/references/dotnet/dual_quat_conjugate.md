# DualQuatConjugate (Operator)

## Name

`DualQuatConjugate` — Conjugate a dual quaternion.

## Signature

`static void HOperatorSet.DualQuatConjugate(HTuple dualQuaternion, out HTuple dualQuaternionConjugate)`

`static HDualQuaternion[] HDualQuaternion.DualQuatConjugate(HDualQuaternion[] dualQuaternion)`

`HDualQuaternion HDualQuaternion.DualQuatConjugate()`

## Description

The operator `DualQuatConjugate` computes the conjugation
*`dualQuaternionConjugate`* of the input dual quaternion
*`dualQuaternion`*.

For a brief introduction to dual quaternions, the used notation, and the
relationship between dual quaternions and screws, see
`“Solution Guide III-C - 3D Vision”`.

The conjugation of a dual quaternion
$\hat{q} = q_r + \varepsilon q_d$ ![figure](../assets/58fb67719e5d2ee1.svg) is given by $\hat{q} = \hat{q}_r + \varepsilon \hat{q}_d$ ![figure](../assets/949ad0fe69b08a79.svg), where
$\overline{q_r}$ ![figure](../assets/29e5391379772ce9.svg) and $\overline{q}_{d}$ ![figure](../assets/f62a8d44de961627.svg)
are the conjugations of the quaternions $q_{r}$ and
$q_{d}$.

For the conjugation of quaternions see [`QuatConjugate`](quat_conjugate.md).

If *`dualQuaternion`* is a unit dual quaternion and, hence, represents
a 3D rigid transformation, its inverse is its conjugate, i.e.,
$\hat{q}^{-1} = \hat{q}$ ![figure](../assets/af4670436ac2570b.svg). Consequently,
*`dualQuaternionConjugate`* represents the inverse 3D rigid
transformation of *`dualQuaternion`*. Therefore,
`DualQuatConjugate` can be used to invert a 3D rigid transformation
analogously to [`PoseInvert`](pose_invert.md) or [`HomMat3dInvert`](hom_mat3d_invert.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dualQuaternion`** (input_control)  dual_quaternion(-array) `→` [HDualQuaternion](HDualQuaternion.md), [HTuple](HTuple.md) (*double*)

Dual quaternion.

**`dualQuaternionConjugate`** (output_control)  dual_quaternion(-array) `→` [HDualQuaternion](HDualQuaternion.md), [HTuple](HTuple.md) (*double*)

Conjugate of the dual quaternion.

## Possible Predecessors

`DualQuatCompose`,
`PoseToDualQuat`,
`ScrewToDualQuat`

## Possible Successors

`DualQuatCompose`,
`DualQuatToHomMat3d`,
`DualQuatToScrew`,
`DualQuatInterpolate`,
`DualQuatToPose`

## Alternatives

`PoseInvert`,
`HomMat3dInvert`

## See also

`DualQuatNormalize`,
`SerializeDualQuat`,
`DeserializeDualQuat`,
`DualQuatTransLine3d`,
`DualQuatTransPoint3d`,
`QuatConjugate`

## Module

Foundation
