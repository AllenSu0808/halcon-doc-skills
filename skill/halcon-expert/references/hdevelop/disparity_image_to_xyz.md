# disparity_image_to_xyz (Operator)

## Name

`disparity_image_to_xyz` — Transform a disparity image into 3D points in a rectified stereo
system.

## Signature

`disparity_image_to_xyz(Disparity : X, Y, Z : CamParamRect1, CamParamRect2, RelPoseRect : )`

## Description

Given the disparity image *`Disparity`* of a rectified
binocular stereo system, `disparity_image_to_xyz` computes the
corresponding 3D points. Their coordinates relative to the rectified
camera 1 are stored as gray values in the images *`X`*,
*`Y`*, and *`Z`*, i.e., the pixels at the position
(Row,Column) in *`X`*, *`Y`*, and *`Z`* contain the
x, y, and z coordinate, respectively, of the pixel (Row,Column) in
the disparity image.

The rectified binocular camera system is specified by its internal
camera parameters *`CamParamRect1`* of the rectified camera 1
and *`CamParamRect2`* of the rectified camera 2, and the
external parameters *`RelPoseRect`*. The latter one is a pose in the
form $\text{ccs}R_1 P_{\mathrm{ccs}}R_2$ ![figure](../assets/959330a2a3b8ae9b.svg), thus it defines the
relative pose of the rectified camera coordinate system 2 (*ccsR2*)
relative to the rectified camera coordinate system 1 (*ccsR1*)
(see [Transformations / Poses](toc_transformations_poses.md) and
`“Solution Guide III-C - 3D Vision”`).
These camera parameters can be obtained from the operators
[`calibrate_cameras`](calibrate_cameras.md) and [`gen_binocular_rectification_map`](gen_binocular_rectification_map.md).

## Attention

Stereo setups that contain cameras with and without hypercentric
lenses at the same time are not supported.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on domain level.

## Parameters

**`Disparity`** (input_object)  singlechannelimage(-array) `→` object (real)

Disparity image.

**`X`** (output_object)  singlechannelimage(-array) `→` object (real)

X coordinates of the points in the rectified camera
system 1.

**`Y`** (output_object)  singlechannelimage(-array) `→` object (real)

Y coordinates of the points in the rectified camera
system 1.

**`Z`** (output_object)  singlechannelimage(-array) `→` object (real)

Z coordinates of the points in the rectified camera
system 1.

**`CamParamRect1`** (input_control)  campar `→`  (real / integer / string)

Internal camera parameters of the rectified camera 1.

**`CamParamRect2`** (input_control)  campar `→`  (real / integer / string)

Internal camera parameters of the rectified camera 2.

**`RelPoseRect`** (input_control)  pose `→`  (real / integer)

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

The operator `disparity_image_to_xyz` returns the value 2 (
H_MSG_TRUE)
if the input is not empty. The behavior in case of empty input (no
input image available) is set via the operator
`set_system('no_object_result',<Result>)`. The behavior in
case of empty region (the region is the empty set) is set via
`set_system('empty_region_result',<Result>)`. If necessary an
exception is raised.

## Possible Predecessors

`binocular_disparity`

## Possible Successors

`threshold`,
`write_image`

## Alternatives

`disparity_to_point_3d`,
`binocular_distance`

## See also

`binocular_calibration`,
`gen_binocular_rectification_map`,
`intersect_lines_of_sight`

## Module

3D Metrology
