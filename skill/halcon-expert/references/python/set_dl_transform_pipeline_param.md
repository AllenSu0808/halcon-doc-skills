# set_dl_transform_pipeline_param (Operator)

## Name

`set_dl_transform_pipeline_param` — Set parameter values for a given transform in the transform pipeline,
or for the transform pipeline itself.

## Signature

`def set_dl_transform_pipeline_param(transform_pipeline: HHandle, transform_name: str, param_name: str, param_value: MaybeSequence[Union[int, float, str]]) -> None`

## Description

The operator `set_dl_transform_pipeline_param` sets the value
*`param_value`* of the parameter *`param_name`* for the transform
*`transform_name`* in the transform pipeline *`transform_pipeline`*.

The operator can also be used to set parameters of the transform pipeline
*`transform_pipeline`* itself, if *`transform_name`* is set to
*""*.

The transform names can be retrieved using
[`get_dl_transform_pipeline_param`](get_dl_transform_pipeline_param.md) with the parameter
*"transform_names"*.

Which parameters are gettable and settable is described in the operator
reference of [`get_dl_transform_pipeline_param`](get_dl_transform_pipeline_param.md).

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

Name of the parameter to set.

Default:
"fill_value"

List of values:
"alignment", "bbox_min_side_length", "class_ids_no_orientation", "clip_size", "direction", "fill_value", "height", "ignore_direction", "image_dimensions", "instance_min_visibility", "interpolation", "method", "name", "probability", "range_h", "range_perspective", "range_rot", "range_s", "range_scale", "range_shear", "range_strength", "range_trans", "range_v", "width", "zoom_type"

**`param_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[int, float, str]]

Value of the parameter.

Default:
[]

List of values:
[512,512,3], 0.0, 0.5, 1.0, "fill", "resize"

## Possible Predecessors

`create_dl_transform_pipeline`

## See also

`get_dl_transform_pipeline_param`,
`transform_dl_sample_batch`

## Module

Foundation
