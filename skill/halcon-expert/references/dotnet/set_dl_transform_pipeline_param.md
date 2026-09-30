# SetDlTransformPipelineParam (Operator)

## Name

`SetDlTransformPipelineParam` — Set parameter values for a given transform in the transform pipeline,
or for the transform pipeline itself.

## Signature

`static void HOperatorSet.SetDlTransformPipelineParam(HTuple transformPipeline, HTuple transformName, HTuple paramName, HTuple paramValue)`

`static void HDlTransform.SetDlTransformPipelineParam(HDlTransformPipeline transformPipeline, string transformName, string paramName, HTuple paramValue)`

`static void HDlTransform.SetDlTransformPipelineParam(HDlTransformPipeline transformPipeline, string transformName, string paramName, int paramValue)`

`void HDlTransformPipeline.SetDlTransformPipelineParam(string transformName, string paramName, HTuple paramValue)`

`void HDlTransformPipeline.SetDlTransformPipelineParam(string transformName, string paramName, int paramValue)`

## Description

The operator `SetDlTransformPipelineParam` sets the value
*`paramValue`* of the parameter *`paramName`* for the transform
*`transformName`* in the transform pipeline *`transformPipeline`*.

The operator can also be used to set parameters of the transform pipeline
*`transformPipeline`* itself, if *`transformName`* is set to
*""*.

The transform names can be retrieved using
[`GetDlTransformPipelineParam`](get_dl_transform_pipeline_param.md) with the parameter
*"transform_names"*.

Which parameters are gettable and settable is described in the operator
reference of [`GetDlTransformPipelineParam`](get_dl_transform_pipeline_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`transformPipeline`** (input_control)  dl_transform_pipeline `→` [HDlTransformPipeline](HDlTransformPipeline.md), [HTuple](HTuple.md) (*IntPtr*)

Transform pipeline handle

**`transformName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the target transform.

Default:
""

**`paramName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the parameter to set.

Default:
"fill_value"

List of values:
"alignment", "bbox_min_side_length", "class_ids_no_orientation", "clip_size", "direction", "fill_value", "height", "ignore_direction", "image_dimensions", "instance_min_visibility", "interpolation", "method", "name", "probability", "range_h", "range_perspective", "range_rot", "range_s", "range_scale", "range_shear", "range_strength", "range_trans", "range_v", "width", "zoom_type"

**`paramValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Value of the parameter.

Default:
[]

List of values:
[512,512,3], 0.0, 0.5, 1.0, "fill", "resize"

## Possible Predecessors

`CreateDlTransformPipeline`

## See also

`GetDlTransformPipelineParam`,
`TransformDlSampleBatch`

## Module

Foundation
