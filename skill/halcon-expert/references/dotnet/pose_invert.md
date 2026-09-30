# PoseInvert (Operator)

## Name

`PoseInvert` — Invert each pose in a tuple of 3D poses.

## Signature

`static void HOperatorSet.PoseInvert(HTuple pose, out HTuple poseInvert)`

`static HPose[] HPose.PoseInvert(HPose[] pose)`

`HPose HPose.PoseInvert()`

## Description

`PoseInvert` inverts each pose of the given tuple *`pose`* by
transforming it into the corresponding homogeneous transformation matrix
$\mathbf{H}$ and inverting this matrix. The resulting matrix
is converted into a pose. This pose is returned at the respective index
in the tuple *`poseInvert`*. The returned poses have the same types
as the original poses.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`pose`** (input_control)  pose(-array) `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

Tuple of 3D poses.

**`poseInvert`** (output_control)  pose(-array) `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

Tuple of inverted 3D poses.

## Result

`PoseInvert` returns 2 (
H_MSG_TRUE)
if all parameters are valid.
If necessary, an exception is raised.

## Possible Predecessors

`ReadPose`,
`HomMat3dToPose`,
`CreatePose`,
`ConvertPoseType`,
`PoseCompose`

## Possible Successors

`ConvertPoseType`

## Alternatives

`HomMat3dInvert`,
`DualQuatConjugate`

## See also

`PoseToHomMat3d`,
`HomMat3dToPose`

## Module

Foundation
