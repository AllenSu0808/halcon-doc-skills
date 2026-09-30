# proj_hom_mat2d_to_pose (Operator)

## Name

`proj_hom_mat2d_to_pose` — Compute a pose out of a homography describing the relation between world
and image coordinates.

## Signature

`def proj_hom_mat2d_to_pose(homography: Sequence[float], camera_matrix: Sequence[float], method: str) -> Sequence[Union[float, int]]`

## Description

`proj_hom_mat2d_to_pose` computes a pose out of a homography
*`homography`* that describes the relation between 2D world-
(unit meters) and 2D image coordinates. The homography can be
obtained by the use of [`vector_to_proj_hom_mat2d`](vector_to_proj_hom_mat2d.md). To compute
a pose, a camera matrix (obtained by [`cam_par_to_cam_mat`](cam_par_to_cam_mat.md), for
example) has to be passed in *`camera_matrix`*. By setting the
Parameter *`method`*, it is possible to choose which
computation algorithm is used. Currently a direct decomposition
(*`method`* = 'decomposition') and a singular value
decomposition based method (*`method`* = 'decomposition_svd')
are supported. In general due to numeric reasons, the direct
decomposition method returns more stable results.

The subsequent calls of [`vector_to_proj_hom_mat2d`](vector_to_proj_hom_mat2d.md) and
`proj_hom_mat2d_to_pose` are similar to [`vector_to_pose`](vector_to_pose.md)
for 2D objects, whereas no refinement due to redundancy is
possible.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`homography`** (input_control)  hom_mat2d `→` Sequence[float]

The homography from world- to image coordinates.

**`camera_matrix`** (input_control)  hom_mat2d `→` Sequence[float]

The camera calibration matrix K.

**`method`** (input_control)  string `→` str

Type of pose computation.

Default:
"decomposition"

List of values:
"decomposition", "decomposition_svd"

**`pose`** (output_control)  pose `→` Sequence[Union[float, int]]

Pose of the 2D object.

## Result

`proj_hom_mat2d_to_pose` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct.

## Possible Predecessors

`image_points_to_world_plane`,
`vector_to_proj_hom_mat2d`

## See also

`vector_to_proj_hom_mat2d`,
`image_points_to_world_plane`,
`vector_to_pose`,
`camera_calibration`

## Module

Calibration
