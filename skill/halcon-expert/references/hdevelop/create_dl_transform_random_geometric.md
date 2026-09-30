# create_dl_transform_random_geometric (Operator)

## Name

`create_dl_transform_random_geometric` — Create a random geometric transform.

## Signature

`create_dl_transform_random_geometric( : : TransformName, Probability, RangeScale, RangeTrans, RangeRot, RangeShear, RangePerspective, ClipSize, GenParamName, GenParamValue : RandomGeometric)`

## Description

The operator `create_dl_transform_random_geometric` creates a random
geometric transform and returns the transform handle in *`RandomGeometric`*.
The transform performs a random scaling, translation, rotation, as well as small
shearing or perspective transformations of the centered input image.

The parameter *`TransformName`* specifies a unique, non-empty name
for the transform. Note that when creating a transform pipeline using
[`create_dl_transform_pipeline`](create_dl_transform_pipeline.md), each transform within the pipeline
must have a unique name.

The parameter *`Probability`* specifies the probability with which the
transform is executed in the pipeline. The probability must be between
*0.0* and *1.0*. A value of *0.0* disables execution,
while a value of *1.0* guarantees that the operation is executed.

The parameters *`RangeScale`*, *`RangeTrans`*,
*`RangeRot`*, *`RangeShear`* and *`RangePerspective`*
define the ranges for the random geometric transformations scaling,
translation, rotation, shearing and perspective of the input image,
respectively. The ranges are tuples of the form
*[range_min, range_max]*, where *'range_min'* and
*'range_max'* must be
between *0.5* and *1.5* relative to the input size
for *`RangeScale`*,
between *-1.0* and *1.0* relative to the output size
for *`RangeTrans`*,
between *-180.0* and *180.0* in degrees for *`RangeRot`*,
between *-10.0* and *10.0* in degrees for *`RangeShear`*,
and a strength between *-0.001* and *0.001* for
*`RangePerspective`*. Set *`RangeScale`* to *[1.0, 1.0]*
to disable scaling, or set *`RangeTrans`*, *`RangeRot`*,
*`RangeShear`* and *`RangePerspective`* to *[0.0, 0.0]*
to disable translation, rotation, shearing and perspective transformation,
respectively.

The parameter *`ClipSize`* contains the
output image dimensions `'width'` and `'height'` as a tuple.
Passing *-1* keeps the
corresponding dimension of the input image unchanged. *`RangeTrans`*
shifts the image center by a random fraction of *`ClipSize`*.

The following generic parameters *`GenParamName`* and the
corresponding values *`GenParamValue`* are supported:

- ***'interpolation'*:** —

  Specifies the interpolation mode.
  Currently the modes *'bilinear'* and
  *'nearest_neighbor'* are supported.

  Default:
   *'bilinear'*.

Padding is applied if required, the *'fill_value'*
can be specified using [`set_dl_transform_pipeline_param`](set_dl_transform_pipeline_param.md).
Note that for axis-aligned object detection, rotation, shearing and
perspective transformation may cause bounding
boxes to fit less tightly around objects than before the transformation.

The following parameters are specific to the transforms of type
*'random_geometric'*. They can respectively be get or set using the
operators [`get_dl_transform_pipeline_param`](get_dl_transform_pipeline_param.md) and
[`set_dl_transform_pipeline_param`](set_dl_transform_pipeline_param.md):

| ParamName | `set` | `get` |
| --- | --- | --- |
| *'range_scale'* | `x` | `x` |
| *'range_trans'* | `x` | `x` |
| *'range_rot'* | `x` | `x` |
| *'range_shear'* | `x` | `x` |
| *'range_perspective'* | `x` | `x` |
| *'clip_size'* | `x` | `x` |
| *'interpolation'* | `x` | `x` |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`TransformName`** (input_control)  string `→`  (string)

Name of the output transform.

Default:
'random_geometric'

**`Probability`** (input_control)  real `→`  (real)

Probability to execute the transform.

Default:
1.0

**`RangeScale`** (input_control)  real-array `→`  (real)

Tuple with random scale range.

Default:
[0.5,1.5]

**`RangeTrans`** (input_control)  real-array `→`  (real)

Tuple with random translation range.

Default:
[-0.1,0.1]

**`RangeRot`** (input_control)  real-array `→`  (real)

Tuple with random rotation range.

Default:
[0.0,0.0]

**`RangeShear`** (input_control)  real-array `→`  (real)

Tuple with random shear range.

Default:
[0.0,0.0]

**`RangePerspective`** (input_control)  real-array `→`  (real)

Tuple with random perspective range.

Default:
[0.0,0.0]

**`ClipSize`** (input_control)  integer-array `→`  (integer)

Tuple containing output image size.

Default:
[-1,-1]

**`GenParamName`** (input_control)  attribute.name-array `→`  (string)

Generic input parameter names.

Default:
[]

List of values:
'interpolation'

**`GenParamValue`** (input_control)  attribute.value-array `→`  (string)

Generic input parameter values.

Default:
[]

Suggested values:

**`RandomGeometric`** (output_control)  dl_transform `→`  (handle)

Random geometric transform.

## Possible Successors

`create_dl_transform_pipeline`

## See also

`create_dl_transform_random_hsv`

## Module

Foundation
