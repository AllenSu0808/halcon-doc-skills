# create_scaled_shape_model_xld (Operator)

## Name

`create_scaled_shape_model_xld` — Prepare an isotropically scaled shape model for matching from XLD contours.

## Signature

`create_scaled_shape_model_xld(Contours : : NumLevels, AngleStart, AngleExtent, AngleStep, ScaleMin, ScaleMax, ScaleStep, Optimization, Metric, MinContrast : ModelID)`

## Description

The operator `create_scaled_shape_model_xld` creates an isotropically
scaled shape model used for matching from the XLD contours passed in
*`Contours`*. The XLD contours represent the gray value edges of the
object to be searched for. In contrast to the operator
[`create_scaled_shape_model`](create_scaled_shape_model.md), which creates a shape model from a
template image, the operator `create_scaled_shape_model_xld` creates
the shape model from XLD contours, i.e., without the use of a template
image.

The output parameter *`ModelID`* is
a handle for this model, which is used in subsequent calls to
[`find_scaled_shape_model`](find_scaled_shape_model.md). The center of gravity of the smallest
surrounding rectangle of the *`Contours`* that is parallel to the
coordinate axes is used as the origin (reference point) of the model.
A different origin can be set with [`set_shape_model_origin`](set_shape_model_origin.md). The model
is generated for multiple image pyramid levels and is stored in memory. If
a complete pregeneration of the model is selected (see below), the model
is generated at multiple rotations and scales on each level. The model can
be extended by clutter parameters with [`set_shape_model_clutter`](set_shape_model_clutter.md).

### Input parameters in detail

- ***`NumLevels`*:** —

  The number of pyramid levels is determined with the parameter
  *`NumLevels`*. It should be chosen as large as possible because by this
  the time necessary to find the object is significantly reduced. On the other
  hand, *`NumLevels`* must be chosen such that the model is still
  recognizable and contains a sufficient number of points (at least four) on
  the highest pyramid level. If not enough model points are generated, the
  number of pyramid levels is reduced internally until enough model points are
  found on the highest pyramid level. If this procedure would lead to a model
  with no pyramid levels, i.e., if the number of model points is already too
  small on the lowest pyramid level, `create_scaled_shape_model_xld`
  returns with an error message.

  If *`NumLevels`* is set to *'auto'*,
  `create_scaled_shape_model_xld` determines the number of pyramid
  levels automatically. The computed number of pyramid levels can
  be queried using [`get_shape_model_params`](get_shape_model_params.md). In rare cases, it might
  happen that `create_scaled_shape_model_xld` determines a value for the
  number of pyramid levels that is too large or too small. If the number of
  pyramid levels is chosen too large, the model may not be recognized in the
  image or it may be necessary to select very low parameters for
  `MinScore` or `Greediness` in
  [`find_scaled_shape_model`](find_scaled_shape_model.md) in order to find the model. If the number
  of pyramid levels is chosen too small, the time required to find
  the model in [`find_scaled_shape_model`](find_scaled_shape_model.md) may increase. In these cases,
  the number of pyramid levels should be selected manually.
- ***`AngleStart`*, *`AngleExtent`*, and *`AngleStep`*:** —

  The parameters *`AngleStart`* and *`AngleExtent`* determine the
  range of possible rotations, in which the object can occur in the image
  during the search. Note that the object can only be found in this range of
  angles by [`find_scaled_shape_model`](find_scaled_shape_model.md). The parameter *`AngleStep`*
  determines the step length within the selected range of angles. Hence, if
  subpixel accuracy is not specified in [`find_scaled_shape_model`](find_scaled_shape_model.md), this
  parameter specifies the accuracy that is achievable for the angles in
  [`find_scaled_shape_model`](find_scaled_shape_model.md). *`AngleStep`* should be chosen based
  on the size of the object. Smaller models do not have many different
  discrete rotations in the image, and hence *`AngleStep`* should be
  chosen larger for smaller models. If *`AngleExtent`* is not an integer
  multiple of *`AngleStep`*, *`AngleStep`* is modified accordingly.
  To ensure that for model instances without rotation angle values of
  exactly 0.0 are returned by [`find_scaled_shape_model`](find_scaled_shape_model.md),
  the range of possible
  rotations is modified as follows: If there is no positive integer
  value n such that *`AngleStart`* plus n times
  *`AngleStep`* is exactly 0.0, *`AngleStart`* is decreased
  by up to *`AngleStep`* and *`AngleExtent`* is increased by
  *`AngleStep`*.
- ***`ScaleMin`*, *`ScaleMax`*, and *`ScaleStep`*:** —

  The parameters *`ScaleMin`* and *`ScaleMax`* determine the
  range of possible scales (sizes) of the object. A scale of 1
  corresponds to the original size of the model. The parameter
  *`ScaleStep`* determines the step length within the selected
  range of scales. Hence, if subpixel accuracy is not specified in
  [`find_scaled_shape_model`](find_scaled_shape_model.md), this parameter specifies the
  accuracy that is achievable for the scales in
  [`find_scaled_shape_model`](find_scaled_shape_model.md). Like *`AngleStep`*,
  *`ScaleStep`* should be chosen based on the size of the object.
  If the range of scales is not an integer multiple of
  *`ScaleStep`*, *`ScaleStep`* is modified accordingly.
  To ensure that for model instances that are not scaled scale values of
  exactly 1.0 are returned by [`find_scaled_shape_model`](find_scaled_shape_model.md),
  the range of possible
  scales is modified as follows: If there is no positive integer value
  n such that *`ScaleMin`* plus n times *`ScaleStep`* is
  exactly 1.0, *`ScaleMin`* is decreased by up to
  *`ScaleStep`* and *`ScaleMax`* is increased such that the
  range of possible scales is increased by *`ScaleStep`*.
- ***`Optimization`*:** —

  For particularly large models, it may be useful to reduce the number
  of model points by setting *`Optimization`* to a value
  different from *'none'*. If *`Optimization`* =
  *'none'*, all model points are stored. In all other cases,
  the number of points is reduced according to the value of
  *`Optimization`*. If the number of points is reduced, it may
  be necessary in [`find_scaled_shape_model`](find_scaled_shape_model.md) to set the parameter
  `Greediness` to a smaller value, e.g., *0.7* or *0.8*.
  For small models, the reduction of the number of model points does not result
  in a speed-up of the search because in this case usually
  significantly more potential instances of the model must be
  examined.

  If *`Optimization`* is set to *'auto'*,
  `create_scaled_shape_model_xld` automatically determines the
  reduction of the number of model points.
- ***`Metric`*:** —

  The parameter *`Metric`* determines the conditions under which
  the model is recognized in the image.

  If *`Metric`* = *'use_polarity'*, the object in the image and
  the model must have the same contrast. If, for example, the model is a
  bright object on a dark background, the object is found only if it is also
  brighter than the background.

  If *`Metric`* = *'ignore_global_polarity'*, the object is
  found in the image also if the contrast reverses globally. In the above
  example, the object hence is also found if it is darker than the background.
  The runtime of [`find_scaled_shape_model`](find_scaled_shape_model.md) will increase slightly in
  this case.

  Note that the metrics (*'use_polarity'* and
  *'ignore_global_polarity'*) can only be selected if all
  *`Contours`* provide the attribute *'edge_direction'*, which
  defines the polarity of the edges. This attribute is available for contours
  created, e.g., with [`edges_sub_pix`](edges_sub_pix.md) with the parameter `Method`
  set to, e.g., *'canny'*. Otherwise, these two metrics can be
  selected with the operator [`set_shape_model_metric`](set_shape_model_metric.md), which determines
  the polarity of the edges from an image.

  If *`Metric`* = *'ignore_local_polarity'*,
  the model is found even if the contrast changes locally. This mode
  can, for example, be useful if the object consists of a part with
  medium gray value, within which either darker or brighter
  sub-objects lie. Since in this case the runtime of
  [`find_scaled_shape_model`](find_scaled_shape_model.md) increases significantly, it is
  usually better to create several models that reflect the possible
  contrast variations of the object with
  `create_scaled_shape_model_xld`, and to match them simultaneously
  with [`find_scaled_shape_models`](find_scaled_shape_models.md).

  The above three metrics can only be applied to single-channel images.
  If a multichannel image is used as the model image or as the search image,
  only the first channel will be used (and no error message will be returned).

  If *`Metric`* = *'ignore_color_polarity'*, the model is
  found even if the color contrast changes locally. This is, for
  example, the case if parts of the object can change their color,
  e.g., from red to green. In particular, this mode is useful if it
  is not known in advance in which channels the object is visible. In
  this mode, the runtime of [`find_scaled_shape_model`](find_scaled_shape_model.md) can also
  increase significantly. The metric *'ignore_color_polarity'*
  can be used for images with an arbitrary number of channels. If it
  is used for single-channel images it has the same effect as
  *'ignore_local_polarity'*. It should be noted that for
  *`Metric`* = *'ignore_color_polarity'* the
  channels do not need to contain a spectral subdivision of the light
  (like in an RGB image). The channels can, for example, also contain
  images of the same object that were obtained by illuminating the
  object from different directions.

  Note that the first two metrics (*'use_polarity'* and
  *'ignore_global_polarity'*) can only be selected if all
  *`Contours`* provide the attribute *'edge_direction'*, which
  defines the polarity of the edges. For more information about
  contour attributes like *'edge_direction'* see
  [`get_contour_attrib_xld`](get_contour_attrib_xld.md).
  Otherwise, these two metrics can be selected with the operator
  [`set_shape_model_metric`](set_shape_model_metric.md), which determines
  the polarity of the edges from an image.
- ***`MinContrast`*:** —

  With *`MinContrast`*, it can be determined which contrast the
  object edges must at least have in the recognition performed by
  [`find_scaled_shape_model`](find_scaled_shape_model.md). In other words, this parameter
  separates the object from the noise in the image. Therefore, a good
  choice is the range of gray value changes caused by the noise in the
  image. If, for example, the gray values fluctuate within a range of
  10 gray levels, *`MinContrast`* should be set to 10. If
  multichannel images are used for the model and the search images,
  and if the parameter *`Metric`* is set to
  *'ignore_color_polarity'* (see above) the noise in one
  channel must be multiplied by the square root of the number of
  channels to determine *`MinContrast`*. If, for example, the
  gray values fluctuate within a range of 10 gray levels in a single
  channel and the image is a three-channel image *`MinContrast`*
  should be set to 17. If the model should be recognized
  in very low contrast images, *`MinContrast`* must be set to a
  correspondingly small value. If the model should be recognized even
  if it is severely occluded, *`MinContrast`* should be slightly
  larger than the range of gray value fluctuations created by noise in
  order to ensure that the position and rotation of the model are
  extracted robustly and accurately by
  [`find_scaled_shape_model`](find_scaled_shape_model.md).

### Complete pregeneration of the model

Optionally, a second value can be passed in *`Optimization`*.
This value determines whether the model is pregenerated completely
or not. To do so, the second value of *`Optimization`* must be
set to either *'pregeneration'* or
*'no_pregeneration'*. If the second value is not used (i.e.,
if only one value is passed), the mode that is set with
`set_system('pregenerate_shape_models',...)` is used. With
the default value (*'pregenerate_shape_models'* =
*'false'*), the model is not pregenerated completely. The
complete pregeneration of the model normally leads to slightly lower
runtimes because the model does not need to be transformed at
runtime. However, in this case, the memory requirements and the
time required to create the model are significantly higher. It
should also be noted that it cannot be expected that the two modes
return exactly identical results because transforming the model at
runtime necessarily leads to different internal data for the
transformed models than pregenerating the transformed models. For
example, if the model is not pregenerated completely,
[`find_scaled_shape_model`](find_scaled_shape_model.md) typically returns slightly lower
scores, which may require setting a slightly lower value for
`MinScore` than for a completely pregenerated model.
Furthermore, the poses obtained by interpolation may differ slightly
in the two modes.
If maximum accuracy is desired, the pose of the model should
be determined by least-squares adjustment.

If a complete pregeneration of the model is selected,
the model is pregenerated for the selected angle and scale range
and stored in memory. The memory required to store the model is
proportional to the number of angle steps, the number of scale
steps, and the number of points in the model. Hence, if
*`AngleStep`* or *`ScaleStep`* are too small or
*`AngleExtent`* or the range of scales are too big, it may
happen that the model no longer fits into the (virtual) memory. In
this case, either *`AngleStep`* or *`ScaleStep`* must be
enlarged or *`AngleExtent`* or the range of scales must be
reduced. In any case, it is desirable that the model completely
fits into the main memory, because this avoids paging by the
operating system, and hence the time to find the object will be much
smaller. Since angles can be determined with subpixel resolution by
[`find_scaled_shape_model`](find_scaled_shape_model.md), *`AngleStep`* >= 1° and *`ScaleStep`* >= 0.02 can be selected for models of a
diameter smaller than about 200 pixels.

If *`AngleStep`* = *'auto'* or *`ScaleStep`* = *'auto'*
is selected, `create_scaled_shape_model_xld`
automatically determines a suitable angle or scale step length,
respectively, based on the size of the model. The automatically computed
angle and scale step lengths can be queried using
[`get_shape_model_params`](get_shape_model_params.md).

If a complete pregeneration of the model is not selected, the model
is only created in a reference pose on each pyramid level. In this
case, the model must be transformed to the different angles and
scales at runtime in [`find_scaled_shape_model`](find_scaled_shape_model.md). Because of
this, the recognition of the model might require slightly more time.

Note that pregenerated shape models are tailored to a specific image size.
For runtime reasons using images of different sizes during the search with
the same model in parallel is not supported. In this case, copies of the same
model must be used, otherwise the program may crash!

## Attention

The XLD contours passed in *`Contours`* should have been scaled
to approximately the average size of the object in the search images.
This means that the product $\texttt{ScaleMin}\times\texttt{ScaleMax}$ should be
approximately equal to 1.

Note that, in contrast to the operator
[`create_scaled_shape_model`](create_scaled_shape_model.md), it is not possible to specify a
minimum size of the model components. To avoid small model
components in the shape model, short contours can be eliminated
before calling `create_scaled_shape_model_xld` with the
operator [`select_contours_xld`](select_contours_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`Contours`** (input_object)  xld_cont(-array) `→` object

Input contours that will be used to create the model.

**`NumLevels`** (input_control)  integer `→`  (integer / string)

Maximum number of pyramid levels.

Default:
'auto'

List of values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'auto'

**`AngleStart`** (input_control)  angle.rad `→`  (real)

Smallest rotation of the pattern.

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

**`AngleStep`** (input_control)  angle.rad `→`  (real / string)

Step length of the angles (resolution).

Default:
'auto'

Suggested values:
'auto', 0.0175, 0.0349, 0.0524, 0.0698, 0.0873

Restriction:
`AngleStep >= 0 && AngleStep <= pi / 2`

**`ScaleMin`** (input_control)  number `→`  (real)

Minimum scale of the pattern.

Default:
0.9

Suggested values:
0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Restriction:
`ScaleMin > 0`

**`ScaleMax`** (input_control)  number `→`  (real)

Maximum scale of the pattern.

Default:
1.1

Suggested values:
1.0, 1.1, 1.2, 1.3, 1.4, 1.5

Restriction:
`ScaleMax >= ScaleMin`

**`ScaleStep`** (input_control)  number `→`  (real / string)

Scale step length (resolution).

Default:
'auto'

Suggested values:
'auto', 0.01, 0.02, 0.05, 0.1, 0.15, 0.2

Restriction:
`ScaleStep >= 0`

**`Optimization`** (input_control)  string(-array) `→`  (string)

Kind of optimization and optionally method used
for generating the model.

Default:
'auto'

List of values:
'auto', 'no_pregeneration', 'none', 'point_reduction_high', 'point_reduction_low', 'point_reduction_medium', 'pregeneration'

**`Metric`** (input_control)  string `→`  (string)

Match metric.

Default:
'ignore_local_polarity'

List of values:
'ignore_color_polarity', 'ignore_global_polarity', 'ignore_local_polarity', 'use_polarity'

**`MinContrast`** (input_control)  number `→`  (integer)

Minimum contrast of the objects in the search images.

Default:
5

Suggested values:
1, 2, 3, 5, 7, 10, 20, 30, 40

**`ModelID`** (output_control)  shape_model `→`  (handle)

Handle of the model.

## Result

If the parameters are valid, the operator
`create_scaled_shape_model_xld` returns the value 2 (
H_MSG_TRUE)
. If necessary
an exception is raised. If the parameter *`NumLevels`* is chosen such
that the model contains too few points, the error 8510 is raised.

## Possible Predecessors

`read_contour_xld_dxf`,
`edges_sub_pix`,
`select_contours_xld`

## Possible Successors

`find_scaled_shape_model`,
`find_scaled_shape_models`,
`get_shape_model_params`,
`clear_shape_model`,
`write_shape_model`,
`set_shape_model_origin`,
`set_shape_model_param`,
`set_shape_model_metric`,
`set_shape_model_clutter`

## Alternatives

`create_generic_shape_model`

## See also

`set_system`,
`get_system`

## Module

Matching
