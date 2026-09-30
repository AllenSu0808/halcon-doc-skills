# create_planar_uncalib_deformable_model_xld (Operator)

## Name

`create_planar_uncalib_deformable_model_xld` — Prepare a deformable model for planar uncalibrated matching
from XLD contours.

## Signature

`create_planar_uncalib_deformable_model_xld(Contours : : NumLevels, AngleStart, AngleExtent, AngleStep, ScaleRMin, ScaleRMax, ScaleRStep, ScaleCMin, ScaleCMax, ScaleCStep, Optimization, Metric, MinContrast, GenParamName, GenParamValue : ModelID)`

## Description

The operator `create_planar_uncalib_deformable_model_xld` creates a
deformable model used for planar uncalibrated matching from the XLD contours
passed in *`Contours`*. The XLD contours represent the gray-value edges
of the object to be searched for. In contrast to the operator
[`create_planar_uncalib_deformable_model`](create_planar_uncalib_deformable_model.md), which creates a deformable
model from a template image, the operator
`create_planar_uncalib_deformable_model_xld` creates
the deformable model from XLD contours.

The model is generated for multiple image pyramid levels and is
stored in memory. The center of gravity of the smallest surrounding rectangle
of the *`Contours`* that is parallel to the coordinate axes is used as
the origin (reference point) of the model. A different origin can be set
with [`set_deformable_model_origin`](set_deformable_model_origin.md). The output parameter
*`ModelID`* is a handle for this model, which is used in subsequent
calls to [`find_planar_uncalib_deformable_model`](find_planar_uncalib_deformable_model.md).

### Some Input parameters in detail

- ***`NumLevels`*:** —

  The number of pyramid levels is determined with the parameter
  *`NumLevels`*. It should be chosen as large as possible
  because by this the time necessary to find the object is
  significantly reduced. On the other hand, *`NumLevels`* must
  be chosen such that the model is still recognizable and contains a
  sufficient number of points (at least four) on the highest pyramid
  level. If not enough model points are generated, the number of pyramid
  levels is reduced internally until enough model points are found on the
  highest pyramid level. If this procedure leads to a model with no pyramid
  levels, i.e., if the number of model points is already too small on the
  lowest pyramid level, `create_planar_uncalib_deformable_model_xld`
  returns with an error message. If *`NumLevels`* is set to
  *'auto'*, `create_planar_uncalib_deformable_model_xld`
  determines the number of pyramid levels automatically. The computed number
  of pyramid levels can be queried using [`get_deformable_model_params`](get_deformable_model_params.md).
  In rare cases, it might happen that
  `create_planar_uncalib_deformable_model_xld` determines a value for the
  number of pyramid levels that is too large or too small. If the number of
  pyramid levels is chosen too large, the model may not be recognized in the
  search image or it may be necessary to select very low parameters for
  `MinScore` or `Greediness` in
  [`find_planar_uncalib_deformable_model`](find_planar_uncalib_deformable_model.md) to find the object.
  If the number of pyramid levels is chosen too small, the time required to find
  the object with [`find_planar_uncalib_deformable_model`](find_planar_uncalib_deformable_model.md) may increase.
  In both cases, the number of pyramid levels should be selected manually.
- ****Angle and Scale parameters:**** —

  Note that the parameters *`AngleStart`*, *`AngleExtent`*,
  *`ScaleRMax`*, and *`ScaleCMax`* are not used by this operator.
  Instead, they have to be specified within the operator
  [`find_planar_uncalib_deformable_model`](find_planar_uncalib_deformable_model.md). *`ScaleRMin`* and
  *`ScaleCMin`* can be relevant if you expect matches that are
  smaller than the given XLD *`Contours`*. Then, if
  *`NumLevels`* is set to *'auto'*, the number of used pyramid
  levels may decrease.

  Generally, the parameters *`AngleStep`*, *`ScaleRStep`* and
  *`ScaleCStep`* can be determined automatically. The automatically
  computed angle and scale step lengths can be queried using
  [`get_deformable_model_params`](get_deformable_model_params.md). For more information
  about how these parameters work, please refer to the operator
  [`find_planar_uncalib_deformable_model`](find_planar_uncalib_deformable_model.md).
- ***`Optimization`*:** —

  For particularly large models, it may be useful to reduce the number
  of model points by setting *`Optimization`* to a value
  different from *'none'*. If *`Optimization`* =
  *'none'* is set, all model points are stored. In all other cases,
  the number of points is reduced according to the value of
  *`Optimization`*.
  If the number of points is reduced, it may be necessary in
  [`find_planar_uncalib_deformable_model`](find_planar_uncalib_deformable_model.md) to set the parameter
  `Score` and `Greediness` to a smaller value as, e.g.,
  *0.7* or *0.8*.
  For small models, the reduction of the number of model points does not result
  in a speed-up of the search, because in this case usually
  significantly more potential instances of the model must be
  examined. If *`Optimization`* is set to *'auto'*,
  `create_planar_uncalib_deformable_model_xld` automatically determines
  the reduction of the number of model points.
- ***`MinContrast`*:** —

  With *`MinContrast`*, it can be determined which contrast the
  object contours must at least have in the recognition performed by
  [`find_planar_uncalib_deformable_model`](find_planar_uncalib_deformable_model.md). In other words, this parameter
  separates the object from the noise in the image. Therefore, a good
  choice is the range of gray-value changes caused by the noise in the
  image. If, e.g., the gray values fluctuate within a range of
  10 gray levels, *`MinContrast`* should be set to 10. If
  multi-channel images are used for the model and the search images,
  and if the parameter *`Metric`* is set to
  *'ignore_color_polarity'* (see below) the noise in one
  channel must be multiplied by the square root of the number of
  channels to determine *`MinContrast`*. If, e.g., the
  gray values fluctuate within a range of 10 gray levels in a single
  channel and the image is a three-channel image, *`MinContrast`*
  should be set to 17. If the model should be recognized
  in very low contrast images, *`MinContrast`* must be set to a
  correspondingly small value. If the model should be recognized even
  if it is severely occluded, *`MinContrast`* should be slightly
  larger than the range of gray value fluctuations created by noise to ensure
  that the position and rotation of the model are extracted robustly and
  accurately by [`find_planar_uncalib_deformable_model`](find_planar_uncalib_deformable_model.md).
- ***`Metric`*:** —

  The parameter *`Metric`* determines the conditions under which
  the model is recognized in the image. If *`Metric`* =
  *'use_polarity'*, the object in the image and the model must
  have the same contrast. If, e.g., the model is a bright object on a dark
  background, the object is found only if it is also brighter than the
  background. If *`Metric`* = *'ignore_global_polarity'*, the
  object is found in the image also if the contrast reverses globally. In the
  above example, the object hence is also found if it is darker than the
  background. The runtime of [`find_planar_uncalib_deformable_model`](find_planar_uncalib_deformable_model.md) will
  increase slightly in this case. If
  *`Metric`* = *'ignore_part_polarity'*
  or *`Metric`* = *'ignore_local_polarity'*,
  the model is found even if the contrast changes locally. These modes
  can, e.g., be useful if the object consists of a part with a medium gray
  value, within which either darker or brighter sub-objects lie. The above
  mentioned four metrics can only be applied to single-channel images. If a
  multi-channel image is used as the search image, only the first channel will
  be used (and no error message will be returned).
  If *`Metric`* = *'ignore_color_polarity'*, the model is found
  even if the color contrast changes locally. This is, e.g., the case
  if parts of the object can change their color, e.g., from red to green.
  In particular, this mode is useful if it is not known in advance in which
  channels the object is visible. In this mode, the runtime of
  [`find_planar_calib_deformable_model`](find_planar_calib_deformable_model.md) can also increase significantly.
  The metric *'ignore_color_polarity'*
  can be used for images with an arbitrary number of channels. If it
  is used for single-channel images, it has the same effect as
  *'ignore_local_polarity'*. It should be noted that for
  *`Metric`* = *'ignore_color_polarity'* the
  channels do not need to contain a spectral
  subdivision of the light (like in an RGB image). The channels can,
  e.g., also contain images of the same object that were
  obtained by illuminating the object from different directions.
  Note that the first two metrics (*'use_polarity'* and
  *'ignore_global_polarity'*) can only be selected if all
  *`Contours`* provide the attribute *'edge_direction'*, which
  defines the polarity of the contained contours. For more information about
  contour attributes like *'edge_direction'* see
  [`get_contour_attrib_xld`](get_contour_attrib_xld.md). Otherwise, these two
  metrics can be selected with the operator
  [`set_planar_uncalib_deformable_model_metric`](set_planar_uncalib_deformable_model_metric.md), which determines the
  polarity of the model contours from a representative image.

## Attention

Note that, in contrast to the operator
[`create_planar_uncalib_deformable_model`](create_planar_uncalib_deformable_model.md), it is not possible to specify a
minimum size of the model components. To avoid small model
components in the model, short contours can be eliminated
before calling `create_planar_uncalib_deformable_model_xld` with the
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

Suggested values:
'auto', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

**`AngleStart`** (input_control)  angle.rad-array `→`  (real)

This parameter is not used.

Default:
[]

**`AngleExtent`** (input_control)  angle.rad-array `→`  (real)

This parameter is not used.

Default:
[]

**`AngleStep`** (input_control)  angle.rad `→`  (real / string)

Step length of the angles (resolution).

Default:
'auto'

Suggested values:
'auto', 0.0175, 0.0349, 0.0524, 0.0698, 0.0873

Restriction:
`AngleStep > 0 && AngleStep <= pi / 16`

**`ScaleRMin`** (input_control)  number `→`  (real)

Minimum scale of the pattern in row direction.

Default:
1.0

Suggested values:
0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Restriction:
`ScaleRMin > 0`

**`ScaleRMax`** (input_control)  number-array `→`  (real)

This parameter is not used.

Default:
[]

**`ScaleRStep`** (input_control)  number `→`  (real / string)

Scale step length (resolution) in row direction.

Default:
'auto'

Suggested values:
'auto', 0.01, 0.02, 0.05, 0.1, 0.15, 0.2

Restriction:
`ScaleRStep > 0`

**`ScaleCMin`** (input_control)  number `→`  (real)

Minimum scale of the pattern in column direction.

Default:
1.0

Suggested values:
0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Restriction:
`ScaleCMin > 0`

**`ScaleCMax`** (input_control)  number-array `→`  (real)

This parameter is not used.

Default:
[]

**`ScaleCStep`** (input_control)  number `→`  (real / string)

Scale step length (resolution) in the column direction.

Default:
'auto'

Suggested values:
'auto', 0.01, 0.02, 0.05, 0.1, 0.15, 0.2

Restriction:
`ScaleCStep > 0`

**`Optimization`** (input_control)  string(-array) `→`  (string)

Kind of optimization used for generating the model.

Default:
'auto'

List of values:
'auto', 'none', 'point_reduction_high', 'point_reduction_low', 'point_reduction_medium'

**`Metric`** (input_control)  string `→`  (string)

Match metric.

Default:
'ignore_local_polarity'

List of values:
'ignore_color_polarity', 'ignore_global_polarity', 'ignore_local_polarity', 'ignore_part_polarity', 'use_polarity'

**`MinContrast`** (input_control)  number `→`  (integer)

Minimum contrast of the objects in the search images.

Default:
5

Suggested values:
1, 2, 3, 5, 7, 10, 20, 30, 40

**`GenParamName`** (input_control)  string-array `→`  (string)

The generic parameter names.

Default:
[]

List of values:
[], 'part_size'

**`GenParamValue`** (input_control)  integer-array `→`  (integer / real / string)

Values of the generic parameters.

Default:
[]

List of values:
[], 'big', 'medium', 'small'

**`ModelID`** (output_control)  deformable_model `→`  (handle)

Handle of the model.

## Result

If the parameters are valid, the operator
`create_planar_uncalib_deformable_model_xld` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised. If the parameter *`NumLevels`* is
chosen such that the model contains too few points, the error 8510 is raised.

## Possible Predecessors

`read_contour_xld_dxf`,
`edges_sub_pix`,
`select_contours_xld`

## Possible Successors

`find_planar_uncalib_deformable_model`

## See also

`create_planar_uncalib_deformable_model`

## Module

Matching
