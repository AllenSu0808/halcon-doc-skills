# FindAnisoShapeModel (Operator)

## Name

`FindAnisoShapeModel` — Find the best matches of an anisotropically scaled shape model
in an image.

## Signature

`static void HOperatorSet.FindAnisoShapeModel(HObject image, HTuple modelID, HTuple angleStart, HTuple angleExtent, HTuple scaleRMin, HTuple scaleRMax, HTuple scaleCMin, HTuple scaleCMax, HTuple minScore, HTuple numMatches, HTuple maxOverlap, HTuple subPixel, HTuple numLevels, HTuple greediness, out HTuple row, out HTuple column, out HTuple angle, out HTuple scaleR, out HTuple scaleC, out HTuple score)`

`void HShapeModel.FindAnisoShapeModel(HImage image, double angleStart, double angleExtent, double scaleRMin, double scaleRMax, double scaleCMin, double scaleCMax, HTuple minScore, int numMatches, double maxOverlap, HTuple subPixel, HTuple numLevels, double greediness, out HTuple row, out HTuple column, out HTuple angle, out HTuple scaleR, out HTuple scaleC, out HTuple score)`

`void HShapeModel.FindAnisoShapeModel(HImage image, double angleStart, double angleExtent, double scaleRMin, double scaleRMax, double scaleCMin, double scaleCMax, double minScore, int numMatches, double maxOverlap, string subPixel, int numLevels, double greediness, out HTuple row, out HTuple column, out HTuple angle, out HTuple scaleR, out HTuple scaleC, out HTuple score)`

`void HImage.FindAnisoShapeModel(HShapeModel modelID, double angleStart, double angleExtent, double scaleRMin, double scaleRMax, double scaleCMin, double scaleCMax, HTuple minScore, int numMatches, double maxOverlap, HTuple subPixel, HTuple numLevels, double greediness, out HTuple row, out HTuple column, out HTuple angle, out HTuple scaleR, out HTuple scaleC, out HTuple score)`

`void HImage.FindAnisoShapeModel(HShapeModel modelID, double angleStart, double angleExtent, double scaleRMin, double scaleRMax, double scaleCMin, double scaleCMax, double minScore, int numMatches, double maxOverlap, string subPixel, int numLevels, double greediness, out HTuple row, out HTuple column, out HTuple angle, out HTuple scaleR, out HTuple scaleC, out HTuple score)`

## Description

The operator `FindAnisoShapeModel` finds the best
*`numMatches`* instances of the anisotropically scaled
shape model *`modelID`* in the input image *`image`*. The
model must have been created previously by calling
[`CreateAnisoShapeModel`](create_aniso_shape_model.md) or [`ReadShapeModel`](read_shape_model.md).

The position, rotation, and scale in the row and column direction of
the found instances of the model are returned in *`row`*,
*`column`*, *`angle`*, *`scaleR`*, and
*`scaleC`*. Additionally, the score of each found instance is returned in
*`score`*.

### Input parameters in detail

- ***`image`* and its domain:** —

  The domain of the image *`image`* determines the search space
  for the reference point of the model, i.e., for the center of
  gravity of the domain (region) of the image that was used to create
  the shape model with [`CreateAnisoShapeModel`](create_aniso_shape_model.md). A different
  origin set with [`SetShapeModelOrigin`](set_shape_model_origin.md) is not taken into
  account. The model is searched within those points of the domain of
  the image, in which the model lies completely within the image.
  This means that the model will not be found if it extends beyond the
  borders of the image, even if it would achieve a score greater than
  *`minScore`* (see below). Note that, if for a certain pyramid
  level the model touches the image border, it might not be found
  even if it lies completely within the original image.
  As a rule of thumb, the model might not be found if its distance to
  an image border falls below $2^{NumLevels-1}$.
  This behavior can be changed with
  `set_system('border_shape_models','true')` for all models or
  with `set_shape_model_param(ModelID,'border_shape_models','true')`
  for a specific model, which will cause
  models that extend beyond the image border to be found if they
  achieve a score greater than *`minScore`*. Here, points lying
  outside the image are regarded as being occluded, i.e., they lower
  the score. It should be noted that the runtime of the search will
  increase in this mode. Note further, that in rare cases, which occur
  typically only for artificial images, the model might not be found
  also if for certain pyramid levels the model touches the border
  of the reduced domain. Then, it may help to enlarge the reduced
  domain by $2^{NumLevels-1}$ using,
  e.g., [`DilationCircle`](dilation_circle.md).
- ***`angleStart`*, *`angleExtent`*, *`scaleRMin`*,
  *`scaleRMax`*, *`scaleCMin`*, *`scaleCMax`*:** —

  The parameters *`angleStart`* and *`angleExtent`*
  determine the range of rotations for which the model is searched.
  The parameters *`scaleRMin`*, *`scaleRMax`*,
  *`scaleCMin`*, and *`scaleCMax`* determine the range of
  scales in the row and column directions for which the model is
  searched. If necessary, both ranges are clipped to the range given
  when the model was created with [`CreateAnisoShapeModel`](create_aniso_shape_model.md).
  In particular, this means that the angle ranges of the model and the
  search must overlap.

  If in *`modelID`* a model is passed that was created by
  using [`CreateShapeModel`](create_shape_model.md) or [`CreateScaledShapeModel`](create_scaled_shape_model.md)
  then the model is searched with an isotropic scaling of 1.0
  or with an isotropic scaling within the range from *`scaleRMin`*
  to *`scaleRMax`*, respectively. In this case, for *`scaleR`*
  and *`scaleC`* identical values are returned.

  Note that in some cases instances with a rotation or scale that is
  slightly outside the specified range are found. This may happen if
  the specified range is smaller than the range given during the
  creation of the model. *`angleStart`* and *`angleExtent`*
  as well as *`scaleRMin`*/*`scaleCMin`* and
  *`scaleRMax`*/*`scaleCMax`* are checked only
  at the highest pyramid level. Matches that are found on the highest
  pyramid level are refined to the lowest pyramid level. For performance
  reasons, however, during the refinement it is no longer checked
  whether the matches are still within the specified ranges.
- ***`minScore`*:** —

  The parameter *`minScore`* determines what score a potential
  match must at least have to be regarded as an instance of the model
  in the image. The larger *`minScore`* is chosen, the faster
  the search is. If the model can be expected never to be occluded in
  the images, *`minScore`* may be set as high as 0.8 or even 0.9.
  If the matches are not tracked to the lowest pyramid level (see
  below) it might happen that instances with a score slightly below
  *`minScore`* are found.

  In case that the shape model has been extended by clutter parameters with
  [`SetShapeModelClutter`](set_shape_model_clutter.md) and thus *"use_clutter"* is enabled,
  *`minScore`* expects a second value which determines what clutter
  value a potential match must at most have to be regarded as an instance
  of the model in the image. The runtime using clutter parameters will be at
  least as high as the runtime without clutter parameters and
  *`numMatches`* set to *0*. Changing this second value does not
  influence the runtime.
- ***`numMatches`*:** —

  The maximum number of instances to be found can be determined with
  *`numMatches`*. If more than *`numMatches`* instances
  with a score greater than *`minScore`* are found in the image,
  only the best *`numMatches`* instances are returned. If fewer
  than *`numMatches`* are found, only that number is returned,
  i.e., the parameter *`minScore`* takes precedence over
  *`numMatches`*. If all model instances exceeding
  *`minScore`* in the image should be found, *`numMatches`*
  must be set to *0*.

  When tracking the matches through the image pyramid, on each level
  (except the top level),
  some less promising matches are rejected based on *`numMatches`*. Thus,
  it is possible that some matches are rejected that would have had a higher
  score on the lowest pyramid level. Due to this, for example, the found
  match for *`numMatches`* set to *1* might be
  different from the match with the highest score returned when setting
  *`numMatches`* to *0* or > *1*.

  If multiple objects with a similar score are expected, but only the one with
  the highest score should be returned, it might be preferable to raise
  *`numMatches`*, and then select the match with the highest score.

  In case that the shape model has been extended by clutter parameters
  using [`SetShapeModelClutter`](set_shape_model_clutter.md), *`numMatches`* also
  considers the second value passed in *`minScore`*: If more than
  *`numMatches`* instances with a score greater than the first
  entry of *`minScore`* and a clutter score smaller than the second
  entry of *`minScore`* are found in the image,
  only the best *`numMatches`* instances with respect to clutter
  are returned. Still,
  *`minScore`* takes precedence over *`numMatches`* and
  *`numMatches`* must be set to *0* if all model instances
  fulfilling the conditions imposed by *`minScore`* should be
  found. Please note that using clutter parameters, when tracking the matches
  through the image pyramid, no matches are rejected. Thus the runtime
  using clutter parameters will be at least as high as the runtime without clutter
  parameters and *`numMatches`* set to *0*.
- ***`maxOverlap`*:** —

  If the model exhibits symmetries it may happen that multiple
  instances with similar positions but different rotations are found
  in the image. The parameter *`maxOverlap`* determines by what
  fraction (i.e., a number between 0 and 1) two instances may at most
  overlap in order to consider them as different instances, and hence
  to be returned separately. If two instances overlap each other by
  more than *`maxOverlap`* only the best instance is returned.
  The calculation of the overlap is based on the smallest enclosing
  rectangle of arbitrary orientation (see [`SmallestRectangle2`](smallest_rectangle2.md))
  of the found instances. If *`maxOverlap`*=0, the found
  instances may not overlap at all, while for *`maxOverlap`*=1
  all instances are returned.
- ***`subPixel`*:** —

  The parameter *`subPixel`* determines whether the instances
  should be extracted with subpixel accuracy. If *`subPixel`* is
  set to *"none"* (or *"false"* for backwards
  compatibility) the model's pose is only determined with pixel
  accuracy and the angle and scale resolution that was specified with
  [`CreateAnisoShapeModel`](create_aniso_shape_model.md). If *`subPixel`* is set to
  *"interpolation"* (or *"true"*) the position as well
  as the rotation and scale are determined with subpixel accuracy. In
  this mode, the model's pose is interpolated from the score function.
  This mode costs almost no computation time and achieves an accuracy
  that is high enough for most applications. In some applications,
  however, the accuracy requirements are extremely high. In these
  cases, the model's pose can be determined through a least-squares
  adjustment, i.e., by minimizing the distances of the model points to
  their corresponding image points. In contrast to
  *"interpolation"*, this mode requires additional computation
  time. The different modes for least-squares adjustment
  (*"least_squares"*, *"least_squares_high"*, and
  *"least_squares_very_high"*) can be used to determine the
  accuracy with which the minimum distance is being searched. The
  higher the accuracy is chosen, the longer the subpixel extraction
  will take, however. Usually, *`subPixel`* should be set to
  *"interpolation"*. If least-squares adjustment is desired,
  *"least_squares"* should be chosen because this results in
  the best trade-off between runtime and accuracy.

  Objects that are slightly deformed with respect to the model, in
  some cases cannot be found or are found but only with a low
  accuracy. For such objects it is possible to additionally pass a
  maximal allowable object deformation in the parameter
  *`subPixel`*. The deformation must be specified in pixels. This
  can be done by passing the optional parameter value
  *"max_deformation "* followed by an integer value between
  *0* and *32* (in the same string), which specifies the
  maximum deformation. For example, if the shape of the object may be
  deformed by up to 2 pixels with respect to the shape that is stored
  in the model, the value *"max_deformation 2"* must be passed
  in *`subPixel`* in addition to the above described mode for the
  subpixel extraction, i.e., for example
  *["least_squares", "max_deformation 2"]*.
  Passing the value *"max_deformation 0"*
  corresponds to a search without allowing deformations, i.e., the
  behavior is the same as if no *"max_deformation "* is passed.
  Note that higher values for the maximum deformation often result in
  an increased runtime. Furthermore, the higher the deformation value
  is chosen, the higher is the risk of finding wrong model instances.
  Both problems mainly arise when searching for small objects or for
  objects with fine structures. This is because such kinds of objects
  for higher deformations lose their characteristic shape, which is
  important for a robust search. Also note that for higher
  deformations the accuracy of partially occluded objects might
  decrease if clutter is present close to the object. Consequently,
  the maximum deformation should be chosen as small as possible and
  only as high as necessary.
  Approximately rotationally symmetric objects may not be found if
  *"max_deformation"* and *`angleExtent`* are both set to a value
  greater than 0. In that case, ambiguities may occur that cannot be resolved,
  and the match is rejected as false. If this happens, try to set either
  *"max_deformation"* or *`angleExtent`* to 0, or adjust the model
  such that symmetries are reduced. When specifying a deformation higher
  than *0* the computation of the score depends on the chosen
  value for the subpixel extraction. In most cases, the score of a
  match changes if *"least_squares"*,
  *"least_squares_high"*, or *"least_squares_very_high"*
  (see above) is chosen for the subpixel extraction (in comparison to
  *"none"* or *"interpolation"*). Furthermore, if one of
  the least-squares adjustments is selected the score might increase
  when increasing the maximum deformation because then for the model
  points more corresponding image points can be found.
  To get a meaningful score value and to avoid erroneous matches, we
  recommend to always combine the allowance of a deformation with a
  least-squares adjustment.
- ***`numLevels`*:** —

  The number of pyramid levels used during the search is determined
  with *`numLevels`*. If necessary, the number of levels is
  clipped to the range given when the shape model was created with
  [`CreateAnisoShapeModel`](create_aniso_shape_model.md). If *`numLevels`* is set to
  *0*, the number of pyramid levels specified in
  [`CreateAnisoShapeModel`](create_aniso_shape_model.md) is used.

  In certain cases, the number of pyramid levels that was determined
  automatically with, for example, [`CreateAnisoShapeModel`](create_aniso_shape_model.md) may be
  too high. The consequence may be that some matches that may have a high
  final score are rejected on the highest pyramid level and thus are not
  found. Instead of setting *`minScore`* to a very low value to find all
  matches, it may be better to query the value of *`numLevels`* with
  [`GetShapeModelParams`](get_shape_model_params.md) and then use a slightly lower value in
  `FindAnisoShapeModel`. This approach is often better regarding
  the speed and robustness of the matching.

  Optionally, *`numLevels`* can contain a second value that determines
  the lowest pyramid level to which the found matches are tracked. Hence,
  a value of *[4,2]* for *`numLevels`* means that the
  matching starts at the fourth pyramid level and tracks the matches
  to the second lowest pyramid level (the lowest pyramid level is
  denoted by a value of 1). This mechanism can be used to decrease
  the runtime of the matching. It should be noted, however, that in
  general the accuracy of the extracted pose parameters is lower in
  this mode than in the normal mode, in which the matches are tracked
  to the lowest pyramid level. Hence, if a high accuracy is desired,
  *`subPixel`* should be set to at least
  *"least_squares"*. If the lowest pyramid level to use is
  chosen too large, it may happen that the desired accuracy cannot be
  achieved, or that wrong instances of the model are found because the
  model is not specific enough on the higher pyramid levels to
  facilitate a reliable selection of the correct instance of the
  model. In this case, the lowest pyramid level to use must be set to
  a smaller value.

  In input images of poor quality, i.e., in images that are, e.g.,
  defocused, deformed, or noisy, often no instances of the shape model
  can be found on the lowest pyramid level. The reason for this
  behavior is the missing or deformed edge information which is a
  result of the poor image quality. Nevertheless, the edge
  information may be sufficient on higher pyramid levels. But keep in
  mind the above mentioned restrictions on accuracy and robustness if
  instances that were found on higher pyramid levels are used. The
  selection of the suitable pyramid level, i.e., the lowest pyramid
  level on which at least one instance of the shape model can be
  found, depends on the model and on the input image. This pyramid
  level may vary from image to image. To facilitate the matching on
  images of poor quality, the lowest pyramid level on which at least
  one instance of the model can be found can be determined
  automatically during the matching. To activate this mechanism, i.e.,
  to use the so-called 'increased tolerance mode', the
  lowest pyramid level must be specified negatively in
  *`numLevels`*. If, e.g., *`numLevels`* is set to
  *[4,-2]*, the matching starts at the fourth pyramid level and
  tracks the matches to the second lowest pyramid level. This means
  that an instance of the shape model is searched on the pyramid level
  2. If no instance of the model can be found on this pyramid level,
  the lowest pyramid level is determined on which at least one
  instance of the model can be found. The instances of this pyramid
  level will then be returned.

  If the *`modelID`* was adapted with [`AdaptShapeModelHighNoise`](adapt_shape_model_high_noise.md)
  the estimated lowest pyramid level will be used by default.
  However, the user can override the estimated lowest pyramid level by
  providing two values to *`numLevels`* and explicitly setting
  the lowest pyramid level.
- ***`greediness`*:** —

  The parameter *`greediness`* determines how “greedily” the
  search should be carried out. If *`greediness`*=0, a safe
  search heuristic is used, which always finds the model if it is
  visible in the image and the other parameters are set appropriately.
  However, the search will be relatively time
  consuming in this case. If *`greediness`*=1, an unsafe
  search heuristic is used, which may cause the model not to be found
  in rare cases, even though it is visible in the image. For
  *`greediness`*=1, the maximum search speed is achieved. In
  almost all cases, the shape model will always be found for
  *`greediness`*=0.9.

### Output parameters in detail

- ***`row`*, *`column`*, *`angle`*, *`scaleR`*,
  *`scaleC`*:** —

  The position, rotation, and scale in the row and column direction of
  the found instances of the model are returned in *`row`*,
  *`column`*, *`angle`*, *`scaleR`*, and
  *`scaleC`*.
  The coordinates *`row`* and *`column`* are related to the
  position of the origin of the shape model in the search image.
  However, *`row`* and *`column`* do not
  exactly correspond to this position.
  Instead, `FindAnisoShapeModel` returns slightly modified values
  that are optimized for creating a transformation matrix, that can be used for
  alignment or visualization of the model contours.
  (This has to do with the way HALCON transforms iconic objects,
  see [`AffineTransPixel`](affine_trans_pixel.md)).
  The example below shows how to create the transformation matrix for alignment
  of the found matches and how to use it to display them in the search image.

  By default, the model
  origin is the center of gravity of the domain (region) of the image
  that was used to create the shape model with
  [`CreateAnisoShapeModel`](create_aniso_shape_model.md). A different origin can be set with
  [`SetShapeModelOrigin`](set_shape_model_origin.md).
- ***`score`*:** —

  The score of each found instance is returned in
  *`score`*. The score is a number between 0 and 1, which is an
  approximate measure of how much of the model is visible in the
  image. If, for example, half of the model is occluded, the score
  cannot exceed 0.5.

  In case that the shape model has been extended by clutter parameters
  using [`SetShapeModelClutter`](set_shape_model_clutter.md), following the above values
  *`score`* also returns the clutter scores of each found instance.
  If, for example, half of the clutter region is filled by clutter edges,
  the clutter score will equal 0.5.
  If, e.g., two instances are found, the score is 0.9 for
  the first instance and 0.8 for the second instance, and the clutter score
  is 0.2 for the first instance and 0.1 for the second instance,
  *`score`* = *[0.9,0.8,0.2,0.1]* is returned.
  Please note that of all shape-based matching results, clutter scores are
  affected the most when a variation of illumination occurs.

### Specifying a timeout

Using the operator [`SetShapeModelParam`](set_shape_model_param.md) you can specify a
*"timeout"* for `FindAnisoShapeModel`.
If `FindAnisoShapeModel` reaches this *"timeout"*, it
terminates without results and returns the error code 9400 (H_ERR_TIMEOUT).
Depending on the scaling ranges specified by *`scaleRMin`*,
*`scaleRMax`*, *`scaleCMin`*, and *`scaleCMax`*,
`FindAnisoShapeModel` needs a significant
amount of time to free cached transformations if the shape model is not
pregenerated. As this transformations have to be freed after a timeout
occurs, the runtime of `FindAnisoShapeModel` exceeds the value of
the specified *"timeout"* by this time.

### Visualization of the results

To display the results found by shape-based matching,
we highly recommend the usage of the procedure
`dev_display_shape_matching_results`.

### Further Information

For an explanation of the different 2D coordinate systems
used in HALCON, see the introduction of chapter
[Transformations / 2D Transformations](toc_transformations_2dtransformations.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator supports canceling timeouts and interrupts.

## Parameters

**`image`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / uint2)

Input image in which the model should be found.

**`modelID`** (input_control)  shape_model `→` [HShapeModel](HShapeModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

**`angleStart`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Smallest rotation of the model.

Default:
-0.39

Suggested values:
-3.14, -1.57, -0.79, -0.39, -0.20, 0.0

**`angleExtent`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Extent of the rotation angles.

Default:
0.79

Suggested values:
6.29, 3.14, 1.57, 0.79, 0.39, 0.0

Restriction:
`AngleExtent >= 0`

**`scaleRMin`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Minimum scale of the model in the row direction.

Default:
0.9

Suggested values:
0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Restriction:
`ScaleRMin > 0`

**`scaleRMax`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Maximum scale of the model in the row direction.

Default:
1.1

Suggested values:
1.0, 1.1, 1.2, 1.3, 1.4, 1.5

Restriction:
`ScaleRMax >= ScaleRMin`

**`scaleCMin`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Minimum scale of the model in the column direction.

Default:
0.9

Suggested values:
0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Restriction:
`ScaleCMin > 0`

**`scaleCMax`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Maximum scale of the model in the column direction.

Default:
1.1

Suggested values:
1.0, 1.1, 1.2, 1.3, 1.4, 1.5

Restriction:
`ScaleCMax >= ScaleCMin`

**`minScore`** (input_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Minimum score of the instances of the model to
be found.

Default:
0.5

Suggested values:
0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Value range:
`0
≤
minScore
≤
1`

Minimum increment:
0.01

Recommended increment:
0.05

**`numMatches`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of instances of the model to be found
(or 0 for all matches).

Default:
1

Suggested values:
0, 1, 2, 3, 4, 5, 10, 20

**`maxOverlap`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Maximum overlap of the instances of the model
to be found.

Default:
0.5

Suggested values:
0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Value range:
`0
≤
maxOverlap
≤
1`

Minimum increment:
0.01

Recommended increment:
0.05

**`subPixel`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Subpixel accuracy if not equal to *"none"*.

Default:
"least_squares"

Suggested values:
"none", "interpolation", "least_squares", "least_squares_high", "least_squares_very_high", "max_deformation 1", "max_deformation 2", "max_deformation 3", "max_deformation 4", "max_deformation 5", "max_deformation 6"

**`numLevels`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Number of pyramid levels used in the matching
(and lowest pyramid level to use if
|*`numLevels`*| = 2).

Default:
0

List of values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

**`greediness`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

“Greediness” of the search heuristic (0: safe
but slow; 1: fast but matches may be missed).

Default:
0.9

Suggested values:
0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Value range:
`0
≤
greediness
≤
1`

Minimum increment:
0.01

Recommended increment:
0.05

**`row`** (output_control)  point.y-array `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the found instances of the model.

**`column`** (output_control)  point.x-array `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the found instances of the model.

**`angle`** (output_control)  angle.rad-array `→` [HTuple](HTuple.md) (*double*)

Rotation angle of the found instances of the model.

**`scaleR`** (output_control)  number-array `→` [HTuple](HTuple.md) (*double*)

Scale of the found instances of the model in
the row direction.

**`scaleC`** (output_control)  number-array `→` [HTuple](HTuple.md) (*double*)

Scale of the found instances of the model in
the column direction.

**`score`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Score of the found instances of the model.

## Example (HDevelop)

```
create_aniso_shape_model (ImageReduced, 0, rad(-15), rad(30), 0, \
                          0.9, 1.1, 0, 0.9, 1.1, 0, 'none', \
                          'use_polarity', 30, 10, ModelID)
get_shape_model_contours (ModelXLD, ModelID, 1)
find_aniso_shape_model (SearchImage, ModelID, rad(-15), rad(30), \
                        0.9, 1.1, 0.9, 1.1, 0.5, 1, 0.5, 'interpolation', \
                        0, 0, Row, Column, Angle, ScaleR, ScaleC, Score)
* Create transformation matrix
hom_mat2d_identity (HomMat2DIdentity)
hom_mat2d_scale (HomMat2DIdentity, ScaleR, ScaleC, 0, 0, HomMat2DScale)
hom_mat2d_rotate (HomMat2DScale, Angle, 0, 0, HomMat2DRotate)
hom_mat2d_translate (HomMat2DRotate, Row, Column, HomMat2DObject)
* Calculate true position of the model origin in the search image
affine_trans_pixel (HomMat2DObject, 0, 0, RowObject, ColObject)
* Display results
dev_display_shape_matching_results (ModelID, 'red', Row, Column, Angle, \
                  ScaleR, ScaleC, 0)
```

## Result

If the parameter values are correct, the operator
`FindAnisoShapeModel` returns the value 2 (
H_MSG_TRUE)
. If the
input is empty (no input images are available) the behavior can be
set via `set_system('no_object_result',<Result>)`. If
necessary, an exception is raised.

## Possible Predecessors

`CreateAnisoShapeModel`,
`ReadShapeModel`,
`SetShapeModelOrigin`,
`SetShapeModelClutter`

## Possible Successors

`ClearShapeModel`

## Alternatives

`FindGenericShapeModel`

## See also

`SetSystem`,
`GetSystem`

## Module

Matching
