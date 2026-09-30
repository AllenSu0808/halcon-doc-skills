# find_shape_model_3d (Operator)

## Name

`find_shape_model_3d` — Find the best matches of a 3D shape model in an image.

## Signature

`def find_shape_model_3d(image: HObject, shape_model_3did: HHandle, min_score: float, greediness: float, num_levels: Sequence[int], gen_param_name: Sequence[str], gen_param_value: Sequence[Union[int, float, str]]) -> Tuple[Sequence[Union[int, float]], Sequence[float], Sequence[float]]`

## Description

The operator `find_shape_model_3d` finds the best matches of
the 3D shape model *`shape_model_3did`* in the input
*`image`*. The 3D shape model must have been created
previously by calling [`create_shape_model_3d`](create_shape_model_3d.md) or
[`read_shape_model_3d`](read_shape_model_3d.md).

The 3D pose of the found instances of the model is returned in
*`pose`*. The pose is in the form
$\mathrm{ccs} \mathbf{P}_{\mathrm{mcs}}$ ![figure](../assets/36630faf4c6dcd27.svg), where
*ccs* denotes the camera coordinate system and
*mcs* the model coordinate system (which is a 3D world coordinate
system), see [Transformations / Poses](toc_transformations_poses.md) and
`“Solution Guide III-C - 3D Vision”`.
Hence, it describes the pose of the 3D object model in camera coordinates.
It should be noted that the resulting
*`pose`* does not refer to reference coordinate system that is
introduced in [`create_shape_model_3d`](create_shape_model_3d.md) but to the original 3D
object model coordinate system used in the CAD file. If a pose
refinement was applied (see below), additionally the accuracy of the
six pose parameters are returned in *`cov_pose`*. By default,
*`cov_pose`* contains the 6 standard deviations of the pose
parameters for each match. In contrast, if the generic parameter
*"cov_pose_mode"* (see below) was set to
*"covariances"*, *`cov_pose`* contains the 36 values of
the complete 6×6 covariance matrix of the 6
pose parameters. Note that this reflects only an inner accuracy from
which the real accuracy of the pose may differ. Finally, the score
of each found instance is returned in *`score`*. The score is
a number between 0 and 1, which is an approximate measure of how
much of the model is visible in the image. If, for example, half of
the model is occluded, the score cannot exceed 0.5.

### Input parameters in detail

- ***`image`* and its domain:** —

  The domain of the image *`image`* determines the search space
  for the reference point of the 3D object model. There is no need to
  correct any distortions in *`image`* as the calibration data has
  already been provided during the model creation.
- ***`min_score`*:** —

  The parameter *`min_score`* determines what score a potential
  match must at least have to be regarded as an instance of the model
  in the image. The larger *`min_score`* is chosen, the faster
  the search is. If the model can be expected never to be occluded in
  the images, *`min_score`* may be set as high as 0.8 or even 0.9.
  Note that in images with a high degree of clutter or strong
  background texture, *`min_score`* should be set to a value not
  much lower than *0.7* since otherwise false matches could
  be found.
- ***`greediness`*:** —

  The parameter *`greediness`* determines how “greedily” the
  search should be carried out. If *`greediness`*=0, a safe
  search heuristic is used, which always finds the model if it is
  visible in the image. However, the search will be relatively time
  consuming in this case. If *`greediness`*=1, an unsafe
  search heuristic is used, which may cause the model not to be found
  in rare cases, even though it is visible in the image. For
  *`greediness`*=1, the maximum search speed is achieved. In
  almost all cases, the 3D shape model will always be found for
  *`greediness`*=0.9.
- ***`num_levels`*:** —

  The number of pyramid levels used during the search is determined
  with *`num_levels`*. If necessary, the number of levels is
  clipped to the range given when the 3D shape model was created with
  [`create_shape_model_3d`](create_shape_model_3d.md). If *`num_levels`* is set to
  *0*, the number of pyramid levels specified in
  [`create_shape_model_3d`](create_shape_model_3d.md) is used. Optionally,
  *`num_levels`* can contain a second value that determines the
  lowest pyramid level to which the found matches are tracked. Hence,
  a value of *[4,2]* for *`num_levels`* means that the
  matching starts at the fourth pyramid level and tracks the matches
  to the second lowest pyramid level (the lowest pyramid level is
  denoted by a value of 1). This mechanism can be used to decrease
  the runtime of the matching. If the lowest pyramid level to use is
  chosen too large, it may happen that the desired accuracy cannot be
  achieved, or that wrong instances of the model are found because the
  model is not specific enough on the higher pyramid levels to
  facilitate a reliable selection of the correct instance of the
  model. In this case, the lowest pyramid level to use must be set to
  a smaller value.
- ***`gen_param_name`* and *`gen_param_value`*:** —

  In addition to the parameters described above, there are some
  generic parameters that can optionally be used to influence the
  matching. For most applications these parameters need not to be
  specified but can be left at their default values. If desired, these
  parameters and their corresponding values can be specified by using
  *`gen_param_name`* and *`gen_param_value`*, respectively.
  The following values for *`gen_param_name`* are possible:

  - If the pose range in which the model is to be searched is smaller
    than the pose range that was specified during the model creation
    with [`create_shape_model_3d`](create_shape_model_3d.md), the pose range can be
    restricted appropriately with the following parameters. If the
    values lie outside the pose range of the model, the values are
    automatically clipped to the pose range of the model.

    - ***"longitude_min"*:** —

      Sets the minimum longitude of the pose range.

      Suggested values:
       *"rad(-45)"*, *"rad(-30)"*,
      *"rad(-15)"*

      Default:
       *"rad(-180)"*
    - ***"longitude_max"*:** —

      Sets the maximum longitude of the pose range.

      Suggested values:
       *"rad(15)"*, *"rad(30)"*,
      *"rad(45)"*

      Default:
       *"rad(180)"*
    - ***"latitude_min"*:** —

      Sets the minimum latitude of the pose range.

      Suggested values:
       *"rad(-45)"*, *"rad(-30)"*,
      *"rad(-15)"*

      Default:
       *"rad(-90)"*
    - ***"latitude_max"*:** —

      Sets the maximum latitude of the pose range.

      Suggested values:
       *"rad(15)"*, *"rad(30)"*,
      *"rad(45)"*

      Default:
       *"rad(90)"*
    - ***"cam_roll_min"*:** —

      Sets the minimum camera roll angle of the pose range.

      Suggested values:
       *"rad(-45)"*, *"rad(-30)"*,
      *"rad(-15)"*

      Default:
       *"rad(-180)"*
    - ***"cam_roll_max"*:** —

      Sets the maximum camera roll angle of the pose range.

      Suggested values:
       *"rad(15)"*, *"rad(30)"*,
      *"rad(45)"*

      Default:
       *"rad(180)"*
    - ***"dist_min"*:** —

      Sets the minimum camera-object-distance of the pose range.

      Suggested values:
       *0.05*, *0.1*,
      *0.5*, *1.0*

      Default:
       *0*
    - ***"dist_max"*:** —

      Sets the maximum camera-object-distance of the pose range.

      Suggested values:
       *0.05*, *0.1*,
      *0.5*, *1.0*

      Default:
       $(\infty)$
  - Further generic parameters that do not concern the pose range can be
    specified:

    - ***"num_matches"*:** —

      With this parameter the maximum number of instances to be found
      can be determined. If more than the specified number of
      instances with a score greater than *`min_score`* are found
      in the image, only the best *"num_matches"* instances are
      returned. If fewer than *"num_matches"* are found, only
      that number is returned, i.e., the parameter *`min_score`*
      takes precedence over *"num_matches"*. If
      *"num_matches"* is set to *0*, all matches that
      satisfy the score criterion are returned. Note that the more
      matches should be found the slower the matching will be.

      Suggested values:
       *0*, *1*, *2*,
      *3*

      Default:
       *1*
    - ***"max_overlap"*:** —

      It may happen that multiple instances with similar positions but
      with different orientations are found in the image. The
      parameter *"max_overlap"* determines by what fraction
      (i.e., a number between 0 and 1) two instances may at most
      overlap in order to consider them as different instances, and
      hence to be returned separately. If two instances overlap each
      other by more than the specified value only the best instance is
      returned. The calculation of the overlap is based on the
      smallest enclosing rectangle of arbitrary orientation (see
      [`smallest_rectangle2`](smallest_rectangle2.md)) of the found instances.
      If in [`create_shape_model_3d`](create_shape_model_3d.md) for
      *"lowest_model_level"* a value larger than *1*
      was passed, the overlap calculation is based on the projection
      of the smallest enclosing axis-parallel cuboid of the 3D
      object model. Because in this case the overlap might be
      overestimated, in some cases it could be necessary to increase
      the value for *"max_overlap"*. If
      *"max_overlap"*=0, the found instances may not overlap
      at all, while for *"max_overlap"*=1 all instances are
      returned.

      Suggested values:
       *0.0*, *0.2*, *0.4*,
      *0.6*, *0.8*, *1.0*

      Default:
       *0.5*
    - ***"pose_refinement"*:** —

      This parameter
      determines whether the poses of the instances should be refined
      after the matching. If *"pose_refinement"* is set to
      *"none"* the model's pose is only determined with a
      limited accuracy. In this case, the accuracy depends on several
      sampling steps that are used inside the matching process and,
      therefore cannot be predicted very well. Therefore,
      *"pose_refinement"* should only be set to *"none"*
      when the computation time is of primary concern and an
      approximate pose is sufficient. In all other cases the pose
      should be determined through a least-squares adjustment, i.e.,
      by minimizing the distances of the model points to their
      corresponding image points. In order to achieve a high
      accuracy, this refinement is directly performed in
      3D. Therefore, the refinement requires additional computation
      time. If the system variable (see [`set_system`](set_system.md))
      *"opengl_hidden_surface_removal_enable"* is set to
      *"true"* (which is default if it is available) and the model
      *`shape_model_3did`* was created with
      *"fast_pose_refinement"* set to *"false"*, the
      projection of the model in the pose refinement step is accelerated
      using the graphics card. Depending on the graphics card this is
      significantly faster than the non accelerated algorithm. Be aware that
      the results of the OpenGL projection are slightly different
      compared to the analytic projection.
      The different modes for least-squares adjustment
      (*"least_squares"*, *"least_squares_high"*, and
      *"least_squares_very_high"*) can be used to determine the
      accuracy with which the minimum distance is searched for. The
      higher the accuracy is chosen, the longer the pose refinement
      will take, however. For most applications
      *"least_squares_high"* should be chosen because this
      results in the best trade-off between runtime and accuracy. Note
      that the pose refinement can be sped up by passing
      *"fast_pose_refinement"* for the parameter
      `gen_param_name` of the operator
      [`create_shape_model_3d`](create_shape_model_3d.md).

      List of values:
       *"none"*, *"least_squares"*,
      *"least_squares_high"*, *"least_squares_very_high"*

      Default:
       *"least_squares_high"*
    - ***"recompute_score"*:** —

      This parameter determines
      whether the score of the matches is recomputed after the pose
      refinement. If *"recompute_score"* is set to
      *"false"*, the score is returned that was computed before
      the pose refinement. In some cases, however, the pose
      refinement changes the object pose by more than one pixel in the
      image. Consequently, the original score does not appropriately
      describe the refined match any longer. This could result in
      wrong matches obtaining high scores or perfect matches obtaining
      low scores. To obtain a more meaningful score that reflects the
      pose changes due to the pose refinement, the score can be
      recomputed after the pose refinement by setting
      *"recompute_score"* to *"true"*. Note that this
      might change the order of the matches as well as the selection
      of matches that is returned. Also note that the recomputation
      of the score values needs additional computation time. This
      increase of the run-time can be reduced by setting the generic
      parameter *"fast_pose_refinement"* of the operator
      [`create_shape_model_3d`](create_shape_model_3d.md) to *"true"*.

      List of values:
       *"false"*, *"true"*

      Default:
       *"false"*
    - ***"outlier_suppression"*:** —

      This parameter only takes effect if *"pose_refinement"*
      is set to a value other than *"none"*, and hence, a
      least-squares adjustment is performed. Then, in some cases it
      might be useful to apply a robust outlier suppression during the
      least-squares adjustment. This might be necessary, for example,
      if a high degree of clutter is present in the image, which
      prevents the least-squares adjustment from finding the optimum
      pose. In this case, *"outlier_suppression"* should be set
      to either *"medium"* (eliminates a medium proportion of
      outliers) or *"high"* (eliminates a high proportion of
      outliers). However, in most applications, no robust outlier
      suppression is necessary, and hence, *"outlier_suppression"*
      can be set to *"none"*. It should be noted that
      activating the outlier suppression comes along with a
      significantly increasing computation time.

      List of values:
       *"none"*, *"medium"*, *"high"*

      Default:
       *"none"*
    - ***"cov_pose_mode"*:** —

      This parameter only
      takes effect if *"pose_refinement"* is set to a value
      other than *"none"*, and hence, a least-squares
      adjustment is performed. *"cov_pose_mode"* determines the
      mode in which the accuracies that are computed during the
      least-squares adjustment are returned in *`cov_pose`*. If
      *"cov_pose_mode"* is set to
      *"standard_deviations"*, the 6 standard deviations of the
      6 pose parameters are returned for each match. In contrast, if
      *"cov_pose_mode"* is set to *"covariances"*,
      *`cov_pose`* contains the 36 values of the complete 6×6
      covariance matrix of the 6 pose parameters.

      List of values:
       *"standard_deviations"*,
      *"covariances"*

      Default:
       *"standard_deviations"*
    - ***"border_model"*:** —

      The model is searched within those points of the domain of the
      image in which the model lies completely within the image.
      This means that the model will not be found if it extends beyond
      the borders of the image, even if it would achieve a score
      greater than *`min_score`*. Note that, if for a certain pyramid
      level the model touches the image border, it might not be found
      even if it lies completely within the original image.
      As a rule of thumb, the model might not be found if its distance to
      an image border falls below $2^{NumLevels-1}$.
      This behavior can be changed by setting *"border_model"* to
      *"true"*, which will
      cause models that extend beyond the image border to be found if
      they achieve a score greater than *`min_score`*. Here,
      points lying outside the image are regarded as being occluded,
      i.e., they lower the score. It should be noted that the runtime
      of the search will increase in this mode. Note further, that in
      rare cases, which occur typically only for artificial images, the
      model might not be found also if for certain pyramid levels the
      model touches the border of the reduced domain. Then, it may help
      to enlarge the reduced domain by
      $2^{NumLevels-1}$ using, e.g.,
      [`dilation_circle`](dilation_circle.md).

      List of values:
       *"false"*, *"true"*

      Default:
       *"false"*

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  (multichannel-)image `→` HObject (byte / uint2)

Input image in which the model should be found.

**`shape_model_3did`** (input_control)  shape_model_3d `→` HHandle

Handle of the 3D shape model.

**`min_score`** (input_control)  real `→` float

Minimum score of the instances of the model to
be found.

Default:
0.7

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

**`num_levels`** (input_control)  integer-array `→` Sequence[int]

Number of pyramid levels used in the matching
(and lowest pyramid level to use if
|*`num_levels`*| = 2).

Default:
0

List of values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

**`gen_param_name`** (input_control)  attribute.name-array `→` Sequence[str]

Names of (optional) parameters for
controlling the behavior of the operator.

Default:
[]

List of values:
"border_model", "cam_roll_max", "cam_roll_min", "cov_pose_mode", "dist_max", "dist_min", "latitude_max", "latitude_min", "longitude_max", "longitude_min", "max_overlap", "num_matches", "outlier_suppression", "pose_refinement", "recompute_score"

**`gen_param_value`** (input_control)  attribute.name-array `→` Sequence[Union[int, float, str]]

Values of the optional generic parameters.

Default:
[]

Suggested values:
-0.78, -0.35, -0.17, 0.0, 0.17, 0.35, 0.78, 0.1, 0.2, 0.5, "none", "false", "true", "least_squares", "least_squares_high", "least_squares_very_high", "standard_deviations", "covariances", "medium", "high"

**`pose`** (output_control)  pose(-array) `→` Sequence[Union[int, float]]

3D pose of the 3D shape model.

**`cov_pose`** (output_control)  real-array `→` Sequence[float]

6 standard deviations or 36 covariances
of the pose parameters.

**`score`** (output_control)  real-array `→` Sequence[float]

Score of the found instances of the 3D shape model.

## Example (HDevelop)

```
read_object_model_3d (DXFModelFileName, 'm', [], [], ObjectModel3D, \
                      DxfStatus)
CamParam := ['area_scan_division',0.01221,2791,7.3958e-6,7.4e-6,\
             308.21,245.92,640,480]
create_shape_model_3d (ObjectModel3D, CamParam, 0, 0, 0, 'gba', \
                       -rad(20), rad(20), -rad(20), rad(20), 0, \
                       rad(360), 0.15, 0.2, 10, [], [], ShapeModel3DID)
grab_image_async (Image, AcqHandle, -1)
find_shape_model_3d (Image, ShapeModel3DID, 0.6, 0.9, 0, [], [], \
                     Pose, CovPose, Score)
project_shape_model_3d (ModelContours, ShapeModel3DID, CamParam, \
                        Pose, 'true', rad(30))
```

## Result

If the parameter values are correct, the operator
`find_shape_model_3d` returns the value 2 (
H_MSG_TRUE)
. If the input is
empty (no input images are available) the behavior can be set via
`set_system('no_object_result',<Result>)`. If necessary, an
exception is raised. If the model was created with
`find_shape_model_3d` by setting *"metric"* to
*"ignore_part_polarity"* and a multi-channel input image is
passed in *`image`*, the error 3359 is raised.

## Possible Predecessors

`create_shape_model_3d`,
`read_shape_model_3d`

## Possible Successors

`project_shape_model_3d`

## See also

`convert_point_3d_cart_to_spher`,
`convert_point_3d_spher_to_cart`,
`create_cam_pose_look_at_point`,
`trans_pose_shape_model_3d`

## Module

3D Metrology
