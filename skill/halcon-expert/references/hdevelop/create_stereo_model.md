# create_stereo_model (Operator)

## Name

`create_stereo_model` — Create a HALCON stereo model.

## Signature

`create_stereo_model( : : CameraSetupModelID, Method, GenParamName, GenParamValue : StereoModelID)`

## Description

The operator `create_stereo_model` creates a HALCON stereo model
and returns a handle to it in *`StereoModelID`*. The model provides
functionality for reconstructing either 3D points or surfaces from a
calibrated multi-view stereo camera setup specified in
*`CameraSetupModelID`* (refer to [Calibration / Multi-View](toc_calibration_multiview.md) for
further details on calibration of multiple cameras).

For *`Method`*=*'points_3d'*, a stereo model is created that,
after being configured, can be passed to
[`reconstruct_points_stereo`](reconstruct_points_stereo.md). The latter reconstructs 3D points by
intersecting lines of sight from point correspondences, extracted from
multiple calibrated images (see [`reconstruct_points_stereo`](reconstruct_points_stereo.md) for more
details).

For *`Method`*=*'surface_pairwise'* or
*`Method`*=*'surface_fusion'*, a stereo model is created
that, after being configured, can be passed to
[`reconstruct_surface_stereo`](reconstruct_surface_stereo.md). The latter obtains disparity images
from preselected image pairs in a calibrated multi-view stereo setup and
fuses the collected 3D information in a single surface reconstruction
(see [`reconstruct_surface_stereo`](reconstruct_surface_stereo.md) for more details).

The parameters *`GenParamName`* and *`GenParamValue`* can
be used to set general model parameters. Alternatively, these parameters
can be modified with the operator [`set_stereo_model_param`](set_stereo_model_param.md)
before the corresponding reconstruction operator is called (see
[`set_stereo_model_param`](set_stereo_model_param.md) for more details on the available
model parameters).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`CameraSetupModelID`** (input_control)  camera_setup_model `→`  (handle)

Handle to the camera setup model.

**`Method`** (input_control)  string `→`  (string)

Reconstruction method.

Default:
'surface_pairwise'

List of values:
'points_3d', 'surface_fusion', 'surface_pairwise'

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Name of the model parameter to be set.

Default:
[]

List of values:
'binocular_filter', 'binocular_mask_height', 'binocular_mask_width', 'binocular_method', 'binocular_mg_cycle_type', 'binocular_mg_default_parameters', 'binocular_mg_gradient_constancy', 'binocular_mg_gray_constancy', 'binocular_mg_initial_guess', 'binocular_mg_initial_level', 'binocular_mg_iterations', 'binocular_mg_post_relax', 'binocular_mg_pre_relax', 'binocular_mg_pyramid_factor', 'binocular_mg_smoothness', 'binocular_mg_solver', 'binocular_ms_consistency_check', 'binocular_ms_edge_smoothing', 'binocular_ms_similarity_measure', 'binocular_ms_sub_disparity', 'binocular_ms_surface_smoothing', 'binocular_num_levels', 'binocular_score_thresh', 'binocular_sub_disparity', 'binocular_texture_thresh', 'bounding_box', 'color', 'color_invisible', 'disparity_method', 'max_disparity', 'min_disparity', 'min_thickness', 'persistence', 'point_meshing', 'rectif_interpolation', 'rectif_method', 'resolution', 'smoothing', 'sub_sampling_step', 'surface_tolerance'

**`GenParamValue`** (input_control)  attribute.value-array `→`  (real / integer / string)

Value of the model parameter to be set.

Default:
[]

Suggested values:
-1, -2, -5, 0, 0.3, 0.5, 0.9, 1, 2, 3, 'census_dense', 'census_sparse', 'binocular', 'ncc', 'none', 'sad', 'ssd', 'bilinear', 'viewing_direction', 'geometric', 'false', 'very_accurate', 'accurate', 'fast_accurate', 'fast', 'v', 'w', 'none', 'gauss_seidel', 'multigrid', 'true', 'poisson', 'isosurface', 'interpolation', 'left_right_check', 'full_multigrid', 'binocular_mg', 'binocular_ms', 'smallest_distance', 'mean_by_distance', 'line_of_sight', 'mean_by_line_of_sight', 'median'

**`StereoModelID`** (output_control)  stereo_model `→`  (handle)

Handle of the stereo model.

## Possible Successors

`set_stereo_model_param`,
`set_stereo_model_image_pairs`,
`reconstruct_surface_stereo`,
`reconstruct_points_stereo`

## Module

3D Metrology
