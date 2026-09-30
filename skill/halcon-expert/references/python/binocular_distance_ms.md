# binocular_distance_ms (Operator)

## Name

`binocular_distance_ms` — Compute the distance values for a rectified stereo image pair using
multi-scanline optimization.

## Signature

`def binocular_distance_ms(image_rect_1: HObject, image_rect_2: HObject, cam_param_rect_1: Sequence[Union[int, float, str]], cam_param_rect_2: Sequence[Union[int, float, str]], rel_pose_rect: Sequence[Union[int, float]], min_disparity: int, max_disparity: int, surface_smoothing: int, edge_smoothing: int, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[str, int]]) -> Tuple[HObject, HObject]`

## Description

`binocular_distance_ms` computes the distance values for a
rectified stereo image pair using multi-scanline optimization. The
operator first calculates the disparities between two rectified
images *`image_rect_1`* and *`image_rect_2`* similar to
[`binocular_disparity_ms`](binocular_disparity_ms.md). The resulting disparity values are
then transformed into distance values of the corresponding 3D world
points to the rectified stereo camera system as in
[`disparity_to_distance`](disparity_to_distance.md). The distances are returned in the
single-channel image *`distance`* in which each gray value
represents the distance of the respective 3D world point to the
stereo camera system.

[`binocular_disparity_ms`](binocular_disparity_ms.md) requires a reference image
*`image_rect_1`* and a search image *`image_rect_2`* which
both must be rectified, i.e., corresponding pixels must have the
same row coordinate. If this assumption is violated, the images can
be rectified by using the operators [`calibrate_cameras`](calibrate_cameras.md),
[`gen_binocular_rectification_map`](gen_binocular_rectification_map.md), and [`map_image`](map_image.md).

For the transformation of the disparity to the distance, the
internal camera parameters of the rectified camera 1
*`cam_param_rect_1`* and of the rectified camera 2
*`cam_param_rect_2`*, as well as the relative pose of the cameras
*`rel_pose_rect`* must be specified. The relative pose defines a
point transformation from the rectified camera system 2 to the
rectified camera system 1. These parameters can be obtained from the
operators [`calibrate_cameras`](calibrate_cameras.md) and
[`gen_binocular_rectification_map`](gen_binocular_rectification_map.md).

A detailed description of the remaining parameters can be found in
the documentation of [`binocular_disparity_ms`](binocular_disparity_ms.md).

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
`binocular_distance_ms` does not support a stereo setup of
mixed type. For stereo setups of mixed type, please use
[`reconstruct_surface_stereo`](reconstruct_surface_stereo.md), in which the reference
coordinate system can be chosen arbitrarily. Alternatively,
[`binocular_disparity_ms`](binocular_disparity_ms.md) and [`disparity_image_to_xyz`](disparity_image_to_xyz.md)
might be used.

Additionally, stereo setups that contain cameras with and without hypercentric
lenses at the same time are not supported.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on internal data level.

## Parameters

**`image_rect_1`** (input_object)  singlechannelimage `→` HObject (byte*) **allowed for compute devices*

Rectified image of camera 1.

**`image_rect_2`** (input_object)  singlechannelimage `→` HObject (byte*) **allowed for compute devices*

Rectified image of camera 2.

**`distance`** (output_object)  singlechannelimage `→` HObject (real)

Distance image.

**`score`** (output_object)  singlechannelimage `→` HObject (real)

Score of the calculated disparity.

**`cam_param_rect_1`** (input_control)  campar `→` Sequence[Union[int, float, str]]

Internal camera parameters of the rectified camera 1.

**`cam_param_rect_2`** (input_control)  campar `→` Sequence[Union[int, float, str]]

Internal camera parameters of the rectified camera 2.

**`rel_pose_rect`** (input_control)  pose `→` Sequence[Union[int, float]]

Point transformation from the rectified camera 2 to
the rectified camera 1.

Number of elements:
7

**`min_disparity`** (input_control)  integer `→` int

Minimum of the expected disparities.

Default:
-30

Value range:
`-32768
≤
min_disparity
≤
32768`

Restriction:
`MinDisparity <= MaxDisparity`

**`max_disparity`** (input_control)  integer `→` int

Maximum of the expected disparities.

Default:
30

Value range:
`-32768
≤
max_disparity
≤
32768`

Restriction:
`MinDisparity <= MaxDisparity`

**`surface_smoothing`** (input_control)  integer `→` int

Smoothing of surfaces.

Default:
50

Suggested values:
20, 50, 100

Restriction:
`SurfaceSmoothing >= 0`

**`edge_smoothing`** (input_control)  integer `→` int

Smoothing of edges.

Default:
50

Suggested values:
20, 50, 100

Restriction:
`EdgeSmoothing >= 0`

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Parameter name(s) for the multi-scanline algorithm.

Default:
[]

List of values:
"consistency_check", "disparity_offset", "num_levels", "similarity_measure", "sub_disparity"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[str, int]]

Parameter value(s) for the multi-scanline algorithm.

Default:
[]

Suggested values:
"census_dense", "census_sparse", "true", "false"

## Result

If the parameter values are correct, `binocular_distance_ms`
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
`binocular_distance_mg`,
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
