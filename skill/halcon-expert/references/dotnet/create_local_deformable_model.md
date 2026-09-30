# CreateLocalDeformableModel (Operator)

## Name

`CreateLocalDeformableModel` — Creates a deformable model for local, deformable matching.

## Signature

`static void HOperatorSet.CreateLocalDeformableModel(HObject template, HTuple numLevels, HTuple angleStart, HTuple angleExtent, HTuple angleStep, HTuple scaleRMin, HTuple scaleRMax, HTuple scaleRStep, HTuple scaleCMin, HTuple scaleCMax, HTuple scaleCStep, HTuple optimization, HTuple metric, HTuple contrast, HTuple minContrast, HTuple genParamName, HTuple genParamValue, out HTuple modelID)`

`void HDeformableModel.CreateLocalDeformableModel(HImage template, HTuple numLevels, HTuple angleStart, HTuple angleExtent, HTuple angleStep, double scaleRMin, HTuple scaleRMax, HTuple scaleRStep, double scaleCMin, HTuple scaleCMax, HTuple scaleCStep, HTuple optimization, string metric, HTuple contrast, HTuple minContrast, HTuple genParamName, HTuple genParamValue)`

`void HDeformableModel.CreateLocalDeformableModel(HImage template, int numLevels, HTuple angleStart, HTuple angleExtent, double angleStep, double scaleRMin, HTuple scaleRMax, double scaleRStep, double scaleCMin, HTuple scaleCMax, double scaleCStep, string optimization, string metric, HTuple contrast, int minContrast, HTuple genParamName, HTuple genParamValue)`

`HDeformableModel HImage.CreateLocalDeformableModel(HTuple numLevels, HTuple angleStart, HTuple angleExtent, HTuple angleStep, double scaleRMin, HTuple scaleRMax, HTuple scaleRStep, double scaleCMin, HTuple scaleCMax, HTuple scaleCStep, HTuple optimization, string metric, HTuple contrast, HTuple minContrast, HTuple genParamName, HTuple genParamValue)`

`HDeformableModel HImage.CreateLocalDeformableModel(int numLevels, HTuple angleStart, HTuple angleExtent, double angleStep, double scaleRMin, HTuple scaleRMax, double scaleRStep, double scaleCMin, HTuple scaleCMax, double scaleCStep, string optimization, string metric, HTuple contrast, int minContrast, HTuple genParamName, HTuple genParamValue)`

## Description

The operator `CreateLocalDeformableModel` prepares a
template, which is passed in the image *`template`*, as a deformable
model used for local deformable matching. The ROI of the model is passed as
the domain of *`template`*.

The local deformable matching can be used to detect an object that is
distorted by a local deformation, estimate the deformation,
and rectify the image area where the object is found. For a distinction from
further matching methods we refer to the `“Solution Guide I”`
chapter '2D Matching'.

As described in [`CreatePlanarUncalibDeformableModel`](create_planar_uncalib_deformable_model.md), the origin
(reference point) of the model is defined as the center of gravity of the
domain (region) of the model image *`template`*. Further, the
axis-aligned enclosing rectangle of the domain of the *`template`* is
used to determine the area of the search image that is rectified in calls of
[`FindLocalDeformableModel`](find_local_deformable_model.md).

For further explanation on the parameters used for the creation of a local
deformable model we refer to the description of
[`CreatePlanarUncalibDeformableModel`](create_planar_uncalib_deformable_model.md). Note, that the parameters
of the actual deformation are set with the call of
[`FindLocalDeformableModel`](find_local_deformable_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`template`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / uint2)

Input image whose domain will be used to create
the model.

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

Scale step length (resolution) in column direction.

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

The generic parameter names.

Default:
[]

List of values:
[], "min_size", "part_size"

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
`CreateLocalDeformableModel` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`DetermineDeformableModelParams`

## Possible Successors

`SetDeformableModelOrigin`,
`SetDeformableModelParam`,
`GetDeformableModelContours`,
`FindLocalDeformableModel`,
`GetDeformableModelParams`,
`WriteDeformableModel`,
`ClearDeformableModel`

## Alternatives

`ReadDeformableModel`

## See also

`CreatePlanarUncalibDeformableModel`,
`CreatePlanarCalibDeformableModel`

## Module

Matching
