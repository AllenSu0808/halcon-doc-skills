# create_dl_transform_normalize (Operator)

## Name

`create_dl_transform_normalize` — Create a normalize transform.

## Signature

`create_dl_transform_normalize( : : TransformName, Mean, Deviation, GenParamName, GenParamValue : Normalize)`

## Description

The operator `create_dl_transform_normalize` creates a normalization
transform and returns the transform handle in *`Normalize`*.

The parameter *`TransformName`* specifies a unique, non-empty name
for the transform. Note that when creating a transform pipeline using
[`create_dl_transform_pipeline`](create_dl_transform_pipeline.md), each transform within the pipeline
must have a unique name.

The parameters *`Mean`* and *`Deviation`* will normalize each
channel by
output := (input - *`Mean`*) / *`Deviation`*.

No generic parameters *`GenParamName`* and *`GenParamValue`* are
supported for this transform. Only the value *[]* can be set.

The following parameters are specific to the transforms of type
*'normalize'*. They can respectively be get or set using the
operators [`get_dl_transform_pipeline_param`](get_dl_transform_pipeline_param.md) and
[`set_dl_transform_pipeline_param`](set_dl_transform_pipeline_param.md):

| ParamName | `set` | `get` |
| --- | --- | --- |
| *'mean'* | `x` | `x` |
| *'deviation'* | `x` | `x` |
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
'normalize'

**`Mean`** (input_control)  real-array `→`  (real / integer)

Mean.

Default:
0.0

**`Deviation`** (input_control)  real-array `→`  (real / integer)

Deviation.

Default:
255.0

**`GenParamName`** (input_control)  attribute.name-array `→`  (string)

Generic input parameter names.

Default:
[]

**`GenParamValue`** (input_control)  attribute.value-array `→`  (string / real / integer)

Generic input parameter values.

Default:
[]

**`Normalize`** (output_control)  dl_transform `→`  (handle)

Normalize transform.

## Possible Successors

`create_dl_transform_pipeline`

## Module

Foundation
