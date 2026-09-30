# CreateScaledShapeModel (Operator)

## Name

`CreateScaledShapeModel` — Prepare an isotropically scaled shape model for matching.

## Signature

`static void HOperatorSet.CreateScaledShapeModel(HObject template, HTuple numLevels, HTuple angleStart, HTuple angleExtent, HTuple angleStep, HTuple scaleMin, HTuple scaleMax, HTuple scaleStep, HTuple optimization, HTuple metric, HTuple contrast, HTuple minContrast, out HTuple modelID)`

`public HShapeModel(HImage template, HTuple numLevels, double angleStart, double angleExtent, HTuple angleStep, double scaleMin, double scaleMax, HTuple scaleStep, HTuple optimization, string metric, HTuple contrast, HTuple minContrast)`

`public HShapeModel(HImage template, int numLevels, double angleStart, double angleExtent, double angleStep, double scaleMin, double scaleMax, double scaleStep, string optimization, string metric, int contrast, int minContrast)`

`void HShapeModel.CreateScaledShapeModel(HImage template, HTuple numLevels, double angleStart, double angleExtent, HTuple angleStep, double scaleMin, double scaleMax, HTuple scaleStep, HTuple optimization, string metric, HTuple contrast, HTuple minContrast)`

`void HShapeModel.CreateScaledShapeModel(HImage template, int numLevels, double angleStart, double angleExtent, double angleStep, double scaleMin, double scaleMax, double scaleStep, string optimization, string metric, int contrast, int minContrast)`

`HShapeModel HImage.CreateScaledShapeModel(HTuple numLevels, double angleStart, double angleExtent, HTuple angleStep, double scaleMin, double scaleMax, HTuple scaleStep, HTuple optimization, string metric, HTuple contrast, HTuple minContrast)`

`HShapeModel HImage.CreateScaledShapeModel(int numLevels, double angleStart, double angleExtent, double angleStep, double scaleMin, double scaleMax, double scaleStep, string optimization, string metric, int contrast, int minContrast)`

## Description

The operator `CreateScaledShapeModel` prepares a template,
which is passed in the image *`template`*, as an isotropically scaled
shape model used for matching. The ROI of the model is passed
as the domain of *`template`*.

The output parameter *`modelID`* is a handle for this model, which is
used in subsequent calls to [`FindScaledShapeModel`](find_scaled_shape_model.md).
The center of gravity of the domain (region) of the model image
*`template`* is used as the origin (reference point) of the
model. A different origin can be set with [`SetShapeModelOrigin`](set_shape_model_origin.md).
The model is generated using multiple image pyramid levels and is
stored in memory. If a complete pregeneration of the model is
selected (see below), the model is generated at multiple rotations
and scales on each level. The model can be extended by clutter parameters
with [`SetShapeModelClutter`](set_shape_model_clutter.md).

### Input parameters in detail

- ***`numLevels`*:** —

  The number of pyramid levels is determined with the parameter
  *`numLevels`*. It should be chosen as large as possible
  because by this the time necessary to find the object is
  significantly reduced. On the other hand, *`numLevels`* must
  be chosen such that the model is still recognizable and contains a
  sufficient number of points (at least four) on the highest pyramid
  level. This can be checked using the output of
  [`InspectShapeModel`](inspect_shape_model.md). If not enough model points are
  generated, the number of pyramid levels is reduced internally until
  enough model points are found on the highest pyramid level. If this
  procedure would lead to a model with no pyramid levels, i.e., if the
  number of model points is already too small on the lowest pyramid
  level, `CreateScaledShapeModel` returns with an error
  message.

  If *`numLevels`* is set to *"auto"* (or *0* for backwards
  compatibility), `CreateScaledShapeModel` determines the number
  of pyramid levels automatically. The automatically computed number of
  pyramid levels can be queried using [`GetShapeModelParams`](get_shape_model_params.md).
  In rare cases, it might happen that `CreateScaledShapeModel`
  determines a value for the number of pyramid levels that is too
  large or too small. If the number of pyramid levels is chosen too
  large, the model may not be recognized in the image or it may be
  necessary to select very low parameters for `minScore` or
  `greediness` in [`FindScaledShapeModel`](find_scaled_shape_model.md) in order to find the
  model.
  If the number of pyramid levels is chosen too small, the time required
  to find the model in [`FindScaledShapeModel`](find_scaled_shape_model.md) may increase.
  In these cases, the number of pyramid levels should be selected
  using the output of [`InspectShapeModel`](inspect_shape_model.md).
- ***`angleStart`*, *`angleExtent`* and *`angleStep`*:** —

  The parameters *`angleStart`* and *`angleExtent`*
  determine the range of possible rotations, in which the model can
  occur in the image. Note that the model can only be found in this
  range of angles by [`FindScaledShapeModel`](find_scaled_shape_model.md). The parameter
  *`angleStep`* determines the step length within the selected
  range of angles. Hence, if subpixel accuracy is not specified in
  [`FindScaledShapeModel`](find_scaled_shape_model.md), this parameter specifies the
  accuracy that is achievable for the angles in
  [`FindScaledShapeModel`](find_scaled_shape_model.md). *`angleStep`* should be
  chosen based on the size of the object. Smaller models do not have
  many different discrete rotations in the image, and hence
  *`angleStep`* should be chosen larger for smaller models. If
  *`angleExtent`* is not an integer multiple of
  *`angleStep`*, *`angleStep`* is modified accordingly.
  To ensure that for model instances without rotation angle values of
  exactly 0.0 are returned by [`FindScaledShapeModel`](find_scaled_shape_model.md),
  the range of possible
  rotations is modified as follows: If there is no positive integer
  value n such that *`angleStart`* plus n times
  *`angleStep`* is exactly 0.0, *`angleStart`* is decreased
  by up to *`angleStep`* and *`angleExtent`* is increased by
  *`angleStep`*.
- ***`scaleMin`*, *`scaleMax`*, and *`scaleStep`*:** —

  The parameters *`scaleMin`* and *`scaleMax`* determine the
  range of possible scales (sizes) of the model. A scale of 1
  corresponds to the original size of the model. The parameter
  *`scaleStep`* determines the step length within the selected
  range of scales. Hence, if subpixel accuracy is not specified in
  [`FindScaledShapeModel`](find_scaled_shape_model.md), this parameter specifies the
  accuracy that is achievable for the scales in
  [`FindScaledShapeModel`](find_scaled_shape_model.md). Like *`angleStep`*,
  *`scaleStep`* should be chosen based on the size of the object.
  If the range of scales is not an integer multiple of
  *`scaleStep`*, *`scaleStep`* is modified accordingly.
  To ensure that for model instances that are not scaled scale values of
  exactly 1.0 are returned by [`FindScaledShapeModel`](find_scaled_shape_model.md),
  the range of possible
  scales is modified as follows: If there is no positive integer value
  n such that *`scaleMin`* plus n times *`scaleStep`* is
  exactly 1.0, *`scaleMin`* is decreased by up to
  *`scaleStep`* and *`scaleMax`* is increased such that the
  range of possible scales is increased by *`scaleStep`*.
- ***`optimization`*:** —

  For particularly large models, it may be useful to reduce the number
  of model points by setting *`optimization`* to a value
  different from *"none"*. If *`optimization`* =
  *"none"*, all model points are stored. In all other cases,
  the number of points is reduced according to the value of
  *`optimization`*. If the number of points is reduced, it may
  be necessary in [`FindScaledShapeModel`](find_scaled_shape_model.md) to set the parameter
  `greediness` to a smaller value, e.g., *0.7* or *0.8*.
  For small models, the reduction of the number of model points does not result
  in a speed-up of the search because in this case usually
  significantly more potential instances of the model must be
  examined.

  If *`optimization`* is set to *"auto"*,
  `CreateScaledShapeModel` automatically determines the
  reduction of the number of model points.
- ***`metric`*:** —

  The parameter *`metric`* determines the conditions under which
  the model is recognized in the image.

  If *`metric`* = *"use_polarity"*, the object in the image and
  the model must have the same contrast. If, for example, the model is a
  bright object on a dark background, the object is found only if it is also
  brighter than the background.

  If *`metric`* = *"ignore_global_polarity"*, the object is
  found in the image also if the contrast reverses globally. In the above
  example, the object hence is also found if it is darker than the background.
  The runtime of [`FindScaledShapeModel`](find_scaled_shape_model.md) will increase slightly in
  this case.

  If *`metric`* = *"ignore_local_polarity"*,
  the model is found even if the contrast changes locally. This mode
  can, for example, be useful if the object consists of a part with
  medium gray value, within which either darker or brighter
  sub-objects lie. Since in this case the runtime of
  [`FindScaledShapeModel`](find_scaled_shape_model.md) increases significantly, it is
  usually better to create several models that reflect the possible
  contrast variations of the object with
  `CreateScaledShapeModel`, and to match them simultaneously
  with [`FindScaledShapeModels`](find_scaled_shape_models.md).

  The above three metrics can only be applied to single-channel images.
  If a multichannel image is used as the model image or as the search image,
  only the first channel will be used (and no error message will be returned).

  If *`metric`* = *"ignore_color_polarity"*, the model is
  found even if the color contrast changes locally. This is, for
  example, the case if parts of the object can change their color,
  e.g., from red to green. In particular, this mode is useful if it
  is not known in advance in which channels the object is visible. In
  this mode, the runtime of [`FindScaledShapeModel`](find_scaled_shape_model.md) can also
  increase significantly. The metric *"ignore_color_polarity"*
  can be used for images with an arbitrary number of channels. If it
  is used for single-channel images it has the same effect as
  *"ignore_local_polarity"*. It should be noted that for
  *`metric`* = *"ignore_color_polarity"* the number of
  channels in the model creation with
  `CreateScaledShapeModel` and in the search with
  [`FindScaledShapeModel`](find_scaled_shape_model.md) can be different. This can, for
  example, be used to create a model from a synthetically generated
  single-channel image. Furthermore, it should be noted that the
  channels do not need to contain a spectral subdivision of the light
  (like in an RGB image). The channels can, for example, also contain
  images of the same object that were obtained by illuminating the
  object from different directions.
- ***`contrast`*:** —

  The parameter *`contrast`* determines the contrast the model
  points must have. The contrast is a measure for local gray value
  differences between the object and the background and between
  different parts of the object. *`contrast`* should be chosen
  such that only the significant features of the template are used for
  the model. *`contrast`* can also contain a tuple with two
  values. In this case, the model is segmented using a method similar
  to the hysteresis threshold method used in [`EdgesImage`](edges_image.md).
  Here, the first element of the tuple determines the lower threshold,
  while the second element determines the upper threshold. For more
  information about the hysteresis threshold method, see
  [`HysteresisThreshold`](hysteresis_threshold.md). Optionally, *`contrast`* can
  contain a third value as the last element of the tuple. This value
  determines a threshold for the selection of significant model
  components based on the size of the components, i.e., components
  that have fewer points than the minimum size thus specified are
  suppressed. As the minimum size is applied on the extent of the components,
  the derived model contours can still be smaller than the specified minimum
  size.
  This threshold for the minimum size is divided by two
  for each successive pyramid level. If small model components should
  be suppressed, but hysteresis thresholding should not be performed,
  nevertheless three values must be specified in *`contrast`*.
  In this case, the first two values can simply be set to identical
  values. The effect of this parameter can be checked in advance with
  [`InspectShapeModel`](inspect_shape_model.md).

  If *`contrast`* is set to *"auto"*,
  `CreateScaledShapeModel` determines the three above described
  values automatically. Besides, only the contrast
  (*"auto_contrast"*), the hysteresis thresholds
  (*"auto_contrast_hyst"*), or the minimum size
  (*"auto_min_size"*) can be determined automatically.
  The remaining values that are not determined automatically can
  additionally be passed in the form of a tuple. Also various
  combinations are allowed: If, for example,
  *["auto_contrast","auto_min_size"]* is passed, both the
  contrast and the minimum size are determined automatically. If
  *["auto_min_size",20,30]* is passed, the minimum size is
  determined automatically while the hysteresis thresholds are set to
  *20* and *30*, etc. In certain cases, it might happen
  that the automatic determination of the contrast thresholds is not
  satisfying. For example, a manual setting of these parameters should
  be preferred if certain model components should be included or
  suppressed because of application-specific reasons or if the object
  contains several different contrasts. Therefore, the contrast
  thresholds should be automatically determined with
  [`DetermineShapeModelParams`](determine_shape_model_params.md) and subsequently verified using
  [`InspectShapeModel`](inspect_shape_model.md) before calling
  `CreateScaledShapeModel`. Note that *`minContrast`*
  influences the automatic contrast estimation, and hence also the estimation
  of the minimum size.
- ***`minContrast`*:** —

  With *`minContrast`*, it can be determined which contrast the
  model must at least have in the recognition performed by
  [`FindScaledShapeModel`](find_scaled_shape_model.md). In other words, this parameter
  separates the model from the noise in the image. Therefore, a good
  choice is the range of gray value changes caused by the noise in the
  image. If, for example, the gray values fluctuate within a range of
  10 gray levels, *`minContrast`* should be set to 10. If
  multichannel images are used for the model and the search images,
  and if the parameter *`metric`* is set to
  *"ignore_color_polarity"* (see above) the noise in one
  channel must be multiplied by the square root of the number of
  channels to determine *`minContrast`*. If, for example, the
  gray values fluctuate within a range of 10 gray levels in a single
  channel and the image is a three-channel image *`minContrast`*
  should be set to 17. Obviously, *`minContrast`* must be
  smaller than *`contrast`*. If the model should be recognized
  in very low contrast images, *`minContrast`* must be set to a
  correspondingly small value. If the model should be recognized even
  if it is severely occluded, *`minContrast`* should be slightly
  larger than the range of gray value fluctuations created by noise in
  order to ensure that the position and rotation of the model are
  extracted robustly and accurately by
  [`FindScaledShapeModel`](find_scaled_shape_model.md).

  If *`minContrast`* is set to *"auto"*, the minimum contrast is
  determined automatically based on the noise in the model image.
  Consequently, an automatic determination only makes sense if the image noise
  during the recognition is similar to the noise in the model image.
  Furthermore, in some cases it is advisable to increase the
  automatically determined value in order to increase the robustness
  against occlusions (see above). The automatically computed minimum
  contrast can be queried using [`GetShapeModelParams`](get_shape_model_params.md).

### Complete pregeneration of the model

Optionally, a second value can be passed in *`optimization`*.
This value determines whether the model is pregenerated completely
or not. To do so, the second value of *`optimization`* must be
set to either *"pregeneration"* or
*"no_pregeneration"*. If the second value is not used (i.e.,
if only one value is passed), the mode that is set with
`set_system('pregenerate_shape_models',...)` is used. With
the default value (*"pregenerate_shape_models"* =
*"false"*), the model is not pregenerated completely. The
complete pregeneration of the model normally leads to slightly lower
runtimes because the model does not need to be transformed at
runtime. However, in this case, the memory requirements and the
time required to create the model are significantly higher. It
should also be noted that it cannot be expected that the two modes
return exactly identical results because transforming the model at
runtime necessarily leads to different internal data for the
transformed models than pregenerating the transformed models. For
example, if the model is not pregenerated completely,
[`FindScaledShapeModel`](find_scaled_shape_model.md) typically returns slightly lower
scores, which may require setting a slightly lower value for
`minScore` than for a completely pregenerated model.
Furthermore, the poses obtained by interpolation may differ slightly in the
two modes. If maximum accuracy is desired, the pose of the model should
be determined by least-squares adjustment.

If a complete pregeneration of the model is selected,
the model is pregenerated for the selected angle and scale range
and stored in memory. The memory required to store the model is
proportional to the number of angle steps, the number of scale
steps, and the number of points in the model. Hence, if
*`angleStep`* or *`scaleStep`* are too small or
*`angleExtent`* or the range of scales are too big, it may
happen that the model no longer fits into the (virtual) memory. In
this case, either *`angleStep`* or *`scaleStep`* must be
enlarged or *`angleExtent`* or the range of scales must be
reduced. In any case, it is desirable that the model completely
fits into the main memory, because this avoids paging by the
operating system, and hence the time to find the object will be much
smaller. Since angles can be determined with subpixel resolution by
[`FindScaledShapeModel`](find_scaled_shape_model.md), *`angleStep`* >= 1° and *`scaleStep`* >= 0.02 can be selected for models of a
diameter smaller than about 200 pixels.

If *`angleStep`* = *"auto"* or *`scaleStep`* =
*"auto"* (or *0* for backwards compatibility in both
cases) is selected, `CreateScaledShapeModel` automatically
determines a suitable angle or scale step length, respectively,
based on the size of the model. The automatically computed angle
and scale step lengths can be queried using
[`GetShapeModelParams`](get_shape_model_params.md).

If a complete pregeneration of the model is not selected, the model
is only created in a reference pose on each pyramid level. In this
case, the model must be transformed to the different angles and
scales at runtime in [`FindScaledShapeModel`](find_scaled_shape_model.md). Because of
this, the recognition of the model might require slightly more time.

Note that pregenerated shape models are tailored to a specific image size.
For runtime reasons using images of different sizes during the search with
the same model in parallel is not supported. In this case, copies of the same
model must be used, otherwise the program may crash!

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

**`angleStart`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Smallest rotation of the pattern.

Default:
-0.39

Suggested values:
-3.14, -1.57, -0.79, -0.39, -0.20, 0.0

**`angleExtent`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Extent of the rotation angles.

Default:
0.79

Suggested values:
6.29, 3.14, 1.57, 0.79, 0.39

Restriction:
`AngleExtent >= 0`

**`angleStep`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double* / string)

Step length of the angles (resolution).

Default:
"auto"

Suggested values:
"auto", 0.0175, 0.0349, 0.0524, 0.0698, 0.0873

Restriction:
`AngleStep >= 0 && AngleStep <= pi / 2`

**`scaleMin`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Minimum scale of the pattern.

Default:
0.9

Suggested values:
0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Restriction:
`ScaleMin > 0`

**`scaleMax`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Maximum scale of the pattern.

Default:
1.1

Suggested values:
1.0, 1.1, 1.2, 1.3, 1.4, 1.5

Restriction:
`ScaleMax >= ScaleMin`

**`scaleStep`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / string)

Scale step length (resolution).

Default:
"auto"

Suggested values:
"auto", 0.01, 0.02, 0.05, 0.1, 0.15, 0.2

Restriction:
`ScaleStep >= 0`

**`optimization`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Kind of optimization and optionally method used
for generating the model.

Default:
"auto"

List of values:
"auto", "no_pregeneration", "none", "point_reduction_high", "point_reduction_low", "point_reduction_medium", "pregeneration"

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

**`modelID`** (output_control)  shape_model `→` [HShapeModel](HShapeModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

## Result

If the parameters are valid, the operator
`CreateScaledShapeModel` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised. If the parameters
*`numLevels`* and *`contrast`* are chosen such that the
model contains too few points, the error 8510 is raised.

## Possible Predecessors

`DrawRegion`,
`ReduceDomain`,
`Threshold`

## Possible Successors

`FindScaledShapeModel`,
`FindScaledShapeModels`,
`GetShapeModelParams`,
`ClearShapeModel`,
`WriteShapeModel`,
`SetShapeModelOrigin`,
`SetShapeModelClutter`

## Alternatives

`CreateGenericShapeModel`

## See also

`SetSystem`,
`GetSystem`

## Module

Matching
