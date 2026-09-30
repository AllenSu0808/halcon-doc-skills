# CreateDlTransformBlur (Operator)

## Name

`CreateDlTransformBlur` — Create a blur transform.

## Signature

`static void HOperatorSet.CreateDlTransformBlur(HTuple transformName, HTuple probability, HTuple method, HTuple rangeStrength, HTuple genParamName, HTuple genParamValue, out HTuple blur)`

`public HDlTransform(string transformName, double probability, string method, HTuple rangeStrength, HTuple genParamName, HTuple genParamValue)`

`void HDlTransform.CreateDlTransformBlur(string transformName, double probability, string method, HTuple rangeStrength, HTuple genParamName, HTuple genParamValue)`

## Description

The operator `CreateDlTransformBlur` creates a blur transform and
returns the transform handle in *`blur`*.

The parameter *`transformName`* specifies a unique, non-empty name
for the transform. Note that when creating a transform pipeline using
[`CreateDlTransformPipeline`](create_dl_transform_pipeline.md), each transform within the pipeline
must have a unique name.

The parameter *`probability`* specifies the probability with which the
transform is executed in the pipeline. The probability must be between
*0.0* and *1.0*. A value of *0.0* disables execution,
while a value of *1.0* guarantees that the operation is executed.

The parameter *`method`* defines the method used for the blur effect.
Currently, the method *"gaussian"* is supported.

The parameter *`rangeStrength`* defines the range for the strength of
the blur effect. The range is a tuple of the form
*[range_min, range_max]*, where *"range_min"* and
*"range_max"* must be between *0.0* and *10.0*.

No generic parameters *`genParamName`* and *`genParamValue`* are
supported for this transform. Only the value *[]* can be set.

The following parameters are specific to the transforms of type
*"blur"*. They can respectively be get or set using the
operators [`GetDlTransformPipelineParam`](get_dl_transform_pipeline_param.md) and
[`SetDlTransformPipelineParam`](set_dl_transform_pipeline_param.md):

| ParamName | `set` | `get` |
| --- | --- | --- |
| *"method"* | `x` | `x` |
| *"range_strength"* | `x` | `x` |
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
"blur"

**`probability`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Probability to execute the transform

Default:
1.0

**`method`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

The blur method to use

Default:
"gaussian"

**`rangeStrength`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Tuple with range of strength values to draw from

Default:
[1.0,5.0]

**`genParamName`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

Generic input parameter names.

Default:
[]

**`genParamValue`** (input_control)  attribute.value-array `→` [HTuple](HTuple.md) (*string* / double / int / long)

Generic input parameter values.

Default:
[]

**`blur`** (output_control)  dl_transform `→` [HDlTransform](HDlTransform.md), [HTuple](HTuple.md) (*IntPtr*)

Blur transform

## Possible Successors

`CreateDlTransformPipeline`

## See also

`CreateDlTransformNormalize`,
`CreateDlTransformRandomCrop`,
`CreateDlTransformRandomHsv`,
`CreateDlTransformResize`

## Module

Foundation
