# DisparityToPoint3d (Operator)

## Name

`DisparityToPoint3d` — Transform an image point and its disparity into a 3D point in a
rectified stereo system.

## Signature

`static void HOperatorSet.DisparityToPoint3d(HTuple camParamRect1, HTuple camParamRect2, HTuple relPoseRect, HTuple row1, HTuple col1, HTuple disparity, out HTuple x, out HTuple y, out HTuple z)`

`void HCamPar.DisparityToPoint3d(HCamPar camParamRect2, HPose relPoseRect, HTuple row1, HTuple col1, HTuple disparity, out HTuple x, out HTuple y, out HTuple z)`

`void HCamPar.DisparityToPoint3d(HCamPar camParamRect2, HPose relPoseRect, double row1, double col1, double disparity, out double x, out double y, out double z)`

`void HPose.DisparityToPoint3d(HCamPar camParamRect1, HCamPar camParamRect2, HTuple row1, HTuple col1, HTuple disparity, out HTuple x, out HTuple y, out HTuple z)`

`void HPose.DisparityToPoint3d(HCamPar camParamRect1, HCamPar camParamRect2, double row1, double col1, double disparity, out double x, out double y, out double z)`

## Description

Given an image point of the rectified camera 1, specified by its
image coordinates (*`row1`*,*`col1`*), and its disparity
in a rectified binocular stereo system,
`DisparityToPoint3d` computes the corresponding three
dimensional object point. The disparity value *`disparity`*
defines the column difference of the image coordinates of two
corresponding features on an epipolar line according to the equation
$d=c_{2}-c_{1}$. The rectified binocular
camera system is specified by its internal camera parameters
*`camParamRect1`* of camera 1 and *`camParamRect2`* of
camera 2, and the external parameters *`relPoseRect`* defining
the pose of the rectified camera 2 in relation to the rectified
camera 1. These camera parameters can be obtained from the
operators [`CalibrateCameras`](calibrate_cameras.md) and
[`GenBinocularRectificationMap`](gen_binocular_rectification_map.md). The 3D point is returned
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

**`camParamRect1`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Rectified internal camera parameters of camera 1.

**`camParamRect2`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Rectified internal camera parameters of camera 2.

**`relPoseRect`** (input_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

Pose of the rectified camera 2 in relation to the
rectified camera 1.

Number of elements:
7

**`row1`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of a point in the rectified image 1.

**`col1`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of a point in the rectified image 1.

**`disparity`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Disparity of the images of the world point.

**`x`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

X coordinate of the 3D point.

**`y`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Y coordinate of the 3D point.

**`z`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Z coordinate of the 3D point.

## Result

`DisparityToPoint3d` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct. If necessary, an exception is raised.

## Possible Predecessors

`BinocularCalibration`,
`GenBinocularRectificationMap`

## Alternatives

`DisparityImageToXyz`

## See also

`BinocularDisparity`,
`BinocularDistance`,
`IntersectLinesOfSight`

## Module

3D Metrology
