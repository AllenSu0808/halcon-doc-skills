# scene_flow_calib (Operator)

## Name

`scene_flow_calib` — Compute the calibrated scene flow between two stereo image pairs.

## Signature

`scene_flow_calib(ImageRect1T1, ImageRect2T1, ImageRect1T2, ImageRect2T2, Disparity : : SmoothingFlow, SmoothingDisparity, GenParamName, GenParamValue, CamParamRect1, CamParamRect2, RelPoseRect : ObjectModel3D)`

## Description

`scene_flow_calib` computes the calibrated scene flow between
two consecutive rectified stereo image pairs. The scene flow is the
three-dimensional position and motion of surface points in a dynamic
scene. The movement in the images can be caused by objects that
move in the world or by a movement of the camera (or both) between
the acquisition of the two image pairs.

The scene flow is returned as the 3D object model
*`ObjectModel3D`*. The 3D object model contains the
coordinates of the reconstructed 3D points. Furthermore, the 3D
flow is encoded in the 3D object model by the attributes
*'&flow_x'*, *'&flow_y'*, and *'&flow_z'*.

The two consecutive stereo image pairs of the image sequence are
passed in *`ImageRect1T1`*, *`ImageRect2T1`*,
*`ImageRect1T2`*, and *`ImageRect2T2`*. Each stereo image
pair must be rectified. Note that the images can be rectified by
using the operators [`calibrate_cameras`](calibrate_cameras.md),
[`gen_binocular_rectification_map`](gen_binocular_rectification_map.md), and [`map_image`](map_image.md).

The camera geometry of the rectified binocular camera system is
specified by its internal camera parameters *`CamParamRect1`*
of the rectified camera 1 and *`CamParamRect2`* of the
rectified camera 2, and the pose *`RelPoseRect`* that defines
the pose of the rectified camera 2 in relation to the rectified
camera 1. These camera parameters can be obtained from the
operators [`calibrate_cameras`](calibrate_cameras.md) and
[`gen_binocular_rectification_map`](gen_binocular_rectification_map.md). The focal length and scale
factor of the rectified camera system 1 and 2 must be equal.

Furthermore, a single-channel *`Disparity`* image is required,
which specifies for each pixel (r,c1) of the image
*`ImageRect1T1`* a matching pixel (r,c2) of
*`ImageRect2T1`* according to the equation c2=c1+d(r,c1),
where d(r,c) is the *`Disparity`* at pixel (r,c). The
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

**`ImageRect1T1`** (input_object)  singlechannelimage(-array) `→` object (byte / uint2 / real)

Input image 1 at time $t_{1}$.

**`ImageRect2T1`** (input_object)  singlechannelimage(-array) `→` object (byte / uint2 / real)

Input image 2 at time $t_{1}$.

**`ImageRect1T2`** (input_object)  singlechannelimage(-array) `→` object (byte / uint2 / real)

Input image 1 at time $t_{2}$.

**`ImageRect2T2`** (input_object)  singlechannelimage(-array) `→` object (byte / uint2 / real)

Input image 2 at time $t_{2}$.

**`Disparity`** (input_object)  singlechannelimage(-array) `→` object (real)

Disparity between input images 1 and 2 at time
$t_{1}$.

**`SmoothingFlow`** (input_control)  number `→`  (real / integer)

Weight of the regularization term relative to
the data term (derivatives of the optical
flow).

Default:
40.0

Suggested values:
10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0

Restriction:
`SmoothingFlow > 0.0`

**`SmoothingDisparity`** (input_control)  number `→`  (real / integer)

Weight of the regularization term relative to
the data term (derivatives of the disparity
change).

Default:
40.0

Suggested values:
10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0

Restriction:
`SmoothingDisparity > 0.0`

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Parameter name(s) for the algorithm.

Default:
'default_parameters'

Suggested values:
'default_parameters', 'warp_levels', 'warp_zoom_factor', 'warp_last_level', 'outer_iter', 'inner_iter', 'sor_iter', 'omega'

**`GenParamValue`** (input_control)  attribute.value(-array) `→`  (string / integer / real)

Parameter value(s) for the algorithm.

Default:
'accurate'

Suggested values:
'very_accurate', 'accurate', 'fast', 'very_fast', 0, 1, 2, 3, 4, 5, 6, 0.5, 0.6, 0.7, 0.75, 3, 5, 7, 2, 3, 1.9

**`CamParamRect1`** (input_control)  campar `→`  (real / integer / string)

Internal camera parameters of the rectified
camera 1.

**`CamParamRect2`** (input_control)  campar `→`  (real / integer / string)

Internal camera parameters of the rectified
camera 2.

**`RelPoseRect`** (input_control)  pose `→`  (real / integer)

Pose of the rectified camera 2 in relation to
the rectified camera 1.

Number of elements:
7

**`ObjectModel3D`** (output_control)  object_model_3d(-array) `→`  (handle)

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
