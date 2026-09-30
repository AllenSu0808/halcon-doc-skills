# find_local_deformable_model (Operator)

## Name

`find_local_deformable_model` — Find the best matches of a local deformable model in an image.

## Signature

`def find_local_deformable_model(image: HObject, model_id: HHandle, angle_start: float, angle_extent: float, scale_rmin: float, scale_rmax: float, scale_cmin: float, scale_cmax: float, min_score: float, num_matches: int, max_overlap: float, num_levels: int, greediness: float, result_type: Sequence[str], gen_param_name: Sequence[str], gen_param_value: Sequence[Union[int, float, str]]) -> Tuple[HObject, HObject, HObject, Sequence[float], Sequence[float], Sequence[float]]`

## Description

The operator `find_local_deformable_model` finds the best
*`num_matches`* instances of the locally deformable
model *`model_id`* in the input *`image`*. The model must have been
created previously by calling [`create_local_deformable_model`](create_local_deformable_model.md) or
[`read_deformable_model`](read_deformable_model.md).

The model is searched within those points of the domain of the
image in which the model lies completely within the image.
This means that the model will not be found if it extends beyond
the borders of the image, even if it would achieve a score
greater than *`min_score`*. Note that, if for a certain pyramid
level the model touches the image border, it might not be found
even if it lies completely within the original image.
As a rule of thumb, the model might not be found if its distance to
an image border falls below $2^{NumLevels-1}$.
This behavior can be changed with
`set_system('border_shape_models','true')`, which will cause
models that extend beyond the image border to be found if they
achieve a score greater than *`min_score`*. Here, points lying
outside the image are regarded as being occluded, i.e., they lower
the score. It should be noted that the runtime of the search will
increase in this mode.
Note further, that in rare cases, which occur typically only for
artificial images, the model might not be found also if for certain
pyramid levels them model touches the border of the reduced domain.
Then, it may help to enlarge the reduced domain by
$2^{NumLevels-1}$ using, e.g.,
[`dilation_circle`](dilation_circle.md).

The operator
`find_local_deformable_model` returns the *`row`* and
*`column`* coordinates of the found instances.
Additionally, a rectified part of the image, the respective vector field, and
the contours of the found deformed model instance can be returned in
*`image_rectified`*, *`vector_field`*, and *`deformed_contours`*.
By default, these iconic objects are not returned. In case they are
needed the parameter *`result_type`* should be set to
*"image_rectified"*, *"vector_field"* or
*"deformed_contours"*.
The size of *`image_rectified`* and *`vector_field`* is the smallest
axis-aligned rectangle of the domain of the image that was used to create
the local deformable model with [`create_local_deformable_model`](create_local_deformable_model.md).
The size of the rectified image and the vector field can be expanded in all
directions by setting *`gen_param_name`* to *"expand_border"* and the
respective *`gen_param_value`* to the number of pixels. Optionally, a
specific direction can be selected with *"expand_border_top"*,
*"expand_border_bottom"*, *"expand_border_left"*, or
*"expand_border_right"*.
Please note that the returned *`vector_field`* is in absolute coordinates
and can be used for [`convert_map_type`](convert_map_type.md).

The smoothness of the estimated deformation can be selected with
*`gen_param_name`* set to *"deformation_smoothness"*. The value for
*"deformation_smoothness"* can be imagined as the size of a smoothing
filter to the estimated deformation field. A too small value expects
a strong deformation a too big value expects a rigid object. The
minimal value for *"deformation_smoothness"* is *3*,
a typical value is *11*, and the value can be increased further for
only small global deformations.

Finally, the score of each found instance is returned in *`score`*.
The score is a number between 0 and 1, which is an approximate measure of how
much of the model is visible in the image.

For further explanation on the parameters used for the search of a local
deformable model we refer to the description of
[`find_planar_uncalib_deformable_model`](find_planar_uncalib_deformable_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  (multichannel-)image `→` HObject (byte / uint2)

Input image in which the model should be found.

**`image_rectified`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / uint2)

Rectified image of the found model.

**`vector_field`** (output_object)  singlechannelimage(-array) `→` HObject (vector_field)

Vector field of the rectification transformation.

**`deformed_contours`** (output_object)  xld_cont-array `→` HObject

Contours of the found instances of the model.

**`model_id`** (input_control)  deformable_model `→` HHandle

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

**`scale_rmin`** (input_control)  number `→` float

Minimum scale of the model in row direction.

Default:
1.0

Suggested values:
0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Restriction:
`ScaleRMin > 0`

**`scale_rmax`** (input_control)  number `→` float

Maximum scale of the model in row direction.

Default:
1.0

Suggested values:
1.0, 1.1, 1.2, 1.3, 1.4, 1.5

Restriction:
`ScaleRMax >= ScaleRMin`

**`scale_cmin`** (input_control)  number `→` float

Minimum scale of the model in column direction.

Default:
1.0

Suggested values:
0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Restriction:
`ScaleCMin > 0`

**`scale_cmax`** (input_control)  number `→` float

Maximum scale of the model in column direction.

Default:
1.0

Suggested values:
1.0, 1.1, 1.2, 1.3, 1.4, 1.5

Restriction:
`ScaleCMax >= ScaleCMin`

**`min_score`** (input_control)  real `→` float

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
1.0

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

**`num_levels`** (input_control)  integer `→` int

Number of pyramid levels used in the matching.

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

**`result_type`** (input_control)  string-array `→` Sequence[str]

Switch for requested iconic result.

Default:
[]

List of values:
[], "deformed_contours", "image_rectified", "vector_field"

**`gen_param_name`** (input_control)  string-array `→` Sequence[str]

The general parameter names.

Default:
[]

List of values:
[], "angle_step", "deformation_smoothness", "expand_border", "expand_border_bottom", "expand_border_left", "expand_border_right", "expand_border_top", "scale_c_step", "scale_r_step", "subpixel"

**`gen_param_value`** (input_control)  integer-array `→` Sequence[Union[int, float, str]]

Values of the general parameters.

Default:
[]

List of values:
[], "least_squares", "least_squares_high", "least_squares_very_high", "none"

**`score`** (output_control)  real-array `→` Sequence[float]

Scores of the found instances of the model.

**`row`** (output_control)  real-array `→` Sequence[float]

Row coordinates of the found instances of the model.

**`column`** (output_control)  real-array `→` Sequence[float]

Column coordinates of the found instances of the model.

## Result

If the parameters are valid, the operator
`find_local_deformable_model` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`create_local_deformable_model`,
`create_local_deformable_model_xld`,
`read_deformable_model`

## Module

Matching
