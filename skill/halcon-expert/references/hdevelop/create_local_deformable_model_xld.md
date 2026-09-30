# create_local_deformable_model_xld (Operator)

## Name

`create_local_deformable_model_xld` — Prepare a deformable model for local deformable matching from XLD contours.

## Signature

`create_local_deformable_model_xld(Contours : : NumLevels, AngleStart, AngleExtent, AngleStep, ScaleRMin, ScaleRMax, ScaleRStep, ScaleCMin, ScaleCMax, ScaleCStep, Optimization, Metric, MinContrast, GenParamName, GenParamValue : ModelID)`

## Description

The operator `create_local_deformable_model_xld` creates a
deformable model used for local deformable matching from the XLD contours
passed in *`Contours`*. The XLD contours represent the gray-value edges
of the object to be searched for. In contrast to the operator
[`create_local_deformable_model`](create_local_deformable_model.md), which creates a deformable
model from a template image, the operator
`create_local_deformable_model_xld` creates the deformable
model from XLD contours.

The center of gravity of the smallest surrounding rectangle of the
*`Contours`* that is parallel to the coordinate axes is used as the origin
(reference point) of the model. A different origin can be set with
[`set_deformable_model_origin`](set_deformable_model_origin.md).

For further explanation on the deformable model and its parameters we
refer to the description of [`create_planar_uncalib_deformable_model`](create_planar_uncalib_deformable_model.md)
and [`create_local_deformable_model`](create_local_deformable_model.md). Note that
[`set_local_deformable_model_metric`](set_local_deformable_model_metric.md) can be used to change the
metric of the model.

## Attention

Note that, in contrast to the operator
[`create_local_deformable_model`](create_local_deformable_model.md), it is not possible to specify a
minimum size of the model components. To avoid small model components in the
model, short contours can be eliminated with the operator
[`select_contours_xld`](select_contours_xld.md) before calling
`create_local_deformable_model_xld`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`Contours`** (input_object)  xld_cont(-array) `→` object

Input contours that will be used to create the model.

**`NumLevels`** (input_control)  integer `→`  (integer / string)

Maximum number of pyramid levels.

Default:
'auto'

List of values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'auto'

**`AngleStart`** (input_control)  angle.rad-array `→`  (real)

This parameter is not used.

Default:
[]

**`AngleExtent`** (input_control)  angle.rad-array `→`  (real)

This parameter is not used.

Default:
[]

**`AngleStep`** (input_control)  angle.rad `→`  (real / string)

Step length of the angles (resolution).

Default:
'auto'

Suggested values:
'auto', 0.0175, 0.0349, 0.0524, 0.0698, 0.0873

Restriction:
`AngleStep > 0 && AngleStep <= pi / 16`

**`ScaleRMin`** (input_control)  number `→`  (real)

Minimum scale of the pattern in row direction.

Default:
1.0

Suggested values:
0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Restriction:
`ScaleRMin > 0`

**`ScaleRMax`** (input_control)  number-array `→`  (real)

This parameter is not used.

Default:
[]

**`ScaleRStep`** (input_control)  number `→`  (real / string)

Scale step length (resolution) in row direction.

Default:
'auto'

Suggested values:
'auto', 0.01, 0.02, 0.05, 0.1, 0.15, 0.2

Restriction:
`ScaleRStep > 0`

**`ScaleCMin`** (input_control)  number `→`  (real)

Minimum scale of the pattern in column direction.

Default:
1.0

Suggested values:
0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Restriction:
`ScaleCMin > 0`

**`ScaleCMax`** (input_control)  number-array `→`  (real)

This parameter is not used.

Default:
[]

**`ScaleCStep`** (input_control)  number `→`  (real / string)

Scale step length (resolution) in column direction.

Default:
'auto'

Suggested values:
'auto', 0.01, 0.02, 0.05, 0.1, 0.15, 0.2

Restriction:
`ScaleCStep > 0`

**`Optimization`** (input_control)  string(-array) `→`  (string)

Kind of optimization used for generating the model.

Default:
'auto'

List of values:
'auto', 'none', 'point_reduction_high', 'point_reduction_low', 'point_reduction_medium'

**`Metric`** (input_control)  string `→`  (string)

Match metric.

Default:
'ignore_local_polarity'

List of values:
'ignore_color_polarity', 'ignore_global_polarity', 'ignore_local_polarity', 'ignore_part_polarity', 'use_polarity'

**`MinContrast`** (input_control)  number `→`  (integer)

Minimum contrast of the objects in the search images.

Default:
5

Suggested values:
1, 2, 3, 5, 7, 10, 20, 30, 40

**`GenParamName`** (input_control)  string-array `→`  (string)

The generic parameter names.

Default:
[]

List of values:
[], 'part_size'

**`GenParamValue`** (input_control)  integer-array `→`  (integer / real / string)

Values of the generic parameters.

Default:
[]

List of values:
[], 'big', 'medium', 'small'

**`ModelID`** (output_control)  deformable_model `→`  (handle)

Handle of the model.

## Result

If the parameters are valid, the operator
`create_local_deformable_model_xld` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised. If the parameter *`NumLevels`* is
chosen such that the model contains too few points, the error 8510 is raised.

## Possible Predecessors

`read_contour_xld_dxf`,
`edges_sub_pix`,
`select_contours_xld`

## Possible Successors

`find_local_deformable_model`

## See also

`create_local_deformable_model`

## Module

Matching
