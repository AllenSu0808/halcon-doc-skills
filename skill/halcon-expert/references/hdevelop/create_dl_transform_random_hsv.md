# create_dl_transform_random_hsv (Operator)

## Name

`create_dl_transform_random_hsv` — Create a random HSV transform.

## Signature

`create_dl_transform_random_hsv( : : TransformName, Probability, RangeH, RangeS, RangeV, GenParamName, GenParamValue : RandomHSV)`

## Description

The operator `create_dl_transform_random_hsv` creates a random HSV
transform and returns the transform handle in *`RandomHSV`*. The
transform performs a random shift of the hue, saturation, and value channels
of the input image.

The parameter *`TransformName`* specifies a unique, non-empty name
for the transform. Note that when creating a transform pipeline using
[`create_dl_transform_pipeline`](create_dl_transform_pipeline.md), each transform within the pipeline
must have a unique name.

The parameter *`Probability`* specifies the probability with which the
transform is executed in the pipeline. The probability must be between
*0.0* and *1.0*. A value of *0.0* disables execution,
while a value of *1.0* guarantees that the operation is executed.

The parameters *`RangeH`*, *`RangeS`* and *`RangeV`*
define the ranges for the random shift on the hue, saturation and value
channels of the input image. The ranges are tuples of the form
*[range_min, range_max]*, where *'range_min'* and
*'range_max'* must be between *-1.0* and *1.0*.

No generic parameters *`GenParamName`* and *`GenParamValue`* are
supported for this transform. Only the value *[]* can be set.

The following parameters are specific to the transforms of type
*'random_hsv'*. They can respectively be get or set using the
operators [`get_dl_transform_pipeline_param`](get_dl_transform_pipeline_param.md) and
[`set_dl_transform_pipeline_param`](set_dl_transform_pipeline_param.md):

| ParamName | `set` | `get` |
| --- | --- | --- |
| *'range_h'* | `x` | `x` |
| *'range_s'* | `x` | `x` |
| *'range_v'* | `x` | `x` |
|  |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`TransformName`** (input_control)  string `→`  (string)

Name of the output transform.

Default:
'random_hsv'

**`Probability`** (input_control)  real `→`  (real)

Probability to execute the transform

Default:
1.0

**`RangeH`** (input_control)  real-array `→`  (real)

Tuple with random shift range for the hue channel

Default:
[-0.5,0.5]

**`RangeS`** (input_control)  real-array `→`  (real)

Tuple with random shift range for the saturation channel

Default:
[-0.5,0.5]

**`RangeV`** (input_control)  real-array `→`  (real)

Tuple with random shift range for the value channel

Default:
[-0.5,0.5]

**`GenParamName`** (input_control)  attribute.name-array `→`  (string)

Generic input parameter names.

Default:
[]

List of values:
[]

**`GenParamValue`** (input_control)  attribute.value-array `→`  (string / real / integer)

Generic input parameter values.

Default:
[]

Suggested values:
[]

**`RandomHSV`** (output_control)  dl_transform `→`  (handle)

Random HSV transform

## Possible Successors

`create_dl_transform_pipeline`

## See also

`create_dl_transform_blur`,
`create_dl_transform_normalize`,
`create_dl_transform_random_crop`,
`create_dl_transform_resize`

## Module

Foundation
