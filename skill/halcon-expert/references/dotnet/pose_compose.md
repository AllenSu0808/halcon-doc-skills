# PoseCompose (Operator)

## Name

`PoseCompose` — Combine 3D poses given in two tuples.

## Signature

`static void HOperatorSet.PoseCompose(HTuple poseLeft, HTuple poseRight, out HTuple poseCompose)`

`static HPose[] HPose.PoseCompose(HPose[] poseLeft, HPose[] poseRight)`

`HPose HPose.PoseCompose(HPose poseRight)`

## Description

`PoseCompose` combines the poses in the tuples, *`poseLeft`* and
*`poseRight`*. If both tuples contain the same number of poses, the
corresponding elements of both tuples are composed. Otherwise, either tuple
*`poseLeft`* or *`poseRight`* must contain only one pose.
In this case, the composition is performed for each pose of the longer tuple
with the single pose of the other tuple. For each composition, the poses are
interpreted as transformations of coordinate systems. The poses in tuple
*`poseCompose`* are therefore the result of applying the corresponding
poses in *`poseLeft`* and *`poseRight`* in sequence.

First, the respective poses in *`poseLeft`* and *`poseRight`*
are transformed into the corresponding homogeneous transformation matrices
$\mathbf{H}_{\textit{1}}$ and $\mathbf{H}_{\textit{2}}$.
$\mathbf{H}_{\textit{1}}$ is then multiplied with
$\mathbf{H}_{\textit{2}}$. The resulting matrix
$\mathbf{H}_{\textit{1}}\cdot$ $\mathbf{H}_{\textit{2}}$ is converted
into a pose and returned at the corresponding index in tuple
*`poseCompose`*.

If the respective poses in *`poseLeft`* and *`poseRight`* have
different types, the default pose type 0 ('Rp+T', 'gba', 'point') is
returned. Otherwise, the returned poses have the same types as the poses
used for their composition.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`poseLeft`** (input_control)  pose(-array) `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

Tuple containing the left poses.

**`poseRight`** (input_control)  pose(-array) `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

Tuple containing the right poses.

**`poseCompose`** (output_control)  pose(-array) `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

Tuple containing the returned poses.

## Result

`PoseCompose` returns 2 (
H_MSG_TRUE)
if all parameters are valid.
If necessary, an exception is raised.

## Possible Predecessors

`ReadPose`,
`HomMat3dToPose`,
`CreatePose`,
`ConvertPoseType`,
`PoseInvert`

## Possible Successors

`ConvertPoseType`

## Alternatives

`HomMat3dCompose`,
`DualQuatCompose`

## See also

`PoseToHomMat3d`,
`HomMat3dToPose`,
`HomMat3dCompose`

## Module

Foundation
