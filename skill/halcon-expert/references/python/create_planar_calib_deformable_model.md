# create_planar_calib_deformable_model (Operator)

## Name

`create_planar_calib_deformable_model` — Create a deformable model for calibrated perspective matching.

## Signature

`def create_planar_calib_deformable_model(template: HObject, cam_param: Sequence[Union[float, int, str]], reference_pose: Sequence[Union[float, int]], num_levels: Union[int, str], angle_start: Sequence[float], angle_extent: Sequence[float], angle_step: Union[float, str], scale_rmin: float, scale_rmax: Sequence[float], scale_rstep: Union[float, str], scale_cmin: float, scale_cmax: Sequence[float], scale_cstep: Union[float, str], optimization: MaybeSequence[str], metric: str, contrast: Sequence[Union[int, str]], min_contrast: Union[int, str], gen_param_name: Sequence[str], gen_param_value: Sequence[Union[int, float, str]]) -> HHandle`

## Description

The operator `create_planar_calib_deformable_model` creates a
deformable model for planar calibrated matching based on the input image
*`template`*.

The model ROI corresponds to the domain of *`template`*.
The model is generated for multiple image pyramid levels and is
stored in memory. The output parameter
*`model_id`* is a handle for this model and is used in subsequent
calls to [`find_planar_calib_deformable_model`](find_planar_calib_deformable_model.md).

The internal camera parameters are provided in *`cam_param`*. The
internal parameters can typically be determined using
[`calibrate_cameras`](calibrate_cameras.md). By providing *`cam_param`* it is possible to
retrieve a 3D pose of the model as a result of the planar calibrated matching.
See [`create_planar_uncalib_deformable_model`](create_planar_uncalib_deformable_model.md) on how to progress
without using calibration data. See
`“Solution Guide II-B - Matching”` for more information on
these approaches.

![figure](../assets/7c1f6bc4cc4b9bf1.svg)

Scheme of the reference pose *`reference_pose`* in relation to the
absolute pose of the model as projected from the image into the
model plane.

The x- and y-axis of the reference pose *`reference_pose`*
$(x^{r},y^{r},z^{r})$ determine the 3D model plane, thus the
plane in the world coordinate system, the model is located in (see
scheme above).
The 3D model plane can be obtained by using [`calibrate_cameras`](calibrate_cameras.md) or
[`vector_to_pose`](vector_to_pose.md), e.g., by placing and localizing a calibration plate
in the same plane as the model is located in.

The model's origin is located in the center of gravity of the model region
in *`template`*. The projection of this image point onto the 3D model
plane determined by *`reference_pose`* corresponds to the absolute
3D pose of the model $(x^{m},y^{m},z^{m})$. The projection
is depicted in the scheme above. After the model creation you can query
the absolute pose of the model in world coordinates using
[`get_deformable_model_params`](get_deformable_model_params.md).
The 3D pose of the model differs from the reference pose by a
2D translation in the model plane.

Further input parameters that specify the model are described in
[`create_planar_uncalib_deformable_model`](create_planar_uncalib_deformable_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`template`** (input_object)  (multichannel-)image `→` HObject (byte / uint2)

Input image whose domain will be used to create
the model.

**`cam_param`** (input_control)  campar `→` Sequence[Union[float, int, str]]

The parameters of the internal orientation of the
camera.

**`reference_pose`** (input_control)  pose `→` Sequence[Union[float, int]]

The reference pose of the object in the reference
image.

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

Scale step length (resolution) in the column direction.

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

The parameter names.

Default:
[]

List of values:
[], "part_size"

**`gen_param_value`** (input_control)  integer-array `→` Sequence[Union[int, float, str]]

Values of the parameters.

Default:
[]

List of values:
[], "big", "medium", "small"

**`model_id`** (output_control)  deformable_model `→` HHandle

Handle of the model.

## Result

If the parameters are valid, the operator
`create_planar_calib_deformable_model` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`determine_deformable_model_params`

## Possible Successors

`set_deformable_model_origin`,
`set_deformable_model_param`,
`get_deformable_model_contours`,
`find_planar_calib_deformable_model`,
`get_deformable_model_params`,
`write_deformable_model`,
`clear_deformable_model`

## Alternatives

`read_deformable_model`

## See also

`create_planar_uncalib_deformable_model`

## Module

Matching
