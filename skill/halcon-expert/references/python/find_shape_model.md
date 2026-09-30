# find_shape_model (Operator)

## Name

`find_shape_model` — Find the best matches of a shape model in an image.

## Signature

`def find_shape_model(image: HObject, model_id: HHandle, angle_start: float, angle_extent: float, min_score: MaybeSequence[float], num_matches: int, max_overlap: float, sub_pixel: MaybeSequence[str], num_levels: MaybeSequence[int], greediness: float) -> Tuple[Sequence[float], Sequence[float], Sequence[float], Sequence[float]]`

## Description

The operator `find_shape_model` finds the best
*`num_matches`* instances of the shape model *`model_id`* in
the input image *`image`*. The model must have been created
previously by calling [`create_shape_model`](create_shape_model.md) or
[`read_shape_model`](read_shape_model.md).

The position and rotation of the found instances of the model is
returned in *`row`*, *`column`*, and *`angle`*.
Additionally, the score of each found instance is returned in
*`score`*.

### Input parameters in detail

- ***`image`* and its domain:** —

  The domain of the image *`image`* determines the search space
  for the reference point of the model, i.e., for the center of
  gravity of the domain (region) of the image that was used to create
  the shape model with [`create_shape_model`](create_shape_model.md). A different origin
  set with [`set_shape_model_origin`](set_shape_model_origin.md) is not taken into account.
  The model is searched within those points of the domain of the
  image, in which the model lies completely within the image. This
  means that the model will not be found if it extends beyond the
  borders of the image, even if it would achieve a score greater than
  *`min_score`* (see below). Note that, if for a certain pyramid
  level the model touches the image border, it might not be found
  even if it lies completely within the original image.
  As a rule of thumb, the model might not be found if its distance to
  an image border falls below $2^{NumLevels-1}$.
  This behavior can be changed with
  `set_system('border_shape_models','true')` for all models or
  with `set_shape_model_param(ModelID,'border_shape_models','true')`
  for a specific model, which will cause
  models that extend beyond the image border to be found if they
  achieve a score greater than *`min_score`*. Here, points lying
  outside the image are regarded as being occluded, i.e., they lower
  the score. It should be noted that the runtime of the search will
  increase in this mode. Note further, that in rare cases, which occur
  typically only for artificial images, the model might not be found
  also if for certain pyramid levels the model touches the border
  of the reduced domain. Then, it may help to enlarge the reduced
  domain by $2^{NumLevels-1}$ using,
  e.g., [`dilation_circle`](dilation_circle.md).
- ***`angle_start`* and *`angle_extent`*:** —

  The parameters *`angle_start`* and *`angle_extent`*
  determine the range of rotations for which the model is searched.
  If necessary, the range of rotations is clipped to the range given
  when the model was created with [`create_shape_model`](create_shape_model.md). In
  particular, this means that the angle ranges of the model and the
  search must overlap.

  Note that in some cases instances with a rotation that is slightly
  outside the specified range are found. This may happen if the specified
  range is smaller than the range given during the creation of the model.
  *`angle_start`* and *`angle_extent`* are checked only
  at the highest pyramid level. Matches that are found on the highest
  pyramid level are refined to the lowest pyramid level. For performance
  reasons, however, during the refinement it is no longer checked
  whether the matches are still within the specified range.
- ***`min_score`*:** —

  The parameter *`min_score`* determines what score a potential
  match must at least have to be regarded as an instance of the model
  in the image. The larger *`min_score`* is chosen, the faster
  the search is. If the model can be expected never to be occluded in
  the images, *`min_score`* may be set as high as 0.8 or even 0.9.
  If the matches are not tracked to the lowest pyramid level (see
  below) it might happen that instances with a score slightly below
  *`min_score`* are found.

  In case that the shape model has been extended by clutter parameters with
  [`set_shape_model_clutter`](set_shape_model_clutter.md) and thus *"use_clutter"* is enabled,
  *`min_score`* expects a second value which determines what clutter
  score a potential match must at most have to be regarded as an instance
  of the model in the image. The runtime using clutter parameters will be at
  least as high as the runtime without clutter parameters and
  *`num_matches`* set to *0*. Changing this second value does not
  influence the runtime.
- ***`num_matches`*:** —

  The maximum number of instances to be found can be determined with
  *`num_matches`*. If more than *`num_matches`* instances
  with a score greater than *`min_score`* are found in the image,
  only the best *`num_matches`* instances are returned. If fewer
  than *`num_matches`* are found, only that number is returned,
  i.e., the parameter *`min_score`* takes precedence over
  *`num_matches`*. If all model instances exceeding
  *`min_score`* in the image should be found, *`num_matches`*
  must be set to *0*.

  When tracking the matches through the image pyramid, on each level
  (except the top level),
  some less promising matches are rejected based on *`num_matches`*. Thus,
  it is possible that some matches are rejected that would have had a higher
  score on the lowest pyramid level. Due to this, for example, the found
  match for *`num_matches`* set to *1* might be
  different from the match with the highest score returned when setting
  *`num_matches`* to *0* or > *1*.

  If multiple objects with a similar score are expected, but only the one with
  the highest score should be returned, it might be preferable to raise
  *`num_matches`*, and then select the match with the highest score.

  In case that the shape model has been extended by clutter parameters
  using [`set_shape_model_clutter`](set_shape_model_clutter.md), *`num_matches`* also
  considers the second value passed in *`min_score`*.
  Matched instances will be in this case instances with a score greater
  than the first entry of *`min_score`* and a clutter score smaller
  than its second entry. If the number of matched instances in the image
  is larger than *`num_matches`*, the best *`num_matches`* instances
  with respect to clutter scores are returned. Still,
  *`min_score`* takes precedence over *`num_matches`* and
  *`num_matches`* must be set to *0* if all model instances
  fulfilling the conditions imposed by *`min_score`* should be
  returned. Please note that using clutter parameters, when tracking the
  matches through the image pyramid, no matches are rejected. Thus the runtime
  using clutter parameters will be at least as high as the runtime without clutter
  parameters and *`num_matches`* set to *0*.
- ***`max_overlap`*:** —

  If the model exhibits symmetries it may happen that multiple
  instances with similar positions but different rotations are found
  in the image. The parameter *`max_overlap`* determines by what
  fraction (i.e., a number between 0 and 1) two instances may at most
  overlap in order to consider them as different instances, and hence
  to be returned separately. If two instances overlap each other by
  more than *`max_overlap`* only the best instance is returned.
  The calculation of the overlap is based on the smallest enclosing
  rectangle of arbitrary orientation (see [`smallest_rectangle2`](smallest_rectangle2.md))
  of the found instances. If *`max_overlap`*=0, the found
  instances may not overlap at all, while for *`max_overlap`*=1
  all instances are returned.
- ***`sub_pixel`*:** —

  The parameter *`sub_pixel`* determines whether the instances
  should be extracted with subpixel accuracy. If *`sub_pixel`* is
  set to *"none"* (or *"false"* for backwards
  compatibility) the model's pose is only determined with pixel
  accuracy and the angle resolution that was specified with
  [`create_shape_model`](create_shape_model.md). If *`sub_pixel`* is set to
  *"interpolation"* (or *"true"*) the position as well
  as the rotation are determined with subpixel accuracy. In this
  mode, the model's pose is interpolated from the score function.
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
  will take, however. Usually, *`sub_pixel`* should be set to
  *"interpolation"*. If least-squares adjustment is desired,
  *"least_squares"* should be chosen because this results in
  the best trade-off between runtime and accuracy.

  Objects that are slightly deformed with respect to the model, in
  some cases cannot be found or are found but only with a low
  accuracy. For such objects it is possible to additionally pass a
  maximal allowable object deformation in the parameter
  *`sub_pixel`*. The deformation must be specified in pixels. This
  can be done by passing the optional parameter value
  *"max_deformation "* followed by an integer value between
  *0* and *32* (in the same string), which specifies the
  maximum deformation. For example, if the shape of the object may be
  deformed by up to 2 pixels with respect to the shape that is stored
  in the model, the value *"max_deformation 2"* must be passed
  in *`sub_pixel`* in addition to the above described mode for the
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
  *"max_deformation"* and *`angle_extent`* are both set to a value
  greater than 0. In that case, ambiguities may occur that cannot be resolved,
  and the match is rejected as false. If this happens, try to set either
  *"max_deformation"* or *`angle_extent`* to 0, or adjust the model
  such that symmetries are reduced.
  When specifying a deformation higher
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
- ***`num_levels`*:** —

  The number of pyramid levels used during the search is determined
  with *`num_levels`*. If necessary, the number of levels is
  clipped to the range given when the shape model was created with
  [`create_shape_model`](create_shape_model.md). If *`num_levels`* is set to
  *0*, the number of pyramid levels specified in
  [`create_shape_model`](create_shape_model.md) is used.

  In certain cases, the number of pyramid levels that was determined
  automatically with, for example, [`create_shape_model`](create_shape_model.md) may be too high.
  The consequence may be that some matches that may have a high final score
  are rejected on the highest pyramid level and thus are not found. Instead
  of setting *`min_score`* to a very low value to find all matches, it
  may be better to query the value of *`num_levels`* with
  [`get_shape_model_params`](get_shape_model_params.md) and then use a slightly lower value in
  `find_shape_model`. This approach is often better regarding the speed
  and robustness of the matching.

  Optionally, *`num_levels`*
  can contain a second value that determines the lowest pyramid level
  to which the found matches are tracked. Hence, a value of
  *[4,2]* for *`num_levels`* means that the matching starts
  at the fourth pyramid level and tracks the matches to the second
  lowest pyramid level (the lowest pyramid level is denoted by a value
  of 1). This mechanism can be used to decrease the runtime of the
  matching. It should be noted, however, that in general the accuracy
  of the extracted pose parameters is lower in this mode than in the
  normal mode, in which the matches are tracked to the lowest pyramid
  level. Hence, if a high accuracy is desired, *`sub_pixel`*
  should be set to at least *"least_squares"*. If the lowest
  pyramid level to use is chosen too large, it may happen that the
  desired accuracy cannot be achieved, or that wrong instances of the
  model are found because the model is not specific enough on the
  higher pyramid levels to facilitate a reliable selection of the
  correct instance of the model. In this case, the lowest pyramid
  level to use must be set to a smaller value.

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
  *`num_levels`*. If, e.g., *`num_levels`* is set to
  *[4,-2]*, the matching starts at the fourth pyramid level and
  tracks the matches to the second lowest pyramid level. This means
  that an instance of the shape model is searched on the pyramid level
  2. If no instance of the model can be found on this pyramid level,
  the lowest pyramid level is determined on which at least one
  instance of the model can be found. The instances of this pyramid
  level will then be returned.

  If the *`model_id`* was adapted with [`adapt_shape_model_high_noise`](adapt_shape_model_high_noise.md)
  the estimated lowest pyramid level will be used by default.
  However, the user can override the estimated lowest pyramid level by
  providing two values to *`num_levels`* and explicitly setting
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

- ***`row`*, *`column`*, and *`angle`*:** —

  The position and rotation of the found instances of the model is
  returned in *`row`*, *`column`*, and *`angle`*.
  The coordinates *`row`* and *`column`* are related to the
  position of the origin of the shape model in the search image.
  However, *`row`* and *`column`* do not
  exactly correspond to this position.
  Instead, `find_shape_model` returns slightly modified values
  that are optimized for creating a transformation matrix, that can be used for
  alignment or visualization of the model contours.
  (This has to do with the way HALCON transforms iconic objects,
  see [`affine_trans_pixel`](affine_trans_pixel.md)).
  The example below shows how to create the transformation matrix for alignment
  of the found matches and how to use it to display them in the search image.

  By default, the model
  origin is the center of gravity of the domain (region) of the image
  that was used to create the shape model with
  [`create_aniso_shape_model`](create_aniso_shape_model.md). A different origin can be set with
  [`set_shape_model_origin`](set_shape_model_origin.md).
- ***`score`*:** —

  The score of each found instance is returned in
  *`score`*. The score is a number between 0 and 1, which is an
  approximate measure of how much of the model is visible in the
  image. If, for example, half of the model is occluded, the score
  cannot exceed 0.5.

  In case that the shape model has been extended by clutter parameters
  using [`set_shape_model_clutter`](set_shape_model_clutter.md), following the above values
  *`score`* also returns the clutter score of each found instance.
  If, for example, half of the clutter region is filled by clutter edges,
  the clutter score will equal 0.5.
  If, e.g., two instances are found, the score is 0.9 for
  the first instance and 0.8 for the second instance, and the clutter score
  is 0.2 for the first instance and 0.1 for the second instance,
  *`score`* = *[0.9,0.8,0.2,0.1]* is returned.
  Please note that of all shape-based matching results, clutter scores are
  affected the most when a variation of illumination occurs.

### Specifying a timeout

Using the operator [`set_shape_model_param`](set_shape_model_param.md) you can specify a
*"timeout"* for `find_shape_model`. If `find_shape_model`
reaches this *"timeout"*, it terminates without results and
returns the error code 9400 (H_ERR_TIMEOUT).

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

**`image`** (input_object)  (multichannel-)image `→` HObject (byte / uint2)

Input image in which the model should be found.

**`model_id`** (input_control)  shape_model `→` HHandle

Handle of the model.

**`angle_start`** (input_control)  angle.rad `→` float

Smallest rotation of the model.

Default:
-0.39

Suggested values:
-3.14, -1.57, -0.79, -0.39, -0.20, 0.0

**`angle_extent`** (input_control)  angle.rad `→` float

Extent of the rotation angles.

Default:
0.79

Suggested values:
6.29, 3.14, 1.57, 0.79, 0.39, 0.0

Restriction:
`AngleExtent >= 0`

**`min_score`** (input_control)  real(-array) `→` MaybeSequence[float]

Minimum score of the instances of the model to
be found.

Default:
0.5

Suggested values:
0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Value range:
`0
≤
min_score
≤
1`

Minimum increment:
0.01

Recommended increment:
0.05

**`num_matches`** (input_control)  integer `→` int

Number of instances of the model to be found
(or 0 for all matches).

Default:
1

Suggested values:
0, 1, 2, 3, 4, 5, 10, 20

**`max_overlap`** (input_control)  real `→` float

Maximum overlap of the instances of the model
to be found.

Default:
0.5

Suggested values:
0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Value range:
`0
≤
max_overlap
≤
1`

Minimum increment:
0.01

Recommended increment:
0.05

**`sub_pixel`** (input_control)  string(-array) `→` MaybeSequence[str]

Subpixel accuracy if not equal to *"none"*.

Default:
"least_squares"

Suggested values:
"none", "interpolation", "least_squares", "least_squares_high", "least_squares_very_high", "max_deformation 1", "max_deformation 2", "max_deformation 3", "max_deformation 4", "max_deformation 5", "max_deformation 6"

**`num_levels`** (input_control)  integer(-array) `→` MaybeSequence[int]

Number of pyramid levels used in the matching
(and lowest pyramid level to use if
|*`num_levels`*| = 2).

Default:
0

List of values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

**`greediness`** (input_control)  real `→` float

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

**`row`** (output_control)  point.y-array `→` Sequence[float]

Row coordinate of the found instances of the model.

**`column`** (output_control)  point.x-array `→` Sequence[float]

Column coordinate of the found instances of the model.

**`angle`** (output_control)  angle.rad-array `→` Sequence[float]

Rotation angle of the found instances of the model.

**`score`** (output_control)  real-array `→` Sequence[float]

Score of the found instances of the model.

## Example (HDevelop)

```
create_shape_model (ImageReduced, 0, rad(-45), rad(180), 0, \
                    'none', 'use_polarity', 30, 10, ModelID)
get_shape_model_contours (ModelXLD, ModelID, 1)
find_shape_model (SearchImage, ModelID, rad(-45), rad(180), \
                  0.5, 1, 0.5, 'interpolation', \
                  0, 0, Row, Column, Angle, Score)
* Create transformation matrix
vector_angle_to_rigid (0, 0, 0, Row, Column, Angle, HomMat2DObject)
* Display results
dev_display_shape_matching_results (ModelID, 'red', Row, Column, Angle, \
                                    1, 1, 0)
```

## Result

If the parameter values are correct, the operator
`find_shape_model` returns the value 2 (
H_MSG_TRUE)
. If the input is
empty (no input images are available) the behavior can be set via
`set_system('no_object_result',<Result>)`. If necessary, an
exception is raised.

## Possible Predecessors

`create_shape_model`,
`read_shape_model`,
`set_shape_model_origin`,
`set_shape_model_clutter`

## Possible Successors

`clear_shape_model`

## Alternatives

`find_generic_shape_model`

## See also

`set_system`,
`get_system`,
`set_shape_model_param`

## Module

Matching
