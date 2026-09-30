# get_surface_model_param (Operator)

## Name

`get_surface_model_param` — Return the parameters and properties of a surface model.

## Signature

`def get_surface_model_param(surface_model_id: HHandle, gen_param_name: MaybeSequence[str]) -> Sequence[HTupleElementType]`

`def get_surface_model_param_s(surface_model_id: HHandle, gen_param_name: MaybeSequence[str]) -> HTupleElementType`

## Description

The operator `get_surface_model_param` returns parameters and
properties of the surface model *`surface_model_id`*.
The surface model must have been created by [`create_surface_model`](create_surface_model.md)
or [`read_surface_model`](read_surface_model.md).
The names of the desired properties are passed in the generic parameter
*`gen_param_name`*, the corresponding values are returned in
*`gen_param_value`*.

The following values are possible for *`gen_param_name`*:

- ***"diameter"*:** —

  Diameter of the model point cloud. The diameter is the length of the
  diagonal of the axis-parallel bounding box (see parameter
  *"bounding_box1"*).
- ***"center"*:** —

  Center point of the model. The center point is the center of the
  axis-parallel bounding box (see parameter *"bounding_box1"*).
- ***"bounding_box1"*:** —

  Smallest enclosing axis-parallel cuboid
  (min_x, min_y, min_z, max_x, max_y, max_z).
- ***"sampled_model"*:** —

  The 3D points sampled from the model for matching.
  This returns an ObjectModel3D that contains all points sampled from the
  model surface for matching.
- ***"sampled_pose_refinement"*:** —

  The 3D model points subsampled from the model for the pose refinement.
  This returns an ObjectModel3D that contains all points sampled from the
  model surface for pose refinement.
- ***"3d_edges_trained"*:** —

  Returns if the surface model was prepared for edge-supported
  surface-based matching, i.e.,
  if the parameter *"train_3d_edges"* was enabled in
  [`create_surface_model`](create_surface_model.md).
  The returned value is either *"true"* or *"false"*.
- ***"view_based_trained"*:** —

  Returns if the surface model was prepared to support view-based score
  computation for surface-based matching, i.e.,
  if the parameter *"train_view_based"* was enabled in
  [`create_surface_model`](create_surface_model.md).
  The returned value is either *"true"* or *"false"*.
- ***"camera_parameter"*:** —
- ***"camera_parameter X"*:** —

  Returns the camera parameters for camera number X, where X is a zero-based
  index for the cameras. If not given, X defaults zero (first camera).
  The camera parameters must previously have been set by
  [`set_surface_model_param`](set_surface_model_param.md).
- ***"camera_pose"*:** —
- ***"camera_pose X"*:** —

  Returns the camera pose for camera number X, where X is a zero-based
  index for the cameras. If not given, X defaults zero (first camera).
- ***"symmetry_axis_direction"*:** —
- ***"symmetry_axis_origin"*:** —

  Returns the symmetry axis or origin, respectively, as set with
  [`set_surface_model_param`](set_surface_model_param.md). If no axis is set, an empty tuple
  is returned.
- ***"symmetry_poses"*:** —

  Returns the symmetry poses as set with [`set_surface_model_param`](set_surface_model_param.md).
- ***"symmetry_poses_all"*:** —

  Returns all symmetry poses created by [`set_surface_model_param`](set_surface_model_param.md)
  based on the symmetry poses set with [`set_surface_model_param`](set_surface_model_param.md).
- ***"pose_restriction_reference_pose"*:** —

  Returns the reference pose as set with [`set_surface_model_param`](set_surface_model_param.md),
  or an empty tuple if not set.
- ***"pose_restriction_max_angle_diff"*:** —

  Returns the maximum angular difference between the reference pose
  and found poses, in radians, or an empty tuple if not set.
- ***"pose_restriction_allowed_axis_direction"*:** —
- ***"pose_restriction_allowed_axis_origin"*:** —

  Returns the allowed rotation axis and origin, respectively, as set
  with [`set_surface_model_param`](set_surface_model_param.md). If no axis is set, an empty
  tuple is returned.
- ***"pose_restriction_filter_final_poses_only"*:** —

  Returns *"true"* if only the final poses are filtered, or
  *"false"* if the poses are filtered during the matching process
  (default).
- ***"self_similar_poses_trained"*:** —

  Returns if the surface model was prepared for optimizations
  regarding self-similar, almost symmetric poses, i.e.,
  if the parameter *"train_self_similar_poses"* was enabled
  in [`create_surface_model`](create_surface_model.md).
  The returned value is either *"true"* or *"false"*.
- ***"sampled_self_similarity"*:** —

  Returns an ObjectModel3D that contains those 3D points of the model
  that were sampled for the search of self-similar poses.
- ***"self_similar_poses"*:** —

  Returns the poses under which the object is self-similar, i.e., almost
  symmetric.
  If the parameter *"train_self_similar_poses"* was not enabled
  in [`create_surface_model`](create_surface_model.md), an empty tuple is returned.
- ***"self_similar_poses_models"*:** —

  Returns a tuple of ObjectModel3Ds that contains a copy of the original
  model, transformed into the poses returned by *"self_similar_poses"*.
  This allows for a visual inspection of the self-similar poses.
  This parameter is only available if the surface model was created with
  activated parameter *"train_self_similar_poses"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`surface_model_id`** (input_control)  surface_model `→` HHandle

Handle of the surface model.

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Name of the parameter.

Default:
"diameter"

List of values:
"3d_edges_trained", "bounding_box1", "camera_parameter", "camera_pose", "center", "diameter", "pose_restriction_allowed_axis_direction", "pose_restriction_allowed_axis_origin", "pose_restriction_filter_final_poses_only", "pose_restriction_max_angle_diff", "pose_restriction_reference_pose", "sampled_model", "sampled_pose_refinement", "sampled_self_similarity", "self_similar_poses", "self_similar_poses_models", "self_similar_poses_trained", "symmetry_axis_direction", "symmetry_axis_origin", "symmetry_poses", "symmetry_poses_all", "view_based_trained"

**`gen_param_value`** (output_control)  attribute.value(-array) `→` Sequence[HTupleElementType]

Value of the parameter.

## Result

`get_surface_model_param` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`create_surface_model`,
`read_surface_model`

## Possible Successors

`find_surface_model`,
`refine_surface_model_pose`,
`write_surface_model`

## See also

`create_surface_model`,
`set_surface_model_param`

## Module

3D Metrology
