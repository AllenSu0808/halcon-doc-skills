# find_ncc_models (Operator)

## Name

`find_ncc_models` — Find the best matches of multiple NCC models.

## Signature

`def find_ncc_models(image: HObject, model_ids: MaybeSequence[HHandle], angle_start: MaybeSequence[float], angle_extent: MaybeSequence[float], min_score: MaybeSequence[float], num_matches: MaybeSequence[int], max_overlap: MaybeSequence[float], sub_pixel: MaybeSequence[str], num_levels: MaybeSequence[int]) -> Tuple[Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[int]]`

## Description

The operator `find_ncc_models` finds the best
*`num_matches`* instances of the NCC models that are passed in
the tuple *`model_ids`* in the input *`image`*. The
models must have been created previously by calling
[`create_ncc_model`](create_ncc_model.md) or [`read_ncc_model`](read_ncc_model.md).
In contrast to [`find_ncc_model`](find_ncc_model.md), multiple models can
be searched in the same image in one call.

If NCC finds no suitable match or the matching scores are to low,
the search should be performed using a different matching method
(see, e.g., `“Solution Guide II-B - Matching”`).

### Characteristics of the parameter semantics

Compared to [`find_ncc_model`](find_ncc_model.md), the
semantics of all input parameters have changed to some extent.
All input parameters must either contain one element, in which case the
parameter is used for all models, or they must contain the same number of
elements as *`model_ids`*, in which case each parameter element
refers to the corresponding element in *`model_ids`*.
(*`num_levels`* may also contain either two or twice the number
of elements as *`model_ids`*). More details can be found below
in the sections containing information for the respective parameters.
Note that a call to
`find_ncc_models` with multiple
values for *`model_ids`*, *`num_matches`* and
*`max_overlap`* has the same effect as multiple independent
calls to [`find_ncc_model`](find_ncc_model.md) with the respective parameters.
However, a single call to `find_ncc_models` is considerably
more efficient.

### Input parameters in detail

- ***`image`* and its domain:** —

  The domain of the image *`image`* determines the search space
  for the reference point of the model, i.e., for the center of
  gravity of the domain (region) of the image that was used to create
  the NCC model with [`create_ncc_model`](create_ncc_model.md). A different origin
  set with [`set_ncc_model_origin`](set_ncc_model_origin.md) is not taken into account.
  The model has to lie completely within the image. This means that
  the model will not be found if it extends beyond the borders of the
  image, even if it would achieve a score greater than
  *`min_score`* (see below). Note that rounding effects can cause
  matches to lie up to
  $0.5 * 2^{NumLevels-1}$ ![figure](../assets/d238f8d5c1836b07.svg)
  pixels outside the image.

  The input *`image`*
  can contain a single image object or an image object array
  containing multiple image objects. If *`image`* contains a
  single image object, its domain is used as the region of interest
  for all models in *`model_ids`*. If *`image`* contains
  multiple image objects, each domain is used as the region of
  interest for the corresponding model in *`model_ids`*. In this
  case, the images have to be identical except for their domains,
  i.e., *`image`* cannot be constructed in an
  arbitrary manner using [`concat_obj`](concat_obj.md), but must be created from
  the same image using [`add_channels`](add_channels.md) or equivalent calls. If
  this is not the case, an error message is returned.
- ***`angle_start`* and *`angle_extent`*:** —

  The parameters *`angle_start`* and *`angle_extent`*
  determine the range of rotations for which the model is searched.
  If necessary, the range of rotations is clipped to the range given
  when the model was created with [`create_ncc_model`](create_ncc_model.md).

  Furthermore, it should be noted that in some cases instances with a
  rotation that is slightly outside the specified range of rotations
  are found. This may happen if the specified range of rotations is
  smaller than the range given when the model was created.
- ***`min_score`*:** —

  The parameter *`min_score`* determines what score a potential
  match must at least have to be regarded as an instance of the model
  in the image. The larger *`min_score`* is chosen, the faster
  the search is. If the model can be expected never to be occluded in
  the images, *`min_score`* may be set as high as 0.8 or even 0.9.
  If the matches are not tracked to the lowest pyramid level (see
  *`num_levels`*), it might happen that instances with a score
  slightly below *`min_score`* are found.
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

  If *`num_matches`*
  contains one element, `find_ncc_models` returns the best
  *`num_matches`* instances of the model irrespective of the type
  of the model. If, for example, two models are passed in
  *`model_ids`* and *`num_matches`* = 2 is selected, it can
  happen that two instances of the first model and no instances of the
  second model, one instance of the first model and one instance of
  the second model, or no instances of the first model and two
  instances of the second model are returned. If, on the other hand,
  *`num_matches`* contains multiple values, the number of
  instances returned of the different models corresponds to the number
  specified in the respective entry in *`num_matches`*. If, for
  example, *`num_matches`* = [1,1] is selected, one instance of
  the first model and one instance of the second model is returned.
- ***`max_overlap`*:** —

  If the model exhibits symmetries it may happen that multiple
  instances with similar positions but different rotations are found
  in the image. The parameter *`max_overlap`* determines by what
  fraction (i.e., a number between 0 and 1) two instances may at most
  overlap in order to consider them as different instances, and hence
  to be returned separately. If two instances overlap each other by
  more than *`max_overlap`*, only the best instance is returned.
  The calculation of the overlap is based on the smallest enclosing
  rectangle of arbitrary orientation (see [`smallest_rectangle2`](smallest_rectangle2.md))
  of the found instances. If *`max_overlap`*=0, the found
  instances may not overlap at all, while for *`max_overlap`*=1
  all instances are returned.

  If a single value is passed in
  *`max_overlap`*, the overlap is computed for all found instances
  of the different models, irrespective of the model type, i.e.,
  instances of the same or of different models that overlap too much
  are eliminated. If, on the other hand, multiple values are passed
  in *`max_overlap`*, the overlap is only computed for found
  instances of the model that have the same model type, i.e., only
  instances of the same model that overlap too much are eliminated.
  In this mode, models of different types may overlap completely.
- ***`sub_pixel`*:** —

  The parameter *`sub_pixel`* determines whether the instances
  should be extracted with subpixel accuracy. If *`sub_pixel`* is
  set to *"false"* the model's pose is only determined with pixel
  accuracy and the angle resolution that was specified with
  [`create_ncc_model`](create_ncc_model.md). If *`sub_pixel`* is set to
  *"true"*, the position as well as the rotation are determined with
  subpixel accuracy. In this mode, the model's pose is interpolated from
  the score function.
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
  `find_ncc_models`. This approach is often better regarding the speed
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
  level. If the lowest pyramid level to use is chosen too large, it may
  happen that the desired accuracy cannot be achieved, or that wrong instances
  of the model are found because the model is not specific enough on the
  higher pyramid levels to facilitate a reliable selection of the
  correct instance of the model. In this case, the lowest pyramid
  level to use must be set to a smaller value.

  If the lowest pyramid
  level is specified separately for each model, *`num_levels`*
  must contain twice the number of elements as *`model_ids`*. In
  this case, the number of pyramid levels and the lowest pyramid level
  must be specified interleaved in *`num_levels`*. If, for
  example, two models are specified in *`model_ids`*, the number
  of pyramid levels is 5 for the first model and 4 for the second
  model, and the lowest pyramid level is 2 for the first model and 1
  for the second model, *`num_levels`* = *[5,2,4,1]* must
  be selected. If exactly two models are specified in
  *`model_ids`*, a special case occurs. If in this case the
  lowest pyramid level is to be specified, the number of pyramid
  levels and the lowest pyramid level must be specified explicitly for
  both models, even if they are identical, because specifying two
  values in *`num_levels`* is interpreted as the explicit
  specification of the number of pyramid levels for the two models.

### Output parameters in detail

- ***`row`*, *`column`* and *`angle`*:** —

  The position and rotation of the found instances of the model is
  returned in *`row`*, *`column`*, and *`angle`*. The
  coordinates *`row`* and *`column`* are the coordinates of
  the origin of the NCC model in the search image. By default, the
  origin is the center of gravity of the domain (region) of the image
  that was used to create the NCC model with
  [`create_ncc_model`](create_ncc_model.md). A different origin can be set with
  [`set_ncc_model_origin`](set_ncc_model_origin.md).

  Note that the coordinates *`row`* and *`column`* do not
  exactly correspond to the position of the model in the search
  image. Thus, you cannot directly use them. Instead, the values are
  optimized for creating the transformation matrix with which you can
  use the results of the matching for various tasks, e.g., to align
  ROIs for other processing steps. The example given for
  [`find_ncc_model`](find_ncc_model.md) shows how to create this matrix and use it
  to display the model at the found position in the search image and
  to calculate the exact coordinates.

  Note also that for visualizing the model at the found position, also
  the procedure `dev_display_ncc_matching_results` can be used.
- ***`score`*:** —

  Additionally, the score of each found instance is returned in
  *`score`*.
- ***`model`*:** —

  The type of the found instances of the models is returned in
  *`model`*. The elements of *`model`* are indices into the
  tuple *`model_ids`*, i.e., they can contain values from 0 to
  |*`model_ids`*|-1. Hence, a value of 0 in an element of
  *`model`* corresponds to an instance of the first model in
  *`model_ids`*.

### Specifying a timeout

Using the operator [`set_ncc_model_param`](set_ncc_model_param.md) you can specify a
*"timeout"* for `find_ncc_models`. If the NCC models
referenced by *`model_ids`* hold different values for *"timeout"*,
`find_ncc_models` uses the smallest one.
If `find_ncc_models` reaches this *"timeout"*, it terminates
without results and returns the error code 9400 (H_ERR_TIMEOUT).

### Visualization of the results

To display the results found by correlation-based matching, we highly
recommend the usage of the procedure
`dev_display_ncc_matching_results`.

### Further Information

For an explanation of the different 2D coordinate systems
used in HALCON, see the introduction of chapter
[Transformations / 2D Transformations](toc_transformations_2dtransformations.md).

## Attention

Note that the internally used memory increases with
the number of used threads.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte* / uint2*) **allowed for compute devices*

Input image in which the model should be found.

**`model_ids`** (input_control)  ncc_model(-array) `→` MaybeSequence[HHandle]

Handle of the models.

**`angle_start`** (input_control)  angle.rad(-array) `→` MaybeSequence[float]

Smallest rotation of the models.

Default:
-0.39

Suggested values:
-3.14, -1.57, -0.79, -0.39, -0.20, 0.0

**`angle_extent`** (input_control)  angle.rad(-array) `→` MaybeSequence[float]

Extent of the rotation angles.

Default:
0.79

Suggested values:
6.29, 3.14, 1.57, 0.79, 0.39, 0.0

Restriction:
`AngleExtent >= 0`

**`min_score`** (input_control)  real(-array) `→` MaybeSequence[float]

Minimum score of the instances of the models to
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

**`num_matches`** (input_control)  integer(-array) `→` MaybeSequence[int]

Number of instances of the models to be found
(or 0 for all matches).

Default:
1

Suggested values:
0, 1, 2, 3, 4, 5, 10, 20

**`max_overlap`** (input_control)  real(-array) `→` MaybeSequence[float]

Maximum overlap of the instances of the models
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

Row coordinate of the found instances of the models.

**`column`** (output_control)  point.x-array `→` Sequence[float]

Column coordinate of the found instances of the models.

**`angle`** (output_control)  angle.rad-array `→` Sequence[float]

Rotation angle of the found instances of the models.

**`score`** (output_control)  real-array `→` Sequence[float]

Score of the found instances of the models.

**`model`** (output_control)  integer-array `→` Sequence[int]

Index of the found instances of the models.

## Example (HDevelop)

```
read_image (Image, 'pcb_focus/pcb_focus_telecentric_061')
gen_rectangle1 (ROI_0, 236, 241, 313, 321)
gen_circle (ROI_1, 281, 653, 41)
reduce_domain (Image, ROI_0, ImageReduced1)
reduce_domain (Image, ROI_1, ImageReduced2)
create_ncc_model (ImageReduced1, 'auto', rad(-45), rad(90), 'auto', \
                  'use_polarity', ModelID1)
create_ncc_model (ImageReduced2, 'auto', rad(-45), rad(90), 'auto', \
                  'use_polarity', ModelID2)
ModelIDs:=[ModelID1, ModelID2]
find_ncc_models (Image, ModelIDs, rad(-45), rad(90), 0.7, [1,1], 0.5, \
                 'true', 0, Row, Column, Angle, Score, Model)
dev_display_ncc_matching_results (ModelIDs, 'red', Row, Column, \
                                  Angle, Model)
```

## Result

If the parameter values are correct, the operator
`find_ncc_models` returns the value 2 (
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
