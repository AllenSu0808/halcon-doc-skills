# find_planar_calib_deformable_model (Operator)

## Name

`find_planar_calib_deformable_model` — Find the best matches of a calibrated deformable model in an image and return
their 3D pose.

## Signature

`def find_planar_calib_deformable_model(image: HObject, model_id: HHandle, angle_start: float, angle_extent: float, scale_rmin: float, scale_rmax: float, scale_cmin: float, scale_cmax: float, min_score: float, num_matches: int, max_overlap: float, num_levels: MaybeSequence[int], greediness: float, gen_param_name: Sequence[str], gen_param_value: Sequence[Union[int, float, str]]) -> Tuple[Sequence[Union[float, int]], Sequence[float], Sequence[float]]`

## Description

The operator `find_planar_calib_deformable_model` finds the best
*`num_matches`* instances of the calibrated deformable
model *`model_id`* in the input image *`image`*. The
model must have been created previously by calling
[`create_planar_calib_deformable_model`](create_planar_calib_deformable_model.md) or
[`read_deformable_model`](read_deformable_model.md). There is no need to
correct any distortions in *`image`* as the calibration data has
already been provided during the model creation. The operator
`find_planar_calib_deformable_model` returns the 3D *`pose`* of
the found instances in the camera coordinate system.

Additionally, the accuracy of the six pose parameters are returned in
*`cov_pose`*. By default, *`cov_pose`* contains the 6 standard
deviations of the pose parameters for each match. If the
generic parameter *"cov_pose_mode"* was set to
*"covariances"*, *`cov_pose`* contains the 36 values of
the complete 6x6 covariance matrix of the 6
pose parameters. Note that this reflects only an inner accuracy from
which the real accuracy of the pose may differ. Finally, the score
of each found instance is returned in *`score`*. The score is
a number between 0 and 1, which is an approximate measure of how
much of the model is visible in the image.

For further explanation on the planar deformable model and its parameters we
refer to the description of [`find_planar_uncalib_deformable_model`](find_planar_uncalib_deformable_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  (multichannel-)image `→` HObject (byte / uint2)

Input image in which the model should be found.

**`model_id`** (input_control)  deformable_model `→` HHandle

Handle of the model.

**`angle_start`** (input_control)  angle.rad `→` float

Smallest rotation of the model.

Default:
-0.39

Suggested values:
-3.14, -1.57, -0.78, -0.39, -0.20, 0.0

**`angle_extent`** (input_control)  angle.rad `→` float

Extent of the rotation angles.

Default:
0.78

Suggested values:
6.29, 3.14, 1.57, 0.78, 0.39, 0.0

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

**`gen_param_name`** (input_control)  string-array `→` Sequence[str]

The general parameter names.

Default:
[]

List of values:
[], "angle_change_restriction", "angle_step", "aniso_scale_change_restriction", "cov_pose_mode", "scale_c_step", "scale_r_step", "subpixel"

**`gen_param_value`** (input_control)  integer-array `→` Sequence[Union[int, float, str]]

Values of the general parameters.

Default:
[]

List of values:
[], "covariances", "least_squares", "least_squares_high", "least_squares_very_high", "standard_deviations"

**`pose`** (output_control)  pose(-array) `→` Sequence[Union[float, int]]

Pose of the object.

**`cov_pose`** (output_control)  real-array `→` Sequence[float]

6 standard deviations or 36 covariances
of the pose parameters.

**`score`** (output_control)  real-array `→` Sequence[float]

Score of the found instances of the model.

## Result

If the parameters are valid, the operator
`find_planar_calib_deformable_model` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`create_planar_calib_deformable_model`,
`read_deformable_model`

## Module

Matching
