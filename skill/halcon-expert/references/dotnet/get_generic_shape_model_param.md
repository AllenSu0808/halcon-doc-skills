# GetGenericShapeModelParam (Operator)

## Name

`GetGenericShapeModelParam` — Return the parameters of a shape model.

## Signature

`static void HOperatorSet.GetGenericShapeModelParam(HTuple modelID, HTuple genParamName, out HTuple genParamValue)`

`HTuple HShapeModel.GetGenericShapeModelParam(HTuple genParamName)`

## Description

The operator `GetGenericShapeModelParam` returns the parameters
values *`genParamValue`* of *`genParamName`* for the shape model
*`modelID`*.

For an explanation of the settable *`genParamValue`*, see
[`SetGenericShapeModelParam`](set_generic_shape_model_param.md).
Additional parameters whose value can only be retrieved:

- *"has_samples"*:

  States, whether the model contains training samples for sample-based
  training (*"true"*) or not (*"false"*).
- *"needs_training"*:

  States, whether the model must be
  trained using [`TrainGenericShapeModel`](train_generic_shape_model.md) before it can be used by
  [`FindGenericShapeModel`](find_generic_shape_model.md) (*"true"*) or not
  (*"false"*).
- *"sample_based_training_compatible"*:

  States, whether the model is compatible with the selected
  sample-based training methods (*"true"*) or not (*"false"*).
  Selected methods for the sample-based training are set using
  *"sample_based_training"* and retrievable using
  *"sample_based_training_param"*.

  In order to accomplish a successful sample-based training, the model
  needs to be compatible and contain training samples.
- *"scale_type"*:

  A string which describes the type of scaling of the shape model.
- *"score_visualization_enabled"*:

  States, whether the set parameters are compatible for
  *"score_visualization"* and therewith the calculation
  of the score contribution of each model point is possible
  (*"true"*) or not (*"false"*).

The operator `GetGenericShapeModelParam` returns the value as it is
used by the shape model.
As certain parameters may be modified after calling
[`TrainGenericShapeModel`](train_generic_shape_model.md), their value can differ from the set value.
This applies particularly to parameters whose value is to be determined
automatically, e.g., with values set to *"auto"*.
The (unmodified) set value of a *`genParamName`* can be retrieved by
adding the suffix *'_param'* to its name.

*Example:* After calling [`TrainGenericShapeModel`](train_generic_shape_model.md),
*"num_levels"* returns the estimated value
and *"num_levels_param"* returns the set value, e.g., its value
set by default or the one set by the user.

Exceptions to this rule are:

- *"greediness"* when *"sample_based_training"* is
  set to *"per_level"*.
- *"min_score"* when *"sample_based_training"* is
  set to *"per_level"*.

A parameter *`genParamName`* for which the resulting
*`genParamValue`* can consist of more than a single value,
for example a transformation matrix, cannot be queried together with other
parameters. Instead, it requires a separate call to
`GetGenericShapeModelParam`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- modelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`modelID`** (input_control, state is modified)  shape_model `→` [HShapeModel](HShapeModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the shape model.

**`genParamName`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

Parameter name.

Default:
"min_score"

List of values:
"angle_end", "angle_start", "angle_step", "border_shape_models", "clutter_border_mode", "clutter_contrast", "clutter_hom_mat_2d", "contour_pruning_threshold", "contrast_high", "contrast_low", "greediness", "has_samples", "iso_scale_max", "iso_scale_min", "iso_scale_step", "max_clutter", "max_deformation", "max_overlap", "max_overlap_global_enable", "metric", "min_contrast", "min_score", "min_size", "model_cache", "model_identifier", "needs_training", "num_levels", "num_matches", "num_matches_global_enable", "optimization", "origin_column", "origin_row", "prepare_clutter_region_for_visualization", "prepare_contours_for_visualization", "pyramid_level_highest", "pyramid_level_lowest", "pyramid_level_robust_tracking", "restrict_iso_scale_max", "restrict_iso_scale_min", "restrict_scale_column_max", "restrict_scale_column_min", "restrict_scale_row_max", "restrict_scale_row_min", "sample_based_training", "sample_based_training_compatible", "scale_column_max", "scale_column_min", "scale_column_step", "scale_row_max", "scale_row_min", "scale_row_step", "scale_type", "score_visualization", "score_visualization_enabled", "strict_boundaries", "subpixel", "time_measurement", "timeout", "use_clutter"

**`genParamValue`** (output_control)  attribute.value-array `→` [HTuple](HTuple.md) (*double* / int / long / string)

Parameter value.

## Result

If the parameters are valid, the operator
`GetGenericShapeModelParam` returns the value 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`CreateGenericShapeModel`,
`SetGenericShapeModelParam`,
`TrainGenericShapeModel`

## Module

Matching
