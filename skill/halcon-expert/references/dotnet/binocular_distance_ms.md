# BinocularDistanceMs (Operator)

## Name

`BinocularDistanceMs` — Compute the distance values for a rectified stereo image pair using
multi-scanline optimization.

## Signature

`static void HOperatorSet.BinocularDistanceMs(HObject imageRect1, HObject imageRect2, out HObject distance, out HObject score, HTuple camParamRect1, HTuple camParamRect2, HTuple relPoseRect, HTuple minDisparity, HTuple maxDisparity, HTuple surfaceSmoothing, HTuple edgeSmoothing, HTuple genParamName, HTuple genParamValue)`

`HImage HImage.BinocularDistanceMs(HImage imageRect2, out HImage score, HCamPar camParamRect1, HCamPar camParamRect2, HPose relPoseRect, int minDisparity, int maxDisparity, int surfaceSmoothing, int edgeSmoothing, HTuple genParamName, HTuple genParamValue)`

`HImage HImage.BinocularDistanceMs(HImage imageRect2, out HImage score, HCamPar camParamRect1, HCamPar camParamRect2, HPose relPoseRect, int minDisparity, int maxDisparity, int surfaceSmoothing, int edgeSmoothing, string genParamName, string genParamValue)`

`HImage HCamPar.BinocularDistanceMs(HImage imageRect1, HImage imageRect2, out HImage score, HCamPar camParamRect2, HPose relPoseRect, int minDisparity, int maxDisparity, int surfaceSmoothing, int edgeSmoothing, HTuple genParamName, HTuple genParamValue)`

`HImage HCamPar.BinocularDistanceMs(HImage imageRect1, HImage imageRect2, out HImage score, HCamPar camParamRect2, HPose relPoseRect, int minDisparity, int maxDisparity, int surfaceSmoothing, int edgeSmoothing, string genParamName, string genParamValue)`

`HImage HPose.BinocularDistanceMs(HImage imageRect1, HImage imageRect2, out HImage score, HCamPar camParamRect1, HCamPar camParamRect2, int minDisparity, int maxDisparity, int surfaceSmoothing, int edgeSmoothing, HTuple genParamName, HTuple genParamValue)`

`HImage HPose.BinocularDistanceMs(HImage imageRect1, HImage imageRect2, out HImage score, HCamPar camParamRect1, HCamPar camParamRect2, int minDisparity, int maxDisparity, int surfaceSmoothing, int edgeSmoothing, string genParamName, string genParamValue)`

## Description

`BinocularDistanceMs` computes the distance values for a
rectified stereo image pair using multi-scanline optimization. The
operator first calculates the disparities between two rectified
images *`imageRect1`* and *`imageRect2`* similar to
[`BinocularDisparityMs`](binocular_disparity_ms.md). The resulting disparity values are
then transformed into distance values of the corresponding 3D world
points to the rectified stereo camera system as in
[`DisparityToDistance`](disparity_to_distance.md). The distances are returned in the
single-channel image *`distance`* in which each gray value
represents the distance of the respective 3D world point to the
stereo camera system.

[`BinocularDisparityMs`](binocular_disparity_ms.md) requires a reference image
*`imageRect1`* and a search image *`imageRect2`* which
both must be rectified, i.e., corresponding pixels must have the
same row coordinate. If this assumption is violated, the images can
be rectified by using the operators [`CalibrateCameras`](calibrate_cameras.md),
[`GenBinocularRectificationMap`](gen_binocular_rectification_map.md), and [`MapImage`](map_image.md).

For the transformation of the disparity to the distance, the
internal camera parameters of the rectified camera 1
*`camParamRect1`* and of the rectified camera 2
*`camParamRect2`*, as well as the relative pose of the cameras
*`relPoseRect`* must be specified. The relative pose defines a
point transformation from the rectified camera system 2 to the
rectified camera system 1. These parameters can be obtained from the
operators [`CalibrateCameras`](calibrate_cameras.md) and
[`GenBinocularRectificationMap`](gen_binocular_rectification_map.md).

A detailed description of the remaining parameters can be found in
the documentation of [`BinocularDisparityMs`](binocular_disparity_ms.md).

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
`BinocularDistanceMs` does not support a stereo setup of
mixed type. For stereo setups of mixed type, please use
[`ReconstructSurfaceStereo`](reconstruct_surface_stereo.md), in which the reference
coordinate system can be chosen arbitrarily. Alternatively,
[`BinocularDisparityMs`](binocular_disparity_ms.md) and [`DisparityImageToXyz`](disparity_image_to_xyz.md)
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

**`imageRect1`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte*) **allowed for compute devices*

Rectified image of camera 1.

**`imageRect2`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte*) **allowed for compute devices*

Rectified image of camera 2.

**`distance`** (output_object)  singlechannelimage `→` [HImage](HImage.md) (real)

Distance image.

**`score`** (output_object)  singlechannelimage `→` [HImage](HImage.md) (real)

Score of the calculated disparity.

**`camParamRect1`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Internal camera parameters of the rectified camera 1.

**`camParamRect2`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Internal camera parameters of the rectified camera 2.

**`relPoseRect`** (input_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

Point transformation from the rectified camera 2 to
the rectified camera 1.

Number of elements:
7

**`minDisparity`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Minimum of the expected disparities.

Default:
-30

Value range:
`-32768
≤
minDisparity
≤
32768`

Restriction:
`MinDisparity <= MaxDisparity`

**`maxDisparity`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Maximum of the expected disparities.

Default:
30

Value range:
`-32768
≤
maxDisparity
≤
32768`

Restriction:
`MinDisparity <= MaxDisparity`

**`surfaceSmoothing`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Smoothing of surfaces.

Default:
50

Suggested values:
20, 50, 100

Restriction:
`SurfaceSmoothing >= 0`

**`edgeSmoothing`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Smoothing of edges.

Default:
50

Suggested values:
20, 50, 100

Restriction:
`EdgeSmoothing >= 0`

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Parameter name(s) for the multi-scanline algorithm.

Default:
[]

List of values:
"consistency_check", "disparity_offset", "num_levels", "similarity_measure", "sub_disparity"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / int / long)

Parameter value(s) for the multi-scanline algorithm.

Default:
[]

Suggested values:
"census_dense", "census_sparse", "true", "false"

## Result

If the parameter values are correct, `BinocularDistanceMs`
returns the value 2 (
H_MSG_TRUE)
. If the input is empty (no input images are
available) the behavior can be set via
`set_system('no_object_result',<Result>)`. If necessary, an
exception is raised.

## Possible Predecessors

`MapImage`

## Possible Successors

`Threshold`

## Alternatives

`BinocularDistance`,
`BinocularDistanceMg`,
`BinocularDisparity`,
`BinocularDisparityMg`,
`BinocularDisparityMs`

## See also

`MapImage`,
`GenBinocularRectificationMap`,
`BinocularCalibration`,
`DisparityToDistance`,
`DistanceToDisparity`,
`DisparityImageToXyz`

## Module

3D Metrology
