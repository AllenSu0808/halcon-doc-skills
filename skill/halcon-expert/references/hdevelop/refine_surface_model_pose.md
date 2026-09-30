# refine_surface_model_pose (Operator)

## Name

`refine_surface_model_pose` — Refine the pose of a surface model in a 3D scene.

## Signature

`refine_surface_model_pose( : : SurfaceModelID, ObjectModel3D, InitialPose, MinScore, ReturnResultHandle, GenParamName, GenParamValue : Pose, Score, SurfaceMatchingResultID)`

## Description

The operator `refine_surface_model_pose` refines the approximate
pose *`InitialPose`* of the surface model *`SurfaceModelID`* in
the 3D scene *`ObjectModel3D`*.
The surface model *`SurfaceModelID`* must have been created previously
with [`create_surface_model`](create_surface_model.md) or [`read_surface_model`](read_surface_model.md).
Additionally, [`set_surface_model_param`](set_surface_model_param.md) can be used to
set certain parameters that influence the refinement, such as
restricting the allowed range of rotations.

`refine_surface_model_pose` is useful if the pose of an object in
a scene is approximately known and only needs to be refined.
The refined pose is returned in *`Pose`*, along with a score in
*`Score`*.
It is possible to pass multiple poses for refinement.
Note that, contrary to [`find_surface_model`](find_surface_model.md), the returned poses are
not sorted by their score but are returned in the same order as the input
poses.

The maximum possible error in the approximate pose that can still be
refined depends on the type of object, the amount of clutter in the scene
and the visible parts of the objects.
In general, differences in the orientation of up to 15° and
differences in the position of up to 10% can be refined.

The accuracy of the pose refinement is limited to around
0.1% of the model's size due to numerical reasons. The accuracy
further depends on the noise of the scene points, the number of
scene points and the shape of the model.

Details about the pose refinement and the parameters are described in the
documentation of [`find_surface_model`](find_surface_model.md) in the section about the
dense pose refinement step.
The following generic parameters can be set for
`refine_surface_model_pose`, and are also documented in
[`find_surface_model`](find_surface_model.md):
*'pose_ref_num_steps'*,
*'pose_ref_sub_sampling'*,
*'pose_ref_dist_threshold_rel'*,
*'pose_ref_dist_threshold_abs'*,
*'pose_ref_scoring_dist_rel'*,
*'pose_ref_scoring_dist_abs'*,
*'pose_ref_use_scene_normals'*,
*'3d_edge_min_amplitude_rel'*,
*'3d_edge_min_amplitude_abs'*,
*'3d_edges'*,
*'use_3d_edges'*,
*'use_view_based'*,
*'use_self_similar_poses'*,
*'pose_ref_dist_threshold_edges_rel'*,
*'pose_ref_dist_threshold_edges_abs'*,
*'pose_ref_scoring_dist_edges_rel'*, and
*'pose_ref_scoring_dist_edges_abs'*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

This operator supports canceling timeouts and interrupts.

## Parameters

**`SurfaceModelID`** (input_control)  surface_model `→`  (handle)

Handle of the surface model.

**`ObjectModel3D`** (input_control)  object_model_3d `→`  (handle)

Handle of the 3D object model containing the
scene.

**`InitialPose`** (input_control)  pose(-array) `→`  (real / integer)

Initial pose of the surface model in the scene.

**`MinScore`** (input_control)  real(-array) `→`  (real / integer)

Minimum score of the returned poses.

Default:
0

Restriction:
`MinScore >= 0`

**`ReturnResultHandle`** (input_control)  string `→`  (string)

Enable returning a result handle in
*`SurfaceMatchingResultID`*.

Default:
'false'

List of values:
'false', 'true'

**`GenParamName`** (input_control)  attribute.name-array `→`  (string)

Names of the generic parameters.

Default:
[]

List of values:
'3d_edge_min_amplitude_abs', '3d_edge_min_amplitude_rel', '3d_edges', 'pose_ref_dist_threshold_abs', 'pose_ref_dist_threshold_rel', 'pose_ref_num_steps', 'pose_ref_scoring_dist_abs', 'pose_ref_scoring_dist_rel', 'pose_ref_sub_sampling', 'pose_ref_use_scene_normals', 'use_3d_edges', 'use_self_similar_poses', 'use_view_based', 'viewpoint'

**`GenParamValue`** (input_control)  attribute.value-array `→`  (string / real / integer)

Values of the generic parameters.

Default:
[]

Suggested values:
0, 1, 'true', 'false', 0.005, 0.01, 0.03, 0.05, 0.1

**`Pose`** (output_control)  pose(-array) `→`  (real / integer)

3D pose of the surface model in the scene.

**`Score`** (output_control)  real-array `→`  (real)

Score of the found instances of the model.

**`SurfaceMatchingResultID`** (output_control)  surface_matching_result(-array) `→`  (handle)

Handle of the matching result, if enabled in
*`ReturnResultHandle`*.

## Result

`refine_surface_model_pose` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`read_object_model_3d`,
`xyz_to_object_model_3d`,
`get_object_model_3d_params`,
`read_surface_model`,
`create_surface_model`,
`get_surface_model_param`,
`find_surface_model`,
`edges_object_model_3d`

## Possible Successors

`get_surface_matching_result`,
`clear_surface_matching_result`,
`clear_object_model_3d`

## Alternatives

`find_surface_model`,
`refine_surface_model_pose_image`,
`find_surface_model_image`

## See also

`create_surface_model`,
`find_surface_model`,
`refine_surface_model_pose_image`

## Module

3D Metrology
