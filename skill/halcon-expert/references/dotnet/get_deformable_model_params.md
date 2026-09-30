# GetDeformableModelParams (Operator)

## Name

`GetDeformableModelParams` — Return the parameters of a deformable model.

## Signature

`static void HOperatorSet.GetDeformableModelParams(HTuple modelID, HTuple genParamName, out HTuple genParamValue)`

`HTuple HDeformableModel.GetDeformableModelParams(HTuple genParamName)`

`HTuple HDeformableModel.GetDeformableModelParams(string genParamName)`

## Description

The operator `GetDeformableModelParams` allows to query
parameters of the deformable model. The names of the desired
parameters are passed in the generic parameter
*`genParamName`*, the corresponding values are returned in
*`genParamValue`*.

The following parameters can be queried:

- ***"cam_param"*:** —

  Internal parameters of the camera that is used for the calibrated case.
- ***"cam_param_rect"*:** —

  Rectified internal parameters of the camera that is used for the calibrated
  case.
- ***"reference_pose"*:** —

  Reference position and orientation of the calibrated deformable model. The
  returned pose describes the model plane that the user provided.
- ***"model_pose"*:** —

  Reference position and orientation of the deformable model. The
  returned pose describes the pose of the internally used 3D metric model
  that was used for model generation. The pose refers to the model's center
  of gravity if not explicitly set with [`SetDeformableModelOrigin`](set_deformable_model_origin.md).
- ***"angle_start"*:** —

  The smallest rotation angle of the model.
- ***"angle_extent"*:** —

  The extent of the rotation angle of the model.
- ***"angle_step"*:** —

  The angle step length of the model.
- ***"scale_r_min"*:** —

  The minimum scale of the pattern in row direction.
- ***"scale_r_max"*:** —

  The maximum scale of the pattern in row direction.
- ***"scale_r_step"*:** —

  The scale step of the pattern in row direction.
- ***"scale_c_min"*:** —

  The minimum scale of the pattern in column direction.
- ***"scale_c_max"*:** —

  The maximum scale of the pattern in column direction.
- ***"scale_c_step"*:** —

  The scale step of the pattern in column direction.
- ***"num_levels"*:** —

  User-specified number of pyramid levels.
- ***"optimization"*:** —

  Kind of optimization by reducing the number of model points.
- ***"min_size"*:** —

  Minimum size of the deformable model edge.
- ***"min_contrast"*:** —

  Minimum contrast of the objects in the search images.
- ***"metric"*:** —

  Match metric.
- ***"model_row"*:** —

  Row coordinate of origin in the radial undistorted model image.
- ***"model_col"*:** —

  Column coordinate of origin in the radial undistorted model image.
- ***"model_type"*:** —

  The type of the model: *"planar_uncalib"*, *"planar_calib"*
  or *"local"*.
- ***"created_from_xld"*:** —

  Was the model created from XLD or from an image: *"created_from_xld"*
  or *"created_from_image"*.
- ***"get_deformable_model_contours_coord_system"*:** —

  Coordinate system (*"image"* or *"world"*) in which
  contours are returned when calling the operator
  [`GetDeformableModelContours`](get_deformable_model_contours.md).

A detailed description of the parameters can be looked up with the
operator [`CreatePlanarUncalibDeformableModel`](create_planar_uncalib_deformable_model.md) and
[`CreatePlanarCalibDeformableModel`](create_planar_calib_deformable_model.md) or with the operator
[`GetDeformableModelContours`](get_deformable_model_contours.md).

Note that although the parameter `contrast` can be determined
automatically during the model creation, its value cannot be queried using
`GetDeformableModelParams`.
Instead, the operator [`DetermineDeformableModelParams`](determine_deformable_model_params.md) should be
used to retrieve its value.

It is possible to query the values of several parameters with a
single operator call by passing a tuple containing the names of all
desired parameters to *`genParamName`*. As a result a tuple of
the same length with the corresponding values is returned in
*`genParamValue`*. Note that this is solely possible for
parameters that return only a single value.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`modelID`** (input_control)  deformable_model `→` [HDeformableModel](HDeformableModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters that
are to be queried for the deformable model.

Default:
"angle_start"

List of values:
"angle_extent", "angle_start", "angle_step", "cam_param", "cam_param_rect", "created_from_xld", "get_deformable_model_contours_coord_system", "metric", "min_contrast", "min_size", "model_col", "model_pose", "model_row", "model_type", "num_levels", "optimization", "reference_pose", "scale_c_max", "scale_c_min", "scale_c_step", "scale_r_max", "scale_r_min", "scale_r_step"

**`genParamValue`** (output_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Values of the generic parameters.

## Result

If the parameters are valid, the operator
`GetDeformableModelParams` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`CreatePlanarUncalibDeformableModel`,
`CreatePlanarCalibDeformableModel`,
`CreateLocalDeformableModel`

## Possible Successors

`FindPlanarUncalibDeformableModel`,
`FindPlanarCalibDeformableModel`

## See also

`SetDeformableModelParam`

## Module

Matching
