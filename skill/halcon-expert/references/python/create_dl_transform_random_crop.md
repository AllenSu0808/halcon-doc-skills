# create_dl_transform_random_crop (Operator)

## Name

`create_dl_transform_random_crop` — Create a random crop transform.

## Signature

`def create_dl_transform_random_crop(transform_name: str, probability: float, width: int, height: int, gen_param_name: Sequence[str], gen_param_value: Sequence[Union[str, float, int]]) -> HHandle`

## Description

The operator `create_dl_transform_random_crop` creates a random crop
transform and returns the transform handle in *`random_crop`*. The
transform creates a crop of size *`width`* x *`height`* at a random
position on the input image.

The parameter *`transform_name`* specifies a unique, non-empty name
for the transform. Note that when creating a transform pipeline using
[`create_dl_transform_pipeline`](create_dl_transform_pipeline.md), each transform within the pipeline
must have a unique name.

The parameter *`probability`* specifies the probability with which the
transform is executed in the pipeline. The probability must be between
*0.0* and *1.0*. A value of *0.0* disables execution,
while a value of *1.0* guarantees that the operation is executed.

The parameters *`width`* and *`height`* specify the dimensions of
the crop.

No generic parameters *`gen_param_name`* and *`gen_param_value`* are
supported for this transform. Only the value *[]* can be set.

The following parameters are specific to the transforms of type
*"random_crop"*. They can respectively be get or set using the
operators [`get_dl_transform_pipeline_param`](get_dl_transform_pipeline_param.md) and
[`set_dl_transform_pipeline_param`](set_dl_transform_pipeline_param.md):

| ParamName | `set` | `get` |
| --- | --- | --- |
| *"width"* | `x` | `x` |
| *"height"* | `x` | `x` |
|  |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`transform_name`** (input_control)  string `→` str

Name of the output transform.

Default:
"random_crop"

**`probability`** (input_control)  real `→` float

Probability to execute the transform

Default:
1.0

**`width`** (input_control)  integer `→` int

Crop width

Default:
64

**`height`** (input_control)  integer `→` int

Crop height

Default:
64

**`gen_param_name`** (input_control)  attribute.name-array `→` Sequence[str]

Generic input parameter names.

Default:
[]

List of values:
[]

**`gen_param_value`** (input_control)  attribute.value-array `→` Sequence[Union[str, float, int]]

Generic input parameter values.

Default:
[]

Suggested values:
[]

**`random_crop`** (output_control)  dl_transform `→` HHandle

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
