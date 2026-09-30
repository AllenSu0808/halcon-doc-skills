# refine_surface_model_pose_image (Operator)

## Name

`refine_surface_model_pose_image` — Refine the pose of a surface model in a 3D scene and in images.

## Signature

`def refine_surface_model_pose_image(image: HObject, surface_model_id: HHandle, object_model_3d: HHandle, initial_pose: Sequence[Union[float, int]], min_score: MaybeSequence[Union[float, int]], return_result_handle: str, gen_param_name: Sequence[str], gen_param_value: Sequence[Union[str, float, int]]) -> Tuple[Sequence[Union[float, int]], Sequence[float], Sequence[HHandle]]`

`def refine_surface_model_pose_image_s(image: HObject, surface_model_id: HHandle, object_model_3d: HHandle, initial_pose: Sequence[Union[float, int]], min_score: MaybeSequence[Union[float, int]], return_result_handle: str, gen_param_name: Sequence[str], gen_param_value: Sequence[Union[str, float, int]]) -> Tuple[Sequence[Union[float, int]], Sequence[float], HHandle]`

## Description

The operator `refine_surface_model_pose_image` refines the approximate
pose *`initial_pose`* of the surface model *`surface_model_id`* in
the 3D scene comprised of the 3D surface in *`object_model_3d`* and the
images of the scene in *`image`*.
Note that the number of images passed in *`image`* must correspond
to the number of cameras set with [`set_surface_model_param`](set_surface_model_param.md).
Note also that the surface model must have been created by
[`create_surface_model`](create_surface_model.md) with the parameter *"train_3d_edges"*
enabled.

The refinement simultaneously optimizes the alignment of the
model with the 3D scene as well as the alignment of the reprojected edges
with edges in the passed images. The domain of the images is ignored.

In addition to the parameters documented in
[`refine_surface_model_pose`](refine_surface_model_pose.md), `refine_surface_model_pose_image`
also supports the generic parameters *"min_contrast"* and
*"max_deformation"*, documented in [`find_surface_model_image`](find_surface_model_image.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

This operator supports canceling timeouts and interrupts.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / uint2)

Images of the scene.

**`surface_model_id`** (input_control)  surface_model `→` HHandle

Handle of the surface model.

**`object_model_3d`** (input_control)  object_model_3d `→` HHandle

Handle of the 3D object model containing the
scene.

**`initial_pose`** (input_control)  pose(-array) `→` Sequence[Union[float, int]]

Initial pose of the surface model in the scene.

**`min_score`** (input_control)  real(-array) `→` MaybeSequence[Union[float, int]]

Minimum score of the returned poses.

Default:
0

Restriction:
`MinScore >= 0`

**`return_result_handle`** (input_control)  string `→` str

Enable returning a result handle in
*`surface_matching_result_id`*.

Default:
"false"

List of values:
"false", "true"

**`gen_param_name`** (input_control)  attribute.name-array `→` Sequence[str]

Names of the generic parameters.

Default:
[]

List of values:
"3d_edge_min_amplitude_abs", "3d_edge_min_amplitude_rel", "3d_edges", "max_deformation", "min_contrast", "pose_ref_dist_threshold_abs", "pose_ref_dist_threshold_rel", "pose_ref_num_steps", "pose_ref_scoring_dist_abs", "pose_ref_scoring_dist_rel", "pose_ref_sub_sampling", "pose_ref_use_scene_normals", "use_3d_edges", "use_self_similar_poses", "use_view_based", "viewpoint"

**`gen_param_value`** (input_control)  attribute.value-array `→` Sequence[Union[str, float, int]]

Values of the generic parameters.

Default:
[]

Suggested values:
0, 1, "true", "false", 0.005, 0.01, 0.03, 0.05, 0.1

**`pose`** (output_control)  pose(-array) `→` Sequence[Union[float, int]]

3D pose of the surface model in the scene.

**`score`** (output_control)  real-array `→` Sequence[float]

Score of the found instances of the model.

**`surface_matching_result_id`** (output_control)  surface_matching_result(-array) `→` Sequence[HHandle]

Handle of the matching result, if enabled in
*`return_result_handle`*.

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
