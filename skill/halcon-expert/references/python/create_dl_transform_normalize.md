# create_dl_transform_normalize (Operator)

## Name

`create_dl_transform_normalize` — Create a normalize transform.

## Signature

`def create_dl_transform_normalize(transform_name: str, mean: Sequence[Union[float, int]], deviation: Sequence[Union[float, int]], gen_param_name: Sequence[str], gen_param_value: Sequence[Union[str, float, int]]) -> HHandle`

## Description

The operator `create_dl_transform_normalize` creates a normalization
transform and returns the transform handle in *`normalize`*.

The parameter *`transform_name`* specifies a unique, non-empty name
for the transform. Note that when creating a transform pipeline using
[`create_dl_transform_pipeline`](create_dl_transform_pipeline.md), each transform within the pipeline
must have a unique name.

The parameters *`mean`* and *`deviation`* will normalize each
channel by
output := (input - *`mean`*) / *`deviation`*.

No generic parameters *`gen_param_name`* and *`gen_param_value`* are
supported for this transform. Only the value *[]* can be set.

The following parameters are specific to the transforms of type
*"normalize"*. They can respectively be get or set using the
operators [`get_dl_transform_pipeline_param`](get_dl_transform_pipeline_param.md) and
[`set_dl_transform_pipeline_param`](set_dl_transform_pipeline_param.md):

| ParamName | `set` | `get` |
| --- | --- | --- |
| *"mean"* | `x` | `x` |
| *"deviation"* | `x` | `x` |
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
"normalize"

**`mean`** (input_control)  real-array `→` Sequence[Union[float, int]]

Mean.

Default:
0.0

**`deviation`** (input_control)  real-array `→` Sequence[Union[float, int]]

Deviation.

Default:
255.0

**`gen_param_name`** (input_control)  attribute.name-array `→` Sequence[str]

Generic input parameter names.

Default:
[]

**`gen_param_value`** (input_control)  attribute.value-array `→` Sequence[Union[str, float, int]]

Generic input parameter values.

Default:
[]

**`normalize`** (output_control)  dl_transform `→` HHandle

Normalize transform.

## Possible Successors

`create_dl_transform_pipeline`

## Module

Foundation
