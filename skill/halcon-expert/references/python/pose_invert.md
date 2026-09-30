# pose_invert (Operator)

## Name

`pose_invert` — Invert each pose in a tuple of 3D poses.

## Signature

`def pose_invert(pose: Sequence[Union[float, int]]) -> Sequence[Union[float, int]]`

## Description

`pose_invert` inverts each pose of the given tuple *`pose`* by
transforming it into the corresponding homogeneous transformation matrix
$\mathbf{H}$ and inverting this matrix. The resulting matrix
is converted into a pose. This pose is returned at the respective index
in the tuple *`pose_invert`*. The returned poses have the same types
as the original poses.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`pose`** (input_control)  pose(-array) `→` Sequence[Union[float, int]]

Tuple of 3D poses.

**`pose_invert`** (output_control)  pose(-array) `→` Sequence[Union[float, int]]

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
