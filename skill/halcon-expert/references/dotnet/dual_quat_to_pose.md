# DualQuatToPose (Operator)

## Name

`DualQuatToPose` — Convert a dual quaternion to a 3D pose.

## Signature

`static void HOperatorSet.DualQuatToPose(HTuple dualQuaternion, out HTuple pose)`

`static HPose[] HDualQuaternion.DualQuatToPose(HDualQuaternion[] dualQuaternion)`

`HPose HDualQuaternion.DualQuatToPose()`

## Description

The operator `DualQuatToPose` converts the input
*`dualQuaternion`* into its corresponding 3D *`pose`*.

For a brief introduction to dual quaternions, the used notation, and the
relationship between dual quaternions and screws, see
`“Solution Guide III-C - 3D Vision”`.

Multiple dual quaternions can be passed in *`dualQuaternion`*, in which
case a pose is returned for each of them.

## Attention

`DualQuatToPose` assumes that the input *`dualQuaternion`*
is a unit dual quaternion, and hence represents a 3D rigid
transformation. Otherwise the returned pose is not meaningful.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dualQuaternion`** (input_control)  dual_quaternion(-array) `→` [HDualQuaternion](HDualQuaternion.md), [HTuple](HTuple.md) (*double*)

Unit dual quaternion.

**`pose`** (output_control)  pose(-array) `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

3D pose.

## Possible Predecessors

`DualQuatCompose`,
`DualQuatInterpolate`,
`ScrewToDualQuat`,
`DualQuatConjugate`

## Possible Successors

`CameraCalibration`,
`HandEyeCalibration`,
`WritePose`,
`DispCaltab`,
`SimCaltab`

## Alternatives

`DualQuatToScrew`,
`DualQuatToHomMat3d`

## See also

`PoseToDualQuat`,
`DualQuatNormalize`,
`SerializeDualQuat`,
`DeserializeDualQuat`,
`DualQuatTransLine3d`,
`DualQuatTransPoint3d`,
`QuatToPose`

## Module

Foundation
