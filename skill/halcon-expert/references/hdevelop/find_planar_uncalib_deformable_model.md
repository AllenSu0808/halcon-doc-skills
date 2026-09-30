# find_planar_uncalib_deformable_model (Operator)

## Name

`find_planar_uncalib_deformable_model` — Find the best matches of a planar projective invariant deformable model
in an image.

## Signature

`find_planar_uncalib_deformable_model(Image : : ModelID, AngleStart, AngleExtent, ScaleRMin, ScaleRMax, ScaleCMin, ScaleCMax, MinScore, NumMatches, MaxOverlap, NumLevels, Greediness, GenParamName, GenParamValue : HomMat2D, Score)`

## Description

The operator `find_planar_uncalib_deformable_model` finds the best
*`NumMatches`* instances of the perspectively distorted deformable
model *`ModelID`* in the input image *`Image`*. The
model must have been created previously by calling
[`create_planar_uncalib_deformable_model`](create_planar_uncalib_deformable_model.md) or
[`read_deformable_model`](read_deformable_model.md).

*`HomMat2D`* determines the projective transformation (homography),
which describes the position of the found matches.
In case several objects are found, the different homographies are
concatenated. Then, a single homography can be extracted using
`tuple_select_range(HomMat2D,Index*9,(Index+1)*9-1, SelectedHomMat2D)`.
The different results are sorted according to their *`Score`* in
descending order.

The row and column coordinates of the origin of the deformable model within
the search image can be determined calling
`projective_trans_pixel(HomMat2D,0,0,Row,Column)`.
Usually the origin of the model is the center of gravity of the image region
used to create the deformable model calling
[`create_planar_uncalib_deformable_model`](create_planar_uncalib_deformable_model.md).
The origin can be modified using [`set_deformable_model_origin`](set_deformable_model_origin.md).

The model contours of found instances can be visualized using
[`projective_trans_contour_xld`](projective_trans_contour_xld.md)
with the *`HomMat2D`* and the original model contour, which has been
extracted previously using [`get_deformable_model_contours`](get_deformable_model_contours.md).

The *`Score`* is a number between 0 and 1 and may indicate how much of
the model is visible within the image.

*Example:* Half of the model is occluded in the search image.
As a result, the *`Score`* of this match can not exceed *0.5*.

### Input parameters in detail

- ***`Image`* and its domain:** —

  The domain of the image *`Image`* determines the search space
  for the reference point of the model, i.e., for the center of
  gravity of the domain (region) of the image that was used to create
  the deformable model with [`create_planar_uncalib_deformable_model`](create_planar_uncalib_deformable_model.md).
  A different origin set with [`set_deformable_model_origin`](set_deformable_model_origin.md) is not taken
  into account. The model is searched within those points of the domain of
  the image, in which the model lies completely within the image.
  This means that the model will not be found if it extends beyond the
  borders of the image, even if it would achieve a score greater than
  *`MinScore`* (see below).
  Note that, if for a certain pyramid level the model touches the image
  border, it might not be found
  even if it lies completely within the original image.
  As a rule of thumb, the model might not be found if its distance to
  an image border falls below $2^{NumLevels-1}$.
  This behavior can be changed with
  [`set_system('border_shape_models','true')`](set_system.md), which will cause
  models that extend beyond the image border to be found if they
  achieve a score greater than *`MinScore`*. Here, points lying
  outside the image are regarded as being occluded, i.e., they lower
  the score. It should be noted that the runtime of the search will
  increase in this mode.
  Note further, that in rare cases,
  which occur typically only for artificial images, the model might not be
  found also if for certain pyramid levels the model touches the border
  of the reduced domain. Then, it may help to enlarge the reduced
  domain by $2^{NumLevels-1}$ using,
  e.g., [`dilation_circle`](dilation_circle.md).
- ****Angle and Scale parameters:**** —

  The parameters *`AngleStart`*, *`AngleExtent`*,
  *`ScaleRMin`*, *`ScaleRMax`*, *`ScaleCMin`* and
  *`ScaleCMax`* are used to specify a basic range of up to an anisotropic
  transformation that is exhaustively searched on the top level of the image
  pyramid. The parameters *`AngleStart`* and *`AngleExtent`*
  determine the range of possible rotations in which the model is exhaustively
  searched. *`ScaleRMin`*, *`ScaleRMax`*,
  *`ScaleCMin`*, and *`ScaleCMax`* determine the range of
  possible anisotropic scales that are exhaustively searched in the image.
  A scale of 1 in both scale factors corresponds to the
  original size of the model.

  The operator `find_planar_uncalib_deformable_model` may find
  objects outside this range, e.g., when the object is perspectively
  distorted. Hence, the range parameters are a kind of suggestion for the
  search algorithm. Starting from this, certain models in a wider range of
  transformations can be detected, depending on the used pyramid levels, but
  also on the model/image content. It is important to note that, e.g., small
  scale changes can be tolerated without the need to specify a scale range,
  leading to faster execution times.

  Often, it is not necessary to use an anisotropic scaling to find the object
  on the top level of the pyramid. In these cases, *`ScaleCMin`* and
  *`ScaleCMax`* should be set to *1.0*.
  The search is then performed with isotropic scaling only, which is much faster.
  If the object should be detected despite severe perspective distortions
  anisotropic scaling is required. Here, *`ScaleRMin`* and
  *`ScaleRMax`* specify the anisotropic scaling in row,
  *`ScaleCMin`* and *`ScaleCMax`* in column direction.

  Note that the transformations are treated internally such that the
  scalings are applied first, followed by the rotation. Therefore,
  the model should usually be aligned such that it appears
  horizontally or vertically in the model image.

  Additionally, the operator `find_planar_uncalib_deformable_model`
  processes the parameters *'angle_step'*, *'scale_r_step'* and
  *'scale_c_step'* which are set by the operator
  [`create_planar_uncalib_deformable_model`](create_planar_uncalib_deformable_model.md) during the model
  creation, or, as described below,
  can be set with the generic parameters *`GenParamName`*
  and *`GenParamValue`*.

  The parameter *'angle_step'* determines the step
  size within the selected range of angles. *'angle_step'* should be
  chosen based on the size of the object. Smaller models do not have many
  different discrete rotations in the image, and hence *'angle_step'*
  should be chosen larger for smaller models. If *`AngleExtent`*
  is not an integer multiple of *'angle_step'*, *'angle_step'* is
  modified accordingly. The parameters *'scale_r_step'* and
  *'scale_c_step'* determine the step size within the selected range
  of scales. Like *'angle_step'*, *'scale_r_step'* and
  *'scale_c_step'* should be chosen based on the size of the object.
  If the respective range of scales is not an integer multiple of
  *'scale_r_step'* and *'scale_c_step'*, *'scale_r_step'*
  and *'scale_c_step'* are modified accordingly.
- ***`MinScore`*:** —

  The parameter *`MinScore`* determines what score a potential
  match must at least have to be regarded as an instance of the model
  in the image. The larger *`MinScore`* is chosen, the faster
  the search is. If the model can be expected never to be occluded in
  the images, *`MinScore`* may be set as high as 0.8 or even 0.9.
- ***`NumMatches`*:** —

  The maximum number of instances to be found can be determined with
  *`NumMatches`*. If more than *`NumMatches`* instances
  with a score greater than *`MinScore`* are found in the image,
  only the best *`NumMatches`* instances are returned. If fewer
  than *`NumMatches`* are found, only that number is returned,
  i.e., the parameter *`MinScore`* takes precedence over
  *`NumMatches`*. If all model instances exceeding
  *`MinScore`* in the image should be found, *`NumMatches`*
  must be set to *0*.
  In rare cases, *`NumMatches`* must be set to a
  higher value than the required number of matches. This is
  the case if, for instance, a small *`MinScore`* is set.

  When tracking the matches through the image pyramid, on each level,
  some less promising matches are rejected based on *`NumMatches`*. Thus,
  it is possible that some matches are rejected that would have had a higher
  score on the lowest pyramid level. Due to this, for example, the found
  match for *`NumMatches`* set to *1* might be
  different from the match with the highest score returned when setting
  *`NumMatches`* to *0* or > *1*.

  If multiple objects with a similar score are expected, but only the one with
  the highest score should be returned, it might be preferable to raise
  *`NumMatches`*, and then select the match with the highest score.
- ***`MaxOverlap`*:** —

  If the model exhibits symmetries it may happen that multiple
  instances with similar positions but different rotations are found
  in the image. The parameter *`MaxOverlap`* determines by what
  fraction (i.e., a number between 0 and 1) two instances may at most
  overlap in order to consider them as different instances, and hence
  to be returned separately. If two instances overlap each other by
  more than *`MaxOverlap`* only the best instance is returned.
  The calculation of the overlap is based on the smallest enclosing
  rectangle of arbitrary orientation (see [`smallest_rectangle2`](smallest_rectangle2.md))
  of the found instances. If *`MaxOverlap`*=*0*, the found
  instances may not overlap at all, while for *`MaxOverlap`*=*1*
  all instances are returned.
- ***`GenParamName`*, *`GenParamValue`*:** —

  With the generic parameters *`GenParamName`* and *`GenParamValue`*
  it is possible to adjust parameters that typically do not have to be set by
  the user. By default the pose is extracted with high subpixel accuracy
  (*'least_squares_very_high'*) through a least-squares
  adjustment, i.e., by minimizing the distances of the model points to
  their corresponding image points. However, if no high accuracy is required
  by an application, the subpixel precise extraction can be reduced or
  switched off as it increases the processing time. Here,
  *'subpixel'* must be passed in *`GenParamName`* and
  *'none'*, *'least_squares'*, *'least_squares_high'* for
  *`GenParamValue`*. A further use of *`GenParamName`* and
  *`GenParamValue`* is to override the discretization steps of the
  parameter space *'angle_step'*, *'scale_r_step'* and
  *'scale_c_step'* that have been defined when the model was created
  in [`create_planar_uncalib_deformable_model`](create_planar_uncalib_deformable_model.md).

  As described in [`create_planar_uncalib_deformable_model`](create_planar_uncalib_deformable_model.md) the
  deformable matching algorithm searches exhaustively a basic set of
  parameters that are specified with *`AngleStart`*,*`AngleExtent`*,
  *`ScaleRMin`*,*`ScaleRMax`*,*`ScaleCMin`* and
  *`ScaleCMax`*. However, to allow a detection even when the object is
  imaged under perspective distortion, an additional transformation is
  estimated. This additional transformation transforms the model from the
  original search range to a bigger perspectively distorted one.
  By allowing perspective distortions, the risk of false positives is also
  increased. One possible use of the parameter *`GenParamName`* is to help
  discarding false positives that occur, if for instance a small score was
  specified in *`MinScore`* and the image contains significant clutter
  with similar shape as the model.

  To restrict arbitrary perspective matches from occurring, the values
  *'angle_change_restriction'* and *'aniso_scale_change_restriction'*
  can be used in *`GenParamName`*.
  With *'angle_change_restriction'* the maximal tolerated angular
  distortion can be restricted. As default value $\frac{\pi}{2}$ ![figure](../assets/03802ec6bdd13756.svg)
  is set, which allows arbitrary distortion. By setting
  *'angle_change_restriction'* to *0*,
  no distortion is allowed at all. The set value should be within the
  interval [0, $\frac{\pi}{2}$ ![figure](../assets/03802ec6bdd13756.svg)].
  This parameter tests, if the angle of 90 degree at the corners of the
  axis-aligned rectangle around the model points is changed by more than the
  corresponding *`GenParamValue`* for the found instance of the model.
  Note that this parameter helps to restrict both affine (a shear mapping) and
  perspective parts of the transformation.
  As an example, with *'angle_change_restriction'* a square-like model
  can be prevented to match with a parallelogram or an arbitrary trapezium.

  With the parameter *'aniso_scale_change_restriction'* the ratio of
  anisotropic scaling can be restricted (the smaller scale factor divided by
  the bigger scale factor).
  The value of this parameter ranges from the default value *0.0*, where
  arbitrary distortion is allowed, to *1.0*, where no distortion is
  allowed.
  One typical use for this parameter is to restrict for instance a square-like
  model to deform to a rectangular model.
- ***`NumLevels`*:** —

  The number of pyramid levels used during the search is determined
  with *`NumLevels`*. If necessary, the number of levels is
  clipped to the range given when the deformable model was created with
  [`create_planar_uncalib_deformable_model`](create_planar_uncalib_deformable_model.md). If *`NumLevels`* is set
  to *0*, the number of pyramid levels specified in
  [`create_planar_uncalib_deformable_model`](create_planar_uncalib_deformable_model.md) is used.
- ***`Greediness`*:** —

  The parameter *`Greediness`* determines how “greedily” the
  search should be carried out. If *`Greediness`*=*0*, a safe
  search heuristic is used, which finds the model if it is
  visible in the image and the other parameters are set appropriately.
  However, the search will be relatively time consuming in this case. If
  *`Greediness`*=*1*, an unsafe search heuristic is used, which
  may cause the model not to be found in rare cases, even though it is
  visible in the image.
  For *`Greediness`*=*1*, the maximum search speed is achieved.
  In almost all cases, the deformable model will be found for
  *`Greediness`*=*0.9*.

### Output parameters in detail

- ***`HomMat2D`*:** —

  The projective transformation (homographies) that encode the position of the
  found instances of the model are returned in *`HomMat2D`*. In case that
  multiple objects are found, the different homographies are concatenated. A
  single homography can easily be extracted by
  `tuple_select_range(HomMat2D,Index*9,(Index+1)*9-1, SelectedHomMat2D)`.
  The different detection results are sorted in decreasing
  order of *`Score`*.
  The row and column coordinates are
  the coordinates of the origin of the deformable model in the search image,
  which can be found by calling
  `projective_trans_pixel(HomMat2D,0,0,Row,Column)`. By default, the
  origin is the center of gravity of the domain (region) of the image that was
  used to create the deformable model with
  [`create_planar_uncalib_deformable_model`](create_planar_uncalib_deformable_model.md). A different origin
  can be set with [`set_deformable_model_origin`](set_deformable_model_origin.md).
  For visualization purposes, the model contours that are extracted by
  [`get_deformable_model_contours`](get_deformable_model_contours.md) can be projected to the
  found location given *`HomMat2D`* with
  [`projective_trans_contour_xld`](projective_trans_contour_xld.md).
- ***`Score`*:** —

  Additionally, the score of each found instance is returned in *`Score`*.
  The score is a number between 0 and 1, which is an approximate measure of how
  much of the model is visible in the image. If, for example, half of the
  model is occluded, the score cannot exceed 0.5.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`Image`** (input_object)  (multichannel-)image `→` object (byte / uint2)

Input image in which the model should be found.

**`ModelID`** (input_control)  deformable_model `→`  (handle)

Handle of the model.

**`AngleStart`** (input_control)  angle.rad `→`  (real)

Smallest rotation of the model.

Default:
-0.39

Suggested values:
-3.14, -1.57, -0.79, -0.39, -0.20, 0.0

**`AngleExtent`** (input_control)  angle.rad `→`  (real)

Extent of the rotation angles.

Default:
0.78

Suggested values:
6.29, 3.14, 1.57, 0.79, 0.39, 0.0

Restriction:
`AngleExtent >= 0`

**`ScaleRMin`** (input_control)  number `→`  (real)

Minimum scale of the model in row direction.

Default:
1.0

Suggested values:
0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Restriction:
`ScaleRMin > 0`

**`ScaleRMax`** (input_control)  number `→`  (real)

Maximum scale of the model in row direction.

Default:
1.0

Suggested values:
1.0, 1.1, 1.2, 1.3, 1.4, 1.5

Restriction:
`ScaleRMax >= ScaleRMin`

**`ScaleCMin`** (input_control)  number `→`  (real)

Minimum scale of the model in column direction.

Default:
1.0

Suggested values:
0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Restriction:
`ScaleCMin > 0`

**`ScaleCMax`** (input_control)  number `→`  (real)

Maximum scale of the model in column direction.

Default:
1.0

Suggested values:
1.0, 1.1, 1.2, 1.3, 1.4, 1.5

Restriction:
`ScaleCMax >= ScaleCMin`

**`MinScore`** (input_control)  real `→`  (real)

Minimum score of the instances of the model to
be found.

Default:
0.5

Suggested values:
0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Value range:
`0
≤
MinScore
≤
1`

Minimum increment:
0.01

Recommended increment:
0.05

**`NumMatches`** (input_control)  integer `→`  (integer)

Number of instances of the model to be found
(or 0 for all matches).

Default:
1

Suggested values:
0, 1, 2, 3, 4, 5, 10, 20

**`MaxOverlap`** (input_control)  real `→`  (real)

Maximum overlap of the instances of the model
to be found.

Default:
1.0

Suggested values:
0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Value range:
`0
≤
MaxOverlap
≤
1`

Minimum increment:
0.01

Recommended increment:
0.05

**`NumLevels`** (input_control)  integer(-array) `→`  (integer)

Number of pyramid levels used in the matching
(and lowest pyramid level to use if
|*`NumLevels`*| = 2).

Default:
0

List of values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

**`Greediness`** (input_control)  real `→`  (real)

“Greediness” of the search heuristic (0: safe
but slow; 1: fast but matches may be missed).

Default:
0.9

Suggested values:
0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Value range:
`0
≤
Greediness
≤
1`

Minimum increment:
0.01

Recommended increment:
0.05

**`GenParamName`** (input_control)  string-array `→`  (string)

The general parameter names.

Default:
[]

List of values:
[], 'angle_change_restriction', 'angle_step', 'aniso_scale_change_restriction', 'scale_c_step', 'scale_r_step', 'subpixel'

**`GenParamValue`** (input_control)  integer-array `→`  (integer / real / string)

Values of the general parameters.

Default:
[]

List of values:
[], 'least_squares', 'least_squares_high', 'least_squares_very_high', 'none'

**`HomMat2D`** (output_control)  hom_mat2d(-array) `→`  (real)

Homographies between model and found instances.

**`Score`** (output_control)  real-array `→`  (real)

Score of the found instances of the model.

## Result

If the parameters are valid, the operator
`find_planar_uncalib_deformable_model` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`create_planar_uncalib_deformable_model`,
`read_deformable_model`

## Alternatives

`find_planar_calib_deformable_model`

## Module

Matching
