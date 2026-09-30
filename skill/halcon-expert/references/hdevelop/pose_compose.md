# pose_compose (Operator)

## Name

`pose_compose` — Combine 3D poses given in two tuples.

## Signature

`pose_compose( : : PoseLeft, PoseRight : PoseCompose)`

## Description

`pose_compose` combines the poses in the tuples, *`PoseLeft`* and
*`PoseRight`*. If both tuples contain the same number of poses, the
corresponding elements of both tuples are composed. Otherwise, either tuple
*`PoseLeft`* or *`PoseRight`* must contain only one pose.
In this case, the composition is performed for each pose of the longer tuple
with the single pose of the other tuple. For each composition, the poses are
interpreted as transformations of coordinate systems. The poses in tuple
*`PoseCompose`* are therefore the result of applying the corresponding
poses in *`PoseLeft`* and *`PoseRight`* in sequence.

First, the respective poses in *`PoseLeft`* and *`PoseRight`*
are transformed into the corresponding homogeneous transformation matrices
$\mathbf{H}_{\textit{1}}$ and $\mathbf{H}_{\textit{2}}$.
$\mathbf{H}_{\textit{1}}$ is then multiplied with
$\mathbf{H}_{\textit{2}}$. The resulting matrix
$\mathbf{H}_{\textit{1}}\cdot$ $\mathbf{H}_{\textit{2}}$ is converted
into a pose and returned at the corresponding index in tuple
*`PoseCompose`*.

If the respective poses in *`PoseLeft`* and *`PoseRight`* have
different types, the default pose type 0 ('Rp+T', 'gba', 'point') is
returned. Otherwise, the returned poses have the same types as the poses
used for their composition.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`PoseLeft`** (input_control)  pose(-array) `→`  (real / integer)

Tuple containing the left poses.

**`PoseRight`** (input_control)  pose(-array) `→`  (real / integer)

Tuple containing the right poses.

**`PoseCompose`** (output_control)  pose(-array) `→`  (real / integer)

Tuple containing the returned poses.

## Result

`pose_compose` returns 2 (
H_MSG_TRUE)
if all parameters are valid.
If necessary, an exception is raised.

## Possible Predecessors

`read_pose`,
`hom_mat3d_to_pose`,
`create_pose`,
`convert_pose_type`,
`pose_invert`

## Possible Successors

`convert_pose_type`

## Alternatives

`hom_mat3d_compose`,
`dual_quat_compose`

## See also

`pose_to_hom_mat3d`,
`hom_mat3d_to_pose`,
`hom_mat3d_compose`

## Module

Foundation
