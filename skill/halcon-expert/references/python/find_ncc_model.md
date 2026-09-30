# find_ncc_model (Operator)

## Name

`find_ncc_model` — Find the best matches of an NCC model in an image.

## Signature

`def find_ncc_model(image: HObject, model_id: HHandle, angle_start: float, angle_extent: float, min_score: float, num_matches: int, max_overlap: float, sub_pixel: str, num_levels: MaybeSequence[int]) -> Tuple[Sequence[float], Sequence[float], Sequence[float], Sequence[float]]`

## Description

The operator `find_ncc_model` finds the best
*`num_matches`* instances of the NCC model *`model_id`* in
the input image *`image`*. The model must have been created
previously by calling [`create_ncc_model`](create_ncc_model.md) or
[`read_ncc_model`](read_ncc_model.md).

The position and rotation of the found instances of the model is
returned in *`row`*, *`column`*, and *`angle`*.
Additionally, the score of each found instance is returned in
*`score`*.

If NCC finds no suitable match or the matching scores are to low,
the search should be performed using a different matching method
(see, e.g., `“Solution Guide II-B - Matching”`).

### Input parameters in detail

- ***`image`* and its domain:** —

  The domain of the image *`image`* determines the search space
  for the reference point of the model, i.e., for the center of
  gravity of the domain (region) of the image that was used to create
  the NCC model with [`create_ncc_model`](create_ncc_model.md). A different origin
  set with [`set_ncc_model_origin`](set_ncc_model_origin.md) is not taken into account
  here. The model is searched within those points of the domain of
  the image, in which the model lies completely within the image.
  This means that the model will not be found if it extends beyond the
  borders of the image, even if it would achieve a score greater than
  *`min_score`* (see below). Note that rounding effects can cause
  matches to lie up to
  $0.5 * 2^{NumLevels-1}$ ![figure](../assets/d238f8d5c1836b07.svg)
  pixels outside the image.
- ***`angle_start`* and *`angle_extent`*:** —

  The parameters *`angle_start`* and *`angle_extent`*
  determine the range of rotations for which the model is searched.
  If necessary, the range of rotations is clipped to the range given
  when the model was created with [`create_ncc_model`](create_ncc_model.md).
- ***`min_score`*:** —

  The parameter *`min_score`* determines what score a potential
  match must at least have to be regarded as an instance of the model
  in the image. The larger *`min_score`* is chosen, the faster
  the search is.
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
- ***`max_overlap`*:** —

  If the model exhibits symmetries it may happen that multiple
  instances with similar positions but different rotations are found
  in the image. If the model has repeating structures it may happen
  that multiple instances with identical rotations are found at
  similar positions in the image. The parameter *`max_overlap`*
  determines by what fraction (i.e., a number between 0 and 1) two
  instances may at most overlap in order to consider them as different
  instances, and hence to be returned separately. If two instances
  overlap each other by more than *`max_overlap`* only the best
  instance is returned. The calculation of the overlap is based on
  the smallest enclosing rectangle of arbitrary orientation (see
  [`smallest_rectangle2`](smallest_rectangle2.md)) of the found instances. If
  *`max_overlap`*=0, the found instances may not overlap at all,
  while for *`max_overlap`*=1 all instances are returned.
- ***`sub_pixel`*:** —

  The parameter *`sub_pixel`* determines whether the instances
  should be extracted with subpixel accuracy. If *`sub_pixel`* is
  set to *"false"*, the model's pose is only determined with
  pixel accuracy and the angle resolution that was specified with
  [`create_ncc_model`](create_ncc_model.md). If *`sub_pixel`* is set to
  *"true"*, the position as well as the rotation are determined
  with subpixel accuracy. In this mode, the model's pose is
  interpolated from the score function. This mode costs almost no
  computation time and achieves a high accuracy. Hence,
  *`sub_pixel`* should usually be set to *"true"*.
  Note that the subpixel accurate determination of the model's pose is
  only possible if the found instance lies at least 2 pixels away from
  the image border of the lowest used pyramid level. If the instance
  lies closer to the image border, its pose is only determined with
  pixel accuracy and the angle resolution that was specified with
  [`create_ncc_model`](create_ncc_model.md), even if *`sub_pixel`* is set to
  *"true"*.
- ***`num_levels`*:** —

  The number of pyramid levels used during the search is determined
  with *`num_levels`*. If necessary, the number of levels is
  clipped to the range given when the NCC model was created with
  [`create_ncc_model`](create_ncc_model.md). If *`num_levels`* is set to
  *0*, the number of pyramid levels specified in
  [`create_ncc_model`](create_ncc_model.md) is used.

  In certain cases, the number of pyramid levels that was determined
  automatically with, for example, [`create_ncc_model`](create_ncc_model.md) may be too high.
  The consequence may be that some matches that may have a high final score
  are rejected on the highest pyramid level and thus are not found. Instead
  of setting *`min_score`* to a very low value to find all matches, it
  may be better to query the value of *`num_levels`* with
  [`get_ncc_model_params`](get_ncc_model_params.md) and then use a slightly lower value in
  `find_ncc_model`. This approach is often better regarding the speed
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
  level. If the lowest pyramid level to use is chosen too large, it
  may happen that the desired accuracy cannot be achieved, or that
  wrong instances of the model are found because the model is not
  specific enough on the higher pyramid levels to facilitate a
  reliable selection of the correct instance of the model. In this
  case, the lowest pyramid level to use must be set to a smaller
  value.

### Output parameters in detail

- ***`row`*, *`column`* and *`angle`*:** —

  The position and rotation of the found instances of the model is
  returned in *`row`*, *`column`*, and *`angle`*.
  The coordinates *`row`* and *`column`* are related to the
  position of the origin of the model in the search image. However,
  *`row`* and *`column`* do not exactly correspond to this
  position. Instead, `find_ncc_model` returns slightly modified
  values that are optimized for creating a transformation matrix, that
  can be used for alignment or visualization of the model. (This has to
  do with the way HALCON transforms iconic objects, see
  [`affine_trans_pixel`](affine_trans_pixel.md)). The example below shows how to create
  the transformation matrix for alignment and how to calculate the exact
  coordinates of the found matches.

  By default, the origin is the center of gravity of the domain (region)
  of the image that was used to create the NCC model with
  [`create_ncc_model`](create_ncc_model.md). A different origin can be set with
  [`set_ncc_model_origin`](set_ncc_model_origin.md).
- ***`score`*:** —

  Additionally, the score of each found instance is returned in
  *`score`*. The score is the normalized cross correlation of
  the template t(r,c) and the image i(r,c):
  $$ncc(r,c)=\frac{1}{n}\sum_{(u,v)\in R} \frac{t(u,v)-m_t}{\sqrt{s_t^2}} \cdot \frac{i(r+u,c+v)-m_i(r,c)}{\sqrt{s_i^2(r,c)}}$$ ![figure](../assets/1831fdd1a9d73c0a.svg)
  Here, n denotes the number of points in the template, R denotes
  the domain (ROI) of the template, $m_{t}$ is the mean gray
  value of the template
  $$m_t = \frac{1}{n} \sum_{(u,v) \in R} t(u,v)$$ ![figure](../assets/d173e3e8257aedf8.svg)
  $s_{t}^{2}$ is the variance of the gray values of the
  template
  $$s_t^{2} = \frac{1}{n} \sum_{(u,v) \in R} (t(u,v) - m_t)^{2}$$ ![figure](../assets/0f4befeb39235212.svg)
  $m_{i}(r,c)$ is the mean gray value of the image at
  position (r,c) over all points of the template (i.e., the template
  points are shifted by (r,c))
  $$m_i(r,c) = \frac{1}{n} \sum_{(u,v) \in R} i(r + u, c + v)$$ ![figure](../assets/3b6b88c1acc18527.svg)
  and $s_{i}^{2}(r,c)$ is the variance of the gray
  values of the image at position (r,c) over all points of the
  template
  $$s_i^{2}(r,c) = \frac{1}{n} \sum_{(u,v) \in R} (i(r+u,c+v) - m_i(r,c))^{2}$$ ![figure](../assets/5f0ce74793c1ae3a.svg)

  The NCC measures how well the template and image correspond at a
  particular point (r,c). It assumes values between -1 and 1.
  The larger the absolute value of the correlation, the larger the
  degree of correspondence between the template and image. A value of
  1 means that the gray values in the image are a linear
  transformation of the gray values in the template:
  i(r+u,c+v) = a * t(u,v) + b
  where a > 0. Similarly, a value of -1 means that the gray
  values in the image are a linear transformation of the gray values
  in the template with a < 0. Hence, in this case the template
  occurs with a reversed polarity in the image. Because of the above
  property, the NCC is invariant to linear illumination changes.

  The NCC as defined above is used if the NCC model has been created
  with `metric` = *"use_polarity"*. If the model has
  been created with `metric` =
  *"ignore_global_polarity"*, the absolute value of
  ncc(r,c) is used as the score.

### Specifying a timeout

Using the operator [`set_ncc_model_param`](set_ncc_model_param.md) you can specify a
*"timeout"* for `find_ncc_model`. If `find_ncc_model`
reaches this *"timeout"*, it terminates without results and
returns the error code 9400 (H_ERR_TIMEOUT).

### Visualization of the results

To display the results found by correlation-based matching, we highly
recommend the usage of the procedure
`dev_display_ncc_matching_results`.

### Further Information

For an explanation of the different 2D coordinate systems
used in HALCON, see the introduction of chapter
[Transformations / 2D Transformations](toc_transformations_2dtransformations.md).

## Attention

`find_ncc_model` can be partially executed on OpenCL devices that
support the cl_khr_global_int32_base_atomics OpenCL extension. Only the
initial search for the model in the topmost pyramid level is done on the
OpenCL device, while the tracking of matches is done on the host CPU. If the
domain of the image to search in is substantially smaller than the size of
the image, use [`crop_domain`](crop_domain.md) to reduce the amount of data that needs to
be copied from the OpenCL device to the host CPU. Note that
`find_ncc_model` using OpenCL may run either substantially faster or
slower depending on a wide number of factors, so the only way to tell if
using OpenCL is beneficial is by testing with images from the actual
application.

Furthermore, note that the internally used memory increases with
the number of used threads.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  singlechannelimage `→` HObject (byte* / uint2*) **allowed for compute devices*

Input image in which the model should be found.

**`model_id`** (input_control)  ncc_model `→` HHandle

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

**`min_score`** (input_control)  real `→` float

Minimum score of the instances of the model to
be found.

Default:
0.8

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

**`sub_pixel`** (input_control)  string `→` str

Subpixel accuracy.

Default:
"true"

List of values:
"false", "true"

**`num_levels`** (input_control)  integer(-array) `→` MaybeSequence[int]

Number of pyramid levels used in the matching
(and lowest pyramid level to use if
|*`num_levels`*| = 2).

Default:
0

List of values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

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
create_ncc_model (TemplateImage, 'auto', rad(-45), rad(90), 'auto', \
                  'use_polarity', ModelID)
find_ncc_model (SearchImage, ModelID, rad(-45), rad(90), 0.7, 1, \
                0.5, 'true', 0, Row, Column, Angle, Score)
* Create transformation matrix
vector_angle_to_rigid (0, 0, 0, Row, Column, Angle, HomMat2D)
* Calculate true position of the model origin in the search image
affine_trans_pixel (HomMat2D, 0, 0, RowObject, ColumnObject)
* display the results
dev_display_ncc_matching_results (ModelID, 'red', Row, Column, \
                                  Angle, 0)
```

## Result

If the parameter values are correct, the operator
`find_ncc_model` returns the value 2 (
H_MSG_TRUE)
. If the input is
empty (no input images are available) the behavior can be set via
`set_system('no_object_result',<Result>)`. If necessary, an
exception is raised.

## Possible Predecessors

`create_ncc_model`,
`read_ncc_model`,
`set_ncc_model_origin`

## Possible Successors

`clear_ncc_model`

## Alternatives

`find_generic_shape_model`

## Module

Matching
