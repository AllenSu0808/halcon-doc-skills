# disparity_to_point_3d (Operator)

## Name

`disparity_to_point_3d` — Transform an image point and its disparity into a 3D point in a
rectified stereo system.

## Signature

`disparity_to_point_3d( : : CamParamRect1, CamParamRect2, RelPoseRect, Row1, Col1, Disparity : X, Y, Z)`

## Description

Given an image point of the rectified camera 1, specified by its
image coordinates (*`Row1`*,*`Col1`*), and its disparity
in a rectified binocular stereo system,
`disparity_to_point_3d` computes the corresponding three
dimensional object point. The disparity value *`Disparity`*
defines the column difference of the image coordinates of two
corresponding features on an epipolar line according to the equation
$d=c_{2}-c_{1}$. The rectified binocular
camera system is specified by its internal camera parameters
*`CamParamRect1`* of camera 1 and *`CamParamRect2`* of
camera 2, and the external parameters *`RelPoseRect`* defining
the pose of the rectified camera 2 in relation to the rectified
camera 1. These camera parameters can be obtained from the
operators [`calibrate_cameras`](calibrate_cameras.md) and
[`gen_binocular_rectification_map`](gen_binocular_rectification_map.md). The 3D point is returned
in Cartesian coordinates (*`X`*,*`Y`*,*`Z`*) of the
rectified camera system 1.

## Attention

Stereo setups that contain cameras with and without hypercentric
lenses at the same time are not supported.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`CamParamRect1`** (input_control)  campar `→`  (real / integer / string)

Rectified internal camera parameters of camera 1.

**`CamParamRect2`** (input_control)  campar `→`  (real / integer / string)

Rectified internal camera parameters of camera 2.

**`RelPoseRect`** (input_control)  pose `→`  (real / integer)

Pose of the rectified camera 2 in relation to the
rectified camera 1.

Number of elements:
7

**`Row1`** (input_control)  number(-array) `→`  (real / integer)

Row coordinate of a point in the rectified image 1.

**`Col1`** (input_control)  number(-array) `→`  (real / integer)

Column coordinate of a point in the rectified image 1.

**`Disparity`** (input_control)  number(-array) `→`  (real / integer)

Disparity of the images of the world point.

**`X`** (output_control)  real(-array) `→`  (real)

X coordinate of the 3D point.

**`Y`** (output_control)  real(-array) `→`  (real)

Y coordinate of the 3D point.

**`Z`** (output_control)  real(-array) `→`  (real)

Z coordinate of the 3D point.

## Result

`disparity_to_point_3d` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct. If necessary, an exception is raised.

## Possible Predecessors

`binocular_calibration`,
`gen_binocular_rectification_map`

## Alternatives

`disparity_image_to_xyz`

## See also

`binocular_disparity`,
`binocular_distance`,
`intersect_lines_of_sight`

## Module

3D Metrology
