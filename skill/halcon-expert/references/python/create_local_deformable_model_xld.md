# create_local_deformable_model_xld (Operator)

## Name

`create_local_deformable_model_xld` — Prepare a deformable model for local deformable matching from XLD contours.

## Signature

`def create_local_deformable_model_xld(contours: HObject, num_levels: Union[int, str], angle_start: Sequence[float], angle_extent: Sequence[float], angle_step: Union[float, str], scale_rmin: float, scale_rmax: Sequence[float], scale_rstep: Union[float, str], scale_cmin: float, scale_cmax: Sequence[float], scale_cstep: Union[float, str], optimization: MaybeSequence[str], metric: str, min_contrast: int, gen_param_name: Sequence[str], gen_param_value: Sequence[Union[int, float, str]]) -> HHandle`

## Description

The operator `create_local_deformable_model_xld` creates a
deformable model used for local deformable matching from the XLD contours
passed in *`contours`*. The XLD contours represent the gray-value edges
of the object to be searched for. In contrast to the operator
[`create_local_deformable_model`](create_local_deformable_model.md), which creates a deformable
model from a template image, the operator
`create_local_deformable_model_xld` creates the deformable
model from XLD contours.

The center of gravity of the smallest surrounding rectangle of the
*`contours`* that is parallel to the coordinate axes is used as the origin
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

**`contours`** (input_object)  xld_cont(-array) `→` HObject

Input contours that will be used to create the model.

**`num_levels`** (input_control)  integer `→` Union[int, str]

Maximum number of pyramid levels.

Default:
"auto"

List of values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "auto"

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
`ScaleRStep > 0`

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
`ScaleCStep > 0`

**`optimization`** (input_control)  string(-array) `→` MaybeSequence[str]

Kind of optimization used for generating the model.

Default:
"auto"

List of values:
"auto", "none", "point_reduction_high", "point_reduction_low", "point_reduction_medium"

**`metric`** (input_control)  string `→` str

Match metric.

Default:
"ignore_local_polarity"

List of values:
"ignore_color_polarity", "ignore_global_polarity", "ignore_local_polarity", "ignore_part_polarity", "use_polarity"

**`min_contrast`** (input_control)  number `→` int

Minimum contrast of the objects in the search images.

Default:
5

Suggested values:
1, 2, 3, 5, 7, 10, 20, 30, 40

**`gen_param_name`** (input_control)  string-array `→` Sequence[str]

The generic parameter names.

Default:
[]

List of values:
[], "part_size"

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
`create_local_deformable_model_xld` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised. If the parameter *`num_levels`* is
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
