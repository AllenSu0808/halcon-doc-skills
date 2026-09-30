# create_local_deformable_model (Operator)

## Name

`create_local_deformable_model` — Creates a deformable model for local, deformable matching.

## Signature

`def create_local_deformable_model(template: HObject, num_levels: Union[int, str], angle_start: Sequence[float], angle_extent: Sequence[float], angle_step: Union[float, str], scale_rmin: float, scale_rmax: Sequence[float], scale_rstep: Union[float, str], scale_cmin: float, scale_cmax: Sequence[float], scale_cstep: Union[float, str], optimization: MaybeSequence[str], metric: str, contrast: Sequence[Union[int, str]], min_contrast: Union[int, str], gen_param_name: Sequence[str], gen_param_value: Sequence[Union[int, float, str]]) -> HHandle`

## Description

The operator `create_local_deformable_model` prepares a
template, which is passed in the image *`template`*, as a deformable
model used for local deformable matching. The ROI of the model is passed as
the domain of *`template`*.

The local deformable matching can be used to detect an object that is
distorted by a local deformation, estimate the deformation,
and rectify the image area where the object is found. For a distinction from
further matching methods we refer to the `“Solution Guide I”`
chapter '2D Matching'.

As described in [`create_planar_uncalib_deformable_model`](create_planar_uncalib_deformable_model.md), the origin
(reference point) of the model is defined as the center of gravity of the
domain (region) of the model image *`template`*. Further, the
axis-aligned enclosing rectangle of the domain of the *`template`* is
used to determine the area of the search image that is rectified in calls of
[`find_local_deformable_model`](find_local_deformable_model.md).

For further explanation on the parameters used for the creation of a local
deformable model we refer to the description of
[`create_planar_uncalib_deformable_model`](create_planar_uncalib_deformable_model.md). Note, that the parameters
of the actual deformation are set with the call of
[`find_local_deformable_model`](find_local_deformable_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`template`** (input_object)  (multichannel-)image `→` HObject (byte / uint2)

Input image whose domain will be used to create
the model.

**`num_levels`** (input_control)  integer `→` Union[int, str]

Maximum number of pyramid levels.

Default:
"auto"

List of values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "auto"

**`angle_start`** (input_control)  angle.rad-array `→` Sequence[float]

This parameter is not used.

Default:
[]

**`angle_extent`** (input_control)  angle.rad-array `→` Sequence[float]

This parameter is not used.

Default:
[]

**`angle_step`** (input_control)  angle.rad `→` Union[float, str]

Step length of the angles (resolution).

Default:
"auto"

Suggested values:
"auto", 0.0175, 0.0349, 0.0524, 0.0698, 0.0873

Restriction:
`AngleStep > 0 && AngleStep <= pi / 16`

**`scale_rmin`** (input_control)  number `→` float

Minimum scale of the pattern in row direction.

Default:
1.0

Suggested values:
0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Restriction:
`ScaleRMin > 0`

**`scale_rmax`** (input_control)  number-array `→` Sequence[float]

This parameter is not used.

Default:
[]

**`scale_rstep`** (input_control)  number `→` Union[float, str]

Scale step length (resolution) in row direction.

Default:
"auto"

Suggested values:
"auto", 0.01, 0.02, 0.05, 0.1, 0.15, 0.2

Restriction:
`ScaleRStep >= 0`

**`scale_cmin`** (input_control)  number `→` float

Minimum scale of the pattern in column direction.

Default:
1.0

Suggested values:
0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Restriction:
`ScaleCMin > 0`

**`scale_cmax`** (input_control)  number-array `→` Sequence[float]

This parameter is not used.

Default:
[]

**`scale_cstep`** (input_control)  number `→` Union[float, str]

Scale step length (resolution) in column direction.

Default:
"auto"

Suggested values:
"auto", 0.01, 0.02, 0.05, 0.1, 0.15, 0.2

Restriction:
`ScaleCStep >= 0`

**`optimization`** (input_control)  string(-array) `→` MaybeSequence[str]

Kind of optimization used for generating the model.

Default:
"none"

List of values:
"auto", "none", "point_reduction_high", "point_reduction_low", "point_reduction_medium"

**`metric`** (input_control)  string `→` str

Match metric.

Default:
"use_polarity"

List of values:
"ignore_color_polarity", "ignore_global_polarity", "ignore_local_polarity", "ignore_part_polarity", "use_polarity"

**`contrast`** (input_control)  number-array `→` Sequence[Union[int, str]]

Thresholds or hysteresis thresholds for the contrast
of the object in the template image.

Default:
"auto"

Suggested values:
"auto", 10, 20, 30, 40, 60, 80, 100, 120, 140, 160

**`min_contrast`** (input_control)  number `→` Union[int, str]

Minimum contrast of the objects in the search images.

Default:
"auto"

Suggested values:
"auto", 1, 2, 3, 5, 7, 10, 20, 30, 40

Restriction:
`MinContrast < Contrast`

**`gen_param_name`** (input_control)  string-array `→` Sequence[str]

The generic parameter names.

Default:
[]

List of values:
[], "min_size", "part_size"

**`gen_param_value`** (input_control)  integer-array `→` Sequence[Union[int, float, str]]

Values of the generic parameters.

Default:
[]

List of values:
[], "big", "medium", "small"

**`model_id`** (output_control)  deformable_model `→` HHandle

Handle of the model.

## Result

If the parameters are valid, the operator
`create_local_deformable_model` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`determine_deformable_model_params`

## Possible Successors

`set_deformable_model_origin`,
`set_deformable_model_param`,
`get_deformable_model_contours`,
`find_local_deformable_model`,
`get_deformable_model_params`,
`write_deformable_model`,
`clear_deformable_model`

## Alternatives

`read_deformable_model`

## See also

`create_planar_uncalib_deformable_model`,
`create_planar_calib_deformable_model`

## Module

Matching
