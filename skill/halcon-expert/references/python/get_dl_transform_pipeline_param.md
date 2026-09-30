# get_dl_transform_pipeline_param (Operator)

## Name

`get_dl_transform_pipeline_param` — Retrieve parameter values for a given transform in the transform pipeline,
or for the transform pipeline itself.

## Signature

`def get_dl_transform_pipeline_param(transform_pipeline: HHandle, transform_name: str, param_name: str) -> Sequence[Union[str, float, int]]`

`def get_dl_transform_pipeline_param_s(transform_pipeline: HHandle, transform_name: str, param_name: str) -> Union[str, float, int]`

## Description

The operator `get_dl_transform_pipeline_param` returns the value of
the parameter *`param_name`* in *`param_value`* for the transform
*`transform_name`* in the transform pipeline *`transform_pipeline`*.

The operator can also be used to return parameters of the transform pipeline
*`transform_pipeline`* itself, if *`transform_name`* is set to
*""*.

The transform names can be retrieved using
`get_dl_transform_pipeline_param` with the parameter
*"transform_names"*.

General parameters of a transform pipeline:

| *`param_name`* | `set` | `get` |
| --- | --- | --- |
| *"fill_value"* | `x` | `x` |
| *"num_additional_samples"* |  | `x` |
| *"transform_names"* |  | `x` |
| *"ignore_direction"* | `x` | `x` |
| *"class_ids_no_orientation"* | `x` | `x` |
| *"bbox_min_side_length"* | `x` | `x` |
| *"instance_min_visibility"* | `x` | `x` |

- ***"fill_value"*:** —

  Value used to fill padded regions if required by the transforms.

  Restriction:
   Only values of type integer or float are allowed.

  Default:
   *0.0*
- ***"num_additional_samples"*:** —

  Total number of additional samples required by all transforms in the
  pipeline.
- ***"transform_names"*:** —

  Names of the transforms contained in the pipeline.
- ***"ignore_direction"*:** —

  Determines whether directions of oriented bounding boxes shall be
  used (*"false"*) or ignored (*"true"*).
  Only for transformation of samples for detection models of
  *"instance_type"* = *"rectangle2"*.

  List of values:
   *"true"*, *"false"*

  Default:
   *"false"*
- ***"class_ids_no_orientation"*:** —

  Array containing all class IDs that have no orientation,
  e.g., round or other point symmetrical objects. The labels
  are replaced by the smallest enclosing axis-aligned bounding boxes.
  Only for transformation of samples for detection models of
  *"instance_type"* = *"rectangle2"*.

  Default:
   *"class_ids_no_orientation"* = *[]*
- ***"bbox_min_side_length"*:** —

  Minimum allowed side length of a transformed box instance. Smaller
  box instances are not transferred to output.

  Default:
   *2*
- ***"instance_min_visibility"*:** —

  Minimum allowed visibility fraction of a transformed instance.
  Instances with lower visibility are not transferred to output.

  Default:
   *0.5*

Parameters common to each transform:

| *`param_name`* | `set` | `get` |
| --- | --- | --- |
| *"name"* | `x` | `x` |
| *"num_additional_samples"* |  | `x` |
| *"probability"* | `x` | `x` |
| *"type"* |  | `x` |

- ***"name"*:** —

  Name of the transform.
- ***"num_additional_samples"*:** —

  Number of additional samples required by the transform.
- ***"probability"*:** —

  Probability with which the transform is executed.

  Restriction:
   Not settable for transforms of type
  *"resize"*.
- ***"type"*:** —

  Type of the transform.

The parameters that are gettable and settable for a specific transform are
described in the corresponding operator reference of the respective
transform (`create_dl_transform_*`).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`transform_pipeline`** (input_control)  dl_transform_pipeline `→` HHandle

Transform pipeline handle

**`transform_name`** (input_control)  string `→` str

Name of the target transform.

Default:
""

**`param_name`** (input_control)  string `→` str

Name of the parameter to query.

Default:
"transform_names"

List of values:
"alignment", "bbox_min_side_length", "class_ids_no_orientation", "clip_size", "deviation", "direction", "fill_value", "height", "ignore_direction", "image_dimensions", "instance_min_visibility", "interpolation", "mean", "method", "name", "num_additional_samples", "probability", "range_h", "range_perspective", "range_rot", "range_s", "range_scale", "range_shear", "range_strength", "range_trans", "range_v", "transform_names", "type", "width", "zoom_type"

**`param_value`** (output_control)  tuple(-array) `→` Sequence[Union[str, float, int]]

Value of the parameter.

## Possible Predecessors

`create_dl_transform_pipeline`

## See also

`set_dl_transform_pipeline_param`,
`transform_dl_sample_batch`

## Module

Foundation
