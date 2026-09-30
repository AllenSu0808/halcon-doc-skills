# DetermineDeformableModelParams (Operator)

## Name

`DetermineDeformableModelParams` — Determine the parameters of a deformable model.

## Signature

`static void HOperatorSet.DetermineDeformableModelParams(HObject template, HTuple numLevels, HTuple angleStart, HTuple angleExtent, HTuple scaleMin, HTuple scaleMax, HTuple optimization, HTuple metric, HTuple contrast, HTuple minContrast, HTuple genParamName, HTuple genParamValue, HTuple parameters, out HTuple parameterName, out HTuple parameterValue)`

`HTuple HImage.DetermineDeformableModelParams(HTuple numLevels, double angleStart, double angleExtent, HTuple scaleMin, HTuple scaleMax, string optimization, string metric, HTuple contrast, HTuple minContrast, HTuple genParamName, HTuple genParamValue, HTuple parameters, out HTuple parameterValue)`

`HTuple HImage.DetermineDeformableModelParams(int numLevels, double angleStart, double angleExtent, double scaleMin, double scaleMax, string optimization, string metric, int contrast, int minContrast, HTuple genParamName, HTuple genParamValue, string parameters, out HTuple parameterValue)`

## Description

`DetermineDeformableModelParams` determines certain parameters
of a deformable model automatically from the model image
*`template`*. The parameters to be determined can be specified
with *`parameters`*. `DetermineDeformableModelParams` can
be used to determine the same parameters that are determined
automatically when the respective parameter in
[`CreatePlanarUncalibDeformableModel`](create_planar_uncalib_deformable_model.md) is set to *"auto"*:
the number of pyramid levels (*`parameters`* =
*"num_levels"*), the angle step length (*`parameters`*
= *"angle_step"*), the scale step length
(*`parameters`* = *"scale_step"* for isotropic scaling
and *"scale_r_step"* and/or *"scale_c_step"* for
anisotropic scaling), the kind of optimization (*`parameters`*
= *"optimization"*), the threshold (*`parameters`* =
*"contrast"*) or the hysteresis thresholds
(*`parameters`* = *"contrast_hyst"*) for the contrast,
the minimum size of the object parts (*`parameters`* =
*"min_size"*), and the minimum contrast (*`parameters`*
= *"min_contrast"*). By passing a tuple of the above
values in *`parameters`*, an arbitrary combination of these
parameters can be determined. If all of the above parameters should
be determined, the value *"all"* can be passed. In this case
both hysteresis thresholds are determined, i.e., the operator
behaves like passing *"contrast_hyst"* instead of
*"contrast"*.

`DetermineDeformableModelParams` is mainly useful to determine
the above parameters before creating the model, e.g., in an
interactive system, which makes suggestions for these parameters to
the user, but enables the user to modify the suggested values.

The automatically determined parameters are returned as a name-value
pair in *`parameterName`* and *`parameterValue`*. The
parameter names in *`parameterName`* are identical to the names
in *`parameters`*, where, of course, the value *"all"*
is replaced by the actual parameter names. An exception is the
parameter *"contrast_hyst"*, for which the two values
*"contrast_low"* and *"contrast_high"* are returned.

The remaining parameters (*`numLevels`*, *`angleStart`*,
*`angleExtent`*, *`scaleMin`*, *`scaleMax`*,
*`optimization`*, *`metric`*, *`contrast`*, and
*`minContrast`*) have the same meaning as in
[`CreatePlanarUncalibDeformableModel`](create_planar_uncalib_deformable_model.md) and
[`FindPlanarUncalibDeformableModel`](find_planar_uncalib_deformable_model.md). The description of these
parameters can be looked up with these operators. These parameters
are used by `DetermineDeformableModelParams` to calculate the
parameters to be determined in the same manner as in
[`CreatePlanarUncalibDeformableModel`](create_planar_uncalib_deformable_model.md). It should be noted that if
the parameters of a deformable model with isotropic scaling should be
determined, i.e., if *`parameters`* contains
*"scale_step"* either explicitly or implicitly via
*"all"*, the parameters *`scaleMin`* and
*`scaleMax`* must contain one value each. If the parameters of
a deformable model with anisotropic scaling should be determined, i.e.,
if *`parameters`* contains *"scale_r_step"* or
*"scale_c_step"* either explicitly or implicitly, the
parameters *`scaleMin`* and *`scaleMax`* must contain two
values each. In this case, the first value of the respective
parameter refers to the scaling in row direction, while the
second value refers to scaling in the column direction.

Note that in `DetermineDeformableModelParams` some parameters
appear that can also be determined automatically
(*`numLevels`*, *`optimization`*, *`contrast`*,
*`minContrast`*). If these parameters should not be determined
automatically, i.e., their name is not passed in
*`parameterName`*, the corresponding parameters must contain
valid values and must not be set to *"auto"*. In contrast, if
these parameters are to be determined automatically, their values
are treated in the following way: If the optimization or the
(hysteresis) contrast is to be determined automatically, i.e.,
*`parameterName`* contains the value *"optimization"* or
*"contrast"* (*"contrast_hyst"*), the values passed in
*`optimization`* and *`contrast`* are ignored. In
contrast, if the maximum number of pyramid levels or the minimum
contrast is to be determined automatically, i.e.,
*`parameterName`* contains the value *"num_levels"* or
*"min_contrast"*, you can let HALCON determine suitable
values and at the same time specify an upper or lower boundary,
respectively:

If the maximum number of pyramid levels should be specified in
advance, *`numLevels`* can be set to the particular value. If
in this case *`parameters`* contains the value
*"num_levels"*, the computed number of pyramid levels is at
most *`numLevels`*. If *`numLevels`* is set to
*"auto"* (or *0* for backwards compatibility), the
number of pyramid levels is determined without restrictions as large
as possible.

If the minimum contrast should be specified in advance,
*`minContrast`* can be set to the particular value. If in this
case *`parameters`* contains the value *"min_contrast"*,
the computed minimum contrast is at least *`minContrast`*. If
*`minContrast`* is set to *"auto"*, the minimum contrast
is determined without restrictions.

If the user wishes to create a calibrated, deformable model
with [`CreatePlanarCalibDeformableModel`](create_planar_calib_deformable_model.md), the internal camera
parameters are needed for the correct estimation of the parameters in
*`parameterValue`*. The camera parameters can be provided by setting
*`genParamName`* to *"cam_param"* and providing the tuple containing
the camera parameters in *`genParamValue`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

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

**`angleStart`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Smallest rotation of the model.

Default:
-0.39

Suggested values:
-3.14, -1.57, -0.79, -0.39, -0.20, 0.0

**`angleExtent`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Extent of the rotation angles.

Default:
0.79

Suggested values:
6.28, 3.14, 1.57, 0.79, 0.39

Restriction:
`AngleExtent >= 0`

**`scaleMin`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Minimum scale of the model.

Default:
0.9

Suggested values:
0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Restriction:
`ScaleMin > 0`

**`scaleMax`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Maximum scale of the model.

Default:
1.1

Suggested values:
1.0, 1.1, 1.2, 1.3, 1.4, 1.5

Restriction:
`ScaleMax >= ScaleMin`

**`optimization`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Kind of optimization.

Default:
"auto"

List of values:
"auto", "none", "point_reduction_high", "point_reduction_low", "point_reduction_medium"

**`metric`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Match metric.

Default:
"use_polarity"

List of values:
"ignore_color_polarity", "ignore_global_polarity", "ignore_local_polarity", "use_polarity"

**`contrast`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long / string)

Threshold or hysteresis thresholds for the contrast
of the object in the template image and optionally
minimum size of the object parts.

Default:
"auto"

Suggested values:
"auto", "auto_contrast", "auto_contrast_hyst", "auto_min_size", 10, 20, 30, 40, 60, 80, 100, 120, 140, 160

**`minContrast`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long / string)

Minimum contrast of the objects in the search images.

Default:
"auto"

Suggested values:
"auto", 1, 2, 3, 5, 7, 10, 20, 30, 40

Restriction:
`MinContrast < Contrast`

**`genParamName`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string*)

The general parameter names.

Default:
[]

List of values:
"cam_param"

**`genParamValue`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long / string)

Values of the general parameter.

Default:
[]

List of values:
[]

**`parameters`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Parameters to be determined automatically.

Default:
"all"

List of values:
"all", "angle_step", "contrast", "contrast_hyst", "min_contrast", "min_size", "num_levels", "optimization", "scale_c_step", "scale_r_step", "scale_step"

**`parameterName`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Name of the automatically determined parameter.

**`parameterValue`** (output_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Value of the automatically determined parameter.

## Result

If the parameters are valid, the operator
`DetermineDeformableModelParams` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised. If the parameters
*`numLevels`* and *`contrast`* are chosen such that the
model contains too few points, or the input image does not contain a
sufficient number of significant features, the error message 8510 is
raised.

## Possible Successors

`CreatePlanarUncalibDeformableModel`,
`CreatePlanarCalibDeformableModel`,
`CreateLocalDeformableModel`

## See also

`FindPlanarUncalibDeformableModel`,
`FindPlanarCalibDeformableModel`

## Module

Matching
