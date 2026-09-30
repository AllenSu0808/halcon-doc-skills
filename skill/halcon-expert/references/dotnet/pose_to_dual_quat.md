# PoseToDualQuat (Operator)

## Name

`PoseToDualQuat` — Convert a 3D pose to a unit dual quaternion.

## Signature

`static void HOperatorSet.PoseToDualQuat(HTuple pose, out HTuple dualQuaternion)`

`public HDualQuaternion(HPose pose)`

`static HDualQuaternion[] HDualQuaternion.PoseToDualQuat(HPose[] pose)`

`void HDualQuaternion.PoseToDualQuat(HPose pose)`

## Description

The operator `PoseToDualQuat` converts the input *`pose`*
into its corresponding unit dual quaternion *`dualQuaternion`*.

For a brief introduction to dual quaternions, the used notation, and the
relationship between dual quaternions and screws, see
`“Solution Guide III-C - 3D Vision”`.

Because $\hat{q}$ ![figure](../assets/2e9ecba020103681.svg) and $-\hat{q}$ ![figure](../assets/eeef33b74ca60093.svg) represent the same rigid
transformation, the sign of the resulting dual quaternion
*`dualQuaternion`* is chosen such that the scalar part of the real
part is $\ge0$.

Multiple poses can be passed in *`pose`*, in which case a unit dual
quaternion is returned for each of them.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`pose`** (input_control)  pose(-array) `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

3D pose.

**`dualQuaternion`** (output_control)  dual_quaternion(-array) `→` [HDualQuaternion](HDualQuaternion.md), [HTuple](HTuple.md) (*double*)

Unit dual quaternion.

## Possible Predecessors

`CreatePose`,
`ReadPose`

## Possible Successors

`DualQuatCompose`,
`DualQuatInterpolate`,
`DualQuatToScrew`,
`DualQuatConjugate`

## Alternatives

`PoseToHomMat3d`,
`ScrewToDualQuat`

## See also

`DualQuatToHomMat3d`,
`DualQuatToPose`,
`DualQuatNormalize`,
`SerializeDualQuat`,
`DeserializeDualQuat`,
`DualQuatTransLine3d`,
`DualQuatTransPoint3d`,
`PoseToQuat`

## Module

Foundation
