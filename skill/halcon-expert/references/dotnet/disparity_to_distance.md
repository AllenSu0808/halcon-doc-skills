# DisparityToDistance (Operator)

## Name

`DisparityToDistance` — Transform a disparity value into a distance value in a rectified
binocular stereo system.

## Signature

`static void HOperatorSet.DisparityToDistance(HTuple camParamRect1, HTuple camParamRect2, HTuple relPoseRect, HTuple disparity, out HTuple distance)`

`HTuple HCamPar.DisparityToDistance(HCamPar camParamRect2, HPose relPoseRect, HTuple disparity)`

`double HCamPar.DisparityToDistance(HCamPar camParamRect2, HPose relPoseRect, double disparity)`

`HTuple HPose.DisparityToDistance(HCamPar camParamRect1, HCamPar camParamRect2, HTuple disparity)`

`double HPose.DisparityToDistance(HCamPar camParamRect1, HCamPar camParamRect2, double disparity)`

## Description

`DisparityToDistance` transforms a disparity value into a
distance of an object point to the binocular stereo system. The
cameras of this system must be rectified and are defined by the
rectified internal parameters *`camParamRect1`* of camera 1 and
*`camParamRect2`* of camera 2, and the external parameters
*`relPoseRect`*. Latter specifies the relative pose of both
cameras to each other by defining a point transformation from
rectified camera system 2 to rectified camera system 1. These
parameters can be obtained from the operator
[`CalibrateCameras`](calibrate_cameras.md) and
[`GenBinocularRectificationMap`](gen_binocular_rectification_map.md). The disparity value
*`disparity`* is defined by the column difference of the image
coordinates of two corresponding points on an epipolar line
according to the equation $d=c_{2}-c_{1}$(see also [`BinocularDisparity`](binocular_disparity.md)). This value characterises
a set of 3D object points of an equal distance to a plane being
parallel to the rectified image plane of the stereo system.
The distance to the subset plane z=0 which is parallel to
the rectified image plane and contains the optical centers of both
cameras is returned in *`distance`*.

## Attention

If using cameras with telecentric lenses, the *`distance`* is
not defined as the distance of a point to the camera but as the
distance from the point to the plane, defined by the y-axes of both
cameras and their baseline (see
[`GenBinocularRectificationMap`](gen_binocular_rectification_map.md)).

For a stereo setup of mixed type (i.e., for a stereo setup in which
one of the original cameras is a perspective camera and the other
camera is a telecentric camera; see
[`GenBinocularRectificationMap`](gen_binocular_rectification_map.md)), the rectifying plane of
the two cameras is in a position with respect to the object that
would lead to very unintuitive distances. Therefore,
`DisparityToDistance` does not support stereo setups of
mixed type. For stereo setups of mixed type,
[`DisparityToPoint3d`](disparity_to_point_3d.md) should be used instead.

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

**`disparity`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Disparity between the images of the world point.

**`distance`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Distance of a world point to the rectified camera
system.

## Result

`DisparityToDistance` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct. If necessary, an exception is raised.

## Possible Predecessors

`BinocularCalibration`,
`GenBinocularRectificationMap`,
`MapImage`,
`BinocularDisparity`

## Alternatives

`BinocularDistance`

## See also

`DistanceToDisparity`,
`DisparityToPoint3d`

## Module

3D Metrology
