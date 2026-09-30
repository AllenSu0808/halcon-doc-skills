# QuatToPose (Operator)

## Name

`QuatToPose` — Convert a quaternion into the corresponding 3D pose.

## Signature

`static void HOperatorSet.QuatToPose(HTuple quaternion, out HTuple pose)`

`HPose HQuaternion.QuatToPose()`

## Description

The operator `QuatToPose` converts the input quaternion
*`quaternion`* into its corresponding 3D pose *`pose`*. Note that
the translation of *`pose`* is zero in any case.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`quaternion`** (input_control)  quaternion `→` [HQuaternion](HQuaternion.md), [HTuple](HTuple.md) (*double*)

Rotation quaternion.

**`pose`** (output_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

3D Pose.

## Possible Predecessors

`AxisAngleToQuat`,
`QuatCompose`,
`QuatConjugate`

## Possible Successors

`CameraCalibration`,
`WritePose`,
`DispCaltab`,
`SimCaltab`

## See also

`PoseToQuat`,
`AxisAngleToQuat`,
`QuatCompose`,
`QuatRotatePoint3d`,
`QuatToHomMat3d`,
`QuatNormalize`,
`DualQuatToPose`

## Module

Foundation
