# create_dl_transform_flip (Operator)

## Name

`create_dl_transform_flip` — Create a flip transform.

## Signature

`def create_dl_transform_flip(transform_name: str, probability: float, direction: str, gen_param_name: Sequence[str], gen_param_value: Sequence[Union[str, float, int]]) -> HHandle`

## Description

The operator `create_dl_transform_flip` creates a flip
transform and returns the transform handle in *`flip`*.
The transform performs a flip of the input image in horizontal or vertical
direction.

The parameter *`transform_name`* specifies a unique, non-empty name
for the transform. Note that when creating a transform pipeline using
[`create_dl_transform_pipeline`](create_dl_transform_pipeline.md), each transform within the pipeline
must have a unique name.

The parameter *`probability`* specifies the probability with which the
transform is executed in the pipeline. The probability must be between
*0.0* and *1.0*. A value of *0.0* disables execution,
while a value of *1.0* guarantees that the operation is executed.

The parameter *`direction`* defines in which direction the input image
is flipped. The flip direction can be *"horizontal"* or
*"vertical"*.

No generic parameters *`gen_param_name`* and *`gen_param_value`* are
supported for this transform. Only the value *[]* can be set.

The following parameters are specific to the transforms of type
*"flip"*. They can respectively be get or set using the
operators [`get_dl_transform_pipeline_param`](get_dl_transform_pipeline_param.md) and
[`set_dl_transform_pipeline_param`](set_dl_transform_pipeline_param.md):

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

**`transform_name`** (input_control)  string `→` str

Name of the output transform.

Default:
"flip"

**`probability`** (input_control)  real `→` float

Probability to execute the transform

Default:
1.0

**`direction`** (input_control)  string `→` str

Flip direction.

Default:
"horizontal"

List of values:
"horizontal", "vertical"

**`gen_param_name`** (input_control)  attribute.name-array `→` Sequence[str]

Generic input parameter names.

Default:
[]

**`gen_param_value`** (input_control)  attribute.value-array `→` Sequence[Union[str, float, int]]

Generic input parameter values.

Default:
[]

**`flip`** (output_control)  dl_transform `→` HHandle

Flip transform.

## Possible Successors

`create_dl_transform_pipeline`

## See also

`create_dl_transform_random_hsv`,
`create_dl_transform_random_crop`,
`transform_dl_sample_batch`

## Module

Foundation
