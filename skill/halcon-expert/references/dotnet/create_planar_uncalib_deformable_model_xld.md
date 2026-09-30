# CreatePlanarUncalibDeformableModelXld (Operator)

## Name

`CreatePlanarUncalibDeformableModelXld` — Prepare a deformable model for planar uncalibrated matching
from XLD contours.

## Signature

`static void HOperatorSet.CreatePlanarUncalibDeformableModelXld(HObject contours, HTuple numLevels, HTuple angleStart, HTuple angleExtent, HTuple angleStep, HTuple scaleRMin, HTuple scaleRMax, HTuple scaleRStep, HTuple scaleCMin, HTuple scaleCMax, HTuple scaleCStep, HTuple optimization, HTuple metric, HTuple minContrast, HTuple genParamName, HTuple genParamValue, out HTuple modelID)`

`public HDeformableModel(HXLDCont contours, HTuple numLevels, HTuple angleStart, HTuple angleExtent, HTuple angleStep, double scaleRMin, HTuple scaleRMax, HTuple scaleRStep, double scaleCMin, HTuple scaleCMax, HTuple scaleCStep, HTuple optimization, string metric, int minContrast, HTuple genParamName, HTuple genParamValue)`

`public HDeformableModel(HXLDCont contours, int numLevels, HTuple angleStart, HTuple angleExtent, double angleStep, double scaleRMin, HTuple scaleRMax, double scaleRStep, double scaleCMin, HTuple scaleCMax, double scaleCStep, string optimization, string metric, int minContrast, HTuple genParamName, HTuple genParamValue)`

`void HDeformableModel.CreatePlanarUncalibDeformableModelXld(HXLDCont contours, HTuple numLevels, HTuple angleStart, HTuple angleExtent, HTuple angleStep, double scaleRMin, HTuple scaleRMax, HTuple scaleRStep, double scaleCMin, HTuple scaleCMax, HTuple scaleCStep, HTuple optimization, string metric, int minContrast, HTuple genParamName, HTuple genParamValue)`

`void HDeformableModel.CreatePlanarUncalibDeformableModelXld(HXLDCont contours, int numLevels, HTuple angleStart, HTuple angleExtent, double angleStep, double scaleRMin, HTuple scaleRMax, double scaleRStep, double scaleCMin, HTuple scaleCMax, double scaleCStep, string optimization, string metric, int minContrast, HTuple genParamName, HTuple genParamValue)`

`HDeformableModel HXLDCont.CreatePlanarUncalibDeformableModelXld(HTuple numLevels, HTuple angleStart, HTuple angleExtent, HTuple angleStep, double scaleRMin, HTuple scaleRMax, HTuple scaleRStep, double scaleCMin, HTuple scaleCMax, HTuple scaleCStep, HTuple optimization, string metric, int minContrast, HTuple genParamName, HTuple genParamValue)`

`HDeformableModel HXLDCont.CreatePlanarUncalibDeformableModelXld(int numLevels, HTuple angleStart, HTuple angleExtent, double angleStep, double scaleRMin, HTuple scaleRMax, double scaleRStep, double scaleCMin, HTuple scaleCMax, double scaleCStep, string optimization, string metric, int minContrast, HTuple genParamName, HTuple genParamValue)`

## Description

The operator `CreatePlanarUncalibDeformableModelXld` creates a
deformable model used for planar uncalibrated matching from the XLD contours
passed in *`contours`*. The XLD contours represent the gray-value edges
of the object to be searched for. In contrast to the operator
[`CreatePlanarUncalibDeformableModel`](create_planar_uncalib_deformable_model.md), which creates a deformable
model from a template image, the operator
`CreatePlanarUncalibDeformableModelXld` creates
the deformable model from XLD contours.

The model is generated for multiple image pyramid levels and is
stored in memory. The center of gravity of the smallest surrounding rectangle
of the *`contours`* that is parallel to the coordinate axes is used as
the origin (reference point) of the model. A different origin can be set
with [`SetDeformableModelOrigin`](set_deformable_model_origin.md). The output parameter
*`modelID`* is a handle for this model, which is used in subsequent
calls to [`FindPlanarUncalibDeformableModel`](find_planar_uncalib_deformable_model.md).

### Some Input parameters in detail

- ***`numLevels`*:** —

  The number of pyramid levels is determined with the parameter
  *`numLevels`*. It should be chosen as large as possible
  because by this the time necessary to find the object is
  significantly reduced. On the other hand, *`numLevels`* must
  be chosen such that the model is still recognizable and contains a
  sufficient number of points (at least four) on the highest pyramid
  level. If not enough model points are generated, the number of pyramid
  levels is reduced internally until enough model points are found on the
  highest pyramid level. If this procedure leads to a model with no pyramid
  levels, i.e., if the number of model points is already too small on the
  lowest pyramid level, `CreatePlanarUncalibDeformableModelXld`
  returns with an error message. If *`numLevels`* is set to
  *"auto"*, `CreatePlanarUncalibDeformableModelXld`
  determines the number of pyramid levels automatically. The computed number
  of pyramid levels can be queried using [`GetDeformableModelParams`](get_deformable_model_params.md).
  In rare cases, it might happen that
  `CreatePlanarUncalibDeformableModelXld` determines a value for the
  number of pyramid levels that is too large or too small. If the number of
  pyramid levels is chosen too large, the model may not be recognized in the
  search image or it may be necessary to select very low parameters for
  `minScore` or `greediness` in
  [`FindPlanarUncalibDeformableModel`](find_planar_uncalib_deformable_model.md) to find the object.
  If the number of pyramid levels is chosen too small, the time required to find
  the object with [`FindPlanarUncalibDeformableModel`](find_planar_uncalib_deformable_model.md) may increase.
  In both cases, the number of pyramid levels should be selected manually.
- ****Angle and Scale parameters:**** —

  Note that the parameters *`angleStart`*, *`angleExtent`*,
  *`scaleRMax`*, and *`scaleCMax`* are not used by this operator.
  Instead, they have to be specified within the operator
  [`FindPlanarUncalibDeformableModel`](find_planar_uncalib_deformable_model.md). *`scaleRMin`* and
  *`scaleCMin`* can be relevant if you expect matches that are
  smaller than the given XLD *`contours`*. Then, if
  *`numLevels`* is set to *"auto"*, the number of used pyramid
  levels may decrease.

  Generally, the parameters *`angleStep`*, *`scaleRStep`* and
  *`scaleCStep`* can be determined automatically. The automatically
  computed angle and scale step lengths can be queried using
  [`GetDeformableModelParams`](get_deformable_model_params.md). For more information
  about how these parameters work, please refer to the operator
  [`FindPlanarUncalibDeformableModel`](find_planar_uncalib_deformable_model.md).
- ***`optimization`*:** —

  For particularly large models, it may be useful to reduce the number
  of model points by setting *`optimization`* to a value
  different from *"none"*. If *`optimization`* =
  *"none"* is set, all model points are stored. In all other cases,
  the number of points is reduced according to the value of
  *`optimization`*.
  If the number of points is reduced, it may be necessary in
  [`FindPlanarUncalibDeformableModel`](find_planar_uncalib_deformable_model.md) to set the parameter
  `score` and `greediness` to a smaller value as, e.g.,
  *0.7* or *0.8*.
  For small models, the reduction of the number of model points does not result
  in a speed-up of the search, because in this case usually
  significantly more potential instances of the model must be
  examined. If *`optimization`* is set to *"auto"*,
  `CreatePlanarUncalibDeformableModelXld` automatically determines
  the reduction of the number of model points.
- ***`minContrast`*:** —

  With *`minContrast`*, it can be determined which contrast the
  object contours must at least have in the recognition performed by
  [`FindPlanarUncalibDeformableModel`](find_planar_uncalib_deformable_model.md). In other words, this parameter
  separates the object from the noise in the image. Therefore, a good
  choice is the range of gray-value changes caused by the noise in the
  image. If, e.g., the gray values fluctuate within a range of
  10 gray levels, *`minContrast`* should be set to 10. If
  multi-channel images are used for the model and the search images,
  and if the parameter *`metric`* is set to
  *"ignore_color_polarity"* (see below) the noise in one
  channel must be multiplied by the square root of the number of
  channels to determine *`minContrast`*. If, e.g., the
  gray values fluctuate within a range of 10 gray levels in a single
  channel and the image is a three-channel image, *`minContrast`*
  should be set to 17. If the model should be recognized
  in very low contrast images, *`minContrast`* must be set to a
  correspondingly small value. If the model should be recognized even
  if it is severely occluded, *`minContrast`* should be slightly
  larger than the range of gray value fluctuations created by noise to ensure
  that the position and rotation of the model are extracted robustly and
  accurately by [`FindPlanarUncalibDeformableModel`](find_planar_uncalib_deformable_model.md).
- ***`metric`*:** —

  The parameter *`metric`* determines the conditions under which
  the model is recognized in the image. If *`metric`* =
  *"use_polarity"*, the object in the image and the model must
  have the same contrast. If, e.g., the model is a bright object on a dark
  background, the object is found only if it is also brighter than the
  background. If *`metric`* = *"ignore_global_polarity"*, the
  object is found in the image also if the contrast reverses globally. In the
  above example, the object hence is also found if it is darker than the
  background. The runtime of [`FindPlanarUncalibDeformableModel`](find_planar_uncalib_deformable_model.md) will
  increase slightly in this case. If
  *`metric`* = *"ignore_part_polarity"*
  or *`metric`* = *"ignore_local_polarity"*,
  the model is found even if the contrast changes locally. These modes
  can, e.g., be useful if the object consists of a part with a medium gray
  value, within which either darker or brighter sub-objects lie. The above
  mentioned four metrics can only be applied to single-channel images. If a
  multi-channel image is used as the search image, only the first channel will
  be used (and no error message will be returned).
  If *`metric`* = *"ignore_color_polarity"*, the model is found
  even if the color contrast changes locally. This is, e.g., the case
  if parts of the object can change their color, e.g., from red to green.
  In particular, this mode is useful if it is not known in advance in which
  channels the object is visible. In this mode, the runtime of
  [`FindPlanarCalibDeformableModel`](find_planar_calib_deformable_model.md) can also increase significantly.
  The metric *"ignore_color_polarity"*
  can be used for images with an arbitrary number of channels. If it
  is used for single-channel images, it has the same effect as
  *"ignore_local_polarity"*. It should be noted that for
  *`metric`* = *"ignore_color_polarity"* the
  channels do not need to contain a spectral
  subdivision of the light (like in an RGB image). The channels can,
  e.g., also contain images of the same object that were
  obtained by illuminating the object from different directions.
  Note that the first two metrics (*"use_polarity"* and
  *"ignore_global_polarity"*) can only be selected if all
  *`contours`* provide the attribute *"edge_direction"*, which
  defines the polarity of the contained contours. For more information about
  contour attributes like *"edge_direction"* see
  [`GetContourAttribXld`](get_contour_attrib_xld.md). Otherwise, these two
  metrics can be selected with the operator
  [`SetPlanarUncalibDeformableModelMetric`](set_planar_uncalib_deformable_model_metric.md), which determines the
  polarity of the model contours from a representative image.

## Attention

Note that, in contrast to the operator
[`CreatePlanarUncalibDeformableModel`](create_planar_uncalib_deformable_model.md), it is not possible to specify a
minimum size of the model components. To avoid small model
components in the model, short contours can be eliminated
before calling `CreatePlanarUncalibDeformableModelXld` with the
operator [`SelectContoursXld`](select_contours_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`contours`** (input_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Input contours that will be used to create the model.

**`numLevels`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long / string)

Maximum number of pyramid levels.

Default:
"auto"

Suggested values:
"auto", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

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
`ScaleRStep > 0`

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

Scale step length (resolution) in the column direction.

Default:
"auto"

Suggested values:
"auto", 0.01, 0.02, 0.05, 0.1, 0.15, 0.2

Restriction:
`ScaleCStep > 0`

**`optimization`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Kind of optimization used for generating the model.

Default:
"auto"

List of values:
"auto", "none", "point_reduction_high", "point_reduction_low", "point_reduction_medium"

**`metric`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Match metric.

Default:
"ignore_local_polarity"

List of values:
"ignore_color_polarity", "ignore_global_polarity", "ignore_local_polarity", "ignore_part_polarity", "use_polarity"

**`minContrast`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Minimum contrast of the objects in the search images.

Default:
5

Suggested values:
1, 2, 3, 5, 7, 10, 20, 30, 40

**`genParamName`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string*)

The generic parameter names.

Default:
[]

List of values:
[], "part_size"

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
`CreatePlanarUncalibDeformableModelXld` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised. If the parameter *`numLevels`* is
chosen such that the model contains too few points, the error 8510 is raised.

## Possible Predecessors

`ReadContourXldDxf`,
`EdgesSubPix`,
`SelectContoursXld`

## Possible Successors

`FindPlanarUncalibDeformableModel`

## See also

`CreatePlanarUncalibDeformableModel`

## Module

Matching
