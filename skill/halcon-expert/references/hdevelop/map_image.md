# map_image (Operator)

## Name

`map_image` — Apply a general transformation to an image.

## Signature

`map_image(Image, Map : ImageMapped : : )`

## Description

`map_image` transforms an image *`Image`* using an arbitrary
transformation *`Map`* which, for example, was previously generated
using [`gen_image_to_world_plane_map`](gen_image_to_world_plane_map.md) or
[`gen_radial_distortion_map`](gen_radial_distortion_map.md). The multi-channel image *`Map`*
must be organized as follows:

The height and the width of *`Map`* define the size of the output
image *`ImageMapped`*. The number of channels in *`Map`* defines
whether no interpolation or bilinear interpolation should be used.
If *`Map`* only consists of one channel, no interpolation is applied
during the transformation. This channel contains 'int4' (resp. 'int8' in
HALCON XL if the value range of 'int4' is not sufficient) values that
describe the geometric transformation: For each pixel in the output image
*`ImageMapped`* the linearized coordinate of the pixel in the input
image *`Image`* from which the gray value should be taken is stored.

If bilinear interpolation between the pixels in the input image should be
applied, *`Map`* must consist of 5 channels. The first channel again
consists of an 'int4' resp. 'int8' image and describes the geometric
transformation. The channels 2-5 consist of an 'uint2' image each and
contain the weights [0...1] of the four neighboring pixels that are used
during bilinear interpolation. If the overall brightness of the output image
*`ImageMapped`* should not differ from the overall brightness of the
input image *`Image`*, the sum of the four unscaled weights must
be 1 for each pixel. The
weights [0...1] are scaled to the range of values of the
'uint2' image and therefore hold integer values from 0 to 65535.

Furthermore, the weights must be chosen in a way that the range of values
of the output image *`ImageMapped`* is not exceeded. The geometric
relation between
the four channels 2-5 is illustrated in the following sketch:

|  |  |
| --- | --- |
| 2 | 3 |
| 4 | 5 |

The reference point of the four pixels is the upper left pixel. The
linearized
coordinate of the reference point is stored in the first channel.

It is also possible to use a *`Map`* that consists of a vector field
containing absolute subpixel precise row and column coordinates
(i.e., the field must be of the semantic type 'vector_field_absolute'). The
two *`Map`* types described above can be converted into this type
using [`convert_map_type`](convert_map_type.md). This type is the only type supported on
compute devices!

## Attention

The weights must be chosen in a way that the range of values of the output
image *`ImageMapped`* is not exceeded.

For runtime reasons during the mapping process, it is not checked whether
the linearized coordinates lie inside the input image. Thus, it must
be ensured by the user that this constraint is fulfilled.
In case interpolation is used, this also applies to the pixels to the right,
below, and below to the right of this coordinate. Otherwise, the
program may crash!

`map_image` is parallelized automatically if and only if the
specified type for *`Map`* is either *'bilinear'*
or *'coord_map_sub_pix'*.

`map_image` is executed on an OpenCL compute device only if the
input map is of type *'coord_map_sub_pix'* and if the input image
does not exceed the maximum size of image objects of the selected device.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / uint2 / real)

Image to be mapped.

**`Map`** (input_object)  (multichannel-)image `→` object (int4 / int8 / uint2 / vector_field*) **allowed for compute devices*

Image containing the mapping data.

**`ImageMapped`** (output_object)  (multichannel-)image(-array) `→` object (byte / uint2 / real)

Mapped image.

## Result

`map_image` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct. If necessary, an exception is raised.

## Possible Predecessors

`gen_image_to_world_plane_map`,
`gen_radial_distortion_map`,
`convert_map_type`

## See also

`affine_trans_image`,
`rotate_image`

## Module

Foundation
