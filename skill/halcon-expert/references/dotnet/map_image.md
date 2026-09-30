# MapImage (Operator)

## Name

`MapImage` — Apply a general transformation to an image.

## Signature

`static void HOperatorSet.MapImage(HObject image, HObject map, out HObject imageMapped)`

`HImage HImage.MapImage(HImage map)`

## Description

`MapImage` transforms an image *`image`* using an arbitrary
transformation *`map`* which, for example, was previously generated
using [`GenImageToWorldPlaneMap`](gen_image_to_world_plane_map.md) or
[`GenRadialDistortionMap`](gen_radial_distortion_map.md). The multi-channel image *`map`*
must be organized as follows:

The height and the width of *`map`* define the size of the output
image *`imageMapped`*. The number of channels in *`map`* defines
whether no interpolation or bilinear interpolation should be used.
If *`map`* only consists of one channel, no interpolation is applied
during the transformation. This channel contains 'int4' (resp. 'int8' in
HALCON XL if the value range of 'int4' is not sufficient) values that
describe the geometric transformation: For each pixel in the output image
*`imageMapped`* the linearized coordinate of the pixel in the input
image *`image`* from which the gray value should be taken is stored.

If bilinear interpolation between the pixels in the input image should be
applied, *`map`* must consist of 5 channels. The first channel again
consists of an 'int4' resp. 'int8' image and describes the geometric
transformation. The channels 2-5 consist of an 'uint2' image each and
contain the weights [0...1] of the four neighboring pixels that are used
during bilinear interpolation. If the overall brightness of the output image
*`imageMapped`* should not differ from the overall brightness of the
input image *`image`*, the sum of the four unscaled weights must
be 1 for each pixel. The
weights [0...1] are scaled to the range of values of the
'uint2' image and therefore hold integer values from 0 to 65535.

Furthermore, the weights must be chosen in a way that the range of values
of the output image *`imageMapped`* is not exceeded. The geometric
relation between
the four channels 2-5 is illustrated in the following sketch:

|  |  |
| --- | --- |
| 2 | 3 |
| 4 | 5 |

The reference point of the four pixels is the upper left pixel. The
linearized
coordinate of the reference point is stored in the first channel.

It is also possible to use a *`map`* that consists of a vector field
containing absolute subpixel precise row and column coordinates
(i.e., the field must be of the semantic type 'vector_field_absolute'). The
two *`map`* types described above can be converted into this type
using [`ConvertMapType`](convert_map_type.md). This type is the only type supported on
compute devices!

## Attention

The weights must be chosen in a way that the range of values of the output
image *`imageMapped`* is not exceeded.

For runtime reasons during the mapping process, it is not checked whether
the linearized coordinates lie inside the input image. Thus, it must
be ensured by the user that this constraint is fulfilled.
In case interpolation is used, this also applies to the pixels to the right,
below, and below to the right of this coordinate. Otherwise, the
program may crash!

`MapImage` is parallelized automatically if and only if the
specified type for *`map`* is either *"bilinear"*
or *"coord_map_sub_pix"*.

`MapImage` is executed on an OpenCL compute device only if the
input map is of type *"coord_map_sub_pix"* and if the input image
does not exceed the maximum size of image objects of the selected device.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Image to be mapped.

**`map`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (int4 / int8 / uint2 / vector_field*) **allowed for compute devices*

Image containing the mapping data.

**`imageMapped`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Mapped image.

## Result

`MapImage` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct. If necessary, an exception is raised.

## Possible Predecessors

`GenImageToWorldPlaneMap`,
`GenRadialDistortionMap`,
`ConvertMapType`

## See also

`AffineTransImage`,
`RotateImage`

## Module

Foundation
