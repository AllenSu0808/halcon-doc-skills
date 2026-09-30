# GenRadialDistortionMap (Operator)

## Name

`GenRadialDistortionMap` — Generate a projection map that describes the mapping of images corresponding
to a changing radial distortion.

## Signature

`static void HOperatorSet.GenRadialDistortionMap(out HObject map, HTuple camParamIn, HTuple camParamOut, HTuple mapType)`

`void HImage.GenRadialDistortionMap(HCamPar camParamIn, HCamPar camParamOut, string mapType)`

`HImage HCamPar.GenRadialDistortionMap(HCamPar camParamOut, string mapType)`

## Description

`GenRadialDistortionMap` computes the mapping of images
corresponding to a changing radial distortion in accordance to the internal
camera parameters *`camParamIn`* and *`camParamOut`* which can be
obtained, e.g., using the operator [`CalibrateCameras`](calibrate_cameras.md).
*`camParamIn`* and *`camParamOut`* contain the old and the new
camera parameters including the old and the new radial distortion,
respectively (also see [Calibration](toc_calibration.md) for the sequence of
the parameters and the underlying camera model). Each pixel of the
potential output image is transformed into the image plane using
*`camParamOut`* and subsequently projected into a subpixel position
of the potential input image using *`camParamIn`*. Note that
`GenRadialDistortionMap` can only be used with area scan cameras.

The mapping function is stored in the output image *`map`*. The size of
*`map`* is given by the camera parameters *`camParamOut`* and
therefore defines the size of the resulting mapped images using
[`MapImage`](map_image.md). The size of the images to be mapped with [`MapImage`](map_image.md)
is determined by the camera parameters *`camParamIn`*.
*`mapType`* is used to specify the type of the output *`map`*.
If *"nearest_neighbor"* is chosen, *`map`* consists of one image
containing one channel, in which for each pixel of the resulting image the
linearized coordinate of the pixel of the input image is stored that is the
nearest neighbor to the transformed coordinates. If *"bilinear"*
interpolation is chosen, *`map`* consists of one image containing five
channels. In the first channel for each pixel in the resulting image the
linearized coordinates of the pixel in the input image is stored that is in
the upper left position relative to the transformed coordinates.
The four other channels contain the weights of the four neighboring pixels
of the transformed coordinates which are used for the bilinear interpolation,
in the following order:

|  |  |
| --- | --- |
| 2 | 3 |
| 4 | 5 |

The second channel, for example, contains the weights of the pixels that
lie to the upper left relative to the transformed coordinates.
If *"coord_map_sub_pix"* is chosen, *`map`* consists of
one vector field image of the semantic type 'vector_field_absolute', in
which for each pixel of the resulting image the subpixel precise
coordinates in the input image are stored.

If *`camParamOut`* was computed via
[`ChangeRadialDistortionCamPar`](change_radial_distortion_cam_par.md), the mapping describes the effect
of a lens with a modified radial distortion $\kappa$. If
$\kappa=0$, the mapping corresponds to a rectification.
A subsequent pose estimation (determination of the
external camera parameters) is not affected by this operation.

If several images have to be mapped using the same camera parameters,
`GenRadialDistortionMap` in combination with
[`MapImage`](map_image.md) is much more efficient than the operator
[`ChangeRadialDistortionImage`](change_radial_distortion_image.md) because the transformation
must be computed only once.

If you want to re-use the created map in another program, you can save it as
a multi-channel image with the operator [`WriteImage`](write_image.md), using the format
*"tiff"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`map`** (output_object)  (multichannel-)image `→` [HImage](HImage.md) (int4 / int8 / uint2 / vector_field)

Image containing the mapping data.

**`camParamIn`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Old camera parameters.

**`camParamOut`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

New camera parameters.

**`mapType`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of the mapping.

Default:
"bilinear"

List of values:
"bilinear", "coord_map_sub_pix", "nearest_neighbor"

## Result

`GenRadialDistortionMap` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct. If necessary, an exception is raised.

## Possible Predecessors

`ChangeRadialDistortionCamPar`,
`CameraCalibration`,
`HandEyeCalibration`

## Possible Successors

`MapImage`

## Alternatives

`ChangeRadialDistortionImage`

## See also

`ChangeRadialDistortionContoursXld`

## Module

Calibration
