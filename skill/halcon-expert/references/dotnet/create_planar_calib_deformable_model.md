# CreatePlanarCalibDeformableModel (Operator)

## Name

`CreatePlanarCalibDeformableModel` — Create a deformable model for calibrated perspective matching.

## Signature

`static void HOperatorSet.CreatePlanarCalibDeformableModel(HObject template, HTuple camParam, HTuple referencePose, HTuple numLevels, HTuple angleStart, HTuple angleExtent, HTuple angleStep, HTuple scaleRMin, HTuple scaleRMax, HTuple scaleRStep, HTuple scaleCMin, HTuple scaleCMax, HTuple scaleCStep, HTuple optimization, HTuple metric, HTuple contrast, HTuple minContrast, HTuple genParamName, HTuple genParamValue, out HTuple modelID)`

`public HDeformableModel(HImage template, HCamPar camParam, HPose referencePose, HTuple numLevels, HTuple angleStart, HTuple angleExtent, HTuple angleStep, double scaleRMin, HTuple scaleRMax, HTuple scaleRStep, double scaleCMin, HTuple scaleCMax, HTuple scaleCStep, HTuple optimization, string metric, HTuple contrast, HTuple minContrast, HTuple genParamName, HTuple genParamValue)`

`public HDeformableModel(HImage template, HCamPar camParam, HPose referencePose, int numLevels, HTuple angleStart, HTuple angleExtent, double angleStep, double scaleRMin, HTuple scaleRMax, double scaleRStep, double scaleCMin, HTuple scaleCMax, double scaleCStep, string optimization, string metric, HTuple contrast, int minContrast, HTuple genParamName, HTuple genParamValue)`

`void HDeformableModel.CreatePlanarCalibDeformableModel(HImage template, HCamPar camParam, HPose referencePose, HTuple numLevels, HTuple angleStart, HTuple angleExtent, HTuple angleStep, double scaleRMin, HTuple scaleRMax, HTuple scaleRStep, double scaleCMin, HTuple scaleCMax, HTuple scaleCStep, HTuple optimization, string metric, HTuple contrast, HTuple minContrast, HTuple genParamName, HTuple genParamValue)`

`void HDeformableModel.CreatePlanarCalibDeformableModel(HImage template, HCamPar camParam, HPose referencePose, int numLevels, HTuple angleStart, HTuple angleExtent, double angleStep, double scaleRMin, HTuple scaleRMax, double scaleRStep, double scaleCMin, HTuple scaleCMax, double scaleCStep, string optimization, string metric, HTuple contrast, int minContrast, HTuple genParamName, HTuple genParamValue)`

`HDeformableModel HImage.CreatePlanarCalibDeformableModel(HCamPar camParam, HPose referencePose, HTuple numLevels, HTuple angleStart, HTuple angleExtent, HTuple angleStep, double scaleRMin, HTuple scaleRMax, HTuple scaleRStep, double scaleCMin, HTuple scaleCMax, HTuple scaleCStep, HTuple optimization, string metric, HTuple contrast, HTuple minContrast, HTuple genParamName, HTuple genParamValue)`

`HDeformableModel HImage.CreatePlanarCalibDeformableModel(HCamPar camParam, HPose referencePose, int numLevels, HTuple angleStart, HTuple angleExtent, double angleStep, double scaleRMin, HTuple scaleRMax, double scaleRStep, double scaleCMin, HTuple scaleCMax, double scaleCStep, string optimization, string metric, HTuple contrast, int minContrast, HTuple genParamName, HTuple genParamValue)`

`HDeformableModel HCamPar.CreatePlanarCalibDeformableModel(HImage template, HPose referencePose, HTuple numLevels, HTuple angleStart, HTuple angleExtent, HTuple angleStep, double scaleRMin, HTuple scaleRMax, HTuple scaleRStep, double scaleCMin, HTuple scaleCMax, HTuple scaleCStep, HTuple optimization, string metric, HTuple contrast, HTuple minContrast, HTuple genParamName, HTuple genParamValue)`

`HDeformableModel HCamPar.CreatePlanarCalibDeformableModel(HImage template, HPose referencePose, int numLevels, HTuple angleStart, HTuple angleExtent, double angleStep, double scaleRMin, HTuple scaleRMax, double scaleRStep, double scaleCMin, HTuple scaleCMax, double scaleCStep, string optimization, string metric, HTuple contrast, int minContrast, HTuple genParamName, HTuple genParamValue)`

`HDeformableModel HPose.CreatePlanarCalibDeformableModel(HImage template, HCamPar camParam, HTuple numLevels, HTuple angleStart, HTuple angleExtent, HTuple angleStep, double scaleRMin, HTuple scaleRMax, HTuple scaleRStep, double scaleCMin, HTuple scaleCMax, HTuple scaleCStep, HTuple optimization, string metric, HTuple contrast, HTuple minContrast, HTuple genParamName, HTuple genParamValue)`

`HDeformableModel HPose.CreatePlanarCalibDeformableModel(HImage template, HCamPar camParam, int numLevels, HTuple angleStart, HTuple angleExtent, double angleStep, double scaleRMin, HTuple scaleRMax, double scaleRStep, double scaleCMin, HTuple scaleCMax, double scaleCStep, string optimization, string metric, HTuple contrast, int minContrast, HTuple genParamName, HTuple genParamValue)`

## Description

The operator `CreatePlanarCalibDeformableModel` creates a
deformable model for planar calibrated matching based on the input image
*`template`*.

The model ROI corresponds to the domain of *`template`*.
The model is generated for multiple image pyramid levels and is
stored in memory. The output parameter
*`modelID`* is a handle for this model and is used in subsequent
calls to [`FindPlanarCalibDeformableModel`](find_planar_calib_deformable_model.md).

The internal camera parameters are provided in *`camParam`*. The
internal parameters can typically be determined using
[`CalibrateCameras`](calibrate_cameras.md). By providing *`camParam`* it is possible to
retrieve a 3D pose of the model as a result of the planar calibrated matching.
See [`CreatePlanarUncalibDeformableModel`](create_planar_uncalib_deformable_model.md) on how to progress
without using calibration data. See
`“Solution Guide II-B - Matching”` for more information on
these approaches.

![figure](../assets/7c1f6bc4cc4b9bf1.svg)

Scheme of the reference pose *`referencePose`* in relation to the
absolute pose of the model as projected from the image into the
model plane.

The x- and y-axis of the reference pose *`referencePose`*
$(x^{r},y^{r},z^{r})$ determine the 3D model plane, thus the
plane in the world coordinate system, the model is located in (see
scheme above).
The 3D model plane can be obtained by using [`CalibrateCameras`](calibrate_cameras.md) or
[`VectorToPose`](vector_to_pose.md), e.g., by placing and localizing a calibration plate
in the same plane as the model is located in.

The model's origin is located in the center of gravity of the model region
in *`template`*. The projection of this image point onto the 3D model
plane determined by *`referencePose`* corresponds to the absolute
3D pose of the model $(x^{m},y^{m},z^{m})$. The projection
is depicted in the scheme above. After the model creation you can query
the absolute pose of the model in world coordinates using
[`GetDeformableModelParams`](get_deformable_model_params.md).
The 3D pose of the model differs from the reference pose by a
2D translation in the model plane.

Further input parameters that specify the model are described in
[`CreatePlanarUncalibDeformableModel`](create_planar_uncalib_deformable_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`template`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / uint2)

Input image whose domain will be used to create
the model.

**`camParam`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

The parameters of the internal orientation of the
camera.

**`referencePose`** (input_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

The reference pose of the object in the reference
image.

**`numLevels`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long / string)

Maximum number of pyramid levels.

Default:
"auto"

List of values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "auto"

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
`ScaleRStep >= 0`

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
`ScaleCStep >= 0`

**`optimization`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Kind of optimization used for generating the model.

Default:
"none"

List of values:
"auto", "none", "point_reduction_high", "point_reduction_low", "point_reduction_medium"

**`metric`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Match metric.

Default:
"use_polarity"

List of values:
"ignore_color_polarity", "ignore_global_polarity", "ignore_local_polarity", "ignore_part_polarity", "use_polarity"

**`contrast`** (input_control)  number-array `→` [HTuple](HTuple.md) (*int* / long / string)

Thresholds or hysteresis thresholds for the contrast
of the object in the template image.

Default:
"auto"

Suggested values:
"auto", 10, 20, 30, 40, 60, 80, 100, 120, 140, 160

**`minContrast`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long / string)

Minimum contrast of the objects in the search images.

Default:
"auto"

Suggested values:
"auto", 1, 2, 3, 5, 7, 10, 20, 30, 40

Restriction:
`MinContrast < Contrast`

**`genParamName`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string*)

The parameter names.

Default:
[]

List of values:
[], "part_size"

**`genParamValue`** (input_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long / double / string)

Values of the parameters.

Default:
[]

List of values:
[], "big", "medium", "small"

**`modelID`** (output_control)  deformable_model `→` [HDeformableModel](HDeformableModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

## Result

If the parameters are valid, the operator
`CreatePlanarCalibDeformableModel` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`DetermineDeformableModelParams`

## Possible Successors

`SetDeformableModelOrigin`,
`SetDeformableModelParam`,
`GetDeformableModelContours`,
`FindPlanarCalibDeformableModel`,
`GetDeformableModelParams`,
`WriteDeformableModel`,
`ClearDeformableModel`

## Alternatives

`ReadDeformableModel`

## See also

`CreatePlanarUncalibDeformableModel`

## Module

Matching
