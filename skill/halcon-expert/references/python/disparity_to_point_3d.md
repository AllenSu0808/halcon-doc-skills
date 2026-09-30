# disparity_to_point_3d (Operator)

## Name

`disparity_to_point_3d` — Transform an image point and its disparity into a 3D point in a
rectified stereo system.

## Signature

`def disparity_to_point_3d(cam_param_rect_1: Sequence[Union[int, float, str]], cam_param_rect_2: Sequence[Union[int, float, str]], rel_pose_rect: Sequence[Union[int, float]], row_1: MaybeSequence[Union[int, float]], col_1: MaybeSequence[Union[int, float]], disparity: MaybeSequence[Union[int, float]]) -> Tuple[Sequence[float], Sequence[float], Sequence[float]]`

`def disparity_to_point_3d_s(cam_param_rect_1: Sequence[Union[int, float, str]], cam_param_rect_2: Sequence[Union[int, float, str]], rel_pose_rect: Sequence[Union[int, float]], row_1: MaybeSequence[Union[int, float]], col_1: MaybeSequence[Union[int, float]], disparity: MaybeSequence[Union[int, float]]) -> Tuple[float, float, float]`

## Description

Given an image point of the rectified camera 1, specified by its
image coordinates (*`row_1`*,*`col_1`*), and its disparity
in a rectified binocular stereo system,
`disparity_to_point_3d` computes the corresponding three
dimensional object point. The disparity value *`disparity`*
defines the column difference of the image coordinates of two
corresponding features on an epipolar line according to the equation
$d=c_{2}-c_{1}$. The rectified binocular
camera system is specified by its internal camera parameters
*`cam_param_rect_1`* of camera 1 and *`cam_param_rect_2`* of
camera 2, and the external parameters *`rel_pose_rect`* defining
the pose of the rectified camera 2 in relation to the rectified
camera 1. These camera parameters can be obtained from the
operators [`calibrate_cameras`](calibrate_cameras.md) and
[`gen_binocular_rectification_map`](gen_binocular_rectification_map.md). The 3D point is returned
in Cartesian coordinates (*`x`*,*`y`*,*`z`*) of the
rectified camera system 1.

## Attention

Stereo setups that contain cameras with and without hypercentric
lenses at the same time are not supported.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`cam_param_rect_1`** (input_control)  campar `→` Sequence[Union[int, float, str]]

Rectified internal camera parameters of camera 1.

**`cam_param_rect_2`** (input_control)  campar `→` Sequence[Union[int, float, str]]

Rectified internal camera parameters of camera 2.

**`rel_pose_rect`** (input_control)  pose `→` Sequence[Union[int, float]]

Pose of the rectified camera 2 in relation to the
rectified camera 1.

Number of elements:
7

**`row_1`** (input_control)  number(-array) `→` MaybeSequence[Union[int, float]]

Row coordinate of a point in the rectified image 1.

**`col_1`** (input_control)  number(-array) `→` MaybeSequence[Union[int, float]]

Column coordinate of a point in the rectified image 1.

**`disparity`** (input_control)  number(-array) `→` MaybeSequence[Union[int, float]]

Disparity of the images of the world point.

**`x`** (output_control)  real(-array) `→` Sequence[float]

X coordinate of the 3D point.

**`y`** (output_control)  real(-array) `→` Sequence[float]

Y coordinate of the 3D point.

**`z`** (output_control)  real(-array) `→` Sequence[float]

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
