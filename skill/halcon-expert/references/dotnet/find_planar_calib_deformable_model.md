# FindPlanarCalibDeformableModel (Operator)

## Name

`FindPlanarCalibDeformableModel` — Find the best matches of a calibrated deformable model in an image and return
their 3D pose.

## Signature

`static void HOperatorSet.FindPlanarCalibDeformableModel(HObject image, HTuple modelID, HTuple angleStart, HTuple angleExtent, HTuple scaleRMin, HTuple scaleRMax, HTuple scaleCMin, HTuple scaleCMax, HTuple minScore, HTuple numMatches, HTuple maxOverlap, HTuple numLevels, HTuple greediness, HTuple genParamName, HTuple genParamValue, out HTuple pose, out HTuple covPose, out HTuple score)`

`HPose[] HDeformableModel.FindPlanarCalibDeformableModel(HImage image, double angleStart, double angleExtent, double scaleRMin, double scaleRMax, double scaleCMin, double scaleCMax, double minScore, int numMatches, double maxOverlap, HTuple numLevels, double greediness, HTuple genParamName, HTuple genParamValue, out HTuple covPose, out HTuple score)`

`HPose HDeformableModel.FindPlanarCalibDeformableModel(HImage image, double angleStart, double angleExtent, double scaleRMin, double scaleRMax, double scaleCMin, double scaleCMax, double minScore, int numMatches, double maxOverlap, int numLevels, double greediness, HTuple genParamName, HTuple genParamValue, out HTuple covPose, out HTuple score)`

`HPose[] HImage.FindPlanarCalibDeformableModel(HDeformableModel modelID, double angleStart, double angleExtent, double scaleRMin, double scaleRMax, double scaleCMin, double scaleCMax, double minScore, int numMatches, double maxOverlap, HTuple numLevels, double greediness, HTuple genParamName, HTuple genParamValue, out HTuple covPose, out HTuple score)`

`HPose HImage.FindPlanarCalibDeformableModel(HDeformableModel modelID, double angleStart, double angleExtent, double scaleRMin, double scaleRMax, double scaleCMin, double scaleCMax, double minScore, int numMatches, double maxOverlap, int numLevels, double greediness, HTuple genParamName, HTuple genParamValue, out HTuple covPose, out HTuple score)`

## Description

The operator `FindPlanarCalibDeformableModel` finds the best
*`numMatches`* instances of the calibrated deformable
model *`modelID`* in the input image *`image`*. The
model must have been created previously by calling
[`CreatePlanarCalibDeformableModel`](create_planar_calib_deformable_model.md) or
[`ReadDeformableModel`](read_deformable_model.md). There is no need to
correct any distortions in *`image`* as the calibration data has
already been provided during the model creation. The operator
`FindPlanarCalibDeformableModel` returns the 3D *`pose`* of
the found instances in the camera coordinate system.

Additionally, the accuracy of the six pose parameters are returned in
*`covPose`*. By default, *`covPose`* contains the 6 standard
deviations of the pose parameters for each match. If the
generic parameter *"cov_pose_mode"* was set to
*"covariances"*, *`covPose`* contains the 36 values of
the complete 6x6 covariance matrix of the 6
pose parameters. Note that this reflects only an inner accuracy from
which the real accuracy of the pose may differ. Finally, the score
of each found instance is returned in *`score`*. The score is
a number between 0 and 1, which is an approximate measure of how
much of the model is visible in the image.

For further explanation on the planar deformable model and its parameters we
refer to the description of [`FindPlanarUncalibDeformableModel`](find_planar_uncalib_deformable_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / uint2)

Input image in which the model should be found.

**`modelID`** (input_control)  deformable_model `→` [HDeformableModel](HDeformableModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

**`angleStart`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Smallest rotation of the model.

Default:
-0.39

Suggested values:
-3.14, -1.57, -0.78, -0.39, -0.20, 0.0

**`angleExtent`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Extent of the rotation angles.

Default:
0.78

Suggested values:
6.29, 3.14, 1.57, 0.78, 0.39, 0.0

Restriction:
`AngleExtent >= 0`

**`scaleRMin`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Minimum scale of the model in row direction.

Default:
1.0

Suggested values:
0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Restriction:
`ScaleRMin > 0`

**`scaleRMax`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Maximum scale of the model in row direction.

Default:
1.0

Suggested values:
1.0, 1.1, 1.2, 1.3, 1.4, 1.5

Restriction:
`ScaleRMax >= ScaleRMin`

**`scaleCMin`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Minimum scale of the model in column direction.

Default:
1.0

Suggested values:
0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Restriction:
`ScaleCMin > 0`

**`scaleCMax`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Maximum scale of the model in column direction.

Default:
1.0

Suggested values:
1.0, 1.1, 1.2, 1.3, 1.4, 1.5

Restriction:
`ScaleCMax >= ScaleCMin`

**`minScore`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

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
1.0

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

**`genParamName`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string*)

The general parameter names.

Default:
[]

List of values:
[], "angle_change_restriction", "angle_step", "aniso_scale_change_restriction", "cov_pose_mode", "scale_c_step", "scale_r_step", "subpixel"

**`genParamValue`** (input_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long / double / string)

Values of the general parameters.

Default:
[]

List of values:
[], "covariances", "least_squares", "least_squares_high", "least_squares_very_high", "standard_deviations"

**`pose`** (output_control)  pose(-array) `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

Pose of the object.

**`covPose`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

6 standard deviations or 36 covariances
of the pose parameters.

**`score`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Score of the found instances of the model.

## Result

If the parameters are valid, the operator
`FindPlanarCalibDeformableModel` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`CreatePlanarCalibDeformableModel`,
`ReadDeformableModel`

## Module

Matching
