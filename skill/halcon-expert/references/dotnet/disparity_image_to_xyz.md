# DisparityImageToXyz (Operator)

## Name

`DisparityImageToXyz` — Transform a disparity image into 3D points in a rectified stereo
system.

## Signature

`static void HOperatorSet.DisparityImageToXyz(HObject disparity, out HObject x, out HObject y, out HObject z, HTuple camParamRect1, HTuple camParamRect2, HTuple relPoseRect)`

`HImage HImage.DisparityImageToXyz(out HImage y, out HImage z, HCamPar camParamRect1, HCamPar camParamRect2, HPose relPoseRect)`

`HImage HCamPar.DisparityImageToXyz(HImage disparity, out HImage y, out HImage z, HCamPar camParamRect2, HPose relPoseRect)`

`HImage HPose.DisparityImageToXyz(HImage disparity, out HImage y, out HImage z, HCamPar camParamRect1, HCamPar camParamRect2)`

## Description

Given the disparity image *`disparity`* of a rectified
binocular stereo system, `DisparityImageToXyz` computes the
corresponding 3D points. Their coordinates relative to the rectified
camera 1 are stored as gray values in the images *`x`*,
*`y`*, and *`z`*, i.e., the pixels at the position
(Row,Column) in *`x`*, *`y`*, and *`z`* contain the
x, y, and z coordinate, respectively, of the pixel (Row,Column) in
the disparity image.

The rectified binocular camera system is specified by its internal
camera parameters *`camParamRect1`* of the rectified camera 1
and *`camParamRect2`* of the rectified camera 2, and the
external parameters *`relPoseRect`*. The latter one is a pose in the
form $\text{ccs}R_1 P_{\mathrm{ccs}}R_2$ ![figure](../assets/959330a2a3b8ae9b.svg), thus it defines the
relative pose of the rectified camera coordinate system 2 (*ccsR2*)
relative to the rectified camera coordinate system 1 (*ccsR1*)
(see [Transformations / Poses](toc_transformations_poses.md) and
`“Solution Guide III-C - 3D Vision”`).
These camera parameters can be obtained from the operators
[`CalibrateCameras`](calibrate_cameras.md) and [`GenBinocularRectificationMap`](gen_binocular_rectification_map.md).

## Attention

Stereo setups that contain cameras with and without hypercentric
lenses at the same time are not supported.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on domain level.

## Parameters

**`disparity`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (real)

Disparity image.

**`x`** (output_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (real)

X coordinates of the points in the rectified camera
system 1.

**`y`** (output_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (real)

Y coordinates of the points in the rectified camera
system 1.

**`z`** (output_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (real)

Z coordinates of the points in the rectified camera
system 1.

**`camParamRect1`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Internal camera parameters of the rectified camera 1.

**`camParamRect2`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Internal camera parameters of the rectified camera 2.

**`relPoseRect`** (input_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

Pose of the rectified camera 2 in relation to the
rectified camera 1.

Number of elements:
7

## Example (HDevelop)

```
disparity_image_to_xyz (ImageDisparity, ImgX, ImgY, ImgZ, RectCamParL, \
                        RectCamParR, RectLPosRectR)
get_region_points (ImageDisparity, Rows, Columns)
get_grayval (ImgX, Rows, Columns, XValues)
get_grayval (ImgY, Rows, Columns, YValues)
get_grayval (ImgZ, Rows, Columns, ZValues)
```

## Result

The operator `DisparityImageToXyz` returns the value 2 (
H_MSG_TRUE)
if the input is not empty. The behavior in case of empty input (no
input image available) is set via the operator
`set_system('no_object_result',<Result>)`. The behavior in
case of empty region (the region is the empty set) is set via
`set_system('empty_region_result',<Result>)`. If necessary an
exception is raised.

## Possible Predecessors

`BinocularDisparity`

## Possible Successors

`Threshold`,
`WriteImage`

## Alternatives

`DisparityToPoint3d`,
`BinocularDistance`

## See also

`BinocularCalibration`,
`GenBinocularRectificationMap`,
`IntersectLinesOfSight`

## Module

3D Metrology
