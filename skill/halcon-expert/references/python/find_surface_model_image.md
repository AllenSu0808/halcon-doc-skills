# find_surface_model_image (Operator)

## Name

`find_surface_model_image` — Find the best matches of a surface model in a 3D scene and images.

## Signature

`def find_surface_model_image(image: HObject, surface_model_id: HHandle, object_model_3d: HHandle, rel_sampling_distance: float, key_point_fraction: float, min_score: MaybeSequence[Union[float, int]], return_result_handle: str, gen_param_name: Sequence[str], gen_param_value: Sequence[Union[str, float, int]]) -> Tuple[Sequence[Union[float, int]], Sequence[float], Sequence[HHandle]]`

`def find_surface_model_image_s(image: HObject, surface_model_id: HHandle, object_model_3d: HHandle, rel_sampling_distance: float, key_point_fraction: float, min_score: MaybeSequence[Union[float, int]], return_result_handle: str, gen_param_name: Sequence[str], gen_param_value: Sequence[Union[str, float, int]]) -> Tuple[Sequence[Union[float, int]], Sequence[float], HHandle]`

## Description

The operator `find_surface_model_image` finds the best matches of
the surface model *`surface_model_id`* in the scene that is comprised
of the 3D surface in *`object_model_3d`* and the images of the scene in
*`image`*.
Note that the number of images passed in *`image`* must correspond
to the number of cameras set with [`set_surface_model_param`](set_surface_model_param.md).
Note also that the surface model must have been created by
[`create_surface_model`](create_surface_model.md) with the parameter *"train_3d_edges"*
enabled.

The images are used only in the sparse and dense refinement step.
For this, the refinement simultaneously optimizes the alignment of the
model with the 3D scene as well as the alignment of the reprojected edges
of the model silhouette with edges in the passed images. The domain of
the images is ignored.

In addition to the parameters documented in
[`find_surface_model`](find_surface_model.md), `find_surface_model_image` also supports
the following generic parameters:

- ***"min_contrast"*:** —

  Sets the minimum contrast of the object in the search images. Edges
  with a contrast below this threshold are ignored in the refinement.

  Suggested values:
   *5*, *10*, *20*

  Default:
   *10*

  Restriction:
   *"min_contrast"* >= *0*
- ***"max_deformation"*:** —

  Sets the search range in pixels for corresponding edges in the image.
  This parameter can be used if the shape of the object is slightly deformed
  compared to the original 3D model used in [`create_surface_model`](create_surface_model.md).
  Note that increasing this parameter can have a significant impact on the
  runtime of the refinement.

  Suggested values:
   *0*, *1*, *5*

  Default:
   *1*

  Restriction:
   *"max_deformation"* >= *0*

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

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

**`rel_sampling_distance`** (input_control)  real `→` float

Scene sampling distance relative to the diameter
of the surface model.

Default:
0.05

Suggested values:
0.1, 0.07, 0.05, 0.04, 0.03

Restriction:
`0 < RelSamplingDistance < 1`

**`key_point_fraction`** (input_control)  real `→` float

Fraction of sampled scene points used as
key points.

Default:
0.2

Suggested values:
0.3, 0.2, 0.1, 0.05

Restriction:
`0 < KeyPointFraction <= 1`

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

Suggested values:
"true", "false"

**`gen_param_name`** (input_control)  attribute.name-array `→` Sequence[str]

Names of the generic parameters.

Default:
[]

List of values:
"3d_edge_min_amplitude_abs", "3d_edge_min_amplitude_rel", "3d_edges", "dense_pose_refinement", "max_deformation", "max_gap", "max_overlap_dist_abs", "max_overlap_dist_rel", "min_contrast", "num_matches", "pose_ref_dist_threshold_abs", "pose_ref_dist_threshold_rel", "pose_ref_num_steps", "pose_ref_scoring_dist_abs", "pose_ref_scoring_dist_rel", "pose_ref_sub_sampling", "pose_ref_use_scene_normals", "scene_invert_normals", "scene_normal_computation", "sparse_pose_refinement", "use_3d_edges", "use_self_similar_poses", "use_view_based", "viewpoint"

**`gen_param_value`** (input_control)  attribute.value-array `→` Sequence[Union[str, float, int]]

Values of the generic parameters.

Default:
[]

Suggested values:
0, 1, "true", "false", 0.005, 0.01, 0.03, 0.05, 0.1, "num_scene_points", "model_point_fraction", "num_model_points", "fast", "mls"

**`pose`** (output_control)  pose(-array) `→` Sequence[Union[float, int]]

3D pose of the surface model in the scene.

**`score`** (output_control)  real-array `→` Sequence[float]

Score of the found instances of the surface
model.

**`surface_matching_result_id`** (output_control)  surface_matching_result(-array) `→` Sequence[HHandle]

Handle of the matching result, if enabled in
*`return_result_handle`*.

## Result

`find_surface_model_image` returns 2 (
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
`edges_object_model_3d`

## Possible Successors

`refine_surface_model_pose`,
`get_surface_matching_result`,
`clear_surface_matching_result`,
`clear_object_model_3d`

## Alternatives

`refine_surface_model_pose`,
`find_surface_model`,
`refine_surface_model_pose_image`

## See also

`refine_surface_model_pose`,
`find_surface_model`

## Module

3D Metrology
