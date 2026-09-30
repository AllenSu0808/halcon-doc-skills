# find_planar_calib_deformable_model (Operator)

## Name

`find_planar_calib_deformable_model` — Find the best matches of a calibrated deformable model in an image and return
their 3D pose.

## Signature

`find_planar_calib_deformable_model(Image : : ModelID, AngleStart, AngleExtent, ScaleRMin, ScaleRMax, ScaleCMin, ScaleCMax, MinScore, NumMatches, MaxOverlap, NumLevels, Greediness, GenParamName, GenParamValue : Pose, CovPose, Score)`

## Description

The operator `find_planar_calib_deformable_model` finds the best
*`NumMatches`* instances of the calibrated deformable
model *`ModelID`* in the input image *`Image`*. The
model must have been created previously by calling
[`create_planar_calib_deformable_model`](create_planar_calib_deformable_model.md) or
[`read_deformable_model`](read_deformable_model.md). There is no need to
correct any distortions in *`Image`* as the calibration data has
already been provided during the model creation. The operator
`find_planar_calib_deformable_model` returns the 3D *`Pose`* of
the found instances in the camera coordinate system.

Additionally, the accuracy of the six pose parameters are returned in
*`CovPose`*. By default, *`CovPose`* contains the 6 standard
deviations of the pose parameters for each match. If the
generic parameter *'cov_pose_mode'* was set to
*'covariances'*, *`CovPose`* contains the 36 values of
the complete 6x6 covariance matrix of the 6
pose parameters. Note that this reflects only an inner accuracy from
which the real accuracy of the pose may differ. Finally, the score
of each found instance is returned in *`Score`*. The score is
a number between 0 and 1, which is an approximate measure of how
much of the model is visible in the image.

For further explanation on the planar deformable model and its parameters we
refer to the description of [`find_planar_uncalib_deformable_model`](find_planar_uncalib_deformable_model.md).

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
-3.14, -1.57, -0.78, -0.39, -0.20, 0.0

**`AngleExtent`** (input_control)  angle.rad `→`  (real)

Extent of the rotation angles.

Default:
0.78

Suggested values:
6.29, 3.14, 1.57, 0.78, 0.39, 0.0

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
[], 'angle_change_restriction', 'angle_step', 'aniso_scale_change_restriction', 'cov_pose_mode', 'scale_c_step', 'scale_r_step', 'subpixel'

**`GenParamValue`** (input_control)  integer-array `→`  (integer / real / string)

Values of the general parameters.

Default:
[]

List of values:
[], 'covariances', 'least_squares', 'least_squares_high', 'least_squares_very_high', 'standard_deviations'

**`Pose`** (output_control)  pose(-array) `→`  (real / integer)

Pose of the object.

**`CovPose`** (output_control)  real-array `→`  (real)

6 standard deviations or 36 covariances
of the pose parameters.

**`Score`** (output_control)  real-array `→`  (real)

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
