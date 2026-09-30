# CreateDlTransformNormalize (Operator)

## Name

`CreateDlTransformNormalize` — Create a normalize transform.

## Signature

`static void HOperatorSet.CreateDlTransformNormalize(HTuple transformName, HTuple mean, HTuple deviation, HTuple genParamName, HTuple genParamValue, out HTuple normalize)`

`public HDlTransform(string transformName, HTuple mean, HTuple deviation, HTuple genParamName, HTuple genParamValue)`

`void HDlTransform.CreateDlTransformNormalize(string transformName, HTuple mean, HTuple deviation, HTuple genParamName, HTuple genParamValue)`

## Description

The operator `CreateDlTransformNormalize` creates a normalization
transform and returns the transform handle in *`normalize`*.

The parameter *`transformName`* specifies a unique, non-empty name
for the transform. Note that when creating a transform pipeline using
[`CreateDlTransformPipeline`](create_dl_transform_pipeline.md), each transform within the pipeline
must have a unique name.

The parameters *`mean`* and *`deviation`* will normalize each
channel by
output := (input - *`mean`*) / *`deviation`*.

No generic parameters *`genParamName`* and *`genParamValue`* are
supported for this transform. Only the value *[]* can be set.

The following parameters are specific to the transforms of type
*"normalize"*. They can respectively be get or set using the
operators [`GetDlTransformPipelineParam`](get_dl_transform_pipeline_param.md) and
[`SetDlTransformPipelineParam`](set_dl_transform_pipeline_param.md):

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

**`transformName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the output transform.

Default:
"normalize"

**`mean`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double* / int / long)

Mean.

Default:
0.0

**`deviation`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double* / int / long)

Deviation.

Default:
255.0

**`genParamName`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

Generic input parameter names.

Default:
[]

**`genParamValue`** (input_control)  attribute.value-array `→` [HTuple](HTuple.md) (*string* / double / int / long)

Generic input parameter values.

Default:
[]

**`normalize`** (output_control)  dl_transform `→` [HDlTransform](HDlTransform.md), [HTuple](HTuple.md) (*IntPtr*)

Normalize transform.

## Possible Successors

`CreateDlTransformPipeline`

## Module

Foundation
