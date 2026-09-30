# pose_invert (Operator)

## Name

`pose_invert` — Invert each pose in a tuple of 3D poses.

## Signature

`pose_invert( : : Pose : PoseInvert)`

## Description

`pose_invert` inverts each pose of the given tuple *`Pose`* by
transforming it into the corresponding homogeneous transformation matrix
$\mathbf{H}$ and inverting this matrix. The resulting matrix
is converted into a pose. This pose is returned at the respective index
in the tuple *`PoseInvert`*. The returned poses have the same types
as the original poses.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Pose`** (input_control)  pose(-array) `→`  (real / integer)

Tuple of 3D poses.

**`PoseInvert`** (output_control)  pose(-array) `→`  (real / integer)

Tuple of inverted 3D poses.

## Result

`pose_invert` returns 2 (
H_MSG_TRUE)
if all parameters are valid.
If necessary, an exception is raised.

## Possible Predecessors

`read_pose`,
`hom_mat3d_to_pose`,
`create_pose`,
`convert_pose_type`,
`pose_compose`

## Possible Successors

`convert_pose_type`

## Alternatives

`hom_mat3d_invert`,
`dual_quat_conjugate`

## See also

`pose_to_hom_mat3d`,
`hom_mat3d_to_pose`

## Module

Foundation
