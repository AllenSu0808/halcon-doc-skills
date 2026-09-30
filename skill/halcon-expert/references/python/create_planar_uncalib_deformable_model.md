# create_planar_uncalib_deformable_model (Operator)

## Name

`create_planar_uncalib_deformable_model` — Creates a deformable model for uncalibrated, perspective matching.

## Signature

`def create_planar_uncalib_deformable_model(template: HObject, num_levels: Union[int, str], angle_start: Sequence[float], angle_extent: Sequence[float], angle_step: Union[float, str], scale_rmin: float, scale_rmax: Sequence[float], scale_rstep: Union[float, str], scale_cmin: float, scale_cmax: Sequence[float], scale_cstep: Union[float, str], optimization: MaybeSequence[str], metric: str, contrast: Sequence[Union[int, str]], min_contrast: Union[int, str], gen_param_name: Sequence[str], gen_param_value: Sequence[Union[int, float, str]]) -> HHandle`

## Description

The operator `create_planar_uncalib_deformable_model` prepares a
template, which is passed in the image *`template`*, as a deformable
model used for uncalibrated perspective matching. The ROI of the model is
passed as the domain of *`template`*.

The planar uncalibrated matching can be used to detect planar objects
or planar subparts of non-planar objects that are distorted by a projective
view.

This is an alternative to [`create_generic_shape_model`](create_generic_shape_model.md),
where typically the search image must be rectified by
[`calibrate_cameras`](calibrate_cameras.md) and [`gen_image_to_world_plane_map`](gen_image_to_world_plane_map.md)
beforehand.

In contrast to [`create_shape_model_3d`](create_shape_model_3d.md) there is no need to
pre-generate different views of an object, resulting into a smaller memory
consumption. Hence, in case of a planar perspectively distorted object,
`create_planar_uncalib_deformable_model` should be preferred.

The model is generated using multiple image pyramid levels and is
stored in memory. The output parameter
*`model_id`* is a handle for this model, which is used in
subsequent calls to [`find_planar_uncalib_deformable_model`](find_planar_uncalib_deformable_model.md).

### Input parameters in detail

- ***`num_levels`*:** —

  The number of pyramid levels is determined with the parameter
  *`num_levels`*. It should be chosen as large as possible
  because by this the time necessary to find the object is
  significantly reduced. On the other hand, *`num_levels`* must
  be chosen such that the model is still recognizable and contains a
  sufficient number of points on the highest pyramid level. If not enough
  model points are generated, the number of pyramid levels is reduced
  internally until enough model points are found on the highest pyramid level.
  If this procedure would lead to a model with no pyramid levels, i.e., if the
  number of model points is already too small on the lowest pyramid level,
  `create_planar_uncalib_deformable_model` returns with an error message.
  If *`num_levels`* is set to *"auto"*,
  `create_planar_uncalib_deformable_model` determines the number of
  pyramid levels automatically. The automatically computed number of pyramid
  levels can be queried using [`get_deformable_model_params`](get_deformable_model_params.md). In rare
  cases, it might happen that `create_planar_uncalib_deformable_model`
  determines a value for the number of pyramid levels that is too
  large or too small. If the number of pyramid levels is chosen too
  large, the model may not be recognized in the image or it may be
  necessary to select very low parameters for `min_score` or
  `greediness` in [`find_planar_uncalib_deformable_model`](find_planar_uncalib_deformable_model.md) in order
  to find the model.
  If the number of pyramid levels is chosen too small, the time required
  to find the model in [`find_planar_uncalib_deformable_model`](find_planar_uncalib_deformable_model.md) increases.
  In these cases, the number of pyramid levels should be selected using the
  output of [`inspect_shape_model`](inspect_shape_model.md).
- ****Angle and Scale parameters:**** —

  Note that the parameters *`angle_start`*, *`angle_extent`*,
  *`scale_rmax`*, and *`scale_cmax`* are not used by this operator.
  Instead, they have to be specified within the operator
  [`find_planar_uncalib_deformable_model`](find_planar_uncalib_deformable_model.md). *`scale_rmin`* and
  *`scale_cmin`* can be relevant if you expect matches that are
  smaller than in the original image *`template`*. Then, if
  *`num_levels`* is set to *"auto"*, the number of used pyramid
  levels may decrease.

  Generally, the parameters *`angle_step`*, *`scale_rstep`* and
  *`scale_cstep`* can be determined automatically. The automatically
  computed angle and scale step lengths can be queried using
  [`get_deformable_model_params`](get_deformable_model_params.md). For more information
  about how these parameters work, please refer to the operator
  [`find_planar_uncalib_deformable_model`](find_planar_uncalib_deformable_model.md).
- ***`optimization`*:** —

  For particularly large models, it may be useful to reduce the number
  of model points by setting *`optimization`* to a value
  different from *"none"*. If *`optimization`* =
  *"none"*, all model points are stored. In all other cases,
  the number of points is reduced according to the value of
  *`optimization`*.
  If the number of points is reduced, it may be necessary in
  [`find_planar_uncalib_deformable_model`](find_planar_uncalib_deformable_model.md) to set the parameter
  `score` and `greediness` to a smaller value as, e.g.,
  *0.7* or *0.8*.
  For small models, the reduction of the number of model points does not result
  in a speed-up of the search because in this case usually
  significantly more potential instances of the model must be
  examined. If *`optimization`* is set to *"auto"*,
  `create_planar_uncalib_deformable_model` automatically determines the
  reduction of the number of model points.
- ***`contrast`*:** —

  The parameter *`contrast`* determines the contrast the model
  points (edges) must have. The contrast is a measure for local gray value
  differences between the object and the background and between
  different parts of the object. *`contrast`* should be chosen
  such that only the significant features of the template are used for
  the model.

  The following values can be set for *`contrast`*:

  - A single contrast value. You can set:

    - an integer value: the manually determined value is used.
    - *"auto_contrast"*: the contrast value is computed
      automatically.
  - Hysteresis thresholds. In this case, the model is segmented using a
    method similar to the hysteresis threshold method used in
    [`edges_image`](edges_image.md).
    For more information about the hysteresis threshold method, see
    [`hysteresis_threshold`](hysteresis_threshold.md).
    You can set:

    - A tuple of two values: The first value determines the lower
      threshold, the second value determines the upper threshold.
    - *"auto"* (default value) or *"auto_contrast_hyst"*:
      The hysteresis thresholds are computed automatically.

  In certain cases, it might happen that the automatic determination of the
  contrast thresholds is not satisfying. For example, a manual setting of these
  parameters should be preferred if certain model components should be included
  or suppressed because of application-specific reasons or if the object
  contains several different contrasts. Therefore, the contrast
  thresholds should be automatically determined with
  [`determine_deformable_model_params`](determine_deformable_model_params.md) and subsequently verified using
  [`inspect_shape_model`](inspect_shape_model.md) before calling
  `create_planar_uncalib_deformable_model`. Note that
  *`min_contrast`* influences the automatic contrast estimation, and
  hence also the estimation of the minimum size.
- ***`min_contrast`*:** —

  With *`min_contrast`*, it can be determined which minimal contrast the
  model must have in the recognition performed by
  [`find_planar_uncalib_deformable_model`](find_planar_uncalib_deformable_model.md). In other words, this parameter
  separates the model from the noise in the image. Therefore, a good
  choice is the range of gray value changes caused by the noise in the
  image. If, for example, the gray values fluctuate within a range of
  10 gray levels, *`min_contrast`* should be set to 10.
  Obviously, *`min_contrast`* must be smaller than *`contrast`*. If
  the model should be recognized in very low contrast images,
  *`min_contrast`* must be set to a correspondingly small value. If the
  model should be recognized even if it is severely occluded,
  *`min_contrast`* should be slightly larger than the range of gray value
  fluctuations created by noise in order to ensure that the position and
  rotation of the model are extracted robustly and accurately by
  [`find_planar_uncalib_deformable_model`](find_planar_uncalib_deformable_model.md). If *`min_contrast`* is set
  to *"auto"*, the minimum contrast is determined automatically
  based on the noise in the model image. Consequently, an automatic
  determination only makes sense if the image noise during the recognition is
  similar to the noise in the model image. Furthermore, in some cases it is
  advisable to increase the automatically determined value in order to
  increase the robustness against occlusions (see above). The automatically
  computed minimum contrast can be queried using
  [`get_deformable_model_params`](get_deformable_model_params.md). The *`min_contrast`* of a deformable
  model can later be changed with the help of
  [`set_deformable_model_param`](set_deformable_model_param.md).
- ***`metric`*:** —

  The parameter *`metric`* determines the conditions under which
  the model is recognized in the image. If *`metric`* =
  *"use_polarity"*, the object in the image and the model must
  have the same contrast. If, for example, the model is a bright
  object on a dark background, the object is found only if it is also
  brighter than the background. If *`metric`* =
  *"ignore_global_polarity"*, the object is found in the image
  also if the contrast reverses globally. In the above example, the
  object hence is also found if it is darker than the background. The runtime
  of [`find_planar_uncalib_deformable_model`](find_planar_uncalib_deformable_model.md) will increase slightly in
  this case. If *`metric`* = *"ignore_part_polarity"*, the
  the contrast polarity is allowed to change only between different
  parts of the model, whereas the polarity of model points that are
  within the same model part must not change. Please note that the
  term *"ignore_part_polarity"* is capable of being
  misunderstood. It means that polarity changes between
  neighboring model parts do not influence the score, and hence
  are ignored. If *`metric`* = *"ignore_local_polarity"*,
  the model is found even if the contrast changes for each individual model
  point. This mode can, for example, be useful if the object consists of a part
  with medium gray value, within which either darker or brighter
  sub-objects lie. In this case the runtime of
  [`find_planar_uncalib_deformable_model`](find_planar_uncalib_deformable_model.md) increases significantly. The
  above four metrics can only be applied to single-channel images. If a
  multichannel image is used as the model image or as the search image only the
  first channel will be used (and no error message will be returned). If
  *`metric`* = *"ignore_color_polarity"*, the model is
  found even if the color contrast changes locally. This is, for
  example, the case if parts of the object can change their color,
  e.g., from red to green. In particular, this mode is useful if it
  is not known in advance in which channels the object is visible. In
  this mode, the runtime of [`find_planar_uncalib_deformable_model`](find_planar_uncalib_deformable_model.md) can
  also increase significantly. The metric *"ignore_color_polarity"* can
  be used for images with an arbitrary number of channels. If it is used
  for single-channel images it has the same effect as
  *"ignore_local_polarity"*. It should be noted that for
  *`metric`* = *"ignore_color_polarity"* the number of
  channels in the model creation with
  `create_planar_uncalib_deformable_model` and in the search with
  [`find_planar_uncalib_deformable_model`](find_planar_uncalib_deformable_model.md) can be different. This
  can, for example, be used to create a model from a synthetically
  generated single-channel image. Furthermore, it should be noted
  that the channels do not need to contain a spectral subdivision of
  the light (like in an RGB image). The channels can, for example,
  also contain images of the same object that were obtained by
  illuminating the object from different directions.
- ***`gen_param_name`*, *`gen_param_value`*:** —

  With the help of the generic parameters *`gen_param_name`* and
  *`gen_param_value`*, the user can set parameters for the deformable model
  generation.

  The following parameters can be set for *`gen_param_name`*.

  - ***"part_size"*:** —

    Adapts the average size of the sub-parts
    that the deformable model should consist of.
    For objects that consist of many small contours, *"small"*
    should be selected. For objects that consist of only big contours,
    *"big"* should be set.

    List of values:
     *"small"*, *"medium"*, *"big"*

    Default:
     *"big"*.
  - ***"min_size"*:** —

    Determines a threshold for the selection of
    significant model components based on the size of the components,
    i.e., components that have fewer points than the minimum size specified
    in the corresponding *`gen_param_value`* are suppressed.
    This threshold for the minimum size is divided by two for each
    successive pyramid level. *"min_size"* can be set to an
    arbitrary integer value greater or equal *0*.
    It can also be set to *"auto"* which means that
    the minimum size will be determined automatically.

    Default:
     *"auto"*

  The center of gravity of the domain (region) of the model image
  *`template`* is used as the origin (reference point) of the model.
  A different origin for the model can be set with
  [`set_deformable_model_origin`](set_deformable_model_origin.md).

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

Values of the generic parameter.

Default:
[]

List of values:
[], "big", "medium", "small"

**`model_id`** (output_control)  deformable_model `→` HHandle

Handle of the model.

## Result

If the parameters are valid, the operator
`create_planar_uncalib_deformable_model` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`determine_deformable_model_params`

## Possible Successors

`set_deformable_model_origin`,
`set_deformable_model_param`,
`get_deformable_model_contours`,
`find_planar_uncalib_deformable_model`,
`get_deformable_model_params`,
`write_deformable_model`,
`clear_deformable_model`

## Alternatives

`read_deformable_model`

## Module

Matching
