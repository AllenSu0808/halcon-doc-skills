# SceneFlowCalib (Operator)

## Name

`SceneFlowCalib` — Compute the calibrated scene flow between two stereo image pairs.

## Signature

`static void HOperatorSet.SceneFlowCalib(HObject imageRect1T1, HObject imageRect2T1, HObject imageRect1T2, HObject imageRect2T2, HObject disparity, HTuple smoothingFlow, HTuple smoothingDisparity, HTuple genParamName, HTuple genParamValue, HTuple camParamRect1, HTuple camParamRect2, HTuple relPoseRect, out HTuple objectModel3D)`

`static HObjectModel3D[] HObjectModel3D.SceneFlowCalib(HImage imageRect1T1, HImage imageRect2T1, HImage imageRect1T2, HImage imageRect2T2, HImage disparity, HTuple smoothingFlow, HTuple smoothingDisparity, HTuple genParamName, HTuple genParamValue, HCamPar camParamRect1, HCamPar camParamRect2, HPose relPoseRect)`

`void HObjectModel3D.SceneFlowCalib(HImage imageRect1T1, HImage imageRect2T1, HImage imageRect1T2, HImage imageRect2T2, HImage disparity, double smoothingFlow, double smoothingDisparity, string genParamName, string genParamValue, HCamPar camParamRect1, HCamPar camParamRect2, HPose relPoseRect)`

`HObjectModel3D[] HCamPar.SceneFlowCalib(HImage imageRect1T1, HImage imageRect2T1, HImage imageRect1T2, HImage imageRect2T2, HImage disparity, HTuple smoothingFlow, HTuple smoothingDisparity, HTuple genParamName, HTuple genParamValue, HCamPar camParamRect2, HPose relPoseRect)`

`HObjectModel3D HCamPar.SceneFlowCalib(HImage imageRect1T1, HImage imageRect2T1, HImage imageRect1T2, HImage imageRect2T2, HImage disparity, double smoothingFlow, double smoothingDisparity, string genParamName, string genParamValue, HCamPar camParamRect2, HPose relPoseRect)`

`HObjectModel3D[] HPose.SceneFlowCalib(HImage imageRect1T1, HImage imageRect2T1, HImage imageRect1T2, HImage imageRect2T2, HImage disparity, HTuple smoothingFlow, HTuple smoothingDisparity, HTuple genParamName, HTuple genParamValue, HCamPar camParamRect1, HCamPar camParamRect2)`

`HObjectModel3D HPose.SceneFlowCalib(HImage imageRect1T1, HImage imageRect2T1, HImage imageRect1T2, HImage imageRect2T2, HImage disparity, double smoothingFlow, double smoothingDisparity, string genParamName, string genParamValue, HCamPar camParamRect1, HCamPar camParamRect2)`

## Description

`SceneFlowCalib` computes the calibrated scene flow between
two consecutive rectified stereo image pairs. The scene flow is the
three-dimensional position and motion of surface points in a dynamic
scene. The movement in the images can be caused by objects that
move in the world or by a movement of the camera (or both) between
the acquisition of the two image pairs.

The scene flow is returned as the 3D object model
*`objectModel3D`*. The 3D object model contains the
coordinates of the reconstructed 3D points. Furthermore, the 3D
flow is encoded in the 3D object model by the attributes
*"&flow_x"*, *"&flow_y"*, and *"&flow_z"*.

The two consecutive stereo image pairs of the image sequence are
passed in *`imageRect1T1`*, *`imageRect2T1`*,
*`imageRect1T2`*, and *`imageRect2T2`*. Each stereo image
pair must be rectified. Note that the images can be rectified by
using the operators [`CalibrateCameras`](calibrate_cameras.md),
[`GenBinocularRectificationMap`](gen_binocular_rectification_map.md), and [`MapImage`](map_image.md).

The camera geometry of the rectified binocular camera system is
specified by its internal camera parameters *`camParamRect1`*
of the rectified camera 1 and *`camParamRect2`* of the
rectified camera 2, and the pose *`relPoseRect`* that defines
the pose of the rectified camera 2 in relation to the rectified
camera 1. These camera parameters can be obtained from the
operators [`CalibrateCameras`](calibrate_cameras.md) and
[`GenBinocularRectificationMap`](gen_binocular_rectification_map.md). The focal length and scale
factor of the rectified camera system 1 and 2 must be equal.

Furthermore, a single-channel *`disparity`* image is required,
which specifies for each pixel (r,c1) of the image
*`imageRect1T1`* a matching pixel (r,c2) of
*`imageRect2T1`* according to the equation c2=c1+d(r,c1),
where d(r,c) is the *`disparity`* at pixel (r,c). The
disparity image can be computed using [`BinocularDisparity`](binocular_disparity.md) or
[`BinocularDisparityMg`](binocular_disparity_mg.md).

To calculate the calibrated scene flow, internally
[`SceneFlowUncalib`](scene_flow_uncalib.md) is first executed. The results are then
converted to 3D points and 3D flow vectors using the stereo camera
geometry parameters described above.

For a description of the remaining parameters of
`SceneFlowCalib`, please refer to
[`SceneFlowUncalib`](scene_flow_uncalib.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`imageRect1T1`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Input image 1 at time $t_{1}$.

**`imageRect2T1`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Input image 2 at time $t_{1}$.

**`imageRect1T2`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Input image 1 at time $t_{2}$.

**`imageRect2T2`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Input image 2 at time $t_{2}$.

**`disparity`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (real)

Disparity between input images 1 and 2 at time
$t_{1}$.

**`smoothingFlow`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Weight of the regularization term relative to
the data term (derivatives of the optical
flow).

Default:
40.0

Suggested values:
10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0

Restriction:
`SmoothingFlow > 0.0`

**`smoothingDisparity`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Weight of the regularization term relative to
the data term (derivatives of the disparity
change).

Default:
40.0

Suggested values:
10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0

Restriction:
`SmoothingDisparity > 0.0`

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Parameter name(s) for the algorithm.

Default:
"default_parameters"

Suggested values:
"default_parameters", "warp_levels", "warp_zoom_factor", "warp_last_level", "outer_iter", "inner_iter", "sor_iter", "omega"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Parameter value(s) for the algorithm.

Default:
"accurate"

Suggested values:
"very_accurate", "accurate", "fast", "very_fast", 0, 1, 2, 3, 4, 5, 6, 0.5, 0.6, 0.7, 0.75, 3, 5, 7, 2, 3, 1.9

**`camParamRect1`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Internal camera parameters of the rectified
camera 1.

**`camParamRect2`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Internal camera parameters of the rectified
camera 2.

**`relPoseRect`** (input_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

Pose of the rectified camera 2 in relation to
the rectified camera 1.

Number of elements:
7

**`objectModel3D`** (output_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D object model.

## Result

If the parameter values are correct, the operator
`SceneFlowCalib` returns the value 2 (
H_MSG_TRUE)
. If the input is
empty (no input images are available) the behavior can be set via
`set_system('no_object_result',<Result>)`. If necessary, an
exception is raised.

## Possible Predecessors

`BinocularDisparity`,
`BinocularDisparityMg`

## Alternatives

`SceneFlowUncalib`,
`OpticalFlowMg`

## References

A. Wedel, C. Rabe, T. Vaudrey, T. Brox, U. Franke and D. Cremers:
“Efficient dense scene flow from sparse or dense stereo data”;
In: Proceedings of the 10th European Conference on Computer Vision:
Part I, pages 739-751. Springer-Verlag, 2008.

## Module

Foundation
