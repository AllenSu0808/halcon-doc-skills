# CreateDlTransformRandomGeometric (Operator)

## Name

`CreateDlTransformRandomGeometric` — Create a random geometric transform.

## Signature

`static void HOperatorSet.CreateDlTransformRandomGeometric(HTuple transformName, HTuple probability, HTuple rangeScale, HTuple rangeTrans, HTuple rangeRot, HTuple rangeShear, HTuple rangePerspective, HTuple clipSize, HTuple genParamName, HTuple genParamValue, out HTuple randomGeometric)`

`public HDlTransform(string transformName, double probability, HTuple rangeScale, HTuple rangeTrans, HTuple rangeRot, HTuple rangeShear, HTuple rangePerspective, HTuple clipSize, HTuple genParamName, HTuple genParamValue)`

`void HDlTransform.CreateDlTransformRandomGeometric(string transformName, double probability, HTuple rangeScale, HTuple rangeTrans, HTuple rangeRot, HTuple rangeShear, HTuple rangePerspective, HTuple clipSize, HTuple genParamName, HTuple genParamValue)`

## Description

The operator `CreateDlTransformRandomGeometric` creates a random
geometric transform and returns the transform handle in *`randomGeometric`*.
The transform performs a random scaling, translation, rotation, as well as small
shearing or perspective transformations of the centered input image.

The parameter *`transformName`* specifies a unique, non-empty name
for the transform. Note that when creating a transform pipeline using
[`CreateDlTransformPipeline`](create_dl_transform_pipeline.md), each transform within the pipeline
must have a unique name.

The parameter *`probability`* specifies the probability with which the
transform is executed in the pipeline. The probability must be between
*0.0* and *1.0*. A value of *0.0* disables execution,
while a value of *1.0* guarantees that the operation is executed.

The parameters *`rangeScale`*, *`rangeTrans`*,
*`rangeRot`*, *`rangeShear`* and *`rangePerspective`*
define the ranges for the random geometric transformations scaling,
translation, rotation, shearing and perspective of the input image,
respectively. The ranges are tuples of the form
*[range_min, range_max]*, where *"range_min"* and
*"range_max"* must be
between *0.5* and *1.5* relative to the input size
for *`rangeScale`*,
between *-1.0* and *1.0* relative to the output size
for *`rangeTrans`*,
between *-180.0* and *180.0* in degrees for *`rangeRot`*,
between *-10.0* and *10.0* in degrees for *`rangeShear`*,
and a strength between *-0.001* and *0.001* for
*`rangePerspective`*. Set *`rangeScale`* to *[1.0, 1.0]*
to disable scaling, or set *`rangeTrans`*, *`rangeRot`*,
*`rangeShear`* and *`rangePerspective`* to *[0.0, 0.0]*
to disable translation, rotation, shearing and perspective transformation,
respectively.

The parameter *`clipSize`* contains the
output image dimensions `'width'` and `'height'` as a tuple.
Passing *-1* keeps the
corresponding dimension of the input image unchanged. *`rangeTrans`*
shifts the image center by a random fraction of *`clipSize`*.

The following generic parameters *`genParamName`* and the
corresponding values *`genParamValue`* are supported:

- ***"interpolation"*:** —

  Specifies the interpolation mode.
  Currently the modes *"bilinear"* and
  *"nearest_neighbor"* are supported.

  Default:
   *"bilinear"*.

Padding is applied if required, the *"fill_value"*
can be specified using [`SetDlTransformPipelineParam`](set_dl_transform_pipeline_param.md).
Note that for axis-aligned object detection, rotation, shearing and
perspective transformation may cause bounding
boxes to fit less tightly around objects than before the transformation.

The following parameters are specific to the transforms of type
*"random_geometric"*. They can respectively be get or set using the
operators [`GetDlTransformPipelineParam`](get_dl_transform_pipeline_param.md) and
[`SetDlTransformPipelineParam`](set_dl_transform_pipeline_param.md):

| ParamName | `set` | `get` |
| --- | --- | --- |
| *"range_scale"* | `x` | `x` |
| *"range_trans"* | `x` | `x` |
| *"range_rot"* | `x` | `x` |
| *"range_shear"* | `x` | `x` |
| *"range_perspective"* | `x` | `x` |
| *"clip_size"* | `x` | `x` |
| *"interpolation"* | `x` | `x` |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`transformName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the output transform.

Default:
"random_geometric"

**`probability`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Probability to execute the transform.

Default:
1.0

**`rangeScale`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Tuple with random scale range.

Default:
[0.5,1.5]

**`rangeTrans`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Tuple with random translation range.

Default:
[-0.1,0.1]

**`rangeRot`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Tuple with random rotation range.

Default:
[0.0,0.0]

**`rangeShear`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Tuple with random shear range.

Default:
[0.0,0.0]

**`rangePerspective`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Tuple with random perspective range.

Default:
[0.0,0.0]

**`clipSize`** (input_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Tuple containing output image size.

Default:
[-1,-1]

**`genParamName`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

Generic input parameter names.

Default:
[]

List of values:
"interpolation"

**`genParamValue`** (input_control)  attribute.value-array `→` [HTuple](HTuple.md) (*string*)

Generic input parameter values.

Default:
[]

Suggested values:

**`randomGeometric`** (output_control)  dl_transform `→` [HDlTransform](HDlTransform.md), [HTuple](HTuple.md) (*IntPtr*)

Random geometric transform.

## Possible Successors

`CreateDlTransformPipeline`

## See also

`CreateDlTransformRandomHsv`

## Module

Foundation
