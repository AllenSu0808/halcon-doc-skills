# scene_flow_calib (Operator)

## Name

`scene_flow_calib` — Compute the calibrated scene flow between two stereo image pairs.

## Signature

`def scene_flow_calib(image_rect_1t1: HObject, image_rect_2t1: HObject, image_rect_1t2: HObject, image_rect_2t2: HObject, disparity: HObject, smoothing_flow: Union[float, int], smoothing_disparity: Union[float, int], gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]], cam_param_rect_1: Sequence[Union[float, int, str]], cam_param_rect_2: Sequence[Union[float, int, str]], rel_pose_rect: Sequence[Union[float, int]]) -> Sequence[HHandle]`

`def scene_flow_calib_s(image_rect_1t1: HObject, image_rect_2t1: HObject, image_rect_1t2: HObject, image_rect_2t2: HObject, disparity: HObject, smoothing_flow: Union[float, int], smoothing_disparity: Union[float, int], gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]], cam_param_rect_1: Sequence[Union[float, int, str]], cam_param_rect_2: Sequence[Union[float, int, str]], rel_pose_rect: Sequence[Union[float, int]]) -> HHandle`

## Description

`scene_flow_calib` computes the calibrated scene flow between
two consecutive rectified stereo image pairs. The scene flow is the
three-dimensional position and motion of surface points in a dynamic
scene. The movement in the images can be caused by objects that
move in the world or by a movement of the camera (or both) between
the acquisition of the two image pairs.

The scene flow is returned as the 3D object model
*`object_model_3d`*. The 3D object model contains the
coordinates of the reconstructed 3D points. Furthermore, the 3D
flow is encoded in the 3D object model by the attributes
*"&flow_x"*, *"&flow_y"*, and *"&flow_z"*.

The two consecutive stereo image pairs of the image sequence are
passed in *`image_rect_1t1`*, *`image_rect_2t1`*,
*`image_rect_1t2`*, and *`image_rect_2t2`*. Each stereo image
pair must be rectified. Note that the images can be rectified by
using the operators [`calibrate_cameras`](calibrate_cameras.md),
[`gen_binocular_rectification_map`](gen_binocular_rectification_map.md), and [`map_image`](map_image.md).

The camera geometry of the rectified binocular camera system is
specified by its internal camera parameters *`cam_param_rect_1`*
of the rectified camera 1 and *`cam_param_rect_2`* of the
rectified camera 2, and the pose *`rel_pose_rect`* that defines
the pose of the rectified camera 2 in relation to the rectified
camera 1. These camera parameters can be obtained from the
operators [`calibrate_cameras`](calibrate_cameras.md) and
[`gen_binocular_rectification_map`](gen_binocular_rectification_map.md). The focal length and scale
factor of the rectified camera system 1 and 2 must be equal.

Furthermore, a single-channel *`disparity`* image is required,
which specifies for each pixel (r,c1) of the image
*`image_rect_1t1`* a matching pixel (r,c2) of
*`image_rect_2t1`* according to the equation c2=c1+d(r,c1),
where d(r,c) is the *`disparity`* at pixel (r,c). The
disparity image can be computed using [`binocular_disparity`](binocular_disparity.md) or
[`binocular_disparity_mg`](binocular_disparity_mg.md).

To calculate the calibrated scene flow, internally
[`scene_flow_uncalib`](scene_flow_uncalib.md) is first executed. The results are then
converted to 3D points and 3D flow vectors using the stereo camera
geometry parameters described above.

For a description of the remaining parameters of
`scene_flow_calib`, please refer to
[`scene_flow_uncalib`](scene_flow_uncalib.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`image_rect_1t1`** (input_object)  singlechannelimage(-array) `→` HObject (byte / uint2 / real)

Input image 1 at time $t_{1}$.

**`image_rect_2t1`** (input_object)  singlechannelimage(-array) `→` HObject (byte / uint2 / real)

Input image 2 at time $t_{1}$.

**`image_rect_1t2`** (input_object)  singlechannelimage(-array) `→` HObject (byte / uint2 / real)

Input image 1 at time $t_{2}$.

**`image_rect_2t2`** (input_object)  singlechannelimage(-array) `→` HObject (byte / uint2 / real)

Input image 2 at time $t_{2}$.

**`disparity`** (input_object)  singlechannelimage(-array) `→` HObject (real)

Disparity between input images 1 and 2 at time
$t_{1}$.

**`smoothing_flow`** (input_control)  number `→` Union[float, int]

Weight of the regularization term relative to
the data term (derivatives of the optical
flow).

Default:
40.0

Suggested values:
10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0

Restriction:
`SmoothingFlow > 0.0`

**`smoothing_disparity`** (input_control)  number `→` Union[float, int]

Weight of the regularization term relative to
the data term (derivatives of the disparity
change).

Default:
40.0

Suggested values:
10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0

Restriction:
`SmoothingDisparity > 0.0`

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Parameter name(s) for the algorithm.

Default:
"default_parameters"

Suggested values:
"default_parameters", "warp_levels", "warp_zoom_factor", "warp_last_level", "outer_iter", "inner_iter", "sor_iter", "omega"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[int, float, str]]

Parameter value(s) for the algorithm.

Default:
"accurate"

Suggested values:
"very_accurate", "accurate", "fast", "very_fast", 0, 1, 2, 3, 4, 5, 6, 0.5, 0.6, 0.7, 0.75, 3, 5, 7, 2, 3, 1.9

**`cam_param_rect_1`** (input_control)  campar `→` Sequence[Union[float, int, str]]

Internal camera parameters of the rectified
camera 1.

**`cam_param_rect_2`** (input_control)  campar `→` Sequence[Union[float, int, str]]

Internal camera parameters of the rectified
camera 2.

**`rel_pose_rect`** (input_control)  pose `→` Sequence[Union[float, int]]

Pose of the rectified camera 2 in relation to
the rectified camera 1.

Number of elements:
7

**`object_model_3d`** (output_control)  object_model_3d(-array) `→` Sequence[HHandle]

Handle of the 3D object model.

## Result

If the parameter values are correct, the operator
`scene_flow_calib` returns the value 2 (
H_MSG_TRUE)
. If the input is
empty (no input images are available) the behavior can be set via
`set_system('no_object_result',<Result>)`. If necessary, an
exception is raised.

## Possible Predecessors

`binocular_disparity`,
`binocular_disparity_mg`

## Alternatives

`scene_flow_uncalib`,
`optical_flow_mg`

## References

A. Wedel, C. Rabe, T. Vaudrey, T. Brox, U. Franke and D. Cremers:
“Efficient dense scene flow from sparse or dense stereo data”;
In: Proceedings of the 10th European Conference on Computer Vision:
Part I, pages 739-751. Springer-Verlag, 2008.

## Module

Foundation
