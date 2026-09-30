# DistanceToDisparity (Operator)

## Name

`DistanceToDisparity` — Transform a distance value into a disparity in a rectified stereo
system.

## Signature

`static void HOperatorSet.DistanceToDisparity(HTuple camParamRect1, HTuple camParamRect2, HTuple relPoseRect, HTuple distance, out HTuple disparity)`

`HTuple HCamPar.DistanceToDisparity(HCamPar camParamRect2, HPose relPoseRect, HTuple distance)`

`double HCamPar.DistanceToDisparity(HCamPar camParamRect2, HPose relPoseRect, double distance)`

`HTuple HPose.DistanceToDisparity(HCamPar camParamRect1, HCamPar camParamRect2, HTuple distance)`

`double HPose.DistanceToDisparity(HCamPar camParamRect1, HCamPar camParamRect2, double distance)`

## Description

`DistanceToDisparity` transforms a distance of a 3D point to
the binocular stereo system into a disparity value. The cameras of
this system must be rectified and are defined by the rectified
internal parameters *`camParamRect1`* of the camera
1 and *`camParamRect2`* of the camera 2 and the
external parameters *`relPoseRect`*. The latter specifies the
relative pose of both camera systems to each other by defining a
point transformation from the rectified camera system 2 to the
rectified camera system 1. These parameters can be obtained from the
operator [`CalibrateCameras`](calibrate_cameras.md) and
[`GenBinocularRectificationMap`](gen_binocular_rectification_map.md). The distance value is
passed in *`distance`* and the resulting disparity value
*`disparity`* is defined by the column difference of the image
coordinates of two corresponding features on an epipolar line
according to the equation $d=c_{2}-c_{1}$.

## Attention

If using cameras with telecentric lenses, the *`distance`* is
not defined as the distance of a point to the camera but as the
distance from the point to the plane, defined by the y-axes of both
cameras and their baseline (see
[`GenBinocularRectificationMap`](gen_binocular_rectification_map.md)).

For stereo setups of mixed type (i.e., for a stereo setup in which
one of the original cameras is a perspective camera and the other
camera is a telecentric camera; see
[`GenBinocularRectificationMap`](gen_binocular_rectification_map.md)), the rectifying plane of
the two cameras is in a position with respect to the object that
would lead to very unintuitive distances. Therefore,
`DistanceToDisparity` does not support stereo setups of
mixed type.

Additionally, stereo setups that contain cameras with and without hypercentric
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

Point transformation from the rectified camera 2 to
the rectified camera 1.

Number of elements:
7

**`distance`** (input_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Distance of a world point to camera 1.

**`disparity`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Disparity between the images of the point.

## Result

`DistanceToDisparity` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct. If necessary, an exception is raised.

## Possible Predecessors

`BinocularCalibration`,
`GenBinocularRectificationMap`

## Possible Successors

`BinocularDisparity`

## Module

3D Metrology
