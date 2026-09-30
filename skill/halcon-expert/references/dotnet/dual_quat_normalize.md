# DualQuatNormalize (Operator)

## Name

`DualQuatNormalize` — Normalize a dual quaternion.

## Signature

`static void HOperatorSet.DualQuatNormalize(HTuple dualQuaternion, out HTuple dualQuaternionNormalized)`

`static HDualQuaternion[] HDualQuaternion.DualQuatNormalize(HDualQuaternion[] dualQuaternion)`

`HDualQuaternion HDualQuaternion.DualQuatNormalize()`

## Description

The operator `DualQuatNormalize` normalizes the input dual
quaternion *`dualQuaternion`* and returns the normalized dual
quaternion, which is also called a unit dual quaternion,
in *`dualQuaternionNormalized`*.

For a brief introduction to dual quaternions, the used notation, and the
relationship between dual quaternions and screws, see
`“Solution Guide III-C - 3D Vision”`.

The norm of a unit dual quaternion
$\hat{q} = q_r + \varepsilon q_d$ ![figure](../assets/58fb67719e5d2ee1.svg)
is 1, i.e., $\hat{q}\hat{q}=1$ ![figure](../assets/d8667844b46f184e.svg). This is
equivalent to the following two conditions:
$$\|q_r\|\, = \\bar{q}_r \\bar{q}_r = 1 \\\nq_r \bar{q}_d + \bar{q}_r q_d = 0$$ ![figure](../assets/a011c9e8e1545972.svg)
where $\overline{q}$ ![figure](../assets/c62a28b14aa80af0.svg) represents the conjugate quaternion of
$q$ (see [`QuatConjugate`](quat_conjugate.md)).

A 3D rigid transformation can be represented by a unit dual quaternion.

## Attention

If the norm of the real part of *`dualQuaternion`* is 0,
`DualQuatNormalize` returns the error code 9310 (H_ERR_DQ_ZERO_NORM)
because in this case no normalization is possible.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dualQuaternion`** (input_control)  dual_quaternion(-array) `→` [HDualQuaternion](HDualQuaternion.md), [HTuple](HTuple.md) (*double*)

Unit dual quaternion.

**`dualQuaternionNormalized`** (output_control)  dual_quaternion(-array) `→` [HDualQuaternion](HDualQuaternion.md), [HTuple](HTuple.md) (*double*)

Normalized dual quaternion.

## Possible Predecessors

`DualQuatCompose`

## Possible Successors

`DualQuatToHomMat3d`

## See also

`DualQuatInterpolate`,
`PoseToDualQuat`,
`ScrewToDualQuat`,
`DualQuatToScrew`,
`DualQuatToPose`,
`DualQuatConjugate`,
`SerializeDualQuat`,
`DeserializeDualQuat`,
`DualQuatTransLine3d`,
`DualQuatTransPoint3d`,
`QuatNormalize`

## Module

Foundation
