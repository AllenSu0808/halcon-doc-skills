# DualQuatCompose (Operator)

## Name

`DualQuatCompose` — Multiply two dual quaternions.

## Signature

`static void HOperatorSet.DualQuatCompose(HTuple dualQuaternionLeft, HTuple dualQuaternionRight, out HTuple dualQuaternionComposed)`

`static HDualQuaternion[] HDualQuaternion.DualQuatCompose(HDualQuaternion[] dualQuaternionLeft, HDualQuaternion[] dualQuaternionRight)`

`HDualQuaternion HDualQuaternion.DualQuatCompose(HDualQuaternion dualQuaternionRight)`

## Description

The operator `DualQuatCompose` multiplies the two dual quaternions
*`dualQuaternionLeft`* and *`dualQuaternionRight`* and returns the
product in *`dualQuaternionComposed`*.

For a brief introduction to dual quaternions, the used notation, and the
relationship between dual quaternions and screws, see
`“Solution Guide III-C - 3D Vision”`.

The multiplication of the dual quaternions $\hat{p}$ ![figure](../assets/c802e896b3d639bf.svg) and
$\hat{q}$ ![figure](../assets/2e9ecba020103681.svg) is $\hat{p}\hat{q} = p_r q_r + \epsilon(p_r q_d + p_d q_r)$ ![figure](../assets/05b34277bfdd45a7.svg).

For the multiplication of quaternions see [`QuatCompose`](quat_compose.md).

Note that the multiplication of two dual quaternions is not commutative,
i.e., $\hat{p}\hat{q} \neq \hat{q}\hat{p}$ ![figure](../assets/1cb2b8f39d3a0a80.svg).

If *`dualQuaternionLeft`* and *`dualQuaternionRight`* are unit
dual quaternions and, hence, represent 3D rigid transformations, their
multiplication corresponds to the multiplication of their corresponding
homogeneous transformation matrices. Consequently, `DualQuatCompose`
can be used to concatenate two 3D rigid transformations analogously to
[`PoseCompose`](pose_compose.md) or [`HomMat3dCompose`](hom_mat3d_compose.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dualQuaternionLeft`** (input_control)  dual_quaternion(-array) `→` [HDualQuaternion](HDualQuaternion.md), [HTuple](HTuple.md) (*double*)

Left dual quaternion.

**`dualQuaternionRight`** (input_control)  dual_quaternion(-array) `→` [HDualQuaternion](HDualQuaternion.md), [HTuple](HTuple.md) (*double*)

Right dual quaternion.

**`dualQuaternionComposed`** (output_control)  dual_quaternion(-array) `→` [HDualQuaternion](HDualQuaternion.md), [HTuple](HTuple.md) (*double*)

Product of the dual quaternions.

## Possible Predecessors

`ScrewToDualQuat`

## Possible Successors

`DualQuatToHomMat3d`,
`DualQuatToPose`,
`DualQuatToScrew`

## Alternatives

`PoseCompose`,
`HomMat3dCompose`

## See also

`DualQuatInterpolate`,
`PoseToDualQuat`,
`DualQuatNormalize`,
`DualQuatConjugate`,
`SerializeDualQuat`,
`DeserializeDualQuat`,
`DualQuatTransLine3d`,
`DualQuatTransPoint3d`,
`QuatCompose`

## Module

Foundation
