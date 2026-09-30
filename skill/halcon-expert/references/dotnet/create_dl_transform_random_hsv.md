# CreateDlTransformRandomHsv (Operator)

## Name

`CreateDlTransformRandomHsv` — Create a random HSV transform.

## Signature

`static void HOperatorSet.CreateDlTransformRandomHsv(HTuple transformName, HTuple probability, HTuple rangeH, HTuple rangeS, HTuple rangeV, HTuple genParamName, HTuple genParamValue, out HTuple randomHSV)`

`public HDlTransform(string transformName, double probability, HTuple rangeH, HTuple rangeS, HTuple rangeV, HTuple genParamName, HTuple genParamValue)`

`void HDlTransform.CreateDlTransformRandomHsv(string transformName, double probability, HTuple rangeH, HTuple rangeS, HTuple rangeV, HTuple genParamName, HTuple genParamValue)`

## Description

The operator `CreateDlTransformRandomHsv` creates a random HSV
transform and returns the transform handle in *`randomHSV`*. The
transform performs a random shift of the hue, saturation, and value channels
of the input image.

The parameter *`transformName`* specifies a unique, non-empty name
for the transform. Note that when creating a transform pipeline using
[`CreateDlTransformPipeline`](create_dl_transform_pipeline.md), each transform within the pipeline
must have a unique name.

The parameter *`probability`* specifies the probability with which the
transform is executed in the pipeline. The probability must be between
*0.0* and *1.0*. A value of *0.0* disables execution,
while a value of *1.0* guarantees that the operation is executed.

The parameters *`rangeH`*, *`rangeS`* and *`rangeV`*
define the ranges for the random shift on the hue, saturation and value
channels of the input image. The ranges are tuples of the form
*[range_min, range_max]*, where *"range_min"* and
*"range_max"* must be between *-1.0* and *1.0*.

No generic parameters *`genParamName`* and *`genParamValue`* are
supported for this transform. Only the value *[]* can be set.

The following parameters are specific to the transforms of type
*"random_hsv"*. They can respectively be get or set using the
operators [`GetDlTransformPipelineParam`](get_dl_transform_pipeline_param.md) and
[`SetDlTransformPipelineParam`](set_dl_transform_pipeline_param.md):

| ParamName | `set` | `get` |
| --- | --- | --- |
| *"range_h"* | `x` | `x` |
| *"range_s"* | `x` | `x` |
| *"range_v"* | `x` | `x` |
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
"random_hsv"

**`probability`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Probability to execute the transform

Default:
1.0

**`rangeH`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Tuple with random shift range for the hue channel

Default:
[-0.5,0.5]

**`rangeS`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Tuple with random shift range for the saturation channel

Default:
[-0.5,0.5]

**`rangeV`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Tuple with random shift range for the value channel

Default:
[-0.5,0.5]

**`genParamName`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

Generic input parameter names.

Default:
[]

List of values:
[]

**`genParamValue`** (input_control)  attribute.value-array `→` [HTuple](HTuple.md) (*string* / double / int / long)

Generic input parameter values.

Default:
[]

Suggested values:
[]

**`randomHSV`** (output_control)  dl_transform `→` [HDlTransform](HDlTransform.md), [HTuple](HTuple.md) (*IntPtr*)

Random HSV transform

## Possible Successors

`CreateDlTransformPipeline`

## See also

`CreateDlTransformBlur`,
`CreateDlTransformNormalize`,
`CreateDlTransformRandomCrop`,
`CreateDlTransformResize`

## Module

Foundation
