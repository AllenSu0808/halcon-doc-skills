# determine_shape_model_params (Operator)

## Name

`determine_shape_model_params` — Determine the parameters of a shape model.

## Signature

`determine_shape_model_params(Template : : NumLevels, AngleStart, AngleExtent, ScaleMin, ScaleMax, Optimization, Metric, Contrast, MinContrast, Parameters : ParameterName, ParameterValue)`

## Description

`determine_shape_model_params` determines certain parameters
of a shape model automatically from the model image
*`Template`*. The parameters to be determined can be specified
with *`Parameters`*. `determine_shape_model_params` can
be used to determine the same parameters that are determined
automatically when the respective parameter in
[`create_shape_model`](create_shape_model.md), [`create_scaled_shape_model`](create_scaled_shape_model.md), or
[`create_aniso_shape_model`](create_aniso_shape_model.md) is set to *'auto'*: the
number of pyramid levels (*`Parameters`* =
*'num_levels'*), the angle step length (*`Parameters`*
= *'angle_step'*), the scale step length
(*`Parameters`* = *'scale_step'* for isotropic scaling
and *'scale_r_step'* and/or *'scale_c_step'* for
anisotropic scaling), the kind of optimization (*`Parameters`*
= *'optimization'*), the threshold (*`Parameters`* =
*'contrast'*) or the hysteresis thresholds
(*`Parameters`* = *'contrast_hyst'*) for the contrast,
the minimum size of the object parts (*`Parameters`* =
*'min_size'*), and the minimum contrast (*`Parameters`*
= *'min_contrast'*). By passing a tuple of the above
values in *`Parameters`*, an arbitrary combination of these
parameters can be determined. If all of the above parameters should
be determined, the value *'all'* can be passed. In this case
both hysteresis thresholds are determined, i.e., the operator
behaves like passing *'contrast_hyst'* instead of
*'contrast'*.

`determine_shape_model_params` is mainly useful to determine
the above parameters before creating the model, e.g., in an
interactive system, which makes suggestions for these parameters to
the user, but enables the user to modify the suggested values.

The automatically determined parameters are returned as a name-value
pair in *`ParameterName`* and *`ParameterValue`*. The
parameter names in *`ParameterName`* are identical to the names
in *`Parameters`*, where, of course, the value *'all'*
is replaced by the actual parameter names. An exception is the
parameter *'contrast_hyst'*, for which the two values
*'contrast_low'* and *'contrast_high'* are returned.

The remaining parameters (*`NumLevels`*, *`AngleStart`*,
*`AngleExtent`*, *`ScaleMin`*, *`ScaleMax`*,
*`Optimization`*, *`Metric`*, *`Contrast`*, and
*`MinContrast`*) have the same meaning as in
[`create_shape_model`](create_shape_model.md), [`create_scaled_shape_model`](create_scaled_shape_model.md), and
[`create_aniso_shape_model`](create_aniso_shape_model.md). The description of these
parameters can be looked up with these operators. These parameters
are used by `determine_shape_model_params` to calculate the
parameters to be determined in the same manner as in
[`create_shape_model`](create_shape_model.md), [`create_scaled_shape_model`](create_scaled_shape_model.md), and
[`create_aniso_shape_model`](create_aniso_shape_model.md). It should be noted that if the
parameters of a shape model with isotropic scaling should be
determined, i.e., if *`Parameters`* contains
*'scale_step'* either explicitly or implicitly via
*'all'*, the parameters *`ScaleMin`* and
*`ScaleMax`* must contain one value each. If the parameters of
a shape model with anisotropic scaling should be determined, i.e.,
if *`Parameters`* contains *'scale_r_step'* or
*'scale_c_step'* either explicitly or implicitly, the
parameters *`ScaleMin`* and *`ScaleMax`* must contain two
values each. In this case, the first value of the respective
parameter refers to the scaling in the row direction, while the
second value refers to the scaling in the column direction.

Note that in `determine_shape_model_params` some parameters
appear that can also be determined automatically
(*`NumLevels`*, *`Optimization`*, *`Contrast`*,
*`MinContrast`*). If these parameters should not be determined
automatically, i.e., their name is not passed in
*`Parameters`*, the corresponding parameters must contain
valid values and must not be set to *'auto'*. In contrast, if
these parameters are to be determined automatically, their values
are treated in the following way: If the optimization or the
(hysteresis) contrast is to be determined automatically, i.e.,
*`Parameters`* contains the value *'optimization'* or
*'contrast'* (*'contrast_hyst'*), the values passed in
*`Optimization`* and *`Contrast`* are ignored. In
contrast, if the maximum number of pyramid levels or the minimum
contrast is to be determined automatically, i.e.,
*`Parameters`* contains the value *'num_levels'* or
*'min_contrast'*, you can let HALCON determine suitable
values and at the same time specify an upper or lower boundary,
respectively:

If the maximum number of pyramid levels should be specified in
advance, *`NumLevels`* can be set to the particular value. If
in this case *`Parameters`* contains the value
*'num_levels'*, the computed number of pyramid levels is at
most *`NumLevels`*. If *`NumLevels`* is set to
*'auto'* (or *0* for backwards compatibility), the
number of pyramid levels is determined without restrictions as large
as possible.

If the minimum contrast should be specified in advance,
*`MinContrast`* can be set to the particular value. If in this
case *`Parameters`* contains the value *'min_contrast'*,
the computed minimum contrast is at least *`MinContrast`*. If
*`MinContrast`* is set to *'auto'*, the minimum contrast
is determined without restrictions.

## Attention

In some cases, the maximum number of pyramid levels that is returned by
`determine_shape_model_params` is higher than the number of levels
that are actually used in the shape model. The latter
can be queried by using [`get_shape_model_params`](get_shape_model_params.md) after creating
the model. This might happen if the model is created by using
[`create_scaled_shape_model`](create_scaled_shape_model.md) or [`create_aniso_shape_model`](create_aniso_shape_model.md)
and ScaleMin, ScaleRMin, or ScaleCMin is below *1.0*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Template`** (input_object)  (multichannel-)image `→` object (byte / uint2)

Input image whose domain will be used to create
the model.

**`NumLevels`** (input_control)  integer `→`  (integer / string)

Maximum number of pyramid levels.

Default:
'auto'

List of values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'auto'

**`AngleStart`** (input_control)  angle.rad `→`  (real)

Smallest rotation of the model.

Default:
-0.39

Suggested values:
-3.14, -1.57, -0.79, -0.39, -0.20, 0.0

**`AngleExtent`** (input_control)  angle.rad `→`  (real)

Extent of the rotation angles.

Default:
0.79

Suggested values:
6.29, 3.14, 1.57, 0.79, 0.39

Restriction:
`AngleExtent >= 0`

**`ScaleMin`** (input_control)  number(-array) `→`  (real)

Minimum scale of the model.

Default:
0.9

Suggested values:
0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Restriction:
`ScaleMin > 0`

**`ScaleMax`** (input_control)  number(-array) `→`  (real)

Maximum scale of the model.

Default:
1.1

Suggested values:
1.0, 1.1, 1.2, 1.3, 1.4, 1.5

Restriction:
`ScaleMax >= ScaleMin`

**`Optimization`** (input_control)  string `→`  (string)

Kind of optimization.

Default:
'auto'

List of values:
'auto', 'none', 'point_reduction_high', 'point_reduction_low', 'point_reduction_medium'

**`Metric`** (input_control)  string `→`  (string)

Match metric.

Default:
'use_polarity'

List of values:
'ignore_color_polarity', 'ignore_global_polarity', 'ignore_local_polarity', 'use_polarity'

**`Contrast`** (input_control)  number(-array) `→`  (integer / string)

Threshold or hysteresis thresholds for the contrast
of the object in the template image and optionally
minimum size of the object parts.

Default:
'auto'

Suggested values:
'auto', 'auto_contrast', 'auto_contrast_hyst', 'auto_min_size', 10, 20, 30, 40, 60, 80, 100, 120, 140, 160

**`MinContrast`** (input_control)  integer `→`  (integer / string)

Minimum contrast of the objects in the search images.

Default:
'auto'

Suggested values:
'auto', 1, 2, 3, 5, 7, 10, 20, 30, 40

Restriction:
`MinContrast < Contrast`

**`Parameters`** (input_control)  string(-array) `→`  (string)

Parameters to be determined automatically.

Default:
'all'

List of values:
'all', 'angle_step', 'contrast', 'contrast_hyst', 'min_contrast', 'min_size', 'num_levels', 'optimization', 'scale_c_step', 'scale_r_step', 'scale_step'

**`ParameterName`** (output_control)  string-array `→`  (string)

Name of the automatically determined parameter.

**`ParameterValue`** (output_control)  number-array `→`  (real / integer)

Value of the automatically determined parameter.

## Result

If the parameters are valid, the operator
`determine_shape_model_params` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised. If the parameters
*`NumLevels`* and *`Contrast`* are chosen such that the
model contains too few points, or the input image does not contain a
sufficient number of significant features, the error 8510 is
raised.

## Possible Predecessors

`draw_region`,
`reduce_domain`,
`threshold`

## Possible Successors

`create_generic_shape_model`

## Module

Matching
