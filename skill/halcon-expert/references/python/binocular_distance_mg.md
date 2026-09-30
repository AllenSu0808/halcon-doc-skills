# binocular_distance_mg (Operator)

## Name

`binocular_distance_mg` — Compute the distance values for a rectified stereo image pair using
multigrid methods.

## Signature

`def binocular_distance_mg(image_rect_1: HObject, image_rect_2: HObject, cam_param_rect_1: Sequence[Union[int, float, str]], cam_param_rect_2: Sequence[Union[int, float, str]], rel_pose_rect: Sequence[Union[int, float]], gray_constancy: float, gradient_constancy: float, smoothness: float, initial_guess: float, calculate_score: str, mgparam_name: MaybeSequence[str], mgparam_value: MaybeSequence[Union[str, float, int]]) -> Tuple[HObject, HObject]`

## Description

`binocular_distance_mg` computes the distance values for a
rectified stereo image pair using multigrid methods. The operator
first calculates the disparities between two rectified images
*`image_rect_1`* and *`image_rect_2`* similar to
[`binocular_disparity_mg`](binocular_disparity_mg.md). The resulting disparity values are
then transformed into distance values of the corresponding 3D world
points to the rectified stereo camera system as in
[`disparity_to_distance`](disparity_to_distance.md). The distances are returned in the
single-channel image *`distance`* in which each gray value
represents the distance of the respective 3D world point to the
stereo camera system. Different from [`binocular_distance`](binocular_distance.md)
this operator uses a variational approach based on multigrid
methods. This approach returns distance values also for image parts
that contain no texture.

The input images *`image_rect_1`* and *`image_rect_2`* must be
a pair of rectified stereo images, i.e., corresponding points must
have the same row coordinate. In case this assumption is violated
the images can be rectified by using the operators
[`calibrate_cameras`](calibrate_cameras.md), [`gen_binocular_rectification_map`](gen_binocular_rectification_map.md)
and [`map_image`](map_image.md).

For the transformation of the disparity to the distance, the
internal camera parameters of the rectified camera 1
*`cam_param_rect_1`* and of the rectified camera 2
*`cam_param_rect_2`*, as well as the relative pose of the cameras
*`rel_pose_rect`* must be specified. The relative pose defines a
point transformation from the rectified camera system 2 to the
rectified camera system 1. These parameters can be obtained from
the operators [`calibrate_cameras`](calibrate_cameras.md) and
[`gen_binocular_rectification_map`](gen_binocular_rectification_map.md).

A detailed description of the algorithm and of the remaining
parameters can be found in the documentation of
[`binocular_disparity_mg`](binocular_disparity_mg.md).

## Attention

If using cameras with telecentric lenses, the *`distance`* is
not defined as the distance of a point to the camera but as the
distance from the point to the plane, defined by the y-axes of both
cameras and their baseline (see
[`gen_binocular_rectification_map`](gen_binocular_rectification_map.md)).

For a stereo setup of mixed type (i.e., for a stereo setup in which
one of the original cameras is a perspective camera and the other
camera is a telecentric camera; see
[`gen_binocular_rectification_map`](gen_binocular_rectification_map.md)), the rectifying plane of
the two cameras is in a position with respect to the object that
would lead to very unintuitive distances. Therefore,
`binocular_distance_mg` does not support a stereo setup of
mixed type. For stereo setups of mixed type, please use
[`reconstruct_surface_stereo`](reconstruct_surface_stereo.md), in which the reference
coordinate system can be chosen arbitrarily. Alternatively,
[`binocular_disparity_mg`](binocular_disparity_mg.md) and [`disparity_image_to_xyz`](disparity_image_to_xyz.md)
might be used.

Additionally, stereo setups that contain cameras with and without hypercentric
lenses at the same time are not supported.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on internal data level.

## Parameters

**`image_rect_1`** (input_object)  singlechannelimage(-array) `→` HObject (byte / uint2 / real)

Rectified image of camera 1.

**`image_rect_2`** (input_object)  singlechannelimage(-array) `→` HObject (byte / uint2 / real)

Rectified image of camera 2.

**`distance`** (output_object)  singlechannelimage(-array) `→` HObject (real)

Distance image.

**`score`** (output_object)  singlechannelimage(-array) `→` HObject (real)

Score of the calculated disparity if
*`calculate_score`* is set to *"true"*.

**`cam_param_rect_1`** (input_control)  campar `→` Sequence[Union[int, float, str]]

Internal camera parameters of the rectified camera 1.

**`cam_param_rect_2`** (input_control)  campar `→` Sequence[Union[int, float, str]]

Internal camera parameters of the rectified camera 2.

**`rel_pose_rect`** (input_control)  pose `→` Sequence[Union[int, float]]

Point transformation from the rectified camera 2 to
the rectified camera 1.

Number of elements:
7

**`gray_constancy`** (input_control)  real `→` float

Weight of the gray value constancy in the data term.

Default:
1.0

Suggested values:
0.0, 1.0, 2.0, 10.0

Restriction:
`GrayConstancy >= 0.0`

**`gradient_constancy`** (input_control)  real `→` float

Weight of the gradient constancy in the data term.

Default:
30.0

Suggested values:
0.0, 1.0, 5.0, 10.0, 30.0, 50.0, 70.0

Restriction:
`GradientConstancy >= 0.0`

**`smoothness`** (input_control)  real `→` float

Weight of the smoothness term in relation to the
data term.

Default:
5.0

Suggested values:
1.0, 3.0, 5.0, 10.0

Restriction:
`Smoothness > 0.0`

**`initial_guess`** (input_control)  real `→` float

Initial guess of the disparity.

Default:
0.0

Suggested values:
-30.0, -20.0, -10.0, 0.0, 10.0, 20.0, 30.0

**`calculate_score`** (input_control)  string `→` str

Should the quality measure be returned in
*`score`*?

Default:
"false"

Suggested values:
"true", "false"

**`mgparam_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Parameter name(s) for the multigrid algorithm.

Default:
"default_parameters"

List of values:
"default_parameters", "initial_level", "iterations", "mg_cycle_type", "mg_post_relax", "mg_pre_relax", "mg_solver", "pyramid_factor"

**`mgparam_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[str, float, int]]

Parameter value(s) for the multigrid algorithm.

Default:
"fast_accurate"

Suggested values:
"very_accurate", "accurate", "fast_accurate", "fast", "v", "w", "none", "gauss_seidel", "multigrid", "full_multigrid", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, -1, -2, -3, -4, -5

## Result

If the parameter values are correct, `binocular_distance_mg`
returns the value 2 (
H_MSG_TRUE)
. If the input is empty (no input images are
available) the behavior can be set via
`set_system('no_object_result',<Result>)`. If necessary, an
exception is raised.

## Possible Predecessors

`map_image`

## Possible Successors

`threshold`

## Alternatives

`binocular_distance`,
`binocular_distance_ms`,
`binocular_disparity`,
`binocular_disparity_mg`,
`binocular_disparity_ms`

## See also

`map_image`,
`gen_binocular_rectification_map`,
`binocular_calibration`,
`disparity_to_distance`,
`distance_to_disparity`,
`disparity_image_to_xyz`

## Module

3D Metrology
