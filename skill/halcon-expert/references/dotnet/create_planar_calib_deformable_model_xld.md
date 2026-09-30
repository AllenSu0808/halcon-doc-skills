# CreatePlanarCalibDeformableModelXld (Operator)

## Name

`CreatePlanarCalibDeformableModelXld` — Prepare a deformable model for planar calibrated matching from XLD contours.

## Signature

`static void HOperatorSet.CreatePlanarCalibDeformableModelXld(HObject contours, HTuple camParam, HTuple referencePose, HTuple numLevels, HTuple angleStart, HTuple angleExtent, HTuple angleStep, HTuple scaleRMin, HTuple scaleRMax, HTuple scaleRStep, HTuple scaleCMin, HTuple scaleCMax, HTuple scaleCStep, HTuple optimization, HTuple metric, HTuple minContrast, HTuple genParamName, HTuple genParamValue, out HTuple modelID)`

`public HDeformableModel(HXLDCont contours, HCamPar camParam, HPose referencePose, HTuple numLevels, HTuple angleStart, HTuple angleExtent, HTuple angleStep, double scaleRMin, HTuple scaleRMax, HTuple scaleRStep, double scaleCMin, HTuple scaleCMax, HTuple scaleCStep, HTuple optimization, string metric, int minContrast, HTuple genParamName, HTuple genParamValue)`

`public HDeformableModel(HXLDCont contours, HCamPar camParam, HPose referencePose, int numLevels, HTuple angleStart, HTuple angleExtent, double angleStep, double scaleRMin, HTuple scaleRMax, double scaleRStep, double scaleCMin, HTuple scaleCMax, double scaleCStep, string optimization, string metric, int minContrast, HTuple genParamName, HTuple genParamValue)`

`void HDeformableModel.CreatePlanarCalibDeformableModelXld(HXLDCont contours, HCamPar camParam, HPose referencePose, HTuple numLevels, HTuple angleStart, HTuple angleExtent, HTuple angleStep, double scaleRMin, HTuple scaleRMax, HTuple scaleRStep, double scaleCMin, HTuple scaleCMax, HTuple scaleCStep, HTuple optimization, string metric, int minContrast, HTuple genParamName, HTuple genParamValue)`

`void HDeformableModel.CreatePlanarCalibDeformableModelXld(HXLDCont contours, HCamPar camParam, HPose referencePose, int numLevels, HTuple angleStart, HTuple angleExtent, double angleStep, double scaleRMin, HTuple scaleRMax, double scaleRStep, double scaleCMin, HTuple scaleCMax, double scaleCStep, string optimization, string metric, int minContrast, HTuple genParamName, HTuple genParamValue)`

`HDeformableModel HXLDCont.CreatePlanarCalibDeformableModelXld(HCamPar camParam, HPose referencePose, HTuple numLevels, HTuple angleStart, HTuple angleExtent, HTuple angleStep, double scaleRMin, HTuple scaleRMax, HTuple scaleRStep, double scaleCMin, HTuple scaleCMax, HTuple scaleCStep, HTuple optimization, string metric, int minContrast, HTuple genParamName, HTuple genParamValue)`

`HDeformableModel HXLDCont.CreatePlanarCalibDeformableModelXld(HCamPar camParam, HPose referencePose, int numLevels, HTuple angleStart, HTuple angleExtent, double angleStep, double scaleRMin, HTuple scaleRMax, double scaleRStep, double scaleCMin, HTuple scaleCMax, double scaleCStep, string optimization, string metric, int minContrast, HTuple genParamName, HTuple genParamValue)`

`HDeformableModel HCamPar.CreatePlanarCalibDeformableModelXld(HXLDCont contours, HPose referencePose, HTuple numLevels, HTuple angleStart, HTuple angleExtent, HTuple angleStep, double scaleRMin, HTuple scaleRMax, HTuple scaleRStep, double scaleCMin, HTuple scaleCMax, HTuple scaleCStep, HTuple optimization, string metric, int minContrast, HTuple genParamName, HTuple genParamValue)`

`HDeformableModel HCamPar.CreatePlanarCalibDeformableModelXld(HXLDCont contours, HPose referencePose, int numLevels, HTuple angleStart, HTuple angleExtent, double angleStep, double scaleRMin, HTuple scaleRMax, double scaleRStep, double scaleCMin, HTuple scaleCMax, double scaleCStep, string optimization, string metric, int minContrast, HTuple genParamName, HTuple genParamValue)`

`HDeformableModel HPose.CreatePlanarCalibDeformableModelXld(HXLDCont contours, HCamPar camParam, HTuple numLevels, HTuple angleStart, HTuple angleExtent, HTuple angleStep, double scaleRMin, HTuple scaleRMax, HTuple scaleRStep, double scaleCMin, HTuple scaleCMax, HTuple scaleCStep, HTuple optimization, string metric, int minContrast, HTuple genParamName, HTuple genParamValue)`

`HDeformableModel HPose.CreatePlanarCalibDeformableModelXld(HXLDCont contours, HCamPar camParam, int numLevels, HTuple angleStart, HTuple angleExtent, double angleStep, double scaleRMin, HTuple scaleRMax, double scaleRStep, double scaleCMin, HTuple scaleCMax, double scaleCStep, string optimization, string metric, int minContrast, HTuple genParamName, HTuple genParamValue)`

## Description

The operator `CreatePlanarCalibDeformableModelXld` creates a
deformable model used for planar calibrated matching from the XLD contours
passed in *`contours`*. The XLD contours represent the gray-value edges
of the object to be searched for. In contrast to the operator
[`CreatePlanarCalibDeformableModel`](create_planar_calib_deformable_model.md), which creates a deformable
model from a template image, the operator
`CreatePlanarCalibDeformableModelXld` creates the deformable
model from XLD contours. Note that the operator expects *`contours`* to
be in a metric world coordinate system. This is in contrast to
[`CreatePlanarUncalibDeformableModelXld`](create_planar_uncalib_deformable_model_xld.md), where the
*`contours`* are provided in image coordinates. To check if shape and
size of the model correspond with the objects in the world coordinate
system you can project the model into the image using
[`Project3dPoint`](project_3d_point.md).

Further, the origin (reference point) of the model is taken directly from
the provided *`contours`*. A different origin in the
world coordinate system can be set with [`SetDeformableModelOrigin`](set_deformable_model_origin.md).

The parameters *`modelID`*, *`camParam`* and
*`referencePose`* are described in
[`CreatePlanarCalibDeformableModel`](create_planar_calib_deformable_model.md).
Further input parameters that specify the model are described in
[`CreatePlanarUncalibDeformableModel`](create_planar_uncalib_deformable_model.md).

## Attention

Note that, in contrast to the operator
[`CreatePlanarCalibDeformableModel`](create_planar_calib_deformable_model.md), it is not possible to specify a
minimum size of the model components. To avoid small model components in the
model, short contours can be eliminated before calling
`CreatePlanarCalibDeformableModelXld` with the operator
[`SelectContoursXld`](select_contours_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`contours`** (input_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Input contours that will be used to create the model.

**`camParam`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

The parameters of the internal orientation of the
camera.

**`referencePose`** (input_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

The reference pose of the object.

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

Scale step length (resolution) in the column direction.

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

Values of the generic parameter.

Default:
[]

List of values:
[], "big", "medium", "small"

**`modelID`** (output_control)  deformable_model `→` [HDeformableModel](HDeformableModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

## Result

If the parameters are valid, the operator
`CreatePlanarCalibDeformableModelXld` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised. If the parameter *`numLevels`* is
chosen such that the model contains too few points, the error 8510 is raised.

## Possible Predecessors

`ReadContourXldDxf`,
`EdgesSubPix`,
`SelectContoursXld`

## Possible Successors

`FindPlanarCalibDeformableModel`

## See also

`CreatePlanarCalibDeformableModel`

## Module

Matching
