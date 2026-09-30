# refine_surface_model_pose_image (Operator)

## Name

`refine_surface_model_pose_image` — Refine the pose of a surface model in a 3D scene and in images.

## Signature

`refine_surface_model_pose_image(Image : : SurfaceModelID, ObjectModel3D, InitialPose, MinScore, ReturnResultHandle, GenParamName, GenParamValue : Pose, Score, SurfaceMatchingResultID)`

## Description

The operator `refine_surface_model_pose_image` refines the approximate
pose *`InitialPose`* of the surface model *`SurfaceModelID`* in
the 3D scene comprised of the 3D surface in *`ObjectModel3D`* and the
images of the scene in *`Image`*.
Note that the number of images passed in *`Image`* must correspond
to the number of cameras set with [`set_surface_model_param`](set_surface_model_param.md).
Note also that the surface model must have been created by
[`create_surface_model`](create_surface_model.md) with the parameter *'train_3d_edges'*
enabled.

The refinement simultaneously optimizes the alignment of the
model with the 3D scene as well as the alignment of the reprojected edges
with edges in the passed images. The domain of the images is ignored.

In addition to the parameters documented in
[`refine_surface_model_pose`](refine_surface_model_pose.md), `refine_surface_model_pose_image`
also supports the generic parameters *'min_contrast'* and
*'max_deformation'*, documented in [`find_surface_model_image`](find_surface_model_image.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

This operator supports canceling timeouts and interrupts.

## Parameters

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / uint2)

Images of the scene.

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
'3d_edge_min_amplitude_abs', '3d_edge_min_amplitude_rel', '3d_edges', 'max_deformation', 'min_contrast', 'pose_ref_dist_threshold_abs', 'pose_ref_dist_threshold_rel', 'pose_ref_num_steps', 'pose_ref_scoring_dist_abs', 'pose_ref_scoring_dist_rel', 'pose_ref_sub_sampling', 'pose_ref_use_scene_normals', 'use_3d_edges', 'use_self_similar_poses', 'use_view_based', 'viewpoint'

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

`refine_surface_model_pose_image` returns 2 (
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
`refine_surface_model_pose`,
`find_surface_model_image`

## See also

`create_surface_model`,
`find_surface_model`,
`refine_surface_model_pose`

## Module

3D Metrology
