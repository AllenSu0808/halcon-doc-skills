# gen_radial_distortion_map (Operator)

## Name

`gen_radial_distortion_map` — Generate a projection map that describes the mapping of images corresponding
to a changing radial distortion.

## Signature

`gen_radial_distortion_map( : Map : CamParamIn, CamParamOut, MapType : )`

## Description

`gen_radial_distortion_map` computes the mapping of images
corresponding to a changing radial distortion in accordance to the internal
camera parameters *`CamParamIn`* and *`CamParamOut`* which can be
obtained, e.g., using the operator [`calibrate_cameras`](calibrate_cameras.md).
*`CamParamIn`* and *`CamParamOut`* contain the old and the new
camera parameters including the old and the new radial distortion,
respectively (also see [Calibration](toc_calibration.md) for the sequence of
the parameters and the underlying camera model). Each pixel of the
potential output image is transformed into the image plane using
*`CamParamOut`* and subsequently projected into a subpixel position
of the potential input image using *`CamParamIn`*. Note that
`gen_radial_distortion_map` can only be used with area scan cameras.

The mapping function is stored in the output image *`Map`*. The size of
*`Map`* is given by the camera parameters *`CamParamOut`* and
therefore defines the size of the resulting mapped images using
[`map_image`](map_image.md). The size of the images to be mapped with [`map_image`](map_image.md)
is determined by the camera parameters *`CamParamIn`*.
*`MapType`* is used to specify the type of the output *`Map`*.
If *'nearest_neighbor'* is chosen, *`Map`* consists of one image
containing one channel, in which for each pixel of the resulting image the
linearized coordinate of the pixel of the input image is stored that is the
nearest neighbor to the transformed coordinates. If *'bilinear'*
interpolation is chosen, *`Map`* consists of one image containing five
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
If *'coord_map_sub_pix'* is chosen, *`Map`* consists of
one vector field image of the semantic type 'vector_field_absolute', in
which for each pixel of the resulting image the subpixel precise
coordinates in the input image are stored.

If *`CamParamOut`* was computed via
[`change_radial_distortion_cam_par`](change_radial_distortion_cam_par.md), the mapping describes the effect
of a lens with a modified radial distortion $\kappa$. If
$\kappa=0$, the mapping corresponds to a rectification.
A subsequent pose estimation (determination of the
external camera parameters) is not affected by this operation.

If several images have to be mapped using the same camera parameters,
`gen_radial_distortion_map` in combination with
[`map_image`](map_image.md) is much more efficient than the operator
[`change_radial_distortion_image`](change_radial_distortion_image.md) because the transformation
must be computed only once.

If you want to re-use the created map in another program, you can save it as
a multi-channel image with the operator [`write_image`](write_image.md), using the format
*'tiff'*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Map`** (output_object)  (multichannel-)image `→` object (int4 / int8 / uint2 / vector_field)

Image containing the mapping data.

**`CamParamIn`** (input_control)  campar `→`  (real / integer / string)

Old camera parameters.

**`CamParamOut`** (input_control)  campar `→`  (real / integer / string)

New camera parameters.

**`MapType`** (input_control)  string `→`  (string)

Type of the mapping.

Default:
'bilinear'

List of values:
'bilinear', 'coord_map_sub_pix', 'nearest_neighbor'

## Result

`gen_radial_distortion_map` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct. If necessary, an exception is raised.

## Possible Predecessors

`change_radial_distortion_cam_par`,
`camera_calibration`,
`hand_eye_calibration`

## Possible Successors

`map_image`

## Alternatives

`change_radial_distortion_image`

## See also

`change_radial_distortion_contours_xld`

## Module

Calibration
