# GetStereoModelParam (Operator)

## Name

`GetStereoModelParam` — Get stereo model parameters.

## Signature

`static void HOperatorSet.GetStereoModelParam(HTuple stereoModelID, HTuple genParamName, out HTuple genParamValue)`

`HTuple HStereoModel.GetStereoModelParam(HTuple genParamName)`

`HTuple HStereoModel.GetStereoModelParam(string genParamName)`

## Description

The operator `GetStereoModelParam` can be used to inspect diverse
parameters of the stereo model *`stereoModelID`* by specifying
their names in *`genParamName`* and getting their values in
*`genParamValue`*.
Two types of parameters can be inspected with this operator - general and
specific for surface reconstruction. Note that no specific parameters are
provided for 3D point stereo reconstruction.

All parameters that can be set with [`SetStereoModelParam`](set_stereo_model_param.md)
can also be queried with `GetStereoModelParam` - for a
description see the former operator. In contrast, the following
parameters are set by other operators and cannot be modified
afterwards.

### General parameters

- ***"type"*:** —

  Type of the stereo model (currently either
  *"surface_pairwise"*, *"surface_fusion"*
  or *"points_3d"*).
- ***"camera_setup_model"*:** —

  Handle to a *copy* of the camera setup model set in the
  stereo model.
  Changing properties of the copy does not affect the camera setup model
  stored in the stereo model.
- ***"from_cam_param_rect N"*, *"to_cam_param_rect N"*:** —

  Camera parameters of the rectified *from*- and *to*-cameras
  of camera pair N. See [`SetStereoModelImagePairs`](set_stereo_model_image_pairs.md) for more
  information about camera pairs.
- ***"from_cam_pose_rect N"*, *"to_cam_pose_rect N"*:** —

  Point transformation from the rectified *from*- and *to*-cameras
  of camera pair N to the respective unrectified camera.
  See [`SetStereoModelImagePairs`](set_stereo_model_image_pairs.md) for more
  information about camera pairs.
- ***"rel_pose_rect N"*:** —

  Point transformation from the rectified *to*-camera to the
  rectified *from*-camera.
  See [`SetStereoModelImagePairs`](set_stereo_model_image_pairs.md) for more
  information about camera pairs.

The parameters *"type"* and *"camera_setup_model"* are set
when creating the stereo model with [`CreateStereoModel`](create_stereo_model.md). For
*"from_cam_param_rect N"*, *"to_cam_param_rect N"*,
*"from_cam_pose_rect N"*, *"to_cam_pose_rect N"*,
and *"rel_pose_rect N"*, note that these parameters are only
available *after* setting the image pairs (see
[`SetStereoModelImagePairs`](set_stereo_model_image_pairs.md)).

### A note on tuple-valued model parameters

Most of the stereo model parameters are single-valued. Thus,
you can provide a list (i.e., tuple) of parameter names and get a
list (tuple) of values that has the same length as the output tuple.
In contrast, when querying a tuple-valued parameter, a tuple
of values is returned. When querying such a parameter together with
other parameters, the value-to-parameter-name correspondence is not
obvious anymore. Thus, tuple-valued parameters like
*"bounding_box"*, *"min_disparity"* or *"max_disparity"*
should always be queried in a separate call to
`GetStereoModelParam`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`stereoModelID`** (input_control)  stereo_model `→` [HStereoModel](HStereoModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the stereo model.

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the parameters to be set.

List of values:
"binocular_filter", "binocular_mask_height", "binocular_mask_width", "binocular_method", "binocular_mg_cycle_type", "binocular_mg_gradient_constancy", "binocular_mg_gray_constancy", "binocular_mg_initial_guess", "binocular_mg_initial_level", "binocular_mg_iterations", "binocular_mg_post_relax", "binocular_mg_pre_relax", "binocular_mg_pyramid_factor", "binocular_mg_smoothness", "binocular_mg_solver", "binocular_ms_consistency_check", "binocular_ms_edge_smoothing", "binocular_ms_similarity_measure", "binocular_ms_sub_disparity", "binocular_ms_surface_smoothing", "binocular_num_levels", "binocular_score_thresh", "binocular_sub_disparity", "binocular_texture_thresh", "bounding_box", "camera_setup_model", "color", "color_invisible", "disparity_method", "from_cam_param_rect", "from_cam_pose_rect", "max_disparity", "min_disparity", "min_thickness", "persistence", "point_meshing", "poisson_depth", "poisson_samples_per_node", "poisson_solver_divide", "rectif_interpolation", "rectif_method", "rectif_sub_sampling", "rel_pose_rect", "resolution", "smoothing", "sub_sampling_step", "surface_tolerance", "to_cam_param_rect", "to_cam_pose_rect", "type"

**`genParamValue`** (output_control)  attribute.value-array `→` [HTuple](HTuple.md) (*double* / int / long / string)

Values of the parameters to be set.

## Possible Predecessors

`CreateStereoModel`,
`SetStereoModelParam`

## Possible Successors

`ReconstructSurfaceStereo`,
`ReconstructPointsStereo`

## See also

`SetStereoModelParam`

## Module

3D Metrology
