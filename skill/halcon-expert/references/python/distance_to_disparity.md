# distance_to_disparity (Operator)

## Name

`distance_to_disparity` — Transform a distance value into a disparity in a rectified stereo
system.

## Signature

`def distance_to_disparity(cam_param_rect_1: Sequence[Union[int, float, str]], cam_param_rect_2: Sequence[Union[int, float, str]], rel_pose_rect: Sequence[Union[int, float]], distance: MaybeSequence[float]) -> Sequence[Union[int, float]]`

`def distance_to_disparity_s(cam_param_rect_1: Sequence[Union[int, float, str]], cam_param_rect_2: Sequence[Union[int, float, str]], rel_pose_rect: Sequence[Union[int, float]], distance: MaybeSequence[float]) -> Union[int, float]`

## Description

`distance_to_disparity` transforms a distance of a 3D point to
the binocular stereo system into a disparity value. The cameras of
this system must be rectified and are defined by the rectified
internal parameters *`cam_param_rect_1`* of the camera
1 and *`cam_param_rect_2`* of the camera 2 and the
external parameters *`rel_pose_rect`*. The latter specifies the
relative pose of both camera systems to each other by defining a
point transformation from the rectified camera system 2 to the
rectified camera system 1. These parameters can be obtained from the
operator [`calibrate_cameras`](calibrate_cameras.md) and
[`gen_binocular_rectification_map`](gen_binocular_rectification_map.md). The distance value is
passed in *`distance`* and the resulting disparity value
*`disparity`* is defined by the column difference of the image
coordinates of two corresponding features on an epipolar line
according to the equation $d=c_{2}-c_{1}$.

## Attention

If using cameras with telecentric lenses, the *`distance`* is
not defined as the distance of a point to the camera but as the
distance from the point to the plane, defined by the y-axes of both
cameras and their baseline (see
[`gen_binocular_rectification_map`](gen_binocular_rectification_map.md)).

For stereo setups of mixed type (i.e., for a stereo setup in which
one of the original cameras is a perspective camera and the other
camera is a telecentric camera; see
[`gen_binocular_rectification_map`](gen_binocular_rectification_map.md)), the rectifying plane of
the two cameras is in a position with respect to the object that
would lead to very unintuitive distances. Therefore,
`distance_to_disparity` does not support stereo setups of
mixed type.

Additionally, stereo setups that contain cameras with and without hypercentric
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

Point transformation from the rectified camera 2 to
the rectified camera 1.

Number of elements:
7

**`distance`** (input_control)  real(-array) `→` MaybeSequence[float]

Distance of a world point to camera 1.

**`disparity`** (output_control)  number(-array) `→` Sequence[Union[int, float]]

Disparity between the images of the point.

## Result

`distance_to_disparity` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct. If necessary, an exception is raised.

## Possible Predecessors

`binocular_calibration`,
`gen_binocular_rectification_map`

## Possible Successors

`binocular_disparity`

## Module

3D Metrology
