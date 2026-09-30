# CreateDlTransformFlip (Operator)

## Name

`CreateDlTransformFlip` — Create a flip transform.

## Signature

`static void HOperatorSet.CreateDlTransformFlip(HTuple transformName, HTuple probability, HTuple direction, HTuple genParamName, HTuple genParamValue, out HTuple flip)`

`public HDlTransform(string transformName, double probability, string direction, HTuple genParamName, HTuple genParamValue)`

`void HDlTransform.CreateDlTransformFlip(string transformName, double probability, string direction, HTuple genParamName, HTuple genParamValue)`

## Description

The operator `CreateDlTransformFlip` creates a flip
transform and returns the transform handle in *`flip`*.
The transform performs a flip of the input image in horizontal or vertical
direction.

The parameter *`transformName`* specifies a unique, non-empty name
for the transform. Note that when creating a transform pipeline using
[`CreateDlTransformPipeline`](create_dl_transform_pipeline.md), each transform within the pipeline
must have a unique name.

The parameter *`probability`* specifies the probability with which the
transform is executed in the pipeline. The probability must be between
*0.0* and *1.0*. A value of *0.0* disables execution,
while a value of *1.0* guarantees that the operation is executed.

The parameter *`direction`* defines in which direction the input image
is flipped. The flip direction can be *"horizontal"* or
*"vertical"*.

No generic parameters *`genParamName`* and *`genParamValue`* are
supported for this transform. Only the value *[]* can be set.

The following parameters are specific to the transforms of type
*"flip"*. They can respectively be get or set using the
operators [`GetDlTransformPipelineParam`](get_dl_transform_pipeline_param.md) and
[`SetDlTransformPipelineParam`](set_dl_transform_pipeline_param.md):

| ParamName | `set` | `get` |
| --- | --- | --- |
| *"direction"* | `x` | `x` |
|  |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`transformName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the output transform.

Default:
"flip"

**`probability`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Probability to execute the transform

Default:
1.0

**`direction`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Flip direction.

Default:
"horizontal"

List of values:
"horizontal", "vertical"

**`genParamName`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

Generic input parameter names.

Default:
[]

**`genParamValue`** (input_control)  attribute.value-array `→` [HTuple](HTuple.md) (*string* / double / int / long)

Generic input parameter values.

Default:
[]

**`flip`** (output_control)  dl_transform `→` [HDlTransform](HDlTransform.md), [HTuple](HTuple.md) (*IntPtr*)

Flip transform.

## Possible Successors

`CreateDlTransformPipeline`

## See also

`CreateDlTransformRandomHsv`,
`CreateDlTransformRandomCrop`,
`TransformDlSampleBatch`

## Module

Foundation
