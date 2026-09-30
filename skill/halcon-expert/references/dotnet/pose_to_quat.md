# PoseToQuat (Operator)

## Name

`PoseToQuat` — Convert the rotational part of a 3D pose to a quaternion.

## Signature

`static void HOperatorSet.PoseToQuat(HTuple pose, out HTuple quaternion)`

`static HQuaternion[] HQuaternion.PoseToQuat(HPose[] pose)`

`void HQuaternion.PoseToQuat(HPose pose)`

## Description

The operator `PoseToQuat` converts the rotation of the input 3D pose
*`pose`* into its corresponding quaternion *`quaternion`*.
Note that the translation of *`pose`* is ignored.
Multiple poses can be passed in *`pose`*, in which case a quaternion
is returned for each of them.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`pose`** (input_control)  pose(-array) `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

3D Pose.

**`quaternion`** (output_control)  quaternion(-array) `→` [HQuaternion](HQuaternion.md), [HTuple](HTuple.md) (*double*)

Rotation quaternion.

## Possible Predecessors

`CreatePose`,
`ReadPose`

## Possible Successors

`QuatCompose`,
`QuatRotatePoint3d`,
`QuatInterpolate`

## Alternatives

`AxisAngleToQuat`

## See also

`QuatToPose`,
`QuatToHomMat3d`,
`QuatCompose`,
`QuatRotatePoint3d`,
`PoseToDualQuat`

## Module

Foundation
