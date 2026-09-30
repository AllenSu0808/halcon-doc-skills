# create_dl_transform_random_crop (Operator)

## Name

`create_dl_transform_random_crop` — Create a random crop transform.

## Signature

`create_dl_transform_random_crop( : : TransformName, Probability, Width, Height, GenParamName, GenParamValue : RandomCrop)`

## Description

The operator `create_dl_transform_random_crop` creates a random crop
transform and returns the transform handle in *`RandomCrop`*. The
transform creates a crop of size *`Width`* x *`Height`* at a random
position on the input image.

The parameter *`TransformName`* specifies a unique, non-empty name
for the transform. Note that when creating a transform pipeline using
[`create_dl_transform_pipeline`](create_dl_transform_pipeline.md), each transform within the pipeline
must have a unique name.

The parameter *`Probability`* specifies the probability with which the
transform is executed in the pipeline. The probability must be between
*0.0* and *1.0*. A value of *0.0* disables execution,
while a value of *1.0* guarantees that the operation is executed.

The parameters *`Width`* and *`Height`* specify the dimensions of
the crop.

No generic parameters *`GenParamName`* and *`GenParamValue`* are
supported for this transform. Only the value *[]* can be set.

The following parameters are specific to the transforms of type
*'random_crop'*. They can respectively be get or set using the
operators [`get_dl_transform_pipeline_param`](get_dl_transform_pipeline_param.md) and
[`set_dl_transform_pipeline_param`](set_dl_transform_pipeline_param.md):

| ParamName | `set` | `get` |
| --- | --- | --- |
| *'width'* | `x` | `x` |
| *'height'* | `x` | `x` |
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
'random_crop'

**`Probability`** (input_control)  real `→`  (real)

Probability to execute the transform

Default:
1.0

**`Width`** (input_control)  integer `→`  (integer)

Crop width

Default:
64

**`Height`** (input_control)  integer `→`  (integer)

Crop height

Default:
64

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

**`RandomCrop`** (output_control)  dl_transform `→`  (handle)

Random crop transform

## Possible Successors

`create_dl_transform_pipeline`

## See also

`create_dl_transform_blur`,
`create_dl_transform_normalize`,
`create_dl_transform_random_hsv`,
`create_dl_transform_resize`

## Module

Foundation
