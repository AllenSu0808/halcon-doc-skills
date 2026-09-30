# CreateLocalDeformableModelXld (Operator)

## Name

`CreateLocalDeformableModelXld` — Prepare a deformable model for local deformable matching from XLD contours.

## Signature

`static void HOperatorSet.CreateLocalDeformableModelXld(HObject contours, HTuple numLevels, HTuple angleStart, HTuple angleExtent, HTuple angleStep, HTuple scaleRMin, HTuple scaleRMax, HTuple scaleRStep, HTuple scaleCMin, HTuple scaleCMax, HTuple scaleCStep, HTuple optimization, HTuple metric, HTuple minContrast, HTuple genParamName, HTuple genParamValue, out HTuple modelID)`

`void HDeformableModel.CreateLocalDeformableModelXld(HXLDCont contours, HTuple numLevels, HTuple angleStart, HTuple angleExtent, HTuple angleStep, double scaleRMin, HTuple scaleRMax, HTuple scaleRStep, double scaleCMin, HTuple scaleCMax, HTuple scaleCStep, HTuple optimization, string metric, int minContrast, HTuple genParamName, HTuple genParamValue)`

`void HDeformableModel.CreateLocalDeformableModelXld(HXLDCont contours, int numLevels, HTuple angleStart, HTuple angleExtent, double angleStep, double scaleRMin, HTuple scaleRMax, double scaleRStep, double scaleCMin, HTuple scaleCMax, double scaleCStep, string optimization, string metric, int minContrast, HTuple genParamName, HTuple genParamValue)`

`HDeformableModel HXLDCont.CreateLocalDeformableModelXld(HTuple numLevels, HTuple angleStart, HTuple angleExtent, HTuple angleStep, double scaleRMin, HTuple scaleRMax, HTuple scaleRStep, double scaleCMin, HTuple scaleCMax, HTuple scaleCStep, HTuple optimization, string metric, int minContrast, HTuple genParamName, HTuple genParamValue)`

`HDeformableModel HXLDCont.CreateLocalDeformableModelXld(int numLevels, HTuple angleStart, HTuple angleExtent, double angleStep, double scaleRMin, HTuple scaleRMax, double scaleRStep, double scaleCMin, HTuple scaleCMax, double scaleCStep, string optimization, string metric, int minContrast, HTuple genParamName, HTuple genParamValue)`

## Description

The operator `CreateLocalDeformableModelXld` creates a
deformable model used for local deformable matching from the XLD contours
passed in *`contours`*. The XLD contours represent the gray-value edges
of the object to be searched for. In contrast to the operator
[`CreateLocalDeformableModel`](create_local_deformable_model.md), which creates a deformable
model from a template image, the operator
`CreateLocalDeformableModelXld` creates the deformable
model from XLD contours.

The center of gravity of the smallest surrounding rectangle of the
*`contours`* that is parallel to the coordinate axes is used as the origin
(reference point) of the model. A different origin can be set with
[`SetDeformableModelOrigin`](set_deformable_model_origin.md).

For further explanation on the deformable model and its parameters we
refer to the description of [`CreatePlanarUncalibDeformableModel`](create_planar_uncalib_deformable_model.md)
and [`CreateLocalDeformableModel`](create_local_deformable_model.md). Note that
[`SetLocalDeformableModelMetric`](set_local_deformable_model_metric.md) can be used to change the
metric of the model.

## Attention

Note that, in contrast to the operator
[`CreateLocalDeformableModel`](create_local_deformable_model.md), it is not possible to specify a
minimum size of the model components. To avoid small model components in the
model, short contours can be eliminated with the operator
[`SelectContoursXld`](select_contours_xld.md) before calling
`CreateLocalDeformableModelXld`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`contours`** (input_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Input contours that will be used to create the model.

**`numLevels`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long / string)

Maximum number of pyramid levels.

Default:
"auto"

List of values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "auto"

**`angleStart`** (input_control)  angle.rad-array `→` [HTuple](HTuple.md) (*double*)

This parameter is not used.

Default:
[]

**`angleExtent`** (input_control)  angle.rad-array `→` [HTuple](HTuple.md) (*double*)

This parameter is not used.

Default:
[]

**`angleStep`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double* / string)

Step length of the angles (resolution).

Default:
"auto"

Suggested values:
"auto", 0.0175, 0.0349, 0.0524, 0.0698, 0.0873

Restriction:
`AngleStep > 0 && AngleStep <= pi / 16`

**`scaleRMin`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Minimum scale of the pattern in row direction.

Default:
1.0

Suggested values:
0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Restriction:
`ScaleRMin > 0`

**`scaleRMax`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double*)

This parameter is not used.

Default:
[]

**`scaleRStep`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / string)

Scale step length (resolution) in row direction.

Default:
"auto"

Suggested values:
"auto", 0.01, 0.02, 0.05, 0.1, 0.15, 0.2

Restriction:
`ScaleRStep > 0`

**`scaleCMin`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Minimum scale of the pattern in column direction.

Default:
1.0

Suggested values:
0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Restriction:
`ScaleCMin > 0`

**`scaleCMax`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double*)

This parameter is not used.

Default:
[]

**`scaleCStep`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / string)

Scale step length (resolution) in column direction.

Default:
"auto"

Suggested values:
"auto", 0.01, 0.02, 0.05, 0.1, 0.15, 0.2

Restriction:
`ScaleCStep > 0`

**`optimization`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Kind of optimization used for generating the model.

Default:
"auto"

List of values:
"auto", "none", "point_reduction_high", "point_reduction_low", "point_reduction_medium"

**`metric`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Match metric.

Default:
"ignore_local_polarity"

List of values:
"ignore_color_polarity", "ignore_global_polarity", "ignore_local_polarity", "ignore_part_polarity", "use_polarity"

**`minContrast`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Minimum contrast of the objects in the search images.

Default:
5

Suggested values:
1, 2, 3, 5, 7, 10, 20, 30, 40

**`genParamName`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string*)

The generic parameter names.

Default:
[]

List of values:
[], "part_size"

**`genParamValue`** (input_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long / double / string)

Values of the generic parameters.

Default:
[]

List of values:
[], "big", "medium", "small"

**`modelID`** (output_control)  deformable_model `→` [HDeformableModel](HDeformableModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

## Result

If the parameters are valid, the operator
`CreateLocalDeformableModelXld` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised. If the parameter *`numLevels`* is
chosen such that the model contains too few points, the error 8510 is raised.

## Possible Predecessors

`ReadContourXldDxf`,
`EdgesSubPix`,
`SelectContoursXld`

## Possible Successors

`FindLocalDeformableModel`

## See also

`CreateLocalDeformableModel`

## Module

Matching
