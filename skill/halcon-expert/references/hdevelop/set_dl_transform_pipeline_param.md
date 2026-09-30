# set_dl_transform_pipeline_param (Operator)

## Name

`set_dl_transform_pipeline_param` — Set parameter values for a given transform in the transform pipeline,
or for the transform pipeline itself.

## Signature

`set_dl_transform_pipeline_param( : : TransformPipeline, TransformName, ParamName, ParamValue : )`

## Description

The operator `set_dl_transform_pipeline_param` sets the value
*`ParamValue`* of the parameter *`ParamName`* for the transform
*`TransformName`* in the transform pipeline *`TransformPipeline`*.

The operator can also be used to set parameters of the transform pipeline
*`TransformPipeline`* itself, if *`TransformName`* is set to
*''*.

The transform names can be retrieved using
[`get_dl_transform_pipeline_param`](get_dl_transform_pipeline_param.md) with the parameter
*'transform_names'*.

Which parameters are gettable and settable is described in the operator
reference of [`get_dl_transform_pipeline_param`](get_dl_transform_pipeline_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`TransformPipeline`** (input_control)  dl_transform_pipeline `→`  (handle)

Transform pipeline handle

**`TransformName`** (input_control)  string `→`  (string)

Name of the target transform.

Default:
''

**`ParamName`** (input_control)  string `→`  (string)

Name of the parameter to set.

Default:
'fill_value'

List of values:
'alignment', 'bbox_min_side_length', 'class_ids_no_orientation', 'clip_size', 'direction', 'fill_value', 'height', 'ignore_direction', 'image_dimensions', 'instance_min_visibility', 'interpolation', 'method', 'name', 'probability', 'range_h', 'range_perspective', 'range_rot', 'range_s', 'range_scale', 'range_shear', 'range_strength', 'range_trans', 'range_v', 'width', 'zoom_type'

**`ParamValue`** (input_control)  attribute.value(-array) `→`  (integer / real / string)

Value of the parameter.

Default:
[]

List of values:
[512,512,3], 0.0, 0.5, 1.0, 'fill', 'resize'

## Possible Predecessors

`create_dl_transform_pipeline`

## See also

`get_dl_transform_pipeline_param`,
`transform_dl_sample_batch`

## Module

Foundation
